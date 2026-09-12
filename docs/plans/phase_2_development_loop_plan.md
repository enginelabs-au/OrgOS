---
plan: phase_2_development_loop
status: complete_conditional
created: 2026-09-11
updated: 2026-09-11
owner: lead-agent
source_phase: docs/plans/phase_1_foundation_plan.md
predecessor_gate: docs/workstreams/20260910-engine-labs-company-os/project-lead-subagent/phase-1-handoff.md (CONDITIONAL)
workstream: docs/workstreams/20260910-engine-labs-company-os/manifest.md
blueprint: docs/blueprints/2026-09-10_engine_labs.md
intake: docs/blueprints/company_agent_system_blueprint.md (Phase 08 — Development loop)
release: R1 (D-05); gate G2
risk_tier: tier_3
---

# Phase 2: Development loop — Engine Labs

Generated after G1 CONDITIONAL (2026-09-11). Activated 2026-09-11 by owner request. **Start at T2-1 (SP-1…SP-7) only. Do not enable side-effecting Hermes tools until Security re-review.** Papership web UI is `apps/web` from `docs/ui-blueprint`. Do not treat Engine Labs marketing as this product.

## 1. Objective

Build intake implementation phase 08: a pinned Hermes runtime behind the D-04 adapter, with interception spike SP-1…SP-7 and Security re-review **before any side-effecting toolset is enabled**; bind this repository through a scoped GitHub App; run the governed loop (request → research → specification → plan → assignment → isolated change → tests → review → release proposal); connect the assistant / Hey Engine button to backend-mediated Hermes sessions; persist conversations; show run status, scope, usage, budget, pause/cancel and recovery; contract-test runtime, source-control and action boundaries; prove zero duplicated external effects under restart.

## 2. Relation to project end-state

Phase 1 delivered the substrate (identity, grants, ledger, jobs, desktop shell, fail-closed worker). Phase 2 binds Hermes and GitHub so the founder can complete a real Engine Labs change (R1-ACC-6…9). Phase 3 verifies and packages.

## 3. Entry criteria and inherited evidence

- G1 CONDITIONAL: `bash scripts/ci.sh` exit 0; 12 registry rows `configured`; 0 `working`.
- Worker refuse-to-start if a side-effecting toolset is enabled without artefact+hash (AUTH-25).
- Usage emit off until owner accepts F-G1.
- Owner supplied H-4/H-5 (D-11): OpenRouter terms accepted; Hermes v0.21.1 commercial self-host accepted; pin `v0.21.1`. GitHub App values still owner-created (T2-3). No `MODEL_PROVIDER_API_KEY` in Papership.
- Venue: local or Cloud UI; Cloud Task from the prior Mac session failed (blocker may persist).

## 4. Scope

- SP-1…SP-7 interception spike + Security re-review (first tasks).
- Pin Hermes; adapter implements D-04 operations; no browser calls Hermes.
- GitHub App: `repo.branch` / `repo.change` / `repo.check` / `repo.release` intersection with installation scopes (AUTH-12). Plan/open client is already on the API (`GET`/`POST /github/pulls`, dry-run default). Live open still opt-in after T2-1.
- Loop stages as ledger transitions with timestamps.
- Isolated branches/worktrees; checks; review evidence; release **proposal** only (execute_release remains designated authority).
- `GlobalAgentPanel` / Hey Engine: authenticated API sessions; honest errors; user-equivalent actions under AUTH-07; **no** grant bypass via voice/button.
- Wake-word spike: specify desktop entitlement + on-device vs cloud speech; do not ship a vendor without an owner decision.
- Contract tests at runtime, source-control, and action boundaries.
- Registry updates by lead only with evidence.

## 5. Non-goals

- No production, DNS, billing, prices, publish.
- No additional connectors beyond GitHub.
- No mobile wake word.
- No enabling side-effecting tools before SP-1…SP-7 PASS and Security re-review.
- No second phase-3 plan until this phase is verified.

## 6. Current-state audit

Monorepo exists (`apps/desktop`, `services/api`, `services/worker`, `packages/{ui,contracts}`, `infra/`). Worker has no Hermes client. Desktop Hey Engine opens `unavailable`. Jobs persist in sqlite/file store; DBOS package not imported. Compose files exist; stack not started in G1.

## 7. Assumptions, constraints, risks, and decisions

- `provisional`: OQ-1 this repository is the bound repo.
- Risk: interception mechanism unknown until spike (architecture §14).
- Risk: Cloud/local Docker gaps persist.
- Constraint: fail-closed worker; no secrets in files.

Decisions to draft: interception mechanism; Hermes image digest; GitHub App permission set; wake-word approach (specify only).

## 8. Dependencies

Order: T2-1 spike → Security gate → Hermes pin + adapter → GitHub binding → loop stages → assistant sessions → contract tests → demo R1-ACC-6…9 → role gates → G2 → generate phase 3 plan only.

## 9. Architecture and affected systems

`docs/architecture.md` §7 adapter; §8 DBOS (import for real workflows); worker + Hermes on `worker` network only (D-08). Desktop talks only to API.

## 10. Files and paths in scope

`services/worker/adapter/`, `services/worker/hermes/`, `services/api/` (GitHub action service, sessions), `apps/desktop/src/assistant/`, `packages/contracts/`, `infra/`, workstream `phase-2-*` files. No protected governance files.

## 11. Supporting documents

Update architecture §7 with chosen interception; capabilities statuses (lead); verification V15/V13-5; new decisions as needed.

## 12. Ordered implementation tasks

**T2-1 SP-1…SP-7 interception spike** — State: `implemented` (D-16 then D-17). Security T2-1 CONDITIONAL.

