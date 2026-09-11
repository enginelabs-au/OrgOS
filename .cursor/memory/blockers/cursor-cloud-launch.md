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
4. 2026-09-11 after `6306a6c` on `origin/main`: Cloud failed with `No GitHub access token found with access to repository enginelabs-au/orgos` (cloud subagent `bc-51c02bcc-5917-412e-b24c-1ec765576ce3`).

## Next actions

- T2-1 planning is local: `docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/phase-2-t2-1-plan.md`.
- Owner: grant Cursor Cloud a GitHub token that can read `enginelabs-au/OrgOS`, then relaunch a Cloud agent on `main`.

## Resolution criteria

Cloud Task starts with repo access, **or** owner accepts local planning/implementation as the phase-2 venue (move this file to `blockers-fixed/` after that is recorded).
