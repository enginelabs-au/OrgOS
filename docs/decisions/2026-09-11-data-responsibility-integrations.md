# Decision D-12: Integration data responsibility (H-4 restated)

## Status

`accepted` — owner-directed 2026-09-11.

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md`.

## Context

H-4 asked which model provider receives Papership prompts. The owner restated the product rule for **all** integrations, not only OpenRouter.

## Decision

1. **Integrations are their own data controllers.** If the user connects OpenRouter, a bank, GitHub, or any other third party, that company handles data under **its** terms. Papership/Engine Labs does not adopt or warrant those terms.
2. **Engine Labs does not take responsibility for customer or user data** held by an integration, or for how that integration uses it.
3. **Native, non-integrated features** (local Papership UI, local sqlite/store, on-device settings that never leave the machine) stay **local** and are **managed by the user** of that deployment.
4. Enabling an integration is the user’s choice and the user’s acceptance of that vendor’s data-use terms. Marketing must not claim Engine Labs “covers” an integration’s privacy or training policy.
5. D-11 still names the current Hermes gateway (**OpenRouter**) as the first live model hop. D-12 is the general rule; D-11 is the first instance.

## Limits of this record

This is product policy for Papership. It is not a substitute for published Terms of Service or Australian privacy notices before a paid or multi-tenant launch. Local files this deployment writes (API sqlite, logs) remain on the operator’s machine; “user-managed” means the self-host operator, not a claim that no local data exists.

## Consequences

- H-4 is satisfied as: integrations own their data handling; Engine Labs disclaims controller responsibility for those destinations.
- UI and docs should say “this leaves Papership and is handled by &lt;vendor&gt;” when a connector is enabled.
- Do not store integration secrets in git or agent markdown.
