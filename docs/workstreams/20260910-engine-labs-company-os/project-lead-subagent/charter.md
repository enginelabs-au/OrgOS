---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: project-lead-subagent
status: planning
revision: 1
created_at: 2026-09-10T15:58:00Z
updated_at: 2026-09-10T15:58:00Z
predecessor_handoff: docs/workstreams/20260910-engine-labs-company-os/growth-marketing-subagent/handoff.md
---

# Role Charter: project-lead-subagent

## 1. Role objective

### Mission

Reconcile the five specialist handoffs against the manifest, blueprint, phase 0 plan, and intake; verify traceability, consistency, and completeness of phase 0 artifacts; identify residual risks and unresolved requirements; confirm the Next Plan Generation Prompt is executable; and return the phase 0 gate verdict with proposed state and memory deltas. Tier 3 requires this role at every phase gate.

## 2. Inherited request and evidence

- Manifest; phase 0 plan (T0-12, §19 acceptance criteria); blueprint §17.
- Predecessor handoffs: PM, UI/UX, SE, Security, Growth.
- Product documents: `docs/product.md`, `docs/capabilities.md`, `docs/architecture.md`, `docs/blueprints/ui-blueprint.md`, `docs/roadmap.md`, `docs/verification.md`, `docs/policies/*`, decisions D-01…D-05.
- Validators and tests listed in phase 0 plan §19.

## 3. Scope, non-goals, and ownership

- In scope: cross-role reconciliation; requirement traceability (intake → PRD → registry/architecture/spec → verification); plan/manifest/state consistency; residual risk register; owner-decision list; phase 0 verdict; readiness of the phase-1 prompt.
- Explicit non-goals: producing specialist content; approving production; modifying files.
- Owned/write paths or `read-only`: **read-only**. Lead materializes `evidence.md`, `handoff.md`.
- External-system scope: none.
- Prohibited actions: file edits; overriding a Security BLOCKED verdict; treating verdicts as production authorization.

## 4. Inherited requirements and vertical responsibilities

REQ-01, REQ-06; all requirements for traceability. Vertical per ROLES.md PL section.

## 5. Assumptions, open questions, and clarification decisions

- `verified` — Phase 0 is documentation-only; no release action is being requested.
- `provisional` — CONDITIONAL is acceptable for phase 0 if every open item has an owner and a phase-1 gate.

## 6. Skills, tools, and evidence sources

Repository reads; validator/test outputs supplied by lead; may run read-only validators.

## 7. Outputs and storage paths

Payload → `project-lead-subagent/{evidence,handoff}.md`; proposed deltas for `.cursor/STATE.md`, `MEMORY.md`, manifest §11–§15, phase 0 plan §20–§21.

## 8. Horizontal quality coverage

All domains: reviewed for coverage and consistency; none owned.

## 9. Validation plan and gate criteria

Pass when: every phase 0 acceptance criterion (§19) has evidence; every intake requirement traces to a PRD ID and a phase; every skipped/required role decision is evidenced (none skipped); no unresolved BLOCKED; residual risks and owner decisions listed; Next Plan Generation Prompt references existing artifacts.

## 10. Risks, blockers, and escalation triggers

Escalate contradictions between handoffs to the lead for remediation by the owning role.

## 11. Failure handling and recovery

BLOCKED with the failing criterion and owning role.

## 12. Downstream role and handoff conditions

Downstream: orchestrating lead (state/memory materialization; phase-1 plan generation). Owner decision is not requested at phase 0.

Execution must not begin until this charter is complete, internally consistent, and linked from the workstream manifest.
