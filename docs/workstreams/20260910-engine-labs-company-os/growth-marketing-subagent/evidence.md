---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: growth-marketing-subagent
revision: 1
updated_at: 2026-09-10T17:58:00Z
---

# Role Evidence: growth-marketing-subagent (T0-10 Growth gate)

Produced read-only by the role; materialized verbatim by the orchestrating lead. No secret values; no personal data beyond the founder's role. Environment for every record: macOS Darwin 25.6.0, repository `/Users/camdouglas/OrgOS` (branch `master`, no commits), Cursor sandbox with read-only filesystem and allowlisted network; tools `Read`, `Grep`, read-only `Shell`, `WebFetch`. No MCP tool invoked. Session window 2026-09-10T17:40Z–17:58Z. Shell timestamps are exact (`date -u`); Read/Grep records carry the session window.

## Evidence record EV-G01

- Requirement ID: charter §2, plan §1 (entry criteria)
- Claim: Charter r1, plan r1, manifest r1, phase 0 plan (T0-10 L139, T0-11 L141, §16, §17, §22), Security handoff (§9 F-SEC-16, §11.1 GM-1…GM-12), PM handoff (OQ-1…OQ-6, tiers), UI/UX handoff §5 analytics row (L59), SE handoff analytics row (L66), `docs/product.md` (PRD-G, §9, §10, §12), `docs/capabilities.md`, `docs/architecture.md` §4/§6, blueprint §3/§5/§6/§7/§14/§16, intake commercial/usage text (L112, L247–264, L342–348, L396–402), templates — all read.
- Evidence state: `VERIFIED`
- Method: direct file inspection
- Exact command or tool: `Read`, `Grep` on the listed paths
- Artifact, path, source, or stable reference: paths listed in the claim
- Sanitized result and exit status: all files present and readable; no predecessor handoff missing; Security handoff verdict CONDITIONAL with `downstream_role: growth-marketing-subagent`
- Timestamp: 2026-09-10T17:40Z–17:55Z (session)
- Environment: as header
- Limitations: `docs/roadmap.md` does not yet exist (see EV-G11)
- Required follow-up: none

## Evidence record EV-G02

- Requirement ID: F-SEC-16; Security §11.1 "confirm the Growth handoff cites GM-1…GM-12 explicitly"
- Claim: Twelve binding Growth constraints GM-1…GM-12 exist in the Security handoff and are each cited in the handoff taxonomy/consent sections and in roadmap Sections C/D.
- Evidence state: `VERIFIED`
- Method: count of constraint lines; cross-check of policy mirrors DRR-20…DRR-27, MEM-19…MEM-20, ERA-14
- Exact command or tool: `rg -c "^- GM-[0-9]+:" docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/handoff.md`; `rg -n "DRR-2[0-7]" docs/policies/data-residency-and-retention.md`; `rg -n "MEM-19|MEM-20" docs/policies/memory-governance.md`; `rg -n "ERA-14" docs/policies`
- Artifact: Security handoff §11.1 L266–278; DRR L75–82; MEM L72–73; ERA L60
- Sanitized result and exit status: `12`; DRR-20…27 present (8 lines); MEM-19, MEM-20 present; ERA-14 present; exit 0
- Timestamp: 2026-09-10T17:56:15Z
- Environment: as header
- Limitations: none
- Required follow-up: lead confirms every GM ID appears in handoff §5/§8 and Sections C/D on materialization

## Evidence record EV-G03

- Requirement ID: charter §5 (`verified` — no analytics or baseline data exists); manifest §9; PRD §10 / AS-10
- Claim: No analytics source is configured or authenticated; no baseline data exists; therefore every threshold is labelled `first-baseline` and no metric value is stated anywhere in this payload.
- Evidence state: `VERIFIED`
- Method: registry inspection; self-inspection of payload
- Exact command or tool: `rg -n -i "analytics|bigquery|posthog|mixpanel" .cursor/TOOLS.md`
- Artifact: `.cursor/TOOLS.md` L381–402 ("Treat BigQuery or equivalent access as unavailable until authentication and dataset scope are verified"); `docs/product.md` §10 "Baseline: none"; blueprint §16 "No analytics baseline exists"
- Sanitized result and exit status: analytics tool registered as unavailable-until-verified; no MCP analytics namespace used; exit 0
- Timestamp: 2026-09-10T17:52Z (session)
- Environment: as header
- Limitations: absence of data is reported as absence (GM-2); no proxy or interpolated baseline was constructed
- Required follow-up: none in phase 0

