import { useEffect, useState } from "react";
import { Badge, F, PageHeader, type Theme } from "@engine-labs/ui";
import { loadList, type RegistryRow } from "../api/client";
import { EmptyState } from "./EmptyState";
import { ErrorState } from "./ErrorState";

export function ConnectionsView({ T }: { T: Theme }) {
  const [state, setState] = useState<Awaited<ReturnType<typeof loadList<RegistryRow>>>>({ status: "loading" });

  const reload = () => {
    void loadList<RegistryRow>("/v1/registry", "The capability registry is empty or unavailable.").then(setState);
  };

  useEffect(reload, []);

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 16, fontFamily: F.sans }}>
      <PageHeader T={T} name="Connections" description="Registry (read-only). Planned and unavailable rows stay visible." />
      {state.status === "loading" && <div style={{ color: T.t2, fontSize: 13 }}>Loading registry…</div>}
      {state.status === "empty" && <EmptyState T={T} title="No registry rows" body={state.message} />}
      {state.status === "error" && <ErrorState T={T} body={state.message} onRetry={reload} />}
      {state.status === "ready" && (
        <ul style={{ listStyle: "none", margin: 0, padding: 0, display: "flex", flexDirection: "column", gap: 8 }}>
          {state.data.map((row) => (
            <li
              key={row.id || row.capability_id}
              style={{
                display: "flex",
                justifyContent: "space-between",
                padding: 12,
                border: `1px solid ${T.border}`,
                borderRadius: 8,
                background: T.surface,
              }}
            >
              <span style={{ color: T.t1, fontSize: 13 }}>{row.name || row.capability_id || row.id}</span>
              <Badge T={T}>{row.status || "planned"}</Badge>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
