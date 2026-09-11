import { useRef } from "react";
import { Badge, Btn, F, useEscape, useFocusTrap, type Theme } from "@engine-labs/ui";

const MODES = ["Ask", "Analyse", "Plan", "Draft", "Execute", "Review", "Automate"] as const;

/**
 * Assistant chrome only (AUTH-28). Honest unavailable — never invents text.
 * Closed panel is not rendered so it is out of tab order (F-S7).
 */
export function AssistantPanel({
  T,
  open,
  onClose,
  topOffsetPx = 116,
}: {
  T: Theme;
  open: boolean;
  onClose: () => void;
  topOffsetPx?: number;
}) {
  const panelRef = useRef<HTMLDivElement>(null);
  useFocusTrap(panelRef, open);
  useEscape(onClose, open);
  if (!open) return null;

  return (
    <aside
      ref={panelRef}
      role="dialog"
      aria-modal="false"
      aria-label="Assistant"
      tabIndex={-1}
      style={{
        position: "fixed",
        top: topOffsetPx,
        right: 0,
        width: 420,
        maxWidth: "100vw",
        height: `calc(100vh - ${topOffsetPx}px)`,
        background: T.surface,
        borderLeft: `1px solid ${T.border}`,
        boxShadow: T.shadowLg,
        zIndex: 500,
        display: "flex",
        flexDirection: "column",
        fontFamily: F.sans,
        outline: "none",
      }}
    >
      <div
        style={{
          padding: 12,
          borderBottom: `1px solid ${T.border}`,
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <strong style={{ color: T.t1, fontSize: 14 }}>Assistant</strong>
        <Btn T={T} variant="ghost" small onClick={onClose}>
          Close
        </Btn>
      </div>
      <div style={{ display: "flex", flexWrap: "wrap", gap: 6, padding: 12 }}>
        {MODES.map((mode) => (
          <Badge key={mode} T={T}>
            {mode}
          </Badge>
        ))}
      </div>
      <div style={{ padding: "0 12px 8px", display: "flex", gap: 8, alignItems: "center" }}>
        <Badge T={T} color={T.accent}>
          Scope: organisation
        </Badge>
      </div>
      <div style={{ padding: "0 12px 12px", color: T.t2, fontSize: 12 }}>
        Allowance: remaining run budget is shown when the API provides it. Amounts are not priced here.
      </div>
      <div
        style={{
          margin: 12,
          padding: 16,
          borderRadius: 10,
          background: T.raised,
          border: `1px solid ${T.border}`,
          color: T.t1,
          fontSize: 13,
          lineHeight: 1.55,
        }}
      >
        <strong>unavailable</strong>
        <p style={{ margin: "8px 0 0", color: T.t2 }}>
          The assistant is not connected (AUTH-28). Engine Labs will not invent an answer. Hey Engine only opens this
          panel.
        </p>
      </div>
    </aside>
  );
}
