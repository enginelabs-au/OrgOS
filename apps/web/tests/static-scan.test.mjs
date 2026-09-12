import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");

test("product title is Papership", () => {
  const html = readFileSync(join(root, "index.html"), "utf8");
  assert.match(html, /<title>Papership<\/title>/);
});

test("canonical product route is /papership", () => {
  const app = readFileSync(join(root, "src/App.jsx"), "utf8");
  assert.match(app, /path="\/papership" element=\{<Papership/);
  assert.match(app, /path="\/cc-org-dash" element=\{<Navigate to="\/papership"/);
  assert.match(app, /path="\/" element=\{<Navigate to="\/papership"/);
});

test("localStorage keys are papership-* with legacy migrate", () => {
  const shell = readFileSync(join(root, "src/blueprint2/App.jsx"), "utf8");
  assert.match(shell, /const AUTH_KEY = "papership-auth"/);
  assert.match(shell, /const THEME_KEY = "papership-theme"/);
  assert.match(shell, /const LEGACY_AUTH_KEY = "cc-org-dash-auth"/);
  assert.match(shell, /function migrateStored/);
});

test("narrow chrome uses blueprint-2 bottom tabs", () => {
  const app = readFileSync(join(root, "src/blueprint2/App.jsx"), "utf8");
  const css = readFileSync(join(root, "src/blueprint2/blueprint2.css"), "utf8");
  assert.match(app, /className="bp2-bottom"/);
  assert.match(app, /BOTTOM_TABS = \["today", "work", "inbox"\]/);
  assert.match(css, /@media \(max-width: 767px\)/);
  assert.match(css, /\.bp2-hey \{/);
});

test("today compose has no unpublished allowance quantity", () => {
  const screens = readFileSync(join(root, "src/blueprint2/screens.jsx"), "utf8");
  const app = readFileSync(join(root, "src/blueprint2/App.jsx"), "utf8");
  assert.doesNotMatch(screens, /184640|Remaining allowance:\s*\d/);
  assert.doesNotMatch(app, /184640|Remaining allowance:\s*\d/);
  assert.match(screens, /Remaining allowance: not captured/);
  assert.match(app, /Remaining allowance: not captured/);
});

test("live API client has no OrgOS product name", () => {
  const api = readFileSync(join(root, "src/api/papership.js"), "utf8");
  assert.doesNotMatch(api, /OrgOS|orgos|cc-org/);
  assert.match(api, /papership-token/);
});
