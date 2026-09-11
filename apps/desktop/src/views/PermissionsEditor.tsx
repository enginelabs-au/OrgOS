import { useEffect, useState } from "react";
import { Btn, F, Field, Input, type Theme } from "@engine-labs/ui";
import { apiConfigured, apiFetch, loadList, type GrantRow } from "../api/client";
import { EmptyState } from "./EmptyState";
import { ErrorState } from "./ErrorState";

export function PermissionsEditor({ T }: { T: Theme }) {
  const [state, setState] = useState<Awaited<ReturnType<typeof loadList<GrantRow>>>>({ status: "loading" });
  const [principal, setPrincipal] = useState("");
  const [grantClass, setGrantClass] = useState("");
  const [msg, setMsg] = useState<string | null>(null);

  const reload = () => {
    void loadList<GrantRow>("/v1/grants", "Only the founder seat exists so far. Extra seats arrive in a later release.").then(
      setState,
    );
  };

  useEffect(reload, []);

  const grant = async () => {
    setMsg(null);
    if (!apiConfigured()) {
      setMsg("Cannot save a grant until the API address is configured.");
      return;
    }
    try {
      await apiFetch("/v1/grants", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ principal, grant_class: grantClass }),
      });
      setPrincipal("");
      setGrantClass("");
      reload();
    } catch (err) {
      setMsg(err instanceof Error ? err.message : "The grant was not saved.");
    }
  };

  return (
    <div style={{ fontFamily: F.sans }}>
      <h3 style={{ color: T.t1, fontSize: 16, marginTop: 0 }}>Permissions</h3>
      <p style={{ color: T.t2, fontSize: 13 }}>Owner grants only. Agents cannot be approvers.</p>
      {state.status === "empty" && <EmptyState T={T} title="No grants yet" body={state.message} />}
      {state.status === "error" && <ErrorState T={T} body={state.message} onRetry={reload} />}
      {state.status === "ready" && (
        <ul style={{ color: T.t1, fontSize: 13 }}>
          {state.data.map((g) => (
            <li key={g.id}>
              {g.principal || "principal"} — {g.grant_class || g.class || "class"}
            </li>
          ))}
        </ul>
      )}
      <Field T={T} label="Principal" htmlFor="grant-principal">
        <Input T={T} id="grant-principal" value={principal} onChange={(e) => setPrincipal(e.target.value)} />
      </Field>
      <Field T={T} label="Grant class" htmlFor="grant-class">
        <Input T={T} id="grant-class" value={grantClass} onChange={(e) => setGrantClass(e.target.value)} />
      </Field>
      <Btn T={T} variant="primary" onClick={() => void grant()}>
        Grant
      </Btn>
      {msg && (
        <div role="alert" style={{ color: T.red, marginTop: 8, fontSize: 13 }}>
          {msg}
        </div>
      )}
    </div>
  );
}
