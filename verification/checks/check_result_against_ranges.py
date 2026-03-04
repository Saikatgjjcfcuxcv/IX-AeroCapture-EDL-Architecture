from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def _load_json(p: Path) -> Dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))


def _fail(msg: str) -> int:
    print(f"FAIL: {msg}", file=sys.stderr)
    return 1


def _ok(msg: str) -> None:
    print(f"OK: {msg}")


def _has_key(d: Dict[str, Any], key: str) -> bool:
    return key in d


def _get_nested(d: Dict[str, Any], key: str) -> Any:
    # For now we only support top-level keys.
    return d.get(key)


def check_required_present(result: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if not _has_key(result, k)]
    if missing:
        return f"Missing required keys: {missing}"
    return None


def check_required_substrings(result: Dict[str, Any], req: Dict[str, List[str]]) -> Optional[str]:
    for field, subs in req.items():
        val = _get_nested(result, field)
        if val is None:
            return f"Field '{field}' is missing/null but required_substrings expects content."
        s = str(val)
        for sub in subs:
            if sub not in s:
                return f"Field '{field}' does not contain required substring '{sub}'."
    return None


def check_numeric_ranges(result: Dict[str, Any], ranges: Dict[str, Any]) -> Optional[str]:
    """
    ranges:
      {
        "metric_name": null | {"min": <num>, "max": <num>}
      }
    """
    for metric, spec in ranges.items():
        if spec is None:
            continue  # not checked
        if not isinstance(spec, dict) or "min" not in spec or "max" not in spec:
            return f"Invalid range spec for '{metric}': expected {{'min':..,'max':..}} or null"
        val = result.get(metric, None)
        if val is None:
            return f"Metric '{metric}' is missing/null but range check was specified."
        try:
            x = float(val)
        except Exception:
            return f"Metric '{metric}' value '{val}' is not numeric."
        if x < float(spec["min"]) or x > float(spec["max"]):
            return f"Metric '{metric}' out of range: {x} not in [{spec['min']}, {spec['max']}]"
    return None


def main(argv: List[str]) -> int:
    if len(argv) < 3:
        print("Usage: python check_result_against_ranges.py <result.json> <expected_ranges.json>", file=sys.stderr)
        return 2

    result_p = Path(argv[1]).expanduser().resolve()
    expect_p = Path(argv[2]).expanduser().resolve()

    if not result_p.exists():
        return _fail(f"Result file not found: {result_p}")
    if not expect_p.exists():
        return _fail(f"Expected ranges file not found: {expect_p}")

    result = _load_json(result_p)
    expect = _load_json(expect_p)

    required_present = expect.get("required_present", [])
    required_substrings = expect.get("required_substrings", {})
    numeric_ranges = expect.get("numeric_ranges", {})

    if not isinstance(required_present, list):
        return _fail("expected_ranges.json: required_present must be a list")
    if not isinstance(required_substrings, dict):
        return _fail("expected_ranges.json: required_substrings must be an object/dict")
    if not isinstance(numeric_ranges, dict):
        return _fail("expected_ranges.json: numeric_ranges must be an object/dict")

    err = check_required_present(result, required_present)
    if err:
        return _fail(err)
    _ok("required_present")

    if required_substrings:
        err = check_required_substrings(result, required_substrings)
        if err:
            return _fail(err)
        _ok("required_substrings")

    if numeric_ranges:
        err = check_numeric_ranges(result, numeric_ranges)
        if err:
            return _fail(err)
        _ok("numeric_ranges")

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
