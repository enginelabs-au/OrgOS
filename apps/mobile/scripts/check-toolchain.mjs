#!/usr/bin/env node
import { execSync } from "node:child_process";
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");

function probe(command) {
  try {
    const text = execSync(command, { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim();
    return { ok: true, text: text.split("\n")[0] };
  } catch {
    return { ok: false, text: "not found" };
  }
}

const rustc = probe("rustc --version");
const cargo = probe("cargo --version");
const xcode = probe("xcodebuild -version");
const adb = probe("adb version");
const tauri = probe("npx --yes @tauri-apps/cli --version");

const report = {
  checked_at: new Date().toISOString(),
  wrap: "apps/web blueprint-2 via Tauri 2 mobile (Capacitor fallback not activated)",
  api: "same Papership cloud API; tokens belong in OS keychain/keystore",
  oauth: "system browser only",
  store_submission: "not in G11 scope",
  rustc,
  cargo,
  xcode,
  adb,
  tauri_cli: tauri,
  ios_ready: rustc.ok && xcode.ok,
  android_ready: rustc.ok && adb.ok,
  residual: rustc.ok && (xcode.ok || adb.ok)
    ? "toolchain present; simulator launch is owner/local"
    : "Tauri mobile / Xcode / Android SDK not fully present on this host. Shell config is recorded; store binaries are not claimed.",
};

writeFileSync(join(root, "toolchain-report.json"), `${JSON.stringify(report, null, 2)}\n`);
console.log(JSON.stringify(report, null, 2));
process.exit(0);
