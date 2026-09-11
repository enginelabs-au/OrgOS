# Software Engineer handoff — Phase 4 T4-1

Verdict: **PASS** (bounded)

- Templates: `founder`, `project_lead`, `operator` (`SEAT_TEMPLATES` in `store.py`).
- `GET /seats/templates` lists them.
- `POST /members/invites` (org.admin only) creates principal + seat + `template ∩ actor grants`. `mail: not_sent`. Cannot invite `founder`.
- Tests: `tests/test_seats.py` (5) + full API suite.

OQ-G2 live-seat notice is T4-2. No mail sent.
