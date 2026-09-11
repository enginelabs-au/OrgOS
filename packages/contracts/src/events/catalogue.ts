/** Event catalogue — Growth §5.4.1 `domain.object.action`. */

export type EventName = `${string}.${string}.${string}`;

export interface CatalogueEvent {
  name: EventName;
  domain: string;
  object: string;
  action: string;
  release: "R1" | "R2" | "R3" | "R4";
}

const names = [
  "work.item.created",
  "work.item.edited",
  "work.item.closed",
  "work.stage.completed",
  "agent.run.started",
  "agent.run.paused",
  "agent.run.resumed",
  "agent.run.cancelled",
  "agent.run.completed",
  "agent.run.failed",
  "agent.run.retried",
  "agent.run.recovered",
  "agent.run.escalated",
  "approval.request.created",
  "approval.decision.approved",
  "approval.decision.rejected",
  "approval.request.voided",
  "assistant.session.started",
  "assistant.mode.switched",
  "assistant.panel.opened",
  "assistant.message.sent",
  "nav.view.opened",
  "nav.tab.switched",
  "nav.palette.used",
  "handoff.source_app.opened",
  "connection.api.disconnected",
  "connection.api.reconnected",
  "connection.provider.unavailable",
  "connection.provider.restored",
  "connection.setup.completed",
  "memory.search.executed",
  "memory.item.inspected",
  "permission.grant.changed",
  "view.adaptation.previewed",
  "view.adaptation.applied",
  "view.adaptation.reverted",
  "view.adaptation.reset",
  "usage.provider_event.recorded",
  "usage.budget.reserved",
  "usage.budget.reconciled",
  "auth.session.signed_in",
  "auth.session.signed_out",
] as const;

function parseName(name: string): CatalogueEvent {
  const [domain, object, action] = name.split(".");
  const later = new Set([
    "connection.setup.completed",
    "view.adaptation.previewed",
    "view.adaptation.applied",
    "view.adaptation.reverted",
    "view.adaptation.reset",
  ]);
  return {
    name: name as EventName,
    domain,
    object,
    action,
    release: later.has(name) ? "R2" : "R1",
  };
}

export const EVENT_CATALOGUE: CatalogueEvent[] = names.map(parseName);

export const EVENT_NAME_SET = new Set(names);
