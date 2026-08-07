# Source and Evidence Policy

## Purpose

This repository is designed to minimise hallucination, stale guidance, unsupported claims, and accidental promotion of project observations into universal engineering rules.

The policy applies both to human authors and to AI systems retrieving or modifying repository content.

## Source priority

Use sources in this order unless a documented reason requires otherwise:

1. Current official product documentation and API references.
2. Official architecture guidance, well-architected guidance, security baselines, migration guides, lifecycle notices, and release notes.
3. Official certification study guides and training labs.
4. Official vendor GitHub repositories and samples.
5. Primary research papers, standards, and specifications.
6. High-quality engineering reports and community explanations.

Community material must not be the sole authority for a production recommendation when an official or primary source exists.

## Vendor priority for project design

1. Microsoft Foundry, Azure Architecture Center, Azure Well-Architected Framework, Azure security guidance, and the current AI-103 study guide for Azure implementation and learning scope.
2. Anthropic documentation for agent architecture, context engineering, tool design, MCP, evaluation, Claude Code, and safety.
3. OpenAI documentation for current APIs, Agents SDK, structured outputs, evaluation, safety, and production operations.
4. Google Cloud and AWS primary guidance when the first three do not clearly address the scenario.

Vendor priority does not override recency or relevance. A current product page outranks an older certification module or historical engineering post when they conflict about present behaviour.

## Evidence labels

Every significant recommendation should use one or more of these labels:

- `official`: explicitly documented by an authoritative vendor or standards source.
- `reference-architecture`: demonstrated in an official architecture or supported sample.
- `project-validated`: measured in a real project with stated dataset and scope limitations.
- `official-plus-project-evidence`: official guidance reinforced by sanitised project evidence.
- `engineering-inference`: a reasoned recommendation derived from sources and constraints.
- `experimental`: plausible but not sufficiently validated.
- `unverified`: recorded for follow-up but not suitable for default grounding.

Do not present an `engineering-inference` as a vendor requirement. Do not present `project-validated` results as a universal benchmark.

## Separate metadata dimensions

Do not overload one `status` field with document validity, evidence strength, and product lifecycle. New or substantially revised pages should use these dimensions in `catalog.yaml` and, where practical, in front matter.

### Content type

```text
guide | pattern | anti-pattern | case-study | adr | digest | certification-map
```

### Document status

```text
draft | current | deprecated | superseded | archived
```

### Evidence status

```text
official | reference-architecture | project-validated |
official-plus-project-evidence | engineering-inference |
experimental | unverified
```

### Product lifecycle

```text
ga | preview | experimental | retirement-announced |
deprecated | retired | not-applicable | mixed
```

Historical files may temporarily retain legacy front-matter values such as `validated`, `accepted`, or `validated-project-case-study`. `catalog.yaml` is the retrieval source of truth during migration.

## Required machine metadata

Every default-grounding page must have an entry in `catalog.yaml` with at least:

```yaml
id: stable-kebab-case-id
path: path/to/page.md
title: Page title
content_type: guide
document_status: current
evidence_status: official
product_lifecycle: ga
last_verified: 2026-08-03
next_review_due: 2026-09-03
review_frequency: monthly
metadata_source: front-matter
canonical_for:
  - stable-topic-id
retrieval:
  default_grounding: true
  priority: 90
  role: primary
topics:
  - topic
supersedes: []
superseded_by: []
```

The catalog schema is defined in `schema/catalog.schema.json`.

## Canonical content rules

- A canonical topic must have exactly one current, default-grounding page with `retrieval.role: primary`.
- ADRs may use `decision-context` and case studies may use `supporting-evidence` for the same canonical topic.
- Weekly digests must use `default_grounding: false` and `recent-change-record`.
- Deprecated, superseded, archived, experimental, and unverified content must not be default grounding.
- A deprecated or superseded page must identify its replacement.

## Citation rules

- Link the exact official page supporting each changeable technical claim.
- Record the date each source was checked.
- Prefer lifecycle notices, release notes, or migration guides for retirement and compatibility claims.
- Clearly state when guidance is inferred rather than documented.
- Do not copy large sections of vendor documentation; summarise and link.
- Pin code-reading references to a commit SHA when behaviour at a specific point in time matters.
- Do not cite a certification guide as the sole authority for current production behaviour.

For pages with several important sources, prefer a source table:

| ID | Source | Evidence | Supports | Checked on | Lifecycle/version |
|---|---|---|---|---|---|
| SRC-001 | Exact official page | official | Specific claim | YYYY-MM-DD | GA / version |

The body may refer to `[SRC-001]` so the supported claim is explicit.

## Fast-changing claims

The following always require current official verification before use in a production answer or durable update:

- API, SDK, CLI, model, and framework behaviour;
- default models and model settings;
- preview, GA, deprecation, retirement, and migration status;
- service names and product boundaries;
- pricing, quotas, rate limits, regional availability, and support matrices;
- certification objectives and exam scope;
- security features and identity capabilities.

A page-level `last_verified` date does not prove that every source was checked on that date. Authors should record per-source dates when a page depends on multiple changeable claims.

## Conflict resolution

When sources conflict:

1. Prefer the more recent official source.
2. Prefer current product documentation over older course material.
3. Prefer generally available guidance over preview guidance for production systems.
4. Distinguish product behaviour from an engineering recommendation.
5. Record the conflict and decision in an ADR when it affects architecture.
6. Propose a repository correction rather than silently ignoring stale content.

## Lifecycle claims

Do not add an item to `DEPRECATIONS.md` based only on a community discussion, search snippet, or indirect statement. Require an official lifecycle notice, official product documentation, or an official migration guide that clearly identifies the affected product and date.

When official evidence is not available, record the item as `needs-validation` in a digest or pull request rather than as an active deprecation.

## Failure mode

When evidence is insufficient, the correct result is:

> No sufficiently current and authoritative evidence was found.

Do not fill the gap with an unsupported answer.

## Validation

Run:

```bash
python scripts/validate_content.py
```

The initial validator checks machine metadata, canonical roles, paths, verification-date consistency, digest exclusion, internal links, replacement metadata, and obvious secret material. Human review remains required for source quality, interpretation, publication safety, and current official verification.
