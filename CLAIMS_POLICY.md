# Claims Policy (Reality-Locked)

This repository is intended to be credible to aerospace engineers. That means:
- Claims must be **physically plausible** under known conservation laws.
- Claims must be **traceable** to evidence, models, or measurements.
- Speculation is allowed only when clearly labeled and bounded.

## 1) Allowed claim types
### A) Physics-locked engineering claims (preferred)
Allowed when supported by at least a toy model + stated assumptions:
- Momentum exchange via **propellant**, **atmosphere**, **photons**, or **field-coupled external media** (solar wind / ionosphere / magnetosphere).
- Aerocapture/aerobraking/EDL corridor control concepts.
- Deployables (HIAD/ballute/aeroshell) as drag/BC modifiers.
- Thermal protection and structural survivability strategies.
- Sensing/telemetry architectures and verification logic.

### B) Architecture / interface claims
Allowed when expressed as interfaces and invariants:
- "Module X consumes inputs Y and emits outputs Z"
- "SafetyGate prevents unsafe commands under constraint set C"
- "Telemetry provides reproducible replay and pass/fail evidence"

### C) Research-track hypotheses (allowed, but fenced)
Allowed only when labeled **HYPOTHESIS** and accompanied by:
- What it would take to falsify it (kill criteria),
- Measurement plan,
- Expected magnitude ranges (even if broad),
- And a clear statement that it is NOT flight-validated.

## 2) Disallowed claims (hard ban)
The following are not allowed as dependencies for success in this repo:
- **Reactionless thrust / propellantless net translation** (closed-system momentum violation).
- **Negative-energy requirements** as an assumed engineering input.
- **Warp-drive / inertial-damper functionality** presented as buildable with 2026 hardware.
- "Zero-point extraction" or similar claims as a power source requirement.
- Any claim implying "instant stop" without external momentum exchange.

You may discuss these ideas only as:
- historical context,
- science-fiction inspiration,
- or "why this is not assumed" in a sanity-check section.

## 3) Evidence levels (use these tags)
Use one of these tags in docs and models when making claims:

- **E0 — Concept**: qualitative idea only.
- **E1 — Toy model**: back-of-envelope math, stated assumptions, order-of-magnitude check.
- **E2 — Implemented model**: code runs, units checked, produces repeatable outputs.
- **E3 — Cross-checked**: matches published ranges or independent sim within stated tolerance.
- **E4 — Measured**: hardware or bench test data exists with documented uncertainty.
- **E5 — Flight relevant**: validated against flight or flight-like test conditions.

If a section contains any claim stronger than E1, it must link to:
- the model producing the result, and
- the assumptions used.

## 4) Required hygiene for technical content
- All equations must define variables and units.
- All numeric constants must have provenance (citation or derivation).
- Every plot/table must reference the config that produced it.
- All "wins" must name a baseline for comparison.

## 5) Scope safety note (dual-use)
This repo is about **deceleration architectures** for aerospace vehicles and scientific simulation.
We do not include instructions to build harmful devices or weaponizable systems.
If a concept overlaps with dual-use, it must be treated at **high level** and framed for
safety, validation, and benign applications only.
