# Decision D-06: Release-1 desktop primary tabs and styling token source

## Status

`accepted` — owner-directed H-6 ratification 2026-09-11. Record: `docs/decisions/2026-09-11-owner-ratification-h6.md`.

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md`.

## Context

The Papership `/cc-org-dash` reference (pinned `8a843bd6429faf1ace5a9eb6dcfb7440703d34c4`) has eight primary tabs (Dashboard, Work, Inbox, People, Data, Files, Integrations, Settings, plus a hidden `account` tab) and styles every shell component inline from a `THEMES` object with `light`/`dark`/`dimmed` variants of 40 keys each. SE verification found 0 `className` usages and 0 CSS-variable reads in any shell file; only `react`/`react-dom` are imported (EV-S07). The intake requires the desktop to preserve the Papership design language while the R1 scope (D-05) covers only the development loop, so the tab set must match what is actually available and honest (`unavailable` rows visible, no simulated controls — AUTH-28).

## Decision

1. **Primary tab set for R1: Home, Work, Runs, Connections, Settings** (8 → 5). Inbox, People, Data and Files are deferred with their release buckets and are not shown as tabs in R1; the `PrimaryNavTabs` component and its geometry are preserved (NFR-3). `Connections` hosts the registry view with `planned`/`unavailable` rows visible (PRD-C.5) even though connection setup (B.5) is built in R2.
2. **`THEMES` is the single styling token source.** The three themes are ported to `packages/ui/tokens.ts` as typed objects (`Theme` from `THEMES.light` keys; `ThemeKey = "light" | "dark" | "dimmed"`); components consume tokens through the theme context. CSS custom properties MAY be emitted from `THEMES` for `body`, scrollbars and focus ring only.
3. **Tailwind is not required for the R1 shell** and is not added to `packages/ui` or `apps/desktop`; the reference `index.css`/shadcn layer is not ported. Hover and state styles move to CSS modules (or an equivalent zero-runtime approach) rather than inline handlers.
4. **Token corrections are made in the port, not in the reference:** light `t3` moves from `#94a3b8` (2.56:1) to `#617083` (5.06:1 on `#ffffff`; passes WCAG AA — SE EV-S08 supersedes the UI/UX D-3 proposal `#6b7a90` at 4.36:1); `t4` is reviewed for the same reason; hard-coded neutrals in `FilesScreen` are irrelevant to R1 (deferred tab). Default theme remains `light` pending D-11 acknowledgement; no system-preference detection in R1.
5. **Reference patterns excluded from the port** (AUTH-27): localStorage session `cc-org-dash-auth`, browser-stored provider keys, Security-tab API keys, plan prices, demo credentials, Google sign-in, "Ask AI" FAB.

## Alternatives considered

1. **Keep all eight tabs with disabled/placeholder screens.** Rejected: placeholder screens are simulated capability (AUTH-28; I-04) and contradict the registry-based `unavailable` presentation.
2. **Adopt Tailwind + shadcn from the reference `src/components/ui`.** Rejected: the shell does not use them (EV-S07); adding them would import the 24-advisory dependency tree the port is meant to prune (D-01 alternative 2; LIC-13).
3. **CSS variables as the primary token source, generated from `THEMES`.** Deferred: typed `THEMES` keeps parity with the reference and NFR-3 fidelity checks; variables are allowed as a derived layer only.
4. **Keep `t3 #94a3b8` for fidelity.** Rejected: fails WCAG AA for text; NFR-3 fidelity is structural/visual language, not a licence to ship inaccessible contrast.

## Consequences

- Positive: honest navigation matching D-05 scope; one token source keeps the three themes consistent and testable; smaller bundle with no styling framework.
- Negative / costs: five-tab layout departs from the reference captures (`docs/ui-blueprint/` 122 PNGs) and must be documented as a departure in `docs/blueprints/ui-blueprint.md` §H; CSS-module migration of hover styles is phase-1 work.
- Follow-ups: OQ-5 confirmation; D-3/D-11 acknowledgement; F-S7 (closed assistant panel remains in tab order) fixed in the port; phase-16 re-capture targets the Engine Labs shell, not the reference.

## Evidence and citations

- `docs/blueprints/ui-blueprint.md` §A.4 (primitives, THEMES 40 keys), §C (tabs table L190; theme default L192), §E/§F (styling model; dependency verdict; `packages/ui` targets), §H D-1 (tab set 8 → 5), D-3 (contrast token, `[lead 2026-09-10]` annotation), D-8/D-10/D-11.
- UI/UX handoff `docs/workstreams/20260910-engine-labs-company-os/ui-ux-developer-subagent/handoff.md` §13 (D-06 candidate), §12 (OQ-5, D-3, D-11).
- SE evidence `docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/evidence.md` EV-S07 (0 `className`, imports), EV-S08 (contrast ratios), EV-S16 (captures).
- `docs/policies/authority-model.md` AUTH-26, AUTH-27, AUTH-28.
- `docs/decisions/2026-09-10-monorepo-layout.md` (D-01) `packages/ui` member.
