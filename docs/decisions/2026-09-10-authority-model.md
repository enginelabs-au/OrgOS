# Decision D-03: Authority model

## Status

`proposed` — drafted 2026-09-10 by the orchestrating lead (T0-11) from `security-engineer-subagent` T0-9 output (`docs/policies/authority-model.md`, AUTH-01…AUTH-30; handoff findings F-SEC-01, F-SEC-04, F-SEC-05, decision D-S1) and `product-manager-subagent` T0-6 output (`docs/product.md` PRD-D, PRD-E). For owner ratification at the phase-0 Project Lead gate (T0-12) — Security owner action H-6. Adoption of this decision adopts `docs/policies/authority-model.md` as a normative policy.

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md`. Phase plan: `docs/plans/phase_0_foundations_plan.md` §7 ("D-03 authority model (three seats, server-side checks, source-permission intersection)").

## Context

The intake requires that "authority derives from grants, not titles", that the hierarchy owner → lead → member be expressed as scoped grants, that agents act only under a sponsor's authority with recomputed effective grants, that every authorization decision be made server-side, and that approvals bind to the exact action and target version (intake Phase 03; PRD-D.1–D.13, PRD-E.2). Hermes exposes its own `/v1/runs/{id}/approval` endpoint and grants its full toolset (including terminal execution) to any holder of `API_SERVER_KEY`; the Security review found that neither can be the authority for Engine Labs decisions (F-SEC-01, F-SEC-04; T-18, T-30).

## Decision

1. **Four entities, one source of authority.** Seats, titles, seat templates and grants are distinct; authority derives from grants only (AUTH-01). Templates (Founder, Project Lead, Operator) are provisioning defaults; the resulting grants are recorded individually (AUTH-21).
2. **Three principal types.** Members, agents and service identities are distinct; agents have no interactive credentials; service identities are per-service (AUTH-05). Bearer infrastructure credentials (`HERMES_API_SERVER_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `DATABASE_URL`, `GITHUB_APP_PRIVATE_KEY_PATH`) are transport credentials and never authorization for any principal (AUTH-22).
3. **Agent authority is an intersection.** An agent's effective grants for a run = sponsor's current grants ∩ agent toolset ceiling ∩ grants permitted by the run mode, recomputed at every action step (AUTH-07); agents can never assign, delegate or request grants (AUTH-08). Every run records the nine PRD-E.2 fields (AUTH-06).
4. **Approvals are grants bound to actions.** Approval authority is a grant class `approval.<action-class>` (initial classes `repo.change`, `repo.release`, `data.export`, `data.erase`, `org.admin`, `billing.admin`, `connector.admin`); agents cannot hold any `approval.*` grant, enforced by database constraint and API check (AUTH-09). An approval record binds to a single action id and a hash of (action type, canonical parameters, target id, target version, policy version), recomputed before execution (AUTH-10). Separation of duties for `repo.release`, `data.erase`, `billing.admin`, `org.admin` (AUTH-11). **The Engine Labs API owns the approval record; Hermes `/approval` is never the approval authority** (AUTH-11a, D-S1).
5. **Server-side enforcement everywhere.** Every authorization decision — records, search, aggregates, counts, attachments, notifications, memory retrieval — is made in the Engine Labs API; the desktop is never trusted and hidden UI is not authorization (AUTH-12). For permissioned sources bound in R1 (GitHub) effective authority = Engine Labs grant ∩ source permission, checked before any token is minted (AUTH-12; PRD-D.6 brought forward). Search and counts never reveal unauthorized records (AUTH-17). No simulated authorization or approval control ships (AUTH-28).
6. **Session and data-layer posture.** Access tokens ≤ 15 min, rotating refresh with reuse detection, grant-version check per request and per action step, revocation ≤ 60 s (AUTH-13); desktop purge on sign-out or grant-version change (AUTH-14); INSERT-only audit for every grant/refuse/approve decision (AUTH-15); strong authentication for Founder/Project Lead and for holders of sensitive grants, with reauthentication ≤ 5 min for `data.erase`, `billing.admin`, `org.admin` changes and `repo.release` approvals (AUTH-16); API role non-superuser without `BYPASSRLS`, `SET LOCAL` tenant/principal context, RLS on every tenant-scoped table (AUTH-19); only API + Auth on the `edge` network (AUTH-20).
7. **Runtime boundaries.** Worker and Hermes containers hold no database credentials and are not on the `data` network (AUTH-24); side-effecting Hermes toolsets stay disabled and their registry rows `unavailable` until the phase-2 interception spike (SP-1…SP-7) passes Security re-review; the worker refuses to start otherwise (AUTH-25).
8. **Desktop posture.** Tokens only in the OS keychain via the Tauri secure-storage plugin (AUTH-26); the reference `cc-org-dash-auth` localStorage session, browser-stored provider keys, Security-tab API keys, demo credentials and Google sign-in do not exist in the product (AUTH-27); adaptive views are schema-validated definitions with no filesystem/shell/database/credential access (AUTH-29); minimal Tauri capabilities reviewed by Security (AUTH-30).

## Alternatives considered

1. **Role-based access control with titles as roles.** Rejected: the intake states authority derives from grants, not titles; titles would become a second implicit authority path (PRD-D.4).
2. **Delegate approvals to Hermes `/v1/runs/{id}/approval`.** Rejected: the endpoint has no Engine Labs grant model, no action/version binding and is reachable with the same bearer key that grants terminal execution (F-SEC-01, F-SEC-04, T-30). Hermes may receive a forwarded decision only after the Engine Labs record exists (D-04 decision 6).
3. **Client-side permission gating (hide controls the user lacks).** Rejected as authorization; permitted only as a presentation convenience on top of server-side checks (AUTH-12, AUTH-28).
4. **Single shared service identity across API, worker and jobs.** Rejected: per-service identities with separate secrets are required to keep the worker away from database credentials (AUTH-05, AUTH-24; TB-3/TB-4).

## Consequences

- Positive: one enforceable model across API, desktop, worker and Hermes; approval integrity independent of the runtime vendor; agents are structurally unable to escalate; audit is complete by construction.
- Negative / costs: schema constraints, hash recomputation and per-step grant recomputation add phase-1 work and per-action latency; the phase-2 interception spike gates all side-effecting agent capabilities (registry rows stay `unavailable` until it passes).
- Follow-ups: phase-1 tests listed in `docs/policies/authority-model.md` §5; F-SEC-04 approval-grant schema constraint; F-SEC-05 GitHub intersection; SP-1…SP-7 spike in phase 2; this decision is superseded only by a later decision record referencing the AUTH identifiers it changes.

## Evidence and citations

- Intake: `docs/Company_Agent_System_Blueprint.md` Phase 03 (authority model), Phase 05 (agents and sponsorship), Phase 14 (verification of authority).
- `docs/product.md` PRD-D.1–D.13, PRD-E.2–E.3, R1-ACC-4, R1-ACC-6.
- `docs/policies/authority-model.md` AUTH-01…AUTH-30 (normative text adopted by this decision).
- Security handoff `docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/handoff.md` §9 F-SEC-01, F-SEC-02, F-SEC-04, F-SEC-05, F-SEC-06; §8 D-S1; threats T-18, T-30; §12 H-6; §13 decision candidate.
- `docs/decisions/2026-09-10-hermes-adapter-contract.md` (D-04) decision 6 (approval forwarding).
- `docs/architecture.md` §5–§7 (trust boundaries TB-1…TB-13; network segmentation).
