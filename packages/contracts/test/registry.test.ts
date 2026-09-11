import assert from "node:assert/strict";
import { test } from "node:test";
import {
  REGISTRY_STATUS_VOCABULARY,
  RegistryRowSchema,
  RegistryStatusSchema,
} from "../src/registry.ts";

const sample = {
  domain_id: "B06",
  capability_id: "B06.01",
  user_outcome: "Founder creates plans",
  owner: "native",
  read_actions: ["list_plans"],
  write_actions: ["create_plan"],
  data_authority: "native",
  required_grants: ["ledger.read", "ledger.write"],
  dependencies: ["P02.01"],
  interface_components: ["Work"],
  release_phase: "07 / R1",
  implementation_status: "planned",
  acceptance_evidence: "n/a — planned row",
  registry_version: "0.1.0-phase0",
  status_changed_at: "2026-09-10T16:45:06Z",
  status_evidence: "EV-S10",
  hermes_side_effecting_tool: false,
};

test("D-02 status vocabulary is exactly four values", () => {
  assert.deepEqual(REGISTRY_STATUS_VOCABULARY, [
    "planned",
    "configured",
    "working",
    "unavailable",
  ]);
  assert.equal(RegistryStatusSchema.safeParse("beta").success, false);
});

test("registry row schema accepts a D-02 row", () => {
  const parsed = RegistryRowSchema.parse(sample);
  assert.equal(parsed.capability_id, "B06.01");
  assert.equal(parsed.implementation_status, "planned");
});

test("registry row rejects unknown status and unknown capability id", () => {
  assert.equal(
    RegistryRowSchema.safeParse({ ...sample, implementation_status: "deprecated" }).success,
    false,
  );
  assert.equal(
    RegistryRowSchema.safeParse({ ...sample, capability_id: "Z99.01" }).success,
    false,
  );
});
