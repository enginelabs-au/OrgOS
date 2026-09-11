# Security Engineer charter — Phase 3 T3-3

Task: `20260910-engine-labs-company-os`  
Risk: Tier 3  
Mode: read-only  
Predecessor: `software-engineer-subagent/phase-3-t3-handoff.md` (CONDITIONAL)

## Objective

Independent re-review after the Hermes HTTP API listener is up on `:8642`. Verdict PASS / CONDITIONAL / BLOCKED for live tool execution.

## Must inspect

- `services/worker/policy_hooks/interception.py`, `startup.py`, `catalog.py`, `config/toolsets.yaml`
- `services/worker/adapter/interfaces.py`, `hermes_client.py`
- `services/api/app/main.py` AUTH-12, `hermes_health.py`
- SE evidence `phase-3-t3-evidence.md`
- Do not read secret files or systemd Environment values

## Binding questions

1. Are write receipts fail-closed and external tools approval-then-receipt?
2. Are unknown tools still denied?
3. Does serve-UI still map to non-API / `blocked_runtime`?
4. Is HEAD 405 an acceptable reachability signal, given GET `/health` hangs?
5. May Papership report `/runs` `queued` without a live `accepted` Hermes run?
6. AUTH-12 empty installation permissions?

## Non-goals

No code edits. No starting a second gateway. No copying keys.

## Output

`docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/phase-3-t3-3-handoff.md`
