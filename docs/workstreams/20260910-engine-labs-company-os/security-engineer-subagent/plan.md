---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: security-engineer-subagent
status: ready
revision: 1
created_at: 2026-09-10T15:58:00Z
updated_at: 2026-09-10T15:58:00Z
---

# Role Plan: security-engineer-subagent

## 1. Entry criteria and inherited evidence

Charter complete; SE handoff with `docs/architecture.md` materialized; PM and UI/UX handoffs available.

## 2. Scope, non-goals, and requirement coverage

| Requirement ID | Planned disposition | Expected evidence |
|---|---|---|
| REQ-03 authority | Review D-03 against intake; gap list | Review table |
| REQ-04 boundaries | Threat model over components/boundaries | STRIDE table |
| REQ-05 lifecycle/memory/erasure | Requirements and policy content | Policy drafts |
| Repository hygiene | Secret-pattern grep; `.gitignore` coverage | Command + result |
| Supply chain | Lockfile/pinning/licence inventory plan | Requirements list |

## 3. Dependencies

SE architecture and registry; PM PRD-D/F; UI/UX exposure table.

## 4. Files, interfaces, data, and external systems

Read: `docs/architecture.md`, `docs/product.md`, `docs/ui-blueprint.md`, `docs/capabilities.md`, `.gitignore`, `.cursor/hooks/policy.mjs`, `.cursor/*.json`, intake. No external systems.

## 5. Ownership and concurrency

Read-only.

## 6. Ordered tasks

1. Enumerate components, data stores, trust boundaries, and data destinations from `docs/architecture.md`; note gaps.
2. Threat model (STRIDE per boundary): desktop↔API, API↔Hermes, Hermes↔tools/external systems, API↔Supabase/Postgres, worker isolation, backups, updates/signing, repository automation.
3. Authority-model review: seats, hierarchy, server-side row/field/action checks (search, aggregates, attachments, notifications, memory), source-permission intersection, provisioning/handover/revocation; list gaps as findings.
4. Agent execution controls: sponsorship fields, action lifecycle, approval binding to action+target version, budget reservation, idempotency/receipts, recovery bounds, circuit breakers, prompt-injection posture, tool interception evidence needed in phase 1.
5. Data lifecycle: classification, residency, retention defaults, erasure flows, offboarding, backups (encryption, separate location, restore testing), provider data destinations.
6. Secrets and supply chain: keychain use, server env, no repo secrets; lockfiles; pinning (Hermes version pin); licence inventory plan; `npm ci` scripts stance; dependency review cadence.
7. Repository hygiene: `rg -n "(BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|xox[baprs]-)" --glob '!**/node_modules/**' --glob '!.reference/**'` (record command/exit); `.gitignore` review.
8. Findings list with severity (critical/high/medium/low), owner, remediation, re-verification method, phase gate.
9. Draft policy content for the five policy files.
10. Return handoff payload with verdict.

## 7. Tool and modality plan

Read/grep; no execution of third-party code; no scanners (recommend `npm audit`, `pip-audit`, `cargo audit`, licence scanner for phase 1).

## 8. Horizontal full-stack checklist

Product: reviewed. UI/UX: reviewed. Frontend/backend/data: reviewed. Security/privacy: owned. Testing/observability: reviewed. Deployment/operations: reviewed. Analytics/consent: reviewed. Documentation: owned.

## 9. Risk controls, rollback, and recovery

No mutation.

## 10. Validation steps and expected evidence

Per charter §9.

## 11. Outputs and storage paths

`security-engineer-subagent/{evidence,handoff}.md`; `docs/policies/*` content.

## 12. Gate criteria and downstream handoff

PASS/CONDITIONAL → `growth-marketing-subagent`; findings to PL.

## 13. Deviations and plan change log

- r1 initial.

No deliverable-producing or state-changing action begins until the charter and this exhaustive plan are complete and consistent with the manifest.
