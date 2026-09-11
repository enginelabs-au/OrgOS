---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: product-manager-subagent
status: ready
revision: 1
created_at: 2026-09-10T15:50:00Z
updated_at: 2026-09-10T15:50:00Z
---

# Role Plan: product-manager-subagent

## 1. Entry criteria and inherited evidence

Charter complete; manifest §5 lists the role as required; blueprint and phase 0 plan exist; intake readable.

## 2. Scope, non-goals, and requirement coverage

| Requirement ID | Planned disposition | Expected evidence |
|---|---|---|
| REQ-02 | Define PRD-A…PRD-G with acceptance criteria; registry schema + status vocabulary; 43-domain bucket assignment to releases | PRD table; schema; bucket table citing intake |
| REQ-05 (product aspects) | Runtime sponsorship fields, action lifecycle, memory governance, retention defaults, offboarding/erasure, tier structure as requirements | Requirement entries citing intake sections |
| REQ-06 (inputs) | Release-1 acceptance definition; metric taxonomy inputs | Acceptance definition; metric list |

## 3. Dependencies

Intake; blueprint; phase 0 plan; ROLES.md PM section. No credentials.

## 4. Files, interfaces, data, and external systems

Read: `docs/Company_Agent_System_Blueprint.md`, `docs/blueprints/2026-09-10_engine_labs.md`, `docs/plans/phase_0_foundations_plan.md`, manifest. Output: payload for `docs/product.md`, `evidence.md`, `handoff.md`.

## 5. Ownership and concurrency

Read-only role; single parent materializes. No concurrent writers.

## 6. Ordered tasks

1. Read the intake end to end; list every requirement-bearing section (objective, dependencies: none; evidence: section list).
2. Define PRD-A…PRD-G with sub-IDs (e.g., PRD-A.1) and observable acceptance criteria; map each intake sentence-level requirement to a PRD ID.
3. Define the registry row schema (columns from intake: domain ID, user outcome, native/connector owner, read actions, write actions, data authority, grants, dependencies, interface components, release phase, implementation status, acceptance evidence) and status vocabulary (`planned`, `configured`, `working`, `unavailable`) with transition rules.
4. Assign each of the 43 domain groups to a release bucket consistent with the intake release map; mark release-1 rows (`planned` in phase 0; only development-loop-related rows can reach `working` in release 1).
5. State the three seat templates as product requirements (default views, allowed actions, prohibited exposures).
6. Define release-1 acceptance (the intake's "Final result" made testable) and the metric taxonomy inputs.
7. Define tier structure requirements (Free, Basic, Professional, Enterprise: what each includes; allowance and budget semantics; reservation/reconciliation; rate-card and usage-ledger requirements) with no prices.
8. Record open owner questions and provisional assumptions.
9. Return the canonical handoff payload with verdict and evidence citations.

Rollback/safe failure: return BLOCKED with the missing input; no files touched.

## 7. Tool and modality plan

Repository reads only. GitHub MCP read tools optional for reference confirmation.

## 8. Horizontal full-stack checklist

Product/user: owned. UI/UX: reviewed. Frontend/backend/data/API/integration: reviewed. Security/privacy: reviewed. Testing/observability: reviewed. Deployment/operations: not_applicable (phase 0). Analytics/growth: reviewed. Documentation: owned.

## 9. Risk controls, rollback, and recovery

No mutation; nothing to roll back.

## 10. Validation steps and expected evidence

Lead verifies: every intake section cited at least once; 43 domain rows bucketed; no prices; acceptance criteria observable; handoff verdict supported.

## 11. Outputs and storage paths

`docs/workstreams/20260910-engine-labs-company-os/product-manager-subagent/{evidence,handoff}.md`; `docs/product.md`.

## 12. Gate criteria and downstream handoff

PASS/CONDITIONAL → `ui-ux-developer-subagent`. BLOCKED → lead remediates inputs and relaunches.

## 13. Deviations and plan change log

- r1 initial.

No deliverable-producing or state-changing action begins until the charter and this exhaustive plan are complete and consistent with the manifest.
