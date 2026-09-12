---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: growth-marketing-subagent
status: complete
revision: 1
verdict: CONDITIONAL
started_at: 2026-09-10T17:40:00Z
completed_at: 2026-09-10T17:58:00Z
downstream_role: project-lead-subagent
risk_tier: 3
charter: docs/workstreams/20260910-engine-labs-company-os/growth-marketing-subagent/charter.md (r1)
plan: docs/workstreams/20260910-engine-labs-company-os/growth-marketing-subagent/plan.md (r1)
evidence: docs/workstreams/20260910-engine-labs-company-os/growth-marketing-subagent/evidence.md
predecessor_handoff: docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/handoff.md
---

# Growth Marketing handoff — T0-10 Growth gate

Produced read-only by the role; materialized verbatim by the orchestrating lead. Roadmap insertions are delivered as the "Measurement and validation" and "Commercial activation" sections of `docs/roadmap.md`.

## 1. Outcome

The T0-10 Growth gate is **CONDITIONAL**. Delivered: a sourced positioning statement and differentiation table; a V4/V5 threshold review with a working definition of "baseline" for a single-user pilot and `first-baseline` labels on every quantitative element; a nine-row metric taxonomy (six intake metrics plus PRD §10 additions) with definition, unit, event source, owner, privacy class, consent note and first-baseline rule; one event naming convention (`domain.object.action`) with required, extension and prohibited properties aligned to GM-1, an initial catalogue covering all seven views and the global surfaces, and retention alignment (365 d then aggregated); a pilot learning plan; tier communication principles with no prices; commercial activation prerequisites; later-release GTM posture as drafts only with explicit ethics constraints (GM-7…GM-10). No metric value, baseline, or price is stated anywhere. Nothing was published, written, or spent (EV-G13).

Not PASS because two bounded items are pending outside this role: Security schema review of the proposed identifier/enum extension fields (GM-11, F-SEC-16) and owner decision OQ-4 (tier labels). Not BLOCKED because every required input existed, no claim is unsupported, and no fabricated data exists (EV-G03, EV-G15).

## 2. Scope completed and not completed

Completed (plan §6 tasks 1–8, in order): positioning + differentiation (§5.1); V4/V5 review and baseline definition (§5.2); metric taxonomy (§5.3); event convention, properties, catalogue, retention, Security gate (§5.4); pilot learning plan (§5.5); tier communication principles and activation prerequisites (§5.6); GTM posture drafts and ethics (§5.7); evidence EV-G01…EV-G15 and this handoff.

Not completed / out of scope by charter: publishing; pricing numbers; ad or vendor spend; community posting; analytics tooling selection; instrumentation code; file edits. Not performed: competitor product trials; pricing-page fetches; community-rule fetches (recorded EV-G04, EV-G14). Named-competitor comparison tables were later removed by owner request.

## 3. Charter, plan, and predecessor handoffs

- Charter r1 followed; read-only boundary honoured; §5 assumptions confirmed: "no analytics or baseline data exists" → `verified` (EV-G03); "release 1 has one user; measurement is instrumentation design plus first-baseline capture" → `verified` against PRD §0.4, AS-2, AS-10. §10 escalation triggers not fired: PM tier structure matches the intake row-for-row (EV-G10); no Security constraint prohibits a required metric — GM-1 permits every field the six metrics need at identifier/enum level, with additions routed through GM-11 (EV-G07).
- Plan r1 tasks 1–8 executed in order; one deviation recorded in §8 (positioning claims gated on acceptance evidence).
- Predecessors: Security (CONDITIONAL; §11.1 GM-1…GM-12 binding — adopted in full; F-SEC-16 owner "Growth (adopt), SE (schema)"); PM (CONDITIONAL; OQ-1…OQ-6; tiers §8.1); UI/UX (CONDITIONAL; §5 analytics row "event points implied per view (run start/complete, approvals, navigation, handoffs)"); SE (CONDITIONAL; usage ledger entity, V17-1).

## 4. Outputs, changed paths, and external changes

- Changed paths by this role: none (read-only).
- Materialized by the lead from this payload: `growth-marketing-subagent/evidence.md`, `growth-marketing-subagent/handoff.md`, `docs/roadmap.md` sections "Measurement and validation" and "Commercial activation".
- External changes: none. Network: two read-only GitHub fetches (EV-G04). MCP: none.

## 5. Requirement and horizontal-checklist coverage

