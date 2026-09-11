import { F, type Theme } from "@engine-labs/ui";

export function Wordmark({ T }: { T: Theme }) {
  return (
    <span
      style={{
        fontFamily: F.sans,
        fontSize: 15,
        fontWeight: 700,
        color: T.t1,
        letterSpacing: "-0.01em",
        whiteSpace: "nowrap",
      }}
    >
      Engine Labs
    </span>
  );
}
