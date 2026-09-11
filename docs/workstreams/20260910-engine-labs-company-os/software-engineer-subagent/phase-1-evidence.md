---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: software-engineer-subagent
revision: 1
---

# SE phase-1 evidence (T1-2 partial … T1-17 partial)

Environment: macOS darwin 25.6.0, node v25.6.1, Python 3.11.9, uv present. Docker not required for these checks. UTC timestamps below.

## Commands and exit codes

| When (UTC) | Command | Exit | Notes |
|---|---|---|---|
| 2026-09-11T04:16:00Z | `python3 infra/compose/tests/compose_assertions.py` | 0 | published ports / worker not on `data` |
| 2026-09-11T04:16:00Z | `cd services/api && uv lock && uv sync` | 0 | lockfile written |
| 2026-09-11T04:16:00Z | `cd services/worker && uv lock && uv sync` | 0 | lockfile written |
| 2026-09-11T04:17:00Z | `cd services/worker && uv run pytest -q` | 0 | 6 passed |
| 2026-09-11T04:18:00Z | `npm install --ignore-scripts --workspace=@engine-labs/contracts && npm test --workspace=@engine-labs/contracts` | 0 | 13 passed, 0 failed |
| 2026-09-11T04:19:00Z | `cd services/api && uv run pytest -q` | 0 | 21 passed, 1 warning (Starlette BlockingPortal deprecation) |
| 2026-09-11T04:20:22Z | `cd services/worker && uv run pytest -q` | 0 | 6 passed (reconfirm) |
| 2026-09-11T04:20:30Z | `python3 infra/compose/tests/compose_assertions.py` | 0 | reconfirm |
| 2026-09-11T04:20:30Z | `python3 scripts/seed.py` with `ENGINE_STORE_PATH=/tmp/engine-labs-seed-test.sqlite` | 0 | founder org/seat + 43 registry rows |

`just` was not required. `scripts/ci.sh` `js`/`py`/`compose` paths match the commands above. Full `scripts/ci.sh` / `npm test` at repo root also runs `@engine-labs/desktop` and `@engine-labs/ui` workspaces owned by T1-12/T1-13 (not this batch).

## Requirement coverage

| ID | Evidence state | Result |
|---|---|---|
| T1-3 contracts | VERIFIED | Zod schemas; 43 ids match `docs/capabilities.md`; prohibited UsageEvent fails; emit flag note default 0 |
| T1-4 compose | VERIFIED (static) | networks `edge`/`app`/`data`/`worker`; only proxy publishes a host port; worker networks `['worker']` |
| T1-5 API core | VERIFIED | sqlite/file store; migration SQL has NOSUPERUSER/NOBYPASSRLS/INSERT-only audit/`SET LOCAL`; env allowlist |
| T1-6 identity | PARTIAL | JWT iss/aud/secret + grant_version + founder seat seeded; GoTrue/strong-factor live path not run |
| T1-7 grants | VERIFIED | agent cannot hold `approval.*`; self-approval refused; unprivileged 403 on five surfaces + memory; entitlement ≠ permission; signed URL TTL 300s |
| T1-8 registry | VERIFIED | `GET /registry` 43 rows; `hermes_side_effecting_tools: unavailable` |
| T1-9 ledger | VERIFIED | priority → plan → items → assignments → dependencies → source references |
| T1-10 jobs | VERIFIED | persist-before-202 (crash hook + reopen); SSE resume `last_event_id`; cancel vs disconnect; nine PRD-E.2 fields; `model_configuration=none`; idempotent receipts |
| T1-11 worker | VERIFIED | default starts; enabled+no artefact refuse; hash mismatch refuse; no Hermes client/network; no `DATABASE_URL` in allowlist |
| T1-14 seed | VERIFIED | `scripts/seed.py` / `python -m app.seed` |
| T1-15 usage | VERIFIED | flag off emits zero; prohibited fields 422 |
| T1-16 health/logs | VERIFIED | `/health` db/dbos/worker_config + hermes/github `not_configured`; `x-trace-id` on responses |
| T1-17 lockfiles | VERIFIED | `services/api/uv.lock`, `services/worker/uv.lock`; pytest as above. `npm audit` optional in `scripts/ci.sh` |

## Limitations

- Compose stack was not started; no external port scan / `docker compose config` (unit tests do not need Docker).
- DBOS Python package is not imported; persist-before-202 is enforced in application code against the sqlite file store (D-07 item 10).
- Usage emit stays off pending Security schema review (F-G1).
- Final role `handoff.md` not written (lead-owned).
- `docs/capabilities.md` statuses unchanged.
- Desktop/UI implementation is out of this batch.
