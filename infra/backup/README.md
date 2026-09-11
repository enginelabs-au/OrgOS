# Backup inventory (phase 1 draft)

Nightly encrypted backups are designed in `docs/architecture.md` §11. This directory holds the restore procedure draft. No backup secrets belong here.

- Retention (design): conversations 365 days; logs 30 days; backups 30 days rotating.
- Execution of backups and a dry run are phase 3 / release 4.
- See `RESTORE.md`.