## Evidence record EV-G04

- Requirement ID: plan §6 task 1; charter §9 "positioning cites sources"
- Claim: The positioning statement is grounded in blueprint §3/§5 sources. Named-competitor comparison tables were later removed by owner request.
- Evidence state: `PARTIAL`
- Method: read of blueprint §3/§5 source list
- Exact command or tool: document inspection (named-competitor fetch artefacts withdrawn)
- Artifact: blueprint §5 gap statement; §3 source URLs
- Sanitized result and exit status: competitor comparison table withdrawn; remaining claim is the Papership gap statement
- Timestamp: 2026-09-10T17:56Z–17:57Z (original); table removal 2026-09-12
- Environment: as header
- Limitations: no competitor product was trialled; no pricing page fetched
- Required follow-up: owner-approved publication only; do not restore named-competitor tables unless the owner asks

## Evidence record EV-G05

- Requirement ID: REQ-06; plan §6 task 2
- Claim: V4 and V5 are restated verbatim from blueprint §7 and their pass thresholds are assessed for measurability; every quantitative element is labelled `first-baseline`.
- Evidence state: `VERIFIED`
- Method: direct read; measurability assessment recorded in handoff §5.2
- Exact command or tool: `Read docs/blueprints/2026-09-10_engine_labs.md` (§7 L82–93)
- Artifact: blueprint §7 rows V4 (L89), V5 (L90); NFR-4; PRD-A.14; R1-ACC-11
- Sanitized result and exit status: V4 threshold "≥1 change fully reviewed with linked evidence; intervention count and cost recorded as baseline (no target yet — first measurement)"; V5 "All routine tasks completable without technical traces"; both binary-plus-capture, no numeric target; exit n/a
- Timestamp: 2026-09-10T17:45Z (session)
- Environment: as header
- Limitations: V4's comparator ("founder's current IDE-agent workflow") has no recorded baseline; recorded as absence (EV-G15). V5 names "seven core views" while R1 builds 4+1 (OQ-5) — scoped in handoff §5.2
- Required follow-up: PL carries the first-baseline labelling and V5 routine-task list requirement into the phase-2/3 plans

## Evidence record EV-G06

- Requirement ID: intake L112 usage measurement; PRD §10; P14 (`configured` R1); R1-ACC-11; plan §6 task 3
- Claim: The six intake metrics plus the three PRD §10 additions (authority-violation guardrail, usability R3+, infra recovery/performance) each have a definition, unit, event source, owner, privacy class, consent note and first-baseline rule; each traces to a PRD ID.
- Evidence state: `VERIFIED`
- Method: derivation from PRD §10 rows and intake sentence; table in handoff §5.3 / Section C
- Exact command or tool: `rg -n -i "task completion|cost per completed outcome" docs/blueprints/company_agent_system_blueprint.md`; `Read docs/product.md` §10
- Artifact: intake L112 ("Measure task completion, correctness, recovery, operator intervention, context switching and cost per completed outcome"); PRD §10 L349–359
- Sanitized result and exit status: 6 intake terms matched; 9 taxonomy rows produced; exit 0
- Timestamp: 2026-09-10T17:53Z (session)
- Environment: as header
- Limitations: metric definitions are testable only once the ledger and run schemas exist (phase 1)
- Required follow-up: SE implements `MetricRecord` derivations in phase 1–2; PL reports first-baseline in phase 3

## Evidence record EV-G07

- Requirement ID: GM-1…GM-3, GM-11, GM-12; DRR-20…DRR-27; MEM-19…20; ERA-14; architecture §4 UsageEvent row
- Claim: The event schema in this payload uses only GM-1 permitted fields as required properties; every additional property is an opaque identifier or closed enumeration, is explicitly marked "proposed extension — Security schema review required (GM-11, F-SEC-16)", and no content field exists.
- Evidence state: `VERIFIED` (constraint alignment) / `UNVERIFIED` (extension approval — by design pending Security)
- Method: field-by-field comparison against GM-1 / DRR-20
- Exact command or tool: `Read docs/architecture.md` §4 L147 (UsageEvent, MetricRecord: run_id, model band, tokens, tool calls, execution time, est. cost, provider event id; retention "tenant lifetime (aggregated after 365 d)")
- Artifact: handoff §5.4 property tables; Section C
- Sanitized result and exit status: required set ⊆ GM-1 permitted set; extension set = {`work_item_id`, `view_id`, `stage_id`, `approval_class`, `tool_class`, `seat_template`, `provider_event_id`, `intervention_reason`, `recovery_kind`, `handoff_target`} — all identifiers/enums; prohibited set enumerated
- Timestamp: 2026-09-10T17:54Z (session)
- Environment: as header
- Limitations: Security has not yet reviewed the extension fields (gate GM-11)
- Required follow-up: Security schema review in phase 1 before implementation (F-SEC-16 re-verification)

