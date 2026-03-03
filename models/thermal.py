id="ix_models_thermal_v1"
from __future__ import annotations

from .contracts import RunConfig, TrajectoryState, VehicleParams


def heating_proxy_W_m2(
    cfg: RunConfig,
    vehicle: VehicleParams,
    state: TrajectoryState,
    rho_kg_m3: float,
) -> float:
    """
    Return a convective heating proxy (W/m^2).

    STUB — will be implemented as an explicitly labeled proxy (E1/E2).
    Common early forms scale with rho^0.5 * v^3 (but we will not lock anything
    until we define assumptions + validation targets).

    Raises:
      NotImplementedError until implemented.
    """
    raise NotImplementedError("Heating proxy not implemented yet.")
