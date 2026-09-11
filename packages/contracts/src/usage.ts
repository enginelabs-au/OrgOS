import { z } from "zod";

/**
 * UsageEvent — Growth handoff §5.4.2–5.4.4.
 * Feature flag: emit is off (`ENGINE_USAGE_EMIT` default 0). Schema exists; no production emit.
 */

export const USAGE_EMIT_FEATURE_FLAG = {
  name: "ENGINE_USAGE_EMIT",
  default: 0,
  note: "emit is off until Security schema review (F-G1 / F-SEC-16 / GM-11)",
} as const;

export const PROHIBITED_USAGE_FIELDS = [
  "prompt",
  "message",
  "email",
  "content",
  "url",
  "path",
  "credential",
  "token",
  "name",
] as const;

export const UsageModeSchema = z.enum([
  "Ask",
  "Analyse",
  "Plan",
  "Draft",
  "Execute",
  "Review",
  "Automate",
]);

export const ModelBandSchema = z.enum(["none", "small", "medium", "large"]);

export const EstimatedCostBandSchema = z.enum(["unknown", "low", "medium", "high"]);

export const OutcomeCodeSchema = z.enum([
  "success",
  "failure",
  "cancelled",
  "refused",
  "results_found",
  "none",
]);

export const SeatTemplateUsageSchema = z.enum(["founder", "project_lead", "operator"]);

export const InterventionReasonSchema = z.enum([
  "approval_required",
  "correction",
  "clarification",
  "recovery_escalation",
  "permission_missing",
  "other",
]);

export const RecoveryKindSchema = z.enum([
  "transient_retry",
  "diagnostic_attempt",
  "escalation",
]);

const requiredUsage = {
  event_name: z.string().regex(/^[a-z]+\.[a-z0-9_]+\.[a-z0-9_]+$/),
  event_id: z.string().uuid(),
  occurred_at: z.string().min(1),
  tenant_id: z.string().min(1),
  member_pseudonymous_id: z.string().min(1),
  run_id: z.string().min(1).nullable(),
  mode: UsageModeSchema.nullable(),
  model_band: ModelBandSchema.nullable(),
  tokens_input: z.number().int().nonnegative().nullable(),
  tokens_output: z.number().int().nonnegative().nullable(),
  tokens_cached: z.number().int().nonnegative().nullable(),
  tool_call_counts_by_class: z.record(z.string(), z.number().int().nonnegative()),
  duration_ms: z.number().int().nonnegative().nullable(),
  estimated_cost_band: EstimatedCostBandSchema.nullable(),
  outcome_code: OutcomeCodeSchema,
  schema_version: z.string().min(1),
};

const extensionUsage = {
  work_item_id: z.string().min(1).optional(),
  stage_id: z.string().min(1).optional(),
  view_id: z.string().min(1).optional(),
  approval_class: z.string().min(1).optional(),
  tool_class: z.string().min(1).optional(),
  seat_template: SeatTemplateUsageSchema.optional(),
  provider_event_id: z.string().min(1).optional(),
  intervention_reason: InterventionReasonSchema.optional(),
  recovery_kind: RecoveryKindSchema.optional(),
  handoff_target: z.string().min(1).optional(),
  adaptation_version: z.number().int().nonnegative().optional(),
};

const UsageEventShape = z.object({ ...requiredUsage, ...extensionUsage }).strict();

function collectProhibitedKeys(value: unknown, prefix = ""): string[] {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    return [];
  }
  const found: string[] = [];
  for (const [key, child] of Object.entries(value as Record<string, unknown>)) {
    const path = prefix ? `${prefix}.${key}` : key;
    const lower = key.toLowerCase();
    if ((PROHIBITED_USAGE_FIELDS as readonly string[]).includes(lower)) {
      found.push(path);
    }
    found.push(...collectProhibitedKeys(child, path));
  }
  return found;
}

export function parseUsageEvent(input: unknown) {
  if (input !== null && typeof input === "object") {
    const prohibited = collectProhibitedKeys(input);
    if (prohibited.length > 0) {
      throw new z.ZodError([
        {
          code: z.ZodIssueCode.custom,
          path: prohibited[0].split("."),
          message: `prohibited UsageEvent field: ${prohibited.join(", ")}`,
        },
      ]);
    }
  }
  return UsageEventShape.parse(input);
}

export const UsageEventSchema = z.any().superRefine((value, ctx) => {
  try {
    parseUsageEvent(value);
  } catch (error) {
    if (error instanceof z.ZodError) {
      for (const issue of error.issues) {
        ctx.addIssue(issue);
      }
      return;
    }
    ctx.addIssue({ code: z.ZodIssueCode.custom, message: String(error) });
  }
});

export type UsageEvent = z.infer<typeof UsageEventShape>;
