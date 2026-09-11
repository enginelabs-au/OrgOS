# Decision D-07: Tooling and compatibility pins (phase 1)

## Status

`accepted` — owner-directed H-6 ratification 2026-09-11. Record: `docs/decisions/2026-09-11-owner-ratification-h6.md`.

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md`. Phase plan: `docs/plans/phase_1_foundation_plan.md` T1-1.

## Context

T1-1 must fix D-01 tooling: npm workspaces vs path-deps, `uv` lockfiles, Postgres major, Supabase image pin, proxy, icon source (OQ-U3), font vendoring (OQ-U4). Cursor Cloud launch from this Mac session failed (parent workspace reported 0 git remotes after `origin` was added and `main` was pushed). Implementation continues on the workstation. Preflight 2026-09-11T04:08:00Z: READY; bootstrap not required.

Observed toolchain (2026-09-11):

| Tool | Version / path |
|---|---|
| node | v25.6.1 |
| npm | 11.9.0 |
| Python | 3.11.9 |
| rustc / cargo | 1.84.1 |
| Docker | 27.5.1 |
| Xcode CLT / Xcode | `/Applications/Xcode.app/Contents/Developer` |
| uv | present (`~/.local/bin/uv`) |
| just | missing — `justfile` plus `scripts/ci.sh` equivalent |

## Decision

1. **JS/TS layout:** npm workspaces at the repository root for `apps/desktop`, `packages/ui`, `packages/contracts`. Fallback (not used unless workspace hoist breaks Tauri): path dependencies. Recorded after scaffold: workspaces.
2. **Python:** `uv` lockfiles per service (`services/api`, `services/worker`).
3. **Desktop:** Tauri 2 + Vite 6 + React 18 + TypeScript. Packaged debug build is the target; `vite dev` is an allowed fallback if `tauri build --debug` fails on a given machine.
4. **Task runner:** `justfile` recipes (`dev`, `test`, `compose-up`, `ci`) with `scripts/ci.sh` so CI does not require `just` to be preinstalled.
5. **Postgres:** major **15** (Supabase self-host default range compatible with DBOS Python docs as of 2026-09-11). Application DB and DBOS system DB are separate databases on the same instance.
6. **Proxy:** **Caddy** on `edge` (simpler TLS/static config than Traefik for a single-host Compose stack).
7. **Supabase images:** tags recorded in `infra/digests.lock`; digests filled when `docker pull` succeeds. Pruned stack: Auth, Postgres, Storage, Kong/Caddy gateway. Studio/Realtime/Edge Runtime/imgproxy are not published.
8. **Icons (OQ-U3):** port the reference `icons.jsx` inline SVG set into `packages/ui` — no extra icon package.
9. **Fonts (OQ-U4):** vendor Inter and JetBrains Mono under `apps/desktop/public/fonts/` with licence files; no Google Fonts network request.
10. **DBOS:** Python `dbos` on the API. Persist-before-202 is enforced in application code even when DBOS is not connected (sqlite/file store in unit tests).
11. **Venue deviation:** Cloud-only implementation was the owner plan. Cloud `Task(environment=cloud)` could not start (`found 0` remotes). Local implementation is authorized by the same Build/Agent-mode go-ahead plus the requirement to finish T1-1…T1-21.

## Alternatives considered

1. Path-deps-only desktop (no workspaces) — rejected unless hoist breaks Tauri.
2. Traefik — rejected for R1 simplicity.
3. Skip Tauri until Cloud — rejected; Xcode and Rust are present here.

## Consequences

Phase-1 CI and `just ci` / `scripts/ci.sh` use these pins. D-08 records worker data access independently.

## Evidence

- `node .cursor/skills/launch-pipeline/scripts/preflight.mjs` exit 0, READY, 2026-09-11T04:08:00Z.
- Toolchain commands recorded in `.cursor/memory/memories/2026-09-11-continuation.md`.
