# GitHub App and model key

## What “wired” means

The API reads App ID, installation ID, key path, owner, and repo. It does **not** read a GitHub App OAuth client id or client secret.

- `GET /health` — install ping (`reachable` / `configured` / `missing_key` / `not_configured`).
- `GET /github/pulls` — lists open PRs (authenticated).
- `POST /github/pulls` — founder `org.admin` only. **`dry_run` defaults to true**. Live open requires `dry_run: false` **and** a fresh `reauth_at` claim; then the App creates a branch, writes `.papership/loop/<head>.md`, and opens the PR. Published `.orgos/loop/*.md` files stay readable (`legacy_file_path`).

Hermes side-effecting toolsets stay disabled until T2-1. This client is API-owned, not a Hermes tool.

## Status

- App **papership-dev**, owner `enginelabs-au`, App ID `4918983`, installation `161090499`, `repository_selection=selected`.
- Live local probe 2026-09-12: `GET http://127.0.0.1:8000/health` returned `"github":"reachable"`.
- Key file on disk (never in git): `~/.config/papership/papership-dev.2026-09-12.private-key.pem`.
- IDs/path file (no key material): `~/.config/papership/github-app.paths`.
- OAuth client id / client secret are unused by the current API. If kept, store them in `~/.config/papership/github-app.env` and do not source that file from `scripts/dev-local.sh`.
- `scripts/dev-local.sh` prefers `~/.config/papership/github-app.paths` and falls back to `~/.config/orgos/github-app.paths` once. Default `GITHUB_APP_REPO=papership` (GitHub canonical name).
- VPS `hermes-vps` / `droplet-campbell` (`hermes-droplet-campbell`) has no Papership API and no `GITHUB_APP_*`. Do not copy the App PEM onto that host (API-only).

The Cursor GitHub App is a different install. Leave it alone.
