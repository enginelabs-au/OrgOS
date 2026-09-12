# Runbook: Vercel Papership project only

## Rules

- The only Vercel project this repo may use is the Papership product project (`prj_S74JOIky7KugVTrfu652NhJYOL8l`). Until the owner renames it on Vercel, the dashboard slug is still `orgos` and the preview host is still `orgos-ivory.vercel.app`. Do not invent a second Vercel project.
- **Never** edit, pause, or delete `enginelabs-au-site` or `enginelabs.com.au`. That site is a different Engine Labs product.
- **Never** touch Shuffle, Distroclub, jinglelabs, hermes-playground, or other account projects.
- There are no Vercel projects named `web`, `ui-blueprint`, `desktop`, `api`, or `worker`. Those are folders in this monorepo, not Vercel apps.
- API and worker stay in this repo (`services/api`, `services/worker`). They are not Vercel projects. Host them with Compose/local `uv`, or later Supabase (identity/Postgres) plus a VPS. Redis is optional later for queues; not required for phase 2.

## Deploy

Root `vercel.json` builds `@papership/web` (`apps/web`, blueprint-2 at `/papership`).
