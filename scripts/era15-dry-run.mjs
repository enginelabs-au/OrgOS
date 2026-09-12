#!/usr/bin/env node
/**
 * ERA-15 list-only dry-run. Never destroys a Droplet, volume, or Compose unit.
 * Do not pass DIGITALOCEAN_API_TOKEN into this script.
 */
import { existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const compose = join(root, "infra/compose/docker-compose.yml");

const report = {
  mode: "DRY RUN — no destroy",
  checked_at: new Date().toISOString(),
  compose_file: existsSync(compose) ? "infra/compose/docker-compose.yml" : "missing",
  compose_services: ["proxy", "api", "worker", "postgres", "auth-stub"],
  compose_volumes_named: ["pgdata", "api-store"],
  documented_host:
    "hermes-droplet-campbell (Hermes only; no Papership API on that host as of 2026-09-12)",
  backup_names: ["BACKUP_TARGET_URL", "BACKUP_ENCRYPTION_KEY_PATH"],
  owner_destroy_later: [
    "Confirm a deletion receipt exists.",
    "Destroy the Droplet and attached volumes only from the DigitalOcean dashboard or an owner-controlled script.",
    "Verify volume deletion with the provider (ERA-15 / A-4).",
    "This script must stay list-only.",
  ],
};

process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
if (!existsSync(compose)) process.exit(1);
