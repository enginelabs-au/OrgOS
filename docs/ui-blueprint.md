---
document: ui-blueprint
title: Engine Labs — UI Blueprint (Papership `/cc-org-dash` derived)
status: specification_complete; captures_complete (SE sections filled 2026-09-10; 122 PNGs for all 52 states captured by the orchestrating lead 2026-09-10T17:15Z — see §0.4)
revision: 3
created: 2026-09-10
updated: 2026-09-10
owner_role: ui-ux-developer-subagent (read-only; materialized by orchestrating lead); capture sections owned by software-engineer-subagent
task_id: 20260910-engine-labs-company-os
intake: docs/Company_Agent_System_Blueprint.md (Phase 03, Phase 16)
product: docs/product.md (PRD-A.10–A.17, §5.1, PRD-B.5–B.6, PRD-D.7/D.13, PRD-E.4, PRD-G.6, §9, NFR-2, NFR-3)
blueprint: docs/blueprints/2026-09-10_engine_labs.md §10–§12
phase_plan: docs/plans/phase_0_foundations_plan.md (T0-7 spec, T0-8 capture)
manifest: docs/workstreams/20260910-engine-labs-company-os/manifest.md
role_handoff: docs/workstreams/20260910-engine-labs-company-os/ui-ux-developer-subagent/handoff.md
predecessor: docs/workstreams/20260910-engine-labs-company-os/product-manager-subagent/handoff.md
reference: enginelabs-au/Papership @ 8a843bd6429faf1ace5a9eb6dcfb7440703d34c4, route `/cc-org-dash` (`src/App.jsx` L10 redirects `/` here)
---

# Engine Labs — UI Blueprint

All reference citations are `path Lstart–Lend` in the pinned commit; line numbers are approximate (±5). "Ref" = reference behaviour observed in source; "EL" = Engine Labs requirement. Nothing here is runtime proof; §G defines the screenshots that make it so.

## §0 Reference commit, launch, capture index

Completed by `software-engineer-subagent` (T0-8) on 2026-09-10 from the local clone at `.reference/orgos/` (git-ignored). Evidence records EV-S03–EV-S09 in `docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/evidence.md`.

### §0.1 Commit and clone

- Clone: `git clone https://github.com/enginelabs-au/OrgOS.git .reference/orgos` (exit 0, 1 s) then `git -C .reference/orgos checkout 8a843bd6429faf1ace5a9eb6dcfb7440703d34c4` (exit 0). `git -C .reference/orgos rev-parse HEAD` → `8a843bd6429faf1ace5a9eb6dcfb7440703d34c4` (matches the pin).
- In-repo snapshot (2026-09-11): the same tree (no `node_modules`, no `.git`) lives under `docs/ui-blueprint/` (`src/`, `public/`, lockfile, Vite/Tailwind configs). Pin record: `docs/ui-blueprint/SOURCE.md`. Phase-1 desktop port reads this snapshot; do not run its `npm` install or `dev` server. `.reference/orgos/` remains git-ignored.
- `git log -1 --format='%H %ad %an %s' --date=iso-strict` → `8a843bd6429faf1ace5a9eb6dcfb7440703d34c4 2026-09-10T23:07:59+10:00 Cursor Agent Initial Papership import.` (single-commit repository; detached HEAD).
- No `.nvmrc` in the reference; lockfile `package-lock.json` present; `vercel.json` present (web deployment artefact, not needed for desktop).

### §0.2 File inventory (bytes; sha256 first 16 hex; `shasum -a 256`)

| File | Bytes | sha256[0:16] |
|---|---|---|
| `src/pages/cc-org-dash.jsx` | 24 088 | `c1a78cfa90435116` |
| `src/App.jsx` | 768 | `a56e25a3a317f5c2` |
| `src/components/cc-org-dash/AccountScreen.jsx` | 20 451 | `0583c7dd45ff02bc` |
| `src/components/cc-org-dash/AuthPortal.jsx` | 22 733 | `83eabcd07e2eefa0` |
| `src/components/cc-org-dash/DataScreen.jsx` | 18 244 | `2b5cc1e51d539176` |
| `src/components/cc-org-dash/FilesScreen.jsx` | 23 805 | `b661675d1c9e62f8` |
| `src/components/cc-org-dash/GlobalAgentPanel.jsx` | 22 831 | `2cab8c5d173fa014` |
| `src/components/cc-org-dash/GlobalCommandDetail.jsx` | 6 770 | `95e1a416716debfb` |
| `src/components/cc-org-dash/GlobalCommandRail.jsx` | 9 553 | `cdddd60543d82279` |
| `src/components/cc-org-dash/HomeScreen.jsx` | 24 488 | `627569924be8f8e7` |
| `src/components/cc-org-dash/InboxScreen.jsx` | 51 515 | `6ba713b46b336567` |
| `src/components/cc-org-dash/IntegrationsScreen.jsx` | 6 867 | `9c70240ad5a46b53` |
| `src/components/cc-org-dash/NotifDrawer.jsx` | 1 982 | `59d42b0b21296943` |
| `src/components/cc-org-dash/PeopleScreen.jsx` | 6 873 | `5a72b685d54cef22` |
| `src/components/cc-org-dash/PlatformStatusBar.jsx` | 15 736 | `228eb4d7ac54b6af` |
| `src/components/cc-org-dash/SettingsScreen.jsx` | 36 806 | `23765b85cef2ceff` |
| `src/components/cc-org-dash/WorkScreen.jsx` | 34 382 | `4915369e157ed6d2` |
| `src/components/cc-org-dash/WorkflowVis.jsx` | 18 162 | `ad8b08b818ede3cd` |
| `src/components/cc-org-dash/data.jsx` | 21 898 | `60dd16d767ea451e` |
| `src/components/cc-org-dash/icons.jsx` | 14 713 | `47e0db1763d72f3e` |
| `src/components/cc-org-dash/primitives.jsx` | 27 026 | `2194652ce963adf7` |
| `src/components/cc-org-dash/useIsMobile.jsx` | 541 | `85c3c1b7aab2cfa4` |

20 component files (sizes match the UI/UX directory listing in §A.2/§A.3 exactly) plus the shell page and router.

### §0.3 Launch commands, toolchain, and build results (2026-09-10, macOS Darwin 25.6.0 arm64)

| Command (in `.reference/orgos/`) | Exit | Duration | Result |
|---|---|---|---|
| `npm ci` | 0 | 6 s | 605 packages added; lifecycle scripts **not** suppressed (`--ignore-scripts` fallback not needed); `npm audit` summary reported 24 advisories (2 low, 10 moderate, 11 high, 1 critical) — for Security review, not remediated here |
| `npm run build` (`vite build`) | 0 | 2 s | `dist/index.html`, `dist/assets/index-DIi3HLzA.js` 527 303 B, `dist/assets/index-BEAdeZQn.css` 62 040 B (588 K total) |
| `npm run lint` (`eslint . --quiet`) | 1 | 2 s | 2 errors, both `unused-imports/no-unused-imports`: `FilesScreen.jsx:2:15` (`Avi`), `PeopleScreen.jsx:4:31` (`Plus`); auto-fixable |
| `npm run typecheck` (`tsc -p ./jsconfig.json`) | 2 | 2 s | 328 errors over JSX (`checkJs`); 199 in `cc-org-dash/*` (Account 34, Settings 32, Work 29, Home 21, People 17, Files 16, Inbox 15, Integrations 10, Data 10, WorkflowVis 6, GlobalCommandDetail 4, NotifDrawer 2, shell 2, primitives 1), 129 in legacy `Dashboard*.jsx`. Expected for untyped JSX; confirms the §F JSX→TSX port must add types rather than rely on the reference typecheck |
| `npm run dev -- --port 5173 --strictPort --host 127.0.0.1` | running | — | `curl -sI http://127.0.0.1:5173/cc-org-dash` → `HTTP/1.1 200 OK`; Vite module transforms verified: `/src/pages/cc-org-dash.jsx` 200 (113 629 B), `primitives.jsx` 200, `GlobalAgentPanel.jsx` 200, `data.jsx` 200 |

Toolchain: node v25.6.1, npm 11.9.0, vite 6.4.1, typescript 5.9.3, eslint 9.39.2, Python 3.11.9, rustc/cargo 1.84.1 (Homebrew), Docker 27.5.1, git 2.51.0. Launch command for later captures: `cd .reference/orgos && npm run dev -- --port 5173 --strictPort` then open `http://localhost:5173/cc-org-dash` (only route; `src/App.jsx` L10–13 redirect `/`, `/EcoOS`, `/ecoos` here; legacy `/Dashboard`, `/Dashboard_new` remain routable).

### §0.4 Capture index (files under `docs/ui-blueprint/`)

**Status (lead, 2026-09-10T17:15Z): 52 of 52 states captured — 122 PNGs, ~20 MB.** Method: the orchestrating lead drove the host Google Chrome 152.0.7977.83 binary in `--headless=new` mode with `--remote-debugging-port=9333` over CDP (WebSocket) from `docs/ui-blueprint/capture.mjs` (Node 25, no installs; `Emulation.setDeviceMetricsOverride` for viewports/scale, `Runtime.evaluate` for localStorage seeding and clicks, `Page.captureScreenshot`). Each state reloads the app fresh and captures within ~0.5–3.5 s of load, so the random status-bar ticker shows only its seeded feed (`Math.random` was not stubbed). The Cursor IDE browser could not be used: it reaches public `http`/`https` hosts but returns `chrome-error://chromewebdata/` for `127.0.0.1`, `localhost` and the LAN address (4 attempts; public control URLs loaded), so loopback is blocked for that tool in this environment. Reproduce: start `npm run dev -- --port 5173 --strictPort --host 127.0.0.1` in `.reference/orgos/`, start Chrome headless with the flags above, then `node docs/ui-blueprint/capture.mjs [only=nn,nn]`.

Coverage: 52/52 states; V1 for all, V2–V4 where §G requires; light + dark for every state; dimmed for 03; @2x for 03 (V1, three themes), @1x for all others. Filenames follow `<nn>-<surface>-<state>-<theme>-<W>x<H>@<scale>x.png`. Trigger notes where the §G trigger was adapted: 07 clicks the first pointer-cursor row containing a `%` (first Active Project → "Q2 Growth Initiative" slide-over); 11 adds a tab via the panel `+`, sets the textarea and dispatches `Enter` (shows the `[Demo] Using gpt-4o @ 0.70 …` reply); 13 clicks the first button after the FYI digest row (initiative "Revenue engine Q2"); 14 clicks the first button after the `BLOCKERS` label ("Legal review — enterprise DPAs"); 20 is a 60 px bottom clip; 23 ticks the 2nd and 3rd issue checkboxes (bulk bar visible); 25 clicks the first `div[role=button]` issue row (CCO-245 slide-over); 29 dispatches a click on the first SVG node; 31 clicks the "Inbox" tab whose text includes the unread badge ("Inbox3"); 36 clicks the first card of the `auto-fill` grid; 44/47 use the actual label "Plan & Billing"; 51 sends two real `Input.dispatchKeyEvent` Tab presses; 52 sets `prefers-reduced-motion: reduce` via `Emulation.setEmulatedMedia` and captures ~0.2 s after opening the panel.

