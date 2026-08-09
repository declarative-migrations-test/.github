# declmig-e2e independent test bootstrap

This tree is ready to become `declarative-migrations-test/declmig-e2e`.

It is the canonical hostile-consumer orchestrator for exact production revisions. Pull-request CI validates pins and contracts without credentials. Scheduled/manual lanes run PostgreSQL 16/17, CockroachDB 25.2.4, advisory-lease, stale-plan, convergence, and least-privilege checks, then emit source-bound evidence.

Current exact production input: `declarative-migrations/declarative-postgres-migrate.rs@b829384df970e3b9415b566ef9d87511bdc163c7`.
