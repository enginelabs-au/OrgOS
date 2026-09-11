/**
 * UsageEvent identifier/enum field names (Growth §5.4.2 required set).
 * Settings → Data disclosure is generated from this list only.
 * Extension fields are omitted until Security schema review (F-G1).
 */
export const USAGE_EVENT_FIELDS = [
  "event_name",
  "event_id",
  "occurred_at",
  "tenant_id",
  "member_pseudonymous_id",
  "run_id",
  "mode",
  "model_band",
  "tokens_input",
  "tokens_output",
  "tokens_cached",
  "tool_call_counts_by_class",
  "duration_ms",
  "estimated_cost_band",
  "outcome_code",
  "schema_version",
] as const;

export type UsageEventField = (typeof USAGE_EVENT_FIELDS)[number];

export const RETENTION_DEFAULTS = [
  { id: "conversations", label: "Conversations", period: "365 days" },
  { id: "logs", label: "Logs", period: "30 days" },
  { id: "backups", label: "Backups", period: "30 days" },
  { id: "knowledge", label: "Approved knowledge", period: "until superseded" },
] as const;
