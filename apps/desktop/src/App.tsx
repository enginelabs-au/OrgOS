import { useCallback, useEffect, useMemo, useState } from "react";
import {
  Briefcase,
  Btn,
  F,
  HeyEngineButton,
  Home,
  Plug,
  PrimaryNavTabs,
  SettingsIcon,
  THEMES,
  useViewport,
  Zap,
  type ThemeKey,
} from "@engine-labs/ui";
import styles from "./App.module.css";
import { AssistantPanel } from "./assistant/AssistantPanel";
import { SignInForm } from "./auth/SignInForm";
import { clearSession, readSession } from "./auth/keychain";
import { StatusBar } from "./chrome/StatusBar";
import { Wordmark } from "./chrome/Wordmark";
import { ConnectionsView } from "./views/ConnectionsView";
import { HomeView } from "./views/HomeView";
import { RunsView } from "./views/RunsView";
import { SettingsView } from "./views/SettingsView";
import { WorkView } from "./views/WorkView";

const TABS = [
  { id: "home", label: "Home", icon: <Home size={16} /> },
  { id: "work", label: "Work", icon: <Briefcase size={16} /> },
  { id: "runs", label: "Runs", icon: <Zap size={16} /> },
  { id: "connections", label: "Connections", icon: <Plug size={16} /> },
  { id: "settings", label: "Settings", icon: <SettingsIcon size={16} /> },
];

export default function App() {
  const [themeKey, setThemeKey] = useState<ThemeKey>("light");
  const T = useMemo(() => THEMES[themeKey], [themeKey]);
  const { isMobile } = useViewport();
  const [signedIn, setSignedIn] = useState(false);
  const [ready, setReady] = useState(false);
  const [tab, setTab] = useState("home");
  const [assistantOpen, setAssistantOpen] = useState(false);
  const [railOpen, setRailOpen] = useState(true);

  useEffect(() => {
    void readSession().then((session) => {
      setSignedIn(Boolean(session?.accessToken));
      setReady(true);
    });
  }, []);

  const signOut = useCallback(async () => {
    await clearSession();
    setSignedIn(false);
    setAssistantOpen(false);
  }, []);

  const openAssistant = useCallback(() => setAssistantOpen(true), []);

  if (!ready) {
    return (
      <div style={{ minHeight: "100vh", background: T.canvas, color: T.t2, fontFamily: F.sans, padding: 24 }}>
        Starting Engine Labs…
      </div>
    );
  }

  if (!signedIn) {
    return <SignInForm T={T} onSignedIn={() => setSignedIn(true)} />;
  }

  return (
    <div className={styles.shell} style={{ background: T.pageGradient, color: T.t1, fontFamily: F.sans }}>
      <header className={styles.top} style={{ background: T.nav, borderBottom: `1px solid ${T.border}` }}>
        <Btn T={T} variant="ghost" small onClick={() => setRailOpen((v) => !v)}>
          {railOpen ? "Hide rail" : "Show rail"}
        </Btn>
        <Wordmark T={T} />
        <div className={styles.spacer} />
        <HeyEngineButton T={T} onOpenAssistant={openAssistant} />
        <Btn T={T} variant="ghost" small onClick={() => void signOut()}>
          Sign out
        </Btn>
      </header>
      <PrimaryNavTabs T={T} tabs={TABS} active={tab} onChange={setTab} isMobile={isMobile} />
      <main className={styles.main} style={{ background: T.canvas }}>
        {tab === "home" && <HomeView T={T} railOpen={railOpen} />}
        {tab === "work" && <WorkView T={T} />}
        {tab === "runs" && <RunsView T={T} />}
        {tab === "connections" && <ConnectionsView T={T} />}
        {tab === "settings" && <SettingsView T={T} themeKey={themeKey} onTheme={setThemeKey} />}
      </main>
      <StatusBar T={T} />
      <AssistantPanel T={T} open={assistantOpen} onClose={() => setAssistantOpen(false)} />
    </div>
  );
}
