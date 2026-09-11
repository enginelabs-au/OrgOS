import {
  useId,
  useRef,
  useState,
  type CSSProperties,
  type KeyboardEvent,
  type MouseEvent,
  type ReactNode,
} from "react";
import { useEscape, useFocusTrap, useViewport } from "./a11y";
import { F, type Theme } from "./tokens";

export { F } from "./tokens";

type Style = CSSProperties;

function mergeFocusHover(
  hovered: boolean,
  focused: boolean,
  rest: string,
  active: string,
): string {
  return hovered || focused ? active : rest;
}

export function Surface({
  children,
  T,
  style: ex = {},
  onClick,
  hoverable,
}: {
  children: ReactNode;
  T: Theme;
  style?: Style;
  onClick?: () => void;
  hoverable?: boolean;
}) {
  const [hov, setHov] = useState(false);
  const [focused, setFocused] = useState(false);
  const rest = T.shadowSubtle != null ? T.shadowSubtle : "none";
  const style: Style = {
    background: T.surface,
    border: `1px solid ${T.border}`,
    borderRadius: 10,
    boxShadow: mergeFocusHover(hov, focused, rest, T.shadowMd),
    transition: "all 0.15s",
    cursor: onClick ? "pointer" : "default",
    fontFamily: F.sans,
    ...ex,
  };
  if (onClick) {
    return (
      <button
        type="button"
        onClick={onClick}
        onMouseEnter={() => hoverable && setHov(true)}
        onMouseLeave={() => hoverable && setHov(false)}
        onFocus={() => hoverable && setFocused(true)}
        onBlur={() => setFocused(false)}
        style={{ ...style, textAlign: "left", width: "100%" }}
      >
        {children}
      </button>
    );
  }
  return (
    <div
      onMouseEnter={() => hoverable && setHov(true)}
      onMouseLeave={() => hoverable && setHov(false)}
      style={style}
    >
      {children}
    </div>
  );
}

export type BtnVariant = "primary" | "default" | "ghost" | "outline" | "accent" | "danger" | "success" | "rainbow";

export function Btn({
  children,
  onClick,
  variant = "default",
  small,
  disabled,
  T,
  full,
  style: ex = {},
  type = "button",
}: {
  children: ReactNode;
  onClick?: () => void;
  variant?: BtnVariant;
  small?: boolean;
  disabled?: boolean;
  T: Theme;
  full?: boolean;
  style?: Style;
  type?: "button" | "submit" | "reset";
}) {
  const [hov, setHov] = useState(false);
  const [focused, setFocused] = useState(false);
  const v = {
    primary: { bg: T.btnPrimary, hbg: T.btnPrimaryHover, color: "#fff", border: "1px solid rgba(31,35,40,0.15)" },
    default: { bg: T.raised, hbg: T.hover, color: T.t1, border: `1px solid ${T.border}` },
    ghost: { bg: "transparent", hbg: T.hover, color: T.t2, border: "1px solid transparent" },
    outline: { bg: "transparent", hbg: T.hover, color: T.t1, border: `1px solid ${T.border}` },
    accent: { bg: T.accent, hbg: T.accentHover, color: "#fff", border: "1px solid rgba(31,35,40,0.15)" },
    danger: { bg: T.raised, hbg: T.redBg, color: T.red, border: `1px solid ${T.border}` },
    success: { bg: T.greenBg, hbg: `${T.green}22`, color: T.green, border: `1px solid ${T.greenBorder}` },
    rainbow: { bg: T.rainbow, hbg: T.rainbow, color: "#fff", border: "1px solid transparent" },
  }[variant];
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      onMouseEnter={() => setHov(true)}
      onMouseLeave={() => setHov(false)}
      onFocus={() => setFocused(true)}
      onBlur={() => setFocused(false)}
      style={{
        background: mergeFocusHover(hov, focused, v.bg, v.hbg),
        color: v.color,
        border: v.border,
        outline: focused ? `2px solid ${T.accent}` : "none",
        outlineOffset: 2,
        borderRadius: 6,
        padding: small ? "3px 10px" : "5px 14px",
        fontSize: small ? 12 : 13,
        fontWeight: 500,
        cursor: disabled ? "not-allowed" : "pointer",
        fontFamily: F.sans,
        display: "inline-flex",
        alignItems: "center",
        gap: 6,
        opacity: disabled ? 0.5 : 1,
        transition: "all 0.12s",
        whiteSpace: "nowrap",
        width: full ? "100%" : undefined,
        justifyContent: full ? "center" : undefined,
        lineHeight: 1.4,
        minHeight: 32,
        ...ex,
      }}
    >
      {children}
    </button>
  );
}

