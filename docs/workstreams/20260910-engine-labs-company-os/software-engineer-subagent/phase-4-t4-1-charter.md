# Software Engineer charter — Phase 4 T4-1

Task: `20260910-engine-labs-company-os`  
Risk: Tier 3  
Mode: write  
Predecessor: T4-0 complete (R1 APPROVE + live read `accepted` + PR #1)

## Objective

Persist `founder` / `project_lead` / `operator` seat templates. `POST /members/invites` creates a principal + subset grants and does not send mail. No live second-seat activation (OQ-G2 is T4-2).

## Allowed paths

- `services/api/app/store.py`
- `services/api/app/main.py`
- `services/api/tests/test_seats.py` (new)
- this charter / a short handoff

## Non-goals

No mail. No Gmail/Slack. No prices. No marketing site. No Hermes write `accepted`.
