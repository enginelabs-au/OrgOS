-- Engine Labs application schema (Postgres). Unit tests use sqlite/file store.
-- Application role is not superuser and cannot bypass RLS (F-SEC-03).
-- Audit tables are INSERT-only for the application role (F-SEC-15).
-- Request path must SET LOCAL the principal (engine.set_principal).

CREATE SCHEMA IF NOT EXISTS engine;

CREATE ROLE engine_app NOLOGIN NOSUPERUSER NOBYPASSRLS NOCREATEDB NOCREATEROLE;

CREATE TABLE IF NOT EXISTS engine.principals (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  kind TEXT NOT NULL CHECK (kind IN ('human', 'agent')),
  seat_id TEXT,
  grant_version INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS engine.grants (
  id TEXT PRIMARY KEY,
  principal_id TEXT NOT NULL REFERENCES engine.principals (id),
  tenant_id TEXT NOT NULL,
  grant_class TEXT NOT NULL,
  scope TEXT NOT NULL,
  CONSTRAINT agent_no_approval CHECK (
    grant_class NOT LIKE 'approval.%'
    OR (SELECT kind FROM engine.principals WHERE id = principal_id) <> 'agent'
  )
);

CREATE TABLE IF NOT EXISTS engine.entitlements (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  principal_id TEXT NOT NULL,
  feature TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS engine.registry (
  capability_id TEXT PRIMARY KEY,
  domain_id TEXT NOT NULL,
  payload JSONB NOT NULL
);

CREATE TABLE IF NOT EXISTS engine.work_items (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  title TEXT NOT NULL,
  owner_principal_id TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS engine.jobs (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  status TEXT NOT NULL,
  purpose TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS engine.audit_records (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  actor_principal_id TEXT NOT NULL,
  action TEXT NOT NULL,
  target_type TEXT NOT NULL,
  target_id TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS engine.usage_events (
  id TEXT PRIMARY KEY,
  tenant_id TEXT NOT NULL,
  payload JSONB NOT NULL
);

ALTER TABLE engine.principals ENABLE ROW LEVEL SECURITY;
ALTER TABLE engine.grants ENABLE ROW LEVEL SECURITY;
ALTER TABLE engine.entitlements ENABLE ROW LEVEL SECURITY;
ALTER TABLE engine.work_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE engine.jobs ENABLE ROW LEVEL SECURITY;
ALTER TABLE engine.audit_records ENABLE ROW LEVEL SECURITY;
ALTER TABLE engine.usage_events ENABLE ROW LEVEL SECURITY;

CREATE OR REPLACE FUNCTION engine.set_principal(p_principal TEXT)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
  PERFORM set_config('engine.principal_id', p_principal, true);
END;
$$;

CREATE POLICY principals_isolation ON engine.principals
  USING (id = current_setting('engine.principal_id', true)
         OR tenant_id = (SELECT tenant_id FROM engine.principals p WHERE p.id = current_setting('engine.principal_id', true)));

CREATE POLICY work_items_isolation ON engine.work_items
  USING (tenant_id = (SELECT tenant_id FROM engine.principals p WHERE p.id = current_setting('engine.principal_id', true)));

CREATE POLICY jobs_isolation ON engine.jobs
  USING (tenant_id = (SELECT tenant_id FROM engine.principals p WHERE p.id = current_setting('engine.principal_id', true)));

CREATE POLICY audit_insert_only ON engine.audit_records
  FOR SELECT
  USING (tenant_id = (SELECT tenant_id FROM engine.principals p WHERE p.id = current_setting('engine.principal_id', true)));

CREATE POLICY audit_insert ON engine.audit_records
  FOR INSERT
  WITH CHECK (true);

REVOKE ALL ON engine.audit_records FROM engine_app;
GRANT INSERT, SELECT ON engine.audit_records TO engine_app;
-- UPDATE and DELETE are intentionally not granted.

GRANT USAGE ON SCHEMA engine TO engine_app;
GRANT SELECT, INSERT, UPDATE ON engine.principals, engine.grants, engine.entitlements,
  engine.registry, engine.work_items, engine.jobs, engine.usage_events TO engine_app;

COMMENT ON FUNCTION engine.set_principal(TEXT) IS
  'Call as SET LOCAL via SELECT engine.set_principal(...) at the start of each request.';
