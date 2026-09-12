const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

const SEAT_LABEL = {
  founder: "Founder",
  project_lead: "Project Lead",
  operator: "Operator",
  guest: "Guest",
};

export const CONNECTOR_CATALOG = [
  {
    id: "github",
    initials: "GH",
    name: "GitHub",
    kind: "Bound repository",
    status: "configured",
    destination_class: "source_control",
    scope: "Branch, change and check are granted. Release is off. Live write stays dry-run or approval-bound.",
    verified: "Configured in Papership.",
    recovery: "",
    handoff: "Authorise the GitHub App in the browser. Papership never embeds a provider sign-in.",
  },
  {
    id: "gmail",
    initials: "GM",
    name: "Gmail",
    kind: "Comms channel",
    status: "planned",
    destination_class: "mailbox",
    scope: "Read and draft stay dry-run until GMAIL_OAUTH_CLIENT_ID is set. Send needs approval then a receipt.",
    verified: "Not enabled",
    recovery: "",
    handoff: "Create a Google OAuth client, then set GMAIL_OAUTH_CLIENT_ID and GMAIL_OAUTH_REDIRECT_URL.",
  },
  {
    id: "slack",
    initials: "SL",
    name: "Slack",
    kind: "Comms channel",
    status: "planned",
    destination_class: "chat",
    scope: "Read stays dry-run until SLACK_CLIENT_ID is set. Messages need approval then a receipt.",
    verified: "Not enabled",
    recovery: "",
    handoff: "Create a Slack app, then set SLACK_CLIENT_ID.",
  },
  {
    id: "telegram",
    initials: "TG",
    name: "Telegram",
    kind: "Comms channel",
    status: "planned",
    destination_class: "chat",
    scope: "Planned until a bot mapping is supplied.",
    verified: "Not enabled",
    recovery: "",
    handoff: "Telegram stays planned until a bot mapping is supplied.",
  },
  {
    id: "whatsapp",
    initials: "WA",
    name: "WhatsApp",
    kind: "Comms channel",
    status: "planned",
    destination_class: "chat",
    scope: "Planned until a business mapping is supplied.",
    verified: "Not enabled",
    recovery: "",
    handoff: "WhatsApp Cloud API stays planned until a business mapping is supplied.",
  },
];

function token() {
  try {
    const current = localStorage.getItem("papership-token");
    if (current) return current;
    const legacy = localStorage.getItem("engine-os-token");
    if (legacy) {
      localStorage.setItem("papership-token", legacy);
      return legacy;
    }
    return "";
  } catch {
    return "";
  }
}

export async function fetchPapershipJson(path) {
  const headers = { Accept: "application/json" };
  const jwt = token();
  if (jwt) headers.Authorization = `Bearer ${jwt}`;
  const response = await fetch(`${API_BASE}${path}`, { headers });
  if (!response.ok) {
    const err = new Error(`Papership API ${path} returned ${response.status}`);
    err.status = response.status;
    throw err;
  }
  return response.json();
}

export async function loadPapershipOverlay() {
  const jwt = token();
  if (!jwt) {
    return {
      source: "unauthenticated",
      people: [],
      guests: [],
      teams: [],
      connections: CONNECTOR_CATALOG,
      threads: [],
      measurement: defaultMeasurement(),
      memory: [],
      strategy: [],
      personalisation: defaultPersonalisation(),
      view: { fallback: true, personalisation: false },
      domains: [],
      references: defaultReferences(),
      schedules: [],
    };
  }
  try {
    const [people, teams, inbox, connections, measurement, memory, strategy, personalisation, view, domains, references, schedules] = await Promise.all([
      fetchPapershipJson("/people"),
      fetchPapershipJson("/teams"),
      fetchPapershipJson("/inbox"),
      fetchPapershipJson("/connections"),
      fetchPapershipJson("/settings/measurement"),
      fetchPapershipJson("/memory"),
      fetchPapershipJson("/strategy"),
      fetchPapershipJson("/settings/personalisation"),
      fetchPapershipJson("/views/current"),
      fetchPapershipJson("/domains/catalogue"),
      fetchPapershipJson("/references"),
      fetchPapershipJson("/schedules"),
    ]);
    return {
      source: "api",
      people: people.items || [],
      guests: people.guests || [],
      teams: teams.items || [],
      connections: connections.items || CONNECTOR_CATALOG,
      threads: inbox.items || [],
      measurement,
      inboxState: inbox.state,
      peopleState: people.state,
      memory: memory.items || [],
      strategy: strategy.items || [],
      strategyKpi: strategy.kpi_status || "not_captured",
      personalisation,
      view,
      domains: domains.items || [],
      references,
      schedules: schedules.items || [],
    };
  } catch (error) {
    return {
      source: "error",
      error: error.message,
      people: [],
      guests: [],
      teams: [],
      connections: CONNECTOR_CATALOG,
      threads: [],
      measurement: defaultMeasurement(),
      memory: [],
      strategy: [],
      personalisation: defaultPersonalisation(),
      view: { fallback: true, personalisation: false },
      domains: [],
      references: defaultReferences(),
      schedules: [],
    };
  }
}

