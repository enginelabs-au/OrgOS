# SP-7 interception artefact (T2-1)

Date: 2026-09-11  
Pin: Hermes Agent v0.21.1 (`hermes serve` on droplet-campbell:9119)  
`interception_verified`: **false** (AUTH-25). Do not enable toolsets until Security re-review PASS.

## Mechanism (D-16)

**Restricted toolsets + Engine Labs API action service (SP-4).**  
The documented API-server approval hook (SP-2) is not available on this deployment. SP-3 bind/forward is implemented and unit-tested against a fake Hermes; it is not live-proven.

## Digests (sha256)

| Path | sha256 |
|---|---|
| `services/worker/config/toolsets.yaml` | `3c59af42d1ed156bfb14ec72a8a964cf01f7bb5ac06487948d16b33b9fed4636` |
| `services/worker/policy_hooks/interception.py` | `0d20adfe39815e7223704b0019fc3246cdc7269271dd847b9ed21acf31b5061d` |
| `services/worker/policy_hooks/egress.py` | `75de97272cc5d254e6f95aff52eb9989f8a737142a1f23b9073b27f9ef4896d0` |
| `services/worker/adapter/approvals.py` | `81cad9a48f877545cc4d82ed4b856a8d648077181a7a7b329bbac168944be9d0` |

## Transcripts

- Live: `GET http://127.0.0.1:9119/health` → 302 `/login` (2026-09-11T11:31:45Z). Same for `/v1/capabilities` and `/v1/toolsets`.
- VPS listen: `hermes` on `:9119` and messaging `:9900`. No API-server listener.
- Tests: `services/worker/tests/test_interception.py`, `test_egress.py`, `test_approvals.py`, `test_startup.py`.

## SP score

| ID | Verdict | Note |
|---|---|---|
| SP-1 | PASS (limited) | Inventory of deployed serve UI + documented API-server surface |
| SP-2 | NOT PROVEN | No API server; cannot pause-before-tool on this pin |
| SP-3 | UNIT PASS | Persist-before-forward; never-forward leaves Hermes pending |
| SP-4 | PASS | Default yaml all disabled; policy error on terminal |
| SP-5 | PASS | Injection prompt cannot override policy |
| SP-6 | UNIT PASS | Non-allowlisted host denied. Live Compose/Docker not run |
| SP-7 | THIS FILE | Hash-backed; `interception_verified` stays false |
