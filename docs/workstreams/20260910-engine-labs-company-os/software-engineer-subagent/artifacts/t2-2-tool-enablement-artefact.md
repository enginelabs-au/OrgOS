# SP-7 interception artefact (T2-2 owner enablement, T3-1 bind)

Date: 2026-09-11  
Pin: Hermes Agent v0.21.1  
Owner request: enable the widest documented tool catalog with Papership policy in front.

`interception_verified`: **true** only when this file's sha256 matches `toolsets.yaml` and `catalog_sha256` matches `policy_hooks/catalog.py`.

## Mechanism (D-17 / T3-1)

Catalog allowlist + risk class + Papership receipts/approvals + egress deny for private/metadata hosts.

| Risk | Tools | Gate |
|---|---|---|
| read | search, read_file, snapshots, memory_read, skills list | catalog only |
| write | terminal, write_file, browser, execute_code, media gen | persist receipt required |
| external | github, email_send, ha_call_service, computer_use | persist approval then receipt |
| unknown | anything not in `policy_hooks/catalog.py` | denied |

Every Hermes tool-shaped SSE/event is intercepted (`tool_call_from_event`). Missing receipt/approval hooks fail closed. Hermes `API_SERVER_KEY` remains transport-only (D-04). GitHub mutations still prefer the Papership API (`POST /github/pulls`). Desktop never holds provider keys.

## Live limitation

`hermes serve` on :9119 is the login UI. Live `/v1/runs` requires the gateway API server on :8642. Adapter `start_run` reports `blocked_runtime` until that listener is an HTTP API (not a 302 login). That is not a silent allow.
