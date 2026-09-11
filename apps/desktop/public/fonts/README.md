# Fonts (OQ-U4 / D-07)

This folder holds **licence files only** for Inter and JetBrains Mono (SIL Open Font License 1.1).

WOFF2 binaries are **not** vendored in this commit. Do **not** fetch them from Google Fonts or any `fonts.googleapis.com` / `fonts.gstatic.com` URL (`index.html` has no external font links).

Until binaries are added here by an owner-approved vendor step:

- `local.css` uses `local("Inter")` / `local("JetBrains Mono")` plus the system stack already defined in `@engine-labs/ui` tokens (`F.sans`, `F.mono`).
- If the named fonts are not installed on the machine, the OS UI and monospace fallbacks apply.

Licence files:

- `OFL-Inter.txt` — Inter Project Authors
- `OFL-JetBrainsMono.txt` — JetBrains Mono Project Authors
