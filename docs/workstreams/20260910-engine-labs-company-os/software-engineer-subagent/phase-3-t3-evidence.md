# Software Engineer evidence — Phase 3 T3-1…T3-6 (revision 2)

Date: 2026-09-11  
Worker tests: **30 passed**. API tests: **47 passed**.  
HEAD: `7d1af364c8448020e57540dccb1bef73e4f8257c`

## Closure pass (r2)

- AUTH-10: `action_binding_hash` bound on persist approval/receipt; mismatch refused (`test_auth10_*`).
- Probe: HEAD `/health` first (API + worker). GET 302 → `serve_ui` / `blocked_runtime` unit-tested.
- V14-3: voided approval and revoked `run.start` block later job steps (`test_voided_approval_blocks_job_step`, `test_revoked_grant_blocks_queued_job_step`).
- F-G7: product Settings no longer shows “Most Popular”.
- F-G8 / D-09: `scripts/dev-local.sh` defaults `ENGINE_USAGE_EMIT=0`. Live `/health` `usage_emit: false`.
- Hermes inventory: `artifacts/t3-hermes-inventory.md`.
- Traceability: `artifacts/t3-v13-1-traceability.md`.
- Licence: `artifacts/t3-licence-inventory.md`.
- Compose: `docker compose -f infra/compose/docker-compose.yml config --quiet` exit 0 (not brought up).

## Still not claimed

- Live Hermes tool `accepted`.
- Live GitHub `dry_run: false` / `execute_release`.
- Usage first-baseline (F-G1).
- Packaged signed Tauri; axe gallery; Settings click in Cursor browser (MCP click hook-blocked).
