from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Optional

from telemetry.env import capture_env_info
from telemetry.hash import sha256_short, stable_json_dumps


@dataclass(frozen=True)
class ProofBundle:
    """
    References artifacts produced by a run directory.
    This does not embed large files; it points to them.
    """
    run_id: str
    config_hash: str

    # Artifact paths (relative or absolute; we store as strings)
    config_echo_path: str
    telemetry_path: str
    result_path: str

    # Environment metadata
    env: Dict[str, object]

    # Bundle hash (hash of this JSON structure)
    bundle_hash: str

    def to_json_dict(self) -> Dict[str, object]:
        return asdict(self)


def build_proof_bundle(run_dir: Path, run_id: str, config_hash: str) -> ProofBundle:
    """
    Build a proof bundle for a run directory.
    Expected files:
      - config.echo.json
      - telemetry.jsonl
      - result.json
    """
    cfg_p = run_dir / "config.echo.json"
    tel_p = run_dir / "telemetry.jsonl"
    res_p = run_dir / "result.json"

    missing = [p.name for p in (cfg_p, tel_p, res_p) if not p.exists()]
    if missing:
        raise FileNotFoundError(f"Cannot build proof bundle; missing: {missing} in {run_dir}")

    env = capture_env_info().to_json_dict()

    provisional = {
        "run_id": run_id,
        "config_hash": config_hash,
        "config_echo_path": cfg_p.as_posix(),
        "telemetry_path": tel_p.as_posix(),
        "result_path": res_p.as_posix(),
        "env": env,
    }
    bundle_hash = sha256_short(provisional, n=16)

    return ProofBundle(
        run_id=run_id,
        config_hash=config_hash,
        config_echo_path=cfg_p.as_posix(),
        telemetry_path=tel_p.as_posix(),
        result_path=res_p.as_posix(),
        env=env,
        bundle_hash=bundle_hash,
    )


def write_proof_bundle_json(run_dir: Path, bundle: ProofBundle) -> Path:
    p = run_dir / "proof_bundle.json"
    p.write_text(json.dumps(bundle.to_json_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return p
