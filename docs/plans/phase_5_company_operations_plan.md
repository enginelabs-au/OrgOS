---
plan: phase_5_company_operations
status: draft
created: 2026-09-12
updated: 2026-09-12
owner: lead-agent
source_phase: docs/plans/phase_4_collaboration_connections_plan.md
predecessor_gate: G5 PASS (2026-09-12); D-27…D-31
workstream: docs/workstreams/20260910-engine-labs-company-os/manifest.md
blueprint: docs/blueprints/2026-09-10_engine_labs.md
intake: docs/Company_Agent_System_Blueprint.md (Phase 10)
release: R3 (accepted D-28); gate G7 implementation / G8 owner
risk_tier: tier_3
---

# Phase 5: Company operations — Engine Labs / Papership

Generated after Phase 4 G5 PASS. Owner authorized this **plan** (D-31). **Do not implement until this file exists and a later turn starts T5-0.** Papership UI remains `docs/ui-blueprint/blueprint-2` at `/cc-org-dash`. Do not edit `www.enginelabs.com.au`.

## 1. Objective

Build intake Phase 10 (company operations) for R3: a governed memory manager (PRD-A.15 B.6 / PRD-F.3), adaptive views (PRD-A.11 / P16 / AUTH-29), personalisation inspect/disable/reset (PRD-A.12 / MEM-19), and the first business domains named in D-27 — **B01** native goals/initiatives/decisions and **B03** native people/capacity. Remaining R3 registry rows stay discoverable as deny-by-default catalogue shells. No invented KPI, usage, or price figures.

## 2. Relation to the project end-state

Phases 0–4 closed the foundation, development loop, R1 verification, and R2 seats/connections. R3 is the first company-operations slice: members can manage retained knowledge, adapt chrome from trusted definitions, and keep strategy and capacity as native records. It does not start R4 billing, entitlements, mobile, or the connector SDK. After G7, generate exactly one next plan: `docs/plans/phase_6_commercial_delivery_plan.md`. Two execution phase plans remain after this phase (6 and 7). Verification phases 13–18 re-run at R3 close; they are not extra build phases.

## 3. Entry criteria and inherited evidence

- Phase 4 `complete`. G5 PASS 2026-09-12 (`project-lead-subagent/phase-4-handoff.md`). API pytest 66 passed; worker 33 passed.
- Decisions D-22…D-30 accepted; D-31 authorizes this plan only.
- People/Inbox overlay via `apps/web/src/api/papership.js`; unauthenticated = honest empty.
- `GET /memory` lists tenant `memory_items` (`Store.list_memory`). Schema today: `id`, `tenant_id`, `kind`, `class`, `provenance`, `created_at`. Correct/merge/restrict/archive/export/delete are not built.
- Blueprint-2 already has route `rk === "memory"` (`MemoryView` three-pane) and Settings → Personalisation tagged R3 (`Adaptive views: Off`). Both still use local fixture rows.
- Usage first-baseline is `not_captured` when `event_count=0`.
- OQ-G2 default remains `oq_g2_recorded=false` until live `POST /settings/oq-g2`.
- Live write/external Hermes stay gated (D-25).
- Outstanding owner residuals: `docs/handover/outstanding-actions-and-decisions.md`. None block this plan.

## 4. Scope

