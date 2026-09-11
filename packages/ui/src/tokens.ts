/**
 * Theme tokens for Engine Labs desktop.
 * Single styling source (D-06). Ported from docs/ui-blueprint primitives THEMES.
 *
 * decision: D-06 proposed
 * - light.t3 MUST be #617083 (AA on canvas/surface; supersedes reference #94a3b8 and UI/UX #6b7a90).
 * - t4 is decorative-only (borders of empty glyphs, unused slots). Do not use t4 for text.
 * - AA micro-adjustments (same decision): light.t2/navText #63738a (was #64748b, 4.47:1 on canvas);
 *   dimmed.t3 #8795aa (was #7d8ba0, failed surface).
 */

export const TOKEN_DECISION = "D-06 proposed" as const;

export const F = {
  sans: "'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif",
  mono: "'JetBrains Mono',ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace",
} as const;

export type ThemeKey = "light" | "dark" | "dimmed";

/** pageGradient + shadowSubtle are optional; solids match gradient mid-tones for fills/notches */
export const THEMES = {
  light: {
    name: "Light",
    icon: "sun",
    pageGradient: "linear-gradient(180deg, #eef2ff 0%, #f4f7fd 42%, #fafcfe 100%)",
    bg: "#ffffff",
    canvas: "#f5f8fe",
    surface: "#ffffff",
    raised: "#f0f4fc",
    hover: "#e8eef9",
    border: "rgba(59, 130, 246, 0.14)",
    borderMuted: "rgba(59, 130, 246, 0.09)",
    borderHover: "rgba(59, 130, 246, 0.22)",
    t1: "#1e293b",
    t2: "#63738a",
    t3: "#617083",
    /** Decorative only — not a text color (decision: D-06 proposed). */
    t4: "#a8b4c4",
    accent: "#3b82f6",
    accentBg: "#eff6ff",
    accentBorder: "rgba(59, 130, 246, 0.35)",
    accentHover: "#2563eb",
    green: "#059669",
    greenBg: "#ecfdf5",
    greenBorder: "#6ee7b7",
    red: "#e11d48",
    redBg: "#fff1f2",
    redBorder: "#fecdd3",
    amber: "#d97706",
    amberBg: "#fffbeb",
    amberBorder: "#fcd34d",
    purple: "#7c3aed",
    purpleBg: "#f5f3ff",
    purpleBorder: "#c4b5fd",
    nav: "#f8faff",
    navText: "#63738a",
    navActive: "#1e293b",
    navHover: "#eef2ff",
    btnPrimary: "#3b82f6",
    btnPrimaryHover: "#2563eb",
    shadow: "0 1px 2px rgba(15, 23, 42, 0.04)",
    shadowSubtle: "0 2px 12px rgba(15, 23, 42, 0.05)",
    shadowMd: "0 4px 20px rgba(15, 23, 42, 0.08)",
    shadowLg: "0 12px 40px rgba(15, 23, 42, 0.1)",
  },
  dark: {
    name: "Dark",
    icon: "moon",
    pageGradient: "linear-gradient(180deg, #080c14 0%, #0c111d 38%, #0f1419 100%)",
    bg: "#0c111d",
    canvas: "#0e1420",
    surface: "#121a28",
    raised: "#182235",
    hover: "#1f2d42",
    border: "rgba(96, 165, 250, 0.14)",
    borderMuted: "rgba(96, 165, 250, 0.08)",
    borderHover: "rgba(96, 165, 250, 0.24)",
    t1: "#e8eef9",
    t2: "#9fb0cc",
    t3: "#7c8ca8",
    /** Decorative only — not a text color (decision: D-06 proposed). */
    t4: "#647896",
    accent: "#60a5fa",
    accentBg: "rgba(59, 130, 246, 0.14)",
    accentBorder: "rgba(96, 165, 250, 0.35)",
    accentHover: "#93c5fd",
    green: "#4ade80",
    greenBg: "rgba(34, 197, 94, 0.12)",
    greenBorder: "rgba(74, 222, 128, 0.45)",
    red: "#fb7185",
    redBg: "rgba(251, 113, 133, 0.1)",
    redBorder: "rgba(251, 113, 133, 0.35)",
    amber: "#fbbf24",
    amberBg: "rgba(251, 191, 36, 0.1)",
    amberBorder: "rgba(251, 191, 36, 0.35)",
    purple: "#c084fc",
    purpleBg: "rgba(192, 132, 252, 0.1)",
    purpleBorder: "rgba(192, 132, 252, 0.35)",
    nav: "#121a28",
    navText: "#9fb0cc",
    navActive: "#e8eef9",
    navHover: "#182235",
    btnPrimary: "#3b82f6",
    btnPrimaryHover: "#60a5fa",
    shadow: "0 0 transparent",
    shadowSubtle: "0 2px 12px rgba(0, 0, 0, 0.35)",
    shadowMd: "0 6px 24px rgba(0, 0, 0, 0.45)",
    shadowLg: "0 16px 48px rgba(0, 0, 0, 0.55)",
  },
  dimmed: {
    name: "Dimmed",
    icon: "palette",
    pageGradient: "linear-gradient(180deg, #1a1d28 0%, #1e2433 45%, #222838 100%)",
    bg: "#222838",
    canvas: "#1e2433",
    surface: "#262d3f",
    raised: "#2e3750",
    hover: "#38445e",
    border: "rgba(100, 149, 237, 0.16)",
    borderMuted: "rgba(100, 149, 237, 0.1)",
    borderHover: "rgba(100, 149, 237, 0.26)",
    t1: "#dce4f0",
    t2: "#9aa8bc",
    t3: "#8795aa",
    /** Decorative only — not a text color (decision: D-06 proposed). */
    t4: "#6b788c",
    accent: "#6b9ef5",
    accentBg: "rgba(83, 155, 245, 0.16)",
    accentBorder: "rgba(107, 158, 245, 0.4)",
    accentHover: "#8bb4f8",
    green: "#6ecf7a",
    greenBg: "rgba(87, 171, 90, 0.14)",
    greenBorder: "rgba(110, 207, 122, 0.4)",
    red: "#f1887f",
    redBg: "rgba(229, 83, 75, 0.12)",
    redBorder: "rgba(241, 136, 127, 0.35)",
    amber: "#e3b341",
    amberBg: "rgba(198, 144, 38, 0.12)",
    amberBorder: "rgba(227, 179, 65, 0.35)",
    purple: "#b794f4",
    purpleBg: "rgba(152, 110, 226, 0.14)",
    purpleBorder: "rgba(183, 148, 244, 0.4)",
    nav: "#262d3f",
    navText: "#9aa8bc",
    navActive: "#dce4f0",
    navHover: "#2e3750",
    btnPrimary: "#539bf5",
    btnPrimaryHover: "#6cb6ff",
    shadow: "0 0 transparent",
    shadowSubtle: "0 2px 10px rgba(0, 0, 0, 0.28)",
    shadowMd: "0 5px 20px rgba(0, 0, 0, 0.38)",
    shadowLg: "0 14px 40px rgba(0, 0, 0, 0.48)",
  },
} as const;

export type Theme = {
  [K in keyof typeof THEMES.light]: string;
};

export const TEXT_TOKENS = ["t1", "t2", "t3"] as const;
export const TEXT_SURFACES = ["canvas", "surface"] as const;
export const DECORATIVE_TOKENS = ["t4"] as const;