Runtime observations recorded for §G "Also record": computed `font-family` on `body` = `ui-sans-serif, system-ui, …` (Tailwind preflight), on shell text = `Inter, -apple-system, …` (`F.sans`); `document.fonts` lists only Roboto faces (Google Fonts, `unloaded`) — Inter/JetBrains Mono are not declared by the app, so their rendering depends on local installation (confirms OQ-U4). Keyboard focus order after load with the agent panel **closed** goes first to the off-screen panel controls ("Model & parameters", "Variables & context", "Agent", "Sources", "Attach", textarea) — the closed panel is translated off-screen but remains in the tab order (a11y defect to fix in phase 1 alongside D-10; the primary tabs are not reached within the first six Tab presses, so 51 shows no visible ring on a tab). Computed z-index stack on Home: 1 (×23), 2 (×2), 201 (×2 — SlideOver), 499, 500, 520 (top bar), 10050 (status-bar portal). The `cursor-ide-browser` limitation in the SE session is preserved below for the record.

Original SE-session record: 0 of 52 planned PNGs were written in the SE session. The `cursor-ide-browser` tool namespace was discovered (`browser_navigate`, `browser_take_screenshot`, `browser_cdp` schemas inspected) but every navigation attempt from the sub-agent context returned `No browser tab available. Please navigate to a page first.`: (1) `browser_navigate {newTab:true}`; (2) `browser_tabs {action:"new"}` → returned `viewId c07e4f`, then `browser_navigate {viewId}` → `Browser view not found`; (3) `browser_navigate` without `viewId`; (4) `browser_tabs {action:"list"}` → empty; (5) retry of (1) after confirming the dev server served `200`. Per charter §5 and the T0-8 constraint, Playwright/Chromium was **not** installed. The Vite dev server was left **running** for the lead to capture: PID `86187`, `http://127.0.0.1:5173/cc-org-dash` (managed background job; stop with `kill 86187`).

Seeding script for the lead's capture session (run via `browser_cdp Runtime.evaluate` before reload; derived from `cc-org-dash.jsx` L37–40):

```js
localStorage.setItem("cc-org-dash-auth", JSON.stringify({email:"founder@example.test",name:"Founder",at:Date.now()}));
localStorage.setItem("cc-org-dash-theme", "light"); // or "dark" | "dimmed"
localStorage.setItem("cc-global-command-open", "1"); // "0" for rail closed
// Stabilise the status-bar ticker (PlatformStatusBar.jsx L206–214 pushes random events every 4.5–10 s):
// capture within 4 s of load, or before load run: Math.random = () => 0.5;
```

Capture index (filename per §G `<nn>-<surface>-<state>-<theme>-<W>x<H>@<scale>x.png`; every row exists in light and dark unless noted):

| nn | Surface / state | Viewports × themes × scale | Files |
|---|---|---|---|
| 01 | auth-login | V1, V4 × light/dark | 4 |
| 02 | auth-signup | V1 | 2 |
| 03 | shell-home-rail-open | V1 (light/dark/dimmed @1x+@2x), V2, V3, V4 | 12 |
| 04 | shell-home-rail-closed | V1, V3 | 4 |
| 05 | home-overview-7d | V1 | 2 |
| 06 | home-overview-90d | V1 | 2 |
| 07 | home-project-slideover | V1 | 2 |
| 08 | agent-panel-open | V1, V4 | 4 |
| 09 | agent-panel-params-open | V1 | 2 |
| 10 | agent-panel-variables-open | V1 | 2 |
| 11 | agent-panel-two-tabs-demo-reply | V1 | 2 |
| 12 | rail-detail-critical | V1 | 2 |
| 13 | rail-detail-initiative | V1 | 2 |
| 14 | rail-detail-blocker | V1 | 2 |
| 15 | notif-drawer | V1 | 2 |
| 16 | cmd-palette | V1 | 2 |
| 17 | cmd-palette-no-results | V1 | 2 |
| 18 | create-menu | V1 | 2 |
| 19 | profile-menu | V1 | 2 |
| 20 | status-bar-collapsed (60 px bottom clip) | V1 | 2 |
| 21 | status-bar-expanded | V1 | 2 |
| 22 | work-projects | V1, V3 | 4 |
| 23 | work-issues-all-selected2 | V1 | 2 |
| 24 | work-issues-filter-review | V1 | 2 |
| 25 | work-issue-slideover | V1 | 2 |
| 26 | work-new-issue-modal | V1 | 2 |
| 27 | work-board | V1 | 2 |
| 28 | work-roadmap | V1 | 2 |
| 29 | work-workflows-node-selected | V1 | 2 |
| 30 | work-wiki-empty | V1 | 2 |
| 31 | inbox-default | V1 | 2 |
| 32 | people-table | V1 | 2 |
| 33 | data-metrics-traces | V1 | 2 |
| 34 | data-trace-slideover | V1 | 2 |
| 35 | files-list | V1 | 2 |
| 36 | files-grid-detail | V1 | 2 |
| 37 | integrations-cards | V1 | 2 |
| 38 | integrations-slideover | V1 | 2 |
| 39–46 | settings-general / appearance / ai / notifications / security / billing / team / docs | V1 | 16 |
| 47 | settings-upgrade-modal | V1 | 2 |
| 48 | account-profile | V1 | 2 |
| 49 | account-login-security | V1 | 2 |
| 50 | mobile-rail-button | V4 | 2 |
| 51 | focus-visible-tab (documents missing ring; focus lands in off-screen panel) | V1 | 2 |
| 52 | reduced-motion-note (panel captured ~0.2 s after open under `prefers-reduced-motion: reduce`) | V1 | 2 |
| — | **Total** | | **122** |

Not captured: the short screen recording of panel open/close and rail collapse (§G "Also record") — frames 03/04 and 03/08 stand in; a recording is deferred to phase 16 verification.

### §0.5 Source-verified component inventory (substitute for DOM inventory)

Verified with `rg`/`python3` on the clone (EV-S07):

- Primitives (`primitives.jsx`, 20 exports): `F`, `THEMES`, `Surface`, `Btn`, `Badge`, `Dot`, `Avi`, `Toggle`, `Input`, `Select`, `Progress`, `Sparkline`, `Table`, `SlideOver`, `Modal`, `Field`, `SectionLabel`, `PrimaryNavTabs`, `SubNav`, `PageHeader` (§A.4 listed 19 + `F`; count matches).
- Icons (`icons.jsx`): 63 exported function components (`rg -c "^export (const|function) [A-Z]"` → 63) — matches §A.5.
- Themes: `THEMES.light/dark/dimmed` each have exactly 40 keys (parsed) — matches §A.4. Default theme is hard-coded `"light"` (`cc-org-dash.jsx` L71, L74).
- Sample data (`data.jsx`, 11 exports): `spark`, `DB`, `INBOX_THREADS`, `INBOX_WORKSPACES`, `GLOBAL_COMMAND`, `FILE_FOLDERS`, `FILE_DATA`, `FILE_ICONS`, `WORKFLOW_PRESETS`, `ROADMAP_QUARTERS`, `ACTIVE_CYCLE` (§A.6 lists these grouped; `FILE_ICONS` and `spark` are the two not named individually there).
- Line references re-cited on the clone: localStorage keys `cc-org-dash.jsx` L37–40 (§A.1 said L37–41 ✔); `TABS` L26 ✔; `topOffsetPx={isMobile ? 104 : 116}` L460 (§A.1 cites L441–447 for the panel mount — actual mount is ~L457–463, within the ±5 tolerance only loosely; treat §A.1 shell line numbers as ±15); `GlobalAgentPanel.jsx` `PANEL_W = 420` L14 ✔, `[Demo] Using ${model}…` reply at L69 (§A.3/EV-U07 said L58–74 ✔); `useIsMobile.jsx` `innerWidth <= breakpoint` L6/L9 ✔; `PlatformStatusBar.jsx` random ticker `setInterval` L206 and tick L213 ✔, portal z-index 10049/10050 L247/L261 ✔; shell top bar `zIndex: 520` L179 ✔; command palette scrim `zIndex: 400` L466 ✔; `SlideOver` scrim/panel z 200/201 `primitives.jsx` L444/L448 ✔; `Modal` z 300 L470 ✔.
- Styling model: `rg -n "className" src/components/cc-org-dash` → **0 matches** (exit 1); `rg -n "className" src/pages/cc-org-dash.jsx` → 0; `rg 'var\(--'` across shell files → 0. All shell styling is inline from `THEMES` (confirms §A.7 and EV-U09, including `InboxScreen.jsx` which was `PARTIAL` for UI/UX).
- Third-party imports across all 21 shell files: `react` (18 files) and `react-dom` (1 file, `PlatformStatusBar`) only; every other import is relative (`./primitives` ×17, `./icons` ×14, `./data` ×12, `./WorkflowVis` ×1, `../components/cc-org-dash/*` from the shell page). Confirms EV-U03: no heavy dependency (`three`, `recharts`, `framer-motion`, `@stripe/*`, `leaflet`, …) is imported by the shell.
- Fonts: `index.html` L7–9 preconnects to Google Fonts and loads **Roboto** 400/500 only; neither Inter nor JetBrains Mono is loaded or bundled, so the `F.sans`/`F.mono` stacks (`primitives.jsx` L5–6) fall back to `-apple-system`/`ui-monospace` unless installed locally. Confirms OQ-U4 (vendor Inter + JetBrains Mono for the desktop; remove the Google Fonts request for offline/privacy).
- Dev stubs confirmed: `src/lib/AuthContext.jsx` (71 lines) and `src/api/entities.js` (52 lines; `localStorage.getItem/setItem` L12/L20) — neither is imported by the shell (`cc-org-dash.jsx` uses its own `cc-org-dash-auth` key), matching PRD-A.16's removal list.

### §0.6 Contrast verification (tool-computed, WCAG 2.1 relative luminance; EV-S08)

Computed with a Python implementation of the WCAG 2.1 formula on the hex values in `primitives.jsx` L11–110 (`/tmp/contrast.py`, reproduced in evidence). Normal-text AA threshold 4.5:1; large-text/UI 3:1.

