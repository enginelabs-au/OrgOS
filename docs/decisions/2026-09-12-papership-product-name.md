# Decision D-20: Product display name is Papership

## Status

`accepted` — owner-directed 2026-09-12. Supersedes D-10 **display name** only.

## Decision

1. The product is **Papership**. User-visible names (wordmark, titles, API title, fixtures, docs) say Papership.
2. **Engine Labs** remains the company. `www.enginelabs.com.au` and Vercel project `enginelabs-au-site` stay untouched.
3. The product UI remains the `/cc-org-dash` route in `apps/web`. Chrome is **blueprint-2 exactly** (D-21 supersedes the earlier hybrid clause).
4. Live infrastructure slugs stay as residual identifiers until the owner renames them on each provider:
   - GitHub repository `enginelabs-au/OrgOS`
   - GitHub App `orgos-dev`
   - Vercel project `orgos`
   - local config `~/.config/orgos/`
   - `GITHUB_APP_REPO=OrgOS`
   - asset filename `papership-icon.png` (supersedes `orgos-icon.png`)
   - internal route `/cc-org-dash` (alias `/papership` added)

## Consequences

- Renaming the local folder `~/OrgOS` → `~/Papership` is safe: git remotes are URL-based and no committed code depends on that absolute path for runtime.
- Renaming the GitHub repo, Vercel project, or GitHub App without also updating those provider settings and `GITHUB_APP_REPO` will break the live App and deploy.
