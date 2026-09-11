# Decision D-10: OrgOS is the product; Engine Labs is the company

## Status

`accepted` — owner-directed 2026-09-11.

## Decision

1. The product in this repository is **OrgOS**. User-visible product names (window title, wordmark, Vercel project `orgos`, API title) say OrgOS.
2. **Engine Labs** is the trading name of the company. It may appear in copyright, licence, and legal entity text. It is not the product.
3. `www.enginelabs.com.au` and Vercel project `enginelabs-au-site` are a **separate** Engine Labs marketing/services site. This workstream must not replace, redirect, edit, or delete that site or move its domains onto OrgOS.
4. The OrgOS product UI is the `docs/ui-blueprint` `/cc-org-dash` tree, deployed from `apps/web` on the `orgos` Vercel project. The Engine Labs landing that was briefly added to `apps/web` is withdrawn.
5. Owner override of D-06 item 1 for the **web** surface: restore the blueprint primary tab set (Dashboard, Work, Inbox, People, Data, Files, Integrations, Settings). The desktop R1 five-tab set remains until the same shell is ported there.

## Consequences

- Do not create or delete Vercel projects for Engine Labs from this repo.
- Do not treat `apps/desktop`, `services/api`, or `services/worker` as separate Vercel apps; they are monorepo members of OrgOS. API/worker stay off Vercel (Python). Suggested hosts if needed later: Docker Compose on a VPS, or Supabase for identity/Postgres.
