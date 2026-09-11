/**
 * Session token store (AUTH-26).
 *
 * Packaged Tauri builds persist tokens through Rust `keychain_*` commands
 * (OS keychain via the `keyring` crate). Vite-dev has no keychain plugin:
 * tokens stay in process memory only.
 *
 * Never use localStorage, sessionStorage, or document.cookie for tokens.
 */

const MEMORY_KEY = "engine-labs.session";

const memory = new Map<string, string>();

function isTauriRuntime(): boolean {
  return typeof window !== "undefined" && "__TAURI_INTERNALS__" in window;
}

async function invokeKeychain<T>(cmd: string, args?: Record<string, unknown>): Promise<T | undefined> {
  if (!isTauriRuntime()) return undefined;
  try {
    const { invoke } = await import("@tauri-apps/api/core");
    return await invoke<T>(cmd, args);
  } catch {
    return undefined;
  }
}

export async function storeToken(token: string): Promise<void> {
  const stored = await invokeKeychain<void>("keychain_set", { value: token });
  if (stored === undefined) memory.set(MEMORY_KEY, token);
}

export async function readToken(): Promise<string | null> {
  const fromTauri = await invokeKeychain<string | null>("keychain_get");
  if (fromTauri !== undefined && fromTauri !== null) return fromTauri;
  return memory.get(MEMORY_KEY) ?? null;
}

export async function clearToken(): Promise<void> {
  await invokeKeychain<void>("keychain_clear");
  memory.delete(MEMORY_KEY);
}

export type SessionRecord = {
  accessToken: string;
  grantVersion?: string;
};

let sessionMemory: SessionRecord | null = null;

export async function storeSession(session: SessionRecord): Promise<void> {
  sessionMemory = session;
  await storeToken(session.accessToken);
}

export async function readSession(): Promise<SessionRecord | null> {
  if (sessionMemory) return sessionMemory;
  const token = await readToken();
  if (!token) return null;
  sessionMemory = { accessToken: token };
  return sessionMemory;
}

export async function clearSession(): Promise<void> {
  sessionMemory = null;
  await clearToken();
}

export function purgeCachesOnGrantVersionChange(previous: string | undefined, next: string | undefined): boolean {
  if (previous && next && previous !== next) {
    sessionMemory = sessionMemory ? { ...sessionMemory, grantVersion: next } : null;
    return true;
  }
  return false;
}
