# Phase 1 UI notes (T1-12, T1-13, T1-16 desktop bits)

Role: `software-engineer-subagent`. Workstream: `20260910-engine-labs-company-os`.  
Plan: `docs/plans/phase_1_foundation_plan.md`. Decision markers: D-06 proposed, D-07 proposed.  
Recorded: 2026-09-11T04:20:24Z.

## Commands and exit codes

| Command | Cwd | Exit | Notes |
|---|---|---|---|
| `npm install --ignore-scripts` | repo root | 0 | 78 packages; 0 vulnerabilities; no `tailwind` in lockfile |
| `npm test` | `packages/ui` | 0 | 12/12 `node:test` then `scripts/contrast.mjs` PASS |
| `npm run typecheck` | `packages/ui` | 0 | `tsc --noEmit` |
| `node scripts/contrast.mjs` | `packages/ui` | 0 | t1/t2/t3 on canvas/surface ≥ 4.5:1; t4 excluded |
| `npm run build` | `apps/desktop` | 0 | `tsc --noEmit && vite build` (Vite 6.4.3); `dist/` written |
| `npm test` | `apps/desktop` | 0 | 2/2 static-scan tests |
| `tauri build` | — | not run | Allowed skip if heavy; Vite build is the required gate |

## Hey Engine

- Path: `packages/ui/src/HeyEngineButton.tsx`
- Wired in chrome: `apps/desktop/src/App.tsx` (`onOpenAssistant` opens `AssistantPanel`)
- Panel: `apps/desktop/src/assistant/AssistantPanel.tsx` — honest `unavailable` (AUTH-28); no invented replies; unmounted when closed (F-S7)

## Tokens (D-06 proposed)

- `packages/ui/src/tokens.ts` marked `decision: D-06 proposed`
- `light.t3` = `#617083` (5.06:1 on `#ffffff`, 4.75:1 on canvas)
- `t4` decorative-only (excluded from contrast assertion)
- AA micro-adjustments (same decision): `light.t2` / `navText` `#63738a` (was `#64748b`, 4.47:1 on canvas); `dimmed.t3` `#8795aa` (was `#7d8ba0`, failed surface)

## Assumptions

- `packages/contracts/package.json` is a workspace stub so root `npm install` resolves D-07 workspaces. T1-3 owns schemas.
- Settings disclosure lists Growth §5.4.2 required field names only (no extension fields pending F-G1).
- Sign-in POSTs to `${ENGINE_API_BASE_URL}/auth/v1/token?grant_type=password` with email + strong factor. No Google, demo credentials, or sign-up.
- Vite-dev tokens stay in process memory; packaged builds use Rust `keychain_*` + `keyring` (AUTH-26). Never `localStorage`.
- Fonts: OFL text files only; no woff2; no Google Fonts. System / `local()` fallback (`apps/desktop/public/fonts/README.md`).
- T1-16 desktop bit: Home rail Health calls `GET /health` when the API base is set.

## Validation limitations

- No axe gallery run (no extra browser/axe dependency installed).
- No packaged `tauri build --debug` in this pass.
- API views show ordinary empty/error copy when `ENGINE_API_BASE_URL` is unset or the API is down.
