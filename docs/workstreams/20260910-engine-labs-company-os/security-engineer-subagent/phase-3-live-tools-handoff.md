---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: security-engineer-subagent
status: complete
revision: 1
verdict: CONDITIONAL
started_at: 2026-09-11T14:07:00Z
completed_at: 2026-09-11T14:25:00Z
charter: docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/phase-3-live-tools-charter.md
plan: docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/plan.md
predecessor_handoffs:
  - docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/artifacts/t3-live-tools-evidence.md
  - docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/phase-3-t3-3-handoff.md
downstream_role: project-lead-subagent
risk_tier: 3
---

# Security Engineer handoff — Phase 3 live-tools re-review

Independent read-only re-review after claimed live Hermes `accepted` and live GitHub PR. `phase-3-t3-evidence.md` does not exist; evidence is recorded here. No secret values.

## Verdict

**CONDITIONAL.**

F-T33-SEC-01’s High-latent bar (no live pre-execution intercept before `POST /v1/runs`) is **remediated for a declared catalogued read tool**. This revision **allows** `runtime.status = accepted` only for that narrow path. It is **not** a Security PASS for write, external, or destructive tools, for `start_run` without `tool=`, or for treating Hermes as scoped to the declared tool.

### Allow `accepted` for catalogued read tools?

**Yes — narrowly.** `HermesRuntimeAdapter.start_run` may return `status=accepted` when all of the following hold:

1. `tool=` is present and `lookup` classifies it `read` (the proven case is `memory_read`).
2. `intercept_tool_call` succeeds **before** `hermes_client.start_run` POSTs `/v1/runs`.
3. Worker `api_server` is true from capabilities `unauthorized` (HTTP 401) or advertised `run_submission` — never from HEAD 405 alone.
4. Hermes returns HTTP 200/201/202.

Lead follow-up (same turn): live `start_run` now raises `PolicyError` when `api_server` is true and `tool=` is missing (F-T33-SEC-09 partial). Write/external still need receipt/approval.

### Write / external still need receipt / approval?

**Yes.** Unchanged and fail-closed:

- `write` / `external` / `destructive` require `persist_receipt`; missing or empty persist → `PolicyError`.
- `external` / `destructive` require `persist_approval` **then** receipt (order asserted).
- Unknown tools remain denied. Prompt text cannot override.

## Binding answers

| # | Question | Answer | Evidence state |
|---|---|---|---|
| 1 | Catalogued read `memory_read` through `start_run` intercept before `POST /v1/runs`? | **Yes (adapter path).** `interfaces.py` `start_run` calls `self.intercept(...)` when `tool` is in kwargs, then `probe_hermes`, then `hermes_start` → `POST /v1/runs`. Predecessor live record: intercept `{tool: memory_read, risk: read}` then HTTP 202, idempotency `orgos-worker-live-read-4`, `run_ee41560dd3ee46eb9bef3fcd6615e6ba`, status `accepted`. **No (Hermes tool body).** Purpose/input was “Reply with the single word pong. Do not use any tools.” — `memory_read` was the Papership declared tool, not a demonstrated Hermes tool invocation. | VERIFIED (code + unit `test_head_405_plus_capabilities_401_is_api_server`); PARTIAL (live HTTP — predecessor-attributed; this role did not replay POST and must not read the transport key) |
| 2 | `api_server` proven by capabilities 401 / `run_submission`, never HEAD 405 alone? | **Yes.** `probe_hermes`: HEAD 405/200/204/401 is reachability; `api_server` only if `_get_json("/v1/capabilities")` is `unauthorized: true` or `"run_submission" in str(caps)`. Unit: HEAD 405 + `_get_json` None → `api_server=False` → `blocked_runtime`; HEAD 405 + `{unauthorized: true}` → `api_server=True`. API `/health` may still call HEAD 405 `reachable` (queue only). | VERIFIED |
| 3 | Write receipts fail-closed? External = approval then receipt? | **Yes (unit + source).** `intercept_tool_call`: write/external/destructive without `persist_receipt` raise; external/destructive without `persist_approval` raise; empty persist raises “API must own…”. `test_external_requires_approval` order `["approval","receipt"]`. AUTH-10 mismatch still refused. | VERIFIED |
| 4 | Unknown tools denied? | **Yes.** `lookup` miss → `allow_tool` false → `PolicyError`. Prompt ignored. `test_unknown_tools_default_deny`, `test_injection_cannot_override_policy`. | VERIFIED |
| 5 | Serve-UI → `blocked_runtime`? | **Yes.** Redirects 301/302/303/307/308 → worker `mode=serve_ui`, `api_server=False` → `start_run` `blocked_runtime`. API `hermes_health` → `serve_ui`. `test_redirect_probe_is_serve_ui_not_api_server`, `test_probe_get_302_is_serve_ui`. | VERIFIED |
| 6 | AUTH-12 empty installation perms refuse live open? | **Yes on the product HTTP route.** `POST /github/pulls` with `dry_run=false`: empty `installation_permissions()` → 403 `installation permissions are empty; refuse live open`; then `may_open_pull`. `test_live_open_refuses_empty_installation_perms`. The live PR did **not** traverse this route (see F-T33-SEC-10). | VERIFIED (control); PARTIAL (live exercise) |
| 7 | API never reads `HERMES_API_SERVER_KEY`? | **Yes.** Name is in `PHASE2_ENV_NAMES` and **not** in `API_ENV_ALLOWLIST`. `load_settings` refuses if it leaks into the allowlist and never `os.environ.get`s it. `test_phase2_env_names_are_not_read`. No `services/api` or `apps/` import of worker `hermes_client` / `_transport_key`. Worker allowlist may hold it (transport only). | VERIFIED |
| 8 | Live PR used Papership `open_pull` (App orgos-dev), not Cursor GitHub App? | **Yes.** Independent GitHub read of https://github.com/enginelabs-au/OrgOS/pull/1: user `orgos-dev[bot]`; commit `orgos: Papership loop: Phase 3 live close-out` by `orgos-dev[bot]`; single file `.orgos/loop/orgos-loop-r1-close.md` matching `plan_pull` / `_put_receipt`. Not a Cursor App author. SE used `open_pull(..., dry_run=False)` because the running API lacked `SUPABASE_JWT_SECRET` for founder `reauth_at`. | VERIFIED (PR identity); PARTIAL (library vs HTTP route) |

