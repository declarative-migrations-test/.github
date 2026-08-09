#!/usr/bin/env bash
set -euo pipefail
: "${DPM_TEST_DATABASE_URL:?DPM_TEST_DATABASE_URL is required}"
psql "$DPM_TEST_DATABASE_URL" -v ON_ERROR_STOP=1 <<'SQL'
DROP SCHEMA IF EXISTS product CASCADE;
DROP SCHEMA IF EXISTS web_state CASCADE;
DROP ROLE IF EXISTS declmig_web_ro;
DROP ROLE IF EXISTS declmig_web_state_rw;
DROP ROLE IF EXISTS declmig_api_rw;
DROP ROLE IF EXISTS declmig_migrator;
CREATE ROLE declmig_web_ro NOLOGIN;
CREATE ROLE declmig_web_state_rw NOLOGIN;
CREATE ROLE declmig_api_rw NOLOGIN;
CREATE ROLE declmig_migrator NOLOGIN;
CREATE SCHEMA product AUTHORIZATION declmig_migrator;
CREATE SCHEMA web_state AUTHORIZATION declmig_migrator;
CREATE TABLE product.widgets (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, name text NOT NULL);
CREATE TABLE web_state.sessions (id text PRIMARY KEY, payload jsonb NOT NULL);
GRANT USAGE ON SCHEMA product TO declmig_web_ro, declmig_api_rw;
GRANT SELECT ON ALL TABLES IN SCHEMA product TO declmig_web_ro;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA product TO declmig_api_rw;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA product TO declmig_api_rw;
GRANT USAGE ON SCHEMA web_state TO declmig_web_state_rw;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA web_state TO declmig_web_state_rw;
SET ROLE declmig_web_ro; SELECT count(*) FROM product.widgets; RESET ROLE;
SET ROLE declmig_api_rw; INSERT INTO product.widgets(name) VALUES ('api-owned-write'); RESET ROLE;
SET ROLE declmig_web_state_rw; INSERT INTO web_state.sessions(id,payload) VALUES ('synthetic','{}'); RESET ROLE;
SET ROLE declmig_migrator; CREATE TABLE product.migration_probe (id integer PRIMARY KEY); RESET ROLE;
SQL
expect_denied() {
  local label="$1" sql="$2"
  if psql "$DPM_TEST_DATABASE_URL" -v ON_ERROR_STOP=1 -c "$sql" >/tmp/declmig.out 2>/tmp/declmig.err; then
    echo "unexpectedly allowed: $label" >&2
    exit 1
  fi
  echo "denied as expected: $label"
}
expect_denied 'web product write' "SET ROLE declmig_web_ro; INSERT INTO product.widgets(name) VALUES ('forbidden');"
expect_denied 'web DDL' "SET ROLE declmig_web_ro; CREATE TABLE product.forbidden_web_ddl(id int);"
expect_denied 'web-state product write' "SET ROLE declmig_web_state_rw; INSERT INTO product.widgets(name) VALUES ('forbidden');"
expect_denied 'api DDL' "SET ROLE declmig_api_rw; CREATE TABLE product.forbidden_api_ddl(id int);"