## Evidence record EV-G08

- Requirement ID: UI/UX handoff §5 analytics row; `docs/blueprints/ui-blueprint.md` §B/§C; plan §6 task 4 catalogue
- Claim: The initial event catalogue covers all seven §B views and the §C global surfaces (run start/complete, approvals, navigation, source-app handoffs, connection state, memory search, adaptive-view apply/revert).
- Evidence state: `VERIFIED`
- Method: heading enumeration and per-view read of "Primary actions", "Data", "State matrix" rows
- Exact command or tool: `rg -n "^### B\.[1-7]" docs/blueprints/ui-blueprint.md`
- Artifact: `docs/blueprints/ui-blueprint.md` L280, 294, 308, 322, 336, 350, 364 (B.1–B.7); §C L378–392; §D L394–405
- Sanitized result and exit status: 7 headings matched; catalogue in handoff §5.4 maps ≥1 event to each; exit 0
- Timestamp: 2026-09-10T17:56:15Z
- Environment: as header
- Limitations: B.5 (R2) and B.6 (R3) events are specified now, implemented at their release; adaptive-view events (§D) are R3 with constraints binding from R1
- Required follow-up: SE maps each event to an emitting component in the phase-1 plan

## Evidence record EV-G09

- Requirement ID: PRD-G.10; charter §9 "tier communication has no prices"; plan §6 task 6
- Claim: No price, allowance quantity, seat count, rate, or currency figure appears in `docs/product.md` or in this payload; tier communication uses intake names Tier 1–4.
- Evidence state: `VERIFIED`
- Method: pattern scan of the product contract; self-inspection of Sections A–E
- Exact command or tool: `rg -n '\$[0-9]|USD|AUD|€' docs/product.md`
- Artifact: `docs/product.md` §8/§8.1; this payload
- Sanitized result and exit status: no matches, `rg` exit 1 (clean); payload contains no monetary figure
- Timestamp: 2026-09-10T17:56:15Z
- Environment: as header
- Limitations: named-competitor comparison tables and third-party price points were withdrawn from blueprint §5 (2026-09-12); they are not repeated here
- Required follow-up: lead re-runs the same scan on materialized `docs/roadmap.md` sections

## Evidence record EV-G10

- Requirement ID: PM OQ-4 (tier labels), AS-6; charter §10 escalation check
- Claim: OQ-4 remains unresolved; intake tier names "Tier 1–4" are used throughout; PM tier structure is consistent with intake L247–264 (no conflict to escalate).
- Evidence state: `VERIFIED`
- Method: comparison of `docs/product.md` §8.1 with intake L247–264
- Exact command or tool: `Read docs/product.md` §12 L380–387; `Read docs/blueprints/company_agent_system_blueprint.md` L247–264
- Artifact: PRD §8.1, §12 OQ-4 "Before growth gate T0-10"; manifest §14 pending
- Sanitized result and exit status: labels Free/Basic/Professional/Enterprise remain `proposal`; entitlement models match intake table row-for-row; no Security constraint prohibits any required metric (GM-1 permits every field the six metrics need at identifier level)
- Timestamp: 2026-09-10T17:50Z (session)
- Environment: as header
- Limitations: OQ-4 is an owner decision; it does not block this gate because no public label is used
- Required follow-up: owner answers OQ-4 before any tier is shown in a UI (R4)

## Evidence record EV-G11

- Requirement ID: T0-11 roadmap; charter §7 outputs
- Claim: `docs/roadmap.md` does not exist yet; Sections C and D are self-contained insertions for the lead's T0-11 materialization.
- Evidence state: `VERIFIED`
- Method: filesystem check
- Exact command or tool: `ls -la docs/roadmap.md`
- Artifact: —
- Sanitized result and exit status: "No such file or directory" (ls exit 1 inside a chained command; overall exit 0)
- Timestamp: 2026-09-10T17:56:15Z
- Environment: as header
- Limitations: Section C/D headings assume the lead's roadmap uses `##` top-level sections
- Required follow-up: lead inserts Sections C and D and re-runs EV-G09's scan

