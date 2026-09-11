---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: security-engineer-subagent
status: planning
revision: 1
created_at: 2026-09-10T15:58:00Z
updated_at: 2026-09-10T15:58:00Z
predecessor_handoff: docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/handoff.md
---

# Role Charter: security-engineer-subagent

## 1. Role objective

### Mission

Independently review the release-1 architecture, authority model, data lifecycle, agent execution model, and repository hygiene of Engine Labs before any implementation: produce a threat model, an authority-model review (D-03), data-destination/retention/erasure review, agent tool side-effect and prompt-injection control requirements, secrets and supply-chain requirements, and a findings list with severity and required remediation gates for phase 1. Tier 3 mandates this role.

## 2. Inherited request and evidence

- Manifest (Tier 3 rationale §4); phase 0 plan (T0-9); blueprint §12.
- Predecessor handoffs: PM (PRD-D authority, PRD-F lifecycle), UI/UX (exposure per seat), SE (architecture, trust boundaries, data destinations, adapter contract, `.gitignore`, registry).
- Intake sections: authority model, runtime, action lifecycle, isolation, recovery, memory governance, retention, offboarding, erasure, data residency, licensing.
- Repository controls: `.cursor/hooks/policy.mjs`, `.cursor/hooks.json`, `.cursor/cli.json`, `.cursor/sandbox.json`, `.cursor/permissions.json`, `.cursorignore`, `.github/workflows/agent-governance.yml` (read-only).

## 3. Scope, non-goals, and ownership

- In scope: STRIDE-style threat model over release-1 components and trust boundaries; authority-model review; data classification and destination map review; retention/erasure/offboarding requirements; agent execution controls (isolation, tool interception, approval binding, idempotency/receipts, budget); prompt-injection posture; secrets handling requirements (desktop keychain, server env, no secrets in repo); supply-chain baseline (lockfiles, pinning, licence inventory plan, `npm ci` lifecycle-script stance); repository hygiene check (grep for secret patterns; `.gitignore` coverage); policy documents content for `docs/policies/*`.
- Explicit non-goals: implementing controls; penetration testing; production configuration; modifying protected files; approving production.
- Owned/write paths or `read-only`: **read-only**. Lead materializes `evidence.md`, `handoff.md`, and `docs/policies/*`.
- Read-only paths: repository including `.reference/orgos/` (do not execute).
- External-system scope: none.
- Prohibited actions: file edits; MCP writes; executing reference code; secret-value handling; waiving Tier 3 gates.

## 4. Inherited requirements and vertical responsibilities

REQ-03 (authority), REQ-04 (boundaries), REQ-05 (lifecycle, memory, erasure). Vertical per ROLES.md Security section: threat, privacy, authorization, dependency, secrets, infrastructure, abuse-case review.

## 5. Assumptions, open questions, and clarification decisions

- `verified` — Development-time fail-closed hooks are live.
- `provisional` — Hermes API bearer auth is transport-only; authorization enforced by Engine Labs action service (blueprint §10). Review must state what evidence phase 1 needs to confirm tool interception is enforceable.
- Open: whether Hermes' `/v1/runs/{id}/approval` can be the sole approval path or Engine Labs must wrap it; record as a phase-1 spike requirement.

## 6. Skills, tools, and evidence sources

Repository read/grep; documentation URLs from the blueprint; SE architecture document. No scanners configured (record; recommend for phase 1).

## 7. Outputs and storage paths

Payload → `security-engineer-subagent/{evidence,handoff}.md`; content for `docs/policies/{authority-model,data-residency-and-retention,memory-governance,erasure-and-offboarding,licensing}.md`.

## 8. Horizontal quality coverage

- Product and user acceptance: reviewed (acceptance criteria include security evidence).
- UI/UX and accessibility: reviewed (exposure per seat; disclosure of AI-generated views).
- Frontend/backend/data/API/integration impact: reviewed (boundaries).
- Security/privacy/compliance/abuse: owned.
- Testing/observability/reliability/performance: reviewed (audit log requirements, receipt verification).
- Deployment/rollback/operations: reviewed (backup encryption, restore testing, secrets in Compose).
- Analytics/growth/consent: reviewed (consent and data minimisation for usage events).
- Documentation/handoff: owned (policies content).

## 9. Validation plan and gate criteria

Pass when: threat model covers every component and boundary in `docs/architecture.md`; each threat has a control and a phase in which it is verified; authority model reviewed against intake requirements with gaps listed; data-destination map reviewed; retention/erasure requirements complete; findings have severity, owner, remediation, re-verification method; no critical/high finding lacks a phase-1 gate; repository hygiene grep clean. Unsupported claims → BLOCKED.

## 10. Risks, blockers, and escalation triggers

Escalate if architecture places secrets or privileged execution on the desktop, or if the adapter contract cannot enforce per-tool authorization.

## 11. Failure handling and recovery

Return BLOCKED with the missing input or the blocking finding.

## 12. Downstream role and handoff conditions

Downstream: `growth-marketing-subagent` requires consent/data-minimisation constraints for measurement; `project-lead-subagent` requires the findings list and phase-1 gates.

Execution must not begin until this charter is complete, internally consistent, and linked from the workstream manifest.
