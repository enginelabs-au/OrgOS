---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: security-engineer-subagent
status: complete
revision: 1
verdict: CONDITIONAL
completed_at: 2026-09-12T12:55:00Z
lift_authorized: false
---

# Security Engineer handoff — D-25 lift review

**Verdict: CONDITIONAL. Live write/external Hermes `accepted` is not authorized.**

Independent review 2026-09-12 ([D-25 Hermes write gate](47859d89-6e71-416d-ae15-e0c05433bc26) + [Security Review](456e859e-3ffe-48e8-8fe3-c8a0a2ce0995)). D-25 is not lifted.

## Binding answers

| Question | Answer |
|---|---|
| May catalogued live **write** Hermes tools be `accepted`? | No |
| May catalogued live **external** Hermes tools be `accepted`? | No |
| Write = receipt proven? | Yes on intercept. No `start_run` → `accepted` for write. |
| External = approval then receipt proven? | Yes on intercept. No `start_run` → `accepted` for external. |
| What `accepted` is proven? | Catalogued **read** only (`memory_read`) |
| Does D-25 itself authorize this lift? | No |

## Why the lift fails

1. The only `start_run` → `accepted` test is catalogued read.
2. Hermes is not scoped to the declared `tool=` (F-T33-SEC-07).
3. Subscribe intercepts **after** Hermes may have executed (F-T33-SEC-03).
4. Job consumer has `persist_receipt` only — no `persist_approval`.
5. API `POST /runs` queues work; it never calls `HermesRuntimeAdapter.start_run`.

## Does not authorize

- `accepted` for write / external / destructive Hermes tools
- Treating intercept unit tests as a lift
- Changing `toolsets.yaml` as a substitute for this PASS

Keep D-25. A future lift needs SE implementation of the gaps above, live or staging replay, then a **new** Security PASS.