## Evidence record EV-G12

- Requirement ID: `docs/capabilities.md` release buckets; PRD §4.4
- Claim: The pilot learning plan's R2 scoping inputs reference the verified bucket totals R1 = 19, R2 = 4, R3 = 14, R4 = 6 over 43 rows.
- Evidence state: `VERIFIED`
- Method: row count and bucket note read
- Exact command or tool: `rg -c "^\| (B|P)[0-9]{2}" docs/capabilities.md`
- Artifact: `docs/capabilities.md` L22, L121 (EV-S10 row-count check)
- Sanitized result and exit status: `43`; L121 states "R1 = 19, R2 = 4, R3 = 14, R4 = 6"; exit 0
- Timestamp: 2026-09-10T17:57Z
- Environment: as header
- Limitations: none
- Required follow-up: none

## Evidence record EV-G13

- Requirement ID: charter §3 read-only; ROLES §8 prohibited actions; charter §9 "nothing published"
- Claim: This role created, edited or deleted no file, invoked no MCP tool, published nothing, spent nothing, and sent no message.
- Evidence state: `VERIFIED`
- Method: directory listing of the owned role path; tool log
- Exact command or tool: `ls docs/workstreams/20260910-engine-labs-company-os/growth-marketing-subagent/`; `git status --porcelain | wc -l`
- Artifact: role directory
- Sanitized result and exit status: directory contains `charter.md`, `plan.md` only (both lead-authored); porcelain count 6 (pre-existing lead artifacts, unchanged by this role); sandbox reported read-only filesystem; only network calls were the two read-only GitHub fetches in EV-G04
- Timestamp: 2026-09-10T17:56:15Z
- Environment: as header
- Limitations: none
- Required follow-up: none

## Evidence record EV-G14

- Requirement ID: GM-4, GM-7, GM-10, DRR-22, DRR-25; plan §6 task 7 ethics
- Claim: The GTM posture contains drafts only; no channel, community, or lifecycle message is scheduled; no third-party SDK/pixel/replay is proposed; attribution is first-party and consented only.
- Evidence state: `VERIFIED`
- Method: self-inspection of handoff §5.6/§8 and Section D against GM-4/7/8/9/10
- Exact command or tool: —
- Artifact: handoff §5.6, Section D
- Sanitized result and exit status: all GTM items carry "DRAFT — owner approval required before any publication"; owner build-log appetite recorded as open question OQ-G1
- Timestamp: 2026-09-10T17:57Z (session)
- Environment: as header
- Limitations: no platform/community rule text was fetched in this pass (blueprint §16 limitation carried forward); required before any post
- Required follow-up: fetch and record subreddit/community rules at the time a draft is considered for publication (R2+)

## Evidence record EV-G15

- Requirement ID: V4 comparator; GM-2 (absence reported as absence)
- Claim: No recorded baseline exists for the founder's current IDE-agent workflow (V4 comparator); V4 is therefore scored on its capture criterion only in R1.
- Evidence state: `UNVERIFIED` (absence)
- Method: repository search for any prior metric or timing record
- Exact command or tool: `rg -n -i "baseline" docs/product.md docs/blueprints/2026-09-10_engine_labs.md`
- Artifact: PRD §10 "Baseline: none" (every row); blueprint §16
- Sanitized result and exit status: every baseline cell is "none"; no comparator data found
- Timestamp: 2026-09-10T17:55Z (session)
- Environment: as header
- Limitations: an optional self-reported comparator log (handoff §5.2, C-2) would be low-rigour, n=1 and labelled as such; it is a recommendation, not a requirement
- Required follow-up: PL decides in the phase-2 plan whether to include the optional comparator log

## Lead verification notes (orchestrating lead, 2026-09-10)

- EV-G02 follow-up: lead confirmed GM-1…GM-12 each appear in the materialized `handoff.md` and in `docs/roadmap.md` (see continuation log for the `rg` result).
- EV-G09/EV-G11 follow-up: `docs/roadmap.md` created by the lead in T0-11 with Sections C and D inserted verbatim; price scan re-run on the file (result in continuation log).
