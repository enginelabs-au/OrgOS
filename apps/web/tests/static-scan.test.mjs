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