- Memory operations on the governed store: search, inspect, correct (new version), merge, restrict, archive, scoped export/delete; provenance fields MEM-01…12; credential-exclusion scan (PRD-F.2, F.3, F.4). Org-wide erasure (PRD-F.8 three confirmations) stays R4.
- Memory manager UI on blueprint-2 matching `docs/ui-blueprint.md` §B.6 (kinds + class filter, list, provenance detail, honest empty). Seat visibility: Founder full; Project Lead domain/project correct/restrict; Operator own sessions/preferences inspect-only.
- Adaptive view schema (versioned JSON), validation, fallback to the fixed seat template, pin / undo / reset, “Adapted for” badge + Why? (no prompts or schema). AUTH-29: no filesystem, shell, database, or credential access; trusted §F components only; stable chrome never moves.
- Personalisation settings: inspect, disable, reset; **off by default**. When disabled, no adaptation occurs.
- B01 native strategy records: goals, initiatives, decisions, risk appetite as store rows on Home / Company rail. KPI snapshots stay `not_captured` without a connected source.
- B03 native capacity: availability and workload on People. **No live HR OAuth** and no payroll/compensation connector.
- Remaining R3 rows (B04, B05, B09, B10, B13, B15, B16, B17, B18, B22) as planned / deny-by-default catalogue shells, not live CRM/finance/support connectors.
- P08 canonical references without invented metrics.
- P05 / PRD-E.1 Automate + schedules `configured` (definitions persist; no live cron to external systems).
- Security re-review: AUTH-29, memory retrieval isolation, restriction propagation to derived summaries. No write/external Hermes lift.
- Growth: first-baseline targets stay `not_captured` if no data; no prices; emit `memory.*` / `view.adaptation.*` enums only.

## 5. Non-goals

- R4 billing, prices, entitlements, allowances, mobile clients, connector SDK / domain packs (P19).
- Marketing site / Vercel `enginelabs-au-site`.
- Live write or external Hermes `accepted` (needs a new Security PASS; D-25 is not that licence).
- Implementing all 14 R3 rows as `working`.
- Live HR, CRM, finance, support, or marketing OAuth.
- Inventing KPI, usage, or price numbers.
- Renaming GitHub / Vercel / App remotes, or changing live receipt path `.orgos/loop/`.
- Public build-log (D-30).
- Promoting R1-ACC-6…9 to VERIFIED without new SHA-linked evidence.
- Generating Phase 6 from this file.

## 6. Current-state audit

| Area | Reality |
|---|---|
| Memory API | `GET /memory` list only; table lacks title, owner, version, restriction, archive, expiry, content |
| Memory UI | Blueprint-2 `MemoryView` renders fixture `memoryNav` / `memoryRows` / `provenance`; empty state not honest |
| Adaptive views | Specified in `docs/ui-blueprint.md` §D; no schema, store, or renderer |
| Personalisation | Settings pane exists; copy says “Release 3”; toggle is fixture `Off` |
| B01 | Home/Company rail uses blueprint fixtures for priorities/decisions; no native goal/initiative/decision API |
| B03 | People overlay lists members/teams; no availability/workload fields |
| Other R3 | Registry rows `planned`; no catalogue shells |
| Automate | Six assistant modes; Automate / schedules not persisted |
| Measurement | Usage emit exists; first-baseline `not_captured` at zero events |
| Auth | Founder JWT; second seat / guest refuse until OQ-G2 |
| Hermes | Catalogued read `accepted` only; write/external gated |

## 7. Assumptions, constraints, risks, and decisions

- `accepted` (D-27): first R3 domains are B01 and B03; memory manager and adaptive views are core.
- `accepted` (D-28): this phase is intake 10 / R3.
- `accepted` (D-31): plan now; do not implement in the planning turn.
- `provisional`: B03 in this phase is **native capacity** (availability, workload, leave reference as a local field), not a live HR system. Live HR remains `connector:tbd`.
- `provisional`: B01 KPI values stay labelled `not_captured` until a later source is bound; do not invent snapshots.
- `provisional`: adaptive views are tenant-stored declarative JSON, validated server-side, rendered only by trusted blueprint-2 components already in `screens.jsx` / `App.jsx`.
- `provisional`: scoped delete archives then tombstones; org-wide erasure remains R4.
- `provisional`: OQ-G2 still required before a live second seat; Phase 5 tests use founder + fixture principals.
- Constraint: AUTH-29 and PRD-A.14 — adapted views never expose prompts, schemas, runtime config, or credentials.
- Constraint: no secrets in repo; no new HR/CRM/finance OAuth env names until a later Security PASS.
- Risk: MemoryView currently shows invented counts (`Sessions 42`). Implementation must replace those with API data or honest empty — never keep fake counts.
- Risk: Home rail already shows fixture decisions; B01 must not present those as live KPIs.
- D-12, D-14, D-21, D-22, D-25, D-26, D-29, D-30 stand.

## 8. Dependencies

