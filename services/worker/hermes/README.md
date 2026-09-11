# Hermes pin

- Pin: `HERMES_VERSION_PIN=v0.21.1` (Hermes Agent on droplet-campbell).
- HTTP API: VPS `127.0.0.1:8642` via existing `hermes-gateway`. Local: `scripts/hermes-tunnel.sh` or `-L 127.0.0.1:8642`.
- `:9119` is `hermes serve` login UI (302 `/login`). Do not send `/v1/runs` there.
- Worker probe: HEAD `/health` for reachability; `api_server` only from `/v1/capabilities` 401 or `run_submission`.
- Live `start_run` requires a catalogued `tool=`. Read tools may `accepted` after intercept. Write/external still need receipt/approval.
- Transport key is worker/VPS only (`HERMES_API_SERVER_KEY`). Do not copy `auth.json` or the key into this repo.
