# Decision D-05: Release-1 scope boundary

## Status

`proposed` — drafted 2026-09-10 by the orchestrating lead (T0-11) from `product-manager-subagent` T0-6 output (`docs/product.md` §4, §9) and the roadmap (`docs/roadmap.md` §2.1). For owner ratification at the phase-0 Project Lead gate (T0-12). Owner open question OQ-5 (R1 view set) and OQ-3 (phase-to-release numbering for 09–12) may amend items 3 and 6 without reopening the rest.

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md`. Phase plan: `docs/plans/phase_0_foundations_plan.md` §7 ("D-05 release-1 scope boundary (07+08 only)").

## Context

The intake sets "the first release around implementation phases 07–08 and their required controls" and assigns later capabilities to subsequent releases while keeping them visible as `planned` (intake Phase 06; I-06). The blueprint's no-build criterion is that the governed loop must complete one real Engine Labs change with linked evidence and bounded authority before any expansion (blueprint §15). Scope pull toward the 43 domains before the loop works is the named product risk.

## Decision

Release 1 consists of intake implementation phases **07 Foundation** and **08 Development loop**, verified by phases 13–18 for the enabled scope, and nothing else:

1. **Registry scope** — the 19 rows bucketed R1 in `docs/capabilities.md`; the maximum status any R1 row may reach is the "R1 target" column (several rows target `configured`, e.g. usage measurement P14). The remaining 24 rows (R2 = 4, R3 = 14, R4 = 6) stay `planned` and visible in the registry view (PRD-C.5).
2. **Loop** — the 11-stage development loop of PRD-B.1 executed against this repository (OQ-1) with GitHub as the only permissioned source; one real Engine Labs change completed end-to-end with sponsored, scoped, budgeted run, action-bound approval, receipts and linked evidence (R1-ACC-6); zero duplicated external effects under interruption (PRD-B.7, V3).
3. **Views** — home, work item, assistant, agent run and a minimal permissions editor (owner grants) — the `proposal` in PRD-A.15 pending OQ-5; connection setup (B.5) and memory manager (B.6) are specified in phase 0 and built in R2/R3. Primary tabs per D-06.
4. **Deployment** — single-tenant, self-hosted, one DigitalOcean Droplet per customer with Docker Compose networks `edge`/`app`/`data`/`worker`; only the Engine Labs API and Supabase Auth published (architecture §10; AUTH-20).
5. **Agents** — one Hermes-backed agent behind the adapter (D-04) with read-only toolsets until the interception spike passes Security re-review (AUTH-25); no delegation between agents, no scheduling, no additional connectors.
6. **Commercial** — usage measurement `configured` (first-baseline capture per `docs/roadmap.md` §3); no entitlement enforcement, no billing, no prices, no tier UI (PRD-G.10); tiers referred to as Tier 1–4 (OQ-4).
7. **Users** — the founder only (Founder seat); no invited seats (R2).
8. **Explicit non-goals for R1** — memory manager and adaptive views (R3), connectors beyond GitHub (R2), mobile clients and SDK (R4), commercial activation (R4), multi-tenant hosting, any public launch or publication.

Any addition to R1 scope requires a decision record superseding this one and a PL gate re-check; removal of an R1 item requires the same plus an update to `docs/capabilities.md` buckets.

## Alternatives considered

1. **R1 = phases 07–09 (include collaboration and connections).** Rejected: contradicts the intake's `verified` R1 definition and the no-build criterion; connectors multiply the authority-intersection and erasure surface before the loop is proven.
2. **R1 = phase 07 only (foundation without the loop).** Rejected: the loop is the value hypothesis (V4) and the only evidence that can inform R2 scope and pricing (Growth §5.5); a foundation-only release produces no first baseline.
3. **Seven views in R1.** Rejected pending OQ-5: B.5 and B.6 depend on R2/R3 capabilities (connections, memory manager) that would ship as simulated controls, which AUTH-28 prohibits.

## Consequences

- Positive: bounded blast radius for agent-authored change; every R1 acceptance row (R1-ACC-1…15) maps to a phase-1/2/3 task; the registry shows honestly what is not yet available.
- Negative / costs: R1 has one user and no external validation beyond the founder; several intake capabilities remain `planned` for a full release cycle.
- Follow-ups: `phase_1_foundation_plan.md` (phase 07) generated after the phase-0 PL verdict; `phase_2_development_loop_plan.md` (phase 08); `phase_3_release_verification_plan.md` (13–18); OQ-3 and OQ-5 answers recorded as amendments.

## Evidence and citations

- Intake: `docs/Company_Agent_System_Blueprint.md` Phase 06 (release scope), Phases 07–08.
- `docs/product.md` §4.1 (release definition, `verified` R1), §4.2 (bucket rule), §4.3–§4.4 (43 rows), §9 (R1-ACC-1…15), §12 (OQ-3, OQ-5), PRD-A.15, PRD-G.10.
- `docs/capabilities.md` L121 bucket totals (R1 = 19, R2 = 4, R3 = 14, R4 = 6).
- `docs/blueprints/2026-09-10_engine_labs.md` §9 (MVP scope and non-goals), §13, §15 (no-build criteria).
- `docs/roadmap.md` §1–§2.
- PM handoff `docs/workstreams/20260910-engine-labs-company-os/product-manager-subagent/handoff.md` §13 (D-05 candidate).