| Theme | Token | Hex | on `surface` | on `canvas` | on `raised` | Verdict (normal text) |
|---|---|---|---|---|---|---|
| light | `t1` | `#1e293b` | 14.63 | 13.75 | 13.27 | AAA |
| light | `t2` | `#64748b` | **4.76** | 4.47 | 4.32 | AA on white only; **below 4.5 on `canvas`/`raised`** |
| light | `t3` | `#94a3b8` | 2.56 | 2.41 | 2.33 | FAIL (UI/UX estimate ≈2.5 confirmed) |
| light | `t4` | `#a8b4c4` | 2.10 | 1.98 | 1.91 | FAIL (estimate ≈2.0 confirmed) |
| dark | `t2` | `#9fb0cc` | 7.94 | 8.39 | 7.24 | AAA |
| dark | `t3` | `#7c8ca8` | 5.13 | 5.42 | 4.68 | AA (estimate ~4.6 confirmed) |
| dark | `t4` | `#647896` | 3.88 | 4.10 | 3.54 | large text / UI only |
| dimmed | `t2` | `#9aa8bc` | 5.69 | 6.42 | 4.89 | AA |
| dimmed | `t3` | `#7d8ba0` | 3.97 | 4.48 | 3.41 | **large text / UI only** (UI/UX estimate ~4.4 was optimistic; fails 4.5 on all three) |
| dimmed | `t4` | `#6b788c` | 3.07 | 3.46 | 2.64 | UI only; FAIL on `raised` |
| light | D-3 proposed `t3` | `#6b7a90` | **4.36** | 4.10 | 3.96 | **does not reach 4.5:1** (UI/UX estimated ≈4.6) |
| light | SE alternative `t3` | `#617083` | 5.06 | 4.75 | 4.59 | AA on all three light backgrounds |
| light/dark/dimmed | white on `accent` (`btnPrimary` text) | `#3b82f6` / `#60a5fa` / `#6b9ef5` | 3.68 / 2.54 / 2.68 | — | — | 13px button labels fail AA in all themes (UI-component 3:1 passes only in light) |

Findings for UI/UX and the owner (recorded in the SE handoff §9 as F-S1): D-3 as written does not achieve AA; `#617083` (or `t2` `#64748b` on white only) does. Dimmed `t3` and `t4`, dark `t4`, and white-on-accent primary buttons also need treatment in phase 1 (larger type, darker accent for button fills, or `t2` for metadata text). These are token-level, reversible, and do not change layout; §E and §H remain the UI/UX-owned specification.

## §A Reference inventory

### A.1 Shell (`src/pages/cc-org-dash.jsx`)

| Element | Ref evidence | Notes |
|---|---|---|
| 8 primary tabs: Dashboard, Work, Inbox, People, Data, Files, Integrations, Settings (+ hidden `account`) | `TABS` L26–35; `account` reachable only via profile menu L300–306 and tab switch L408 | Icons 16px from `icons.jsx` |
| Persisted UI keys (localStorage) | `cc-org-dash-theme`, legacy `ecoos_theme`, `cc-global-command-open`, `cc-org-dash-auth` L37–41 | Auth is a dev stub (email/name JSON), see AuthPortal |
| Theme default `light`; `THEMES[themeKey]` | L67–77, L80–82 | No system-preference detection |
| Top bar height 60 desktop / 52 mobile; padding 16/10 | L176 | Contains: rail toggle (36×36, purple border), wordmark `cc-org-dash` (JetBrains Mono 15/700), search button (`⌘K`, max 400), create menu (+), bell with unread dot, avatar/profile menu, agent-panel toggle (36×36, `Bot`) |
| Command palette ⌘/Ctrl+K | listener L134–137; overlay L451–485, z 400, width 520, results grouped "Jump to / Actions / Agents" from `TABS` and `DB.agents` L155–162 | No arrow-key navigation; ESC hint only (no handler) |
| Primary tabs row (`PrimaryNavTabs`) under top bar, notched active tab | L332–344 | Inbox badge = unread notifications |
| Body = `GlobalCommandRail` (left) + main column (`maxWidth 1280`, padding 24/28 desktop, 16/12 mobile, `paddingBottom 38` for status bar) | L347–425 | Mobile: rail rendered above content with a toggle button L353–378 |
| Global overlays: `SlideOver` (460 wide) for command detail L427–437; `NotifDrawer` L439; `GlobalAgentPanel` L441–447 (`topOffsetPx` 116/104); `PlatformStatusBar` L449 | z-order: top nav 520 > agent panel 500/499 > cmd palette 400 > modal 300 > slideover 201/200; status bar portal 10050 | Click anywhere on root closes menus (`onClick={close}` L165) |
| Theme easing `cubic-bezier(0.32,0.72,0,1)` ("ATLAS_EASE") | L41 | Also in GlobalAgentPanel L13, PlatformStatusBar L6 |

### A.2 Screens (`src/components/cc-org-dash/`)

| File | Size | What it renders | Sub-navigation | Data | Demo/simulation to remove |
|---|---|---|---|---|---|
| `HomeScreen.jsx` | 24 488 | Greeting + "Dashboard" title L187–192; `SubNav` Overview/Pulse/Starred/Following L172–177; range pills 7d/30d/90d L198–219; onboarding strip "Finish setup" L221–234; 4 circular KPIs L237–260; 4 stat cards L263–277; Throughput area chart + Work-mix donut L279–330; Team delivery chart L332–370; Active Projects list + Recent activity L372–455; project `SlideOver` L457–510 | SubNav | `DB.stats/projects/tasks/activity/integrations` | `buildSeries()` pseudo-random series L24–32; hard-coded "Due this week 12" L183; `TEAMS_PERF` L126 |
| `WorkScreen.jsx` | 34 382 | Header "Work" + "New issue" L153–162; `SubNav` Projects/Issues/Board/Roadmap/Workflows/Wiki L143–150; Projects `Table` L167–183; Issues grouped list with `IssueTicketRow` (checkbox, key, dot, title, labels, due, avatar) L49–88, L185–270 incl. sticky bulk bar; Roadmap 3-column (list/timeline/cycle) L272–370; Kanban 4 columns HTML5 drag L372–490; Workflows → `WorkflowVis` L492; Wiki empty state L494–501; detail `SlideOver` (Edit / Close issue) L503–520; "New Issue" `Modal` L522–535 | SubNav | `DB.projects/tasks/people`, `ROADMAP_QUARTERS`, `ACTIVE_CYCLE`, `WORKFLOW_PRESETS` | Fake timeline bar positions L318–326; burndown SVG L347–352; `cycles` alias effect L133–136 |
| `InboxScreen.jsx` | 51 515 | Ticketed agent conversations: workspace switcher, `SubNav` All/Mentions/Starred/Archived L248–251, thread list, message pane, detail rail; compose public/internal L218–235; reactions | SubNav | `INBOX_THREADS`, `INBOX_WORKSPACES`, `DB.chats/agents` | Canned assistant reply "[Connect your OpenAI key…]" L230; rail state in localStorage `ccod_inbox_rail_*` L38–39 |
| `PeopleScreen.jsx` | 6 873 | People `Table`, Teams cards, Pending invites; person `SlideOver`; Invite `Modal` | SubNav | `DB.people/tasks` | Static teams/invites arrays |
| `DataScreen.jsx` | 18 244 | Collapsible `DataAppsRail` (228/52) L60–262; `SubNav` Metrics/AI Traces/Events/Alerts; live sparkline stat cards (2 s interval) L266–274; "AI Run Traces" `Table` (name, agent, model, tokens, cost, latency, status, time) L330–372; "Trace Detail" `SlideOver` L456–478 | SubNav + rail | `DB.stats`, `spark()` | Random sparkline mutation; hard-coded trace rows L336–343 |
| `FilesScreen.jsx` | 23 805 | Dropbox-style: left nav 228, list/grid toggle, detail panel 240, Upload `Modal` | None (nav) | `FILE_FOLDERS`, `FILE_DATA` | Hard-coded neutral colours `#6e7781`/`#1f2328` L22–26 bypass THEMES |
| `IntegrationsScreen.jsx` | 6 867 | Header + "Add integration"; `SubNav` Installed/Browse/Webhooks; category filter; 2-col integration cards (logo, status dot+badge, users, last sync) L43–61; detail `SlideOver` with Permissions toggles, View logs / Disconnect / Reconnect L84–118 | SubNav | `DB.integrations` | Emoji logos; toggles no-op |
| `SettingsScreen.jsx` | 36 806 | Left pill nav (220) L207–225: General, AI & Agents, Notifications, Security, Plan & Billing, Team, Appearance, Docs; Appearance lists `THEMES` L467–481; AI tab stores OpenAI key in localStorage L154, L179; Security shows API keys; Billing shows plan prices L193–197 and Upgrade `Modal` L600–624; Docs is a 3-pane doc site L232–450 | Sidebar | `DB.agents/people`, `THEMES` | Prices, API key in browser storage, "LangSmith Project", "Ask AI" FAB L432–450 |
| `AccountScreen.jsx` | 20 451 | Sidebar groups General / Contact & access L70–88; Public profile form, Branding, My link, Phone, Login & security toggles, Cookie settings; Delete account `Modal` | Sidebar | none (static) | "EcoAdmin" identity; "demo" copy |
| `AuthPortal.jsx` | 22 733 | Login / Sign-up cards (max 400/420), Google button, `AuthFooter` fixed bottom with language + theme cycler L106–190; theme order light→dark→dimmed L16 | — | none | Pre-filled demo credentials L254–262; fake Google sign-in L287–289 |
| `WorkflowVis.jsx` | 18 162 | Node-graph editor: left rail 216, SVG canvas with orthogonal connectors, right node inspector 210, Node/Sequence toggle, "AI assist" banner, Run/Save | — | `WORKFLOW_PRESETS` | Purple hard-coded `#8250df`/`#5a32a3` L330–333 |

### A.3 Global panels and rails