| Requirement ID | Result | Evidence |
|---|---|---|
| REQ-05 commercial controls — communication and measurement | met — §5.6 principles (no prices), §5.3/§5.4 taxonomy and events | EV-G06, EV-G07, EV-G09 |
| REQ-06 validation thresholds | met — §5.2 V4/V5 review, `first-baseline` labels | EV-G05, EV-G15 |
| Intake L112 usage measurement; PRD §10; PRD-G.11; P14/P18 `configured` R1; R1-ACC-11/12 | met — nine-row taxonomy traceable to PRD | EV-G06 |
| Blueprint §6 positioning; §14 GTM | met — §5.1 sourced statement; §5.7 drafts only | EV-G04, EV-G14 |
| F-SEC-16 / GM-1…GM-12 adoption | met — cited individually in §5.3, §5.4, §5.7, §8 | EV-G02, EV-G07 |
| PRD-G.6/G.7/G.9/G.10 communication constraints | met — §5.6 | EV-G09 |
| PM OQ-4 | carried — Tier 1–4 used; no public label | EV-G10 |
| Horizontal: Product/user acceptance | reviewed — thresholds align with R1-ACC-11, NFR-4 | EV-G05 |
| Horizontal: UI/UX and accessibility | reviewed — events are passive, no UX change; disclosure copy in Settings → Data (§5.4.6) | EV-G08 |
| Horizontal: Frontend/backend/data/API/integration | reviewed — events map to existing `UsageEvent`/`MetricRecord` entities and ledger transitions; no new store | EV-G07 |
| Horizontal: Security/privacy/compliance/abuse | reviewed — GM-1…GM-12 adopted; extension fields gated on GM-11 | EV-G02, EV-G07 |
| Horizontal: Testing/observability/reliability/performance | reviewed — each metric has a testable derivation rule (§5.3) | EV-G06 |
| Horizontal: Deployment/rollback/operations | not_applicable in phase 0 | — |
| Horizontal: Analytics/growth/consent | owned — §5.3–§5.7 | EV-G03, EV-G14 |
| Horizontal: Documentation/handoff | owned — this file, evidence, roadmap sections | EV-G11 |

### 5.1 Positioning and differentiation (plan task 1)

**Positioning statement (57 words; DRAFT — publishable only after the cited acceptance rows are VERIFIED):**

> Engine Labs is the company operating system for founders who run work through agents they must be able to hold accountable: every run is sponsored, scoped, budgeted and receipted; approvals bind to the exact action and version; jobs survive a closed laptop; and every decision is retained as governed company memory — starting with shipping your own software.

Claim-to-evidence map (GM-8: claims must match verified architecture; no certification, compliance, "zero retention" or provider-guarantee language is used):

| Clause | Requirement | Verifying acceptance row | Status today |
|---|---|---|---|
| sponsored, scoped, budgeted, receipted | PRD-E.2, E.3 | R1-ACC-6, R1-ACC-8 | design only — unverified |
| approvals bind to exact action and version | PRD-D.10; AUTH-10 | R1-ACC-6; F-SEC-04 phase-1 gate | design only — unverified |
| jobs survive a closed laptop | PRD-E.4 | R1-ACC-3 | design only — unverified |
| decisions retained as governed memory | PRD-F.1–F.2 | R1-ACC-6 (retained knowledge stage) | design only — unverified |
| starting with shipping your own software | PRD-B.1; blueprint §6 wedge | R1-ACC-6 | design only — unverified |

Audience (blueprint §4): founders and very small teams already using agents for engineering work who have no sponsor/budget/receipt model and recover failures manually. Message hierarchy: (1) accountability primitives are the product, (2) durable cloud execution the operator can disconnect from, (3) the founder's own development loop as proof, (4) company memory. Objections and evidence limits: "governance is table stakes" (blueprint §3 implication — differentiation must come from execution quality, which R1 must demonstrate); "single founder is not a market" (deferred to design-partner stage, §5.7).

Papership capability table (named-competitor columns removed by owner request, 2026-09-12). No prices.

| Dimension | Papership design intent | PRD |
|---|---|---|
| Company work ledger + organisation model | Native ledger (plans, assignments, dependencies, decisions, evidence) + 8 org entities | A.3, D.4 |
| Per-run sponsorship, scoped grants, action-bound approvals | Nine run fields; grant classes; approval bound to action + target version | E.2, D.10 |
| Durable cloud execution operator can disconnect from | Close ≠ cancel; reconnect/resume; receipts; idempotency | E.4, E.7 |
| Desktop operating experience | Tauri desktop from Papership shell; no prompts/schemas for operators | A.14, D.13 |
| Governed company memory with provenance | Seven provenance fields; class source/approved/inferred | F.1–F.3 |
| Audience and deployment | Founder-first, single-tenant self-hosted per customer | architecture §10 |

Engine Labs must be measurably better on operator experience, recovery and business-record integration (blueprint §5) — these are exactly the V4/V5 dimensions.

### 5.2 Value hypothesis and V4/V5 threshold review (plan task 2)

Value hypothesis (from blueprint §6/§7, PRD §0.4): a founder completing a real software change through the governed loop obtains a reviewed, evidenced, releasable change with fewer manual recoveries and no lost audit trail than with disconnected IDE-agent tooling, at a cost per completed outcome that can be measured and later priced. In R1 this hypothesis is **instrumented, not tested**; R1 produces the first baseline that R2 targets are set from (NFR-4).

Restated thresholds (blueprint §7, verbatim):

| # | Riskiest assumption | Experiment | Pass threshold (blueprint) | Phase |
|---|---|---|---|---|
| V4 | The governed loop is faster and safer than the founder's current IDE-agent workflow | Complete three real Engine Labs changes through the loop; measure operator interventions, context switches, wall time, cost per completed outcome | ≥1 change fully reviewed with linked evidence; intervention count and cost recorded as baseline (no target yet — first measurement) | 2 |
| V5 | Founder can operate the product without seeing prompts, schemas, or runtime config | Usability pass over the seven core views with the Founder seat | All routine tasks completable without technical traces | 3 |

Measurability assessment:

- V4 — measurable as written. Pass element (a) "≥1 change fully reviewed with linked evidence" is binary and verified by R1-ACC-6. Pass element (b) "recorded as baseline" is a capture criterion satisfied when all four V4 measures (interventions, context switches, wall time, cost per completed outcome) exist for each of the ≥3 changes on the release revision. The assumption text "faster and safer than the founder's current workflow" is **not testable in R1**: no comparator baseline exists (EV-G15). Label: `first-baseline`. Optional recommendation C-2 (§9): a self-reported comparator log for 3 comparable changes done the current way (wall time, interventions, cost if known), labelled `self-report, n=1, low rigour` and never presented as a measured result.
- V5 — measurable once the "routine task" list is fixed. Proposed list (derived from R1-ACC-2, 3, 6, 8, 13 and `docs/ui-blueprint.md` §B primary actions): create priority and plan; start a run from a work item; approve/reject a decision; pause/resume/cancel a run; reconnect after closing the app; read remaining allowance and estimated cost; search/inspect memory via the assistant; view the registry and a "needs connection" explanation; grant a repository grant class. Measure: pass/fail per task plus count of technical-trace exposures (prompt text, schema, runtime config, session id outside the designated technical view) — the exposure count must be zero (PRD-A.14 acceptance). Scope: the views actually built in R1 (4+1 per OQ-5 proposal); B.5/B.6 tasks are `NOT_APPLICABLE` until R2/R3. Label: `first-baseline` for task time and error counts; zero-exposure is a requirement, not a target.

Definition of "baseline" for the single-user pilot (binding for R1 reporting):

1. Population: one founder (n=1), one release revision, ≥3 completed changes (V4) and one usability pass (V5). No statistical inference, confidence claim or trend is made.
2. Baseline = the recorded per-item values and their min/median/max across the pilot items, stored as `MetricRecord` rows linked to work items and runs, reported in `docs/verification.md` (R1-ACC-11) with the revision SHA.
3. Purpose = first-baseline capture, not optimisation: no target is asserted in advance (NFR-4, I-06); R2 targets are derived from these records before R2 tests.
4. Absence rule: if a measure could not be captured for an item, the record states `not_captured` with a reason; no interpolation, proxy or estimate is substituted (GM-2, DRR-21).
5. Every quantitative threshold in this workstream that lacks data carries the literal label `first-baseline`. The only fixed values are requirements, not targets: zero duplicated external effects (PRD-B.7), zero successful authority violations (PRD §10 guardrail), zero technical-trace exposures for operators (PRD-A.14).

### 5.3 Metric taxonomy (plan task 3)

Privacy class per `docs/policies/data-residency-and-retention.md` §3: usage events and metric records are **C2 confidential**; personal-data flag **true (pseudonymous)** because a pseudonymous member id is present (DRR-01). Owners: definition = Growth; instrumentation and derivation = SE; schema review = Security (GM-11); reporting at gates = PL. Consent baseline for all rows: first-party, in-tenant, no third-party SDK (GM-4, DRR-22); disclosed in Settings → Data alongside retention settings (PRD-F.4); R1 data subject and controller are the same founder; R2 member notice requirement in §5.4.6.

| Metric (intake/PRD) | Definition | Unit | Event source (catalogue §5.4.5) | First-baseline rule | PRD |
|---|---|---|---|---|---|
| Task completion | Per work item: number of the 11 PRD-B.1 stages reached and completed; loop completed end-to-end (yes/no); wall time request→release proposal | stages (0–11); boolean; seconds | `work.stage.completed`, `work.item.closed`, `agent.run.completed` | record per item; report count of items completing all 11 | PRD-B.1, §10 |
| Correctness | Per change: review outcome (approved / changes requested), check pass ratio at review, defects linked after review | enum; ratio; count | `work.stage.completed` (stage=review, outcome_code), check-result records, incident links | record per change; no target | PRD-B.3, §10 |
| Recovery | Per run: transient retries, diagnostic attempts, escalations; seconds from failure event to resumed progress; duplicated external effects | counts; seconds; count (requirement = 0) | `agent.run.retried`, `agent.run.recovered`, `agent.run.escalated`, receipt reconciliation | record per run; duplicates are a hard requirement, not a metric target (PRD-B.7) | PRD-E.7, E.8, §10 |
| Operator intervention | Per completed outcome: approvals decided, manual corrections, clarifications answered, escalations answered, permission grants added mid-work | count by `intervention_reason` enum | `approval.decision.*`, `work.item.edited` (by human during run), `agent.run.escalated` (answered), `permission.grant.changed` | record per item; enum reasons enable R2 delegation design | PRD-D.9, E.8, §10 |
| Context switching | Per work item: distinct views used, view changes, source-app handoffs, assistant-panel opens | counts | `nav.view.opened`, `handoff.source_app.opened`, `assistant.panel.opened` | record per item; no target | PRD-A.5, §10 |
| Cost per completed outcome | Per completed work item: tokens by model band, tool calls by class, execution seconds, estimated cost band (external view) and ledger cost (internal, PRD-G.3) without double counting | tokens; count; seconds; band enum; ledger amount (internal only) | `usage.provider_event.recorded` (dedupe by `provider_event_id`), `usage.budget.reserved`, `usage.budget.reconciled` | record per item; ledger sum must equal provider-reported usage (PRD-G.3); external reporting uses bands only (GM-1) | PRD-G.3, G.11, §10 |
| Guardrail: authority violations | Refused unauthorised attempts (count) and successful unauthorised actions (must be 0) | count; count | audit events (`approval.request.voided`, refusals) — AuditEvent, not UsageEvent | requirement, not target | PRD-D.5, D.11, §10 |
| Usability (R3+) | Completion time and error count, adaptive vs fixed views; routine work without technical traces | seconds; count | `view.adaptation.applied/reverted`, task timing from `nav.view.opened` | set targets from pilot baseline before R3 tests | PRD-A.11, A.12, NFR-4 |
| Infra recovery/performance | Restore time, potential data loss window, resource headroom | seconds; seconds; percent | operations measurement (NFR-5/6), not product events | set from pilot baseline before testing; V6/V17-5 | NFR-4, NFR-6 |