## Findings

| ID | Severity | Status | Notes |
|---|---|---|---|
| F-T33-SEC-01 | High latent → **closed for declared-read intercept** | **Remediated (bounded)** | Live/unit path: `start_run(tool=memory_read)` intercepts `{tool, risk: read}` before POST. Reopens High/BLOCKED if `accepted` is claimed for write/external, for `start_run` without `tool=`, or if yaml/catalog/artefact hashes change. |
| F-T33-SEC-02 | Medium | Mitigated (holds) | Worker does not set `api_server` from HEAD 405. API test name is now `test_probe_head_405_means_reachable`. |
| F-T33-SEC-03 | Medium | **Open** | `subscribe` intercepts **after** SSE `stream_events` yields. Worker `worker.py` still only `validate_default()` then sleeps — it never subscribes. Mid-run Hermes tools are not pre-blocked. |
| F-T33-SEC-04 | Medium | Remediated | AUTH-10 persist hash; mismatch fail-closed. Residual Low: persist need not echo `auth10`. |
| F-T33-SEC-05 | Low | Remediated | 302 → `serve_ui` / `blocked_runtime` unit-tested. |
| F-T33-SEC-06 | Low | Remediated | Inventory exists; GET `/health` still hangs; HEAD 405 is reachability only. |
| F-T33-SEC-07 | Medium (now material) | **Open** | Full D-17 catalog remains enabled. A read-labeled `accepted` run does not constrain Hermes’s own toolset. `API_SERVER_KEY` is still full-access transport. Owner: keep write/external on receipt/approval; do not treat purpose text as a control. |
| F-T33-SEC-08 | Owner | Open | Mailbox `Environment=` (do not paste values); public HTTPS residual; git pin not image digest. |
| F-T33-SEC-09 | Medium | **Partial (lead, same turn)** | Live POST now requires catalogued `tool=` (`PolicyError` if missing). Hermes is still not scoped to that tool; subscribe still idle. Re-review if job consumer or assistant turns are treated as `accepted`. |
| F-T33-SEC-10 | Low | **Open (new)** | Live PR used `open_pull` library, not `POST /github/pulls`, so AUTH-12 HTTP was not the live gate. Control remains on the route. Do not treat library `open_pull(dry_run=False)` as AUTH-12-enforced. |

No open **High** or **Critical** after the bounded reclassification of F-T33-SEC-01. Open High would return **BLOCKED**.

## Residual risks

- Hermes may execute tools other than the declared read tool during an `accepted` run (F-T33-SEC-03, F-T33-SEC-07, F-T33-SEC-09).
- Live `POST /v1/runs` HTTP facts were not independently replayed (charter forbids reading `HERMES_API_SERVER_KEY` / starting a second gateway).
- Worker still does not consume jobs; `accepted` is an adapter status, not a job-loop guarantee.
- Live GitHub mutation bypassed the AUTH-12 HTTP gate (F-T33-SEC-10).
- GET `/health` hang; mailbox `Environment=`; no `execute_release`.

## Does not authorize

- `accepted` for write / external / destructive tools
- treating Papership `/runs` `queued` or HEAD 405 as a tool PASS
- a second Hermes gateway
- copying or logging `HERMES_API_SERVER_KEY`
- `execute_release` / production deploy
- waiving F-T33-SEC-03 / 07

## Downstream

`project-lead-subagent`. Conditions that remain binding:

1. Keep `accepted` limited to catalogued **read** `tool=` after intercept.
2. Write/external still need Papership receipt / approval-then-receipt.
3. Hash change of yaml / catalog / artefact invalidates this verdict.
4. Wiring a job consumer or subscribe path requires Security re-review.
