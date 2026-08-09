# `declarative-migrations-test/declmig-e2e`

Status on 2026-08-09: the target repository is not yet provisioned. This policy repository holds the reviewed bootstrap tree and factory entry until an authorized repository-creation path is available.

## Independent role

The test organization is a hostile consumer, not an extension of the production release trust domain. `declmig-e2e` consumes exact production commits, uses synthetic fixtures and ephemeral databases, and emits immutable evidence. It never writes code back to production and never promotes a mutable branch, tag, package, action, or container reference.

The orchestrator complements, rather than replaces, focused repositories such as `concurrent-migrator-lock`, `postgres-forward-rollback`, `cockroach-forward-rollback`, `schema-drift-detection`, `failure-injection-atomicity`, and `cli-mcp-contract`. It binds their evidence to one source SHA and enforces a common classification vocabulary.

## Required scenarios

- PostgreSQL 16 and 17 convergence, repeated apply, CLI lifecycle, lease ownership, stale reviewed-plan rejection, and killed-owner recovery;
- CockroachDB 25.2.4 convergence and interruption recovery;
- web read-only product identity, API product read/write identity, isolated web-state identity, and migrator-only DDL;
- exact Zed-package version/digest contract for `*-lib-core` consumers;
- deterministic evidence including harness SHA, source SHA, engine, scenario, result, classification, and artifact SHA-256 digests.

`blocked-dependency` is an explicit non-pass result. Protected private MCP parity may be blocked on credentials without weakening public core certification.
