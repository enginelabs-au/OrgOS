# T3 live tools + live PR evidence

Date: 2026-09-11  
Pin: Hermes `v0.21.1`

## Hermes API

- Listener: VPS `127.0.0.1:8642` on existing `hermes-gateway.service` (no second gateway).
- HEAD `/health` → 405 Allow: GET (reachability).
- GET `/health` still hangs (do not use for readiness).
- Authenticated GET `/v1/capabilities` → 200, `features.run_submission: true`.
- Auth uses Hermes **secret-scoped** `API_SERVER_KEY`, not the systemd EnvironmentFile / yaml extra copy. Worker holds the transport key locally in `~/.config/orgos/hermes-api-server.env` (mode 600, not in git). API/desktop do not read it.

## Probe change

`services/worker/adapter/hermes_client.py`: after HEAD 405/200/204/401, GET `/v1/capabilities`. `api_server` is true only when capabilities is unauthorized or advertises `run_submission`. HEAD 405 alone stays reachability.

`start_run` now sends Hermes-required `input` (from `purpose` when omitted).

Worker tests: **31** passed.

## Live runs

| Path | Idempotency-Key | HTTP | status | run_id |
|---|---|---|---|---|
| VPS `POST /v1/runs` | `orgos-live-read-1` | 202 | started | `run_28816b981114450dab32b3d8857ed5cc` |
| VPS `POST /v1/runs` | `orgos-live-read-3` | 202 | started | `run_0d618f92f48d48d199628c6f5c38af63` |
| Papership `HermesRuntimeAdapter.start_run(tool=memory_read)` | `orgos-worker-live-read-4` | 202 | accepted | `run_ee41560dd3ee46eb9bef3fcd6615e6ba` |

Pre-execution intercept for the worker run: `{tool: memory_read, risk: read}` before POST.

Prompt was read-only: “Reply with the single word pong. Do not use any tools.”

## Live GitHub PR

Product `open_pull(..., dry_run=False)` with App **orgos-dev** / installation perms `contents:write`, `pull_requests:write`, `checks:write`, `statuses:write`, `metadata:read` (non-empty; AUTH-12 would pass).

- PR: https://github.com/enginelabs-au/OrgOS/pull/1
- Number: 1
- Head: `orgos-loop-r1-close`
- Receipt path: `.orgos/loop/orgos-loop-r1-close.md`

Live API `POST /github/pulls` was not used because the running API process has no `SUPABASE_JWT_SECRET` (founder `reauth_at` tokens cannot be minted against it). Same `open_pull` function the route calls.

## Not done here

- Hermes GET `/health` hang (aiohttp).
- Mailbox `EMAIL_*` still on gateway `Environment=` (recommended EnvironmentFile move; values not copied).
- Compose full bring-up + backup drill.
- Apple signing / DigitalOcean / wake-word vendor (D-18).