| Component | Ref evidence | Behaviour |
|---|---|---|
| `GlobalCommandRail.jsx` (9 553) | widths open 264 / closed 54 L15; header "Company command · Portfolio · ops · risk" L82–85; sections LIVE SIGNALS (Critical/Attention/FYI counts) L86–124, INITIATIVES L126–160, OBJECTIVES & MILESTONES (collapsible "Execution") L162–200, BLOCKERS (red tint rows) L202–228, EXEC PINBOARD L230–242 | Every row calls `onSelectDetail({kind,id|group})`; closed state renders nothing inside (no icon strip) L60–62 |
| `GlobalCommandDetail.jsx` (6 770) | `getGlobalCommandTitle` L4–18; footer "Open Work" / "Close" L34–43; branches for signals-feed, initiative, objective, milestone, blocker, note L45–165 | Rendered inside shell `SlideOver` width 460 |
| `GlobalAgentPanel.jsx` (22 831) | fixed `aside` right, width 420 (`PANEL_W` L14), top 116/104, height calc L113–134; scrim L96–112; browser-style session tabs + "+" L136–222; message list (bubbles 18px radius, assistant labelled) L224–258; footer: "Model & parameters" (model select gpt-4o/…, temperature 0–2, max tokens 512–16384, scope organization/project/inbox-only) L261–368; "Variables & context" (tenant_id/env/locale) L370–427; Agent / Sources menus + attach L429–556; pill composer (textarea rows 2, Enter sends, Shift+Enter newline, round send button) L558–615 | `send()` appends `[Demo] Using ${model}…` L58–74 — simulated reply handler named in PRD-B.5 |
| `PlatformStatusBar.jsx` (15 736) | `SIGNAL_LABELS` 17 chips L10–28; `chipStyle` maps to THEME colour trios L57–86; collapsed 32px bar: `Activity` icon, mono age (72px), latest message, live chip (`aria-live="polite"`), chevron L322–400; expanded feed max 40vh/380px with absolute timestamps L253–320; Escape closes L221–228; `createPortal` to body, z 10050 L409 | Seeds 12 fake events L181–204 and pushes random events every 4.5–10 s L206–214 — simulation |
| `NotifDrawer.jsx` (1 982) | `SlideOver` width 360, "Mark all read", severity dot, unread rows tinted `raised` | Local state only from `DB.notifications` |
| `useIsMobile.jsx` (541) | `window.innerWidth <= 768` L4–13 | Single breakpoint for entire shell |

### A.4 Primitives (`primitives.jsx`)

| Export | Ref lines | Anatomy / tokens | Accessibility gaps (to fix in migration) |
|---|---|---|---|
| `F` | L4–7 | `sans` Inter stack; `mono` JetBrains Mono stack | Fonts not bundled; SE must vendor Inter + JetBrains Mono for Tauri offline |
| `THEMES.light/dark/dimmed` | L10–137 | 40 keys each: `pageGradient, bg, canvas, surface, raised, hover, border, borderMuted, borderHover, t1–t4, accent(+Bg/Border/Hover), green/red/amber/purple (+Bg/Border), nav, navText, navActive, navHover, btnPrimary(+Hover), shadow, shadowSubtle, shadowMd, shadowLg`; light accent `#3b82f6`, purple `#7c3aed`; dark surface `#121a28`; dimmed surface `#262d3f` | `t3` light `#94a3b8` on `#ffffff` ≈ 2.5:1 and `t4 #a8b4c4` ≈ 2.0:1 — fail WCAG AA for text; see §E/§H |
| `Surface` | L140–158 | radius 10, 1px border, `shadowSubtle` rest / `shadowMd` hover | Clickable `div` when `onClick`; no role/tabIndex |
| `Btn` | L161–193 | variants primary/default/ghost/outline/accent/danger/success; radius 6; 13px/12px small | Hover via JS state; no `:focus-visible`; `disabled` opacity .5 |
| `Badge` | L196–218 | pill h20, 12px | — |
| `Dot` | L221–231 | status→colour map incl. `disconnected/error` red, `in_progress` accent, `paused/todo` t3 | Colour-only; needs adjacent text or `aria-label` |
| `Avi` | L233–243 | initials, 7-colour palette by first char | Decorative; add `aria-hidden` or name |
| `Toggle` | L245–259 | 32×18 `div` | Not a control: needs `button role="switch" aria-checked` |
| `Input` / `Select` | L261–303 | focus ring `0 0 0 3px accentBg` | OK; `Select` custom chevron via data-URI |
| `Progress` | L305–315 | h6 bar | needs `role="progressbar"` + values |
| `Sparkline` | L317–328 | SVG polyline | decorative |
| `Table` | L331–440 | `card`/`flush` variants; header 12/600; row 14×18 padding; `emptyMsg` default "No data"; selection `accentBg` | Row click not keyboard reachable |
| `SlideOver` | L442–468 | fixed right, width 420 default, top 116/100, scrim `.4`, `translateX` 250 ms; header title/subtitle + ✕ | No focus trap, no ESC, ✕ has no `aria-label`; computes mobile from `window` at render (no hook) |
| `Modal` | L470–486 | centred, max 520, 88vh, z 300 | No focus trap/ESC/`role="dialog"` |
| `Field`, `SectionLabel` | L488–505 | label 14/600; hint 12 | `label` not associated (`htmlFor`) |
| `PrimaryNavTabs` | L511–620 | notched active tab radius 11, canvas fill, badge pill | Buttons, not `role="tablist"`; no arrow-key nav |
| `SubNav` | L623–705 | capsule pills on `raised` bar radius 12; count pills | same |
| `PageHeader` | L708–725 | breadcrumb "org / name" + `Private` badge | Unused by shell screens (they inline headers) |

### A.5 Icons (`icons.jsx`, 14 713)

63 inline lucide-compatible SVG components via `Svg` wrapper (L3–21: `size`, `color`, `strokeWidth` default 2, `viewBox 0 0 24 24`): Home, Briefcase, Inbox, Users, BarChart3, FolderOpen, Plug, SettingsIcon, Search, Bell, Plus, ChevronDown, User, LogOut, GitBranch, CheckCircle2, ArrowUp, CircleDot, LogIn, AtSign, Star, Archive, Edit2, Paperclip, Smile, Code2, Bot, Clock, Upload, LayoutGrid, List, ChevronRight, ChevronLeft, ExternalLink, PanelLeft, Target, Calendar, GitPullRequest, Activity, TrendingUp, TrendingDown, Shield, Mail, UserPlus, Zap, Key, Lock, Eye, EyeOff, Globe, CreditCard, Palette, Sun, Moon, Workflow, BookOpen, AlertCircle, Trash2, ImageIcon, MoreHorizontal, MoreVertical, Rocket, Monitor. No `aria-hidden`/`role="img"` on any. EL additions needed (same style): Pause, Play/Resume, StopCircle (cancel), RotateCcw (recovery/retry), ShieldCheck (approval), Database/Brain (memory), Coins (cost), WifiOff (disconnected), Pin/PinOff, Undo (adaptive), KeyRound (grant).

### A.6 Sample-data contracts (`data.jsx`) — all are demo fixtures, prohibited in production screens (PRD-A.16)

| Export | Lines | Shape (fields) | EL replacement source |
|---|---|---|---|
| `DB.stats` | 5–10 | `{id,label,value,delta,up,color}` | Health checks (P17) + ledger counts |
| `DB.activity` | 11–18 | `{id,user,action,time,type,dot}` | Audit/provenance events (P13) |
| `DB.projects` | 19–26 | `{id,name,dept,status(on_track/at_risk/planning/done),progress,owner,due,priority}` | Ledger `Project` |
| `DB.tasks` | 27–37 | `{id,issueKey,title,project,assignee,priority,status(todo/in_progress/review/done),due,labels[]}` | Ledger `Task`/assignment |
| `DB.people` | 38–45 | `{id,name,role,dept,status,email}` | `Member` + `Seat` |
| `DB.agents` | 46–52 | `{id,name,role,status(online/idle/paused),model,calls}` | `Agent` (P01) — model shown only in technical views |
| `DB.integrations` | 53–64 | `{id,name,cat,status(connected/degraded),logo,users,synced}` | `Connector`/`ProviderAccount` + registry status |
| `DB.notifications` | 65–71 | `{id,sev(high/medium/low),title,body,time,read}` | Notification service (PRD-E.4 completion, approvals) |
| `DB.chats` | 72–92 | `{role,name,content,time}` per agent | Persisted Hermes sessions (PRD-B.5) |
| `INBOX_THREADS`, `INBOX_WORKSPACES` | 96–180 | ticket-like threads | R2 (B12) |
| `GLOBAL_COMMAND` | 183–215 | `signals{critical[],attention[],fyiCount}`, `initiatives[{health}]`, `objectives[{progress}]`, `milestones[{date,risk}]`, `blockers[{impact,team}]`, `notes[]` | Health checks, approvals, projects, plan milestones, ledger blockers, decisions |
| `FILE_*`, `WORKFLOW_PRESETS`, `ROADMAP_QUARTERS`, `ACTIVE_CYCLE` | 217–378 | files, node graphs, quarters, cycle | R2+/deferred |

### A.7 Theme sources: `src/index.css`, `tailwind.config.js`

- `index.css` defines shadcn HSL variables (`--background`, `--primary`, `--sidebar-*`, `--radius .5rem`) for `:root` and `.dark` L5–76 and applies `bg-background text-foreground` to `body` L84–87. `tailwind.config.js` maps them (`darkMode: ["class"]`, `tailwindcss-animate`) L1–86.
- Finding: **no `cc-org-dash` file uses Tailwind classes or these variables**; every shell component styles inline from `THEMES`. `index.css` matters only for body background before React mounts and for `src/components/ui/*` (shadcn) which the shell does not import. Migration rule: keep `THEMES` as the single token source; optionally emit CSS custom properties from `THEMES` for global `body`, scrollbars, focus ring; Tailwind is not required for the R1 shell.

## §B Seven-view specification

Conventions: state matrix uses L=loading, E=empty, X=error, D=disconnected (API/SSE unreachable or Hermes unavailable), P=pending approval, R=running, C=completed, Z=restricted (seat lacks grant). Seat columns: F=Founder, PL=Project Lead (R2), OP=Operator (R2). Copy must be plain language (NFR-8); never expose prompts, schemas, runtime config outside designated technical views (PRD-A.14).

### B.1 Home — R1

