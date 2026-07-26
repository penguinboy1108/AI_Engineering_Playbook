# AI Engineering Playbook

A production-first, source-grounded engineering playbook for designing, implementing, evaluating, securing, and operating AI applications and agents.

## Source priority

1. Current official Microsoft documentation, especially Microsoft Foundry, Azure Architecture Center, Azure Well-Architected Framework, and the AI-103 study guide.
2. Current official Anthropic documentation for Claude, Claude Code, tools, MCP, context engineering, evaluation, and safety.
3. Current official OpenAI documentation for the Responses API, Agents SDK, structured outputs, evals, safety, and production operations.
4. Google Cloud and AWS primary guidance when the first three sources do not clearly cover the topic.
5. High-quality community material only as secondary explanation or implementation evidence.

See [SOURCE_POLICY.md](SOURCE_POLICY.md) for evidence labels, citation rules, conflict handling, and abstention requirements.

## Core principles

- Production readiness over demo-only designs.
- Prefer deterministic workflows where they are sufficient; introduce agents only where adaptive reasoning adds measurable value.
- Treat security, identity, human approval, evaluation, observability, reliability, and cost control as first-class requirements.
- Separate documented vendor guidance from project-specific engineering judgment.
- Mark preview, experimental, deprecated, superseded, and unverified content explicitly.
- Every fast-changing technical claim should include a primary source and a `last_verified` date.

## Repository map

The playbook is organized by engineering lifecycle rather than by vendor. See [PLAYBOOK_MAP.md](PLAYBOOK_MAP.md) for the planned structure and initial priorities.

Key governance files:

- [GOVERNANCE.md](GOVERNANCE.md)
- [CHANGELOG.md](CHANGELOG.md)
- [DEPRECATIONS.md](DEPRECATIONS.md)
- [Playbook entry template](templates/playbook-entry.md)
- [Weekly digest template](templates/weekly-digest.md)
- [ADR template](decisions/ADR-template.md)

## Repository workflow

Weekly research updates are proposed through draft pull requests. Automated updates must not merge directly into `main`.

```text
Official and primary-source research
                ↓
Classify added / changed / superseded / deprecated
                ↓
Create or update weekly digest
                ↓
Update durable playbook guidance where justified
                ↓
Update changelog and deprecation registry
                ↓
Open draft pull request for human review
```

## Current status

The repository is in its bootstrap phase. Initial governance and templates are being established before vendor-specific technical guidance is added.