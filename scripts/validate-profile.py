#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
relationships = json.loads((root / "repository-relationships.json").read_text())
expected = [
    ".github",
    "postgres-forward-rollback",
    "cockroach-forward-rollback",
    "cross-engine-compatibility",
    "concurrent-migrator-lock",
    "failure-injection-atomicity",
    "schema-drift-detection",
    "cli-mcp-contract",
]
observed = [row["name"] for row in relationships["repositories"]]
assert observed == expected, (observed, expected)
assert relationships["production"]["commit"] == "21eb846e356b2a5aff068b21e77903e6cca50452"
for path in ["profile/README.md", "SECURITY.md", "repository-relationships.json", "workflow-templates/dpm-certification.yml", "workflow-templates/dpm-certification.properties.json"]:
    assert (root / path).is_file(), path
print("organization profile contract validated")
