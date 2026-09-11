import { useEffect, useState } from "react";
import { Btn, F, PageHeader, type Theme } from "@engine-labs/ui";
import { apiFetch, loadList, type JobRecord } from "../api/client";
import { EmptyState } from "./EmptyState";
import { ErrorState } from "./ErrorState";

export function RunsView({ T }: { T: Theme }) {
  const [state, setState] = useState<Awaited<ReturnType<typeof loadList<JobRecord>>>>({ status: "loading" });
  const [selected, setSelected] = useState<JobRecord | null>(null);
  const [actionError, setActionError] = useState<string | null>(null);

  const reload = () => {
    setActionError(null);
    void loadList<JobRecord>("/v1/jobs", "No runs yet. Started jobs will appear here.").then((next) => {
      setState(next);
      if (next.status === "ready") setSelected(next.data[0] ?? null);
      else setSelected(null);
    });
  };

  useEffect(reload, []);

  const cancel = async () => {
    if (!selected) return;
    setActionError(null);
    try {
      await apiFetch(`/v1/jobs/${selected.id}/cancel`, { method: "POST" });
      reload();
    } catch (err) {
      setActionError(err instanceof Error ? err.message : "Cancel did not succeed.");
    }
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 16, fontFamily: F.sans, flex: 1, minHeight: 0 }}>
      <PageHeader T={T} name="Runs" description="Jobs with status, scope, budget, cancel, and recovery." />
      {state.status === "loading" && <div style={{ color: T.t2, fontSize: 13 }}>Loading runs…</div>}
      {state.status === "empty" && <EmptyState T={T} title="No runs" body={state.message} />}
      {state.status === "error" && <ErrorState T={T} body={state.message} onRetry={reload} />}
      {state.status === "ready" && (
        <div style={{ display: "grid", gridTemplateColumns: "280px 1fr", gap: 16 }}>
          <ul style={{ listStyle: "none", margin: 0, padding: 0 }}>
            {state.data.map((job) => (
              <li key={job.id}>
                <button
                  type="button"
                  onClick={() => setSelected(job)}
                  style={{
                    width: "100%",
                    textAlign: "left",
                    padding: "10px 8px",
                    border: "none",
                    background: selected?.id === job.id ? T.accentBg : "transparent",
                    color: T.t1,
                    cursor: "pointer",
                    fontFamily: F.sans,
                    fontSize: 13,
                  }}
                >
                  {job.purpose || job.id} · {job.status || "unknown"}
                </button>
              </li>
            ))}
          </ul>
          <div>
            {selected ? (
              <>
                <div style={{ color: T.t1, fontSize: 18, fontWeight: 600 }}>{selected.purpose || selected.id}</div>
                <dl style={{ color: T.t2, fontSize: 13, lineHeight: 1.7 }}>
                  <div>Status: {selected.status || "unknown"}</div>
                  <div>Scope: {selected.scope || "Not recorded"}</div>
                  <div>Budget: {selected.budget || "Recorded on the job when available (no prices shown here)."}</div>
                  <div>Recovery: {selected.recovery || "No recovery state"}</div>
                </dl>
                <Btn T={T} variant="danger" onClick={() => void cancel()}>
                  Cancel run
                </Btn>
                {actionError && (
                  <div role="alert" style={{ color: T.red, marginTop: 8, fontSize: 13 }}>
                    {actionError}
                  </div>
                )}
              </>
            ) : (
              <EmptyState T={T} title="Select a run" body="Choose a job to see detail and cancel if needed." />
            )}
          </div>
        </div>
      )}
    </div>
  );
}
