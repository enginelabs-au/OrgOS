/** https-only external open with an explicit confirmation (F-SEC-17). */
export async function openExternalHttps(url: string): Promise<void> {
  let parsed: URL;
  try {
    parsed = new URL(url);
  } catch {
    return;
  }
  if (parsed.protocol !== "https:") return;
  const ok = window.confirm(`Open this address in your browser?\n${parsed.href}`);
  if (!ok) return;
  try {
    const { open } = await import("@tauri-apps/plugin-shell");
    await open(parsed.href);
  } catch {
    window.open(parsed.href, "_blank", "noopener,noreferrer");
  }
}
