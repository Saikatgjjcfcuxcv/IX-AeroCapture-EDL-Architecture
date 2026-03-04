from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


REQUIRED_FIELDS = ["t", "event", "run_id", "config_hash"]


def _fail(msg: str) -> int:
    print(f"FAIL: {msg}", file=sys.stderr)
    return 1


def _ok(msg: str) -> None:
    print(f"OK: {msg}")


def validate_jsonl(path: Path) -> Optional[str]:
    """
    Basic validation: each line is JSON object containing required fields.
    Dependency-light on purpose (no jsonschema dependency).
    """
    if not path.exists():
        return f"File not found: {path}"

    line_no = 0
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line_no += 1
            s = line.strip()
            if not s:
                continue
            try:
                obj = json.loads(s)
            except Exception as e:
                return f"Line {line_no}: invalid JSON: {e}"
            if not isinstance(obj, dict):
                return f"Line {line_no}: expected object, got {type(obj)}"
            for k in REQUIRED_FIELDS:
                if k not in obj:
                    return f"Line {line_no}: missing required field '{k}'"
    return None


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("Usage: python -m telemetry.validate_basic <telemetry.jsonl>", file=sys.stderr)
        return 2
    p = Path(argv[1]).expanduser().resolve()
    err = validate_jsonl(p)
    if err:
        return _fail(err)
    _ok("telemetry.jsonl basic validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