| Item | Specification |
|---|---|
| Purpose | Answer "what needs me now" and start work via the universal assistant (PRD-A.13). |
| PRD | A.13, A.4, A.16, A.17 (`proposal` read-only registry entry point), E.4 (completion notifications surface), G.6 (allowance only), NFR-2/3/8; R1-ACC-2, R1-ACC-13. |
| Layout (regions → reference) | Keep `HomeScreen` header (greeting + title, rename "Dashboard"→"Home") L187–192 and `SubNav` L194 (tabs: Overview · Decisions(count) · Running(count) · Registry). Replace metrics/charts blocks (L198–370) with five regions in the same grid rhythm: (1) **System health** strip = 4 `Surface` KPI cards (pattern L237–260) for API, workers/Hermes, database, bound repository — each `Dot` + label + last check time; (2) **Active priorities** = Active Projects list pattern L372–425 fed by ledger priorities/plans with `Progress`; (3) **Running work** = right column list (Recent activity pattern L427–455) of runs with status `Badge`, elapsed, estimated cost, "Open run" link; (4) **Required decisions** = approvals list rows (pattern from `GlobalCommandDetail` signal rows L45–63) with Approve/Reject `Btn` (danger for reject) and target/version text; (5) **Universal assistant prompt** = full-width `Surface` (onboarding-strip pattern L221–234) with heading "What would you like to do?", a single `Input` and mode chips (Ask/Analyse/Plan/Draft/Execute/Review); submit opens `GlobalAgentPanel` with the text pre-filled. Region order desktop: (5) top, (1), then 2-col grid [(2)+(4)] / (3). |
| Primary actions | Ask the assistant (submit prompt); Approve / Reject decision (P→ reauth if destructive, PRD-D.7); Open run; Open work item. |
| Secondary | Create priority/plan (`+` menu in top bar, keep pattern L242–262 with items New priority / New plan / New request); View registry; Retry health check. |
| Data | `GET /health` composite; ledger priorities/plans; runs (status, started, est. cost, allowance remaining); approvals (action, target, version, requester); notifications unread. |
| State matrix | L: skeleton cards (same dimensions, `raised` fill, no shimmer under reduced motion). E: each region has own empty copy — "No priorities yet. Create one or ask the assistant." / "Nothing running." / "No decisions waiting." Health region never empty. X: region-level inline error `Surface` with `AlertCircle`, message, "Retry" — other regions keep rendering. D: health strip shows `disconnected` dots + banner "Can't reach Engine Labs cloud. Showing last known state from HH:MM. Work already started continues in the cloud." (PRD-E.4). P: decisions region count badge on SubNav; row shows "Waiting for you". R: running region rows with live `Progress`/elapsed via SSE. C: completed runs appear for 24 h with `done` dot and "View result". Z: regions the seat cannot read render "Not in your scope" card, no counts leak (PRD-D.5). |
| Seat visibility | F: all five regions, org-wide. PL: priorities/running/decisions filtered to delegated scope; health = summary only (no host/DB detail). OP: own assignments, own runs, decisions addressed to them; health = single "All systems normal / Degraded" line. |
| Accessibility | Region landmarks (`section aria-labelledby`); h1 "Home", h2 per region; KPI cards convey status by text + icon (not colour alone); assistant input has visible label; approvals buttons named "Approve <action>"; live region (`aria-live=polite`) for run status changes throttled ≥5 s; all lists keyboard navigable; skeletons `aria-busy`. |

### B.2 Work item — R1

| Item | Specification |
|---|---|
| Purpose | One ledger record (priority, plan, task/assignment, request) with its loop chain and evidence (PRD-B.1). |
| PRD | A.3, A.10 (filters persist), A.16, B.1, B.3, B.8 (status evidence links), D.5, NFR-8; R1-ACC-2, R1-ACC-6. |
| Layout | **List**: keep `WorkScreen` header L153–162 and `SubNav` L143–150 reduced to Priorities · Plans · Assignments · Board (R1) — Roadmap/Workflows/Wiki deferred (§H). Grouped list uses `IssueTicketRow` L49–88 (checkbox, key, `Dot`, title, labels, due, `Avi`) with groups from ledger statuses; Projects `Table` L167–183 for plans. **Detail**: promote the `SlideOver` L503–520 to a dedicated detail view (route `/work/:id`) — `SlideOver` remains as quick-peek from lists. Detail regions: header (key, title, status `Badge`, priority `Badge`, owner `Avi`, due); **Loop chain** stepper of the eleven PRD-B.1 stages (horizontal on ≥1280, vertical below) each with state dot and link to its record/artifact and revision SHA; **Details** key/value rows (pattern L508–513); **Dependencies** list; **Runs** table (pattern `DataScreen` L330–372: run, mode, status, cost, started); **Evidence & decisions** list with provenance; **Activity** timeline. |
| Primary | Create/edit (Modal pattern L522–535 with Title, Plan, Priority, Due, Assignee — assignee from `Member`, not `DB.people`); Start a run on this item (opens assistant panel scoped to item, mode Plan/Execute); Change status (bulk bar pattern L253–262). |
| Secondary | Link dependency; Add decision; Open branch/PR (external handoff, PRD-A.5 style); Close item (`danger`, confirm). |
| Data | Ledger record + children; loop stage records; runs by item; evidence links; repository binding status for stages needing it. |
| State matrix | L: list skeleton rows (8) / detail skeleton header + stepper. E: list "No work yet — create a priority to begin." with primary `Btn`; detail sections: "No runs yet", "No evidence yet". X: list-level error card + Retry; detail: header renders from cache, failed sections show inline error. D: banner as B.1; editing disabled with tooltip "Reconnect to save"; reads served from cache labelled "Last synced HH:MM". P: stage chip "Awaiting approval" with who/what; item-level `Badge` amber. R: stage chip animated dot (static under reduced motion) + link "View run". C: stage chips `done`; item status `done`; "Release proposal exists" callout when PRD-B.3 reached. Z: item not in scope → 404-equivalent "You don't have access to this item" (no title leak, PRD-D.5); stage records the seat cannot read show "Restricted" chip. |
| Seat visibility | F: all items, edit, close, start runs. PL: items in delegated projects; cannot edit org-wide defaults. OP: assigned items; can update status/report exception; cannot delete or reassign beyond assignment. |
| Accessibility | Stepper = `ol` with `aria-current="step"`; status conveyed by text; checkbox rows keep `role="button"`/Enter/Space (present in ref L52–57); bulk bar announces selection count; Modal gets `role="dialog"`, focus trap, ESC, focus return; due dates as `<time datetime>`; label pills have ≥4.5:1 text (ref `labelPillStyle` L7–15 uses HSL 26% L on 92% L — passes, keep). |

### B.3 Assistant (universal) — R1

| Item | Specification |
|---|---|
| Purpose | Conversational entry to every capability under backend-enforced mode/tool access (PRD-E.1), persisted and streamed (PRD-B.5). |
| PRD | A.13, A.14, B.5, E.1, E.2 (sponsor/scope shown), E.4 (close ≠ cancel), G.6, NFR-3 (assistant panel preserved); R1-ACC-7. |
| Layout | Keep `GlobalAgentPanel` geometry exactly: fixed right, width 420, top 116/104, scrim, ATLAS_EASE slide L96–134; browser-style session tabs + "+" L136–222 (sessions = persisted conversations, tab title from first user message, close tab = archive, never delete); message list L224–258 with assistant label and streaming cursor. **Footer replaced**: remove "Model & parameters" L261–368 and "Variables & context" L370–427 entirely from Operator/PL and from Founder default (PRD-A.14). Footer becomes: row 1 = **Mode** segmented chips (Ask · Analyse · Plan · Draft · Execute · Review; Automate shown disabled "Coming later" R3) reusing scope-chip style L329–350; **Scope** pill ("Organisation" / "Project: X" / "Item: KEY") reusing Agent/Sources pill style L433–450, read-only unless seat may widen; row 2 = "Remaining allowance: N · This action ≈ est." mono text (PRD-G.6). Composer unchanged L558–615 (Enter sends, Shift+Enter newline). Founder-only "Technical details" link opens a designated technical `SlideOver` (session id, model band, policy version) — never inline. |
| Primary | Send; Stop generating (replaces send button while streaming — this stops the reply, not the run); New tab; Switch mode. |
| Secondary | Open run (when reply spawned a run — inline run card with status/"Open"); Approve inline when the assistant requests approval (card with action/target/version, Approve/Reject); Attach (R2); Archive tab. |
| Data | Sessions list; messages; SSE events (token, tool call summary in plain words, run started, approval requested, error); allowance + estimate; mode set permitted for seat. |
| State matrix | L: panel opens immediately with skeleton bubbles while history loads. E: greeting from server config (replaces canned text L20–26): "What would you like to do?" + 3 suggested actions from home data. X: failed send → message row with red border, "Couldn't send. Retry" button; message retained in composer. D: composer disabled, placeholder "Reconnecting…"; banner inside panel; on reconnect, history re-streams and a "Resumed" divider appears (PRD-E.4). P: approval card, panel tab shows amber dot. R: streaming indicator; if a run was started, run card shows live status; **closing the panel or app never cancels** (label under card: "Closing this panel won't stop the work"). C: run card `done` + "View result"; completion notification also goes to NotifDrawer. Z: mode chips the seat lacks are hidden (not disabled); server refusal renders "That action isn't available in your scope" — no policy text. |
| Seat visibility | F: all six modes, scope switch, technical details link. PL: modes within delegated ceiling (PRD-E.2), scope = delegated projects. OP: modes per assignment (default Ask/Analyse/Draft), scope fixed to assignment, no technical link. |
| Accessibility | `aside role="complementary" aria-label="Assistant"`; focus moves into panel on open and returns on close; ESC closes panel (not cancel); message list `role="log" aria-live="polite"` (streaming announced at sentence boundaries); tabs `role="tablist"` with arrow keys; mode chips `role="radiogroup"`; send/stop buttons have `aria-label`; scrim not focusable. |

### B.4 Agent run — R1

| Item | Specification |
|---|---|
| Purpose | Supervise one run: status, scope, sources, model/tool usage, budget, pause/cancel, recovery (PRD-B.6). |
| PRD | B.6, E.2, E.4, E.7, E.8 (recovery/incident/escalation), G.6/G.11 (cost & usage per run), A.14, D.12; R1-ACC-3, R1-ACC-8. |
| Layout (documented extension) | New view `/runs` list + `/runs/:id` detail built from primitives; nearest references: `DataScreen` AI Run Traces `Table` L330–372 (columns → run, item, mode, status, started, elapsed, est./actual cost) and its "Trace Detail" `SlideOver` L456–478 (key/value rows). Detail layout: header (run title = purpose; status `Badge`; sponsor `Avi`; acting identity; deadline) with action cluster right (Pause / Resume / Cancel); **left column** (2/3): **Progress** — step list (`ol`) with checkpoint marks, current step live line, expandable plain-language tool receipts ("Read 3 files", "Ran tests: 14 passed"); **Recovery** callout appears on retry/diagnostic/escalation events (PRD-E.8) with what happened and proposed next action; **right column** (1/3, 340px like Home L372): **Scope** card (organisation/project/item, grant classes in words), **Sources** card (list of sources with `Dot` and last-sync), **Usage** card (model band, tool calls, execution time, tokens as bars; PRD-G.11), **Budget** card (`Progress` reserved vs allowance, est. cost; PRD-G.6). Runs list uses `SubNav` Running · Waiting · Completed · Failed. |
| Primary | Pause (→ `paused`), Resume, **Cancel** (confirm dialog: "Stop this run? Work done so far is kept. This can't be undone." — distinct from closing; PRD-E.4), Approve/Reject when P. |
| Secondary | Open work item; Open conversation; Copy run id (technical, Founder); Retry (only when failed and policy allows); Report problem. |
| Data | Run record (9 PRD-E.2 fields), steps/checkpoints, receipts, SSE events, incidents/escalations, usage events, budget reservation, approval requests. |
| State matrix | L: header skeleton + 5 step placeholders. E (list): "No runs yet. Start one from a work item or the assistant." X: event stream error → "Live updates paused. Retrying…" then "Show what we have"; detail from last snapshot. D: same as X plus global banner; **run keeps going in cloud** — copy states it explicitly. P: status `waiting for approval`, step highlighted amber, approval card pinned at top of Progress; Pause/Cancel still available. R: `in_progress` accent dot, elapsed ticks, current step streams; Pause/Cancel enabled. C: `done` green, "Completed HH:MM", result/artifact links, usage final; actions collapse to Open item/Open conversation. Also `cancelled` (t3 dot, "Stopped by <who> at HH:MM") and `failed` (red, incident summary + escalation next action). Z: run outside scope → access message; within scope but lacking cancel authority → Cancel hidden, tooltip-free "Ask <sponsor> to stop this run" text. |
| Seat visibility | F: all runs, all controls, technical ids. PL: runs in delegated scope; pause/cancel runs they sponsor; usage without model band detail. OP: own runs; pause/cancel own; usage shows only remaining allowance/est. cost (PRD-G.6). |
| Accessibility | Status text always adjacent to dot; step list `aria-current`; SSE updates to `aria-live=polite` at step boundaries only; Cancel confirm is a modal with focus trap and default focus on "Keep running"; elapsed timer not announced; charts have text equivalents; controls ≥32px hit area (ref `Btn` 5×14 padding → enforce `minHeight: 32`). |

