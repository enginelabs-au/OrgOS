export const PACK_KINDS = ["declarative", "executable"] as const;
export type PackKind = (typeof PACK_KINDS)[number];

export const PACK_TRUST_VERDICTS = ["none", "pending", "accepted", "refused"] as const;
export type PackTrustVerdict = (typeof PACK_TRUST_VERDICTS)[number];

export type PackManifest = {
  id: string;
  version: string;
  kind: PackKind;
  domain_ids: string[];
  label: string;
  description: string;
  grants_declared: string[];
  custom_fields: Array<{ id: string; type: string; required: boolean }>;
  executable: boolean;
};

export const FIXTURE_PACK_ID = "education-demo";
