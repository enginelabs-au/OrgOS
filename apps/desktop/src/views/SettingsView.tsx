import { F, PageHeader, SubNav, type Theme, type ThemeKey } from "@engine-labs/ui";
import { useState } from "react";
import { RETENTION_DEFAULTS, USAGE_EVENT_FIELDS } from "../usage/usageEventFields";
import { PermissionsEditor } from "./PermissionsEditor";

export function SettingsView({
  T,
  themeKey,
  onTheme,
}: {
  T: Theme;
  themeKey: ThemeKey;
  onTheme: (key: ThemeKey) => void;
}) {
  const [tab, setTab] = useState("data");

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 16, fontFamily: F.sans }}>
      <PageHeader T={T} name="Settings" description="Appearance, data disclosure, retention, and permissions." />
      <SubNav
        T={T}
        active={tab}
        onChange={setTab}
        tabs={[
          { id: "data", label: "Data" },
          { id: "appearance", label: "Appearance" },
          { id: "permissions", label: "Permissions" },
        ]}
      />
      {tab === "data" && (
        <div>
          <h3 style={{ color: T.t1, fontSize: 16 }}>What Papership measures</h3>
          <p style={{ color: T.t2, fontSize: 13, lineHeight: 1.5 }}>
            Papership does not own your content. Usage events store only these identifier and enum fields.
            Content, names, emails, and secrets are not included. A second seat stays blocked until this notice
            is accepted.
          </p>
          <ul style={{ color: T.t1, fontSize: 13, columns: 2 }}>
            {USAGE_EVENT_FIELDS.map((field) => (
              <li key={field} style={{ fontFamily: F.mono, fontSize: 12 }}>
                {field}
              </li>
            ))}
          </ul>
          <h3 style={{ color: T.t1, fontSize: 16 }}>Retention (read-only)</h3>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
            <thead>
              <tr>
                <th style={{ textAlign: "left", color: T.t2, padding: "8px 0" }}>Record</th>
                <th style={{ textAlign: "left", color: T.t2, padding: "8px 0" }}>Kept for</th>
              </tr>
            </thead>
            <tbody>
              {RETENTION_DEFAULTS.map((row) => (
                <tr key={row.id}>
                  <td style={{ color: T.t1, padding: "8px 0", borderTop: `1px solid ${T.border}` }}>{row.label}</td>
                  <td style={{ color: T.t2, padding: "8px 0", borderTop: `1px solid ${T.border}` }}>{row.period}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      {tab === "appearance" && (
        <div>
          <p style={{ color: T.t2, fontSize: 13 }}>Theme. Default is light until the owner chooses otherwise.</p>
          <div style={{ display: "flex", gap: 8 }}>
            {(["light", "dark", "dimmed"] as ThemeKey[]).map((key) => (
              <button
                key={key}
                type="button"
                onClick={() => onTheme(key)}
                style={{
                  padding: "8px 12px",
                  borderRadius: 8,
                  border: `1px solid ${themeKey === key ? T.accentBorder : T.border}`,
                  background: themeKey === key ? T.accentBg : T.surface,
                  color: T.t1,
                  cursor: "pointer",
                  fontFamily: F.sans,
                }}
              >
                {key}
              </button>
            ))}
          </div>
        </div>
      )}
      {tab === "permissions" && <PermissionsEditor T={T} />}
    </div>
  );
}
