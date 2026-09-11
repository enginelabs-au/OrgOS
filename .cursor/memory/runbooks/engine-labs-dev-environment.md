# Runbook: Engine Labs development environment

Recorded 2026-09-11. Names only; no secret values.

## Commands

| Recipe | Command | Notes |
|---|---|---|
| Checks | `bash scripts/ci.sh` | exit 0 on 2026-09-11T04:22Z (js + api 21 + worker 6 + compose assertions) |
| JS only | `bash scripts/ci.sh js` | `npm ci --ignore-scripts` then workspace tests |
| Python only | `bash scripts/ci.sh py` | `uv sync` + pytest in `services/api` and `services/worker` |
| Compose assert | `bash scripts/ci.sh compose` | static YAML; does not start Docker |
| Seed | `python3 scripts/seed.py` | set `ENGINE_STORE_PATH` to a local sqlite path |
| API local | `(cd services/api && uv run uvicorn app.main:app --reload --port 8000)` | uses sqlite store if `DATABASE_URL` unset |
| Desktop vite | `(cd apps/desktop && npm run dev)` | do **not** run `docs/ui-blueprint` |
| Compose up | `just compose-up` or `bash scripts/dev.sh up` | optional; not required for unit CI |

## Versions observed

node v25.6.1, npm 11.9.0, Python 3.11.9, rustc 1.84.1, Docker 27.5.1, uv present, just missing.

## Caveats

- Do not execute `docs/ui-blueprint` (`npm install` / `dev` — LIC-12/13).
- Tokens: vite-dev in-memory; packaged Tauri uses keychain (not verified this pass).
- Usage emit stays off (`ENGINE_USAGE_EMIT=0`) until Security schema review is owner-accepted.
- Worker has no database URL (D-08).
- Keychain entry names (when packaged): `engine-labs.session` (see `apps/desktop/src-tauri`).
