# Decision D-13: Papership prism brand (provisional)

## Status

`accepted` — owner-directed 2026-09-11. May be revised later.

## Decision

1. The product mark is the low-poly prism head on the fractured-purple rounded square. Canonical file is `brand/papership-icon.png`. Only pixels *outside* that plate are transparent. An 8px-inset iOS squircle then cuts leftover red/maroon rim pixels (boat reds are interior and stay). The purple plate is part of the icon. The 2026-09-12 owner render supersedes every earlier `orgos-icon.png`. Web/desktop/PWA/Android/iOS/Tauri slots are generated from that master by `scripts/generate-papership-icons.py`.
2. **Primary:** blue (`#2563eb` / `#3b82f6`) for most chrome, buttons, links, and selected states.
3. **Accents:** rainbow prism (blue → cyan → green → amber → pink → violet) on Hey Engine and similar highlights only.
4. **Secondary:** fractured purple (`#6d28d9` light / deep `#16082e` dark) for nav, page field, and secondary surfaces.
5. D-06 text contrast still applies. `light.t3` stays `#617083`.
