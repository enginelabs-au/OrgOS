---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: growth-marketing-subagent
status: ready
revision: 1
created_at: 2026-09-10T15:58:00Z
updated_at: 2026-09-10T15:58:00Z
---

# Role Plan: growth-marketing-subagent

## 1. Entry criteria and inherited evidence

Charter complete; PM, UI/UX, Security handoffs materialized.

## 2. Scope, non-goals, and requirement coverage

| Requirement ID | Planned disposition | Expected evidence |
|---|---|---|
| REQ-05 commercial communication | Tier communication principles; activation prerequisites | Section with no prices |
| REQ-06 thresholds | V4/V5 review; first-baseline labelling | Threshold table |
| Usage measurement (intake) | Metric taxonomy; event naming; consent constraints | Taxonomy table |
| Positioning (blueprint §6) | Statement + differentiation grounded in sources | Cited statement |

## 3. Dependencies

PM metric inputs and tier structure; UI/UX event points; Security consent constraints.

## 4. Files, interfaces, data, and external systems

Read: blueprint, `docs/product.md`, `docs/ui-blueprint.md`, Security handoff, intake. Optional read-only web research with citations.

## 5. Ownership and concurrency

Read-only.

## 6. Ordered tasks

1. Positioning statement and Papership capability table (cite blueprint sources; add new sources only if fetched).
2. Value hypothesis and validation threshold review for V4/V5; define what "baseline" means for a single-user pilot.
3. Metric taxonomy: task completion, correctness, recovery, operator intervention, context switching, cost per completed outcome — definition, unit, event source, owner, privacy class.
4. Event naming convention (`domain.object.action`), required properties, prohibited properties (no PII, no prompt text), consent and retention alignment with Security.
5. Pilot learning plan: what release 1 must record to inform release 2 scope and pricing.
6. Tier communication principles (transparency of allowances, budgets, reservations; no prices) and commercial activation prerequisites (measured costs, rate card evidence, licensing).
7. Later-release GTM posture (communities, trust assets, sequence) as drafts; ethics constraints.
8. Return handoff payload with verdict.

## 7. Tool and modality plan

Repository reads; web read-only optional.

## 8. Horizontal full-stack checklist

Product: reviewed. UI/UX: reviewed. Frontend/backend/data: reviewed. Security/privacy: reviewed. Testing: reviewed. Deployment: not_applicable. Analytics/consent: owned. Documentation: owned.

## 9. Risk controls, rollback, and recovery

No mutation; nothing published.

## 10. Validation steps and expected evidence

Per charter §9.

## 11. Outputs and storage paths

`growth-marketing-subagent/{evidence,handoff}.md`; `docs/roadmap.md` sections.

## 12. Gate criteria and downstream handoff

PASS/CONDITIONAL → `project-lead-subagent`.

## 13. Deviations and plan change log

- r1 initial.

No deliverable-producing or state-changing action begins until the charter and this exhaustive plan are complete and consistent with the manifest.
