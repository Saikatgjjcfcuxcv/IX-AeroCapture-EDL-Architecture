# Verification Pack (Scaffold)

Status: **Scaffold only** (models are not implemented yet)

Purpose:
- Establish a repeatable verification workflow:
  1) Run a case config
  2) Produce a result bundle
  3) Check outputs against expected **ranges** (not exact values early on)
  4) Record pass/fail evidence

Why ranges:
- Early models are proxies (E1/E2)
- Ranges prevent false precision
- Ranges make it easy to tighten targets as fidelity improves (E3+)

Folder layout:
- `verification/cases/` — golden cases
- `verification/checks/` — checkers (range checks, schema checks)
- `verification/run_case.py` — wrapper to run + check a case (lightweight)

Rule:
- A case must include:
  - `config.json`
  - `expected_ranges.json`
  - a short `README.md` explaining assumptions and what “pass” means
