# Blocker (fixed): Cursor Cloud GitHub access to `enginelabs-au/Papership`

## Status

- Fixed 2026-09-11 (UTC). Owner restored Cloud GitHub access.

## Symptoms

1. Early: `environment: "cloud" requires exactly one known git remote; found 0`.
2. Later: `No GitHub access token found with access to repository enginelabs-au/orgos`.

## Resolution

- Cloud subagent `bc-110688dd-a26e-43f2-b93d-2981927d58b4` and reconfirm `bc-90eaf68c-00a5-4820-a0f5-bdbe5b7f8627` both returned `CLOUD_OK` at SHA `7d1af364c8448020e57540dccb1bef73e4f8257c` on `main`. Cursor GitHub App is installed on all `enginelabs-au` repos.
- Local `origin` remains `https://github.com/enginelabs-au/OrgOS.git`.

## Residual

- If Cloud fails again after an org SSO reset, re-grant the Cursor GitHub App on `enginelabs-au/Papership`.
