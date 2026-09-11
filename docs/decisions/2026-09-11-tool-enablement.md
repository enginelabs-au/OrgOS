# D-17 — Owner-authorized tool enablement

Date: 2026-09-11  
Status: accepted — owner-directed. Supersedes D-16 follow-up (“keep toolsets disabled”). AUTH-25 still applies.

## Why they were forbidden

T2-1 could not prove live pause-before-tool: the pin is `hermes serve` (login UI), not the HTTP API server. Security CONDITIONAL required `interception_verified: false` so a model could not call terminal/browser/github with no Papership record. That was a spike gate, not a product rule that tools are banned.

## Decision

1. Enable the documented Hermes `hermes-api-server` catalog in `services/worker/policy_hooks/catalog.py`.
2. Unknown tools stay **denied**.
3. Risk classes: read (catalog), write (receipt), external/destructive (Papership approval then receipt).
4. Egress: deny private, link-local, and cloud-metadata hosts. Public HTTPS is allowed for research.
5. `HERMES_API_SERVER_KEY` may be held by the **worker only** (transport). The API and desktop never read it.
6. GitHub mutations still prefer `POST /github/pulls` with `repo.*` ∩ installation permissions (AUTH-12).
7. `start_run` is implemented. If Hermes is not an API server, the job is persisted and the runtime is `blocked_runtime` — not a fake success.

## Artefact

`docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/artifacts/t2-2-tool-enablement-artefact.md`  
`interception_verified: true` only while `toolsets.yaml` sha256 matches that file.
