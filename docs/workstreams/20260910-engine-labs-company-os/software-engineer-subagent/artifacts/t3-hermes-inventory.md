# Hermes HTTP API inventory (T3-2 / F-T33-SEC-06)

Date: 2026-09-11  
Pin: `v0.21.1` / `infra/digests.lock` git `20f7ef4d`  
Local tunnel: `127.0.0.1:8642` → VPS gateway. `127.0.0.1:9119` → `hermes serve` login UI.

| Probe | Result | Meaning |
|---|---|---|
| HEAD `http://127.0.0.1:8642/health` | 405 Allow: GET | aiohttp API, not login |
| GET `http://127.0.0.1:8642/health` | hangs (>2s) | readiness still unusable; can fill the accept queue |
| GET `http://127.0.0.1:8642/v1/capabilities` (no key) | JSON `gateway_auth_error` / `API_SERVER_KEY` | `/v1/capabilities` exists; proves `api_server` |
| Authenticated GET `/v1/capabilities` | 200, `run_submission: true` | secret-scoped transport key (worker/VPS only) |
| GET `http://127.0.0.1:9119/health` | 302 `/login` | serve UI |
| Papership worker `probe_hermes` | `reachable` + `api_server` from capabilities 401/`run_submission` | never from HEAD 405 alone |

Live `POST /v1/runs` accepted (catalogued read `tool=memory_read`). See `t3-live-tools-evidence.md`.