export function defaultPersonalisation() {
  return { enabled: false, default: false, inspect: { intent: "fallback", fallback: true, why: "Personalisation is off." }, pins: [], current: { fallback: true } };
}

export function defaultReferences() {
  return { currency: "AUD", calendar: "en-AU", timezone: "Australia/Sydney", kpi_default: "not_captured", metrics: [], status_labels: ["planned", "configured", "working", "unavailable"] };
}

export function defaultMeasurement() {
  return {
    title: "What Papership measures",
    owner: "Papership does not own your content. You do.",
    items: [
      "First-party, in-tenant usage events only.",
      "Identifier and enum fields: event name, ids, seat template, outcome code, token counts, tool-class counts, duration, cost band.",
      "No prompt text, names, emails, file contents, repository diffs, or secrets.",
      "No third-party analytics SDK, pixel, or replay.",
      "Events stay in the tenant store. A second seat is blocked until this notice is accepted (OQ-G2).",
    ],
    oq_g2_recorded: false,
  };
}

function mapPerson(row) {
  const template = row.template || "member";
  const founder = row.id === "principal-founder";
  const availability = row.availability || "unknown";
  const workload = row.workload || "unknown";
  return {
    name: founder ? "Cam Douglas" : SEAT_LABEL[template] || row.id,
    initials: founder ? "CD" : (SEAT_LABEL[template] || "SE").slice(0, 2).toUpperCase(),
    av: founder ? "linear-gradient(135deg,#2563eb,#a78bfa)" : "var(--t3)",
    seat: SEAT_LABEL[template] || template,
    email: founder ? "founder@enginelabs.com.au" : "not issued",
    status: founder ? "Active" : "Issued",
    dot: founder ? "var(--green)" : "var(--t3)",
    availability,
    workload,
    leave: row.leave_reference || "",
    capacity: `${availability} · ${workload}`,
  };
}

function mapTeam(row) {
  return {
    name: row.name,
    meta: row.department || "Team",
    members: row.id || "",
  };
}

function statusStyle(status) {
  if (status === "working") {
    return { bg: "var(--green-soft)", ink: "var(--green)", dot: "var(--green)", bd: "var(--line)", glyphBg: "var(--t1)", glyphInk: "var(--canvas)" };
  }
  if (status === "configured") {
    return { bg: "var(--blue-soft)", ink: "var(--blue)", dot: "var(--blue)", bd: "var(--line)", glyphBg: "var(--raised)", glyphInk: "var(--t3)" };
  }
  if (status === "unavailable") {
    return { bg: "var(--red-soft)", ink: "var(--red)", dot: "var(--red)", bd: "rgba(225,29,72,.35)", glyphBg: "var(--raised)", glyphInk: "var(--t3)" };
  }
  return { bg: "var(--line2)", ink: "var(--t3)", dot: "var(--t3)", bd: "var(--line)", glyphBg: "var(--raised)", glyphInk: "var(--t3)" };
}

export function mapConnection(row, setModal) {
  const status = row.status || "planned";
  const styles = statusStyle(status);
  const actions =
    status === "configured" || status === "working"
      ? [
          { label: "Detail", bd: "var(--line)", ink: "var(--t2)", go: () => {} },
          { label: "Revoke", bd: "var(--red)", ink: "var(--red)", go: () => setModal?.("revoke") },
        ]
      : [{ label: "Set up", bd: "var(--line)", ink: "var(--t2)", go: () => setModal?.("wizard") }];
  return {
    initials: row.initials || (row.label || row.name || row.id || "?").slice(0, 2).toUpperCase(),
    name: row.label || row.name || row.id,
    kind: row.kind || row.destination_class || "Connector",
    status,
    scope: row.scope || row.handoff || "",
    verified: row.verified || (row.last_sync ? `Last sync ${row.last_sync}` : "Not live"),
    recovery: row.recovery || "",
    actions,
    ...styles,
  };
}

