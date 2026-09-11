# D-16 — Interception mechanism (T2-1)

Date: 2026-09-11  
Status: accepted (spike). Security re-review still required before `interception_verified: true`.

## Decision

Release 1 uses **restricted Hermes toolsets + the Papership API action service** (SP-4).

Side-effecting toolsets (`terminal`, `browser`, `github`, `files_write`, `email_send`) stay disabled. Git/worktree effects go through the Papership API (already: `POST /github/pulls` dry-run default). The worker refuses a tool call at the policy layer (`PolicyError`), not via the model.

## Why not the approval hook (SP-2)

The pinned install is `hermes serve` on port 9119 (login UI). The documented HTTP API server (`GET /v1/capabilities`, `POST /v1/runs/{id}/approval`) is **not listening**. A live pause-before-tool transcript cannot be produced without enabling a toolset, which AUTH-25 forbids.

`resolve_owned_approval` is implemented so that if an API server is added later, the adapter still persists the Papership approval first.

## Follow-up

- Do not set `interception_verified` until Security PASS on this spike.
- T2-2 may talk to an API server **if** one is deployed; until then, adapter stays health/inventory only and `start_run` refuse-closed.
