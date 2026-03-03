id="ix_models_atmosphere_v1"
from __future__ import annotations

from .contracts import AtmosphereProfile, RunConfig


def get_atmosphere_profile(cfg: RunConfig) -> AtmosphereProfile:
    """
    Return an AtmosphereProfile selected by cfg.atmosphere_model_id.

    This is a STUB. Implementations will be added after we lock:
      - target body (Mars vs Earth)
      - required altitude range
      - fidelity level (E1/E2/E3...)

    Expected behavior (later):
      - Deterministic profile for a given config + seed (if any)
      - Explicit units and provenance

    Raises:
      NotImplementedError until implemented.
    """
    raise NotImplementedError("Atmosphere model not implemented yet.")