T5-0 (document residuals; no product code) → T5-1 memory API → T5-2 memory manager UI → T5-3 adaptive view schema + fallback + pin/undo/reset → T5-4 personalisation settings → T5-5 B01 native strategy → T5-6 B03 native capacity → T5-7 other R3 catalogue shells → T5-8 P08 canonical refs → T5-9 Automate + schedules `configured` → T5-10 Security → T5-11 Growth → T5-12 PL G7.

T5-3 may start after T5-1 (schema is independent of B01/B03). T5-5 and T5-6 may proceed in parallel after T5-2. T5-7 must not enable live connectors. Owner OAuth / OQ-G2 / provider renames stay off the critical path.

## 9. Architecture and affected systems

Keep D-01 monorepo and D-04 adapter. Memory operations, view definitions, strategy records, and capacity fields live in `services/api` store + HTTP, never in desktop secrets. Adaptive views are data, not generated code: the API validates a view-definition document; the web client maps `component` ids onto existing blueprint-2 primitives. Memory retrieval rechecks grants and source restrictions before returning an item or a derived summary (PRD-F.3). Worker/Hermes catalog is unchanged; do not add write/external `accepted` tools.

## 10. Files and paths in scope

- `services/api/app/store.py`, `services/api/app/main.py`, new helpers as needed (`memory_ops.py`, `view_defs.py`, `strategy.py`)
- `services/api/tests/` (new `test_phase5.py`; extend authz/memory tests)
- `apps/web/src/api/papership.js`
- `apps/web/src/blueprint2/App.jsx`, `apps/web/src/blueprint2/screens.jsx`
- `apps/desktop/src/views/` only if Settings/People already mirror web (keep parity; no new desktop shell)
- `docs/capabilities.md` (lead only, evidence-linked)
- `docs/verification.md` § R3 residuals
- `docs/ui-blueprint.md` §B.6 / §D if implementation reveals a documented extension
- Workstream `docs/workstreams/20260910-engine-labs-company-os/<role>/phase-5-*.md` when implementation starts

No Engine Labs marketing project. No live `.orgos/loop/` path change.

## 11. Supporting documents to create or update

- This plan (canonical).
- D-31 (done).
- `docs/handover/outstanding-actions-and-decisions.md` (done; update if residuals change).
- Role charters/plans/evidence/handoffs `phase-5-*` when implementation starts — not in the planning turn.
- Registry rows move from `planned` only with evidence (D-02). Phase 5 target status is `configured`.
- `docs/verification.md` R3 rows (V14-5 memory operations, V16 adaptive) updated at G7.
- Next plan after G7: `docs/plans/phase_6_commercial_delivery_plan.md` (do not write it now).

## 12. Ordered implementation tasks

**T5-0 Carry owner residuals (document only)** — Confirm residuals in `docs/handover/outstanding-actions-and-decisions.md` still do not block implementation. Do not request credentials. Deps: this plan. Files: handover log, STATE. Validation: table names OQ-G2, Gmail/Slack env names, provider rename, Hermes GET `/health`, write/external Hermes. Completion: residuals listed; none treated as G7 blockers.

**T5-1 Memory API** — Extend `memory_items` with title, owner_principal_id, version, restriction_scope, archived_at, expires_at, content_class, parent_id (merge/correct lineage). Endpoints: search/inspect; `POST` correct (new version, provenance preserved); merge; restrict; archive; scoped export job; scoped delete (Founder; not org-wide erasure). Recheck `memory.read` / `memory.write` and source restrictions before retrieval; hide derived summaries when a source is restricted. Credential-exclusion scan on write. Deps: T5-0. Files: `store.py`, `main.py`, `services/api/tests/test_phase5.py`. Validation: pytest for each operation; unprivileged 403; restricted source hides derived row; scan rejects credential-shaped content. Completion: eight PRD-F.3 operations demonstrated on fixtures.

