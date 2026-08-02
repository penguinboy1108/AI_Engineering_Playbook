# AI Engineering Playbook

A production-first, source-grounded engineering playbook for designing, implementing, evaluating, securing, and operating AI applications and agents.

## Source priority

1. Current official Microsoft documentation, especially Microsoft Foundry, Azure Architecture Center, Azure Well-Architected Framework, and the AI-103 study guide.
2. Current official Anthropic documentation for Claude, Claude Code, tools, MCP, context engineering, evaluation, and safety.
3. Current official OpenAI documentation for the Responses API, Agents SDK, structured outputs, evaluation, safety, and production operations.
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
- Convert private project evidence into public guidance only after sanitisation and publication review.

## Repository map

The playbook is organised by engineering lifecycle rather than by vendor. See [PLAYBOOK_MAP.md](PLAYBOOK_MAP.md) for the planned structure and initial priorities.

Key governance and authoring files:

- [GOVERNANCE.md](GOVERNANCE.md)
- [CHANGELOG.md](CHANGELOG.md)
- [DEPRECATIONS.md](DEPRECATIONS.md)
- [Playbook entry template](templates/playbook-entry.md)
- [Case study template](templates/case-study.md)
- [Pattern template](templates/pattern.md)
- [Weekly digest template](templates/weekly-digest.md)
- [ADR template](decisions/ADR-template.md)

## First project-derived content

- [Case study: Bounded AI Workflow for Enterprise Accounts Payable Automation](09-case-studies/enterprise-accounts-payable-automation.md)
- [Pattern: Bounded Document Automation Workflow](10-patterns/bounded-document-automation-workflow.md)
- [ADR-001: Use a Bounded Workflow Over an Autonomous Agent](decisions/ADR-001-use-bounded-workflow-over-autonomous-agent.md)

The case study is a sanitised public abstraction. Detailed project evidence remains in the private `AI_Engineering_Worklog` repository.

## Knowledge flow

```text
Private project worklog
        ↓
Sanitisation and evidence review
        ↓
Public case study
        ↓
Reusable pattern / ADR / anti-pattern
        ↓
Future project design and evaluation
```

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

The repository is in its bootstrap phase. Governance, authoring templates, and the first project-derived case study and architecture pattern are being established before wider AI-103, Anthropic, and OpenAI topic coverage is added.