### B.5 Connection setup — specified now, built R2 (registry read-only R1 `proposal`)

| Item | Specification |
|---|---|
| Purpose | Register a provider account, grant scoped access, show truthful status and recovery (PRD-A.5–A.9, C.7). |
| PRD | A.4 (explain what needs a connection), A.5, A.6, A.7, A.8, A.9, A.17, C.3, C.7, D.6; R1-ACC-13. |
| Layout | Adapt `IntegrationsScreen`: header + "Add connection" L21–28; `SubNav` → Connected · Available · Unavailable (statuses per §3.2 vocabulary) replacing Installed/Browse/Webhooks L14–18; card grid L43–61 (replace emoji logo with provider glyph or initials `Avi`; card shows status `Dot`+`Badge` using registry status, scope summary, last verified time); detail `SlideOver` L84–118 → **Setup wizard** steps: 1 Choose provider, 2 Authorise (source-app handoff, opens external browser — Tauri shell.open; never embeds credentials), 3 Grant scopes (Permissions toggle list L104–110 becomes read-only source scopes + Engine Labs grant checkboxes per capability row), 4 Verify (runs check, shows outcome), 5 Done. Registry (R1) = same screen, read-only: list of 43 domain groups with capability rows and status chips; "Needs connection: X" text on rows (PRD-A.4). |
| Primary | Add connection; Reconnect (when `unavailable`); Revoke (danger, reauth PRD-D.7). |
| Secondary | View logs (audit for that connector); Test connection; Open in source app. |
| Data | Registry rows (owner, status, dependencies, required grants, status_evidence); `ProviderAccount` list; grant records; health checks. |
| State matrix | L: card skeletons. E: "No connections yet. Your bound repository appears here once set up." X: wizard step error with provider message translated to plain language + Retry. D: cannot start wizard; existing cards show cached status stamped. P: "Awaiting owner approval" when a non-owner requests a connection (R2). R: Verify step spinner "Checking access…". C: Verify success + summary of granted scopes. Z: OP sees registry read-only, no Add; PL sees Add only for delegated domains. `unavailable` rows carry recovery instruction text (PRD-A.9). |
| Seat visibility | F: full. PL: connections in delegated domain; cannot see other accounts' data. OP: read-only status. |
| Accessibility | Wizard `role="dialog"` with step heading focus on change; progress "Step 2 of 5"; external-handoff button announces "opens in your browser"; scope checkboxes with descriptions; status chips text+icon. |

### B.6 Memory manager — specified now, built R3 (R1 search/inspect via assistant per PRD-F.3)

| Item | Specification |
|---|---|
| Purpose | Search, inspect, correct, merge, restrict, archive, export, delete governed memory with provenance (PRD-F.1–F.4). |
| PRD | F.1, F.2, F.3, F.4 (retention settings), F.8 (erasure gated), D.5, A.14. |
| Layout | Documented extension using `FilesScreen` three-pane pattern (left nav 228 / list / detail 240) L206–213, L390–460 and `DataScreen` table. Left nav = memory kinds (Sessions · Preferences · Projects · Domains · Organisation · Skills) + class filter (Source / Approved / Inferred). List = `Table` (title, kind, class `Badge`, owner, verified state, expiry, version). Detail = provenance card (source, owner, source permissions, timestamps, verification, expiry, version — PRD-F.2), content preview, actions. Retention settings (PRD-F.4 four defaults) live in Settings → Data (Founder) and link here. |
| Primary | Search (`Input` with icon); Inspect; Correct (opens editor, creates new version); Restrict (scope picker). |
| Secondary | Merge (multi-select), Archive, Export (developer export R1 `proposal`), Delete (scoped, owner approval + reauth for org-wide, PRD-F.8 — three confirmations). |
| Data | Memory items with 7 provenance fields; class/kind; retrieval permission check results. |
| State matrix | L: list skeleton. E: "No memory yet. Knowledge the assistant retains will appear here with its source." X: search error inline. D: read-only cache, edits disabled. P: deletion/erasure awaiting approval → item `Badge` "Pending deletion". R: export job running (goes to Runs). C: export ready notification. Z: items outside permission never listed; derived summaries hidden when source restricted (PRD-F.3). |
| Seat visibility | F: all + retention + erasure. PL: domain/project memory; correct/restrict within domain; no erasure. OP: own preferences/sessions; inspect only. |
| Accessibility | Search results count announced; table sortable headers as buttons with `aria-sort`; destructive actions require typed confirmation; detail pane `aria-labelledby` item title. |

### B.7 Permissions editor (minimal, owner grants) — R1

| Item | Specification |
|---|---|
| Purpose | Founder views and grants bounded authority: seats, grant classes, repository grants (branch/change/check/release), agent ceilings (PRD-B.2, D.1–D.3, D.9, D.11). |
| PRD | A.10 (owner defaults), B.2, D.1, D.2, D.3, D.7 (reauth), D.9, D.11, D.13, E.2 (ceilings). |
| Layout | Adapt `SettingsScreen` frame (left pill nav 220 L207–225, content max 520–560) with tabs **Seats** (Team tab pattern L582–596: `Avi`, name, seat template `Badge`, `Dot`, "Edit grants"), **Grants** (matrix `Table`: rows = grant classes grouped by capability/registry row; cols = seats; cells = read-only chips in R1 for PL/OP templates, editable for Founder-created grants), **Repository** (four grant classes branch / change / check / release as `Toggle`-rows with description; release default off), **Agents** (ceilings: budget, modes, deadline). Edit opens `SlideOver` with grant detail: capability, actions allowed, scope, expiry, delegated-by; Save requires reauthentication when it widens access or is destructive (PRD-D.7) — modal "Confirm it's you". Security tab items (API keys L537–550) are **removed**; no key material in UI (PRD-D.13). |
| Primary | Grant / revoke; Set repository grant; Set agent ceiling; Save (reauth). |
| Secondary | View audit for grant; Compare seat templates (read-only table from §5.1). |
| Data | Seats, templates, grants (with delegated_by), repository binding, agent ceilings, audit entries. |
| State matrix | L: skeleton rows. E: "Only you (Founder) have a seat. Invite members in release 2." X: save error → keep form, show message, Retry. D: read-only with banner. P: grant change needing higher authority (R2 delegation) → "Requested" chip. R: n/a (saves are synchronous; show `Saving…` on button). C: toast "Grants updated" + audit link. Z: PL sees only delegated scope, no org defaults; OP has no access to this view (tab hidden; direct navigation → access message). Refused self-grant attempts by agents appear in audit list with "Refused" chip (PRD-D.11). |
| Seat visibility | F: full. PL: subset editor for own delegable grants (R2). OP: none. |
| Accessibility | Matrix table with row/column headers; `Toggle` implemented as `role="switch"`; reauth modal traps focus; every grant row has description text not just a name; changes summarised before save ("You are granting: …"). |

## §C Navigation and global surfaces

| Surface | Reference | Engine Labs R1 |
|---|---|---|
| Primary tabs (`PrimaryNavTabs`) | 8 tabs L26–35 | **Home · Work · Runs · Connections · Settings** (5) — Inbox, People, Data, Files removed from R1 (§H D-1); Memory tab added R3; People R2. Keep notched geometry, 16px icons, badge on Runs = waiting-approval count. |
| Top bar | wordmark `cc-org-dash` mono L204 | Wordmark "Engine Labs" (Inter 15/700; mono retained for ids only); rail toggle, search (⌘K), `+` create (New priority / New plan / New request / New run), bell, avatar menu (Profile, Settings, Sign out), agent toggle — unchanged positions. |
| Command rail (`GlobalCommandRail`) | Company command sections L82–242 fed by `GLOBAL_COMMAND` | Rename header "Company" ("Health · work · decisions"). Sections: **SIGNALS** → Health (n degraded) / Decisions (n) / Notifications (n); **PRIORITIES** → top ledger priorities with health dot; **PLANS & MILESTONES** (collapsible) → plans with % and milestones with dates; **BLOCKERS** → ledger blockers; **DECISIONS** (pinboard) → recent decision records. Row select opens `SlideOver` (460) with `GlobalCommandDetail` pattern whose footer becomes "Open" (deep link) / "Close". Closed rail width 54 shows an icon strip (extension; ref renders nothing when closed L60). Persist open state as ref key. |
| Assistant panel | `GlobalAgentPanel` | Per B.3. Open state persists per session; opening does not change tab; panel never blocks top bar (z 500 < 520 as ref). |
| Status bar (`PlatformStatusBar`) | random events L88–214 | Feed = audit/provenance events for the tenant (P13) and run milestones; collapsed bar shows latest event + chip; expanded = last 80 with absolute time. `SIGNAL_LABELS` mapped to EL event kinds (created/modified/deleted/connected/failed/warning/deployed(→"Released")/rotated/exported/signed_in/signed_out/info + new `approved`, `refused`, `run_started`, `run_completed`, `recovered`). Keep `aria-live` chip. Disconnected: chip "Offline" red, message "Reconnecting…". |
| Notifications (`NotifDrawer`) | local `DB.notifications` | Server notifications: run completed (PRD-E.4), approval requested/decided, connection unavailable, incident/escalation. Row click deep-links (run/item/connection). Severity dot + text label. "Mark all read" persists. Bell badge count = unread. |
| Command palette | ⌘K L134–137, L451–485 | Add arrow-key/Enter navigation, ESC handler; groups: Jump to (tabs), Work items (search), Runs, Actions (New…, Change theme, Open assistant). |
| Where run progress surfaces | — | (1) Runs tab list/detail (authoritative), (2) Home "Running work", (3) assistant run card, (4) status bar milestones, (5) notification on completion/approval. One event stream, five projections. |
| Where approvals surface | — | Home "Required decisions" (all), Runs badge + run detail pinned card, assistant inline card, notification. Approve always shows action + target + version (PRD-D.10); if target changed since request the card says "Changed — review again" and old approval is void. |
| Close vs cancel (PRD-E.4) | ref has no jobs | **Close** = closing panel, tab, window or app: never affects cloud work; on reopen, status/history stream and "Resumed" divider shows. **Cancel** = explicit red action in run detail (or assistant run card menu) with confirm; results in `cancelled` state and audit entry. App quit while runs active: macOS window-close simply hides/quits with no prompt about work; optional non-blocking toast "3 runs continue in the cloud". Never phrase close as "stop". |
| Auth (`AuthPortal`) | demo creds L254–262 | Keep layout (card 400, footer theme/language). Remove Google button and sign-up (R1 founder-only; invite-based later); add strong-factor step (PRD-D.7) as second card state; tokens to OS keychain via Tauri (PRD-D.13). Errors in plain words; no lockout detail. |

