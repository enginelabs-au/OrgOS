---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: software-engineer-subagent
status: planning
revision: 1
created_at: 2026-09-10T15:55:00Z
updated_at: 2026-09-10T15:55:00Z
predecessor_handoff: docs/workstreams/20260910-engine-labs-company-os/ui-ux-developer-subagent/handoff.md
---

# Role Charter: software-engineer-subagent

## 1. Role objective

### Mission

Execute the phase-0 foundation checks and produce the engineering documents release 1 depends on: workstation toolchain inventory; root `.gitignore`; reference clone at the pinned commit with `npm ci`, build, run, and state captures; `docs/ui-blueprint.md` completion; `docs/capabilities.md` with all 43 domain rows; `docs/architecture.md` with diagram, entities, trust boundaries, data destinations, and the Hermes adapter contract expectations; `docs/verification.md`; decision drafts D-01 (monorepo layout) and D-04 (Hermes adapter contract). No application code in phase 0.

## 2. Inherited request and evidence

- Manifest; phase 0 plan (T0-8); blueprint §10–§11.
- Predecessor handoffs: PM (registry schema, PRD IDs), UI/UX (capture plan, migration map).
- Documentation already fetched by lead (cite, re-verify if needed): Hermes API server, DBOS Python guide, Tauri 2 overview (URLs in blueprint §2).
- Reference: `enginelabs-au/Papership` @ `8a843bd6429faf1ace5a9eb6dcfb7440703d34c4`.

## 3. Scope, non-goals, and ownership

- In scope: items (a)–(h) of T0-8.
- Explicit non-goals: application code; Docker Compose; schemas; installing Hermes/DBOS/Supabase; installing global toolchains (record absence instead); committing; modifying protected files; modifying `.cursorignore`.
- Owned/write paths: `.gitignore` (new), `.reference/orgos/` (clone), `docs/ui-blueprint.md` (commit/files/launch/capture/component sections; preserve UI/UX specification sections), `docs/ui-blueprint/*.png`, `docs/capabilities.md`, `docs/architecture.md`, `docs/verification.md`, `docs/decisions/2026-09-10-monorepo-layout.md`, `docs/decisions/2026-09-10-hermes-adapter-contract.md`, `docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/{evidence,handoff}.md`.
- Read-only paths: everything else.
- External-system scope: `git clone` of the public reference over HTTPS; `npm ci` from the npm registry (allowed hosts). No pushes, no accounts.
- Prohibited actions: running anything from the reference beyond documented `npm ci`, `npm run build`, `npm run dev`, `npm run lint`, `npm run typecheck`; touching protected files; secrets; network beyond GitHub/npm from sandboxed shell; deleting anything outside owned paths.

## 4. Inherited requirements and vertical responsibilities

REQ-02 (registry file), REQ-03 (ui-blueprint capture), REQ-04 (architecture), REQ-06 (verification index). Vertical: implementation, tooling, documentation, reproducible evidence per ROLES.md SE section.

## 5. Assumptions, open questions, and clarification decisions

- `provisional` — Clone path `.reference/orgos/`, ignored by new `.gitignore`.
- `provisional` — Captures via the Cursor IDE browser tool against `http://localhost:5173/cc-org-dash` at 1440×900 light and dark; if no display/browser path works, record the limitation and provide DOM-based component inventory instead.
- `provisional` — `npm ci` may be run with `--ignore-scripts` if lifecycle scripts fail or are undesirable; record which was used.

## 6. Skills, tools, and evidence sources

Shell (sandboxed; GitHub/npm allowed), Read/Write/Grep, Cursor IDE browser (`cursor-ide-browser`) for captures, GitHub MCP read. Availability of `rustc`/`cargo`/`docker` unknown until checked.

## 7. Outputs and storage paths

As in §3 owned paths. Evidence must include exact commands, exit codes, versions, timestamps.

## 8. Horizontal quality coverage

- Product and user acceptance: reviewed (registry rows carry PRD IDs).
- UI/UX and accessibility: reviewed (captures follow capture plan; departures reported).
- Frontend/backend/data/API/integration impact: owned (architecture, adapter contract).
- Security/privacy/compliance/abuse: reviewed (trust boundaries documented for Security review; no secrets; third-party code handled cautiously).
- Testing/observability/reliability/performance: owned (verification index; recovery expectations).
- Deployment/rollback/operations: reviewed (Compose/backup notes in architecture; not built).
- Analytics/growth/consent: reviewed (usage event storage location in architecture).
- Documentation/handoff: owned.

## 9. Validation plan and gate criteria

Pass when: toolchain versions recorded; `.gitignore` exists and covers `.reference/`, `node_modules/`, `.env*`; clone HEAD equals the pinned SHA (`git rev-parse HEAD`); `npm ci` and `npm run build` exit codes recorded; captures exist or limitation recorded; `docs/capabilities.md` has exactly 43 domain rows with all schema columns; architecture document contains diagram, entity list, trust boundaries, data-destination map, adapter contract table with citations; `docs/verification.md` maps blueprint 13–18; D-01 and D-04 drafted; validators still pass.

## 10. Risks, blockers, and escalation triggers

Reference build failures on current Node (record, try Node version in `.nvmrc` if present); no browser for captures; toolchain absent. Escalate only if nothing can be produced.

## 11. Failure handling and recovery

Any failed command is recorded with output summary; partial progress is reported truthfully; remove partial clone if corrupted; never retry destructive operations.

## 12. Downstream role and handoff conditions

Downstream: `security-engineer-subagent` requires architecture, trust boundaries, data destinations, adapter contract, registry, and `.gitignore` for review.

Execution must not begin until this charter is complete, internally consistent, and linked from the workstream manifest.
