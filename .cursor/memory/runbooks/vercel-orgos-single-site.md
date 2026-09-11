# Runbook: single Vercel project (`orgos`)

## Intent

Keep one Vercel project, `orgos` (`prj_S74JOIky7KugVTrfu652NhJYOL8l`), as the public website for Engine Labs and OrgOS. The site is `apps/web`. Root `vercel.json` builds `@engine-labs/web`.

## What this machine can do

- MCP `list_projects` / `get_project` on team `team_OE661S5TJD0ffByuXVygWH67`.
- Git push to `enginelabs-au/OrgOS` so the linked `orgos` project rebuilds.

## What is blocked here

- Vercel CLI has no credentials (`VERCEL_TOKEN` unset; `vercel whoami` fails).
- MCP has no delete-project tool.
- Docker is unavailable on this workstation, so live Compose is not part of this run.

## Owner actions to finish project removal

1. `npx vercel login` (or set `VERCEL_TOKEN` in the local shell, never in git).
2. Confirm the three extras to delete. Engine Labs–related candidates, **not** Shuffle / Distroclub / z0rb:
   - `enginelabs-au-site` (`prj_qiAcdSA7jgAXrhl7ObzREeetsr5u`) — holds `enginelabs.com.au` / `www.enginelabs.com.au`. Move those domains to `orgos` **before** delete.
   - `hermes-playground` (`prj_vznyVtdP6xrFP3Ey6WL1qCX41un5`) — only if you intend to retire that playground.
   - Third project: name it explicitly. This account has other products (`jinglelabs`, `secretenv-web`, `yournewhandle`, `ginzcoin-web`). Those are not OrgOS entry points and were not deleted.
3. After domains point at `orgos` and a READY deployment exists:
   `npx vercel project rm enginelabs-au-site --yes`
   (repeat for any confirmed extra).
4. Optional: point `enginelabs-au.github.io` at the same `orgos` URL.

## Validation

- `orgos` production deployment READY.
- `https://orgos-cam-douglas-projects.vercel.app` serves the Engine Labs landing (`apps/web`).
- Apex `enginelabs.com.au` serves that same site after the domain move.
- Deleted projects no longer appear in `list_projects`.
