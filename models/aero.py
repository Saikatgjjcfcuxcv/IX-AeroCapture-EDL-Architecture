id="ix_models_aero_v1"
from __future__ import annotations

from .contracts import RunConfig, TrajectoryState, VehicleParams


def compute_dynamic_pressure_Pa(rho_kg_m3: float, v_m_s: float) -> float:
    """
    q = 0.5 * rho * v^2
    """
    return 0.5 * rho_kg_m3 * (v_m_s ** 2)


def step_aero_proxy(
    cfg: RunConfig,
    vehicle: VehicleParams,
    state: TrajectoryState,
    rho_kg_m3: float,
    dt_s: float,
) -> TrajectoryState:
    """
    Advance a minimal trajectory state using an aero proxy.

    STUB — no dynamics implemented yet.
    This will eventually:
      - compute drag/lift acceleration proxies
      - update v, gamma, altitude
      - enforce constraints via GNC SafetyGate (separate module)

    Raises:
      NotImplementedError until implemented.
    """
    raise NotImplementedError("Aero proxy not implemented yet.")
