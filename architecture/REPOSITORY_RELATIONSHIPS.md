# `declarative-migrations-test` repository relationships

Generated from reviewed policy and the current **public** repository inventory.

- Public repositories declared: **13**
- Private repository names withheld: **13**
- Relationship edges: **13**

## Repository roles

| Repository | Role | Lifecycle |
|---|---|---|
| [`.github`](https://github.com/declarative-migrations-test/.github) | `organization_governance` | `active` |
| [`cli-mcp-contract`](https://github.com/declarative-migrations-test/cli-mcp-contract) | `interfaces` | `active` |
| [`schema-drift-detection`](https://github.com/declarative-migrations-test/schema-drift-detection) | `interfaces` | `active` |
| [`cli-install-e2e`](https://github.com/declarative-migrations-test/cli-install-e2e) | `end_to_end_tests` | `active` |
| [`data-preservation-e2e`](https://github.com/declarative-migrations-test/data-preservation-e2e) | `end_to_end_tests` | `active` |
| [`fuzz-property-e2e`](https://github.com/declarative-migrations-test/fuzz-property-e2e) | `end_to_end_tests` | `active` |
| [`homebrew-install-e2e`](https://github.com/declarative-migrations-test/homebrew-install-e2e) | `end_to_end_tests` | `active` |
| [`idempotent-replay-e2e`](https://github.com/declarative-migrations-test/idempotent-replay-e2e) | `end_to_end_tests` | `active` |
| [`cockroach-forward-rollback`](https://github.com/declarative-migrations-test/cockroach-forward-rollback) | `uncategorized` | `active` |
| [`concurrent-migrator-lock`](https://github.com/declarative-migrations-test/concurrent-migrator-lock) | `uncategorized` | `active` |
| [`cross-engine-compatibility`](https://github.com/declarative-migrations-test/cross-engine-compatibility) | `uncategorized` | `active` |
| [`failure-injection-atomicity`](https://github.com/declarative-migrations-test/failure-injection-atomicity) | `uncategorized` | `active` |
| [`postgres-forward-rollback`](https://github.com/declarative-migrations-test/postgres-forward-rollback) | `uncategorized` | `active` |

## Declared edges

| From | Relationship | To | Status/basis |
|---|---|---|---|
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/cli-install-e2e` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/cli-mcp-contract` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/cockroach-forward-rollback` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/concurrent-migrator-lock` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/cross-engine-compatibility` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/data-preservation-e2e` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/failure-injection-atomicity` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/fuzz-property-e2e` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/homebrew-install-e2e` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/idempotent-replay-e2e` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/postgres-forward-rollback` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `declarative-migrations-test/.github` | `governs` | `declarative-migrations-test/schema-drift-detection` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `organization://declarative-migrations-test` | `packaged_via` | `platform://zed-pkg` | `platform-default` / `platform-policy`: Zed resolves artifacts while submodules compose editable source |

## Composition, service, and observability contract

Git submodules compose editable source; Zed packages resolve packages/artifacts; dual-managed commits must match. Production deploys immutable image digests, not runtime source builds. Cross-service access uses APIs/SDKs/events rather than another service database. MCP uses the product API/SDK. Services emit OpenTelemetry traces, bounded metrics, and correlated structured logs.

## Privacy boundary

This public registry deliberately omits private repository names and edges; the count above makes the boundary explicit.
