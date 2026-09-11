import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const src = readFileSync(join(dirname(fileURLToPath(import.meta.url)), "../src/primitives.tsx"), "utf8");

test("Toggle is a switch", () => {
  assert.match(src, /role="switch"/);
  assert.match(src, /aria-checked/);
});

test("overlays use dialog role, focus trap, and Escape", () => {
  assert.match(src, /role="dialog"/);
  assert.match(src, /aria-modal="true"/);
  assert.match(src, /useFocusTrap/);
  assert.match(src, /useEscape/);
});

test("closed overlays are not rendered (F-S7 tab order)", () => {
  assert.match(src, /if \(!open\) return null/);
});

test("hover styles have focus equivalents", () => {
  assert.match(src, /mergeFocusHover/);
  assert.match(src, /onFocus/);
});

test("clickable Surface is a button", () => {
  assert.match(src, /if \(onClick\) \{/);
  assert.match(src, /<button/);
});
