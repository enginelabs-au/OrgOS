# SP-1 inventory — Hermes pin v0.21.1

Date: 2026-09-11  
Pin: `HERMES_VERSION_PIN=v0.21.1`  
Live hop: SSH tunnel `127.0.0.1:9119` → VPS `hermes serve --host 0.0.0.0 --port 9119`

## Live process

| Check | Result |
|---|---|
| `GET /health` | HTTP 302 → `/login?next=/health` (uvicorn). Process up; this is the **desktop/serve UI**, not the HTTP API server. |
| `GET /v1/capabilities` | HTTP 302 → `/login` — no JSON capabilities payload. |
| `GET /v1/toolsets` | HTTP 302 → `/login` — no tool list. |
| VPS listen | `0.0.0.0:9119` `hermes`; `100.126.6.56:9900` messaging gateway. **No** API-server port (no `:8642` / dedicated `/v1` listener). |

Bearer `HERMES_API_SERVER_KEY` was **not** sent (AUTH-22: worker/API must not treat that key as per-tool auth; inventory does not require copying `auth.json`).

## Documented API-server surface (not running on this pin)

From Hermes Agent docs (`GET /v1/capabilities` contract): `run_submission`, `run_status`, `run_events_sse`, `run_stop`, `run_approval` / `run_approval_response`, `tool_progress_events`, `approval_events`, sessions, `GET /v1/toolsets`, `GET /v1/skills`.  
`POST /v1/runs/{id}/approval` exists **on the API server**. It is not reachable on `hermes serve` at 9119.

## Side-effecting tools (R1 classification)

These map to `services/worker/config/toolsets.yaml` and stay **disabled**:

| Toolset | Example tool names | Effect |
|---|---|---|
| `terminal` | terminal, shell, exec | host command / egress |
| `browser` | browser, browser_navigate, web_fetch | network + page side effects |
| `github` | github, git | repo mutation |
| `files_write` | files_write, write_file | filesystem write |
| `email_send` | email_send, send_email | outbound message |

Read-only helpers (e.g. `memory_read`) are not in this list.

## Verdict

SP-1 **PASS with limitation**: inventory of the **deployed** pin is `hermes serve` UI. The documented approval hook is on an API server that is **not listening**. Side-effecting toolsets remain the five named rows above, all `enabled: false`.
