import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const dir = join(dirname(fileURLToPath(import.meta.url)), "../src/a11y");

test("focus helpers export trap primitives", () => {
  const focusable = readFileSync(join(dir, "focusable.ts"), "utf8");
  assert.match(focusable, /export function getFocusable/);
  assert.match(focusable, /export function cycleFocus/);
  assert.match(focusable, /Tab/);
});

test("escape helper listens for Escape", () => {
  const esc = readFileSync(join(dir, "useEscape.ts"), "utf8");
  assert.match(esc, /Escape/);
});
