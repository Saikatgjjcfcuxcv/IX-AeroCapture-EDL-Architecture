# Case 000 — Minimal Scaffold Run

This is a **scaffold-only** verification case.
It exists to prove the run harness + telemetry + result bundle wiring works.

## Expected behavior
- The sim run completes
- A result.json is written
- Telemetry.jsonl exists
- Since physics models are not implemented, most metrics are expected to be null/missing

## Pass/Fail
PASS if:
- `telemetry_path` exists in the result
- `notes` contains scaffold marker text
FAIL otherwise