export function Badge({
  children,
  color,
  bg,
  T,
  variant = "default",
}: {
  children: ReactNode;
  color?: string;
  bg?: string;
  T: Theme;
  variant?: "default" | "colored";
}) {
  const styles = {
    default: { bg: T.raised, color: T.t2, border: T.border },
    colored: { bg: bg || `${color || T.accent}22`, color: color || T.accent, border: `${color || T.accent}44` },
  };
  const s = color || variant === "colored" ? styles.colored : styles.default;
  return (
    <span
      style={{
        background: s.bg,
        color: s.color,
        border: `1px solid ${s.border}`,
        borderRadius: 999,
        padding: "0 7px",
        fontSize: 12,
        fontWeight: 500,
        whiteSpace: "nowrap",
        display: "inline-flex",
        alignItems: "center",
        gap: 4,
        lineHeight: "18px",
        height: 20,
      }}
    >
      {children}
    </span>
  );
}

export type DotStatus =
  | "online"
  | "active"
  | "connected"
  | "on_track"
  | "done"
  | "idle"
  | "away"
  | "degraded"
  | "at_risk"
  | "review"
  | "planning"
  | "paused"
  | "todo"
  | "in_progress"
  | "disconnected"
  | "error"
  | string;

export function Dot({ status, T, size = 8 }: { status: DotStatus; T: Theme; size?: number }) {
  const c: Record<string, string> = {
    online: T.green,
    active: T.green,
    connected: T.green,
    on_track: T.green,
    done: T.green,
    idle: T.amber,
    away: T.amber,
    degraded: T.amber,
    at_risk: T.amber,
    review: T.amber,
    planning: T.t3,
    paused: T.t3,
    todo: T.t3,
    in_progress: T.accent,
    disconnected: T.red,
    error: T.red,
  };
  return (
    <span
      aria-hidden
      style={{
        width: size,
        height: size,
        borderRadius: "50%",
        background: c[status] || T.t3,
        display: "inline-block",
        flexShrink: 0,
      }}
    />
  );
}

export function Avi({ name, size = 28 }: { name?: string; size?: number }) {
  const ini = (name || "?")
    .split(" ")
    .map((w) => w[0])
    .slice(0, 2)
    .join("")
    .toUpperCase();
  const palette = ["#0969da", "#1a7f37", "#8250df", "#9a6700", "#d1242f", "#bf3989", "#0550ae"];
  const c = palette[(name || "X").charCodeAt(0) % palette.length];
  return (
    <div
      aria-hidden
      style={{
        width: size,
        height: size,
        borderRadius: "50%",
        background: c,
        color: "#fff",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontSize: size * 0.38,
        fontWeight: 600,
        flexShrink: 0,
        fontFamily: F.sans,
      }}
    >
      {ini}
    </div>
  );
}

export function Toggle({
  on,
  onChange,
  T,
  label,
}: {
  on: boolean;
  onChange?: (next: boolean) => void;
  T: Theme;
  label?: string;
}) {
  const [focused, setFocused] = useState(false);
  return (
    <button
      type="button"
      role="switch"
      aria-checked={on}
      aria-label={label}
      onClick={() => onChange?.(!on)}
      onFocus={() => setFocused(true)}
      onBlur={() => setFocused(false)}
      style={{
        width: 32,
        height: 18,
        borderRadius: 99,
        background: on ? T.btnPrimary : T.border,
        cursor: "pointer",
        position: "relative",
        transition: "background 0.15s",
        flexShrink: 0,
        border: focused ? `2px solid ${T.accent}` : "2px solid transparent",
        padding: 0,
      }}
    >
      <span
        aria-hidden
        style={{
          width: 14,
          height: 14,
          borderRadius: "50%",
          background: "#fff",
          position: "absolute",
          top: 0,
          left: on ? 14 : 0,
          transition: "left 0.15s",
          boxShadow: "0 1px 2px rgba(0,0,0,.2)",
        }}
      />
    </button>
  );
}