**T5-2 Memory manager UI** — Wire blueprint-2 `MemoryView` to `/memory`. Honest empty: “No memory yet. Knowledge the assistant retains will appear here with its source.” Remove fixture counts. Left nav = six kinds + class filter; list = title/kind/class/owner/version; detail = provenance card + actions. Operator cannot correct/merge/delete. Deps: T5-1. Files: `papership.js`, `App.jsx`, `screens.jsx`. Validation: unauthenticated = empty, not fixtures; Founder can inspect an API item; static scan still expects `<title>Papership</title>`. Completion: §B.6 layout on product path without invented rows.

**T5-3 Adaptive views** — Versioned view-definition schema; store per tenant/member; validate; unknown component or schema fail → fallback seat template (never a blank region). Pin persists; undo reverts last adaptation; reset restores template. Stable chrome (tabs, top bar, rail toggle, assistant, evidence, approvals, destructive actions) never moves. No fs/shell/db/credentials. Deps: T5-1. Files: API view-def module + tests; blueprint-2 renderer using existing components only. Validation: invalid document → fallback test; pin/undo/reset unit tests; AUTH-29 review notes. Completion: P16.01 evidence ready for `configured`.

**T5-4 Personalisation** — Settings → Personalisation: inspect current adaptation, disable, reset. Default **off**. Disabled ⇒ T5-3 apply is refused. Deps: T5-3. Files: Settings pane in `App.jsx`; settings store flag. Validation: disable then apply → 403 or no-op; reset clears pins. Completion: PRD-A.12 inspect/disable/reset demonstrated.

**T5-5 B01 native strategy** — Persist goals, initiatives, decisions, risk-appetite note. Surface on Home / Company rail from the API. KPI fields render `not_captured` without a source. No invented revenue. Deps: T5-2. Files: store + `/strategy` (or equivalent) + Home rail overlay. Validation: founder create/list; unauthenticated rail does not show fixture KPIs as live. Completion: B01.01 evidence for `configured` (native only).

**T5-6 B03 native capacity** — Availability and workload fields on People members. No HR connector, no payroll/compensation source. Deps: T5-2. Files: people/store overlay; People screen. Validation: field round-trip; catalogue still lists live HR as `planned`. Completion: B03.01 evidence for `configured` on the native subset.

**T5-7 Other R3 catalogue shells** — B04, B05, B09, B10, B13, B15, B16, B17, B18, B22 appear in the in-product registry / discovery as `planned` / `unavailable` with “needs connection” copy. Deny-by-default; no OAuth env names. Deps: T5-5. Files: connections/registry overlay. Validation: unknown/unbound domain refuses live write. Completion: PRD-A.17 discoverable without crowding daily work.

**T5-8 P08 canonical refs** — Reference map for currency/calendar/status labels used by B01/B03. Deterministic code only (PRD-E.11). No invented metric values; dashboards that lack a source show `not_captured`. Deps: T5-5. Files: small reference table + read API. Validation: no numeric fixture KPIs in product path. Completion: P08.01 `configured`.

**T5-9 Automate + schedules `configured`** — Persist Automate mode and schedule definitions; they do not fire external systems. Deps: T5-1. Files: store + settings/assistant mode list. Validation: schedule create/list; runner does not call connectors. Completion: P05 / PRD-E.1 Automate `configured`.

**T5-10 Security** — Independent review: AUTH-29, retrieval isolation, restriction propagation, no desktop secrets, no write/external Hermes lift, no new provider secrets. Deps: T5-1…T5-9. Files: `security-engineer-subagent/phase-5-*`. Validation: handoff PASS or CONDITIONAL with bounded residuals. Completion: G7 security gate.

**T5-11 Growth** — Wire `memory.search.executed`, `memory.item.inspected`, `view.adaptation.previewed/applied/reverted/reset` as identifier/enum payloads. First-baseline targets remain `not_captured` if `event_count=0`. No prices. Deps: T5-2, T5-3. Files: usage emit + Growth phase-5 artifacts. Validation: payload scan; CA-10 scan clean. Completion: Growth PASS.

**T5-12 PL G7** — Reconcile role verdicts, move evidence-backed registry rows to `configured`, update verification R3 residuals, outstanding-actions log, STATE. Do not generate Phase 6 from this task until G7 is issued. Deps: T5-10, T5-11. Completion: G7 PASS or CONDITIONAL recorded.