export function applyPapershipOverlay(view, overlay, setModal) {
  const out = { ...view };
  const measurement = overlay.measurement || defaultMeasurement();
  out.apiSource = overlay.source;
  out.apiError = overlay.error || "";
  out.measurement = measurement;
  out.set_data = view.setTitle === "Data & retention";

  if (overlay.source === "loading") {
    out.people = [];
    out.peopleNote = "Loading people from Papership…";
    out.teams = [];
    out.teamsNote = "Loading teams from Papership…";
    out.threads = [];
    out.messages = [];
    out.ticketDetails = [];
    out.inboxNote = "Loading inbox from Papership…";
  } else {
    out.people = (overlay.people || []).map(mapPerson);
    out.peopleNote =
      overlay.source === "error"
        ? overlay.error
        : overlay.source === "unauthenticated"
          ? "No Papership API session. People stay empty until a JWT is stored as papership-token."
          : out.people.length
            ? ""
            : "No members yet.";
    const teams = overlay.teams && overlay.teams.length ? overlay.teams : [];
    out.teams = teams.map(mapTeam);
    out.teamsNote = out.teams.length ? "" : "No teams loaded. Founder can create teams after the API session is present.";
    out.threads = overlay.threads || [];
    out.messages = overlay.threads?.length ? view.messages : [];
    out.ticketDetails = overlay.threads?.length ? view.ticketDetails : [];
    out.inboxNote =
      overlay.source === "error"
        ? overlay.error
        : out.threads.length
          ? ""
          : "Inbox is empty. Papership does not show fixture mail on the product path.";
  }

  const catalog = overlay.connections?.length ? overlay.connections : CONNECTOR_CATALOG;
  out.connections = catalog.map((row) => mapConnection(row, setModal));
  out.wizardProviders = catalog;

  const memoryItems = overlay.memory || [];
  const kinds = ["Sessions", "Preferences", "Projects", "Domains", "Organisation", "Skills"];
  out.memoryNav = kinds.map((label) => {
    const n = memoryItems.filter((item) => (item.kind || "").toLowerCase() === label.toLowerCase()).length;
    return { label, n: String(n), bg: n ? "var(--blue-soft)" : "transparent", fw: n ? "600" : "500" };
  });
  out.memoryRows = memoryItems.map((item, index) => ({
    title: item.title || item.id,
    kind: item.kind || "project",
    cls: item.class || item.content_class || "source",
    version: `v${item.version || 1}`,
    bg: index === 0 ? "var(--blue-soft)" : "transparent",
  }));
  const first = memoryItems[0];
  out.provenance = first
    ? [
        { k: "Source", v: first.provenance?.source || "native" },
        { k: "Owner", v: first.provenance?.owner || first.owner_principal_id || "" },
        { k: "Class", v: first.class || "" },
        { k: "Version", v: String(first.version || 1) },
        { k: "Restriction", v: first.restriction_scope || "none" },
      ]
    : [];
  out.memoryNote =
    overlay.source === "unauthenticated"
      ? "No Papership API session. Memory stays empty until a JWT is stored as papership-token."
      : overlay.source === "error"
        ? overlay.error
        : memoryItems.length
          ? ""
          : "No memory yet. Knowledge the assistant retains will appear here with its source.";
  out.memoryEmpty = !memoryItems.length;

  const personalisation = overlay.personalisation || defaultPersonalisation();
  if (view.setTitle === "Personalisation" || view.setPane === "Personalisation") {
    out.setDesc = personalisation.enabled ? "Adaptive views can apply trusted definitions." : "Adaptive views are off by default. Inspect, disable and reset live here.";
    out.setRows = [
      { k: "Adaptive views", v: personalisation.enabled ? "On" : "Off" },
      { k: "Intent", v: personalisation.inspect?.intent || "fallback" },
      { k: "Fallback", v: personalisation.inspect?.fallback ? "Seat template" : "Adapted" },
    ];
  }
  out.personalisation = personalisation;
  out.adaptedBadge = overlay.view?.fallback || !personalisation.enabled ? "" : `Adapted for: ${overlay.view?.intent || personalisation.inspect?.intent || "intent"}`;

  const strategy = overlay.strategy || [];
  out.strategyKpi = overlay.strategyKpi || overlay.references?.kpi_default || "not_captured";
  if (overlay.source !== "loading") {
    const goals = strategy.filter((row) => row.kind === "goal" || row.kind === "initiative");
    const decisions = strategy.filter((row) => row.kind === "decision" || row.kind === "risk_appetite");
    out.railPriorities = goals.map((row) => ({
      label: row.title,
      meta: `${row.kind} · KPI ${row.kpi_status || "not_captured"}`,
      pct: 0,
      pctw: "0%",
      due: "",
      dot: "var(--t3)",
      open: () => {},
    }));
    out.railDecisions = decisions.map((row) => ({
      label: row.title,
      meta: `${row.kind} · ${row.kpi_status || "not_captured"}`,
      open: () => {},
    }));
  }
  out.domainShells = overlay.domains || [];
  out.references = overlay.references || defaultReferences();
  out.schedules = overlay.schedules || [];
  if (out.modes) {
    out.modes = out.modes.map((mode) => {
      if (!String(mode.label).startsWith("Automate")) return mode;
      return { ...mode, label: "Automate · configured", cursor: "pointer", ink: "var(--t2)" };
    });
  }
  return out;
}