### 5.4 Event naming, properties, catalogue, retention, gate (plan task 4)

#### 5.4.1 Naming convention (one convention; binding)

`<domain>.<object>.<action>` — lowercase ASCII, dot-separated, snake_case within a segment, `action` is a past-tense verb. Domains: `work`, `agent`, `approval`, `assistant`, `nav`, `handoff`, `connection`, `memory`, `view`, `permission`, `usage`, `auth`. New domains/objects/actions require a catalogue revision and Security schema review before emission (GM-11, DRR-26).

#### 5.4.2 Required properties (every event; aligned to GM-1 / DRR-20 permitted fields)

`event_name`, `event_id` (uuid), `occurred_at` (UTC ISO-8601), `tenant_id`, `member_pseudonymous_id` (rotates on offboarding; never an email or auth user id), `run_id` (nullable), `mode` (nullable enum Ask/Analyse/Plan/Draft/Execute/Review/Automate), `model_band` (nullable enum, never full config), `tokens_input`/`tokens_output`/`tokens_cached` (nullable ints), `tool_call_counts_by_class` (map enum→int), `duration_ms` (nullable), `estimated_cost_band` (nullable enum), `outcome_code` (enum), `schema_version`.

#### 5.4.3 Proposed extension properties — Security schema review required before implementation (GM-11, F-SEC-16, DRR-26)

All are opaque identifiers or closed enumerations; none carries content: `work_item_id`, `stage_id` (11 PRD-B.1 stages), `view_id` (enum from §C tabs and §B views), `approval_class` (grant class enum), `tool_class` (enum), `seat_template` (Founder/PL/Operator), `provider_event_id` (dedupe, GM-2/DRR-21), `intervention_reason` (enum: approval_required, correction, clarification, recovery_escalation, permission_missing, other), `recovery_kind` (enum: transient_retry, diagnostic_attempt, escalation), `handoff_target` (provider enum, e.g. github), `adaptation_version` (int).

#### 5.4.4 Prohibited properties (by schema, GM-1 / DRR-20 / DRR-02 / MEM-20)

Prompt text or any message body; conversation, file or document content; memory item content (counts by kind/class only, MEM-20); personal data of external individuals; member names, emails, auth ids, IPs, device fingerprints; full model configuration or provider prompts; credentials, tokens, keys (C3); free-text fields of any kind; repository file paths or diff text; URLs other than the internal deep-link id.

#### 5.4.5 Initial event catalogue (R1 unless stated; view refs `docs/ui-blueprint.md` §B/§C/§D)

| Event | Trigger | View/surface | Extension props | Feeds metric | Release |
|---|---|---|---|---|---|
| `work.item.created` / `work.item.edited` / `work.item.closed` | ledger record create/edit/close (edits by a human while a run is active count as intervention) | B.2 Work item, Home `+` | `work_item_id`, `intervention_reason` (edit) | task completion; intervention | R1 |
| `work.stage.completed` | one of the 11 loop stages reaches done, with outcome | B.2 loop chain | `work_item_id`, `stage_id`, `outcome_code` | task completion; correctness | R1 |
| `agent.run.started` / `.paused` / `.resumed` / `.cancelled` / `.completed` / `.failed` | run state transitions (server-side) | B.4 Agent run; B.3 run card; Home running work | `work_item_id`, `mode`, `model_band` | task completion; cost | R1 |
| `agent.run.retried` / `.recovered` / `.escalated` | PRD-E.8 harness events | B.4 Recovery callout | `recovery_kind`, `duration_ms` (failure→resume) | recovery; intervention (escalation answered) | R1 |
| `approval.request.created` / `approval.decision.approved` / `.rejected` / `approval.request.voided` | approval requested; human decision; target changed → void (PRD-D.10) | Home decisions; B.4 pinned card; B.3 inline card; notifications | `approval_class`, `work_item_id`, `run_id` | intervention; guardrail (audit) | R1 |
| `assistant.session.started` / `assistant.mode.switched` / `assistant.panel.opened` / `assistant.message.sent` (count only, no content) | panel/tab/mode/composer actions | B.3 Assistant | `mode`, `work_item_id` (scope) | context switching; mode usage (OQ-6 input) | R1 |
| `nav.view.opened` / `nav.tab.switched` / `nav.palette.used` | route change, primary tab, ⌘K | §C primary tabs, command palette | `view_id`, `work_item_id` (if scoped) | context switching; usability | R1 |
| `handoff.source_app.opened` | external handoff link (Open branch/PR; "opens in your browser") | B.2 secondary; B.5 wizard step 2 | `handoff_target`, `work_item_id` | context switching | R1 (repo), R2 |
| `connection.api.disconnected` / `.reconnected` | desktop loses/regains API/SSE (state D) | §C status bar; Home banner | `duration_ms` (offline) | recovery (UX); reliability | R1 |
| `connection.provider.unavailable` / `.restored` | registry row → `unavailable` / back | B.5 Connection setup; registry | `handoff_target` (provider) | connector demand (pilot plan) | R1 (repo), R2 |
| `connection.setup.completed` | wizard step 5 done | B.5 | `handoff_target` | activation (R2) | R2 |
| `memory.search.executed` / `memory.item.inspected` | search via assistant (R1) / manager (R3); counts only | B.3 (R1), B.6 (R3) | `outcome_code` (results_found / none) | usability; memory statistics (MEM-20 counts) | R1 / R3 |
| `permission.grant.changed` | grant/revoke/ceiling save (after reauth) | B.7 Permissions editor | `approval_class`, `intervention_reason=permission_missing` when mid-work | intervention | R1 |
| `view.adaptation.previewed` / `.applied` / `.reverted` / `.reset` | §D preview→apply→undo flow | §D adaptive views | `view_id`, `adaptation_version` | usability (adaptive vs fixed) | R3 |
| `usage.provider_event.recorded` / `usage.budget.reserved` / `usage.budget.reconciled` | provider usage ingested (dedupe), reservation before dispatch, reconciliation | B.4 Usage/Budget cards; ledger | `provider_event_id`, token/tool/cost fields | cost per completed outcome; PRD-G.3/G.4 | R1 (measure), R4 (enforce) |
| `auth.session.signed_in` / `.signed_out` | Auth portal | §C Auth | `seat_template` | activation (R2 seats) | R1 |

