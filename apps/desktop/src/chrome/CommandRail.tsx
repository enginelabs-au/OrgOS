import { useEffect, useState } from "react";
import { Dot, F, type Theme } from "@engine-labs/ui";
import { apiConfigured, apiFetch, type HealthPayload } from "../api/client";
import { EmptyState } from "../views/EmptyState";
import { ErrorState } from "../views/ErrorState";

type RailSection = "health" | "priorities" | "plans" | "blockers" | "decisions";

type RailItem = { id: string; label: string; status?: string };

export function CommandRail({ T, open }: { T: Theme; open: boolean }) {
  const [section, setSection] = useState<RailSection>("health");
  const [health, setHealth] = useState<HealthPayload | null>(null);
  const [items, setItems] = useState<RailItem[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [empty, setEmpty] = useState<string | null>(null);

  const load = () => {
    setError(null);
    setEmpty(null);
    if (!apiConfigured()) {
      setEmpty("The command rail is empty until the API address is set.");
      setHealth(null);
      setItems([]);
      return;
    }
    if (section === "health") {
      void apiFetch<HealthPayload>("/health")
        .then((data) => {
          setHealth(data);
          setItems([]);
        })
        .catch((err: unknown) => {
          setHealth(null);
          setError(err instanceof Error ? err.message : "Health could not be read.");
        });
      return;
    }
    const path =
      section === "priorities"
        ? "/v1/priorities"
        : section === "plans"
          ? "/v1/plans"
          : section === "blockers"
            ? "/v1/blockers"
            : "/v1/decisions";
    void apiFetch<RailItem[] | { items?: RailItem[] }>(path)
      .then((data) => {
        const list = Array.isArray(data) ? data : data.items ?? [];
        setItems(list);
        setHealth(null);
        if (list.length === 0) setEmpty(`No ${section} yet.`);
      })
      .catch((err: unknown) => {
        setItems([]);
        setError(err instanceof Error ? err.message : `Could not load ${section}.`);
      });
  };

  useEffect(load, [section]);

  if (!open) {
    return (
      <aside
        aria-hidden
        style={{
          width: 54,
          flexShrink: 0,
          background: T.raised,
          border: `1px solid ${T.borderMuted ?? T.border}`,
          borderRadius: 12,
        }}
      />
    );
  }

  const tabs: Array<{ id: RailSection; label: string }> = [
    { id: "health", label: "Health" },
    { id: "priorities", label: "Priorities" },
    { id: "plans", label: "Plans" },
    { id: "blockers", label: "Blockers" },
    { id: "decisions", label: "Decisions" },
  ];

  return (
    <aside
      style={{
        width: 264,
        flexShrink: 0,
        background: T.raised,
        border: `1px solid ${T.borderMuted ?? T.border}`,
        borderRadius: 12,
        display: "flex",
        flexDirection: "column",
        overflow: "hidden",
        fontFamily: F.sans,
      }}
    >
      <div style={{ padding: "12px 10px 8px", color: T.t1, fontSize: 12, fontWeight: 700, letterSpacing: "0.08em" }}>
        COMPANY
      </div>
      <div style={{ display: "flex", flexWrap: "wrap", gap: 4, padding: "0 8px 8px" }}>
        {tabs.map((t) => (
          <button
            key={t.id}
            type="button"
            onClick={() => setSection(t.id)}
            style={{
              border: "none",
              background: section === t.id ? T.accentBg : "transparent",
              color: section === t.id ? T.accent : T.t2,
              borderRadius: 8,
              padding: "4px 8px",
              fontSize: 12,
              fontWeight: 600,
              cursor: "pointer",
              fontFamily: F.sans,
            }}
          >
            {t.label}
          </button>
        ))}
      </div>
      <div style={{ flex: 1, overflow: "auto", padding: 10 }}>
        {error && <ErrorState T={T} body={error} onRetry={load} />}
        {!error && empty && <EmptyState T={T} title="Nothing here yet" body={empty} />}
        {!error && !empty && health && (
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {Object.entries(health).map(([k, v]) => (
              <div key={k} style={{ display: "flex", justifyContent: "space-between", fontSize: 13, color: T.t1 }}>
                <span>{k}</span>
                <span style={{ color: T.t2 }}>{String(v)}</span>
              </div>
            ))}
          </div>
        )}
        {!error && !empty && items.map((item) => (
          <div key={item.id} style={{ display: "flex", alignItems: "center", gap: 8, padding: "8px 4px", color: T.t1, fontSize: 13 }}>
            {item.status && <Dot T={T} status={item.status} />}
            <span>{item.label || item.id}</span>
          </div>
        ))}
      </div>
    </aside>
  );
}