## 13. Adaptive role and delegation map

Tier 3 + product/UI/SE/security/growth/PL triggers. All six roles required. Charters are written when implementation starts. Same workstream id.

| Role ID | Required or skipped | Reason | Predecessor | Owned paths | Gate evidence | Status |
|---|---|---|---|---|---|---|
| product-manager-subagent | required | R3 ACC for memory ops, adaptive views, B01/B03, catalogue shells; no prices | D-31 / this plan | `.../product-manager-subagent/phase-5-*` | R3 acceptance vs D-27 | not started |
| ui-ux-developer-subagent | required | Memory manager B.6; adaptive §D; personalisation; Home/People honest empty | PM | `.../ui-ux-developer-subagent/phase-5-*` | §B.6/§D states; a11y | not started |
| software-engineer-subagent | required | T5-1…T5-9 | UI/UX | `services/api`, `apps/web/src/blueprint2`, tests | pytest + UI overlay | not started |
| security-engineer-subagent | required | T5-10; AUTH-29; memory isolation | SE | `.../security-engineer-subagent/phase-5-*` | PASS/CONDITIONAL | not started |
| growth-marketing-subagent | required | T5-11; no invented baselines; no prices | Security | `.../growth-marketing-subagent/phase-5-*` | emit enums; CA-10 scan | not started |
| project-lead-subagent | required | T5-12 G7 | Growth | `.../project-lead-subagent/phase-5-*` | G7 verdict | not started |

## 14. Test and validation matrix

| Requirement | Validation method | Expected evidence | Status |
|---|---|---|---|
| PRD-F.3 eight operations | pytest on fixture tenant | each operation + 403 for Operator delete | not started |
| PRD-F.3 restriction propagation | derived summary hidden after source restrict | pass | not started |
| PRD-F.2 provenance | inspect returns required fields; credential scan refuses secrets | pass | not started |
| PRD-A.15 B.6 | MemoryView on API data; honest empty | no fixture counts | not started |
| PRD-A.11 / AUTH-29 | invalid view-def → fallback; no fs/shell/db/credentials | pass | not started |
| PRD-A.11 pin/undo/reset | unit + chrome-stability checklist | stable controls unchanged | not started |
| PRD-A.12 | disable/reset; off by default | no adaptation when disabled | not started |
| B01.01 | native goal/initiative/decision create/list | KPI `not_captured` without source | not started |
| B03.01 | native availability/workload | no HR OAuth | not started |
| Other R3 shells | catalogue planned; live write refused | deny-by-default | not started |
| P08.01 | reference map; no invented metrics | scan clean | not started |
| PRD-E.1 Automate | schedule persist; no external fire | `configured` | not started |
| D-25 residual | no write/external Hermes `accepted` | residual recorded | not started |
| D-29 / CA-10 | no prices in UI/docs | scan clean | not started |

## 15. Security, privacy, reliability, accessibility, and performance checks

- AUTH-29 and authority-model AUTH-07/13: adapted views use the same authenticated read contracts as static views.
- Memory: tenant isolation; grant recheck; source-restriction inheritance; no credential material in items (scan on write).
- D-14: user owns memory and strategy records; export is scoped; erasure remains R4.
- PRD-A.14: Operator chrome has no prompts, schemas, or runtime config. Closed Hey Engine stays unmounted.
- Accessibility: §B.6 search count announced; table `aria-sort`; destructive typed confirm; §D undo/reset keyboard reachable.
- Reliability: failed adaptation returns fallback with a message; memory export is a job, not a silent download of another tenant.
- Performance: list/search paginated; no unbounded fixture arrays.
- Contrast / reduced motion: keep D-06 / D-21 tokens; no new motion that ignores `prefers-reduced-motion`.

## 16. Environment-variable registry

Names only. No values. Do not add HR/CRM/finance OAuth names in this phase.