Projection rule (§C "one event stream, five projections"): UI surfaces never emit duplicate run-lifecycle events; server-side transitions are the single source; UI emits only `nav.*`, `assistant.panel.opened`, `handoff.*`, `connection.api.*`, `view.*`.

#### 5.4.6 Retention, erasure, destination and consent alignment

- Retention: individual events 365 days, then aggregated into `MetricRecord`; not individually erasable; excluded from any export after organisation erasure and aggregated within 30 days of erasure (GM-3, ERA-14; architecture §4 UsageEvent row).
- Destination: tenant Postgres only (native `UsageEvent`/`MetricRecord`); no external measurement destination in R1; any future destination becomes an architecture §6 row and DRR-04 classification before use (GM-12, DRR-26); no third-party SDK, pixel, replay or fingerprinting (GM-4, DRR-22); optional `SENTRY_DSN` telemetry is opt-in per organisation, scrubbed, payload inspected (GM-4, R1-ACC-14).
- Cross-tenant: none — no benchmarking or "customers like you" (GM-5, DRR-23); preference learning never feeds segmentation (GM-6, MEM-19, DRR-24).
- Consent and disclosure: R1 — the founder is both data subject and controller; a plain-language "What Engine Labs measures" list (this catalogue at identifier level) is shown in Settings → Data next to retention defaults (PRD-F.4). R2 — a member-facing notice at seat provisioning is required before any non-founder seat is activated; its legal basis is an owner/legal decision (recorded OQ-G2, §12). No lifecycle messaging exists in R1; any later messaging uses consented channels only, never contacts harvested from connected sources (GM-7, DRR-25). Attribution uses first-party consented identifiers only (GM-10).
- Experiments: none in R1; later A/B scope is presentation and onboarding copy only and never varies authorization, approval, retention, safety or pricing-disclosure behaviour (GM-9, DRR-27).
- Gate: Security reviews the schema (required set, extension set, prohibited set, enum lists) in phase 1 before implementation; this is the F-SEC-16 re-verification (GM-11).

### 5.5 Pilot learning plan (plan task 5)

What release 1 must record (all from existing entities; no new destination) so release 2 scope and later pricing can be decided from evidence rather than assumption — no quantities are proposed here:

| Learning question | Record in R1 | Informs |
|---|---|---|
| What does one completed change cost, by component? | Per completed work item: tokens by model band, cached vs fresh input, tool calls by class, execution seconds, retries, ledger cost (PRD-G.3) | Model-band allowance structure and rate-card line items (PRD-G.2, G.5, G.8) — activation gate only |
| Where does the founder intervene, and why? | `intervention_reason` distribution per item; approvals by class; escalations answered | R2 delegation/seat design (PRD-D.1–D.3); which approvals can be policy-defaulted |
| Where does recovery fail or take long? | Recovery kinds, failure→resume seconds, incident records; interruption-trial outcomes (V3) | R2 reliability priorities; hosting line item |
| Which outcomes needed a connection that did not exist? | `connection.provider.unavailable` and PRD-A.4 "needs connection" explanations shown, by provider | R2 connector ordering (B12, B23, P07 are R2 buckets; 4 of 43) |
| Which modes and views carry the work? | Mode usage; `view_id` opens per item; assistant panel opens | OQ-6 (modes), OQ-5 (views), R3 adaptive-view priorities |
| Can the allowance/cost display be understood without the billing view? | V5 walkthrough item "read remaining allowance and estimated cost" pass/fail | PRD-G.6 copy; tier communication (R4) |
| What resources does the pilot consume? | NFR-6/V6 measurement report (DB, browser, worker) | VPS sizing; hosted-capacity line item (PRD-G.8) |
| What did the founder need that the product lacked? | Qualitative log kept as ledger decisions/evidence records (content stays in the ledger, never in events) | R2 scope; positioning objections |

