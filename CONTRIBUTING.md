# Contributing — IX-AeroCapture-EDL-Architecture

This repo is under active development. The README is intentionally frozen until the architecture stabilizes.

## Ground rules (credibility first)
1) Follow `CLAIMS_POLICY.md` and keep content **reality-locked**.
2) If you add or strengthen a claim, tag it with an evidence level:
   - E0 Concept, E1 Toy model, E2 Implemented model, E3 Cross-checked, E4 Measured, E5 Flight relevant
3) Every numeric model must specify:
   - variables + units
   - assumptions
   - provenance for constants (citation or derivation)

## What to edit while README is frozen
Use these files instead:
- `docs/architecture/ARCH_MAP.md` — working architecture map
- `docs/decision-log/DECISION_LOG.md` — what is locked vs proposed
- `docs/requirements/*` — metrics/constraints/baselines (placeholders allowed)
- `/models` — interfaces/contracts first; implementations only after scope decisions are locked
- `/sim`, `/verification`, `/telemetry` — reproducibility + proof tooling

## How to propose a change (best workflow)
1) Open an issue:
   - “Bug” for incorrect logic, broken scripts, bad assumptions
   - “Feature” for new modules or new verification cases
2) Include:
   - the problem statement
   - affected module(s)
   - what changes (assumptions / interfaces / metrics)
   - evidence level target (E1–E5)
3) If it impacts scope or mission focus, add a Decision entry using:
   - `docs/decision-log/DECISION_TEMPLATE.md`

## Pull request checklist (required)
- [ ] Does not modify README (unless explicitly approved)
- [ ] Updates `ARCH_MAP.md` and/or Decision Log if architecture changed
- [ ] Adds/updates verification cases when behavior changes
- [ ] Adds/updates telemetry fields if new signals are introduced
- [ ] Units and assumptions are explicit
- [ ] No reactionless propulsion or exotic-matter dependency claims

## Safety / dual-use note
This repository is for benign aerospace deceleration architectures and simulation.
Do not submit content that provides instructions for harmful device construction.
High-level discussion is acceptable only when framed around safety, validation, and benign use.
