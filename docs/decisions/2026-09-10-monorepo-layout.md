# Decision D-01: Monorepo layout for Engine Labs release 1

## Status

`accepted` — owner-directed H-6 ratification 2026-09-11. Record: `docs/decisions/2026-09-11-owner-ratification-h6.md`. Drafted 2026-09-10 by `software-engineer-subagent` (T0-8).

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md` (§10 `provisional` assumption). Phase plan: `docs/plans/phase_0_foundations_plan.md` §7. Architecture: `docs/architecture.md` §3.

## Context

Engine Labs release 1 comprises a Tauri 2 desktop client (React/TypeScript/Vite, ported from the OrgOS `/cc-org-dash` reference), a FastAPI + DBOS API, a Hermes runtime adapter worker, shared typed contracts (OpenAPI → TS client, event and view-definition schemas, registry schema), and reproducible Docker Compose infrastructure for a single customer Droplet (intake Phase 04, Phase 07: "Scaffold the smallest coherent repository: desktop/UI, API, agent adapter boundary, shared contracts and deployment configuration"). The repository today contains only governance (`AGENTS.md`, `.cursor/`) and `docs/`; the phase 08 development loop binds *this* repository as the founder's development repository (manifest §10, OQ-1), so the layout must let agents make isolated changes with scoped checks across all components in one change set.

Phase-0 findings that shape the choice (SE evidence EV-S03–EV-S07): the reference shell has zero Tailwind/CSS-variable usage and imports only `react`/`react-dom`, so the UI can be a small self-contained package; the reference `tsc` run over JSX yields 328 errors, so the TSX port needs its own typed package rather than inheriting the reference config; Rust 1.84.1, Node 25.6.1, Python 3.11.9 and Docker 27.5.1 are present on the workstation.

## Decision

Adopt a single monorepo at the repository root with these top-level members:

| Path | Member | Language / tooling |
|---|---|---|
| `apps/desktop` | Tauri 2 desktop app (`src-tauri/` Rust core with `capabilities/*.json`; `src/` React 18 + TypeScript; Vite) | npm workspace member; cargo |
| `services/api` | FastAPI + DBOS Python API (app, migrations, tests) | Python project with lockfile |
| `services/worker` | Hermes runtime adapter, policy hooks, pinned Hermes gateway configuration (no secrets), execution sandbox definitions | Python project with lockfile |
| `packages/contracts` | Generated `openapi.json`, TypeScript client, zod schemas, run/notification event schemas, registry row schema (D-02) | npm workspace member |
| `packages/ui` | Ported primitives, icons, `THEMES` tokens (TSX) — added on the recommendation of `docs/ui-blueprint.md` §F | npm workspace member |
| `infra/` | Compose files and overrides, `.env.example` (names only), backup/restore scripts and runbook, `digests.lock` | shell, YAML |

Conventions: npm workspaces for JS/TS members; one lockfile per Python service; a root task runner (`Makefile` or `justfile`) exposing `dev`, `test`, `typecheck`, `lint`, `compose-up`; CI matrix per member with change-path filters; the `.reference/orgos/` clone stays git-ignored and is never imported by product code. Ownership boundaries for agent work are assigned per member path in phase plans (manifest §8).

## Alternatives considered

1. **Polyrepo (one repository per component).** Rejected: the phase 08 loop must bind one repository; cross-component changes (contract + API + desktop) would require multi-repo coordination and defeat the "isolated code change → tests → review → release proposal" single-change evidence chain (PRD-B.1, B.3).
2. **Frontend-only repository extending the OrgOS reference in place (Vite web app first, Tauri later).** Rejected: the intake requires Tauri 2 from phase 07 with signed releases and keychain storage (PRD-D.13, NFR-7); the reference's dependency tree (24 audit advisories, heavy unused libraries) would be inherited rather than pruned; `vercel.json` web deployment is not the target.
3. **Single Python package serving the built desktop bundle (no separate worker).** Rejected: the worker must be isolated from API credentials and production deployment credentials (PRD-B.10, E.6; architecture TB-3/TB-4); a separate member makes the boundary enforceable in Compose and CI.
4. **Nx/Turborepo/Bazel-style build orchestrator now.** Deferred: unnecessary for two npm members and two Python services in release 1; revisit when connector SDK/domain packs arrive (P19, R4).

## Consequences

- Positive: one change set can span contracts, API, worker, desktop and infra with a single PR, checks, review evidence and release proposal — exactly the loop release 1 must demonstrate (R1-ACC-6). Path-scoped ownership and CI filters keep the blast radius of agent changes bounded. `packages/ui` isolates the OrgOS port and its accessibility fixes from view logic, easing NFR-3 fidelity comparison.
- Negative / costs: mixed toolchains (npm, cargo, Python) in one repository require a root task runner and two lockfile ecosystems; Tauri builds need Rust and (for macOS signing) Apple tooling in CI; repository size grows with generated OpenAPI artifacts (mitigated by generating in CI and committing only the schema).
- Governance: the protected `.cursor/` control plane and `AGENTS.md` remain at the root, unchanged; `.gitignore` (created in T0-8) already covers `.reference/`, `node_modules/`, `dist/`, `target/`, `.env*` (except examples), `coverage/`.
- Follow-ups: phase-1 spike verifies Tauri 2 + Vite 6 + npm workspaces + `packages/ui` TSX imports; branch naming (`master` vs `main`) remains an owner decision (manifest §13); CI workflow in `.github/` is protected and owner-maintained.

## Evidence and citations

- Intake: `docs/Company_Agent_System_Blueprint.md` Phase 04 (stack table), Phase 07 (scaffold sentence), Phase 08 (repository binding).
- Manifest §10 `provisional` monorepo assumption; phase 0 plan §7.
- `docs/ui-blueprint.md` §F (dependency verdict; `packages/ui` targets), §0.5 (import scan: only `react`/`react-dom`).
- SE evidence: `docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/evidence.md` EV-S01 (toolchain), EV-S05/EV-S06 (build/lint/typecheck), EV-S07 (className/dependency scan), EV-S02 (`.gitignore`).
- Tauri 2 project structure (`src-tauri/`, `capabilities/`) — <https://v2.tauri.app/security/capabilities/> ("Configuration Files").
- DBOS Python + FastAPI packaging — <https://docs.dbos.dev/python/programming-guide>.
