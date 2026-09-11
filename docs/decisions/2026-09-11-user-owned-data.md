# Decision D-14: Users own their data

## Status

`accepted` — owner-directed 2026-09-11.

## Decision

1. **Papership / Engine Labs does not own customer or user content.** Prompts, files, tickets, and similar records are the user’s.
2. **What Papership may keep:** generic, anonymous product telemetry only (identifier/enum usage rows already required by GM-1). No content fields.
3. **User ownership:** on a self-host, data lives on the user’s machine (local sqlite/store). The user may delete it or request deletion. Until they do, Papership may retain **side-effect records** it needs to operate (approvals, audit, job receipts) so the loop can prove what it did.
4. **Integrations (D-12):** once data leaves to OpenRouter, GitHub, a bank, or any other vendor, that vendor’s terms apply. Papership does not take those copies back.
5. A later export/delete API is the product path for “request it be deleted” on a hosted tenant. Until that exists, self-host deletion is deleting the local store.

## How users own their data today

- Run Papership on their machine or VPS they control.
- Do not send content to an integration unless they choose to.
- Delete the local store / request erasure when they want it gone.

## Consequences

- Marketing must not say Engine Labs “owns” or trains on user content.
- Side-effect receipts stay until user deletion — they are operational proof, not a content warehouse.
