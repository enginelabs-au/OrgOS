# Decision D-32: Canonical product route is `/papership`

## Status

`accepted` — owner-directed 2026-09-12 (“whatever cc-org is? this was the old UI inspiration so it can be renamed”).

## Decision

1. The live Papership web UI mounts at **`/papership`**. `/` redirects there. Do not invent a marketing landing at `/`.
2. Leftover OrgOS / reference aliases **`/cc-org-dash`**, `/EcoOS`, `/ecoos`, `/Dashboard`, `/Dashboard_new` redirect to `/papership`.
3. Blueprint-2 storage keys are `papership-auth` and `papership-theme`. If a new key is missing, copy once from `cc-org-dash-auth` / `cc-org-dash-theme`. AUTH-27 still forbids treating that localStorage session as the product name or as production identity.
4. Directory `apps/web/src/components/cc-org-dash/` and historical decision filenames stay. This decision is the **public route and storage keys**, not a wholesale rewrite of leftover blueprint-1 components.

## Consequences

- D-20 item 3 and the “internal route `/cc-org-dash` (alias `/papership`)” residual are superseded for the live URL. Chrome remains blueprint-2 exactly (D-21 / D-22).
- Historical captures under `docs/ui-blueprint/blueprint-1/` may still mention `/cc-org-dash`; they are reference artefacts, not the live mount.
- Live GitHub / Vercel / App slugs remain owner residuals (D-26).