Reporting: PL includes the first-baseline records (min/median/max, `not_captured` counts) in the phase-3 verification index (R1-ACC-11) and the owner handoff; R2 targets are then set per NFR-4.

### 5.6 Tier communication principles and commercial activation prerequisites (plan task 6)

Tier naming: intake `Tier 1`–`Tier 4` only, until the owner answers OQ-4; the labels Free/Basic/Professional/Enterprise remain `proposal` and appear in no UI or draft.

Principles (no prices anywhere — PRD-G.10):

1. Non-billing views show only remaining allowance and estimated action cost (band); detailed model, token and rate accounting lives in the billing view (PRD-G.6; B.3 footer, B.4 Budget card).
2. Tokens and money are always shown as separate figures; model band is named, full model configuration is not (PRD-G.2; GM-1).
3. Reservation before dispatch is visible ("reserved vs allowance") so limits are never a surprise (PRD-G.4).
4. Reaching a limit pauses new chargeable work only; records, exports and pending decisions stay accessible and the copy says so (PRD-G.4, R1-ACC-12 spirit).
5. Cross-tier guarantees are stated wherever tiers are described: isolation, permissions, essential audit, export, deletion (PRD-G.7).
6. Hosted capacity, backup storage and support are separate, named line items; customer tool subscriptions are separate unless commercially authorised (PRD-G.8).
7. No comparative nudges ("most popular", countdowns, fake scarcity), no pre-selected upgrades, no obstruction of downgrade or export — dark patterns are prohibited (ROLES §8; blueprint §14).
8. No claim of certifications, compliance frameworks, "zero data retention" or provider no-training guarantees without a decision record with evidence (GM-8, DRR-06).
9. Any pricing-disclosure behaviour is fixed, never experimented on (GM-9, DRR-27).

Commercial activation prerequisites (all must have evidence before publication or charge — commercial decision gate, I-05/I-11, PRD-G.10):

| # | Prerequisite | Evidence | Owner |
|---|---|---|---|
| CA-1 | Measured infrastructure, model/tool and support costs from realistic concurrency (NFR-6, V17-5, phase 11) | measurement report preceding any price proposal | SE / PL |
| CA-2 | First-baseline cost per completed outcome from the pilot (§5.5) | `MetricRecord` set on release revision | SE / PL |
| CA-3 | Versioned rate card; every charge references a rate-card version and ledger entry (PRD-G.5) | rate-card artefact + ledger schema | SE / owner |
| CA-4 | All four entitlement/usage models validated in billing test mode: entitlements, allowances, seat changes, reservations, graduated rates, limit enforcement, provider reconciliation, no duplicate charges (PRD-G.12, V17-2, V17-3) | test-mode results | SE / Security |
| CA-5 | Licensing: `LICENSE`/`NOTICE`, inventory, upstream notices (LIC-01, LIC-02, LIC-07); Hermes licence verified for commercial self-hosted use (LIC-05, H-5); SDK licence decision before external publication (LIC-03) | licence artefacts, decision records | SE / owner |
| CA-6 | Provider data-use terms recorded before real customer content is sent (DRR-06, H-4) | decision record | owner |
| CA-7 | Export at all tiers and erasure/offboarding exercised (PRD-F.7–F.9, phase 11) | test evidence | SE |
| CA-8 | Tier labels decided (OQ-4) | owner decision | owner |
| CA-9 | Support ownership and service targets established from measured behaviour (phase 11) | support runbook | owner / PL |
| CA-10 | Explicit owner decision to publish and to activate charges (two separate decisions) | decision records | owner |

### 5.7 Later-release GTM posture — DRAFTS ONLY (plan task 7)

Every item below is a draft for owner review; nothing is scheduled, posted, or spent. Publication is a human action (phase plan §17 "Approve any publication of go-to-market drafts").

- Where the audience gathers (blueprint §14): founder/indie-hacker communities, AI-agent builder communities, open-source agent-orchestration repositories. Rule text for each community must be fetched and recorded before any draft is considered (EV-G14).
- Trust assets (produced only from verified evidence): the R1 development-loop evidence itself (a real change with receipts, R1-ACC-6); the authority-model and recovery documentation (`docs/policies/authority-model.md`, PRD-E.7/E.8) once adopted; honest capability claims limited to the §5.1 dimensions, each row re-verified against primary sources with fetch dates.
- Sequence (gated on verified workflows): founder-only pilot (R1) → invited Project Lead/Operator seats (R2) → design partners in one sector (R3) → commercial activation with published rates (R4, after CA-1…CA-10).
- Content concepts (blueprint §14; drafts, never posted without owner approval): problem-first "how do you keep agents from repeating an external write after a timeout?"; transparent build journey — receipt/idempotency model after the V3 interruption trials (only after V3 results exist); resource-value — a checklist for scoping agent credentials per task.
- Open question OQ-G1: owner appetite for a public build-log (recorded only; no default).
- Ethics constraints (binding): no astroturfing, sockpuppets or undisclosed promotion; no deceptive scarcity or dark patterns; no rule evasion; disclosure of affiliation in every post; all claims traceable to evidence and matching verified architecture (GM-8); lifecycle messaging only via consented channels, no contact harvesting (GM-7); experiments never touch authorization, approval, retention, safety or pricing disclosure (GM-9); first-party consented attribution only, no cross-site tracking (GM-10); no exploitative targeting.

