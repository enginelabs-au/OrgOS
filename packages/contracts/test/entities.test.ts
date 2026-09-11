import assert from "node:assert/strict";
import { test } from "node:test";
import { EVENT_CATALOGUE } from "../src/events/catalogue.ts";
import {
  ApprovalClassSchema,
  ENTITY_SCHEMAS,
  GrantSchema,
  PrincipalSchema,
  RunSchema,
} from "../src/entities.ts";

test("entity schemas cover the phase-1 contract set", () => {
  const expected = [
    "organisation",
    "legal_entity",
    "department",
    "team",
    "location",
    "project",
    "task",
    "provider_account",
    "principal",
    "seat_template",
    "grant",
    "priority",
    "plan",
    "work_item",
    "assignment",
    "dependency",
    "source_reference",
    "job",
    "job_event",
    "run",
    "receipt",
    "audit_record",
  ];
  assert.deepEqual(Object.keys(ENTITY_SCHEMAS), expected);
});

test("run requires the nine PRD-E.2 fields and model_configuration none", () => {
  const run = RunSchema.parse({
    id: "run-1",
    job_id: "job-1",
    tenant_id: "t1",
    sponsor: "founder",
    acting_identity: "founder",
    purpose: "dev step",
    scope: "tenant",
    policy_version: "1",
    model_configuration: "none",
    budget: "none",
    deadline: "2026-09-12T00:00:00Z",
    accountable_owner: "founder",
    created_at: "2026-09-11T00:00:00Z",
  });
  assert.equal(run.model_configuration, "none");
  assert.equal(RunSchema.safeParse({ ...run, model_configuration: "gpt" }).success, false);
});

test("approval.<class> grant class is accepted; agent kind is distinct", () => {
  assert.equal(ApprovalClassSchema.safeParse("approval.release").success, true);
  assert.equal(ApprovalClassSchema.safeParse("release").success, false);
  const grant = GrantSchema.parse({
    id: "g1",
    principal_id: "p1",
    tenant_id: "t1",
    grant_class: "approval.erasure",
    scope: "org",
    created_at: "2026-09-11T00:00:00Z",
  });
  assert.equal(grant.grant_class, "approval.erasure");
  assert.equal(
    PrincipalSchema.parse({
      id: "a1",
      tenant_id: "t1",
      kind: "agent",
      grant_version: 0,
      created_at: "2026-09-11T00:00:00Z",
    }).kind,
    "agent",
  );
});

test("event catalogue uses domain.object.action", () => {
  assert.ok(EVENT_CATALOGUE.length > 20);
  for (const event of EVENT_CATALOGUE) {
    assert.match(event.name, /^[a-z]+\.[a-z0-9_]+\.[a-z0-9_]+$/);
    assert.equal(`${event.domain}.${event.object}.${event.action}`, event.name);
  }
});