## §D Adaptive-view constraints and preview/apply/revert flow (PRD-A.11, A.12 — R3; constraints binding from R1)

Constraints (checkable):
1. A view definition is a validated declarative document (schema versioned) composed only of the trusted component set in §F (keep/adapt rows). Unknown component or failed validation → **fallback** = the fixed seat-template view; never a blank/broken region.
2. Generated views run with no filesystem, shell, database or credential access; they receive data only through the same authenticated read contracts as fixed views (PRD-D.13).
3. **Stable controls** never move or hide under adaptation: primary tabs, top bar, command rail toggle, assistant toggle, active scope pill, evidence links, approval targets/buttons, allowance/spend text, destructive actions (Cancel/Revoke/Delete) — screenshot-diff enforced (PRD-A.11 acceptance).
4. Pinning: any region has a pin control; pinned regions persist per member across adaptations and upgrades (PRD-A.10).
5. Undo reverts the last adaptation; Reset restores the seat template; both keyboard reachable (⌘Z within view, "Reset layout" in view menu).
6. Disclosure: an adapted view shows a small `Badge` "Adapted for: <intent>" with "Why?" opening a plain explanation; never shows prompts or schema.
7. Personalisation settings (inspect / disable / reset) live in Settings → Personalisation; when disabled no adaptation occurs (PRD-A.12).

Preview → apply → revert flow: trigger (explicit intent, role/task change, connection change) → system prepares candidate → **Preview** rendered in a non-interactive overlay card ("Suggested layout: … [Apply] [Not now]") — nothing changes until Apply → Apply swaps regions with reduced-motion-safe fade and records a version → toast "Layout updated · Undo" (8 s, focusable) → Undo/Reset available from view menu thereafter → failure at any step returns to fallback with message. Adaptations are compared with fixed views for completion time and errors before promotion (I-16).

## §E Accessibility and desktop window behaviour (global)

| Area | Requirement |
|---|---|
| Keyboard | Every interactive element focusable and operable; visible `:focus-visible` ring `0 0 0 3px accentBg` + 1px `accent` (matches `Input` focus L268–269); no hover-only affordances (ref uses `onMouseEnter` style mutation everywhere — replace with CSS classes providing both hover and focus). Shortcuts: ⌘K palette, ⌘J assistant toggle, ⌘\ rail toggle, ESC closes topmost overlay, `?` shows shortcut list. Tab order: top bar → tabs → rail → main → panel. |
| Focus management | Overlays (`SlideOver`, `Modal`, agent panel, notif drawer, palette) trap focus, restore focus on close, set initial focus to heading or first field. Route change moves focus to h1. |
| Semantics | Landmarks: `header`, `nav` (tabs, rail), `main`, `aside` (assistant), `footer`/status `role="status"`. Tabs `role="tablist"/tab/tabpanel`. Tables with `th scope`. Icons `aria-hidden` unless sole content (then `aria-label`). `Dot` never alone. |
| Contrast | Text ≥4.5:1, large text ≥3:1, UI components ≥3:1. Reference `t3`/`t4` fail in light theme (§A.4); rule: `t3`/`t4` allowed only for decorative or duplicated information; body/metadata text uses `t2` (`#64748b` ≈ 4.7:1 on white). Proposed light `t3` → `#6b7a90` (≈4.6:1) recorded as departure D-3 for owner acknowledgement. Dark/dimmed `t3` pass (~4.6/~4.4:1) — verify with tooling. `[SE completed 2026-09-10 → §0.6: dark t3 4.68–5.42 passes; dimmed t3 3.41–4.48 does NOT pass 4.5:1; proposed D-3 #6b7a90 = 4.36:1 on white (fails); #617083 passes on all light backgrounds.]` |
| Motion | Respect `prefers-reduced-motion`: disable slide/transform transitions (agent panel 0.32 s, slideover 0.25 s, rail 0.22 s, status bar 0.32 s), skeleton shimmer, live sparklines; keep opacity fades ≤150 ms. |
| Zoom/text | Layout survives 200% zoom and 1.5× OS text scaling without clipping; `maxWidth 1280` container reflows; min hit area 32×32 (upgrade `Btn` small). |
| Screen reader | Streaming and status via `aria-live=polite`, ≤1 announcement / 5 s per region; errors `role="alert"`. Plain-language copy (NFR-8). |
| Localisation | en-AU default (`toLocaleDateString("en-AU")` in ref L189, L220); dates via `Intl` with member timezone (Account L285); numbers/currency deterministic (PRD-E.11); no RTL in R1 (record). |
| Desktop window (Tauri 2, macOS first) | Default 1440×900; minimum 1024×700 (below 1100 wide the rail auto-collapses to 54; `useIsMobile` ≤768 layout retained but not a supported desktop size); single window R1 (no multi-window/detached panels); native title bar, menu with Edit/View/Window/Help and shortcut mirrors; window position/size persisted; system theme detection sets initial theme unless member chose one (default theme open question in charter §5 → default "system"); external links open in default browser; no embedded webviews for OAuth; offline → D-states, never crash; app quit never cancels cloud work (PRD-E.4). |

## §F Component migration map (21 files: shell + 20 components)

Legend: keep = port to TSX with typing and a11y fixes only; adapt = port and change behaviour/data per §B–§C; replace = new implementation on same primitives; drop = not in R1 (retain in reference clone, not in product). "Dep" = third-party deps the reference file imports.

| # | Reference file | Disposition | R1 target (TSX) | JSX→TSX and behavioural notes | Dep implications |
|---|---|---|---|---|---|
| 0 | `pages/cc-org-dash.jsx` | adapt | `apps/desktop/src/shell/AppShell.tsx` + `router.tsx` | Replace tab state with router (`/home`, `/work`, `/work/:id`, `/runs`, `/runs/:id`, `/connections`, `/settings/*`, `/account`); localStorage → typed preferences store (theme, rail, agent panel) persisted via API + local cache; auth stub → real session; `DB` removed; cmd palette a11y | react-router-dom keep |
| 1 | `primitives.jsx` | keep (+a11y) | `packages/ui/primitives/*.tsx` (one file per export) + `tokens.ts` | Type `Theme` from `THEMES.light` keys (`satisfies`), `ThemeKey = "light"|"dark"|"dimmed"`; `Toggle`→`role="switch"`; `SlideOver`/`Modal` → dialog semantics, focus trap, ESC; `Table` generic `<T>` with keyboard rows; `Surface` renders `button` when clickable; `Field` `htmlFor`; move hover styles to CSS modules/vanilla-extract; remove `window` read in `SlideOver` (use `useIsMobile`) | none; optionally Radix Dialog for trap (already in ref deps) |
| 2 | `icons.jsx` | keep (+add) | `packages/ui/icons/*.tsx` | Add `aria-hidden` default, `title` prop; add 10 EL icons (§A.5); or swap to `lucide-react` (in ref deps) with same names — decision for SE, record | lucide-react optional |
| 3 | `useIsMobile.jsx` | keep | `useViewport.ts` | Return `{isMobile, isNarrow(<1100)}`; `matchMedia` instead of resize listener | none |
| 4 | `data.jsx` | drop (→ labelled fixtures) | `apps/desktop/src/dev/fixtures.ts` behind `VITE_EL_DEMO_DATA`/Storybook only | Never imported by production screens (PRD-A.16); shapes in §A.6 inform contract types | none |
| 5 | `HomeScreen.jsx` | adapt | `views/home/HomeView.tsx` | Five regions per B.1; delete chart helpers (`buildSeries`, `AreaTrendChart`, `DonutChart`) or move to `dev/`; SubNav tabs re-labelled | none (charts are inline SVG) |
| 6 | `WorkScreen.jsx` | adapt | `views/work/WorkListView.tsx`, `WorkItemView.tsx`, `IssueRow.tsx`, `NewWorkItemModal.tsx` | Keep `IssueTicketRow`, grouped list, bulk bar, projects table; drop Roadmap/Kanban/Wiki in R1 (Board optional if time); detail → route | `@hello-pangea/dnd` not used by ref (HTML5 drag) — drop |
| 7 | `GlobalAgentPanel.jsx` | adapt | `shell/AssistantPanel.tsx` (+ `SessionTabs`, `MessageList`, `Composer`, `ModeChips`) | Remove params/variables blocks; replace `send()` with SSE client; session persistence; a11y per B.3 | none |
| 8 | `GlobalCommandRail.jsx` | adapt | `shell/CompanyRail.tsx` | Data from health/ledger/approvals; icon strip when collapsed; keyboard nav | none |
| 9 | `GlobalCommandDetail.jsx` | adapt | `shell/CompanyRailDetail.tsx` | Same branches mapped to EL kinds; footer "Open"/"Close" | none |
| 10 | `PlatformStatusBar.jsx` | adapt | `shell/StatusBar.tsx` | Replace generators with event subscription; keep chip system and a11y; portal OK | none (react-dom) |
| 11 | `NotifDrawer.jsx` | adapt | `shell/NotificationsDrawer.tsx` | Server data, deep links, persisted read state | none |
| 12 | `SettingsScreen.jsx` | adapt (split) | `views/settings/*` : General, Appearance (keep THEMES list), Notifications (keep toggles), Data & retention (new, PRD-F.4), Personalisation (R3), **Permissions** (B.7) | Drop AI & Agents (API key in browser — prohibited), Security API keys, Plan & Billing prices, Docs site, "Ask AI" FAB | none |
| 13 | `AccountScreen.jsx` | adapt (reduce) | `views/account/AccountView.tsx` | Keep sidebar frame + Profile (name, language, date/time format, timezone) + Login & security (factor status, sessions); drop Branding, My link, Phone, Cookies, Delete account (erasure is PRD-F.8 flow, R4) | none |
| 14 | `AuthPortal.jsx` | adapt | `auth/SignInView.tsx` | Per §C Auth row; remove demo defaults/Google/sign-up | none |
| 15 | `IntegrationsScreen.jsx` | adapt | `views/connections/ConnectionsView.tsx` (+ registry list R1, wizard R2) | Per B.5 | none |
| 16 | `DataScreen.jsx` | replace | pattern source for `views/runs/RunsListView.tsx`, `RunDetailView.tsx` | Reuse Traces table + rail pattern; drop metrics/sparkline simulation, "My apps" | none |
| 17 | `FilesScreen.jsx` | drop (R1); pattern for Memory manager (R3) and document intake list (R1 minimal: upload modal L484–520 reused for PRD-A.4 document intake in Work) | `views/memory/*` later | Hard-coded colours → tokens when reused | none |
| 18 | `InboxScreen.jsx` | drop (R2, B12) | — | Messaging connectors not in R1; canned reply L230 must not ship | none |
| 19 | `PeopleScreen.jsx` | drop (R2) — Team list pattern reused in Permissions → Seats | — | | none |
| 20 | `WorkflowVis.jsx` | drop (R3, P05 schedules/Automate) | — | Node editor not needed for R1 loop | none |

