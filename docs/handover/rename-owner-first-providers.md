# Provider-locked names — owner first

GitHub App locked-file follow-up is **done** (2026-09-12). Local `GET /health` returned `"github":"reachable"` for `papership-dev`.

## Still owner / dashboard

1. Vercel project `orgos` (`prj_S74JOIky7KugVTrfu652NhJYOL8l`): relink Git to `enginelabs-au/papership` if needed; rename the project if you want the dashboard slug gone. The `*.vercel.app` host may stay. Never touch `enginelabs-au-site`.

Host / VPS (`hermes-vps` / `droplet-campbell` = `hermes-droplet-campbell`) was inspected 2026-09-12. It runs Hermes only. There is no Papership API, no `GITHUB_APP_*` env, and no `~/.config/orgos` or `~/.config/papership`. `open_pull` runs on the local API (`scripts/dev-local.sh`), already pointed at `papership`. The App PEM was not copied onto Hermes (API-only credential).

## Changed this follow-up

| File | Now |
|---|---|
| `.env.example` | `GITHUB_APP_REPO=papership` |
| `scripts/dev-local.sh` | default repo `papership`; prefer `~/.config/papership/github-app.paths`, else `~/.config/orgos/github-app.paths` once |
| `services/api/app/github_app.py` | new receipts `.papership/loop/{slug}.md`; commit `papership: {title}`; `legacy_file_path` `.orgos/loop/{slug}.md` |
| GitHub / loop tests | repo `papership`, heads `papership/…`, dual-read assertion |

Published receipts already on GitHub under `.orgos/loop/` stay. Do not rewrite git history.

Historical pins stay: `docs/ui-blueprint/blueprint-1/**`, `docs/ui-blueprint/blueprint-2/OrgOS*.html`, unused `apps/web/src/components/cc-org-dash/`, workstream id `20260910-engine-labs-company-os`, decision filenames `2026-09-11-orgos-*.md`. `/cc-org-dash` remains a redirect only.
