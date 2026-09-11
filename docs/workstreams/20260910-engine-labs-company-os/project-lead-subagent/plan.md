---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: project-lead-subagent
status: ready
revision: 1
created_at: 2026-09-10T15:58:00Z
updated_at: 2026-09-10T15:58:00Z
---

# Role Plan: project-lead-subagent

## 1. Entry criteria and inherited evidence

Charter complete; five handoffs materialized; product documents exist; validator outputs available.

## 2. Scope, non-goals, and requirement coverage

| Requirement ID | Planned disposition | Expected evidence |
|---|---|---|
| REQ-01 | Confirm protocol compliance evidence | preflight/bootstrap/validator records |
| REQ-06 | Confirm roadmap, registries, prompt | checks against plan §16–§17, §22 |
| REQ-02…05 | Traceability audit | matrix intake→PRD→artifact→verification |

## 3. Dependencies

All prior handoffs; lead-supplied validator outputs.

## 4. Files, interfaces, data, and external systems

Read all phase 0 artifacts. No external systems.

## 5. Ownership and concurrency

Read-only.

## 6. Ordered tasks

1. Verify each phase 0 acceptance criterion (plan §19) against files; record evidence or gap.
2. Build the traceability matrix (intake section → PRD ID → registry/architecture/spec/policy → verification entry → phase).
3. Check consistency: manifest §5/§6 vs plan §13/§14 vs handoffs; registry row count; env-var names only; human-action queue completeness; decisions present.
4. Review Security findings: any critical/high without a phase-1 gate → BLOCKED.
5. Compile residual risks and owner decisions.
6. Confirm the Next Plan Generation Prompt references existing artifacts and that phase-1 scope is bounded to blueprint 07.
7. Propose STATE/MEMORY/manifest/plan deltas.
8. Return handoff payload with verdict.

## 7. Tool and modality plan

Reads; optional read-only validators.

## 8. Horizontal full-stack checklist

All areas: reviewed.

## 9. Risk controls, rollback, and recovery

No mutation.

## 10. Validation steps and expected evidence

Per charter §9.

## 11. Outputs and storage paths

`project-lead-subagent/{evidence,handoff}.md`.

## 12. Gate criteria and downstream handoff

PASS/CONDITIONAL → lead generates `docs/plans/phase_1_foundation_plan.md`. BLOCKED → remediation by owning role.

## 13. Deviations and plan change log

- r1 initial.

No deliverable-producing or state-changing action begins until the charter and this exhaustive plan are complete and consistent with the manifest.
