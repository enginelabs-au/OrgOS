---
document: verification
title: Engine Labs — Verification Index (blueprint phases 13–18 → release-1 checks)
status: r2_configured
revision: 5
created: 2026-09-10
updated: 2026-09-12
owner_role: software-engineer-subagent (index skeleton, T0-8); results owned by project-lead-subagent with all roles (REQ-13..18)
task_id: 20260910-engine-labs-company-os
intake: docs/Company_Agent_System_Blueprint.md (Phases 13–18)
product: docs/product.md (§9 R1-ACC-1..15, NFR-9, PRD-C.6)
phase_plan: docs/plans/phase_0_foundations_plan.md (§14, §19, T0-8 item g)
manifest: docs/workstreams/20260910-engine-labs-company-os/manifest.md (REQ-06, REQ-13..18)
architecture: docs/architecture.md
registry: docs/capabilities.md
---

# Engine Labs — Verification Index

Purpose: one index that maps every intake verification phase (13–18) to the concrete release-1 checks, the method, the evidence type, and the phase/plan in which the check runs and is recorded (intake Phase 13: "Index results in docs/verification.md and retain detailed evidence in the active workstream"). Evidence states are `VERIFIED` / `PARTIAL` / `UNVERIFIED` / `NOT_APPLICABLE` and are distinct from role-gate verdicts (NFR-9). Checks for capabilities not enabled in release 1 are `NOT_APPLICABLE` for R1 but stay listed (I-13: "mark future-feature checks not applicable without deferring mandatory controls for current use").

Coverage metric (PRD-C.6): count of `working` registry rows per release — R1 baseline is recorded here at release closure. At registry version `0.1.2-phase4` (2026-09-12): 0 `working`, 16 `configured` (prior 12 plus B02.01, B12.01, B23.01, P07.01), 27 `planned`, 0 `unavailable`. Gmail/Slack are `configured` as deny-by-default contracts, not live OAuth.

## 1. Phase 13 — Functional and domain coverage

