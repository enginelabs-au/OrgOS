---
plan: phase_3_release_verification
status: complete
created: 2026-09-11
updated: 2026-09-11
owner: lead-agent
source_phase: docs/plans/phase_2_development_loop_plan.md
predecessor_gate: G2 CONDITIONAL (2026-09-11)
workstream: docs/workstreams/20260910-engine-labs-company-os/manifest.md
blueprint: docs/blueprints/2026-09-10_engine_labs.md
intake: docs/blueprints/company_agent_system_blueprint.md (Phases 13–18)
release: R1 (D-05); gate G3
risk_tier: tier_3
---

# Phase 3: Release verification — Engine Labs / Papership

Generated after Phase 2 G2 CONDITIONAL (2026-09-11). Do **not** start live Hermes tool execution until Security PASS on a real API server. Papership UI remains `apps/web` `/cc-org-dash` and `apps/desktop`. Do not edit `www.enginelabs.com.au`.

## 1. Objective

Apply intake verification phases 13–18 to the enabled R1 scope: prove or honestly mark the development loop, authority, recovery, desktop fidelity, usage, and owner handoff. Close Phase 2 residuals that block G2→G3 (live Hermes API server, live intercept, one real loop change, AUTH-12 fail-closed, image digests).

## 2. Relation to the end-state

Phase 2 built the loop substrate (ledger stages, adapter, catalogued tools behind policy, persisted assistant sessions, GitHub dry-run). Phase 3 is the first release verification pass (G3). It does not start R2 collaboration or commercial delivery. After G3, generate the owner checklist / handoff — not phase 4 — until the owner approves R1 closure.

## 3. Entry criteria and inherited evidence

- Phase 2 `complete_conditional`. Worker 24 / API 41 tests passed.
- D-17 catalog enablement. Security T2-2 CONDITIONAL ([re-review](25fe9df8-506d-44a6-92ef-3abfd466e5eb)).
- AUTH-25 startup (artefact sha256 `390b166c…594e72`) verified. Live intercept **not** cleared.
- Hermes pin may still be `hermes serve` (login UI). `blocked_runtime` is the only allowed live outcome until a new Security PASS.
- GitHub App exists; live PR still opt-in dry-run default.
- Usage emit still off (T2-9 / F-G1).
- G1 CONDITIONAL inherited (Compose live, packaged Tauri).

## 4. Scope

- Deploy or confirm a Hermes **HTTP API server** (not only `hermes serve`) on the worker network.
- Wire intercept on every tool event; fail-closed write receipts; external = approval then receipt.
- One real Papership change through the 11-stage loop with receipts (R1-ACC-6), dry-run first then owner-opt-in live PR.
- AUTH-12: refuse live PR when installation permissions are empty.
- Verification index `docs/verification.md` for R1 rows → VERIFIED / PARTIAL / NOT_APPLICABLE with evidence.
- Desktop fidelity / a11y pass vs ui-blueprint (phase 16 subset).
- Fixture erasure + backup restore **drill design** (execute only if backup target exists).
- Owner handoff draft for G4. No prices. No marketing-site edits.

## 5. Non-goals

- No production DNS, billing, publish, or Apple signing unless the owner supplies accounts.
- No R2 seats, Inbox connectors, Memory manager build, adaptive views, or mobile clients.
- No enabling registry `working` without demonstrated live workflow.
- No wake-word vendor.
- No second phase-4 plan until G3 + owner.

## 6. Assumptions, constraints, risks, decisions

- `verified` (2026-09-11): Hermes HTTP API listens on VPS `127.0.0.1:8642` via the existing gateway unit. Tunnel + Papership default URL retargeted. GET `/health` hangs; HEAD 405 is the reachability signal.
- Risk: public-HTTPS research residual (D-17, owner-accepted).
- Constraint: worker-only `HERMES_API_SERVER_KEY`; API/desktop never read it.
- D-17/D-18 stand. D-16 follow-up (“keep disabled”) remains superseded.

## 7. Dependencies

Order: T3-1 close Security binding items that are code-only → T3-2 live API server (owner) → Security PASS → T3-3 live loop demo → T3-4 verification index → T3-5 desktop/a11y → T3-6 usage first-baseline if F-G1 on → T3-7 PL G3 → owner handoff (not phase 4).

## 8. Files and systems

`services/worker/` (hooks on tool events), `services/api/` (AUTH-12 fail-closed), `apps/desktop/`, `docs/verification.md`, `infra/digests.lock`, workstream `phase-3-*` files. No Engine Labs marketing project.

## 9. Supporting documents

Update `docs/verification.md` states. New Security phase-3 handoff. `docs/handover/phase-3-owner-actions.md` if human actions accumulate.

## 10. Ordered implementation tasks

**T3-1 Code residuals (no live Hermes tools)** — require persist_receipt for write; persist approval before receipt for external; API already maps serve-UI → `blocked_runtime`; refuse live PR when installation perms `{}`; bind yaml/catalog hashes in startup. Deps: this plan.