**T2-2 Hermes pin + adapter** — State: `implemented`. D-04 client + `start_run`; `blocked_runtime` without API server. Security T2-2 CONDITIONAL ([re-review](25fe9df8-506d-44a6-92ef-3abfd466e5eb)).

**T2-3 GitHub App binding** — State: `implemented` (unit AUTH-12 intersection). Live open still opt-in + reauth.

**T2-4 Loop ledger stages** — State: `implemented` (`POST /work-items/{id}/stage`, 11 stages).

**T2-5 Isolated change + checks** — State: `partial`. Dry-run PR client exists; live isolated change not demonstrated.

**T2-6 Assistant / Hey Engine runtime** — State: `implemented`. Sessions persisted; no invented model replies.

**T2-7 Wake-word spike (specify)** — State: `implemented` (`docs/decisions/2026-09-11-wake-word-spike.md`). Not shipped.

**T2-8 Interruption / idempotency trials** — State: `partial`. Persist-before-202 and receipt uniqueness unit-tested; live Hermes kill trial not run.

**T2-9 Usage emit (if F-G1 accepted)** — State: `deferred`. Flag remains off.

**T2-10 Role gates + G2** — SE CONDITIONAL; Security T2-2 CONDITIONAL; UI/UX skipped (no new chrome); PM skipped (R1-ACC-6 not live); Growth skipped (no emit); PL CONDITIONAL G2.

**T2-11 Reconciliation** — State: `implemented`. `docs/plans/phase_3_release_verification_plan.md`.

## 13. Adaptive role and delegation map

| Role ID | Required or skipped | Reason | Predecessor | Owned paths | Gate evidence | Status |
|---|---|---|---|---|---|---|
| software-engineer-subagent | required | T2-1…T2-8 | this plan | apps/services/packages | phase-2-handoff.md | CONDITIONAL |
| security-engineer-subagent | required | D-17 re-review | SE | none | phase-2-t2-2-handoff.md | CONDITIONAL |
| ui-ux-developer-subagent | skipped | No new chrome; Hey Engine uses existing panel | T2-6 | none | skip — assistant copy only | skipped |
| product-manager-subagent | skipped | Live R1-ACC-6 not demonstrated; carried to phase 3 | Security | none | skip | skipped |
| growth-marketing-subagent | skipped | Usage emit still off; no prices added | PM | none | skip | skipped |
| project-lead-subagent | required | G2 CONDITIONAL + phase 3 prompt | Security | none | this plan §20 | CONDITIONAL |

## 14. Test and validation matrix

| Requirement | Method | Evidence | Status |
|---|---|---|---|
| SP-1…SP-7 | spike + Security | T2-1/T2-2 handoffs | CONDITIONAL |
| R1-ACC-6 | one real change | work item + PR | pending — phase 3 |
| V15-3 | kill/restart | unit persist/receipt | PARTIAL |
| AUTH-12 | grant ∩ installation | `test_github_grants.py` | PARTIAL (empty perms fail-open) |
| AUTH-07 | assistant ≤ user grants | session 403 unpriv | PARTIAL |

## 15. Security, privacy, reliability, accessibility, and performance checks

Same as phase 1 plus interception, GitHub token scoping, session isolation, prompt-injection on untrusted repo content (F-SEC-13 remainder).

## 16. Environment-variable registry

Names only. Phase-2 rows become `wired` when added to `.env.example` and allowlists: `HERMES_VERSION_PIN`, `HERMES_API_BASE_URL` (internal), worker transport key **name**, `GITHUB_APP_ID`, `GITHUB_APP_INSTALLATION_ID`, `GITHUB_APP_PRIVATE_KEY` (file path name), `MODEL_PROVIDER_API_KEY` (worker only). Values never committed.

## 17. Deferred human-action queue

| Action | Why agent cannot | Earliest | Blocking now? |
|---|---|---|---|
| H-4 provider terms | recorded D-11 | T2-2 | no |
| H-5 Hermes licence | recorded D-11 | T2-2 | no |
| GitHub App create/install | owner dashboard | T2-3 | no for spike; yes for live git loop |
| H-6 ratify D-01…D-08 | owner | G2 exit | no for T2-1 |
| Wake-word vendor | spend/privacy | later | no |

## 18. Rollback and recovery

Disable all side-effecting toolsets; worker fail-closed. `docker compose down`. Leave phase-1 API usable.

## 19. Acceptance criteria (G2)

SP-1…SP-7 passed Security; one real loop change with receipts; zero duplicate external effects; GitHub intersection; assistant sessions persisted; registry truthful; no prices; no secrets in files; phase 3 plan written only after G2.

## 20. Completion evidence

- 2026-09-11 owner authorized maximum catalogued tools with policy (D-17).
- Worker 24 passed; API 41 passed.
- Security T2-2 CONDITIONAL ([re-review](25fe9df8-506d-44a6-92ef-3abfd466e5eb)).
- G2 **CONDITIONAL**: loop substrate implemented; live Hermes run and live ACC-6 deferred to phase 3.
- Next plan written.

## 21. Deviations and follow-ups

D-16 “keep disabled” superseded by D-17. Live API server still missing. T2-9 emit off. T2-5 live PR not opened. Inherited: Cloud launch; DBOS not imported.

## 22. Next Plan Generation Prompt

Read `/AGENTS.md`, core context, `/instructions/PROJECT_PLANNING.md`, `/instructions/ROLES.md`, this completed plan, phase-0 and phase-1 plans, all handoffs, `docs/roadmap.md` G3, `docs/verification.md`. Confirm G2 and every required role gate. Then generate exactly one plan at `docs/plans/phase_3_release_verification_plan.md` covering intake verification phases 13–18 for the enabled R1 scope. Do not implement it until written.
