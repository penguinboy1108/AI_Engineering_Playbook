# Deprecation and Supersession Registry

Use this registry to prevent outdated APIs, SDKs, models, services, and design patterns from remaining active grounding material.

## Evidence threshold

Add an active entry only when an official lifecycle notice, official product page, official release note, or official migration guide clearly identifies:

- the affected product, API, SDK, model, service, or pattern;
- the lifecycle status;
- the effective or retirement date when applicable;
- the supported replacement or migration path when available.

A community discussion, search result, indirect statement, or missing UI element may trigger investigation but is not sufficient evidence for an active deprecation entry.

Unconfirmed lifecycle information belongs in a weekly digest or pull request under `needs-validation`.

## Entry template

```markdown
## Item name

- Registry ID:
- Status: deprecated | superseded | retirement-announced | retired
- Vendor:
- First recorded:
- Effective or retirement date:
- Last verified:
- Replacement:
- Official source:
- Migration impact:
- Affected playbook pages:
- Catalog entries updated:
- Notes:
```

## Required repository updates

When an entry is added:

1. update affected pages and their lifecycle wording;
2. update `catalog.yaml` document or product lifecycle fields;
3. set `superseded_by` where durable guidance was replaced;
4. add migration and rollback considerations;
5. update `CHANGELOG.md`;
6. add or update a retrieval eval if stale guidance could still be selected.

## Active entries

No entries have been recorded yet.

## Investigations awaiting official evidence

None.
