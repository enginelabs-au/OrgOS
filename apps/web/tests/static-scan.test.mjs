import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");

test("product title is OrgOS and fonts are not loaded from Google", () => {
  const html = readFileSync(join(root, "index.html"), "utf8");
  assert.match(html, /<title>OrgOS<\/title>/);
  assert.doesNotMatch(html, /fonts\.googleapis|fonts\.gstatic/);
});