**T3-2 Hermes API server** — owner/ops: listen documented `/v1/runs` (not login UI). Inventory `GET /v1/capabilities` + `/v1/toolsets`. Digest in `infra/digests.lock`. Deps: T3-1; owner.

**T3-3 Security PASS for live runs** — re-review after T3-2. Do not set runtime `accepted` before PASS.

**T3-4 R1-ACC-6 loop demo** — one work item through 11 stages; isolated branch; checks; review evidence; release **proposal** only. Interrupt/restart trial (V15-3).

**T3-5 Verification index 13–18** — fill `docs/verification.md` for enabled R1 rows.

**T3-6 Desktop / a11y** — Hey Engine session states, Work loop stepper, contrast D-06, tab order F-S7.

**T3-7 Usage first-baseline** — only if owner accepts F-G1 emit; else `not_captured`.

**T3-8 Role gates + G3** — SE, Security, UI/UX, PM, Growth (metrics only), PL.

**T3-9 Owner handoff** — G4 package. Generate `docs/plans/final_implementation_checklist.md` only if this is treated as R1 closure; otherwise wait for owner.

## 11. Adaptive role matrix

| Role ID | Required or skipped | Reason | Status |
|---|---|---|---|
| software-engineer-subagent | required | T3-1, T3-4, tests | CONDITIONAL |
| security-engineer-subagent | required | T3-3 live PASS | CONDITIONAL (accepted forbidden; r3) |
| ui-ux-developer-subagent | required | T3-6 fidelity/a11y | CONDITIONAL |
| product-manager-subagent | required | R1-ACC-6…9 acceptance | CONDITIONAL (PARTIAL) |
| growth-marketing-subagent | required | first-baseline / no prices | CONDITIONAL (`not_captured`) |
| project-lead-subagent | required | G3 | PASS-with-residuals |

## 12. Test and validation matrix

| ID | Method | Phase 3 target |
|---|---|---|
| V13-5 / R1-ACC-6 | one real change | VERIFIED or recorded blocker |
| V15-3 | kill/restart | zero duplicate external effects |
| AUTH-12 | pytest + live installation | fail-closed empty perms |
| AUTH-25 live | Security PASS | required before `accepted` |
| V16 | desktop screenshots vs blueprint | PARTIAL ok if listed |
| V17 | usage events | `not_captured` unless F-G1 |

## 13. Security / privacy / reliability

Carry F-T21-SEC-02/03, F-T22-SEC-01/02/05/06/12, latent F-SEC-01. Public-HTTPS residual stays owner-accepted. No secrets in files.

## 14. Environment-variable names

Already wired: `HERMES_API_BASE_URL`, `HERMES_VERSION_PIN`, `HERMES_API_SERVER_KEY` (worker only), `GITHUB_APP_*`. Phase 3 may add digest pin name in `infra/digests.lock` only.

## 15. Deferred human actions

| Action | Blocking live ACC-6? |
|---|---|
| Hermes HTTP API server (not login UI) | yes |
| Live PR `dry_run: false` + reauth | yes for publication |
| F-G1 usage emit accept | no |
| Docker Compose live + backup target | no for code; yes for V15 backup |
| Apple signing / DigitalOcean | no (packaging) |
| Wake-word vendor | no |

## 16. Rollback

Set `interception_verified: false` and disable toolsets; worker refuse-start. Jobs already persisted stay. No production to roll back.

## 17. Acceptance (G3)

Verification index updated; Security PASS **or** explicit NOT_APPLICABLE on live-run rows with residual recorded; one loop demo or a recorded owner blocker; no prices; no secrets; desktop a11y regressions listed; owner handoff prepared.

## 18. Completion evidence

- Worker 30 / API 47 (2026-09-11T13:10Z).
- Live Papership `GET /health`: `hermes=reachable`, `github=reachable`, `usage_emit=false`, pin `v0.21.1`.
- G3: `docs/workstreams/20260910-engine-labs-company-os/project-lead-subagent/phase-3-g3-handoff.md` (PASS-with-residuals).
- Owner handoff: `docs/workstreams/20260910-engine-labs-company-os/delivery/owner-handoff.md`.
- Checklist: `docs/plans/final_implementation_checklist.md`.
- Owner actions: `docs/handover/phase-3-owner-actions.md`.

## 19. Deviations

Entered from G2 CONDITIONAL, not PASS. Phase 3 must not pretend R1-ACC-6 already happened.

## 20. Next Plan Generation Prompt

Read `/AGENTS.md`, core context, `/instructions/PROJECT_PLANNING.md`, `/instructions/ROLES.md`, `docs/plans/phase_0_foundations_plan.md`, this completed plan, phase-2 plan, workstream handoffs, `docs/roadmap.md` G4, `docs/verification.md`. Confirm G3. Then either generate `docs/plans/final_implementation_checklist.md` (R1 closure) or, only after owner approval for R2, `docs/plans/phase_4_collaboration_connections_plan.md`. Do not implement the next phase until that file exists.

Executed 2026-09-11: owner asked for Phase 4 planning (D-19). G3 remains CONDITIONAL. Plan written at `docs/plans/phase_4_collaboration_connections_plan.md`. R1 checklist not generated.
