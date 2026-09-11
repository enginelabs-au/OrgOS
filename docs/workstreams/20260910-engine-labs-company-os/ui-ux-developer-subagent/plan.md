---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: ui-ux-developer-subagent
status: ready
revision: 1
created_at: 2026-09-10T15:55:00Z
updated_at: 2026-09-10T15:55:00Z
---

# Role Plan: ui-ux-developer-subagent

## 1. Entry criteria and inherited evidence

Charter complete; PM handoff PASS/CONDITIONAL materialized; reference reachable.

## 2. Scope, non-goals, and requirement coverage

| Requirement ID | Planned disposition | Expected evidence |
|---|---|---|
| REQ-03 / PRD-A views | Seven-view specification with states | View/state matrix citing PRD IDs |
| PRD-D exposure rules | Seat-specific visibility and prohibited exposures per view | Seat table per view |
| Adaptive views | Constraint list and preview/revert flow | Section in ui-blueprint |
| Accessibility | Per-view criteria | Checklist |
| Migration | 20-component keep/adapt/replace/drop map | Table citing reference paths |

## 3. Dependencies

PM handoff; reference source via GitHub MCP.

## 4. Files, interfaces, data, and external systems

Read reference files: `src/pages/cc-org-dash.jsx`, `src/components/cc-org-dash/{HomeScreen,WorkScreen,GlobalAgentPanel,GlobalCommandRail,GlobalCommandDetail,PlatformStatusBar,NotifDrawer,SettingsScreen,IntegrationsScreen,PeopleScreen,InboxScreen,DataScreen,FilesScreen,AccountScreen,AuthPortal,WorkflowVis,primitives,icons,data,useIsMobile}.jsx`, `src/index.css`, `tailwind.config.js`. Output payload only.

## 5. Ownership and concurrency

Read-only; lead materializes.

## 6. Ordered tasks

1. Read the shell and component sources; inventory screens, panels, rails, primitives, icon set, sample data contracts (evidence: file paths and line references).
2. Map intake's seven core views to existing screens/components; identify gaps (e.g., agent run view, connection setup, memory manager, permissions editor may not exist as-is).
3. Specify each view: purpose, PRD IDs, layout regions, primary/secondary actions, data needs, states (loading, empty, error, disconnected, pending approval, running, completed, restricted), seat visibility.
4. Define navigation and global surfaces (rail, agent panel, status bar, notifications) and how run progress/approvals surface globally.
5. Define adaptive-view constraints and preview/apply/revert flow.
6. Define accessibility criteria per view and global (keyboard, focus order, contrast, reduced motion, screen-reader labels) and desktop window behaviour (min size, resize, multi-window not in release 1).
7. Produce the component migration map (keep/adapt/replace/drop; JSX→TSX notes; dependency implications such as `three`, `leaflet`, `react-quill`, `jspdf` likely drop for release 1).
8. Produce the capture plan for SE: routes, viewport sizes, theme, states to trigger, filenames under `docs/ui-blueprint/`.
9. Return handoff payload with verdict and evidence.

Safe failure: BLOCKED with missing input.

## 7. Tool and modality plan

GitHub MCP read; repository read. No Figma (none exists). No browser (SE captures).

## 8. Horizontal full-stack checklist

Product: reviewed. UI/UX: owned. Frontend/backend/data: reviewed. Security/privacy: reviewed. Testing: reviewed. Deployment: not_applicable. Analytics: reviewed. Documentation: owned.

## 9. Risk controls, rollback, and recovery

No mutation.

## 10. Validation steps and expected evidence

Lead checks seven views × states, 20-component map, capture plan completeness, citations.

## 11. Outputs and storage paths

`ui-ux-developer-subagent/{evidence,handoff}.md`; `docs/ui-blueprint.md` specification sections.

## 12. Gate criteria and downstream handoff

PASS/CONDITIONAL → `software-engineer-subagent`.

## 13. Deviations and plan change log

- r1 initial.

No deliverable-producing or state-changing action begins until the charter and this exhaustive plan are complete and consistent with the manifest.
