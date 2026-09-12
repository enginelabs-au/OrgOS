# Decision D-04: Hermes runtime adapter contract expectations

## Status

`accepted` — owner-directed H-6 ratification 2026-09-11. Record: `docs/decisions/2026-09-11-owner-ratification-h6.md`. Phase 2 may reopen this record if the Hermes pin invalidates an expectation.

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md` (REQ-04, REQ-08). Architecture: `docs/architecture.md` §7 (expectation table), §5 (TB-3/TB-4/TB-5). Registry: `docs/capabilities.md` §5 (Hermes inventory placeholder).

## Context

The intake requires Engine Labs to "Connect Hermes through its documented API server and supported extension interfaces. Keep the upstream API private. Add typed adapter operations for capabilities it does not expose. Validate streaming, session ownership, cancellation, tool interception, usage reporting and isolation against the pinned version. Keep company records independent of Hermes' internal storage format." It also requires that side-effecting Hermes tools route through the Engine Labs action service, that API authentication is treated as transport access rather than per-tool authorisation, that tool receipts are persisted so recovery never blindly repeats completed actions, and that one Engine Labs workflow layer owns dispatch, schedules and approvals (Phase 04). Release-1 acceptance depends on it: R1-ACC-3 (reconnect to a persisted job), R1-ACC-5 (restart without duplicate effects), R1-ACC-7 (backend-mediated streamed sessions), R1-ACC-8 (run controls), R1-ACC-9 (contract tests).

The Hermes API server documentation fetched by the lead on 2026-09-10 (<https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server>) documents a runs API with durable idempotency, SSE events including subagent lifecycle, stop and approval endpoints, a capabilities endpoint, a sessions API with turn leases, a jobs API, toolset/skill discovery, bearer authentication, and health endpoints. It also documents limitations (no file upload; stored responses capped at 100; SSE buffers expire after 5 minutes when unconsumed; concurrent-run cap with HTTP 429) and a July 2026 breaking change to multi-profile key binding — evidence that the surface moves and must be pinned.

## Decision

1. **Single adapter, typed operations.** All Hermes access goes through `services/worker` adapter operations: `probe_capabilities`, `health`, `readiness`, `start_run`, `get_run`, `stream_events`, `stop_run`, `resolve_approval`, `create_session`, `list_messages`, `fork_session`, `delete_session`, `chat_stream`, `list_jobs` (read-only), `list_toolsets`, `list_skills`, `usage_from_run`. No other component imports a Hermes client or holds `HERMES_API_SERVER_KEY`.
2. **Capability gating.** The worker refuses to start unless `GET /v1/capabilities` advertises `run_submission`, `run_status`, `run_events_sse`, `run_stop`, `run_approval` and the `session_*` features release 1 uses; the payload is stored as registry evidence (P06.01).
3. **Idempotent run creation owned by Engine Labs.** The API persists the Job (DBOS workflow + Job row) and derives a unique, unguessable `Idempotency-Key` from it **before** calling `POST /v1/runs`. A replayed `202` with `Idempotency-Replayed: true` is success; a `409 idempotency_key_conflict` is an alerting defect. Keys are never reused across operations.
4. **One SSE subscriber, many projections.** Only the adapter subscribes to `GET /v1/runs/{id}/events`; it checkpoints normalised events (including `subagent.start`/`subagent.complete` with `child_session_id`, `delegation_id`, tokens/cost) to Postgres, and the API fans out to desktops. After a stream gap longer than the documented 5-minute buffer expiry, the adapter reconciles via `GET /v1/runs/{id}` and session messages rather than assuming loss.
5. **Cancel is explicit; close is not cancel.** `POST /v1/runs/{id}/stop` is invoked only by an authorised Cancel action; run state transitions `stopping → cancelled` are mirrored; desktop close/disconnect never reaches this operation (PRD-E.4).
6. **Approvals are decided in Engine Labs.** Approval requests surfaced by Hermes are bound to the Engine Labs action + target version (PRD-D.10); only the recorded decision is forwarded to `POST /v1/runs/{id}/approval`.
7. **Session ownership and record independence.** One Hermes session per Engine Labs Conversation; `X-Hermes-Session-Key` derived from tenant + principal; Engine Labs persists its own message copy and can operate with Hermes stopped (PRD-E.10, E.12). Hermes profiles are per tenant with distinct `API_SERVER_KEY`s.
8. **Engine Labs owns scheduling.** No Hermes job is created independently in release 1; the adapter may list `/api/jobs` to detect drift (PRD-E.5).
9. **Tool interception is mandatory but mechanism-open.** Side-effecting tools must route through the Engine Labs action service. The concrete mechanism (supported hook, scoped tool adapters, or restricted toolsets plus Engine Labs-provided tools) is selected in the phase-2 spike against the pinned version; if no supported path exists, side-effecting toolsets are disabled and the affected registry rows are `unavailable`, never silently allowed.
10. **Usage without double counting.** UsageEvents are keyed by `(run_id, child_session_id)` from run `usage` and `subagent.complete` payloads (PRD-G.3, G.11).
11. **Transport and network.** Hermes binds only to the worker network; bearer key always required; no CORS; egress restricted (architecture TB-3/TB-4). Concurrency is throttled by the DBOS queue below `max_concurrent_runs`; HTTP 429 triggers backoff.
12. **Contract tests are the acceptance mechanism.** Each expectation in `docs/architecture.md` §7 has a named phase-2 contract test executed against the pinned version (PRD-B.7, R1-ACC-9); the inventory in `docs/capabilities.md` §5 is regenerated on every pin change.

## Alternatives considered

1. **OpenAI-compatible `/v1/chat/completions` or `/v1/responses` as the primary integration.** Rejected for runs: stateless chat completions require client-managed history and offer no stop/approval/idempotency semantics; Responses chains execute delegation synchronously and cap stored responses at 100 (LRU). Retained only as a possible fallback for simple Ask-mode turns if the spike shows benefit.
2. **Let Hermes own scheduling via `/api/jobs`.** Rejected: violates "one Engine Labs workflow layer owns dispatch, schedules and approvals" and risks duplicate obligations (PRD-E.5).
3. **Desktop subscribes to Hermes SSE directly (CORS enabled).** Rejected: exposes the Hermes key/toolset to the client, contradicts PRD-B.5 (desktop talks only to the Engine Labs API) and the documentation's own security guidance.
4. **Rely on Hermes' internal SQLite session/response storage as the conversation record.** Rejected: company records must be independent of Hermes' internal storage format and survive Hermes being stopped (PRD-E.10).
5. **Client-generated idempotency keys without a persisted Job.** Rejected: a crash between key generation and persistence could orphan a Hermes run; persisting the Job first satisfies PRD-E.5 and gives a durable key.
6. **Skip capability gating and trust the pin.** Rejected: the documentation records surface changes within months (July 2026 breaking change); gating turns drift into a fail-closed start-up error instead of a runtime surprise.

## Consequences

- Positive: a single, testable boundary; fail-closed behaviour on version drift; recovery guarantees (idempotent creation, receipts, reconciliation) that map directly to R1-ACC-3/5; Security can review one component for Hermes exposure.
- Negative / costs: adapter development and contract-test maintenance on every pin change; an extra hop for events (adapter → Postgres → API → desktop) adds latency, mitigated by streaming through the API without waiting for durable writes of token deltas (only lifecycle/tool events are checkpointed); tool interception may require restricting Hermes toolsets in release 1 if no supported hook exists.
- Open item: interception mechanism (decision 9) — spike deliverable in phase 2 with Security re-review.
- Environment variables (names only; registry in phase 0 plan §16): `HERMES_API_BASE_URL`, `HERMES_API_SERVER_KEY` (Hermes-side `API_SERVER_KEY`), `HERMES_VERSION_PIN`, `MODEL_PROVIDER_API_KEY` (per provider).

## Evidence and citations

- Hermes API server documentation (fetched 2026-09-10): runs API (`POST /v1/runs`, `Idempotency-Key` semantics, `GET /v1/runs/{id}`, `GET /v1/runs/{id}/events` incl. `subagent.*`, `POST …/stop`, `POST …/approval`), `GET /v1/capabilities`, sessions API and turn leases, jobs API, `GET /v1/toolsets`, `GET /v1/skills`, `/health`, `/health/detailed`, authentication, CORS, concurrent-run cap, limitations, multi-profile routing — <https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server>.
- Intake: `docs/blueprints/company_agent_system_blueprint.md` Phase 04 (Hermes paragraphs), Phase 05 (action lifecycle, recovery), Phase 08 (GlobalAgentPanel, contract tests).
- Product: `docs/product.md` PRD-B.5–B.7, PRD-E.4, E.5, E.7, E.8, E.10, E.12, PRD-G.3, G.11, §9 R1-ACC-3/5/7/8/9.
- Strategy blueprint: `docs/blueprints/2026-09-10_engine_labs.md` §10–§12.
- Architecture: `docs/architecture.md` §7 (expectation table with contract tests), §5 (trust boundaries), §8 (DBOS usage).
- SE evidence: `docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/evidence.md` EV-S11, EV-S13.
