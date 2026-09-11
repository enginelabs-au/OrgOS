import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const tokens = readFileSync(join(root, "src/tokens.ts"), "utf8");
const pkg = JSON.parse(readFileSync(join(root, "package.json"), "utf8"));

test("package name and licence", () => {
  assert.equal(pkg.name, "@engine-labs/ui");
  assert.equal(pkg.license, "SEE LICENSE IN LICENSE");
});

test("no tailwind dependency", () => {
  const deps = { ...pkg.dependencies, ...pkg.devDependencies, ...pkg.peerDependencies };
  for (const name of Object.keys(deps || {})) {
    assert.equal(name.includes("tailwind"), false, name);
  }
});

test("decision D-06 accepted marker and light.t3", () => {
  assert.match(tokens, /decision:\s*D-06 accepted/);
  assert.match(tokens, /t3:\s*"#617083"/);
  assert.match(tokens, /TOKEN_DECISION = "D-06 accepted"/);
  assert.match(tokens, /Decorative only/);
});
