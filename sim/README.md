
# Simulation Harness (Scaffold)

Status: **Scaffold only** (no locked equations yet)

Purpose:
- Provide a stable, reproducible run loop:
  - load config
  - hash config
  - emit JSONL telemetry events (start/stop + placeholders)
  - produce a `RunResult` bundle

Why JSONL:
- It’s append-only
- It’s easy to stream
- It’s easy to diff and replay

## How to run (v1)
```bash
python -m sim.run sim/example_configs/minimal_run.json

Outputs:

./sim_output/<timestamp>_<hash>/telemetry.jsonl

./sim_output/<timestamp>_<hash>/result.json

Notes

YAML support is intentionally not included yet to avoid silently adding dependencies.
JSON is canonical for now.

Models raise NotImplementedError until implemented under /models.


---

### `sim/io.py`
```python
id="ix_sim_io_v1"
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, Tuple

from models.contracts import Constraints, RunConfig, VehicleParams


class ConfigError(ValueError):
    pass


def _require(d: Dict[str, Any], key: str, typ: Any = None) -> Any:
    if key not in d:
        raise ConfigError(f"Missing required key: {key}")
    v = d[key]
    if typ is not None and not isinstance(v, typ):
        raise ConfigError(f"Key '{key}' must be {typ}, got {type(v)}")
    return v


def load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise ConfigError(f"Failed to parse JSON config '{path}': {e}") from e


def parse_run_config(cfg_dict: Dict[str, Any]) -> RunConfig:
    """
    Parse dict into models.contracts.RunConfig with basic type checks.
    This function enforces "no silent defaults" for critical fields.
    """
    mission = _require(cfg_dict, "mission", str)
    body = _require(cfg_dict, "body", str)

    vehicle_d = _require(cfg_dict, "vehicle", dict)
    mass_kg = float(_require(vehicle_d, "mass_kg"))
    ref_area_m2 = float(_require(vehicle_d, "ref_area_m2"))
    cd = float(_require(vehicle_d, "cd"))
    cl = float(vehicle_d.get("cl", 0.0))

    vehicle = VehicleParams(
        mass_kg=mass_kg,
        ref_area_m2=ref_area_m2,
        cd=cd,
        cl=cl,
    )

    constraints_d = cfg_dict.get("constraints", {}) or {}
    if not isinstance(constraints_d, dict):
        raise ConfigError("constraints must be an object/dict if provided")

    constraints = Constraints(
        q_max_Pa=_to_optional_float(constraints_d.get("q_max_Pa")),
        g_max=_to_optional_float(constraints_d.get("g_max")),
        heating_max_W_m2=_to_optional_float(constraints_d.get("heating_max_W_m2")),
        mass_penalty_max_kg=_to_optional_float(constraints_d.get("mass_penalty_max_kg")),
        stowed_volume_max_m3=_to_optional_float(constraints_d.get("stowed_volume_max_m3")),
        peak_power_max_W=_to_optional_float(constraints_d.get("peak_power_max_W")),
    )

    params = cfg_dict.get("params", {}) or {}
    if not isinstance(params, dict):
        raise ConfigError("params must be an object/dict if provided")

    # Model selectors
    atmosphere_model_id = str(cfg_dict.get("atmosphere_model_id", "UNSET"))
    aero_model_id = str(cfg_dict.get("aero_model_id", "UNSET"))
    thermal_model_id = str(cfg_dict.get("thermal_model_id", "UNSET"))
    gnc_model_id = str(cfg_dict.get("gnc_model_id", "UNSET"))
    prebrake_model_id = str(cfg_dict.get("prebrake_model_id", "NONE"))

    return RunConfig(
        mission=mission,
        body=body,
        vehicle=vehicle,
        constraints=constraints,
        atmosphere_model_id=atmosphere_model_id,
        aero_model_id=aero_model_id,
        thermal_model_id=thermal_model_id,
        gnc_model_id=gnc_model_id,
        prebrake_model_id=prebrake_model_id,
        params=params,
    )


def _to_optional_float(v: Any) -> float | None:
    if v is None:
        return None
    try:
        return float(v)
    except Exception as e:
        raise ConfigError(f"Expected a number or null, got '{v}' ({type(v)}): {e}") from e


def stable_config_hash(cfg: RunConfig) -> str:
    """
    Stable hash of the config JSON dictionary (sorted keys).
    """
    payload = json.dumps(cfg.to_json_dict(), sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:12]


def ensure_output_dir(base_dir: Path, run_id: str) -> Path:
    out_dir = base_dir / run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def write_result_json(out_dir: Path, result_dict: Dict[str, Any]) -> Path:
    p = out_dir / "result.json"
    p.write_text(json.dumps(result_dict, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return p


def write_config_echo(out_dir: Path, cfg: RunConfig) -> Path:
    p = out_dir / "config.echo.json"
    p.write_text(json.dumps(cfg.to_json_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return p


def as_pretty_dict(obj: Any) -> Dict[str, Any]:
    """
    Convert dataclasses to dict safely.
    """
    try:
        return asdict(obj)
    except Exception:
        if isinstance(obj, dict):
            return obj
        raise
