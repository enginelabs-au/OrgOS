# Runbook: Papership ↔ Hermes on droplet-campbell

SSH Host `hermes-vps` is in `~/.ssh/config` (user `hermes`, Tailscale). Do not copy keys into this repo.

## What is running on the VPS

- Hermes Agent **v0.21.1** (git `20f7ef4d`)
- `hermes-serve.service`: `hermes serve --host 0.0.0.0 --port 9119` — desktop login UI. `/health` is 302 `/login`.
- `hermes-gateway.service`: messaging + **HTTP API** on `127.0.0.1:8642`. Do not start a second gateway.
- API connect can take >30s on this box. User drop-in sets `HERMES_GATEWAY_PLATFORM_CONNECT_TIMEOUT=120`.
- `GET /health` on `:8642` currently hangs. `HEAD /health` returns 405 Allow: GET (listener is up). Papership probe uses that fallback.

## Local Papership

1. `bash scripts/hermes-tunnel.sh` (background) → `127.0.0.1:9119` (UI) and `127.0.0.1:8642` (API)
2. `bash scripts/dev-local.sh` — defaults `HERMES_API_BASE_URL=http://127.0.0.1:8642`
3. `curl http://127.0.0.1:8000/health` — `hermes` should be `reachable` (not `serve_ui`)

`HERMES_API_SERVER_KEY` is worker/VPS only. The API and desktop must never read it. Model keys stay on the VPS.

## Live path (2026-09-11)

- Worker env file (not in git): `~/.config/papership/hermes-api-server.env` (`HERMES_API_SERVER_KEY`, `HERMES_API_BASE_URL`). Legacy copy may still exist under `~/.config/orgos/`. Never put the key on the API.
- Hermes authenticates with its **secret-scoped** key. Yaml / systemd `API_SERVER_KEY` copies can diverge; do not assume they match.
- After gateway restarts, recreate the local `-L 127.0.0.1:8642` tunnel. Stale forwards hang and can fill the VPS accept queue (GET `/health` hang).
- Do not GET `/health` on `:8642`. HEAD only.
- Live `accepted` is catalogued **read** `tool=` only. Example run `run_ee41560dd3ee46eb9bef3fcd6615e6ba`.

## Still open

- Hermes `GET /health` readiness (hangs)
- Mailbox `EMAIL_*` on gateway `Environment=` (move to EnvironmentFile; do not print values)
