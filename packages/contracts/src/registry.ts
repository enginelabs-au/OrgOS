import { z } from "zod";
import { CAPABILITY_IDS } from "./capabilities.ts";

/** D-02 status vocabulary — exactly four values. */
export const RegistryStatusSchema = z.enum([
  "planned",
  "configured",
  "working",
  "unavailable",
]);

export const DomainIdSchema = z.string().regex(/^(B|P)(0[1-9]|1[0-9]|2[0-4])$/);

export const CapabilityIdSchema = z.enum(CAPABILITY_IDS);

export const RegistryOwnerSchema = z
  .string()
  .min(1)
  .refine(
    (value) => value === "native" || value.startsWith("native") || value.startsWith("connector:"),
    { message: "owner must be native or connector:<provider>" },
  );

export const DataAuthoritySchema = z
  .string()
  .min(1)
  .refine(
    (value) =>
      value === "native" ||
      value.startsWith("native") ||
      value.startsWith("source:") ||
      value.startsWith("shared"),
    { message: "data_authority must be native, source:<system>, or shared" },
  );

/** D-02 registry row schema (docs/product.md §3.1). */
export const RegistryRowSchema = z.object({
  domain_id: DomainIdSchema,
  capability_id: CapabilityIdSchema,
  user_outcome: z.string().min(1),
  owner: RegistryOwnerSchema,
  read_actions: z.array(z.string()),
  write_actions: z.array(z.string()),
  data_authority: DataAuthoritySchema,
  required_grants: z.array(z.string()),
  dependencies: z.array(z.string()),
  interface_components: z.array(z.string()),
  release_phase: z.string().min(1),
  implementation_status: RegistryStatusSchema,
  acceptance_evidence: z.string().min(1),
  registry_version: z.string().min(1),
  status_changed_at: z.string().min(1),
  status_evidence: z.string().min(1),
  hermes_side_effecting_tool: z.boolean().default(false),
});

export type RegistryRow = z.infer<typeof RegistryRowSchema>;
export type RegistryStatus = z.infer<typeof RegistryStatusSchema>;

export const REGISTRY_STATUS_VOCABULARY = RegistryStatusSchema.options;
