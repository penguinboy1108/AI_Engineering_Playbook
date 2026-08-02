# AI Engineering Playbook

A production-first, source-grounded engineering playbook for designing, implementing, evaluating, securing, and operating AI applications and agents.

The primary use case is practical problem solving: when a real project becomes difficult, an AI assistant can retrieve current canonical guidance, accepted decisions, and sanitised project evidence from this repository and explain the result in Simplified Chinese.

## Start here

- [Agent retrieval and authoring contract](AGENTS.md)
- [How to use this repository with GPT](GPT_USAGE.md)
- [Machine-readable knowledge catalog](catalog.yaml)
- [Source and evidence policy](SOURCE_POLICY.md)
- [Repository governance](GOVERNANCE.md)
- [Repository map](PLAYBOOK_MAP.md)
- [Chinese terminology glossary](GLOSSARY.zh-CN.md)

## Source priority

1. Current official product documentation and API references.
2. Official architecture, security, migration, lifecycle, and well-architected guidance.
3. Official certification study guides and training labs.
4. Official vendor repositories and samples.
5. Primary research papers and standards.
6. High-quality community material as secondary explanation or implementation evidence.

For Azure implementation, prioritise current Microsoft Foundry, Azure Architecture Center, Azure Well-Architected Framework, security guidance, and AI-103 scope. Use current Anthropic guidance for agent architecture, context, tools, MCP, evaluation, and safety. Use current OpenAI guidance for APIs, Agents SDK, structured outputs, evaluation, safety, and production operations.

See [SOURCE_POLICY.md](SOURCE_POLICY.md) for evidence labels, citation rules, conflict handling, and abstention requirements.

## Core principles

- Production readiness over demo-only designs.
- Prefer deterministic workflows where they are sufficient; introduce agents only where adaptive reasoning adds measurable value.
- Treat security, identity, human approval, evaluation, observability, reliability, and cost as first-class requirements.
- Separate documented vendor guidance from project-specific evidence and engineering inference.
- Mark preview, experimental, deprecated, superseded, archived, and unverified content explicitly.
- Every fast-changing claim must include a primary source and a `last_verified` date.
- Convert private project evidence into public guidance only after sanitisation and publication review.
- A plausible answer without retrieved evidence is not a playbook-grounded answer.

## Knowledge layers

```text
Current official guidance
        +
Sanitised project evidence
        ↓
Case study
        ↓
Reusable pattern / ADR / anti-pattern
        ↓
Canonical production guide or reference architecture
```

A weekly digest is a time-stamped research record. It is not automatically a permanent recommendation. Durable guidance is promoted only after evidence review.

## Retrieval model

`catalog.yaml` is the machine-readable index. Each entry records:

- content type;
- document and evidence status;
- product lifecycle;
- verification and review dates;
- canonical topics;
- default-grounding eligibility;
- retrieval priority and role;
- related or superseding content.

The default retrieval order is:

```text
canonical guide or pattern
    -> accepted ADR
    -> supporting case study
    -> weekly digest only for recent-change questions
```

Deprecated, superseded, archived, experimental, and unverified content is excluded from default grounding.

## Current content

### Practice guides

- [Specification-Driven AI Coding and Harness Engineering](docs/workflows/specification-driven-ai-coding.md)
- [Agent Capability Containment](07-security/agent-capability-containment.md)
- [SDK Version and Default Control](08-production/sdk-version-and-default-control.md)

### Project-derived knowledge

- [Case study: Bounded AI Workflow for Enterprise Accounts Payable Automation](09-case-studies/enterprise-accounts-payable-automation.md)
- [Pattern: Bounded Document Automation Workflow](10-patterns/bounded-document-automation-workflow.md)
- [ADR-001: Use a Bounded Workflow Over an Autonomous Agent](decisions/ADR-001-use-bounded-workflow-over-autonomous-agent.md)

The case study is a sanitised public abstraction. Detailed project evidence remains in the private `AI_Engineering_Worklog` repository and is not default grounding material.

## Repository quality controls

Run the local validator with:

```bash
python -m pip install pyyaml jsonschema
python scripts/validate_content.py
```

The validator checks the catalog schema, canonical retrieval roles, catalog paths, verification-date consistency, internal links, digest exclusion rules, replacement metadata, and obvious secret material.

GitHub Actions runs the same validation for pull requests and pushes to `main`.

Retrieval behaviour is specified in [evals/retrieval-cases.yaml](evals/retrieval-cases.yaml). The initial eval set checks canonical selection, digest exclusion, evidence boundaries, current-source verification, Chinese answers, and abstention-friendly behaviour.

## Repository workflow

Weekly research updates are proposed through draft pull requests. Automated updates must not merge directly into `main`.

```text
Official and primary-source research
                ↓
Classify added / changed / superseded / deprecated / no-action
                ↓
Create or update weekly digest
                ↓
Promote durable guidance where justified
                ↓
Update catalog, changelog, and deprecation registry
                ↓
Run content and retrieval checks
                ↓
Open draft pull request for human review
```

Use [.github/pull_request_template.md](.github/pull_request_template.md) for evidence, lifecycle, sanitisation, and validation review.

## Current status

The repository is in its initial governed-foundation phase. Source policy, machine-readable retrieval metadata, validation, initial eval cases, authoring templates, and the first project-derived architecture knowledge are established. Wider AI-103, Anthropic, OpenAI, RAG, tool-security, evaluation, observability, and reference-architecture coverage remains to be added incrementally.
