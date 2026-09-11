import assert from "node:assert/strict";
import { test } from "node:test";
import {
  PROHIBITED_USAGE_FIELDS,
  USAGE_EMIT_FEATURE_FLAG,
  parseUsageEvent,
} from "../src/usage.ts";

const valid = {
  event_name: "work.item.created",
  event_id: "11111111-1111-4111-8111-111111111111",
  occurred_at: "2026-09-11T04:00:00Z",
  tenant_id: "tenant-1",
  member_pseudonymous_id: "member-pseudo-1",
  run_id: null,
  mode: null,
  model_band: null,
  tokens_input: null,
  tokens_output: null,
  tokens_cached: null,
  tool_call_counts_by_class: {},
  duration_ms: null,
  estimated_cost_band: null,
  outcome_code: "success",
  schema_version: "1",
};

test("valid UsageEvent parses; emit flag defaults off", () => {
  const parsed = parseUsageEvent(valid);
  assert.equal(parsed.event_name, "work.item.created");
  assert.equal(USAGE_EMIT_FEATURE_FLAG.default, 0);
  assert.match(USAGE_EMIT_FEATURE_FLAG.note, /emit is off/i);
});

test("extension fields are optional", () => {
  const parsed = parseUsageEvent({
    ...valid,
    work_item_id: "wi-1",
    view_id: "work",
    seat_template: "founder",
  });
  assert.equal(parsed.work_item_id, "wi-1");
});

test("prohibited UsageEvent fields fail validation", () => {
  for (const field of PROHIBITED_USAGE_FIELDS) {
    assert.throws(
      () => parseUsageEvent({ ...valid, [field]: "forbidden-value" }),
      /prohibited UsageEvent field/,
    );
  }
});

test("required UsageEvent fields are enforced", () => {
  const { event_name: _, ...missing } = valid;
  assert.throws(() => parseUsageEvent(missing));
});
