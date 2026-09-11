# Restore procedure (draft)

Status: draft for phase 1. A dry run is planned for phase 3; a full drill is release 4.

Do not put secret values in this file.

## Preconditions

1. Isolated environment (not the live Droplet).
2. Backup archive + checksum + manifest (schema version, image digests from `infra/digests.lock`).
3. Owner-held encryption key available on the restore host (`BACKUP_ENCRYPTION_KEY_PATH` — name only).
4. Target Compose stack down.

## Steps

1. Provision isolated Compose (`edge` / `app` / `data` / `worker`) from this repository.
2. Decrypt the archive off-host or in memory; never write the key beside the archive.
3. Restore Postgres (`pg_restore --format=custom`) into the application database and the DBOS system database.
4. Restore the Storage volume consistently with the dump timestamp.
5. Verify checksums, role inventory (`engine_app` is not superuser), and RLS still enabled.
6. Reconcile external systems (GitHub state, pending receipts). Hermes is not configured in phase 1.
7. Only then resume automation.

## Erasure interaction

Erasure receipts must disclose pending backup copies and their expiry.
