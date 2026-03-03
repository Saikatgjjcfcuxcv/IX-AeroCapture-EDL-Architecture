# Metrics (Working) — IX-AeroCapture-EDL-Architecture

Status: **VOLATILE / IN-PROGRESS**
- This file defines the quantitative metrics we will compute and compare.
- Thresholds are placeholders until you lock the mission focus and mass class.

## 1) Primary performance metrics (core)

### M-01 — Captured Energy / ΔV Equivalent Removed (Atmospheric)
- Purpose: quantify how much orbital/arrival energy the atmosphere removes.
- Units: J (energy) and/or m/s (ΔV-equivalent)
- Notes: if we use ΔV-equivalent, we must state the reference mass model.

### M-02 — Remaining ΔV Required (Post-atmosphere)
- Purpose: how much propulsive trim is still needed after aerocapture/EDL shaping.
- Units: m/s
- Baseline comparison required (see BASELINES.md).

### M-03 — Peak Dynamic Pressure (q_max)
- Purpose: structural + aero load driver.
- Units: Pa
- Notes: used as a hard gate for survivability constraints.

### M-04 — Peak Deceleration (g_max) and Jerk Proxy
- Purpose: crew/cargo survivability and structural shock.
- Units: g (dimensionless), and jerk proxy (m/s^3) or Δg/Δt
- Notes: jerk proxy is allowed early as an estimate if sampling/trajectory resolution is stated.

### M-05 — Peak Heating Proxy (q_dot_max)
- Purpose: TPS sizing proxy.
- Units: W/m^2 (proxy)
- Notes: early versions may use a simplified convective model with explicit assumptions and labeled E-level.

### M-06 — Corridor Robustness / Margin
- Purpose: how “wide” the viable corridor is under dispersions.
- Units: % success over Monte Carlo set; or margin in (altitude, flight-path angle) space
- Notes: v1 may be deterministic; Monte Carlo added later.

## 2) Cost / penalty metrics (mass, volume, power)

### M-07 — Decelerator System Mass
- Units: kg (and % of vehicle mass)
- Notes: must include deployment hardware + TPS + structure + sensors.

### M-08 — Stowed Volume / Packaging Efficiency
- Units: m^3
- Notes: critical for HIAD/ballute packaging constraints.

### M-09 — Peak Electrical Power / Energy Budget
- Units: W (peak), Wh or J (integrated)
- Notes: used to gate optional pre-brake couplers and sensor suites.

## 3) Verification metrics (proof quality)

### M-10 — Telemetry Coverage Score
- Definition: fraction of required signals present at required sampling during each phase.
- Units: 0–1 score
- Notes: ties to “proof layer” goal (replay + audit).

### M-11 — Reproducibility Score
- Definition: can a run be reproduced from a config + version hash + environment metadata?
- Units: pass/fail + notes
- Minimum: config file + code version + deterministic seed (where applicable).

## 4) Metric maturity tags
Each metric output must be tagged per Claims Policy:
- E1 Toy Model
- E2 Implemented Model
- E3 Cross-checked
- E4 Measured
- E5 Flight-relevant

## 5) Placeholder thresholds (to be locked)
These are intentionally blank until mission focus is decided:
- q_max threshold: TBD
- g_max threshold: TBD
- heating proxy threshold: TBD
- allowable mass penalty: TBD
- allowable stowed volume: TBD
- target ΔV reduction vs baseline: TBD