## 6. Validation and evidence

Executed by the role (read-only): `date -u` (17:56:15Z, 17:58:00Z); `rg -c "^- GM-[0-9]+:"` → 12; `rg -n '\$[0-9]|USD|AUD|€' docs/product.md` → no match (exit 1); `rg -n "^### B\.[1-7]" docs/ui-blueprint.md` → 7; `rg -c "^\| (B|P)[0-9]{2}" docs/capabilities.md` → 43; `ls docs/roadmap.md` → absent; `ls` of role directory → `charter.md`, `plan.md`. All other validation is document inspection (EV-G01…EV-G15). No tests, builds or analytics queries were possible or attempted (no code; no analytics source).

Recommendations (not executed): optional V4 comparator self-report log (C-2); community rule fetch before any draft publication.

## 7. Tools, skills, modalities, and MCP evidence

- Tools: `Read`, `Grep`, read-only `Shell` (`date`, `rg`, `ls`, `git status --porcelain`, `wc`), `WebFetch` (2 calls, github.com / raw.githubusercontent.com; one timeout).
- Skills: none invoked. MCP: none (no analytics namespace configured; `.cursor/TOOLS.md` L381–402 treats analytics as unavailable until authenticated — EV-G03).
- Modalities: text only.

## 8. Assumptions, decisions, and deviations

- A-G1 (`verified`): no analytics or baseline data exists; every threshold is `first-baseline` (EV-G03, EV-G15).
- A-G2 (`provisional`): R1 built views = home, work item, assistant, agent run, minimal permissions editor (OQ-5 proposal); V5 scope follows it. Validation: OQ-5 answer before phase-1 plan.
- A-G3 (`provisional`): pseudonymous member id is a per-tenant random identifier rotated at offboarding, never derived from email/auth id. Validation: Security schema review.
- A-G4 (`provisional`): the personal-data flag on usage events is `true (pseudonymous)` (conservative reading of DRR-01). Validation: Security review.
- D-G1: identifier/enum extension fields are proposed rather than assumed permitted; emission of any extension field is blocked until GM-11 review passes.
- D-G2: competitor prices are excluded from all Growth artefacts (staleness, blueprint §16; avoids implying an Engine Labs price position).
- D-G3: intake tier names Tier 1–4 are used until OQ-4 is answered.
- Deviation from plan wording: task 1 "positioning statement" is delivered as a DRAFT with a claim-to-evidence gate (positioning cannot be published before R1-ACC-3/6/7/8 are VERIFIED, per GM-8). Recorded, not a scope change.
- Ethics adoption: GM-1…GM-12 adopted in full without exception.

## 9. Findings, severity, risks, and unresolved items

| ID | Severity | Finding | Owner | Remediation | Re-verification |
|---|---|---|---|---|---|
| F-G1 | medium | Context-switching, intervention and task-completion metrics need identifier/enum fields beyond the GM-1 permitted list (`work_item_id`, `view_id`, `stage_id`, enums) | Security (review), SE (schema) | Security schema review in phase 1 (GM-11, F-SEC-16); if refused, metrics fall back to run-level granularity and the taxonomy is revised | Security verdict recorded; schema test asserts no content fields |
| F-G2 | low | V4 comparator baseline absent; "faster and safer" not testable in R1 | PL | Score V4 on capture criterion; optional comparator self-report (C-2) labelled low rigour | phase-2 plan text |
| F-G3 | low | V5 "routine task" list not fixed; V5 references seven views while R1 builds 4+1 | PL / UI-UX | Adopt §5.2 task list in the phase-3 plan; mark B.5/B.6 tasks NOT_APPLICABLE for R1 | phase-3 plan |
| F-G4 | low | OQ-4 tier labels unresolved | owner | Answer before any tier appears in a UI (R4) | decision record |
| F-G5 | low | Positioning claims describe unverified design (PRD-E.4, D.10, E.2/E.3) | PL / owner | Keep DRAFT until R1-ACC-3/6/7/8 VERIFIED; re-verify the Papership capability table against primary sources before publication. Do not restore named-competitor columns. | verification index rows |
| F-G6 | low | R2 member measurement notice/legal basis undefined | owner (legal) | Decide before first non-founder seat (OQ-G2) | decision record |
| Risk | medium | Metric pressure could push registry rows to `working` or thresholds to invented targets | PL | NFR-4 and PRD §3.2 rule 6 enforced at every gate; `first-baseline` label mandatory | gate review |

No high or critical findings. No blocking defect handed downstream. Fabricated data: none.

## 10. Remediation and invalidated gates

None. No prior Growth gate exists. Security F-SEC-16 owner row "Growth (adopt)" may be marked adopted with this handoff; the "SE (schema)" half remains open until phase 1. If Security rejects the extension fields (F-G1), this verdict remains CONDITIONAL and the taxonomy is revised at run-level granularity — it does not revert to BLOCKED because the six intake metrics remain derivable from GM-1 fields plus ledger/audit records.

## 11. Downstream instructions

### 11.1 Next role: `project-lead-subagent`

