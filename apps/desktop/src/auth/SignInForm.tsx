import { useState } from "react";
import { Btn, F, Field, Input, type Theme } from "@engine-labs/ui";
import { signIn } from "../api/client";
import { storeSession } from "./keychain";

export function SignInForm({ T, onSignedIn }: { T: Theme; onSignedIn: () => void }) {
  const [email, setEmail] = useState("");
  const [strongFactor, setStrongFactor] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  const submit = async () => {
    setError(null);
    setBusy(true);
    try {
      const result = await signIn(email.trim(), strongFactor);
      const token = result.access_token || result.accessToken;
      if (!token) {
        setError("Sign-in did not return a session. Try again, or check that the API is running.");
        return;
      }
      await storeSession({
        accessToken: token,
        grantVersion: result.grant_version || result.grantVersion,
      });
      onSignedIn();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Sign-in did not succeed.");
    } finally {
      setBusy(false);
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: T.pageGradient,
        fontFamily: F.sans,
        padding: 24,
      }}
    >
      <form
        onSubmit={(e) => {
          e.preventDefault();
          void submit();
        }}
        style={{
          width: "100%",
          maxWidth: 400,
          background: T.surface,
          border: `1px solid ${T.border}`,
          borderRadius: 12,
          padding: 28,
          boxShadow: T.shadowMd,
        }}
      >
        <div style={{ fontFamily: F.sans, fontSize: 15, fontWeight: 700, color: T.t1, marginBottom: 4 }}>Engine Labs</div>
        <div style={{ color: T.t2, fontSize: 13, marginBottom: 20 }}>Sign in with your email and strong factor.</div>
        <Field T={T} label="Email" htmlFor="signin-email">
          <Input
            T={T}
            id="signin-email"
            name="email"
            type="email"
            autoComplete="username"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </Field>
        <Field
          T={T}
          label="Strong factor"
          htmlFor="signin-factor"
          hint="Authenticator code or the factor your organisation requires. There is no guest or demo sign-in."
        >
          <Input
            T={T}
            id="signin-factor"
            name="strong-factor"
            type="password"
            autoComplete="current-password"
            required
            value={strongFactor}
            onChange={(e) => setStrongFactor(e.target.value)}
          />
        </Field>
        {error && (
          <div role="alert" style={{ color: T.red, fontSize: 13, marginBottom: 12 }}>
            {error}
          </div>
        )}
        <Btn T={T} variant="primary" type="submit" full disabled={busy}>
          {busy ? "Signing in…" : "Sign in"}
        </Btn>
      </form>
    </div>
  );
}
