---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: ui-ux-developer-subagent
status: planning
revision: 1
created_at: 2026-09-10T15:55:00Z
updated_at: 2026-09-10T15:55:00Z
predecessor_handoff: docs/workstreams/20260910-engine-labs-company-os/product-manager-subagent/handoff.md
---

# Role Charter: ui-ux-developer-subagent

## 1. Role objective

### Mission

Specify the release-1 member experience of Engine Labs derived from the Papership `/cc-org-dash` shell at the pinned commit: the seven core views (home, work item, assistant, agent run, connection setup, memory manager, permissions editor), seat-specific flows for the Founder seat with Project Lead/Operator variants noted, adaptive-view rules, accessibility and responsive states, and a component-migration map from the reference's JSX components to the Tauri/TypeScript desktop — so engineering can implement without inventing UX and security can review what is exposed to whom.

## 2. Inherited request and evidence

- Workstream manifest: `docs/workstreams/20260910-engine-labs-company-os/manifest.md`
- Active plan: `docs/plans/phase_0_foundations_plan.md` (T0-7)
- Predecessor handoff: PM handoff (PRD IDs, seat templates, release-1 acceptance)
- Reference: `enginelabs-au/Papership` @ `8a843bd6429faf1ace5a9eb6dcfb7440703d34c4` — `src/App.jsx`, `src/pages/cc-org-dash.jsx`, `src/components/cc-org-dash/*` (20 files), `src/index.css`, `tailwind.config.js`, `components.json`
- Intake sections: "Member experience and authority model", "Design specification", "Adaptive views", `docs/ui-blueprint.md` requirement
- Blueprint §8 PRD-A/PRD-D, §10 desktop layer

## 3. Scope, non-goals, and ownership

- In scope: view specifications (purpose, layout, primary actions, states: loading/empty/error/disconnected/pending-approval/running/completed), navigation model (GlobalCommandRail, GlobalAgentPanel, PlatformStatusBar, NotifDrawer relationships), seat-specific defaults, adaptive-view constraints (schema-driven, sandboxed, no privileged access), accessibility (keyboard, focus, contrast, motion, screen reader), responsive/desktop window behaviour, component migration map and departures from reference, screenshot capture plan for SE.
- Explicit non-goals: visual redesign; implementing components; choosing backend APIs; security controls design; any file edits.
- Owned/write paths or `read-only`: **read-only**. Lead materializes `evidence.md`, `handoff.md`, and the `docs/ui-blueprint.md` specification sections.
- Read-only paths: repository; reference repository via GitHub MCP read tools.
- External-system scope: none. No Figma file exists (verified: none supplied); Figma MCP not used.
- Prohibited actions: file edits; MCP writes; asserting visual details not present in source; exposing prompts/schemas/runtime config in Founder-seat views.

## 4. Inherited requirements and vertical responsibilities

REQ-03 (member experience); PRD-A framework views; PRD-D authority exposure rules as UX constraints; intake Design specification (seven views); adaptive views (schema-driven, sandboxed, accessible, previewable, revertable, permission-checked, disclosed).

## 5. Assumptions, open questions, and clarification decisions

- `verified` — Reference shell files and stack (STATE.md Active Items).
- `provisional` — Release 1 targets macOS desktop window sizes; mobile breakpoints preserved from `useIsMobile.jsx` but not tested.
- `provisional` — `Dashboard.jsx`/`Dashboard_new.jsx` are legacy and excluded from the shell.
- Open question: preferred default theme (reference uses `next-themes`); record as owner preference, default to system.

## 6. Skills, tools, and evidence sources

GitHub MCP `get_file_contents` (verified reachable 2026-09-10) for reading reference source; repository reads. Screenshot capture is delegated to SE (T0-8) because it requires running the reference.

## 7. Outputs and storage paths

Payload → `docs/workstreams/20260910-engine-labs-company-os/ui-ux-developer-subagent/{evidence,handoff}.md`; `docs/ui-blueprint.md` (specification sections; SE completes commit/file/launch/capture sections).

## 8. Horizontal quality coverage

- Product and user acceptance: reviewed (PRD IDs referenced per view).
- UI/UX and accessibility: owned.
- Frontend/backend/data/API/integration impact: reviewed (component migration feasibility; data each view needs).
- Security/privacy/compliance/abuse: reviewed (what each seat sees; disclosure of AI-generated views; no privileged access from views).
- Testing/observability/reliability/performance: reviewed (state coverage for tests).
- Deployment/rollback/operations: not applicable in phase 0.
- Analytics/growth/consent: reviewed (event points per view for Growth taxonomy).
- Documentation/handoff: owned (ui-blueprint specification).

## 9. Validation plan and gate criteria

Pass when: all seven views specified with all states; navigation model documented; seat variants noted; adaptive-view constraints listed; accessibility criteria per view; migration map covers all 20 reference components (keep/adapt/replace/drop with reason); capture plan lists exact routes/states for SE. Claims about the reference must cite file paths.

## 10. Risks, blockers, and escalation triggers

Reference components may embed sample data assumptions (`data.jsx`); flag data contracts SE must replace. Escalate if PM handoff lacks seat templates.

## 11. Failure handling and recovery

Return BLOCKED with missing inputs; no partial output materialized by the role.

## 12. Downstream role and handoff conditions

Downstream: `software-engineer-subagent` requires the capture plan, migration map, and view/state matrix.

Execution must not begin until this charter is complete, internally consistent, and linked from the workstream manifest.