- Required inputs: this handoff §5.2 (baseline definition and V4/V5 labels), §5.3 (taxonomy), §5.4 (schema, catalogue, retention, GM-11 gate), §5.5 (pilot learning plan), §5.6 (principles and CA-1…CA-10), §5.7 (drafts and ethics); `evidence.md` EV-G01…EV-G15; the "Measurement and validation" and "Commercial activation" sections of `docs/roadmap.md`.
- Constraints that remain binding: GM-1…GM-12 (Security §11.1) and their policy mirrors DRR-20…DRR-27, MEM-19…20, ERA-14; PRD-G.10 no prices; NFR-4 no targets before baseline; `first-baseline` label on every threshold without data; positioning stays DRAFT until F-G5 clears; nothing published or spent without owner decision.
- Carry into the phase-1 plan: Security schema review of §5.4.2–5.4.4 before any event is emitted (F-SEC-16 re-verification); `UsageEvent`/`MetricRecord` schema with content fields excluded by construction; Settings → Data disclosure list (§5.4.6); catalogue events marked R1 mapped to emitting components.
- Carry into the phase-2 plan: V4 capture per change (four measures + `not_captured` rule); optional comparator log decision (C-2); `intervention_reason` and `recovery_kind` enums live.
- Carry into the phase-3 plan: V5 routine-task list (§5.2) scoped to built views; first-baseline report format (min/median/max, `not_captured`) in `docs/verification.md` R1-ACC-11; V17-1 evidence.
- Roadmap: the "Measurement and validation" and "Commercial activation" sections are inserted by the lead; ensure CA-1…CA-10 appear at the R4/phase-11 gate and OQ-G1/OQ-G2 in the owner decision list.
- Checks that must be repeated: EV-G09 price scan on materialized roadmap sections; confirm GM-1…GM-12 each appear in the materialized handoff (EV-G02 follow-up).

## 12. Human actions and production approvals

Owner decisions only; no secrets, no production actions:

- OQ-4 — tier public labels (before any tier UI, R4).
- OQ-G1 — appetite for a public build-log / community presence (record only; earliest relevance R2).
- OQ-G2 — legal basis and notice text for member-level usage measurement before the first non-founder seat (R2).
- Approval of any GTM draft before publication (phase plan §17 row).
- Two separate future decisions: publish rates; activate charges (CA-10, R4).
- Carried from Security: H-4 provider terms (DRR-06) and H-5 Hermes licence (LIC-05) are Growth prerequisites CA-6/CA-5.

## 13. Proposed state and memory updates

For lead verification and materialization:

- `.cursor/STATE.md`: T0-10 Growth → complete, verdict CONDITIONAL; active role → `project-lead-subagent` after T0-11; add `docs/roadmap.md` to files in active use once created; next action: T0-11 roadmap then T0-12 PL gate.
- Manifest §5: Growth row → `CONDITIONAL (2026-09-10T17:58Z)`, handoff path `growth-marketing-subagent/handoff.md` → `docs/roadmap.md` measurement/commercial sections. §6: REQ-05 → `in_progress` (Growth communication/measurement delivered; activation R4); REQ-06 evidence adds this handoff §5.2. §10: add `provisional` A-G2…A-G4. §11: add F-G1 (Security schema review, phase 1). §14 pending: add OQ-G1, OQ-G2. §13: none new beyond OQ items.
- Phase 0 plan §20: T0-10 completion evidence — `rg -c GM → 12`; price scan clean (exit 1); 7 views mapped; 43 rows; verdict CONDITIONAL 17:58Z. §17 queue: OQ-4 deadline moves to "before any tier UI (R4)"; add OQ-G1, OQ-G2.
- `docs/verification.md` §role table: Growth row → CONDITIONAL, evidence path, "EV-G01…EV-G15; taxonomy 9 rows; 18 event families; GM-1…GM-12 adopted; F-G1 Security schema review phase 1".
- `.cursor/memory/memories/2026-09-10-continuation.md`: append T0-10 completion (timestamps, verdict, F-G1, OQ-G1/G2).
- `.cursor/memory/MEMORY.md`: durable directive candidate — "Usage measurement is first-party, in-tenant, identifier/enum only (GM-1); every threshold without data is labelled `first-baseline`; no price appears in any UI or document before the R4 commercial gate."
- Decision record candidate (later): `docs/decisions/<date>-usage-event-schema.md` after Security review (F-G1).

## 14. Verdict

**CONDITIONAL.**

Justification against charter §9:
- Positioning cites sources — met (blueprint §3/§5 sources + one primary fetch; secondary rows labelled; EV-G04).
- Each metric has definition, unit, event source, owner — met, plus privacy class, consent note, first-baseline rule (§5.3; EV-G06).
- Event names follow one convention — met (§5.4.1; EV-G08).
- Thresholds labelled `first-baseline` where no data exists — met (§5.2; EV-G05, EV-G15).
- Tier communication has no prices — met (§5.6; EV-G09).
- Ethics constraints explicit — met (§5.7, GM-7…GM-10 cited; EV-G14).
- Nothing published — met (EV-G13).
- Fabricated data — none (EV-G03).

Not PASS: F-G1 (Security schema review of extension fields, phase 1) and F-G4 (OQ-4) are pending with named owners and deadlines. Not BLOCKED: all inputs present; no unsupported claim; the six intake metrics remain derivable even if F-G1 is refused. Conditions: (1) Security reviews §5.4.2–5.4.4 before any event is emitted; (2) positioning remains DRAFT until R1-ACC-3/6/7/8 are VERIFIED; (3) no tier label beyond "Tier 1–4" appears until OQ-4; (4) the phase-2/3 plans carry the V4 capture rule and V5 task list.
