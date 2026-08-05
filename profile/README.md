# declarative-migrations-test

Independent acceptance organization for **declarative-migrations**.

Forward/rollback, engine compatibility, locking, drift, failure atomicity, CLI, and MCP migration certification.

## Portfolio

| Repository | Class | Readiness | Primary dependency path |
|---|---|---|---|
| `postgres-forward-rollback` | database conformance | `ready` | `matrix` |
| `cockroach-forward-rollback` | database conformance | `ready` | `matrix` |
| `cross-engine-compatibility` | database conformance | `ready` | `matrix` |
| `concurrent-migrator-lock` | chaos/fault injection | `ready` | `matrix` |
| `failure-injection-atomicity` | chaos/fault injection | `ready` | `matrix` |
| `schema-drift-detection` | database conformance | `ready` | `matrix` |
| `cli-mcp-contract` | MCP contract | `ready` | `matrix` |

Pull requests run deterministic harness checks. Emulators, desktop matrices, live APIs/providers, databases, chaos, scale, and soaks are scheduled/manual. Missing upstreams or credentials are blocked readiness—not false passes or product regressions.
