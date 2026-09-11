# 2026-09-11 continuation

## Venue and push

- Owner authorized first commit/push to `https://github.com/enginelabs-au/OrgOS` and Cloud-only T1 implementation.
- Nested `8a843bd` UI tree under `docs/ui-blueprint/` (source files; no node_modules). Hey Engine recorded (PRD-E.13 / P03.01).
- `git checkout -B main origin/main` kept `8a843bd` as ancestor. First product commit: `73083c66a2d34f7bc57abd9754a72d8f36bf392a` (GitHub noreply author after GH007 rejected a private-email commit). Fast-forward push `8a843bd..73083c6` on `main`.

## Cloud launch failed

- `Task(environment=cloud)` twice: parent workspace reported 0 remotes despite `origin` present.
- `move_agent_to_root` hook-denied. Bootstrap script path hook-denied; preflight READY, `bootstrap_required: false`.
- Blocker: `.cursor/memory/blockers/cursor-cloud-launch.md`.
- Deviation (D-07): continue T1 on this Mac. Toolchain: node 25.6.1, rustc 1.84.1, Docker 27.5.1, Xcode present, uv present, just missing.

## Implementation started

- D-07 `docs/decisions/2026-09-11-tooling-and-pins.md`, D-08 `docs/decisions/2026-09-11-worker-data-access.md`.
- Root scaffold: LICENSE, NOTICE, package.json workspaces, justfile, scripts/ci.sh, scripts/dev.sh, product-ci.yml, compose env example, digests.lock skeleton.
- Local SE delegates: backend T1-3…T1-11 (`a80e21d3`), UI T1-12/T1-13 (`b73a040b`).

## G1 close

- `bash scripts/ci.sh` exit 0 (desktop 2, ui 12, contracts 13, api 21, worker 6, compose assertions).
- Hey Engine: `packages/ui/src/HeyEngineButton.tsx` (opens assistant `unavailable` only).
- Six phase-1 handoffs CONDITIONAL. Registry 12 `configured`, 0 `working`.
- `docs/plans/phase_2_development_loop_plan.md` generated. Phase 08 not implemented.

## Branch

- No `master` locally or on GitHub. Default is `main`. Pushed phase-1 tree as `e405181`.

## H-6, public site, phase 2 activate

- Owner asked to finish gates, keep Vercel `orgos`, combine entry points, push with Cursor anonymous email, plan phase 2 on Cloud.
- D-09 accepts D-01…D-08 and the five policies. F-G1 emit still off. H-4/H-5/GitHub App/model keys still owner-only.
- `apps/web` is the single public website. Root `vercel.json` builds it. Docker unavailable; Vercel CLI has no token so extras were not deleted. Runbook: `/memory/runbooks/vercel-orgos-single-site.md`.
- Phase 2 plan set `active`. T2-1 charter written. Cloud launch still may fail (0 remotes).

## After 6306a6c

- Push `6306a6c` as Cursor Agent `cursoragent@cursor.com`. Vercel `orgos` production READY (`dpl_5BkY3jyEqNg3V11bfXcBzBZ2AkpD`). Dashboard URLs are SSO-gated; HTML 200 via Vercel MCP.
- Cloud Task failed: no GitHub token for `enginelabs-au/orgos`. T2-1 plan written locally: `phase-2-t2-1-plan.md`.

## Owner correction 2026-09-11 evening

- OrgOS is the product. Engine Labs marketing (`enginelabs.com.au` / `enginelabs-au-site`) must not be touched. D-10 recorded.
- Withdrew the Engine Labs landing. `apps/web` is now the `docs/ui-blueprint` `/cc-org-dash` UI (wordmark OrgOS, Hey Engine).
- Vercel has no projects named web/desktop/api/worker. Nothing deleted. Other account projects left alone.
- Live Compose substitute: `scripts/dev-local.sh` + `scripts/port-scan.sh`. API `/health` PASS on :8000.
- Tauri package: `bundle.active` true; Homebrew rustc 1.84 cannot compile current crates (edition2024). rust-toolchain.toml pins stable.
- Cloud still: Cursor GitHub App cannot see `enginelabs-au/OrgOS`. Owner must grant org access + SSO.
- F-G1 left off. Owner checklist: `docs/handover/phase-2-owner-actions.md`.

