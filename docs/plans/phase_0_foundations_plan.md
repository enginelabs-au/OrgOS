---
plan: phase_0_foundations
status: complete_conditional
created: 2026-09-10
updated: 2026-09-10
owner: lead-agent
source_phase: none
workstream: docs/workstreams/20260910-engine-labs-company-os/manifest.md
blueprint: docs/blueprints/2026-09-10_engine_labs.md
intake: docs/Company_Agent_System_Blueprint.md
---

# Phase 0: Foundations — Engine Labs company operating system

## 1. Objective

Convert the complete product intake into a verified, traceable planning foundation and the approved foundation checks that release 1 depends on: the workstream manifest, six role charters and plans, the strategy blueprint, the product contract, the 43-domain capability registry, the architecture and authority model, the UI blueprint captured from the pinned Papership reference, the roadmap, the verification index, governance policies, the environment-variable registry, and the deferred human-action queue — closing with a Project Lead gate and the exact prompt that generates `phase_1_foundation_plan.md`.

Phase 0 produces documentation, captured evidence, and read-only compatibility findings. It produces no application code and performs no external mutation.

## 2. Relation to project end-state

End-state (intake, "Final result"): a release-ready first version of Engine Labs where the founder signs in to the desktop client, plans work, runs persisted cloud jobs, reconnects to them, and completes a real Engine Labs change through the governed development loop; the full domain registry is visible with truthful statuses; commercial, connector, and mobile scope is planned and gated.

Phase 0 is the root of every later phase: it fixes requirement IDs, the registry schema, the authority model, the runtime-adapter contract expectations, the release map, and the role gates that phases 1–3 must satisfy. Nothing in later phases may introduce requirements that are not traceable to the intake, this plan, or a recorded decision.

## 3. Entry criteria and inherited evidence

- Preflight `MATERIALIZATION_REQUIRED`, `configuration.healthy: true` (2026-09-10).
- Fail-closed hook verified live (deliberate protected write denied, 2026-09-10).
- `bash .cursor/scripts/bootstrap.sh` exit 0 (agent config validation complete; launch validation 79 files).
- Workstream manifest: `docs/workstreams/20260910-engine-labs-company-os/manifest.md` (Tier 3; all six roles required).
- Strategy blueprint: `docs/blueprints/2026-09-10_engine_labs.md` (Build decision; validation experiments V1–V6).
- Reference inspection: `enginelabs-au/Papership` @ `8a843bd6429faf1ace5a9eb6dcfb7440703d34c4` (stack and file inventory recorded in `.cursor/STATE.md`).
- Primary documentation checked: Hermes API server, DBOS Python guide, Tauri 2 overview (links in blueprint §2).
- Prior decision: `docs/decisions/2026-08-18-agent-role-pipeline.md`.

## 4. Scope

Blueprint planning phases 01–06 in full, plus the approved foundation checks that can be executed without credentials:

