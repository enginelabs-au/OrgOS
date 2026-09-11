import { readSession } from "../auth/keychain";

export type LoadState<T> =
  | { status: "loading" }
  | { status: "empty"; message: string }
  | { status: "error"; message: string }
  | { status: "ready"; data: T };

export function apiBase(): string {
  const raw = import.meta.env.ENGINE_API_BASE_URL || import.meta.env.VITE_ENGINE_API_BASE_URL || "";
  return raw.replace(/\/$/, "");
}

export function apiConfigured(): boolean {
  return apiBase().length > 0;
}

async function authHeader(): Promise<Record<string, string>> {
  const session = await readSession();
  if (!session?.accessToken) return {};
  return { Authorization: `Bearer ${session.accessToken}` };
}

export async function apiFetch<T>(path: string, init: RequestInit = {}): Promise<T> {
  const base = apiBase();
  if (!base) {
    throw new Error("The API address is not configured. Set ENGINE_API_BASE_URL.");
  }
  const headers = new Headers(init.headers);
  if (!headers.has("Accept")) headers.set("Accept", "application/json");
  const auth = await authHeader();
  for (const [k, v] of Object.entries(auth)) headers.set(k, v);
  const res = await fetch(`${base}${path}`, { ...init, headers });
  if (!res.ok) {
    let detail = `The server replied with status ${res.status}.`;
    try {
      const body = (await res.json()) as { error?: string; message?: string };
      detail = body.message || body.error || detail;
    } catch {
      /* keep status text */
    }
    throw new Error(plainError(detail));
  }
  if (res.status === 204) return undefined as T;
  return (await res.json()) as T;
}

export function plainError(message: string): string {
  return message.replace(/https?:\/\/\S+/g, "").trim() || "Something went wrong. Try again.";
}

export async function loadList<T>(path: string, emptyMessage: string): Promise<LoadState<T[]>> {
  if (!apiConfigured()) {
    return { status: "empty", message: "Nothing to show yet. The API address is not configured." };
  }
  try {
    const data = await apiFetch<T[] | { items?: T[] }>(path);
    const items = Array.isArray(data) ? data : data.items ?? [];
    if (items.length === 0) return { status: "empty", message: emptyMessage };
    return { status: "ready", data: items };
  } catch (err) {
    return { status: "error", message: err instanceof Error ? err.message : "Could not load this list." };
  }
}

export type SignInResult = { access_token?: string; accessToken?: string; grant_version?: string; grantVersion?: string };

export async function signIn(email: string, strongFactor: string): Promise<SignInResult> {
  const base = apiBase();
  if (!base) {
    throw new Error("The API address is not configured. Set ENGINE_API_BASE_URL.");
  }
  const res = await fetch(`${base}/auth/v1/token?grant_type=password`, {
    method: "POST",
    headers: { Accept: "application/json", "Content-Type": "application/json" },
    body: JSON.stringify({ email, password: strongFactor }),
  });
  if (!res.ok) {
    throw new Error("Sign-in did not succeed. Check the email and strong factor, then try again.");
  }
  return (await res.json()) as SignInResult;
}

export type HealthPayload = {
  status?: string;
  db?: string;
  dbos?: string;
  worker?: string;
  hermes?: string;
  github?: string;
};

export type AuditEvent = {
  id?: string;
  kind?: string;
  message?: string;
  occurred_at?: string;
  occurredAt?: string;
};

export type WorkItem = {
  id: string;
  title?: string;
  status?: string;
  stage?: string;
  evidence?: Array<{ id?: string; summary?: string }>;
  loop?: Array<{ stage?: string; evidence?: string }>;
};

export type JobRecord = {
  id: string;
  status?: string;
  scope?: string;
  budget?: string;
  recovery?: string;
  purpose?: string;
};

export type RegistryRow = {
  id?: string;
  capability_id?: string;
  name?: string;
  status?: string;
};

export type GrantRow = {
  id?: string;
  principal?: string;
  class?: string;
  grant_class?: string;
};
