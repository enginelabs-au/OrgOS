# Phase 4 registry evidence (EV-P4-B02, EV-P4-B12, EV-P4-B23, EV-P4-P07)

Lead-owned status changes. Not `working` — no live Gmail/Slack OAuth and no second human user.

| ID | Implementation | Test |
|---|---|---|
| B02.01 | `Store.organisation`, `list_teams`, `create_team`; `GET /organisation`, `GET/POST /teams` | `test_org_and_teams` |
| B12.01 | `services/api/app/connectors.py`; connect/send routes | `test_connection_wizard_and_unknown_provider`, `test_send_needs_approval_and_intersection` |
| B23.01 | guest template + `POST /guests` | `test_guest_refused_until_oq_g2` |
| P07.01 | `record_sync_checkpoint` on GitHub list/sync | `test_github_checkpoint_after_list` |

API suite: 66 passed (2026-09-12).
