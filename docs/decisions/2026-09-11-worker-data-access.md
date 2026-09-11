# Decision D-08: Worker data access

## Status

`accepted` — owner-directed H-6 ratification 2026-09-11. Record: `docs/decisions/2026-09-11-owner-ratification-h6.md`.

## Context

Architecture §10 originally listed the worker on `data` for receipt persistence. AUTH-24 / C-02 require the worker never to sit on the data network. Persistence must go through the API.

## Decision

1. `services/worker` joins **only** the `worker` Compose network.
2. The worker has **no** `DATABASE_URL` / `DBOS_SYSTEM_DATABASE_URL` in its environment allowlist.
3. All persistence (receipts, job events, usage) is performed by calling the API on the `worker`↔`app` path.
4. Hermes (phase 2) also stays on `worker` only.

## Consequences

Compose assertions fail if `worker` appears in `data`. API must expose authenticated internal routes for worker callbacks. D-07 pins Caddy and Postgres 15 independently.
