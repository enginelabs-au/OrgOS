---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: software-engineer-subagent
status: executing
revision: 1
created_at: 2026-09-11T04:10:00Z
updated_at: 2026-09-11T04:10:00Z
---

# SE phase-1 plan (T1-2 partial … T1-17 partial)

## Entry

- Canonical plan: `docs/plans/phase_1_foundation_plan.md` §10–§12.
- Decisions: D-07 (`docs/decisions/2026-09-11-tooling-and-pins.md`), D-08 (`docs/decisions/2026-09-11-worker-data-access.md`).
- Predecessor: phase-0 SE/Security/UI/UX/PM/Growth/PL handoffs; root scaffold already present (do not overwrite blindly).
- This file is the role plan for this batch. Final `handoff.md` is owned by the lead.

## Scope (this batch)

| ID | Disposition |
|---|---|
| T1-2 | Extend only: workspace stubs so `npm ci` resolves; Python/infra tree. No desktop/UI port. |
| T1-3 | `@engine-labs/contracts` Zod schemas, events, tests. |
| T1-4 | Compose files, networks, assertions, digests skeleton, backup draft. |
| T1-5…T1-10 | FastAPI + file/sqlite store (Docker not required for pytest). |
| T1-11 | Worker adapter interfaces + fail-closed toolsets. No Hermes client. |
| T1-14 | API seed (founder org/seat, 43 registry rows, empty ledger). |
| T1-15 | UsageEvent table; `ENGINE_USAGE_EMIT` default 0. |
| T1-16 | JSON logs + `trace_id`; `/health` composite. |
| T1-17 | `uv.lock` per service; pytest; `scripts/ci.sh` already exists (extend if needed). |

## Non-goals

Desktop/UI (T1-12/T1-13), Hermes, prices, secrets, protected files, `docs/capabilities.md` status edits, `docs/ui-blueprint` npm, final SE handoff.

## Owned write paths

`packages/contracts/**`, `packages/ui/package.json` (stub), `apps/desktop/package.json` (stub), `services/api/**`, `services/worker/**`, `infra/**`, `scripts/**`, this file, `phase-1-evidence.md`.

## Assumptions

- Unit tests use a sqlite/file store so Docker is not required.
- Persist-before-202 is enforced in application code (D-07 item 10).
- Worker has no `DATABASE_URL` (D-08).
- JWT tests use a clearly fake secret only.

## Validation

`npm test` (contracts), `uv run pytest` in api and worker, `python3 infra/compose/tests/compose_assertions.py`. Loop until they pass. Record commands and exit codes in `phase-1-evidence.md`.
