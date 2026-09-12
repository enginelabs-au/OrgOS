# Provider-locked names — owner first

The in-repo leftover sweep to **Papership** is in progress. These files still say OrgOS **on purpose** because they must match the live GitHub repo, GitHub App, and Vercel project. I cannot change them in advance without breaking `open_pull` and deploys.

## Change these on the dashboards first

1. GitHub repository `enginelabs-au/OrgOS` → `enginelabs-au/Papership` (Settings → Rename). Confirm the old URL redirects.
2. GitHub App `orgos-dev`: point selected repos at the renamed repo. If you also want the bot slug gone, create a new App (slugs are often immutable) and copy the PEM.
3. Vercel project `orgos` (`prj_S74JOIky7KugVTrfu652NhJYOL8l`): relink Git if needed; rename the project if you want the dashboard slug gone. The `*.vercel.app` host may stay. Never touch `enginelabs-au-site`.
4. Host env: set `GITHUB_APP_REPO=Papership`. Optional: copy `~/.config/orgos/` → `~/.config/papership/` and point `github-app.paths`.

Then tell me. I will update the files below in one follow-up.

## Files I will not change until you finish the list above

| File | Why it stays |
|---|---|
| `.env.example` `GITHUB_APP_REPO=OrgOS` | Default must match the live repo name |
| `scripts/dev-local.sh` `GITHUB_APP_REPO` default and `~/.config/orgos/github-app.paths` | Live App PEM path and repo lookup |
| `services/api/app/github_app.py` | Receipt `.orgos/loop/{slug}.md`, fallback `orgos-loop`, commit `orgos: {title}` |
| `services/api/tests/test_github_app.py` | Asserts the live receipt path and repo |
| `services/api/tests/test_github_pulls.py` | Fixtures `repo: OrgOS`, heads `orgos/…` |
| `services/api/tests/test_loop.py` | Same live contract |

Published receipts already on GitHub under `.orgos/loop/` stay. After the follow-up, new receipts go to `.papership/loop/` and old files remain readable.

## Already changed this pass (safe)

`NOTICE`, grants JSON (dropped `"orgos"` alias), `engine-os-token` → `papership-token` (copy-once), local API store path, Vercel runbook name, unused-folder comments, and the mistaken product-name audit file (removed).

Historical pins stay: `docs/ui-blueprint/blueprint-1/**`, `docs/ui-blueprint/blueprint-2/OrgOS*.html`, unused `apps/web/src/components/cc-org-dash/`, workstream id `20260910-engine-labs-company-os`, decision filenames `2026-09-11-orgos-*.md`. `/cc-org-dash` remains a redirect only.
