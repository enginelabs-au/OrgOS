import { useEffect, useState } from "react";
import { F, type Theme } from "@engine-labs/ui";
import { apiConfigured, loadList, type AuditEvent } from "../api/client";

export function StatusBar({ T }: { T: Theme }) {
  const [latest, setLatest] = useState<string>("Waiting for audit events.");
  const [offline, setOffline] = useState(false);

  useEffect(() => {
    if (!apiConfigured()) {
      setLatest("No audit events yet. Connect the API to see live status.");
      return;
    }
    void loadList<AuditEvent>("/v1/audit-events", "No audit events yet.").then((state) => {
      if (state.status === "ready") {
        const ev = state.data[0];
        setLatest(ev.message || ev.kind || "Latest audit event");
        setOffline(false);
      } else if (state.status === "empty") {
        setLatest(state.message);
      } else if (state.status === "error") {
        setLatest("Reconnecting…");
        setOffline(true);
      }
    });
  }, []);

  return (
    <footer
      aria-live="polite"
      style={{
        height: 28,
        display: "flex",
        alignItems: "center",
        gap: 10,
        padding: "0 12px",
        borderTop: `1px solid ${T.border}`,
        background: T.nav,
        fontFamily: F.sans,
        fontSize: 12,
        color: T.t2,
      }}
    >
      <span
        style={{
          background: offline ? T.redBg : T.greenBg,
          color: offline ? T.red : T.green,
          border: `1px solid ${offline ? T.redBorder : T.greenBorder}`,
          borderRadius: 99,
          padding: "1px 8px",
          fontWeight: 600,
        }}
      >
        {offline ? "Offline" : "Audit"}
      </span>
      <span style={{ overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{latest}</span>
    </footer>
  );
}
