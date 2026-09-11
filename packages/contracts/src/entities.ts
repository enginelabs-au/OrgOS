import { z } from "zod";

const Id = z.string().min(1);
const Timestamp = z.string().min(1);

export const OrganisationSchema = z.object({
  id: Id,
  tenant_id: Id,
  name: z.string().min(1),
  created_at: Timestamp,
});

export const LegalEntitySchema = z.object({
  id: Id,
  organisation_id: Id,
  name: z.string().min(1),
  created_at: Timestamp,
});

export const DepartmentSchema = z.object({
  id: Id,
  organisation_id: Id,
  name: z.string().min(1),
  created_at: Timestamp,
});

export const TeamSchema = z.object({
  id: Id,
  department_id: Id.optional(),
  organisation_id: Id,
  name: z.string().min(1),
  created_at: Timestamp,
});

export const LocationSchema = z.object({
  id: Id,
  organisation_id: Id,
  name: z.string().min(1),
  created_at: Timestamp,
});

export const ProjectSchema = z.object({
  id: Id,
  organisation_id: Id,
  name: z.string().min(1),
  status: z.string().min(1),
  created_at: Timestamp,
});

export const TaskSchema = z.object({
  id: Id,
  project_id: Id.optional(),
  organisation_id: Id,
  title: z.string().min(1),
  status: z.string().min(1),
  created_at: Timestamp,
});

export const ProviderAccountSchema = z.object({
  id: Id,
  organisation_id: Id,
  provider: z.string().min(1),
  installation_pointer: z.string().min(1),
  created_at: Timestamp,
});

export const PrincipalKindSchema = z.enum(["human", "agent"]);

export const PrincipalSchema = z.object({
  id: Id,
  tenant_id: Id,
  kind: PrincipalKindSchema,
  seat_id: Id.optional(),
  grant_version: z.number().int().nonnegative(),
  created_at: Timestamp,
});

export const SeatTemplateIdSchema = z.enum(["founder", "project_lead", "operator"]);

export const SeatTemplateSchema = z.object({
  id: SeatTemplateIdSchema,
  label: z.string().min(1),
  default_grants: z.array(z.string()),
});

export const ApprovalClassSchema = z
  .string()
  .regex(/^approval\.[a-z][a-z0-9_.]*$/, "approval class must be approval.<class>");

export const GrantClassSchema = z.union([
  z.enum([
    "org.admin",
    "ledger.read",
    "ledger.write",
    "run.start",
    "run.cancel",
    "registry.read",
    "memory.read",
    "memory.write",
    "usage.read",
    "records.read",
    "search.read",
    "aggregates.read",
    "attachments.read",
    "attachments.write",
    "notifications.read",
    "repo.branch",
    "repo.change",
    "repo.check",
    "repo.release",
    "billing.admin",
    "data.export",
    "data.erase",
    "connector.admin",
  ]),
  ApprovalClassSchema,
]);

export const GrantSchema = z.object({
  id: Id,
  principal_id: Id,
  tenant_id: Id,
  grant_class: GrantClassSchema,
  scope: z.string().min(1),
  created_at: Timestamp,
});

export const PrioritySchema = z.object({
  id: Id,
  tenant_id: Id,
  title: z.string().min(1),
  owner_principal_id: Id,
  created_at: Timestamp,
  updated_at: Timestamp,
});

export const PlanSchema = z.object({
  id: Id,
  tenant_id: Id,
  title: z.string().min(1),
  priority_id: Id.optional(),
  created_at: Timestamp,
  updated_at: Timestamp,
});

export const WorkItemSchema = z.object({
  id: Id,
  tenant_id: Id,
  title: z.string().min(1),
  plan_id: Id.optional(),
  stage: z.string().min(1),
  stage_changed_at: Timestamp,
  created_at: Timestamp,
  updated_at: Timestamp,
});

export const AssignmentSchema = z.object({
  id: Id,
  tenant_id: Id,
  work_item_id: Id,
  principal_id: Id,
  created_at: Timestamp,
});

export const DependencySchema = z.object({
  id: Id,
  tenant_id: Id,
  from_work_item_id: Id,
  to_work_item_id: Id,
  created_at: Timestamp,
});

export const SourceReferenceSchema = z.object({
  id: Id,
  tenant_id: Id,
  work_item_id: Id.optional(),
  provider: z.string().min(1),
  installation_pointer: z.string().min(1),
  created_at: Timestamp,
});

export const JobStatusSchema = z.enum([
  "queued",
  "running",
  "cancelled",
  "completed",
  "failed",
]);

export const JobSchema = z.object({
  id: Id,
  tenant_id: Id,
  status: JobStatusSchema,
  purpose: z.string().min(1),
  created_at: Timestamp,
  updated_at: Timestamp,
});

export const JobEventSchema = z.object({
  id: z.number().int().positive(),
  job_id: Id,
  tenant_id: Id,
  type: z.string().min(1),
  payload: z.record(z.unknown()),
  created_at: Timestamp,
});

/** Nine PRD-E.2 fields — all required. Phase 1 model_configuration is "none". */
export const RunSchema = z.object({
  id: Id,
  job_id: Id,
  tenant_id: Id,
  sponsor: Id,
  acting_identity: Id,
  purpose: z.string().min(1),
  scope: z.string().min(1),
  policy_version: z.string().min(1),
  model_configuration: z.literal("none"),
  budget: z.string().min(1),
  deadline: Timestamp,
  accountable_owner: Id,
  created_at: Timestamp,
});

export const ReceiptSchema = z.object({
  id: Id,
  job_id: Id,
  tenant_id: Id,
  step_name: z.string().min(1),
  idempotency_key: z.string().min(1),
  created_at: Timestamp,
});

export const AuditRecordSchema = z.object({
  id: Id,
  tenant_id: Id,
  actor_principal_id: Id,
  action: z.string().min(1),
  target_type: z.string().min(1),
  target_id: z.string().min(1),
  created_at: Timestamp,
});

export const EntitlementSchema = z.object({
  id: Id,
  tenant_id: Id,
  principal_id: Id,
  feature: z.string().min(1),
  created_at: Timestamp,
});

export const ENTITY_SCHEMAS = {
  organisation: OrganisationSchema,
  legal_entity: LegalEntitySchema,
  department: DepartmentSchema,
  team: TeamSchema,
  location: LocationSchema,
  project: ProjectSchema,
  task: TaskSchema,
  provider_account: ProviderAccountSchema,
  principal: PrincipalSchema,
  seat_template: SeatTemplateSchema,
  grant: GrantSchema,
  priority: PrioritySchema,
  plan: PlanSchema,
  work_item: WorkItemSchema,
  assignment: AssignmentSchema,
  dependency: DependencySchema,
  source_reference: SourceReferenceSchema,
  job: JobSchema,
  job_event: JobEventSchema,
  run: RunSchema,
  receipt: ReceiptSchema,
  audit_record: AuditRecordSchema,
} as const;
