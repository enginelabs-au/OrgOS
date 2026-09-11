---
blueprint: engine_labs
status: accepted_for_phase_0
created: 2026-09-10
updated: 2026-09-10
owner: lead-agent (orchestrating)
intake: docs/Company_Agent_System_Blueprint.md
workstream: docs/workstreams/20260910-engine-labs-company-os/manifest.md
phase_0_plan: docs/plans/phase_0_foundations_plan.md
---

# Engine Labs — Strategy and Systems Blueprint

This document is the evidence-based strategy assessment required by `.cursor/instructions/STRATEGY.md`. It does not restate the product intake; it assesses it. The complete product requirements, all 43 domain groups (B01–B24, P01–P19), the seat templates, the connection requirements, the commercial tiers, and the eighteen blueprint phases are canonical in [`docs/Company_Agent_System_Blueprint.md`](../Company_Agent_System_Blueprint.md) and are preserved in full. The versioned capability registry that materializes that scope is `docs/capabilities.md` (phase 0 output).

## 1. Executive decision

**Build**, with the first release deliberately narrowed to a founder-only development loop.

Engine Labs is an operator-led company operating system: one desktop client, a cloud execution plane, a universal assistant backed by Hermes, a governed action ledger, and a capability registry spanning business and platform domains. The market evidence supports the underlying thesis: founders and small teams adopting agents are converging on the same unmet needs — attributable identity per agent, least-privilege grants, approval queues bound to specific actions, replayable audit trails, and one canonical context layer — and the products that exist today either give you primitives without a product (Paperclip, LangGraph, CrewAI), a product without company-level governance (Lindy), or an enterprise workforce platform priced and positioned for 50+ person ops teams (Relevance AI).

