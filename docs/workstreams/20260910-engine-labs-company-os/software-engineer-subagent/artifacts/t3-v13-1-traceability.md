# V13-1 traceability (Phase 3 close)

Date: 2026-09-11  
HEAD: `7d1af364c8448020e57540dccb1bef73e4f8257c` (working tree dirty — Phase 3 closure edits)

R1 `configured` rows only. `planned` rows stay planned. No `working` row.

| capability_id | Requirement | Code path | Test / live | Status |
|---|---|---|---|---|
| B06.01 | Plans + dependencies | `services/api/app/store.py` plans/dependencies; `POST /plans` | `test_ledger.py` | configured |
| B07.01 | Priorities + assignments | `store.create_priority`, `POST /assignments` | `test_ledger.py` | configured |
| P02.01 | Founder identity | seeded `principal-founder`; JWT iss/aud | `test_authz.py` | configured |
| P03.01 | Hey Engine persist | `POST /assistant/sessions/{id}/turns`; desktop `AssistantPanel` | `test_assistant.py`; no streamed Hermes | configured |
| P05.01 | Durable jobs | `POST /jobs`, persist-before-202, cancel | `test_jobs.py` | configured |
| P06.01 | Registry + health | `GET /registry`, `GET /health` | `test_registry.py`, `test_health.py`; live hermes/github reachable | configured |
| P10.01 | Server-side grants | `has_grant`, `/grants/revoke` | `test_authz.py` (incl. V14-3) | configured |
| P11.01 | Retention disclosure | Settings copy | UI only; no expiry job | configured |
| P13.01 | Audit + receipts | `append_audit`, `add_receipt`; AUTH-10 `auth10` on worker persist | `test_jobs.py`, `test_interception.py` | configured |
| P15.01 | Desktop/web shell | `apps/desktop`, `apps/web` `/cc-org-dash` | desktop `tests/*.test.mjs`; web Home snapshot 2026-09-11 | configured |
| P17.01 | Health | `/health` composite; HEAD-first Hermes probe | live `hermes=reachable`, `github=reachable`, `usage_emit=false` | configured |
| P18.01 | Usage schema | `ENGINE_USAGE_EMIT` default 0 | emit off; first-baseline not accepted | configured |
| B08.01 | 11-stage loop | `loop.py`, `test_r1_acc6_walks_all_loop_stages` | PARTIAL — dry-run only; keep `planned` | planned |

Deferred connectors (email, chat, guests, extra seats) remain `planned`. Live Hermes tool `accepted` is not a capability status change.
