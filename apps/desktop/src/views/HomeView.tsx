import { F, PageHeader, type Theme } from "@engine-labs/ui";
import { CommandRail } from "../chrome/CommandRail";

export function HomeView({ T, railOpen }: { T: Theme; railOpen: boolean }) {
  return (
    <div style={{ display: "flex", gap: 16, minHeight: 0, flex: 1, fontFamily: F.sans }}>
      <CommandRail T={T} open={railOpen} />
      <div style={{ flex: 1, minWidth: 0, overflow: "auto" }}>
        <PageHeader T={T} name="Today" description="Here's what's happening in Papership today." />
        <p style={{ color: T.t2, fontSize: 13, lineHeight: 1.6, marginTop: 16 }}>
          Use the company rail for Health, Priorities, Plans, Blockers, and Decisions. Lists come from the API when it
          is available. Phase 2 starts at the interception spike. Nothing here is invented revenue.
        </p>
      </div>
    </div>
  );
}
