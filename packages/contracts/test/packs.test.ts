import assert from "node:assert/strict";
import { test } from "node:test";
import { FIXTURE_PACK_ID, PACK_KINDS } from "../src/packs.ts";

test("pack contract is declarative-first", () => {
  assert.equal(FIXTURE_PACK_ID, "education-demo");
  assert.deepEqual([...PACK_KINDS], ["declarative", "executable"]);
});