- 01 Launch protocol compliance (this plan, manifest, state, memory).
- 02 Product definition and capability registry (`docs/product.md`, `docs/capabilities.md`).
- 03 Member experience and authority model (`docs/ui-blueprint.md`, design specification, permissions model).
- 04 Cloud architecture and connections (`docs/architecture.md`, connector contract, priority connections).
- 05 Agents, memory, lifecycle, commercial controls (`docs/product.md` runtime/memory/commercial sections, `docs/policies/`).
- 06 Release scope, dependencies, acceptance gates (`docs/roadmap.md`, `docs/verification.md`, this plan's §16–§17 registries, Next Plan Generation Prompt).
- Foundation checks: reference clone at the pinned commit, `npm ci`, run, capture; local toolchain availability for Tauri 2/Rust/Node/Python; Hermes and DBOS contract expectations recorded from documentation; monorepo layout decision.

## 5. Non-goals

- No application code, schema, Docker Compose, or infrastructure files (phase 1).
- No Hermes runtime installation with provider credentials (phase 1 spike with owner-supplied env var names populated by the owner).
- No repository commits, branches, pushes, or PRs (owner decision pending on versioning).
- No external accounts, DNS, billing, publishing, marketing posts, or spend.
- No changes to protected governance files.
- No implementation of blueprint phases 07–12.

## 6. Current-state audit

- Repository: fresh (`master`, zero commits). Contents: `AGENTS.md`, `.cursorignore`, `.github/workflows/agent-governance.yml`, `.cursor/` control plane (79 files, validated), `docs/Company_Agent_System_Blueprint.md`, `docs/handover/agent-governance-operator-setup.md`, `docs/decisions/2026-08-18-agent-role-pipeline.md`, bootstrap-seeded `docs/README.md`, `docs/plans/README.md`, `docs/workstreams/README.md`, plus the manifest and blueprint created in this phase.
- No `.gitignore`; no application toolchain files; no tests beyond the control-plane tests (17 pass).
- UI reference (remote, pinned): Vite 6 / React 18 JSX / Tailwind 3.4 / Radix-shadcn / react-router 6 / TanStack Query 5 / Stripe JS / recharts / framer-motion / three / leaflet; `npm run typecheck` = `tsc -p jsconfig.json` over JSX; `vercel.json` present (web deploy artefact, not needed for desktop). Routes: `/` → `/cc-org-dash`; legacy `Dashboard.jsx` (66 KB) and `Dashboard_new.jsx` (71 KB) reachable but not part of the shell. `src/components/cc-org-dash/` has 20 files (intake list plus `AuthPortal.jsx`, `WorkflowVis.jsx`, `useIsMobile.jsx`). `AuthContext.jsx` is a no-op dev stub; `entities.js` is localStorage CRUD for Integration, DashboardWidget, RosterEntry, ReportSnapshot, AIInsight.
- Tooling on the workstation: unknown until T0-7 checks (`node`, `npm`, `rustc`, `cargo`, `python3`, `docker`).
- Governance: hooks live; sandbox network allowlist limited to GitHub/npm/Vercel/Supabase hosts for sandboxed shell; agent web tools used for other documentation.

## 7. Assumptions, constraints, risks, and decisions

Assumptions (labelled):

- `verified` — bootstrap, preflight, hook, and reference reachability as in §3.
- `provisional` — Agent-mode `/launch-pipeline` plus declined Plan Mode is implementation authorization for phase 0 documentation and later local implementation; owner may revoke at any gate.
- `provisional` — Monorepo layout: `apps/desktop` (Tauri 2 + React/TS), `services/api` (FastAPI + DBOS), `services/worker` (Hermes adapter/policy), `packages/contracts` (OpenAPI/types), `infra/` (Compose, backup, ops). Fixed as a decision at the end of phase 0 unless the SE spike contradicts it.
- `provisional` — Reference clone lives at `.reference/orgos/` and is git-ignored via a new root `.gitignore` (not a protected file); captured screenshots live under `docs/ui-blueprint/`.
- `provisional` — The founder's development repository bound in phase 2 is this repository.
- `provisional` — Default branch stays `master` until the owner decides; CI workflow targets `main`.

Constraints: fail-closed policy; no secrets in files; read-only specialists; single parent materializes shared files; Tier 3 gates; no production inference.

Risks specific to phase 0: reference capture may require a display server (mitigation: headless Chromium screenshots via the IDE browser tool or Playwright if available; otherwise record the limitation); toolchain absent (record; owner action queued); documentation drift for Hermes (record fetch date and version string).

Decisions to record in `docs/decisions/` during phase 0: D-01 monorepo layout; D-02 registry schema and status vocabulary; D-03 authority model (three seats, server-side checks, source-permission intersection); D-04 Hermes adapter contract expectations (runs API, idempotency, SSE, stop, approval, capabilities); D-05 release-1 scope boundary (07+08 only).

## 8. Dependencies

- Internal order: manifest → blueprint → this plan → docs index → charters/plans → PM → UI/UX → SE → Security → Growth → PL.
- External (read-only): GitHub access to the reference repository; public documentation for Hermes, DBOS, Tauri, Supabase self-hosting, DigitalOcean.
- Workstation toolchain for T0-7/T0-8 (Node ≥ 18 for the reference; Rust toolchain for Tauri prerequisites check).
- No credentials required in phase 0.

## 9. Architecture and affected systems

Documentation-only phase. Systems described (not built): desktop (Tauri 2), API (FastAPI + DBOS on Postgres), data/identity (self-hosted Supabase), execution (Hermes workers behind adapter/policy), retrieval (Postgres), deployment (Compose on Droplet), operations (logs/traces/backups). The architecture document must include a component diagram (Mermaid), the entity model, trust boundaries, data-destination map, and the adapter contract expectations table.

## 10. Files and paths in scope

Create or update:

- `docs/README.md` (index links)
- `docs/workstreams/20260910-engine-labs-company-os/manifest.md`
- `docs/workstreams/20260910-engine-labs-company-os/<role-id>/{charter,plan,evidence,handoff}.md` for all six roles
- `docs/blueprints/2026-09-10_engine_labs.md`
- `docs/plans/phase_0_foundations_plan.md` (this file)
- `docs/product.md`, `docs/capabilities.md`, `docs/architecture.md`, `docs/ui-blueprint.md`, `docs/ui-blueprint/` (captures), `docs/roadmap.md`, `docs/verification.md`
- `docs/policies/{authority-model,data-residency-and-retention,memory-governance,erasure-and-offboarding,licensing}.md`
- `docs/decisions/2026-09-10-*.md` (D-01…D-06)
- `.gitignore` (new; ignores `.reference/`, `node_modules/`, build outputs, `.env*` except examples)
- `.reference/orgos/` (clone, ignored)
- `.cursor/STATE.md`, `.cursor/memory/MEMORY.md`, `.cursor/memory/memories/2026-09-10-continuation.md`

Read-only: `docs/Company_Agent_System_Blueprint.md`, `.cursor/instructions/**`, `.cursor/agents/**`, `.cursor/templates/**`, remote reference repository.

## 11. Supporting documents to create or update

Listed in §10. Each product document carries a header linking the intake, the blueprint, this plan, and the owning role handoff. Naming: `docs/<topic>.md` as named in the intake (`product.md`, `capabilities.md`, `architecture.md`, `ui-blueprint.md`, `roadmap.md`, `verification.md`, `policies/`).

## 12. Ordered implementation tasks

Each task lists objective, dependencies, exact files/systems, notes, validation evidence, completion state.

**T0-1 Manifest** — objective: create the workstream manifest with Tier 3 classification and six required roles. Deps: bootstrap. Files: manifest. Validation: file exists, all roles present, requirement table populated. State: `complete` (2026-09-10).

**T0-2 Strategy blueprint** — objective: evidence-based Build decision per STRATEGY.md. Deps: T0-1, reference inspection, documentation checks. Files: `docs/blueprints/2026-09-10_engine_labs.md`. Validation: 17 sections present; sources cited; limitations recorded. State: `complete` (2026-09-10).

**T0-3 Phase 0 plan** — this file. Deps: T0-2. Validation: all 22 template sections populated; env-var registry has names only; Next Plan Generation Prompt present. State: `complete` on write; `verified` at PL gate.

**T0-4 Docs index** — objective: link intake, blueprint, plan, manifest, product docs from `docs/README.md`. Deps: T0-3. Validation: links resolve. State: `complete` (2026-09-10).

**T0-5 Role charters and plans** — objective: six charters + six plans from templates, each with owned paths, non-goals, requirement coverage, gate criteria, predecessor. Deps: T0-3. Files: role dirs. Validation: every charter linked from manifest §5; no role executes before its charter/plan exist. State: `complete` (2026-09-10).

**T0-6 Product Manager gate** — objective: product contract: requirement IDs PRD-A…G with acceptance criteria, seat templates, release-1 acceptance definition, registry row schema, commercial tier definitions (no prices), success metrics taxonomy inputs. Deps: T0-5. Method: Task delegation to `product-manager-subagent` (read-only); lead materializes `evidence.md`, `handoff.md`, and `docs/product.md`. Validation: handoff verdict PASS/CONDITIONAL with cited evidence; every intake requirement mapped. State: `complete` (2026-09-10; CONDITIONAL 16:00Z).

**T0-7 UI/UX gate** — objective: experience specification for the seven core views; adaptive-view rules; seat-specific flows; accessibility and responsive states; migration notes from Papership components; screenshot capture plan. Deps: T0-6. Method: Task delegation to `ui-ux-developer-subagent` (read-only, may read the remote reference via GitHub MCP); lead materializes handoff and `docs/ui-blueprint.md` skeleton. Validation: every core view specified with states; departures from reference justified. State: `complete` (2026-09-10; CONDITIONAL 16:31Z).

**T0-8 Software Engineer foundation checks** — objective: (a) toolchain check (`node -v`, `npm -v`, `rustc --version`, `cargo --version`, `python3 --version`, `docker --version`) recorded; (b) root `.gitignore`; (c) clone reference at pinned SHA into `.reference/orgos/`, `npm ci`, `npm run build`, `npm run dev` and capture `/cc-org-dash` states into `docs/ui-blueprint/`; (d) `docs/ui-blueprint.md` completed (commit, file list, launch commands, captured states, component inventory); (e) `docs/capabilities.md` with all 43 domain rows (`planned`) per D-02 schema; (f) `docs/architecture.md` with diagram, entities, trust boundaries, data-destination map, Hermes adapter contract expectations table with documentation citations, DBOS/Supabase/Compose notes; (g) `docs/verification.md` index mapping blueprint 13–18 to release-1 checks; (h) D-01 and D-04 decision records drafted. Deps: T0-7. Method: Task delegation to `software-engineer-subagent` (writable within owned paths). Validation: commands and exit codes recorded in evidence; captures exist; registry row count = 43; documents lint-clean Markdown. State: `complete` (2026-09-10; CONDITIONAL 17:05Z; captures closed by lead 17:20Z, EV-S16).

**T0-9 Security gate** — objective: threat model (STRIDE or equivalent) for release-1 architecture; authority-model review (D-03); data-destination and retention review; agent tool side-effect and prompt-injection controls; secrets handling; supply-chain baseline (lockfiles, dependency licence inventory plan); findings with severity and required remediation before phase 1. Deps: T0-8. Method: Task delegation to `security-engineer-subagent` (read-only); lead materializes handoff and `docs/policies/*` from findings and intake. Validation: no unresolved blocking finding; policies exist. State: `complete` (2026-09-10; CONDITIONAL 17:58Z; five `proposed` policies).

**T0-10 Growth gate** — objective: positioning statement, value hypothesis and validation thresholds review (V4/V5), measurement taxonomy (task completion, correctness, recovery, intervention, context switching, cost per outcome), event naming conventions for release-1 usage measurement, tier communication principles (no prices), consent/ethics constraints. Deps: T0-9. Method: Task delegation to `growth-marketing-subagent` (read-only); lead materializes handoff and `docs/roadmap.md` commercial sections. Validation: no fabricated baselines; taxonomy traceable to PRD. State: `complete` (2026-09-10; CONDITIONAL 17:58Z).

**T0-11 Roadmap** — objective: `docs/roadmap.md` mapping blueprint phases → execution plans → releases, with gates, dependencies, and deferred human actions. Deps: T0-6…T0-10. Method: lead. Validation: every blueprint phase appears once with release and plan. State: `complete` (2026-09-10; 18/18 phases; D-02/D-03/D-05/D-06 drafted).

**T0-12 Project Lead gate** — objective: reconcile all handoffs, traceability, plan/state consistency, residual risks; phase 0 verdict; confirm the Next Plan Generation Prompt is executable. Deps: T0-11. Method: Task delegation to `project-lead-subagent` (read-only); lead materializes handoff. Validation: verdict PASS or CONDITIONAL with bounded items. State: `complete — CONDITIONAL` (2026-09-10T18:22Z).

**T0-13 State and memory reconciliation** — objective: `.cursor/STATE.md`, `MEMORY.md` durable links, continuation log, decisions D-01…D-06 reconciled (ratification is an owner action H-6); PL §13 deltas applied. Deps: T0-12. Validation: preflight `mode_hint` reflects active plan; validators pass. State: `in_progress` (2026-09-10T18:30Z).

## 13. Adaptive role and delegation map

| Role ID | Required or skipped | Reason | Predecessor | Owned paths | Gate evidence | Status |
|---|---|---|---|---|---|---|
| `product-manager-subagent` | required | New product contract, registry schema, seats, tiers, metrics inputs | lead (T0-1…T0-5) | read-only; lead materializes `product-manager-subagent/*`, `docs/product.md` | `product-manager-subagent/handoff.md` PASS/CONDITIONAL | CONDITIONAL (2026-09-10T16:00Z) |
| `ui-ux-developer-subagent` | required | Seven-view design spec, adaptive views, accessibility, Papership migration notes | PM | read-only; lead materializes `ui-ux-developer-subagent/*`, `docs/ui-blueprint.md` skeleton | `ui-ux-developer-subagent/handoff.md` | CONDITIONAL (2026-09-10T16:31Z) |
| `software-engineer-subagent` | required | Foundation checks, reference capture, registry, architecture, verification index | UI/UX | `.gitignore`, `.reference/`, `docs/ui-blueprint*`, `docs/capabilities.md`, `docs/architecture.md`, `docs/verification.md`, `docs/decisions/2026-09-10-{monorepo-layout,hermes-adapter-contract}.md`, `software-engineer-subagent/*` | `software-engineer-subagent/handoff.md` with commands/exit codes | CONDITIONAL (2026-09-10T17:05Z; captures closed 17:20Z) |
| `security-engineer-subagent` | required | Tier 3 mandatory: threat model, authority, data, agent side effects, supply chain | SE | read-only; lead materializes `security-engineer-subagent/*`, `docs/policies/*` | `security-engineer-subagent/handoff.md`; no open blocking finding | CONDITIONAL (2026-09-10T17:58Z) |
| `growth-marketing-subagent` | required | Positioning, thresholds, measurement taxonomy, tier communication, ethics | Security | read-only; lead materializes `growth-marketing-subagent/*`, `docs/roadmap.md` commercial sections | `growth-marketing-subagent/handoff.md` | CONDITIONAL (2026-09-10T17:58Z) |
| `project-lead-subagent` | required | Always for Tier 1–4; phase gate and reconciliation | Growth | read-only; lead materializes `project-lead-subagent/*` | `project-lead-subagent/handoff.md` phase 0 verdict | CONDITIONAL (2026-09-10T18:22Z) |

## 14. Test and validation matrix

| Requirement | Validation method | Expected evidence | Status |
|---|---|---|---|
| REQ-01 launch protocol | preflight, bootstrap, validators, tests | JSON outputs; `bootstrap-exit=0`; 17 tests pass | complete (phase 0; PL EV-PL01) |
| REQ-02 product + registry | PM handoff review; row count check on `docs/capabilities.md` | 43 rows with all schema columns; PRD IDs mapped | complete (phase 0; PL EV-PL04) |
| REQ-03 experience + authority | UI/UX handoff; Security authority review; capture inventory | seven views specified; `docs/ui-blueprint/` captures; D-03 | complete (phase 0; PL EV-PL05/EV-PL08) |
| REQ-04 architecture + connections | Architecture doc review vs documentation citations; Security boundary review | diagram, entities, adapter contract table, connector contract | complete (phase 0 design; C-02 fix phase 1) |
| REQ-05 agents/memory/lifecycle/commercial | PM + Security + Growth handoffs; policies present | `docs/policies/*`; retention defaults; tier definitions without prices | complete (phase 0; PL EV-PL03/EV-PL07) |
| REQ-06 release scope + gates | Roadmap and this plan; PL reconciliation | phase → plan → release map; env-var names; human-action queue; next prompt | complete (phase 0; PL EV-PL09/13/14) |
| Foundation checks | SE evidence with exact commands and exit codes | toolchain versions; `npm ci`/`build` exit codes; captures | complete (EV-S01…EV-S16) |

## 15. Security, privacy, reliability, accessibility, and performance checks

- Security: threat model and authority review (T0-9); no secrets in any file (grep for common secret patterns before PL gate); `.gitignore` covers `.env*`; reference clone is untrusted third-party code — do not execute anything beyond documented `npm ci`/`npm run dev|build`; note that `npm ci` runs lifecycle scripts of pinned dependencies (record `npm ci --ignore-scripts` fallback if the owner prefers).
- Privacy: no personal data in workstream files; screenshots contain only reference sample data.
- Reliability: recovery model and idempotency expectations documented for phase 1 (D-04).
- Accessibility: design spec includes keyboard, focus, contrast, reduced-motion, and screen-reader states for the seven views.
- Performance: none measured in phase 0; targets set from pilot baseline (V4/V6).

## 16. Environment-variable registry

Never include values. Names are proposals for phase 1; the owner supplies values only in the runtime environment.

| Variable name | Purpose | Scope/environment | Required by phase | Source/provider | Status |
|---|---|---|---|---|---|
| `ENGINE_API_BASE_URL` | Desktop → API base URL | desktop | 1 | Engine Labs | planned |
| `ENGINE_API_CORS_ORIGINS` | Allowed desktop origins | api | 1 | Engine Labs | planned |
| `ENGINE_JWT_ISSUER` / `ENGINE_JWT_AUDIENCE` | Token validation parameters | api | 1 | Supabase Auth | planned |
| `DBOS_SYSTEM_DATABASE_URL` | DBOS checkpoint database (Postgres) | api, worker | 1 | self-hosted Postgres | planned |
| `DATABASE_URL` | Application database | api | 1 | self-hosted Postgres | planned |
| `SUPABASE_URL` | Supabase API URL | api, desktop | 1 | self-hosted Supabase | planned |
| `SUPABASE_ANON_KEY` | Public client key | desktop | 1 | self-hosted Supabase | planned |
| `SUPABASE_SERVICE_ROLE_KEY` | Server-side privileged key (never on desktop) | api | 1 | self-hosted Supabase | planned |
| `SUPABASE_JWT_SECRET` | Token signing/verification | api | 1 | self-hosted Supabase | planned |
| `POSTGRES_PASSWORD` | Database superuser password (Compose) | infra | 1 | owner | planned |
| `HERMES_API_BASE_URL` | Hermes API server base (private network) | worker/api | 2 | Hermes | planned |
| `HERMES_API_SERVER_KEY` | Bearer key for Hermes API server (`API_SERVER_KEY` on the Hermes side) | worker/api | 2 | Hermes | planned |
| `HERMES_VERSION_PIN` | Pinned Hermes release/commit | worker | 2 | Engine Labs | planned |
| `MODEL_PROVIDER_API_KEY` (per provider, named on selection) | Model access for Hermes | worker | 2 | provider | planned |
| `GITHUB_APP_ID` / `GITHUB_APP_INSTALLATION_ID` / `GITHUB_APP_PRIVATE_KEY_PATH` | Scoped repository automation | api/worker | 2 | GitHub | planned |
| `BACKUP_TARGET_URL` / `BACKUP_ENCRYPTION_KEY_PATH` | Encrypted off-VPS backups | infra | 3 | owner | planned |
| `DIGITALOCEAN_API_TOKEN` | Droplet provisioning automation (owner/CI only) | ci | 3 | DigitalOcean | planned |
| `TAURI_SIGNING_PRIVATE_KEY` / `TAURI_SIGNING_PRIVATE_KEY_PASSWORD` | Update signing | ci | 3 | Engine Labs | planned |
| `APPLE_ID` / `APPLE_TEAM_ID` / `APPLE_APP_SPECIFIC_PASSWORD` | macOS notarization | ci | 3 | Apple | planned |
| `SENTRY_DSN` or equivalent | Error reporting (if adopted) | api, desktop | 3 | provider | optional |

## 17. Deferred human-action queue

Record actions but do not request them unless they are strict blockers.

| Action | Why agent cannot perform it | Earliest required phase | Blocking now? | Final-checklist destination |
|---|---|---|---|---|
| Decide default branch (`master` vs `main`) and update CI trigger if `master` | Governance/CI choice; workflow file is protected | before first push | no | yes |
| Decide whether to commit the control plane and docs | Versioning policy | before first push | no | yes |
| Confirm the founder development repository for phase 08 (this repo assumed) | Owner knowledge | 2 | no | yes |
| Install/confirm Rust toolchain, Xcode CLT, Node ≥ 18, Python ≥ 3.11, Docker on the workstation if absent | Local machine administration | 1 | no (recorded by T0-8) | yes |
| Provision model provider account and set `MODEL_PROVIDER_API_KEY` | Credentials/spend | 2 | no | yes |
| Provision DigitalOcean account/Droplet; set tokens | Spend/infrastructure authority | 3 | no | yes |
| Create GitHub App for scoped repository automation | Owner account authority | 2 | no | yes |
| Apple developer account for signing/notarization | Owner account/spend | 3 | no | yes |
| Gmail OAuth scope review, Telegram/Slack/WhatsApp developer registrations | Provider terms | release 2 | no | yes |
| Approve any publication of go-to-market drafts | Owner-only | release 2+ | no | yes |
| Ratify D-01…D-06 and adopt the five proposed policies via decision records (H-6) | Owner policy authority | phase-0 gate / before phase-1 token file and phase-2 plan | no | yes |
| Answer OQ-5 (R1 view set); acknowledge D-3 (`#617083`) and D-11 (default theme) | Product/design decision | before phase-1 plan (default recorded) | no | yes |
| H-2 pin GitHub Actions by SHA; enable Dependabot | Protected workflow file | 1 | no | yes |
| H-3 branch protection on product repositories | Owner account authority | 1 | no | yes |
| H-4 record model-provider data-use terms (DRR-06) | Legal/commercial | 2 | no | yes |
| H-5 verify Hermes licence for commercial self-hosted use (LIC-05) | Legal | before phase-2 spike | no | yes |
| H-7 provision CI signing secrets (`TAURI_SIGNING_PRIVATE_KEY`, `TAURI_SIGNING_PRIVATE_KEY_PASSWORD`, `APPLE_ID`, `APPLE_TEAM_ID`, `APPLE_APP_SPECIFIC_PASSWORD`) in a protected environment — names only | Credentials | 3 | no | yes |
| OQ-G2 member measurement notice / legal basis | Legal | R2 | no | yes |
| OQ-G1 public build-log appetite (record only) | Owner preference | R2 | no | yes |
| OQ-4 tier labels; two separate decisions to publish rates and activate charges (CA-10) | Commercial | R4 | no | yes |

## 18. Rollback and recovery

Phase 0 changes are documentation and an ignored reference clone. Rollback = delete created files under `docs/` (except pre-existing), `.gitignore`, `.reference/`, and restore `.cursor/STATE.md` from the continuation log. No external state to recover. If a role gate fails, return to the owning role with the finding; do not proceed downstream.

## 19. Acceptance criteria

- Manifest, blueprint, this plan, docs index, six charters, six plans exist and are consistent.
- Six handoffs materialized with supported verdicts; no BLOCKED verdict outstanding.
- `docs/product.md`, `docs/capabilities.md` (43 rows), `docs/architecture.md`, `docs/ui-blueprint.md` (+ captures or recorded limitation), `docs/roadmap.md`, `docs/verification.md`, `docs/policies/*` exist and cross-link.
- Decisions D-01…D-06 recorded.
- Env-var names and human-action queue complete; no secret values anywhere.
- Validators pass: `node .cursor/skills/launch-pipeline/scripts/preflight.mjs`, `node --test .cursor/skills/launch-pipeline/scripts/preflight.test.mjs .cursor/hooks/policy.test.mjs`, `node .cursor/skills/launch-pipeline/scripts/validate-launch.mjs`, `node .cursor/scripts/validate-agent-config.mjs`.
- `.cursor/STATE.md` reflects reality; continuation log appended; PL verdict recorded.

## 20. Completion evidence

To be appended as tasks complete (commands, exit codes, file paths, handoff verdicts).

- T0-1…T0-3: manifest, `docs/blueprints/2026-09-10_engine_labs.md`, this plan (2026-09-10; `bash .cursor/scripts/bootstrap.sh` exit 0).
- T0-4: `docs/README.md` "Engine Labs" section; 17/17 links resolve (PL EV-PL07, 2026-09-10T18:19Z).
- T0-5: six charters + six plans under `docs/workstreams/20260910-engine-labs-company-os/<role>/` (PL EV-PL06).
- T0-6: PM CONDITIONAL 2026-09-10T16:00Z → `docs/product.md` (PRD-A…G, NFR-1..10, R1-ACC-1..15, OQ-1..6).
- T0-7: UI/UX CONDITIONAL 16:31Z → `docs/ui-blueprint.md` §A–§H (seven views × eight states; 52-state capture plan; D-1..D-11; OQ-U1..U4).
- T0-8: SE CONDITIONAL 17:05Z → `.gitignore`; `.reference/orgos/` @ 8a843bd6 (`npm ci` 0, build 0, lint 1, typecheck 2); `docs/capabilities.md` 43 rows; `docs/architecture.md`; `docs/verification.md`; D-01/D-04. Captures closed by lead 17:20Z: 122 PNGs / 52 states (EV-S16).
- T0-9: Security CONDITIONAL 17:58Z → 19 findings (3 high, all phase-1 gated), STRIDE T-01…T-58, five `proposed` policies, GM-1…12, H-1…H-7; hygiene scan exit 1.
- T0-10: Growth CONDITIONAL 17:58Z → taxonomy 9 rows, 18 event families, `domain.object.action`, CA-1…10, F-G1; price scan exit 1.
- T0-11: `docs/roadmap.md` (18/18 phases mapped once; G0–G4; §5 Security gates; §6 human actions); D-02/D-03/D-05/D-06 `proposed`.
- T0-12: PL CONDITIONAL 2026-09-10T18:22Z — validators: preflight READY exit 0; validate-launch 79 files exit 0; validate-agent-config exit 0; `node --test` 17/17; hygiene exit 1; price scan exit 1; registry 43/`planned` 43 (19/4/14/6); 122 PNGs; roadmap 18/18; C-01…C-16 recorded; verdict and deltas in `project-lead-subagent/handoff.md`.
- T0-13: PL §13 deltas applied to manifest, this plan, `docs/verification.md`, STATE, continuation, MEMORY (2026-09-10T18:30Z); validator re-run recorded in the continuation log.

- T0-1: `docs/workstreams/20260910-engine-labs-company-os/manifest.md` written 2026-09-10.
- T0-2: `docs/blueprints/2026-09-10_engine_labs.md` written 2026-09-10.
- T0-3: this file written 2026-09-10.

## 21. Deviations and follow-ups

- Plan Mode was declined by the owner; the pre-Build plan was delivered inline and this phase proceeds under recorded Agent-mode authorization.
- T0-8 captures were completed by the lead (not the SE role) because the IDE browser tool cannot reach loopback here; method recorded in `docs/ui-blueprint.md` §0.4 and EV-S16.
- T0-12 recorded sixteen consistency items (C-01…C-16), all non-blocking and reconciled in T0-13 or carried to phase 1; D-06 added beyond the five decisions planned in §7.

## 22. Next Plan Generation Prompt

Read `/AGENTS.md`, the complete core agent context, `/instructions/PROJECT_PLANNING.md`, `/instructions/ROLES.md`, the original `docs/plans/phase_0_foundations_plan.md`, this completed phase plan, the active workstream manifest `docs/workstreams/20260910-engine-labs-company-os/manifest.md` and all six role handoffs, all completion evidence, `docs/blueprints/2026-09-10_engine_labs.md`, `docs/product.md`, `docs/capabilities.md`, `docs/architecture.md`, `docs/ui-blueprint.md`, `docs/roadmap.md`, `docs/verification.md`, `docs/policies/`, decisions D-01…D-06, `docs/roadmap.md` §5 Security gates and the phase-1 carry list in `docs/workstreams/20260910-engine-labs-company-os/project-lead-subagent/handoff.md` §11, current repository state, active blockers, and relevant decisions. Confirm this phase and every required role gate are fully implemented and validated. Then generate exactly one exhaustive next phase plan at `docs/plans/phase_1_foundation_plan.md` covering blueprint implementation phase 07 (Foundation: desktop shell from the Papership reference inside Tauri 2, cloud API and data boundary, identity and owner seat, grant checks, capability registry service, work ledger, job persistence with DBOS, streamed status, secure desktop connection, reconnect/resume) plus the applicable verification gates from phases 13–18. Derive it from the phase-0 roadmap and verified current state, preserve unresolved requirements, include all required plan sections and adaptive role decisions, defer non-blocking human actions to the final phase, and do not implement the next phase until the plan is written.