| ID | Release-1 check | Method | Evidence type | Runs in (phase / plan) | R1 state |
|---|---|---|---|---|---|
| V13-1 | Every enabled capability traces requirement → registry row → implementation → configuration → acceptance check | Traceability table generated from `docs/capabilities.md` + PRD IDs + code paths | Table with links (NFR-9) | Phase 3 / `phase_3_verification_plan.md` (PL) | PARTIAL (`software-engineer-subagent/artifacts/t3-v13-1-traceability.md`; 12 configured, B08.01 planned, 0 working) |
| V13-2 | Registry keeps all 43 groups; deferred rows remain `planned`; no reference screen or fixture counted | `rg -c` row count = 43; status audit; static scan for `data.jsx`/`entities.js` imports in production paths | Command output; scan report | Every phase gate; final in phase 3 | PARTIAL (phase 1: 43 rows; 12 `configured` with evidence; no `working`; desktop scan 0 fixtures) |
| V13-3 | Launcher verification: preflight, `node --test` preflight/policy tests, `validate-agent-config.mjs`, `validate-launch.mjs`; blueprint linked from intake, phase 0, manifest, state; fresh `/launch-pipeline` reads requirements, asks only unresolved questions, preserves Build/bootstrap boundary; later invocation resumes recorded gate | Run the four commands; inspect links; two Cursor-session trials recorded separately from static checks | JSON/exit codes; session transcripts | Phase 0 (static) → phase 3 (session evidence) | PARTIAL (phase 0 validators — EV-S14; PL re-run 2026-09-10T18:17:57Z: all four pass, EV-PL01) |
| V13-4 | Complete operator workflows with realistic scoped data, including missing information and failed dependencies | Scripted walkthrough (Founder seat) per R1-ACC-2, R1-ACC-13 | Walkthrough log + screenshots | Phase 3 | PARTIAL (web Home `/cc-org-dash` 2026-09-11; Settings/Work clicks blocked by fail-closed MCP hook) |
| V13-5 | Development loop from request to reviewed change and release rehearsal in a test environment; links/status/artifacts refer to actual records and code version | Execute one real Engine Labs change (R1-ACC-6); verify SHA links | Work-item chain; PR; check results; release proposal record | Phase 2 (demonstration) → phase 3 (verification) | PARTIAL (`test_r1_acc6_walks_all_loop_stages`; live PR https://github.com/enginelabs-au/OrgOS/pull/1 via `open_pull` `dry_run: false`; `execute_release` not run) |
| V13-6 | Unsupported integrations and untested paths reported accurately; mock/visible control never counts as connection | Registry `unavailable`/`planned` audit vs connector health | Registry diff; health log | Phase 3 | PARTIAL (live `/health` hermes+github reachable; extra connectors stay planned; Hermes `accepted` only for catalogued read `tool=`) |
| V13-7 | Defects routed to owning role; invalidated downstream gates recorded and replayed; blocking security findings independently re-verified | Manifest §11 remediation table review | Manifest + handoffs | Every gate | PARTIAL (process in place; no defects yet) |

## 2. Phase 14 — Authority, memory, and data lifecycle

| ID | Release-1 check | Method | Evidence type | Runs in | R1 state |
|---|---|---|---|---|---|
| V14-1 | Isolation across pages, queries, aggregates, notifications, exports, files, agent tools, memory for a second identity / request lacking a grant (R1-ACC-4, PRD-D.5) | Authorization test suite hitting each surface with an unprivileged principal | Test output (pytest) with exit codes | Phase 1 (tests) → phase 3 | PARTIAL (`test_authz.py` five surfaces + memory; 21 API tests exit 0) |
| V14-2 | Separate organisations, roles, project scopes, guest assignments; delegated grant ≤ delegator; billing upgrade creates no data permission | Multi-tenant fixtures; delegation tests; entitlement/permission separation test (PRD-D.6 R1 part) | Test output | Phase 1 (tenant + entitlement separation); R2 for delegation/guests | PARTIAL — R2 guest refuse + seat templates verified (`test_phase4.py`); live second human not issued |
| V14-3 | Revoked credentials, changed assignments, expired approvals, modified action targets → running/queued work rechecks authority (PRD-D.12, D.10) | Fault injection mid-run; approval invalidation test | Run log; audit entries | Phase 2 → phase 3 | VERIFIED (`test_voided_approval_blocks_job_step`, `test_revoked_grant_blocks_queued_job_step`; API 47 passed) |
| V14-4 | Setup access removed at handover (application, cloud, SSH) | Handover checklist + post-handover access test | Checklist record | R2 (PRD-D.8) | NOT_APPLICABLE R1 |
| V14-5 | Memory: source restrictions, correction propagation, archive ownership, offboarding, export, erasure with disposable fixtures; summaries/indexes/caches follow deletion; backup/provider retention disclosed | R1: search/inspect + provenance fields + credential-exclusion scan (PRD-F.2, F.4); R3/R4: full operations and erasure | Test output; scan | Phase 1–2 (R1 subset) → R3/R4 | PARTIAL — R3 operations + restriction + scan verified (`test_phase5.py`); org-wide erasure and backup disclosure remain R4 |

## 3. Phase 15 — Integrations, recovery, and backups

| ID | Release-1 check | Method | Evidence type | Runs in | R1 state |
|---|---|---|---|---|---|
| V15-1 | Bound repository connector: actual authentication, permitted operations (four grant classes), source permissions, refresh/revocation, stale data, unsupported actions | Contract tests at the source-control boundary (PRD-B.7, R1-ACC-9) | Test output | Phase 2 | PARTIAL (live `/health` `github: reachable`; AUTH-12 empty-perms refuse; live PR #1 opened; `execute_release` not run) |
| V15-2 | Webhook authentication and duplicate-event handling | GitHub check-run webhook tests (if webhooks used in R1) | Test output | Phase 2 | NOT_APPLICABLE R1 (no webhook receiver; list/open are on-demand) |
| V15-3 | Interrupt worker and network before/after a potential external write; recovery reconciles source outcome; no duplicated effects (R1-ACC-5, PRD-E.7) | Interruption harness (kill worker, drop network) around a GitHub write; Hermes `Idempotency-Key` replay assertion (architecture §7) | Interruption log; receipt reconciliation | Phase 2 → phase 3 | PARTIAL (persist-before-202 + dual `/runs` unit-tested; live VPS kill/restart of a side-effecting write not run) |
| V15-4 | Cancellation, desktop disconnection, budget exhaustion, diagnostic limits (2 retries + 1 diagnostic), escalation when new authority needed (PRD-E.8) | Fault-injection runs | Run events; incident + escalation records | Phase 2 → phase 3 | PARTIAL (`test_cancel_vs_disconnect`; budget/diagnostic live limits not run) |
| V15-5 | Restore encrypted backup from client-controlled location into isolated environment; verify integrity, key access, permissions, external reconciliation; measure RTO/RPO vs accepted targets; snapshot inventory and retention/deletion procedures | Restore drill per architecture §11 | Drill report | Phase 3 dry run (scripts); full drill R4 | UNVERIFIED (R1 dry run), NOT_APPLICABLE (full drill) |
| V15-6 | Runtime boundary contract tests (Hermes adapter): capabilities probe, idempotent run creation, SSE detach/reattach, stop, approval, session isolation, usage dedupe, concurrency cap | Adapter contract test suite (architecture §7 last column) | Test output vs pinned `HERMES_VERSION_PIN` | Phase 2 | PARTIAL (HEAD-first probe; capabilities prove `api_server`; live `accepted` for catalogued read `memory_read` `run_ee41560dd3ee46eb9bef3fcd6615e6ba`; subscribe/job loop still idle) |

## 4. Phase 16 — Desktop and adaptive experience

| ID | Release-1 check | Method | Evidence type | Runs in | R1 state |
|---|---|---|---|---|---|
| V16-1 | Desktop installation, sign-in, secure token handling (keychain), progress streaming, reconnect, notifications, cancellation, signed update on macOS (R1-ACC-1, 3) | Native platform run (packaged app); keychain inspection; update signature check | Screenshots; logs; `security` CLI output | Phase 1 (sign-in, streaming), phase 3 (packaged, signed) | UNVERIFIED |
| V16-2 | Screens compared with the recorded `/cc-org-dash` reference at matching viewports/themes: layout, typography, spacing, colours, primary tabs, command rail, assistant panel, overlays, responsive behaviour; intentional departures (ui-blueprint §H) recorded; baseline refreshed only by explicit reference update | Screenshot comparison against `docs/ui-blueprint/` captures (§G plan) | Image pairs + diff notes | Phase 0 captures (complete — see §7) → phase 3 comparison | PARTIAL (Home snapshot 2026-09-11; full 52-state diff not re-run) |
| V16-3 | Production screens use real permissions, persisted records and agent events (PRD-A.16) | Static scan: no `data.jsx`/`entities.js`/localStorage fixtures in production imports; runtime check | Scan output | Phase 1 → phase 3 | PARTIAL (desktop `tests/*.test.mjs` exit 0; runtime against live API not run) |
| V16-4 | Keyboard navigation, focus, accessible labels, contrast, responsive layout, readable empty/error states (NFR-2; ui-blueprint §E) | axe/pa11y run + manual keyboard walkthrough; contrast tool report (phase-0 computed ratios in ui-blueprint §0.6 are the baseline) | Accessibility report | Phase 1 (components) → phase 3 | PARTIAL (closed Hey Engine unmounts; Work `aria-current`; no axe; Cursor browser click hook-blocked) |
| V16-5 | Operator completes routine work without technical traces or special prompting; compare Founder/PL/Operator scopes enabled | Founder walkthrough R1; PL/Operator R2 | Walkthrough log | Phase 3 (Founder) ; R2 | PARTIAL scope |
| V16-6 | Adaptive views: stable controls, permitted data, valid schemas, pinning, undo, fallback; completion time vs fixed views; within design system | — | — | R3 | PARTIAL — schema/fallback/pin/undo/reset API (`test_phase5.py`); screenshot-diff and usability timing not run |

## 5. Phase 17 — Usage, deployment, and commercial operations

| ID | Release-1 check | Method | Evidence type | Runs in | R1 state |
|---|---|---|---|---|---|
| V17-1 | Usage records per run (tokens by model band, tool calls, execution time, estimated cost) and run budgets exist; operational monitoring (logs, traces, health, cost metrics) present (PRD-G.11, NFR-5, R1-ACC-12) | Ledger sample; monitoring inspection | Ledger rows; dashboards/log samples | Phase 1–2 → phase 3 | PARTIAL (schema wired; F-G1 emit on after owner close-out; identifier/enum only; no prices) |
| V17-2 | Paid-tier checks: entitlements, model-band allowances, seat changes, reservations, graduated rates, limit enforcement, provider reconciliation in billing test mode; repeated events cannot duplicate charges | pytest reservation/duplicate/charge-disabled | `test_phase6.py` | R4 (phase 11 gate) | PARTIAL (structure + test-mode; no published rates; no charges; CA-10 still owner) |
| V17-3 | Exhausted allowance pauses new chargeable work while preserving records, exports, decisions | pytest exhausted band | `test_exhausted_band_pauses_new_work` | R4 | PARTIAL (band enum; records still readable; no live charge) |
| V17-4 | Clean deployment, supported upgrades, migration recovery, monitoring, alerts, support-access expiry | Compose bring-up in a test environment; migration up/down; alert test | Deployment log | Phase 3 (test environment only; production is owner/CI) | PARTIAL (`docker compose -f infra/compose/docker-compose.yml config --quiet` exit 0; stack not brought up) |
| V17-5 | Capacity and cost under realistic concurrency measured before VPS sizing (NFR-6) | Resource measurement report | Report | Phase 1 (dev) → phase 3 | UNVERIFIED |
| V17-6 | Connectors and distributed dependencies satisfy commercial-access and licence requirements; dependency licence inventory (PRD-G.9) | Licence inventory generation (`license-checker`/`pip-licenses`) | Inventory file | Phase 1 → phase 3 | PARTIAL (`artifacts/t3-licence-inventory.md`; no machine SPDX dump) |

## 6. Phase 18 — Release readiness and owner handoff

| ID | Release-1 check | Method | Evidence type | Runs in | R1 state |
|---|---|---|---|---|---|
| V18-1 | Results from 13–17 consolidated against the exact release commit, configuration and enabled capability set; evidence reused only when code/deps/environment unchanged | PL reconciliation | Consolidated table with commit SHA | Phase 3 | PARTIAL (this index r3 + HEAD `7d1af36`; working tree includes Phase 3 close) |
| V18-2 | All mandatory checks pass; six role verdicts reconciled; open high/critical security findings keep `BLOCKED` | Manifest §5/§11 review | Manifest | Phase 3 | PARTIAL (no BLOCKED; Security live-tools CONDITIONAL allows catalogued-read `accepted`) |
| V18-3 | Residual limitations, blocked scope, deferred capabilities, migration/rollback procedures, operational ownership recorded; missing credentials/policies/platform evidence never recorded as passed | Handoff document review | `delivery/owner-handoff.md` | Phase 3 | VERIFIED (`docs/workstreams/20260910-engine-labs-company-os/delivery/owner-handoff.md`) |
| V18-4 | `docs/plans/final_implementation_checklist.md` created from template with remaining defects, env-var names and sources, human-only actions, production prerequisites | File exists and matches template | File | Phase 3 | VERIFIED (`docs/plans/final_implementation_checklist.md`) |
| V18-5 | Owner decision `APPROVE` / `REQUEST_CHANGES` / `DO_NOT_PROCEED` recorded (not inferred) (R1-ACC-15) | Owner response captured in handoff | Handoff record | Phase 3 closure | VERIFIED (owner APPROVE 2026-09-11; `delivery/owner-handoff.md`) |
| V18-6 | Versioned release artifacts and permitted owner/CI deployment procedure prepared; implemented/verified/ready/deployed/owner-approved states distinguished | Release notes + procedure review | Artifacts + procedure | Phase 3 | PARTIAL (handoff + checklist; not deployed) |

## 6b. Release 2 residuals (Phase 4)

| ID | Check | Evidence | State |
|---|---|---|---|
| R2-SEATS | Three + guest templates; OQ-G2 gates invite | `test_seats.py`, `test_phase4.py::test_invite_without_oq_g2_is_forbidden` | VERIFIED |
| R2-WIZARD | GitHub truthful; others planned | `GET /connections`, blueprint-2 Integrations overlay | VERIFIED (contract) |
| R2-INTERSECT | Empty source perms refuse live write | `intersect_source_grants`; `POST /grants/intersect` | VERIFIED |
| R2-B12 | Unknown provider deny; send needs approval | `test_connection_wizard_and_unknown_provider`, `test_send_needs_approval_and_intersection` | VERIFIED (dry-run) |
| R2-P07 | GitHub checkpoint after list | `test_github_checkpoint_after_list` | VERIFIED |
| R2-B23 | Guest create refused until OQ-G2 | `test_guest_refused_until_oq_g2` | VERIFIED |
| R2-UI | People/Inbox not fixture-auth | `apps/web/src/api/papership.js` + empty InboxView | VERIFIED (unauthenticated empty) |
| R2-WORKER | Queued job consumer + subscribe receipt | `services/worker/jobs.py`, `tests/test_jobs.py` | VERIFIED (unit) |
| R2-USAGE | first-baseline `not_captured` if zero events | `GET/POST /usage/baseline` | VERIFIED |
| R2-LIVE-OAUTH | Gmail/Slack live enablement | owner credentials missing | NOT_APPLICABLE until owner apps |
| R2-PRICES | No prices in UI/docs | CA-10 still closed | VERIFIED (D-29 labels only) |

## 6c. Release 3 residuals (Phase 5)

| ID | Check | Evidence | State |
|---|---|---|---|
| R3-MEM | Eight PRD-F.3 operations; restriction hides derived; credential scan | `test_phase5.py::test_memory_eight_operations_and_credential_scan` | VERIFIED (fixtures) |
| R3-MEM-UI | Memory manager honest empty / API rows | `apps/web/src/api/papership.js`, `MemoryView` | VERIFIED (overlay; browser click-through not run) |
| R3-ADAPT | AUTH-29 fallback; pin/undo/reset; personalisation off | `test_adaptive_views_fallback_pin_undo_reset`, `test_personalisation_off_refuses_apply` | VERIFIED (API) |
| R3-B01 | Native strategy; KPI `not_captured` | `test_strategy_kpis_not_captured` | VERIFIED |
| R3-B03 | Native capacity; no HR OAuth | `test_capacity_native_not_hr` | VERIFIED |
| R3-SHELLS | Other R3 domains deny live write | `test_r3_shells_deny_live_write` | VERIFIED |
| R3-P08 | Canonical refs; no invented metrics | `GET /references` | VERIFIED |
| R3-P05 | Automate schedules `configured`; no external fire | `test_references_and_schedules_configured` | VERIFIED |
| R3-HERMES | No write/external `accepted` lift | D-25 residual | VERIFIED (unchanged) |
| R3-PRICES | No prices | CA-10 | VERIFIED |

## 7. Phase-0 evidence index (produced so far)

| Role | Evidence file | Records | Handoff verdict | Notes |
|---|---|---|---|---|
| `product-manager-subagent` | `docs/workstreams/20260910-engine-labs-company-os/product-manager-subagent/evidence.md` | EV-01 … EV-12 | CONDITIONAL (2026-09-10T16:00Z) | Product contract, registry schema D-02, 43-domain buckets (`docs/product.md`) |
| `ui-ux-developer-subagent` | `docs/workstreams/20260910-engine-labs-company-os/ui-ux-developer-subagent/evidence.md` | EV-U01 … EV-U12 | CONDITIONAL (2026-09-10T16:31Z) | Seven-view spec, migration map, 52-state capture plan (`docs/ui-blueprint.md` §A–§H); EV-U08 contrast PARTIAL → verified by EV-S08; EV-U09 InboxScreen PARTIAL → verified by EV-S07 |
| `software-engineer-subagent` | `docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/evidence.md` | EV-S01 … EV-S16 | CONDITIONAL (2026-09-10T17:05Z; captures closed 17:20Z) | Toolchain inventory, `.gitignore`, clone at pinned SHA, `npm ci`/build/lint/typecheck results, dev-server probe, contrast ratios, className/dependency scans, registry (43 rows), architecture, this index, D-01/D-04, validators; EV-S16 `[lead]`: 52/52 states, 122 PNGs captured via `docs/ui-blueprint/capture.mjs` |
| `security-engineer-subagent` | `docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/evidence.md` | EV-SEC-01 … EV-SEC-14 | CONDITIONAL (2026-09-10T17:58Z) | STRIDE model T-01…T-58 over TB-1…TB-13; 19 findings (3 high with phase-1 gates: F-SEC-01 interception/approval wrap, F-SEC-02 public exposure, F-SEC-04 approval grants); hygiene scan clean (rg exit 1; re-run by lead 17:52Z); five `proposed` policies in `docs/policies/`; Growth constraints GM-1…GM-12; owner actions H-1…H-7 |
| `growth-marketing-subagent` | `docs/workstreams/20260910-engine-labs-company-os/growth-marketing-subagent/evidence.md` | EV-G01 … EV-G15 | CONDITIONAL (2026-09-10T17:58Z) | Taxonomy 9 rows; 18 event families; `domain.object.action`; GM-1…GM-12 adopted (lead-verified in handoff and `docs/roadmap.md`); price scan clean on `docs/roadmap.md` (rg exit 1, 18:13Z); F-G1 Security schema review phase 1; positioning DRAFT until R1-ACC-3/6/7/8 |
| `project-lead-subagent` | CONDITIONAL (2026-09-10T18:22Z) | `project-lead-subagent/handoff.md` | EV-PL01…EV-PL16 | Owns this index from phase 3; phase-0 gate CONDITIONAL, C-01…C-16 reconciled or carried |

Capture status for V16-2: `docs/ui-blueprint/` contains 122 PNGs covering all 52 §G states (captured 2026-09-10T17:15Z by the lead with headless host Chrome via `docs/ui-blueprint/capture.mjs`; index and method in ui-blueprint §0.4). The reference dev server and browser were stopped afterwards; agents must not run the reference dev server again (LIC-12/LIC-13) — re-capture in phase 16 targets the Engine Labs shell.

## 8. Maintenance rules

- Add a row whenever a phase plan introduces a check; never delete rows — change the state and add the evidence link.
- Each `VERIFIED` state must link an evidence record with command, exit code and commit SHA.
- `NOT_APPLICABLE` requires the release in which it becomes applicable.
- The PL updates the coverage metric (§ preamble) at each release closure from `docs/capabilities.md`.
