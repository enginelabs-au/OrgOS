import { F, type Theme } from "@engine-labs/ui";

export function EmptyState({ T, title, body }: { T: Theme; title: string; body: string }) {
  return (
    <div
      style={{
        padding: 28,
        border: `1px dashed ${T.border}`,
        borderRadius: 10,
        background: T.raised,
        fontFamily: F.sans,
      }}
    >
      <div style={{ color: T.t1, fontSize: 15, fontWeight: 600, marginBottom: 6 }}>{title}</div>
      <div style={{ color: T.t2, fontSize: 13, lineHeight: 1.5 }}>{body}</div>
    </div>
  );
}
