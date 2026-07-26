# Source and Evidence Policy

## Purpose

This repository is designed to minimize hallucination, stale guidance, and unsupported claims in AI engineering decisions.

## Source priority

Use sources in this order unless a documented reason requires otherwise:

1. Current official product documentation and API references.
2. Official architecture guidance, well-architected guidance, security baselines, migration guides, and release notes.
3. Official certification study guides and training labs.
4. Official vendor GitHub repositories and samples.
5. Primary research papers and standards.
6. High-quality engineering reports and community explanations.

Community material must not be the sole authority for a production recommendation when an official or primary source exists.

## Vendor priority for project design

1. Microsoft AI-103, Microsoft Foundry, Azure Architecture Center, Azure Well-Architected Framework, and Azure security guidance for Azure implementation.
2. Anthropic documentation for agent architecture, context engineering, tool design, MCP, evaluation, Claude Code, and safety.
3. OpenAI documentation for the Responses API, Agents SDK, structured outputs, evals, safety, and production operations.
4. Google Cloud and AWS primary guidance when the first three do not clearly address the scenario.

## Evidence labels

Every significant recommendation should use one of these labels:

- `official-requirement`: explicitly required by an authoritative source.
- `official-recommendation`: explicitly recommended by an authoritative source.
- `reference-architecture`: demonstrated in an official reference architecture or sample.
- `project-validated`: validated with measured results in a real project.
- `engineering-inference`: reasoned recommendation derived from sources and constraints.
- `experimental`: plausible but not sufficiently validated.
- `deprecated`: no longer recommended or supported.
- `superseded`: replaced by a newer practice, API, or document.

Do not present an `engineering-inference` as a vendor requirement.

## Required metadata

Fast-changing pages should begin with front matter similar to:

```yaml
---
status: current
last_verified: 2026-07-27
source_priority: official
vendors:
  - microsoft
review_frequency: monthly
applies_to:
  - production
  - ai-103
---
```

Recommended status values:

- `current`
- `preview`
- `experimental`
- `project-validated`
- `deprecated`
- `superseded`
- `unverified`

## Citation rules

- Link the exact official page supporting each changeable technical claim.
- Record the date the source was checked.
- Prefer release notes or migration guides for lifecycle changes.
- Clearly state when guidance is inferred rather than documented.
- Do not copy large sections of vendor documentation; summarize and link.

## Conflict resolution

When sources conflict:

1. Prefer the more recent official source.
2. Prefer product documentation over older course material.
3. Prefer generally available guidance over preview guidance for production systems.
4. Document the conflict and the decision in an ADR when it affects architecture.

## Failure mode

When evidence is insufficient, the correct result is:

> No sufficiently current and authoritative evidence was found.

Do not fill the gap with an unsupported answer.