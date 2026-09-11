import { Btn, F, type Theme } from "@engine-labs/ui";

export function ErrorState({
  T,
  title = "This page could not be loaded",
  body,
  onRetry,
}: {
  T: Theme;
  title?: string;
  body: string;
  onRetry?: () => void;
}) {
  return (
    <div
      role="alert"
      style={{
        padding: 28,
        border: `1px solid ${T.redBorder}`,
        borderRadius: 10,
        background: T.redBg,
        fontFamily: F.sans,
      }}
    >
      <div style={{ color: T.t1, fontSize: 15, fontWeight: 600, marginBottom: 6 }}>{title}</div>
      <div style={{ color: T.t2, fontSize: 13, lineHeight: 1.5, marginBottom: onRetry ? 12 : 0 }}>{body}</div>
      {onRetry && (
        <Btn T={T} onClick={onRetry}>
          Try again
        </Btn>
      )}
    </div>
  );
}