| Variable name | Purpose | Scope/environment | Required by phase | Source/provider | Status |
|---|---|---|---|---|---|
| HERMES_API_BASE_URL | API probe | API | carried | existing | wired |
| HERMES_VERSION_PIN | pin | API/worker | carried | existing | wired |
| HERMES_API_SERVER_KEY | Hermes transport | worker only | carried | VPS | must not reach API |
| GITHUB_APP_* | repo connector | API | carried | existing | wired |
| GMAIL_OAUTH_CLIENT_ID | future B12 live | API | not required for G7 | owner | missing |
| GMAIL_OAUTH_REDIRECT_URL | future B12 live | API | not required for G7 | owner | missing |
| SLACK_CLIENT_ID | future B12 live | API | not required for G7 | owner | missing |
| ENGINE_STORE_PATH | local store | API/worker | carried | existing | wired |

## 17. Deferred human-action queue

| Action | Why agent cannot perform it | Earliest required phase | Blocking now? | Final-checklist destination |
|---|---|---|---|---|
| Live `POST /settings/oq-g2` | live tenant | before second human | no for G7 fixtures | yes |
| Gmail/Slack developer apps + three env names | owner accounts | live B12 | no | yes |
| Rename GitHub/App/Vercel; sync `GITHUB_APP_REPO` | provider dashboards | operator hygiene | no | yes |
| Mailbox creds off systemd `Environment=` | VPS owner | now recommended | no | yes |
| Hermes GET `/health` hang | Hermes ops | ops | no | yes |
| Apple signing / DigitalOcean / backup restore | accounts | R1 residual | no | yes |
| `execute_release` | owner | publication | no | yes |
| Live write/external Hermes `accepted` | new Security PASS | before those tools | no — do not treat D-25 as licence | yes |
| Public build-log | D-30 | later publish decision | no | yes |
| Live HR/CRM/finance OAuth | owner + later Security PASS | after R3 shells | no | later phase |
| CA-10 publish rates / activate charges | owner commercial gate | Phase 6 | no | Phase 6 |

## 18. Rollback and recovery

Disable adaptation (`personalisation.enabled=false`) and new memory-write routes via settings flags. Invalid view definitions already fall back to the seat template. Memory correct/merge create versions — rollback is revert-to-prior-version, not silent rewrite. Native B01/B03 rows can be archived. Catalogue shells have no live connectors to disable. No production DNS to roll back.

## 19. Acceptance criteria (G7)

- Memory search/inspect/correct/merge/restrict/archive/export/delete exist with tests; restriction hides derived summaries; credential scan on write.
- Memory manager on blueprint-2 uses the API or honest empty — no invented counts.
- Adaptive views validate, fall back, pin, undo, reset; AUTH-29 holds; personalisation off by default and inspect/disable/reset work.
- B01 native goals/initiatives/decisions on Home/Company rail; KPIs `not_captured` without a source.
- B03 native availability/workload on People; no live HR connector.
- Other R3 domains are planned catalogue shells; live write refused.
- P08 references exist without invented metrics; Automate/schedules `configured` only.
- No prices; no write/external Hermes `accepted`; no marketing-site edits.
- Every required role has an evidence-backed verdict; skipped roles (none) would need a reason.
- Lead moves only evidence-backed rows to `configured` (expected candidates: P09.01 operations, P16.01, B01.01 native, B03.01 native subset, P08.01, P05 Automate).

## 20. Completion evidence

Not started. Record pytest counts, UI overlay paths, registry version, verification § R3, and role handoff paths here at G7.

## 21. Deviations and follow-ups

None yet. Owner residuals inherited from Phase 4 remain owner-only and are not G7 blockers. Phase 6 is not generated from this file.

## 22. Next Plan Generation Prompt

Read `/AGENTS.md`, the complete core agent context, `/instructions/PROJECT_PLANNING.md`, `/instructions/ROLES.md`, `docs/plans/phase_0_foundations_plan.md`, this completed plan, the Phase 4 plan, workstream handoffs, `docs/roadmap.md`, `docs/verification.md`, and `docs/handover/outstanding-actions-and-decisions.md`. Confirm G7 and every required role gate. Then generate exactly one next plan: `docs/plans/phase_6_commercial_delivery_plan.md` (R4 / intake 11). Do not generate Phase 7 or the final checklist from that step. Do not implement Phase 6 until that file exists and the owner asks.
