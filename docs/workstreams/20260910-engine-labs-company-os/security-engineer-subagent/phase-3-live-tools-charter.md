# Security Engineer charter — Phase 3 live-tools re-review

Task: `20260910-engine-labs-company-os`  
Risk: Tier 3  
Mode: read-only  
Predecessor: live close-out evidence in `software-engineer-subagent/artifacts/t3-live-tools-evidence.md`

## Objective

Independent re-review after a live Hermes `accepted` run and a live GitHub PR. Verdict PASS / CONDITIONAL / BLOCKED for keeping `runtime.status = accepted` enabled.

## Must inspect

- `services/worker/policy_hooks/interception.py`, `startup.py`, `catalog.py`, `config/toolsets.yaml`
- `services/worker/adapter/interfaces.py`, `hermes_client.py`
- `services/worker/tests/test_runtime.py`
- `services/api/app/github_app.py` live open path; AUTH-12
- SE prior `phase-3-t3-3-handoff.md`
- Do not read secret files, `~/.config/orgos/*`, or systemd Environment values

## Binding questions

1. Did a catalogued **read** tool (`memory_read`) run through `HermesRuntimeAdapter.start_run` with pre-execution intercept before `POST /v1/runs`?
2. Is `api_server` still proven by capabilities 401 / `run_submission`, never by HEAD 405 alone?
3. Are write receipts still fail-closed and external tools still approval-then-receipt?
4. Are unknown tools still denied?
5. Does serve-UI still map to non-API / `blocked_runtime`?
6. AUTH-12 empty installation permissions still refuse live open?
7. Worker-only transport key (API never reads `HERMES_API_SERVER_KEY`)?
8. Live GitHub PR used the Papership App `open_pull` (not Cursor GitHub App)?

## Non-goals

No code edits. No starting a second gateway. No copying keys. No `execute_release`.

## Output

`docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/phase-3-live-tools-handoff.md`
