---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: software-engineer-subagent
status: ready
revision: 1
created_at: 2026-09-10T15:55:00Z
updated_at: 2026-09-10T15:55:00Z
---

# Role Plan: software-engineer-subagent

## 1. Entry criteria and inherited evidence

Charter complete; PM and UI/UX handoffs materialized with supported verdicts; capture plan and registry schema available.

## 2. Scope, non-goals, and requirement coverage

| Requirement ID | Planned disposition | Expected evidence |
|---|---|---|
| REQ-02 registry file | `docs/capabilities.md`, 43 rows per PM schema | row count; columns |
| REQ-03 capture | clone, run, capture; complete `docs/blueprints/ui-blueprint.md` | SHA, exit codes, PNGs |
| REQ-04 architecture | `docs/architecture.md` + D-01 + D-04 | document with citations |
| REQ-06 verification index | `docs/verification.md` | mapping table |
| Foundation checks | toolchain inventory; `.gitignore` | versions; file |

## 3. Dependencies

Network to GitHub/npm; Node ≥ 18; optional browser tool.

## 4. Files, interfaces, data, and external systems

Owned paths per charter §3. External: GitHub (clone), npm registry.

## 5. Ownership and concurrency

Sole writer of owned paths during T0-8. Lead does not edit them concurrently.

## 6. Ordered tasks

1. Toolchain inventory: `node -v; npm -v; python3 --version; rustc --version; cargo --version; docker --version; git --version` — record each result or "not installed".
2. Create `.gitignore` (`.reference/`, `node_modules/`, `dist/`, `build/`, `target/`, `.env`, `.env.*`, `!.env.example`, `.DS_Store`, `coverage/`).
3. `git clone https://github.com/enginelabs-au/OrgOS.git .reference/orgos && git -C .reference/orgos checkout 8a843bd6429faf1ace5a9eb6dcfb7440703d34c4`; record `git -C .reference/orgos rev-parse HEAD`.
4. `npm ci` in the clone (fallback `--ignore-scripts`); `npm run build`; `npm run lint`; `npm run typecheck`; record exit codes and durations.
5. `npm run dev` in background; confirm `http://localhost:5173/cc-org-dash` responds; capture states per UI/UX capture plan into `docs/ui-blueprint/`; stop the dev server.
6. Complete `docs/blueprints/ui-blueprint.md`: commit, file inventory with sizes, launch commands, capture index, component inventory (from source), departures noted; preserve UI/UX sections.
7. Write `docs/capabilities.md`: header (schema, status vocabulary, transition rules from PM), 43 rows B01–B24, P01–P19, all `planned`, release bucket per PM, dependencies and interface components from intake; Hermes capability inventory placeholder table with version-pin note.
8. Write `docs/architecture.md`: Mermaid component diagram; entity list with ownership/retention/deletion; trust boundaries; data-destination map; Hermes adapter contract expectations table (runs, idempotency, events, stop, approval, capabilities, sessions, jobs, health) with documentation URLs; DBOS usage (workflows/steps/queues, Postgres system DB); Supabase self-host boundary; Compose topology; backup/restore approach; monorepo layout (D-01).
9. Write `docs/verification.md`: blueprint 13–18 → release-1 checks, method, evidence type, phase.
10. Draft `docs/decisions/2026-09-10-monorepo-layout.md` and `docs/decisions/2026-09-10-hermes-adapter-contract.md` (context, decision, alternatives, consequences, evidence).
11. Run validators: `node .cursor/skills/launch-pipeline/scripts/validate-launch.mjs`, `node .cursor/scripts/validate-agent-config.mjs`.
12. Write `evidence.md` and `handoff.md` with verdict.

Rollback: delete `.reference/orgos` if corrupted; remove partial docs if unusable; never touch protected files.

## 7. Tool and modality plan

Shell, file tools, Cursor IDE browser for screenshots, GitHub MCP read as fallback for source inventory.

## 8. Horizontal full-stack checklist

Product: reviewed. UI/UX: reviewed. Frontend/backend/data/API/integration: owned. Security/privacy: reviewed. Testing/observability: owned. Deployment/operations: reviewed. Analytics: reviewed. Documentation: owned.

## 9. Risk controls, rollback, and recovery

Third-party code executed only via documented npm scripts; no global installs; background dev server stopped after captures.

## 10. Validation steps and expected evidence

Per charter §9.

## 11. Outputs and storage paths

Per charter §3.

## 12. Gate criteria and downstream handoff

PASS/CONDITIONAL → `security-engineer-subagent`.

## 13. Deviations and plan change log

- r1 initial.

No deliverable-producing or state-changing action begins until the charter and this exhaustive plan are complete and consistent with the manifest.