The strategic wedge is not "another agent platform". It is a **company operating system that treats authority, provenance, and recovery as the product**, starts with the one workflow the founder does every day (shipping changes to the company's own software), and expands into connected business domains only after that loop is verified.

Two decisions govern the release plan:

1. **Release 1 = blueprint phases 07 + 08.** Founder signs in, plans work, runs a persisted cloud job, reconnects to it, and completes a real Engine Labs change through the governed loop. Nothing commercial is activated.
2. **The full 43-domain registry is scope, not a promise.** Every domain is registered with status `planned` and stays visible; only demonstrated, verified workflows move to `working`.

## 2. Evidence and research method

Performed on 2026-09-10 by the orchestrating lead (read-only):

- Repository intake: full read of `docs/Company_Agent_System_Blueprint.md`; inspection of the UI reference [enginelabs-au/Papership](https://github.com/enginelabs-au/OrgOS) at commit `8a843bd6429faf1ace5a9eb6dcfb7440703d34c4` via GitHub MCP (`package.json`, `README.md`, `src/App.jsx`, `src/pages/`, `src/components/cc-org-dash/`, `src/lib/AuthContext.jsx`, `src/api/entities.js`).
- Primary documentation: Hermes Agent API server ([docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server)), DBOS Python programming guide ([docs](https://docs.dbos.dev/python/programming-guide)), Tauri 2 overview ([docs](https://v2.tauri.app/start/)).
- Market scan: two web searches (agent company-OS platforms for founders; founder pain points around approvals, audit, and access sprawl) yielding six third-party comparison/analysis sources and the Paperclip repository README.

Not performed (recorded as limitations in §16): community/Reddit thread analysis, customer interviews, analytics queries, pricing benchmarks beyond the sources above, Hermes version-pinned capability inventory (phase 0 SE task), Figma inspection (no design file exists).

## 3. Intelligence report

### Demand signals

- Governance is becoming the selling point. Enterprise buyers now ask "what happens when it's wrong, and who signed off before it acted?" and vendors without an approval trail lose deals regardless of model quality ([Startup Fortune](https://startupfortune.com/why-ai-agent-approval-queues-are-replacing-full-autonomy-for-founders/)). The same source documents the July 2025 Replit incident in which a coding agent deleted a production database despite explicit instructions — the canonical cautionary tale in this segment.
- Access sprawl is a named category. Solo builders accumulate long-lived, over-scoped credentials in env files, CI logs, and agent memory; the recommended fix is per-agent identity, short-lived scoped tokens, and every privileged action logged with agent id and task id ([dreaming.press](https://dreaming.press/posts/act-security-60m-agent-access-sprawl-what-founders-do.html)).
- Runtime governance pattern: policy check at every tool call, delegated per-action authority "with a name attached", replayable audit streamed to observability tooling ([Arcade](https://www.arcade.dev/blog/one-question-every-tool-call/)); role-scoped agent-to-tool access with approval workflows for sensitive actions ([Agen](https://agen.co/blog/govern-ai-agents-across-enterprise-apps)).
- Shared canonical context is the underspecified dimension: identity, scope, shared context, audit trail — with drift detection across agents as the early-warning system ([Improvado](https://improvado.io/blog/ai-agent-governance), citing Gartner April 2026 on agent sprawl).

### Implication

The intake's action lifecycle (retrieve authorised context → typed action → validate scope → approval bound to action and target version → reserve budget → execute → verify → receipt) and its insistence that "prompts are not security boundaries" are aligned with where the market is moving, not ahead of it. The differentiation must come from execution quality and from binding governance to real company records, not from the governance concept itself.

## 4. User and problem definition

- **Primary user (release 1):** the founder of Engine Labs, operating as owner seat, building Engine Labs itself.
- **Job to be done:** turn a product request into a shipped, reviewed, monitored change to the company's own software with agents doing the work under bounded authority, without losing the audit trail or duplicating external effects when things fail.
- **Problem today:** agent work happens across disconnected tools (IDE agents, chat assistants, CI, repository, tickets); authority is implicit in whichever credential is in the environment; recovery after a failed step is manual; nothing retains the decision history as company knowledge.
- **Desired outcome:** one operating framework where every run has a sponsor, scope, budget, and receipt; where the desktop can be closed without losing the job; and where the result is a reviewable change with linked evidence.
- **Later users:** Project Lead and Operator seats (release 2), then customer organisations across industries via connected applications and domain modules (releases 3–4).

## 5. Competitive landscape and gap

| Alternative | Type | Where it stops | Source |
|---|---|---|---|
| Paperclip (MIT, self-hosted) | Agent org-chart coordination layer: agents with roles, budgets, heartbeats, approvals, audit; "not a chatbot" | Config-first; developer audience; no business-domain records; security posture not independently documented | [GitHub](https://github.com/paperclipai/paperclip/), [tycoon.us](https://tycoon.us/alternatives/paperclip), [creeta](https://news.creeta.com/en/paperclip-ai-agent-orchestration-platform-2026/) |
| Relevance AI | Hosted multi-agent workforce; RBAC, SSO, SOC 2, approvals, 1000+ integrations | Enterprise ops/GTM positioning; Team tier ~$349/mo; not a company OS with a work ledger | [zoeticai](https://www.zoeticai.com/guides/lindy-vs-relevance-ai-vs-dust/), creeta |
| Lindy | No-code personal productivity agents (~$49.99/mo) | Individual workflows; SMB SaaS limits on governance | zoeticai, [agentshortlist](https://agentshortlist.com/compare/lindy-vs-paperclip) |
| Dust | Team knowledge agents, per-seat | Knowledge-first, not execution/authority-first | zoeticai |
| LangGraph / CrewAI / OpenAI Agents SDK | Frameworks | Governance, persistence, and approvals are "an exercise for the developer" | creeta |
| n8n / Zapier Agents | Workflow automation with agent nodes | Automation graph, not a company model | creeta |
| Do nothing | IDE agent + chat + CI + tickets | No sponsor/budget/receipt model; manual recovery; no retained knowledge | intake |

**Gap:** no product combines (a) a real company work ledger and organisation model, (b) per-run sponsorship, scoped grants, and action-bound approvals, (c) durable cloud execution the operator can disconnect from, (d) an OS-quality desktop experience, and (e) retention of decisions as governed company memory — while remaining usable by a founder who is not standing up frameworks. Paperclip is the closest in philosophy and is the alternative Engine Labs must be measurably better than on operator experience, recovery, and business-record integration.

## 6. Unique value proposition and wedge

**Proposition:** "Run your company's work through agents you can actually hold accountable — every run sponsored, scoped, budgeted, and receipted, from a desktop you can close."

**Wedge:** the founder's own development loop (blueprint phase 08). It is the workflow the founder already performs daily, it exercises every governance primitive (identity, grants, isolated execution, approvals, receipts, recovery, retained knowledge), and it produces verifiable evidence (a merged, reviewed change) without needing a single external business connector.

**Expansion path:** seats and delegated authority → communication connectors (Gmail, Slack, Telegram, WhatsApp) → highest-value domain modules → commercial tiers → SDK and mobile. Each step is gated on demonstrated workflows, per the intake.

## 7. Validation experiments and thresholds

| # | Riskiest assumption | Experiment | Pass threshold | Phase |
|---|---|---|---|---|
| V1 | The Hermes runtime can be governed behind an adapter without forking it | Compatibility spike against the pinned Hermes version: runs API, SSE events, idempotency keys, stop, approval endpoint, session ownership, tool interception | All seven behaviours demonstrated with contract tests; no private-API dependency | 0 → 1 |
| V2 | Papership `/cc-org-dash` can become the Tauri desktop shell without visual regression | Run reference at pinned commit; capture states; load the same route inside Tauri 2 | Route loads and refreshes in the packaged app; screenshots match reference at matching viewport/theme | 0 → 1 |
| V3 | Durable jobs survive desktop disconnect and worker restart without duplicate external effects | Kill worker/desktop before and after a write to the founder repository | Zero duplicated effects across 20 interruption trials; recovery reconciles source state before retry | 2 |
| V4 | The governed loop is faster and safer than the founder's current IDE-agent workflow | Complete three real Engine Labs changes through the loop; measure operator interventions, context switches, wall time, cost per completed outcome | ≥1 change fully reviewed with linked evidence; intervention count and cost recorded as baseline (no target yet — first measurement) | 2 |
| V5 | Founder can operate the product without seeing prompts, schemas, or runtime config | Usability pass over the seven core views with the Founder seat | All routine tasks completable without technical traces | 3 |
| V6 | Self-hosted Supabase + DBOS + Hermes workers fit a single-droplet footprint | Measure database, browser, and worker resource consumption under realistic concurrency before selecting VPS size | Documented headroom; no swap under the pilot load | 3 |

Commercial assumptions (tier pricing, willingness to pay, connector distribution rights) are explicitly deferred to the commercial activation gate (blueprint phase 11) and are not tested in release 1.

## 8. Product requirements document

The PRD is materialized in `docs/product.md` (phase 0) from the intake and the `product-manager-subagent` handoff. It preserves the intake's requirement structure and adds unique requirement IDs:

- **PRD-A Framework:** identity, responsibility scopes, work coordination, conversations, agent supervision, memory governance, approvals, audit, connector administration, adaptive views, entitlements; minimal native work ledger (plans, assignments, dependencies, decisions, evidence). Specialist records stay in connected systems.
- **PRD-B Development loop:** request → research → specification → plan → assignment → isolated code change → tests → review → approved release → monitoring → retained knowledge, against the founder's repository.
- **PRD-C Capability registry:** every row of B01–B24 and P01–P19 with user outcome, native/connector owner, read/write actions, data authority, grants, dependencies, interface components, release phase, implementation status (`planned` / `configured` / `working` / `unavailable`), acceptance evidence.
- **PRD-D Authority model:** three seat templates; owner → lead → member; separation of titles, templates, grants; server-side row/field/action checks including search, aggregates, attachments, notifications, memory; intersection with source permissions and credential scope; provisioning/handover/revocation.
- **PRD-E Runtime:** run sponsorship fields; action lifecycle; isolation; recovery (two transient retries, one bounded diagnostic attempt); circuit breakers; escalation with evidence.
- **PRD-F Memory and lifecycle:** provenance fields; search/inspect/correct/merge/restrict/archive/export/delete; retention defaults (365/30/30 days); offboarding; scoped and organisation-wide erasure with receipts.
- **PRD-G Commercial:** four tiers; model-band allowances and monetary budgets; reservation and reconciliation; rate card; usage ledger; proprietary licence with upstream notices; SDK independently licensable. Design in release 1; activation gated.
- **Non-functional:** cloud execution independent of desktop connection; streamed progress; reconnect/resume; measurable recovery, performance, usability targets set from the pilot baseline.

## 9. MVP scope and non-goals

**Release 1 (required):** blueprint phases 07 and 08 — desktop shell from Papership reference; cloud API and data boundary; identity and owner seat; grant checks; capability registry; work ledger; job persistence; streamed status; secure desktop connection; pinned Hermes runtime behind the adapter; repository binding; the complete development loop with review evidence and release proposal; `GlobalAgentPanel` wired to backend-mediated sessions; contract tests at runtime, source-control, and action boundaries; usage measurement and lifecycle hooks in skeletal form.

**Required later (planned, visible):** phases 09–12 — seats, guests, delegated administration, communication connectors, provisioning-to-handover; domain modules, managed memory, schedules, adaptive views; customer deployment automation, tiers in test mode, backup/restore, offboarding, erasure; SDK, catalogue, iOS/Android.

**Explicitly excluded from release 1:** any external commercial commitment, published pricing, charge activation, production deployment to a customer, DNS, publishing, or marketing launch. The framework must be useful disconnected (organisation setup, planning, configuration, document intake) and must explain which outcomes need a connection.

## 10. System architecture and data model

Initial stack per intake, confirmed feasible against primary documentation (details and tradeoffs in `docs/architecture.md`, phase 0):

| Layer | Choice | Confirmation |
|---|---|---|
| Desktop | Tauri 2 + React + TypeScript + Vite; macOS first | Tauri 2 targets desktop and mobile with any HTML/JS frontend, uses the system webview, and is security-audited per release ([docs](https://v2.tauri.app/start/)) |
| UI | Papership `/cc-org-dash` shell and `src/components/cc-org-dash/*` migrated incrementally from JSX to TS | Reference is Vite 6 / React 18 / Tailwind 3.4 / Radix; typecheck currently runs `tsc -p jsconfig.json`; no TS sources yet |
| API | Python FastAPI, typed models, OpenAPI-generated client, streamed run events | Standard |
| Durable workflows | DBOS with PostgreSQL: checkpointed workflows/steps, queues, `DBOS.sleep`, recovery from last completed step | DBOS recommends Postgres in production via `DBOS_SYSTEM_DATABASE_URL`; FastAPI integration is first-class ([docs](https://docs.dbos.dev/python/programming-guide)) |
| Data/identity | Self-hosted Supabase (PostgreSQL, Auth, Storage) on the customer VPS | Intake requirement; compatibility spike in phase 0/1 |
| Execution | Isolated Hermes workers behind an Engine Labs runtime adapter and policy service | Hermes exposes `POST /v1/runs` with `Idempotency-Key` (durable reservation, replay with `Idempotency-Replayed: true`, 409 on payload conflict), SSE `/v1/runs/{id}/events` incl. `subagent.*` lifecycle, `/stop`, `/approval` (advertised via `/v1/capabilities` as `run_approval`), sessions API with turn leases, jobs API, bearer auth, `/health` ([docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server)) |
| Retrieval | PostgreSQL structured/full-text; pgvector only after retrieval evaluation justifies it | Intake |
| Deployment | Docker Compose on one DigitalOcean Droplet per customer; provider-portable | Intake; sizing after V6 |
| Operations | Structured logs, run traces, health checks, cost metrics, alerting, encrypted off-VPS backups, tested restores | Intake |

**Core entities (release 1):** Organisation, LegalEntity, Department, Team, Location, Project, Task, Member, Seat, Grant, ProviderAccount, Agent, Run, Step, Action, Approval, Receipt, Job, Decision, Evidence, MemoryItem, Capability, Connector, UsageEvent. Ownership, retention, and deletion behaviour are specified per entity in `docs/architecture.md`.

**Key boundaries:** Hermes API authentication is transport access only; per-tool authorisation is enforced by the Engine Labs action service via hooks or scoped tool adapters. Engine Labs owns dispatch, schedules, and approvals; Hermes scheduling/delegation is mapped into that ownership to prevent duplicate obligations. Company records never depend on Hermes' internal storage format. Provider secrets and privileged execution stay off the desktop; generated views never get filesystem, shell, database, or credential access.

## 11. Interfaces and integrations

- **Desktop ↔ API:** authenticated HTTPS + SSE (or WebSocket) for run events; secure token storage in the OS keychain via Tauri; signed releases and updates.
- **API ↔ Hermes:** private network; typed adapter over the documented runs/sessions/jobs endpoints; capability discovery via `/v1/capabilities`; tool interception via supported hooks; usage from run status.
- **API ↔ source control (release 1):** the founder's repository bound with scoped branch/PR/check operations; releases through the protocol's authorisation gates.
- **Connectors (release 2+):** versioned implementations of capabilities over official APIs, reviewed MCP servers, webhooks, polling, file intake, permitted DB access, source-app handoffs; browser automation as controlled fallback. Priority: repository/CI, Gmail (scoped OAuth; production scope review), Telegram, Slack, WhatsApp (Cloud API via Hermes adapter), web research.

## 12. Security, privacy, reliability, and compliance considerations

- Prompts, role names, and handoff verdicts are not authorisation. Enforcement is server-side grants, action policy, sandboxed execution, and the fail-closed development-time hooks already installed in this repository.
- Untrusted inputs: documents, messages, tool output, and retrieved memory are treated as untrusted; permissions live outside prompts.
- Isolation: separate agent profiles from execution isolation; credentials and orchestration databases outside agent mounts; least-privilege filesystem/network.
- Effects: idempotency keys where supported (Hermes runs API supports them natively); receipts persisted so recovery never blindly repeats; a remote write followed by a timeout is treated as potentially completed.
- Data: customer records, conversations, memory, artifacts, secrets, and execution state stay on the assigned VPS; encrypted backups in a separate client-controlled location; model/tool processing is a separate data destination under its own policy; no cross-customer learning by default.
- Retention defaults: conversations 365 days, execution/debug logs 30 days, rotating backups 30 days; visible and overridable by owners.
- Erasure: scoped with owner approval and impact preview; organisation-wide only after reauthentication and double confirmation; deletion receipt; pending backup/provider copies disclosed.
- Licensing: proprietary product licence; upstream notices preserved; dependency licence inventory; SDK independently licensable.

The `security-engineer-subagent` produces the threat model and authority-model review in phase 0 and independently gates each implementation phase.

## 13. Delivery phase map

Materialized in `docs/plans/phase_0_foundations_plan.md` and `docs/roadmap.md`:

| Execution plan | Blueprint coverage | Release |
|---|---|---|
| `phase_0_foundations_plan.md` | Planning 01–06, full roadmap, role routing, approved foundation/compatibility checks | 1 |
| `phase_1_foundation_plan.md` | Implementation 07 + applicable verification gates | 1 |
| `phase_2_development_loop_plan.md` | Implementation 08 + applicable verification gates | 1 |
| `phase_3_release_verification_plan.md` | Verification 13–18, first-release checklist, owner handoff | 1 |
| `phase_4+` | Implementation 09–12 mapped to later releases when approved; each with its own verification and closure | 2–4 |

Human-only actions (accounts, credentials, provider terms, DNS, billing) are deferred to the final phase of each release and consolidated in `docs/plans/final_implementation_checklist.md`.

## 14. Cultural go-to-market strategy

Release 1 has one user and no external launch; this section defines the posture that later releases inherit, without recommending any publication or spend now.

- **Where the audience gathers:** founder and indie-hacker communities, AI-agent builder communities, and open-source agent-orchestration repositories (Paperclip's 43k+ stars indicate the size of the interested developer audience). These communities reward transparent build logs, evidence, and honesty about failures; they punish undisclosed promotion.
- **Trust-building assets (draft-only, later releases):** the verified development-loop evidence itself (a real change shipped through the governed loop with its receipts), the authority-model and recovery documentation, and honest comparisons against Paperclip and Relevance AI on the dimensions where Engine Labs differs.
- **Launch sequence:** founder-only pilot → invited Project Lead/Operator seats → design partners in one sector → commercial activation with published rates. Each stage gated by verified workflows.
- **Reddit concepts (when relevant; drafts, never posted without owner approval):** (1) problem-first — "how do you keep agents from repeating an external write after a timeout?"; (2) transparent build journey — what the receipt/idempotency model looked like after 20 interruption trials; (3) resource-value — a free checklist for scoping agent credentials per task.
- **Ethics:** no astroturfing, deceptive scarcity, dark patterns, or rule evasion; all claims traceable to evidence.

The `growth-marketing-subagent` refines positioning, the measurement taxonomy (task completion, correctness, recovery, operator intervention, context switching, cost per completed outcome), and tier communication in phase 0; publishing remains an owner decision.

## 15. Risks, pivots, and no-build criteria

| Risk | Signal | Response |
|---|---|---|
| Hermes cannot be governed without private APIs or a fork | V1 fails on tool interception or session ownership | Keep the adapter boundary; evaluate a thinner runtime behind the same contract; do not proceed to phase 2 until resolved |
| Papership reference does not survive Tauri packaging or TS migration cleanly | V2 fails | Preserve visual language, rebuild affected screens with the same primitives; record departures in `docs/ui-blueprint.md` |
| Duplicate external effects under interruption | V3 fails | Block release; strengthen receipts and reconciliation before any connector work |
| Scope pull toward 43 domains before the loop works | Registry rows moving to `working` without demonstrated workflows | Registry status discipline; PL gate rejects unsupported status |
| Single-droplet footprint too small | V6 fails | Size up before pilot; document cost; do not pre-optimise before measurement |
| Commercial tiers designed before cost is measured | Pricing published without rate card evidence | Commercial gate stays closed until measured infrastructure, model/tool, and support costs exist |

**No-build / pivot criteria:** if after phase 2 the governed loop has not completed one real Engine Labs change with linked evidence and bounded authority, or requires more operator intervention than the founder's current workflow with no path to reduction, stop expansion and re-plan the product around the narrower runtime-governance layer.

## 16. Sources and research limitations

Sources cited inline in §2, §3, §5, §10. Limitations:

- No community thread analysis or interviews were performed; problem evidence is from published analyses and the intake author's own requirements.
- No analytics baseline exists; all metrics in V4 are first measurements.
- Pricing figures for competitors come from third-party comparison pages and may be stale.
- Hermes capabilities are taken from current documentation; the pinned-version inventory (tools, profiles, sessions, skills, memory, scheduling, delegation, browser, research, execution, documents, media) is a phase 0 engineering task and may narrow what is available.
- DigitalOcean, self-hosted Supabase, and Gmail scope documentation were not re-fetched in this pass; they are verified in the phase 0/1 compatibility spike.

## 17. Handoff into `phase_0_foundations_plan.md`

Phase 0 must: materialize the workstream and all six role charters/plans; produce `docs/product.md`, `docs/capabilities.md` (all 43 domains, status `planned`), `docs/architecture.md`, `docs/ui-blueprint.md` (reference commit, files, launch commands, captured states), `docs/roadmap.md`, `docs/verification.md`, `docs/policies/`; record decisions under `docs/decisions/`; run the V1/V2 compatibility spike scaffolding to the extent possible without credentials; register environment-variable names and the deferred human-action queue; and end with the exact Next Plan Generation Prompt for `phase_1_foundation_plan.md`.