export function Input({
  T,
  value,
  onChange,
  placeholder,
  type = "text",
  style: ex = {},
  icon,
  onKeyDown,
  autoFocus,
  defaultValue,
  id,
  name,
  autoComplete,
  required,
}: {
  T: Theme;
  value?: string;
  onChange?: (event: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder?: string;
  type?: string;
  style?: Style;
  icon?: ReactNode;
  onKeyDown?: (event: KeyboardEvent<HTMLInputElement>) => void;
  autoFocus?: boolean;
  defaultValue?: string;
  id?: string;
  name?: string;
  autoComplete?: string;
  required?: boolean;
}) {
  const [focus, setFocus] = useState(false);
  return (
    <div style={{ position: "relative", width: "100%" }}>
      {icon && (
        <span
          style={{
            position: "absolute",
            left: 9,
            top: "50%",
            transform: "translateY(-50%)",
            color: T.t3,
            display: "flex",
            pointerEvents: "none",
          }}
        >
          {icon}
        </span>
      )}
      <input
        id={id}
        name={name}
        type={type}
        value={value}
        defaultValue={defaultValue}
        onChange={onChange}
        placeholder={placeholder}
        onKeyDown={onKeyDown}
        autoFocus={autoFocus}
        autoComplete={autoComplete}
        required={required}
        onFocus={() => setFocus(true)}
        onBlur={() => setFocus(false)}
        style={{
          background: T.surface,
          border: `1px solid ${focus ? T.accent : T.border}`,
          boxShadow: focus ? `0 0 0 3px ${T.accentBg}` : "none",
          borderRadius: 6,
          color: T.t1,
          padding: icon ? "5px 12px 5px 30px" : "5px 12px",
          fontSize: 14,
          outline: "none",
          fontFamily: F.sans,
          width: "100%",
          boxSizing: "border-box",
          transition: "all .15s",
          minHeight: 32,
          ...ex,
        }}
      />
    </div>
  );
}

export function Select({
  T,
  value,
  onChange,
  children,
  style: ex = {},
  defaultValue,
  id,
}: {
  T: Theme;
  value?: string;
  onChange?: (event: React.ChangeEvent<HTMLSelectElement>) => void;
  children: ReactNode;
  style?: Style;
  defaultValue?: string;
  id?: string;
}) {
  const [focus, setFocus] = useState(false);
  return (
    <select
      id={id}
      value={value}
      defaultValue={defaultValue}
      onChange={onChange}
      onFocus={() => setFocus(true)}
      onBlur={() => setFocus(false)}
      style={{
        background: T.raised,
        border: `1px solid ${focus ? T.accent : T.border}`,
        boxShadow: focus ? `0 0 0 3px ${T.accentBg}` : "none",
        borderRadius: 6,
        color: T.t1,
        padding: "5px 28px 5px 12px",
        fontSize: 14,
        outline: "none",
        fontFamily: F.sans,
        appearance: "none",
        backgroundImage: `url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 16 16' fill='${encodeURIComponent(T.t3)}'%3E%3Cpath d='M4.427 9.427l3.396 3.396a.251.251 0 00.354 0l3.396-3.396A.25.25 0 0011.396 9H4.604a.25.25 0 00-.177.427z'/%3E%3C/svg%3E")`,
        backgroundRepeat: "no-repeat",
        backgroundPosition: "right 8px center",
        cursor: "pointer",
        minHeight: 32,
        ...ex,
      }}
    >
      {children}
    </select>
  );
}

export function Progress({ value, color, T }: { value: number; color?: string; T: Theme }) {
  return (
    <div
      role="progressbar"
      aria-valuenow={Math.round(Math.min(100, value))}
      aria-valuemin={0}
      aria-valuemax={100}
      style={{ background: T.raised, borderRadius: 99, height: 6, overflow: "hidden", border: `1px solid ${T.border}` }}
    >
      <div
        style={{
          width: `${Math.min(100, value)}%`,
          height: "100%",
          background: color || T.accent,
          transition: "width 0.8s ease",
        }}
      />
    </div>
  );
}

export function Sparkline({
  data,
  color,
  height = 28,
  width = 80,
}: {
  data?: number[];
  color: string;
  height?: number;
  width?: number;
}) {
  if (!data || data.length < 2) return null;
  const max = Math.max(...data);
  const min = Math.min(...data);
  const r = max - min || 1;
  const pts = data
    .map((v, i) => `${(i / (data.length - 1)) * width},${height - ((v - min) / r) * height}`)
    .join(" ");
  return (
    <svg width={width} height={height} style={{ overflow: "visible", flexShrink: 0 }} aria-hidden>
      <polyline points={pts} fill="none" stroke={color} strokeWidth="1.5" strokeLinejoin="round" strokeLinecap="round" />
      <polygon points={`0,${height} ${pts} ${width},${height}`} fill={`${color}18`} stroke="none" />
    </svg>
  );
}

export type TableCol<Row> = {
  key: string;
  label: string;
  muted?: boolean;
  render?: (value: unknown, row: Row) => ReactNode;
};

export function Table<Row extends Record<string, unknown>>({
  cols,
  rows,
  T,
  onRow,
  emptyMsg = "No data",
  variant = "card",
  selectedId,
  rowKey = "id",
}: {
  cols: TableCol<Row>[];
  rows: Row[];
  T: Theme;
  onRow?: (row: Row) => void;
  emptyMsg?: string;
  variant?: "card" | "plain";
  selectedId?: unknown;
  rowKey?: string;
}) {
  const [hov, setHov] = useState<number | null>(null);
  const [focusIdx, setFocusIdx] = useState<number | null>(null);
  const rowLine = `1px solid ${T.borderMuted ?? T.border}`;
  const wrap =
    variant === "card"
      ? {
          borderRadius: 8,
          border: `1px solid ${T.border}`,
          overflow: "hidden",
          background: T.surface,
        }
      : {};

  return (
    <div style={wrap}>
      <div style={{ overflowX: "auto" }}>
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              {cols.map((c) => (
                <th
                  key={c.key}
                  scope="col"
                  style={{
                    padding: "12px 18px",
                    textAlign: "left",
                    fontSize: 12,
                    fontWeight: 600,
                    color: T.t2,
                    borderBottom: rowLine,
                    whiteSpace: "nowrap",
                    background: T.surface,
                    letterSpacing: "0.01em",
                  }}
                >
                  {c.label}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.length === 0 && (
              <tr>
                <td colSpan={cols.length} style={{ padding: 40, textAlign: "center", color: T.t3, fontSize: 13 }}>
                  {emptyMsg}
                </td>
              </tr>
            )}
            {rows.map((row, i) => {
              const rid = row[rowKey];
              const selected = selectedId != null && rid === selectedId;
              const rowBg = selected ? T.accentBg : hov === i || focusIdx === i ? T.hover : "transparent";
              const activate = () => onRow?.(row);
              const onKey = (e: KeyboardEvent<HTMLTableRowElement>) => {
                if (e.key === "Enter" || e.key === " ") {
                  e.preventDefault();
                  activate();
                }
              };
              return (
                <tr
                  key={String(rid ?? i)}
                  tabIndex={onRow ? 0 : undefined}
                  onMouseEnter={() => setHov(i)}
                  onMouseLeave={() => setHov(null)}
                  onFocus={() => setFocusIdx(i)}
                  onBlur={() => setFocusIdx(null)}
                  onClick={activate}
                  onKeyDown={onKey}
                  style={{
                    background: rowBg,
                    cursor: onRow ? "pointer" : "default",
                    transition: "background 0.12s ease",
                    outline: focusIdx === i ? `2px solid ${T.accent}` : "none",
                    outlineOffset: -2,
                  }}
                >
                  {cols.map((c) => (
                    <td
                      key={c.key}
                      style={{
                        padding: "14px 18px",
                        fontSize: 13,
                        color: c.muted ? T.t2 : T.t1,
                        borderBottom: i < rows.length - 1 ? rowLine : "none",
                        verticalAlign: "middle",
                        lineHeight: 1.45,
                      }}
                    >
                      {c.render ? c.render(row[c.key], row) : ((row[c.key] as ReactNode) ?? <span style={{ color: T.t4 }}>—</span>)}
                    </td>
                  ))}
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export function SlideOver({
  open,
  onClose,
  title,
  subtitle,
  children,
  T,
  width = 420,
  topOffsetPx,
}: {
  open: boolean;
  onClose: () => void;
  title: string;
  subtitle?: string;
  children: ReactNode;
  T: Theme;
  width?: number;
  topOffsetPx?: number;
}) {
  const { isMobile } = useViewport();
  const panelRef = useRef<HTMLDivElement>(null);
  const titleId = useId();
  useFocusTrap(panelRef, open);
  useEscape(onClose, open);
  if (!open) return null;
  const effectiveWidth = isMobile ? Math.min(typeof window !== "undefined" ? window.innerWidth - 32 : width, width) : width;
  const top = topOffsetPx !== undefined ? topOffsetPx : isMobile ? 100 : 116;
  return (
    <>
      <div onClick={onClose} style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,.4)", zIndex: 200 }} />
      <div
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        tabIndex={-1}
        style={{
          position: "fixed",
          top,
          right: 0,
          bottom: 0,
          width: effectiveWidth,
          maxWidth: "100vw",
          background: T.surface,
          borderLeft: `1px solid ${T.border}`,
          zIndex: 201,
          display: "flex",
          flexDirection: "column",
          boxShadow: T.shadowLg,
          outline: "none",
        }}
      >
        <div
          style={{
            padding: "16px 20px",
            borderBottom: `1px solid ${T.border}`,
            display: "flex",
            justifyContent: "space-between",
            alignItems: "flex-start",
            flexShrink: 0,
          }}
        >
          <div>
            <div id={titleId} style={{ color: T.t1, fontSize: 16, fontWeight: 600 }}>
              {title}
            </div>
            {subtitle && <div style={{ color: T.t3, fontSize: 12, marginTop: 2 }}>{subtitle}</div>}
          </div>
          <Btn T={T} variant="ghost" small onClick={onClose}>
            Close
          </Btn>
        </div>
        <div style={{ flex: 1, overflow: "auto" }}>{children}</div>
      </div>
    </>
  );
}

export function Modal({
  open,
  onClose,
  title,
  children,
  T,
  width = 520,
}: {
  open: boolean;
  onClose: () => void;
  title: string;
  children: ReactNode;
  T: Theme;
  width?: number;
}) {
  const panelRef = useRef<HTMLDivElement>(null);
  const titleId = useId();
  useFocusTrap(panelRef, open);
  useEscape(onClose, open);
  if (!open) return null;
  return (
    <div
      style={{
        position: "fixed",
        inset: 0,
        background: "rgba(0,0,0,.5)",
        zIndex: 300,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        padding: 16,
      }}
      onClick={onClose}
    >
      <div
        ref={panelRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        tabIndex={-1}
        style={{
          background: T.surface,
          borderRadius: 12,
          width: "100%",
          maxWidth: width,
          maxHeight: "88vh",
          overflow: "auto",
          boxShadow: T.shadowLg,
          border: `1px solid ${T.border}`,
          outline: "none",
        }}
        onClick={(e: MouseEvent<HTMLDivElement>) => e.stopPropagation()}
      >
        <div
          style={{
            padding: "16px 20px",
            borderBottom: `1px solid ${T.border}`,
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <div id={titleId} style={{ color: T.t1, fontSize: 15, fontWeight: 600 }}>
            {title}
          </div>
          <Btn T={T} variant="ghost" small onClick={onClose}>
            Close
          </Btn>
        </div>
        <div style={{ padding: "20px 22px" }}>{children}</div>
      </div>
    </div>
  );
}

export function Field({
  label,
  children,
  T,
  hint,
  htmlFor,
}: {
  label: string;
  children: ReactNode;
  T: Theme;
  hint?: string;
  htmlFor?: string;
}) {
  const autoId = useId();
  const id = htmlFor ?? autoId;
  return (
    <div style={{ marginBottom: 16 }}>
      <label htmlFor={id} style={{ display: "block", color: T.t1, fontSize: 14, fontWeight: 600, marginBottom: 6 }}>
        {label}
      </label>
      {children}
      {hint && <div style={{ color: T.t3, fontSize: 12, marginTop: 4 }}>{hint}</div>}
    </div>
  );
}

export function SectionLabel({ children, T, action }: { children: ReactNode; T: Theme; action?: ReactNode }) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: 12,
        paddingBottom: 8,
        borderBottom: `1px solid ${T.border}`,
      }}
    >
      <span style={{ color: T.t1, fontSize: 14, fontWeight: 600 }}>{children}</span>
      {action}
    </div>
  );
}

export type NavTab = { id: string; label: string; icon?: ReactNode; badge?: number };

export function PrimaryNavTabs({
  T,
  tabs,
  active,
  onChange,
  isMobile,
  leading,
}: {
  T: Theme;
  tabs: NavTab[];
  active: string;
  onChange: (id: string) => void;
  isMobile?: boolean;
  leading?: ReactNode;
}) {
  const R = 11;
  const fill = T.canvas;
  const padX = isMobile ? 10 : 13;
  const padY = isMobile ? 9 : 10;
  const [hov, setHov] = useState<string | null>(null);
  const [focusId, setFocusId] = useState<string | null>(null);

  return (
    <div
      role="tablist"
      style={{
        display: "flex",
        alignItems: "flex-end",
        gap: 6,
        padding: isMobile ? "6px 8px 0" : "8px 12px 0",
        overflowX: "auto",
        overflowY: "hidden",
        WebkitOverflowScrolling: "touch",
        scrollbarWidth: "thin",
        minHeight: isMobile ? 46 : 48,
      }}
    >
      {leading != null && (
        <div style={{ flexShrink: 0, paddingBottom: 0, display: "flex", alignItems: "flex-end" }}>{leading}</div>
      )}
      {tabs.map((t) => {
        const isActive = active === t.id;
        const hot = !isActive && (hov === t.id || focusId === t.id);
        return (
          <button
            key={t.id}
            type="button"
            role="tab"
            aria-selected={isActive}
            onClick={(e) => {
              e.stopPropagation();
              onChange(t.id);
            }}
            onMouseEnter={() => setHov(t.id)}
            onMouseLeave={() => setHov(null)}
            onFocus={() => setFocusId(t.id)}
            onBlur={() => setFocusId(null)}
            style={{
              position: "relative",
              zIndex: isActive ? 2 : 1,
              padding: `${padY}px ${padX}px`,
              display: "flex",
              alignItems: "center",
              gap: isMobile ? 5 : 8,
              background: isActive ? fill : hot ? T.navHover : "transparent",
              border: "none",
              borderRadius: isActive ? `${R}px ${R}px 0 0` : 0,
              marginBottom: 0,
              color: isActive || hot ? T.t1 : (T.navText ?? T.t2),
              fontSize: isMobile ? 13 : 14,
              fontWeight: isActive ? 600 : 500,
              cursor: "pointer",
              fontFamily: F.sans,
              transition: "color .12s, background .12s",
              whiteSpace: "nowrap",
              flexShrink: 0,
              boxShadow: isActive ? `0 1px 0 0 ${fill}` : "none",
              outline: focusId === t.id ? `2px solid ${T.accent}` : "none",
              outlineOffset: 2,
            }}
          >
            {isActive && (
              <>
                <span
                  aria-hidden
                  style={{
                    position: "absolute",
                    left: -R,
                    bottom: 0,
                    width: R,
                    height: R,
                    pointerEvents: "none",
                    borderBottomRightRadius: R,
                    boxShadow: `${R}px ${R}px 0 ${R}px ${fill}`,
                  }}
                />
                <span
                  aria-hidden
                  style={{
                    position: "absolute",
                    right: -R,
                    bottom: 0,
                    width: R,
                    height: R,
                    pointerEvents: "none",
                    borderBottomLeftRadius: R,
                    boxShadow: `${-R}px ${R}px 0 ${R}px ${fill}`,
                  }}
                />
              </>
            )}
            <span style={{ display: "flex", color: isActive ? T.t2 : T.t3, position: "relative", zIndex: 1 }}>{t.icon}</span>
            {(!isMobile || isActive) && (
              <span style={{ position: "relative", zIndex: 1, display: "inline-flex", alignItems: "center", gap: 6 }}>
                {t.label}
                {t.badge != null && t.badge !== 0 && (
                  <span
                    style={{
                      background: T.accent,
                      color: "#fff",
                      borderRadius: 99,
                      padding: "1px 6px",
                      fontSize: 10,
                      fontWeight: 700,
                      lineHeight: 1.35,
                    }}
                  >
                    {t.badge}
                  </span>
                )}
              </span>
            )}
          </button>
        );
      })}
    </div>
  );
}

export function SubNav({
  T,
  tabs,
  active,
  onChange,
}: {
  T: Theme;
  tabs: Array<NavTab & { count?: number }>;
  active: string;
  onChange: (id: string) => void;
}) {
  const [hov, setHov] = useState<string | null>(null);
  const [focusId, setFocusId] = useState<string | null>(null);
  return (
    <div
      role="tablist"
      style={{
        display: "flex",
        alignItems: "center",
        gap: 8,
        flexWrap: "nowrap",
        overflowX: "auto",
        overflowY: "hidden",
        WebkitOverflowScrolling: "touch",
        scrollbarWidth: "thin",
        minWidth: 0,
        padding: "10px 4px 12px",
        marginBottom: 4,
        background: T.raised,
        border: `1px solid ${T.borderMuted ?? T.border}`,
        borderRadius: 12,
      }}
    >
      {tabs.map((t) => {
        const isActive = active === t.id;
        const hot = !isActive && (hov === t.id || focusId === t.id);
        return (
          <button
            key={t.id}
            type="button"
            role="tab"
            aria-selected={isActive}
            onClick={() => onChange(t.id)}
            onMouseEnter={() => setHov(t.id)}
            onMouseLeave={() => setHov(null)}
            onFocus={() => setFocusId(t.id)}
            onBlur={() => setFocusId(null)}
            style={{
              padding: "6px 14px",
              display: "inline-flex",
              alignItems: "center",
              gap: 7,
              background: isActive ? T.accentBg : hot ? T.hover : "transparent",
              border: isActive ? `1px solid ${T.accentBorder}` : "1px solid transparent",
              borderRadius: 9999,
              color: isActive ? T.accent : hot ? T.t1 : T.t2,
              fontSize: 14,
              fontWeight: isActive ? 600 : 500,
              cursor: "pointer",
              fontFamily: F.sans,
              transition: "all .12s",
              whiteSpace: "nowrap",
              flexShrink: 0,
              outline: focusId === t.id ? `2px solid ${T.accent}` : "none",
            }}
          >
            {t.icon && <span style={{ display: "flex", color: isActive ? T.accent : T.t3 }}>{t.icon}</span>}
            <span>{t.label}</span>
            {t.count != null && (
              <span
                style={{
                  background: isActive ? `${T.accent}22` : T.surface,
                  border: `1px solid ${isActive ? T.accentBorder : T.border}`,
                  borderRadius: 999,
                  padding: "0 7px",
                  fontSize: 12,
                  fontWeight: 600,
                  color: isActive ? T.accent : T.t2,
                  lineHeight: "18px",
                  minWidth: 20,
                  textAlign: "center",
                }}
              >
                {t.count}
              </span>
            )}
          </button>
        );
      })}
    </div>
  );
}

export function PageHeader({
  T,
  org = "Engine Labs",
  name,
  description,
  actions,
  icon,
}: {
  T: Theme;
  org?: string;
  name: string;
  description?: string;
  actions?: ReactNode;
  icon?: ReactNode;
}) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "flex-start",
        gap: 16,
        paddingBottom: 16,
        borderBottom: `1px solid ${T.border}`,
        marginBottom: 0,
      }}
    >
      <div style={{ minWidth: 0, flex: 1 }}>
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 8,
            fontSize: 20,
            fontWeight: 400,
            marginBottom: description ? 4 : 0,
          }}
        >
          {icon && <span style={{ color: T.t2, display: "flex" }}>{icon}</span>}
          <span style={{ color: T.accent }}>{org}</span>
          <span style={{ color: T.t3 }}>/</span>
          <span style={{ color: T.t1, fontWeight: 600 }}>{name}</span>
          <Badge T={T}>Private</Badge>
        </div>
        {description && <div style={{ color: T.t2, fontSize: 13 }}>{description}</div>}
      </div>
      {actions && <div style={{ display: "flex", gap: 8, flexShrink: 0 }}>{actions}</div>}
    </div>
  );
}
