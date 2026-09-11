import type { CSSProperties } from "react";
import { Moon, Sun } from "./icons";
import type { Theme, ThemeKey } from "./tokens";

export function ThemeToggle({
  T,
  themeKey,
  onToggle,
}: {
  T: Theme;
  themeKey: ThemeKey;
  onToggle: () => void;
}) {
  const isDark = themeKey !== "light";
  return (
    <button
      type="button"
      title={isDark ? "Switch to light mode" : "Switch to dark mode"}
      aria-label={isDark ? "Switch to light mode" : "Switch to dark mode"}
      onClick={onToggle}
      style={{
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
        width: 36,
        height: 36,
        padding: 0,
        borderRadius: 10,
        border: `1px solid ${T.border}`,
        background: T.surface,
        color: isDark ? T.amber : T.purple,
        cursor: "pointer",
      } satisfies CSSProperties}
    >
      {isDark ? <Sun size={16} color="currentColor" /> : <Moon size={16} color="currentColor" />}
    </button>
  );
}
