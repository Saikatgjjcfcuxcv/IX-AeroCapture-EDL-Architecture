# Decision Log — IX-AeroCapture-EDL-Architecture

Purpose: lock decisions explicitly, prevent README churn, and keep scope credible.

Legend:
- **Proposed** → under discussion
- **Locked** → accepted; change requires a new decision entry
- **Deprecated** → previously used; no longer active

---

## Locked decisions (current)
| ID | Date | Status | Decision | Notes |
|---:|:----:|:------:|----------|------|
| D-0001 | 2026-03-03 | Locked | Repo name is `IX-AeroCapture-EDL-Architecture` | Active development |
| D-0002 | 2026-03-03 | Locked | License is Apache-2.0 | Set and forget |
| D-0003 | 2026-03-03 | Locked | README is intentionally **frozen** until architecture stabilizes | Use ARCH_MAP + this log |

---

## Proposed decisions (to be filled)
| ID | Date | Status | Decision | Notes |
|---:|:----:|:------:|----------|------|
| D-0004 | TBD | Proposed | Primary mission focus: (aerocapture-to-orbit) vs (landing EDL) vs (both) | impacts modeling |
| D-0005 | TBD | Proposed | Supported vehicle mass classes (1t/10t/100t) | affects scaling |
| D-0006 | TBD | Proposed | Decelerator family selection (rigid vs HIAD vs ballute) | affects TPS/structure |
| D-0007 | TBD | Proposed | Terminal trim method (propulsive vs hybrid) | affects requirements |
| D-0008 | TBD | Proposed | Optional pre-brake module scope (in-repo vs separate) | research vs core |

---

## How to add a decision
1) Copy `/docs/decision-log/DECISION_TEMPLATE.md`
2) Fill it out
3) Add it under `/docs/decision-log/decisions/D-XXXX.md` (folder added later)
4) Update the tables above
