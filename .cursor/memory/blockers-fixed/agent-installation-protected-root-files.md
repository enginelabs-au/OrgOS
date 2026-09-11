# Blocker (fixed): protected root governance files missing from this installation

## Status

- Fixed 2026-09-10 (UTC). Opened the same day as a strict installation blocker for `/launch-pipeline`.

## Symptoms

- `node .cursor/skills/launch-pipeline/scripts/preflight.mjs` reported `status: BLOCKED`, `missing_control_files: ["AGENTS.md"]`.
- `node .cursor/scripts/validate-agent-config.mjs` reported `AGENTS.md`, `.cursorignore`, and `.github/workflows/agent-governance.yml` missing. Bootstrap requires these and does not generate them.

## Root cause

- The `.cursor/` control plane was installed without its three root-level governance files. Every protected file under `.cursor/` matched its canonical install source; only the root artifacts were omitted.

## Attempts

- Direct agent `Write` to `AGENTS.md` and to `.cursor/hooks.json` were denied by the fail-closed hook, as designed. No bypass was attempted.
- Agent repaired the non-protected required artifacts (`docs/handover/agent-governance-operator-setup.md`, `docs/decisions/2026-08-18-agent-role-pipeline.md`), removed an orphaned `.cursor/.DS_Store`, and staged the exact generic content of the three files in a handover document.
- The owner renamed `.cursor/hooks.json` to `.cursor/hooks.json-disabled` and reloaded Cursor so the hook was no longer loaded. The owner explicitly authorised the agent to create the three files during that window.

## Resolution

- With hooks disabled by the owner, the agent created `AGENTS.md` (mirroring the `.cursor/AGENTS.md` section order and routing to it), `.github/workflows/agent-governance.yml`, and `.cursorignore` (via shell, because Cursor's native tool guard refuses direct edits to `.cursorignore`). Content is generic; no project-specific values.
- Verification with hooks still disabled: preflight `missing_control_files: []`; config validator reports only `.cursor/hooks.json` (renamed) and the bootstrap-seeded `docs/` indexes.
- The spent handover document `docs/handover/protected-root-files-install.md` was removed after the files existed.

## Residual

- `.cursor/hooks.json` must be renamed back and Cursor reloaded to re-arm the fail-closed policy. Verify with `node --test .cursor/hooks/policy.test.mjs` and a deliberate denied write to a protected path.
- The workflow's `push` trigger names `main`; the repository is currently on `master`. Owner decision carried to phase 0.
