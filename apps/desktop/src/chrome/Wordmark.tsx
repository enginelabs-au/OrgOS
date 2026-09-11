import { F, PRODUCT, type Theme } from "@engine-labs/ui";

export function Wordmark({ T }: { T: Theme }) {
  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 8,
        fontFamily: F.sans,
        fontSize: 15,
        fontWeight: 700,
        color: T.navInk ?? T.t1,
        letterSpacing: "-0.01em",
        whiteSpace: "nowrap",
      }}
    >
      <span style={{ display: "inline-flex", flexDirection: "column", lineHeight: 1.1 }}>
        <span style={{ color: "#fff" }}>{PRODUCT.name}</span>
        <span style={{ fontSize: 10, fontWeight: 500, color: T.navInk2 ?? T.t3 }}>{PRODUCT.company}</span>
      </span>
    </span>
  );
}
