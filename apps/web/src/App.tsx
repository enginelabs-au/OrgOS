import { useEffect, useMemo, useState } from "react";
import { Btn, F, THEMES } from "@engine-labs/ui";
import styles from "./App.module.css";

const T = THEMES.light;
const CONTACT = "mailto:hello@enginelabs.com.au";
const REPO = "https://github.com/enginelabs-au/OrgOS";

type Section = "home" | "product" | "about" | "contact";

function sectionFromHash(): Section {
  const raw = window.location.hash.replace("#", "").toLowerCase();
  if (raw === "product" || raw === "about" || raw === "contact") return raw;
  return "home";
}

export default function App() {
  const [section, setSection] = useState<Section>(() =>
    typeof window === "undefined" ? "home" : sectionFromHash(),
  );

  useEffect(() => {
    const onHash = () => setSection(sectionFromHash());
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, []);

  const go = (next: Section) => {
    window.location.hash = next === "home" ? "" : next;
    setSection(next);
  };

  const page = useMemo(() => {
    if (section === "product") return <Product />;
    if (section === "about") return <About />;
    if (section === "contact") return <Contact />;
    return <Home onProduct={() => go("product")} />;
  }, [section]);

  return (
    <div className={styles.page} style={{ background: T.pageGradient, color: T.t1, fontFamily: F.sans }}>
      <header className={styles.top} style={{ background: T.nav, borderBottom: `1px solid ${T.border}` }}>
        <a className={styles.wordmark} href="#/" onClick={() => go("home")} style={{ color: T.t1 }}>
          Engine Labs
        </a>
        <nav className={styles.nav} aria-label="Primary">
          <button type="button" className={styles.link} style={{ color: T.navText }} onClick={() => go("product")}>
            Product
          </button>
          <button type="button" className={styles.link} style={{ color: T.navText }} onClick={() => go("about")}>
            About
          </button>
          <button type="button" className={styles.link} style={{ color: T.navText }} onClick={() => go("contact")}>
            Contact
          </button>
        </nav>
      </header>
      <main className={styles.main}>{page}</main>
      <footer className={styles.foot} style={{ borderTop: `1px solid ${T.border}`, color: T.t3 }}>
        <p>Engine Labs is the trading name of Cam Douglas, an Australian sole trader. ABN 13 141 459 638. New South Wales.</p>
        <p>
          <a href={REPO} style={{ color: T.accent }}>
            Source on GitHub
          </a>
          {" · "}
          <a href={CONTACT} style={{ color: T.accent }}>
            hello@enginelabs.com.au
          </a>
        </p>
      </footer>
    </div>
  );
}

function Home({ onProduct }: { onProduct: () => void }) {
  return (
    <section className={styles.hero} style={{ background: T.surface, border: `1px solid ${T.border}`, boxShadow: T.shadowMd }}>
      <p className={styles.kicker} style={{ color: T.t3 }}>
        Company operating system
      </p>
      <h1 style={{ color: T.t1 }}>One website. One product. Governed work for a founder-led practice.</h1>
      <p className={styles.lead} style={{ color: T.t2 }}>
        Engine Labs builds OrgOS: a desktop company OS with an API, a fail-closed worker, and an honest assistant
        control. This site is the single public entry for the company and the product.
      </p>
      <div className={styles.actions}>
        <Btn T={T} variant="primary" onClick={onProduct}>
          See OrgOS
        </Btn>
        <Btn T={T} variant="ghost" onClick={() => {
          window.location.href = CONTACT;
        }}>
          Email Engine Labs
        </Btn>
      </div>
    </section>
  );
}

function Product() {
  return (
    <section className={styles.hero} style={{ background: T.surface, border: `1px solid ${T.border}`, boxShadow: T.shadowMd }}>
      <p className={styles.kicker} style={{ color: T.t3 }}>
        OrgOS
      </p>
      <h1 style={{ color: T.t1 }}>The desktop product lives in this repository.</h1>
      <p className={styles.lead} style={{ color: T.t2 }}>
        Release 1 is the foundation and the development loop: identity, grants, a job ledger, a Tauri shell, and a
        Hermes worker that refuses to start until interception is proven. Hey Engine is present as a control and
        reports unavailable until the runtime is connected. There is no public download yet.
      </p>
      <div className={styles.actions}>
        <Btn T={T} variant="primary" onClick={() => {
          window.location.href = REPO;
        }}>
          Open the repository
        </Btn>
      </div>
    </section>
  );
}

function About() {
  return (
    <section className={styles.hero} style={{ background: T.surface, border: `1px solid ${T.border}`, boxShadow: T.shadowMd }}>
      <p className={styles.kicker} style={{ color: T.t3 }}>
        About
      </p>
      <h1 style={{ color: T.t1 }}>A New South Wales sole trader, building in public where it is safe to.</h1>
      <p className={styles.lead} style={{ color: T.t2 }}>
        Trading name Engine Labs. Entity type Australian sole trader. Public email hello@enginelabs.com.au. Apex
        domain enginelabs.com.au. This page does not list prices; commercial terms stay with the owner until release
        four decisions are recorded.
      </p>
    </section>
  );
}

function Contact() {
  return (
    <section className={styles.hero} style={{ background: T.surface, border: `1px solid ${T.border}`, boxShadow: T.shadowMd }}>
      <p className={styles.kicker} style={{ color: T.t3 }}>
        Contact
      </p>
      <h1 style={{ color: T.t1 }}>Write to hello@enginelabs.com.au</h1>
      <p className={styles.lead} style={{ color: T.t2 }}>
        Use email for briefs and questions. This site does not collect forms, store briefs, or run a recommender.
      </p>
      <div className={styles.actions}>
        <Btn T={T} variant="primary" onClick={() => {
          window.location.href = CONTACT;
        }}>
          Open email
        </Btn>
      </div>
    </section>
  );
}
