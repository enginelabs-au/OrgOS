import { useEffect, useState } from "react";
import { F, PageHeader, type Theme } from "@engine-labs/ui";
import { loadList, type WorkItem } from "../api/client";
import { EmptyState } from "./EmptyState";
import { ErrorState } from "./ErrorState";

export function WorkView({ T }: { T: Theme }) {
  const [state, setState] = useState<Awaited<ReturnType<typeof loadList<WorkItem>>>>({
    status: "loading",
  });
  const [selected, setSelected] = useState<WorkItem | null>(null);

  const reload = () => {
    setState({ status: "loading" });
    void loadList<WorkItem>("/v1/work-items", "No work items yet. New work will appear here after it is created.").then(
      (next) => {
        setState(next);
        if (next.status === "ready") setSelected(next.data[0] ?? null);
        else setSelected(null);
      },
    );
  };

  useEffect(reload, []);

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 16, fontFamily: F.sans, minHeight: 0, flex: 1 }}>
      <PageHeader T={T} name="Work" description="List, detail, and evidence." />
      {state.status === "loading" && <div style={{ color: T.t2, fontSize: 13 }}>Loading work…</div>}
      {state.status === "empty" && <EmptyState T={T} title="No work items" body={state.message} />}
      {state.status === "error" && <ErrorState T={T} body={state.message} onRetry={reload} />}
      {state.status === "ready" && (
        <div style={{ display: "grid", gridTemplateColumns: "280px 1fr", gap: 16, minHeight: 0 }}>
          <ul style={{ listStyle: "none", margin: 0, padding: 0, borderRight: `1px solid ${T.border}` }}>
            {state.data.map((item) => (
              <li key={item.id}>
                <button
                  type="button"
                  onClick={() => setSelected(item)}
                  style={{
                    width: "100%",
                    textAlign: "left",
                    padding: "10px 8px",
                    border: "none",
                    background: selected?.id === item.id ? T.accentBg : "transparent",
                    color: T.t1,
                    cursor: "pointer",
                    fontFamily: F.sans,
                    fontSize: 13,
                  }}
                >
                  {item.title || item.id}
                </button>
              </li>
            ))}
          </ul>
          <div>
            {selected ? (
              <>
                <div style={{ color: T.t1, fontSize: 18, fontWeight: 600 }}>{selected.title || selected.id}</div>
                <div style={{ color: T.t2, fontSize: 13, marginTop: 4 }}>Status: {selected.status || "unknown"}</div>
                <h3 style={{ color: T.t1, fontSize: 14, marginTop: 20 }}>Evidence</h3>
                {selected.evidence && selected.evidence.length > 0 ? (
                  <ul style={{ color: T.t2, fontSize: 13 }}>
                    {selected.evidence.map((ev, i) => (
                      <li key={ev.id || String(i)}>{ev.summary || ev.id || "Evidence record"}</li>
                    ))}
                  </ul>
                ) : (
                  <EmptyState T={T} title="No evidence yet" body="Evidence attached to this item will show here." />
                )}
              </>
            ) : (
              <EmptyState T={T} title="Select a work item" body="Choose a row on the left to see detail and evidence." />
            )}
          </div>
        </div>
      )}
    </div>
  );
}
