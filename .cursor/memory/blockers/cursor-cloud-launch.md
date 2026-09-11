# Blocker: Cursor Cloud agent launch from this Mac session

## Symptoms

`Task(environment=cloud)` failed twice: `environment: "cloud" requires exactly one known git remote for the parent workspace; found 0`.

`git remote -v` in `/Users/camdouglas/OrgOS` shows a single origin: `https://github.com/enginelabs-au/OrgOS.git`. `main` was pushed (`8a843bd..73083c6`).

`move_agent_to_root` (to refresh Cursor's git view) was denied by the fail-closed hook (state-changing MCP).

`bash .cursor/scripts/bootstrap.sh` is denied as a protected-path shell mutation. Preflight reports `bootstrap_required: false`.

## Evidence

- Push succeeded: `73083c66a2d34f7bc57abd9754a72d8f36bf392a` on `origin/main`.
- Preflight READY 2026-09-11T04:08:00Z.

## Attempts

1. `Task` cloud after push — 0 remotes.
2. Retry — same.
3. `move_agent_to_root` — hook denied.

## Next actions

- Continue phase 1 on this workstation (D-07 venue deviation).
- Owner may launch a Cloud agent from the Cursor Cloud UI on `enginelabs-au/OrgOS` `main` if a second venue is still wanted.

## Resolution criteria

Cloud Task starts with `found 1` remote, **or** owner accepts local implementation as the phase-1 venue (this file moves to `blockers-fixed/` after G1 records the deviation).