Dependency verdict for R1 desktop bundle (from `package.json` L14–75): keep `react`, `react-dom`, `react-router-dom`, `@tanstack/react-query`, `zod` (view-definition and API schema validation), `date-fns`, `clsx`; optional `@radix-ui/react-dialog`/`react-tooltip`, `lucide-react`, `cmdk` (palette a11y). **Drop**: `three`, `react-leaflet`, `react-quill`, `jspdf`, `html2canvas`, `recharts`, `framer-motion`, `@stripe/*`, `canvas-confetti`, `embla-carousel-react`, `moment`, `lodash`, `react-day-picker`, `react-hook-form`/`@hookform/resolvers` (unless forms warrant), `react-markdown` (keep only if assistant renders markdown — recommended keep for assistant replies with sanitisation), `sonner`/`react-hot-toast` (choose one for toasts), `vaul`, `input-otp` (keep if strong factor is OTP), `next-themes` (replace with THEMES store), `@hello-pangea/dnd`, remaining Radix packages not used. None of the dropped libraries is imported by any `cc-org-dash` file (verified by reading all 21 files); removal has zero effect on shell fidelity.

## §G Capture plan for the software engineer (T0-8)

Setup: clone at SHA into `.reference/orgos/`, `npm ci`, `npm run dev` (Vite default `http://localhost:5173`). Only one route exists: `http://localhost:5173/cc-org-dash` (`App.jsx` L10–15); screens are tab state, so each capture step sets state via UI or localStorage then screenshots. Seed before load to skip login: `localStorage.setItem("cc-org-dash-auth", JSON.stringify({email:"founder@example.test",name:"Founder",at:Date.now()}))`; theme: `localStorage.setItem("cc-org-dash-theme","light"|"dark"|"dimmed")`; rail: `cc-global-command-open` = "1"/"0". Disable the status-bar random ticker for stable diffs by capturing within 4 s of load or stubbing `Math.random` — record method. Use device scale 2 (macOS Retina) and also 1 for pixel diffing; PNG.

Viewports (CSS px): **V1 1440×900** (primary), **V2 1280×800**, **V3 1024×700** (min window), **V4 768×1024** (mobile boundary, `isMobile` true). Themes: light + dark for all; dimmed for shell-01 and home only.

Filename: `docs/ui-blueprint/<nn>-<surface>-<state>-<theme>-<W>x<H>@<scale>x.png`.

| nn | Surface / state | How to trigger | Viewports |
|---|---|---|---|
| 01 | auth-login | clear `cc-org-dash-auth`, load | V1, V4 |
| 02 | auth-signup | click "Sign up" | V1 |
| 03 | shell-home-rail-open | default | V1–V4 |
| 04 | shell-home-rail-closed | click rail toggle (top-left) | V1, V3 |
| 05 | home-overview-7d | default subtab | V1 |
| 06 | home-overview-90d | click "90d" | V1 |
| 07 | home-project-slideover | click first Active Project row | V1 |
| 08 | agent-panel-open | click `Bot` toggle (top-right) | V1, V4 |
| 09 | agent-panel-params-open | expand "Model & parameters" | V1 |
| 10 | agent-panel-variables-open | expand "Variables & context" | V1 |
| 11 | agent-panel-two-tabs-demo-reply | click "+", type text, Enter (shows `[Demo]` reply) | V1 |
| 12 | rail-detail-critical | click "Critical" in rail | V1 |
| 13 | rail-detail-initiative | click first initiative | V1 |
| 14 | rail-detail-blocker | click blocker row | V1 |
| 15 | notif-drawer | click bell | V1 |
| 16 | cmd-palette | press ⌘K | V1 |
| 17 | cmd-palette-no-results | type "zzz" | V1 |
| 18 | create-menu | click `+` | V1 |
| 19 | profile-menu | click avatar | V1 |
| 20 | status-bar-collapsed | default (crop bottom 60px too) | V1 |
| 21 | status-bar-expanded | click bar | V1 |
| 22 | work-projects | Work tab | V1, V3 |
| 23 | work-issues-all-selected2 | Issues subtab, tick 2 checkboxes (bulk bar) | V1 |
| 24 | work-issues-filter-review | click "Review" | V1 |
| 25 | work-issue-slideover | click an issue row | V1 |
| 26 | work-new-issue-modal | click "New issue" | V1 |
| 27 | work-board | Board subtab | V1 |
| 28 | work-roadmap | Roadmap subtab | V1 |
| 29 | work-workflows-node-selected | Workflows subtab, click a node | V1 |
| 30 | work-wiki-empty | Wiki subtab | V1 |
| 31 | inbox-default | Inbox tab | V1 |
| 32 | people-table | People tab | V1 |
| 33 | data-metrics-traces | Data tab | V1 |
| 34 | data-trace-slideover | click a trace row | V1 |
| 35 | files-list / 36 files-grid-detail | Files tab; toggle grid; click file | V1 |
| 37 | integrations-cards / 38 integrations-slideover | Integrations tab; click card | V1 |
| 39–46 | settings-general, appearance, ai, notifications, security, billing, team, docs | each settings tab | V1 |
| 47 | settings-upgrade-modal | Billing → "Upgrade plan" | V1 |
| 48 | account-profile / 49 account-login-security | avatar → "Your profile"; sidebar "Login & security" | V1 |
| 50 | mobile-rail-button | V4 with rail closed (shows rail button above content) | V4 |
| 51 | focus-visible-tab | keyboard Tab to a primary tab (documents missing focus ring) | V1 |
| 52 | reduced-motion-note | OS reduce-motion on; capture panel mid-transition or note behaviour | V1 |

Also record: computed font-family on body (expect Inter fallback since fonts are not bundled — note whether Inter is installed locally), `getComputedStyle` of `t3` text contrast via devtools for D-3, the DOM z-index stack, and a short screen recording (or frame set) of agent panel open/close and rail collapse. Capture index, trigger adaptations, computed fonts, focus order and z-index stack: see §0.4 (lead, 2026-09-10T17:15Z — all 52 states captured with headless host Chrome via `docs/ui-blueprint/capture.mjs`; dev server and browser stopped afterwards). The IDE browser tool could not reach loopback in this environment (recorded in §0.4).

## §H Departures from reference and open questions

| ID | Departure / question | Type | Rationale | Owner action |
|---|---|---|---|---|
| D-1 | Primary tab set 8 → 5 (Home, Work, Runs, Connections, Settings); Inbox/People/Data/Files deferred | structural (not aesthetic) | R1 scope (PRD-A.15 proposal, OQ-5); tabs component and geometry preserved (NFR-3) | Confirm with OQ-5 |
| D-2 | Wordmark "cc-org-dash" (JetBrains Mono) → "Engine Labs" (Inter 700) | branding | Intake: "replace prototype branding with Engine Labs" | none |
| D-3 | Light-theme `t3` `#94a3b8` → `#6b7a90` (and `t4` decorative-only) | token change (visible) | NFR-2 contrast; ref fails AA at 12–13px | Acknowledge (minor aesthetic). `[lead 2026-09-10]` SE tool-verified `#6b7a90` = 4.36:1 on white (fails AA); revised proposal `#617083` (5.06 / 4.75 / 4.59 on surface/canvas/raised) — see §0.6, F-S1 |
| D-4 | Assistant footer: remove Model & parameters / Variables & context; add Mode chips, Scope pill, allowance line | content | PRD-A.14, E.1, G.6 | none |
| D-5 | Command rail sections relabelled to Health/Priorities/Plans/Blockers/Decisions; collapsed rail shows icon strip | content + minor structure | Home requirements PRD-A.13; usability of 54px rail | none |
| D-6 | Status bar feed = real audit events; new chip kinds | content | PRD-A.16 no simulation | none |
| D-7 | New views: Runs list/detail, Permissions editor, Connections registry list; later Memory manager | documented extensions | PRD-A.15 "documented extension" clause | none |
| D-8 | Settings: remove AI & Agents (browser-stored API key), Security API keys, Billing prices, Docs site | removal | PRD-D.13, G.10; prices prohibited | none |
| D-9 | Auth: remove Google/sign-up/demo credentials; add strong factor | security | PRD-D.7, R1-ACC-1 | none |
| D-10 | Overlays gain focus trap/ESC/dialog roles; `Toggle` becomes switch; hover styles get focus equivalents | a11y | NFR-2 | none |
| D-11 | Default theme "system" (ref hard-codes light) | preference | charter §5 open question | Owner preference |
| OQ-U1 | Should "Board" (kanban) ship in R1 Work? Proposal: no (list + detail only) | scope | R1 loop does not need it | Owner/PL at phase 1 plan |
| OQ-U2 | Memory search/inspect in R1 (PRD-F.3) without a dedicated view: proposal = via assistant + work-item Evidence section; Memory manager view R3 | scope | PRD-A.15 vs F.3 timing | PL reconciliation T0-12 |
| OQ-U3 | Icons: keep inline `icons.jsx` port vs `lucide-react` | technical | identical glyphs; bundle/typing trade-off | SE: inline port in `packages/ui/src/icons.tsx` (D-07) |
| OQ-U4 | Fonts: Inter and JetBrains Mono must be bundled for offline desktop; licence inventory entry (PRD-G.9) | technical | not bundled in ref | SE: OFL licence files + system/`local()` fallback (`apps/desktop/public/fonts/`); woff2 binaries not vendored in phase 1 |

Material aesthetic departures requiring an owner ask before implementation (NFR-3): none beyond D-3 (contrast token) and D-11 (default theme), both minor and reversible.
