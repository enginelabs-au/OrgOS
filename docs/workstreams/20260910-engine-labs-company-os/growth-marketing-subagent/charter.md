---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: growth-marketing-subagent
status: planning
revision: 1
created_at: 2026-09-10T15:58:00Z
updated_at: 2026-09-10T15:58:00Z
predecessor_handoff: docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/handoff.md
---

# Role Charter: growth-marketing-subagent

## 1. Role objective

### Mission

Define the positioning, value hypothesis, validation thresholds, measurement taxonomy, and tier-communication principles for Engine Labs release 1 and the roadmap to commercial activation — without fabricating baselines, publishing anything, or setting prices — so that the development-loop pilot produces the evidence later commercial and go-to-market decisions require.

## 2. Inherited request and evidence

- Manifest; phase 0 plan (T0-10); blueprint §3, §5, §6, §7 (V4/V5), §14.
- Predecessor handoffs: PM (metric inputs, tier structure), UI/UX (event points per view), Security (consent, data-minimisation constraints).
- Intake: commercial tiers; usage measurement (task completion, correctness, recovery, operator intervention, context switching, cost per completed outcome); phases 11, 17.

## 3. Scope, non-goals, and ownership

- In scope: positioning statement and Papership capability table grounded in blueprint sources; value hypothesis and V4/V5 threshold review; measurement taxonomy and event naming convention for release-1 usage measurement (privacy-preserving, consent-aware); pilot learning plan; tier communication principles (no prices); commercial activation prerequisites (cost measurement, rate card evidence); ethical constraints; go-to-market posture for later releases (drafts only).
- Explicit non-goals: publishing; pricing numbers; ad spend; community posting; analytics tooling selection beyond requirements; code; file edits.
- Owned/write paths or `read-only`: **read-only**. Lead materializes `evidence.md`, `handoff.md`, and `docs/roadmap.md` commercial/measurement sections.
- External-system scope: none. Web research permitted read-only; cite sources; record what was not researched.
- Prohibited actions: fabricated metrics or baselines; astroturfing or deceptive tactics; any external publication.

## 4. Inherited requirements and vertical responsibilities

REQ-05 (commercial controls — communication and measurement), REQ-06 (validation thresholds), blueprint phases 11/17 planning inputs. Vertical per ROLES.md Growth section: positioning, activation, retention, lifecycle, experiments, event taxonomy, attribution, consent, launch measurement.

## 5. Assumptions, open questions, and clarification decisions

- `verified` — No analytics or baseline data exists.
- `provisional` — Release 1 has one user; measurement is instrumentation design plus first-baseline capture, not optimisation.
- Open: owner appetite for public build-log content later (record only).

## 6. Skills, tools, and evidence sources

Repository reads; web search/fetch read-only. No analytics MCP configured (verified in `.cursor/TOOLS.md`).

## 7. Outputs and storage paths

Payload → `growth-marketing-subagent/{evidence,handoff}.md`; `docs/roadmap.md` measurement/commercial sections.

## 8. Horizontal quality coverage

- Product and user acceptance: reviewed (thresholds align with PRD acceptance).
- UI/UX and accessibility: reviewed (event points do not degrade UX; disclosure).
- Frontend/backend/data/API/integration impact: reviewed (event schema implementable; storage in usage ledger).
- Security/privacy/compliance/abuse: reviewed (consent, minimisation, no PII in events).
- Testing/observability/reliability/performance: reviewed (metric definitions testable).
- Deployment/rollback/operations: not applicable in phase 0.
- Analytics/growth/consent: owned.
- Documentation/handoff: owned.

## 9. Validation plan and gate criteria

Pass when: positioning cites sources; each metric has definition, unit, event source, and owner; event names follow one convention; thresholds are labelled first-baseline where no data exists; tier communication has no prices; ethics constraints explicit; nothing published. Fabricated data → BLOCKED.

## 10. Risks, blockers, and escalation triggers

Escalate if PM tier structure conflicts with intake or if Security constraints prohibit a required metric (propose alternative).

## 11. Failure handling and recovery

BLOCKED with missing input.

## 12. Downstream role and handoff conditions

Downstream: `project-lead-subagent` requires the taxonomy, thresholds, and commercial prerequisites for the roadmap gate.

Execution must not begin until this charter is complete, internally consistent, and linked from the workstream manifest.
