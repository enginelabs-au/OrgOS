---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: security-engineer-subagent
status: complete
revision: 3
verdict: CONDITIONAL
started_at: 2026-09-11T12:58:00Z
completed_at: 2026-09-11T13:25:00Z
downstream_role: project-lead-subagent
risk_tier: 3
---

# Security Engineer handoff — Phase 3 T3-3 (r3)

Materialized by the lead from [T3-3 r3](aaebbf56-77db-46c9-b947-d191b697e4cb).

## Verdict

**CONDITIONAL.** AUTH-10 mismatch is fail-closed. F-T33-SEC-04 / 05 / 06 are remediated. Live Hermes tool `accepted` remains **forbidden**. This is not a Security PASS for side-effecting tools.

## Binding

1. Write receipts fail-closed; external = approval then receipt (unit).
2. Unknown tools denied (unit).
3. Serve-UI redirects → `serve_ui` / `blocked_runtime`.
4. HEAD 405 = Papership reachable only. Worker `api_server=False`.
5. AUTH-10 persist hash bound; mismatch refused.
6. V14-3: voided approval and revoked grant block later job steps.
7. AUTH-12 empty installation permissions refuse live PR (403) — inherited r2.
8. yaml/catalog/artefact hash change invalidates this verdict.
9. Papership `queued` is not a Security PASS for tools.

## Findings

| ID | Severity | Status |
|---|---|---|
| F-T33-SEC-01 | High latent | Open — `accepted` forbidden |
| F-T33-SEC-02 | Medium | Mitigated (r2, holds r3) |
| F-T33-SEC-03 | Medium | Open — subscribe intercept is post-SSE |
| F-T33-SEC-04 | Medium | Remediated |
| F-T33-SEC-05 | Low | Remediated |
| F-T33-SEC-06 | Low | Remediated (inventory; GET still hangs) |
| F-T33-SEC-07 | Medium if accepted | Open inherited |
| F-T33-SEC-08 | Owner | Open |

## Does not authorize

`runtime.status = accepted`; worker POST `/v1/runs` for tools; treating `queued` as a Security PASS; a second gateway; copying keys.
