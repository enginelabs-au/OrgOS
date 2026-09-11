import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { test } from "node:test";
import { CAPABILITY_IDS, CAPABILITY_ID_COUNT } from "../src/capabilities.ts";

const repoRoot = join(dirname(fileURLToPath(import.meta.url)), "../../..");

test("capability id list has 43 entries B01.01–B24.01 and P01.01–P19.01", () => {
  assert.equal(CAPABILITY_IDS.length, 43);
  assert.equal(CAPABILITY_ID_COUNT, 43);
  const expected = [
    ...Array.from({ length: 24 }, (_, i) => `B${String(i + 1).padStart(2, "0")}.01`),
    ...Array.from({ length: 19 }, (_, i) => `P${String(i + 1).padStart(2, "0")}.01`),
  ];
  assert.deepEqual([...CAPABILITY_IDS], expected);
});

test("capability ids match docs/capabilities.md", () => {
  const markdown = readFileSync(join(repoRoot, "docs/capabilities.md"), "utf8");
  const fromDoc = [...markdown.matchAll(/^\| (?:B|P)\d{2} \| ((?:B|P)\d{2}\.\d{2}) \|/gm)].map(
    (match) => match[1],
  );
  assert.equal(fromDoc.length, 43);
  assert.deepEqual(fromDoc, [...CAPABILITY_IDS]);
});
