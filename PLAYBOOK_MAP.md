# Playbook Map

The repository is organised primarily by engineering lifecycle rather than by vendor. Vendor guidance is cited inside each topic so patterns remain comparable and portable.

Existing directory numbers are kept stable. New planned areas use unique numbers to avoid path churn and duplicate prefixes.

```text
00-certification/           Certification objectives and evidence mapping
01-problem-framing/         When to use rules, workflows, retrieval, or agents
02-architecture/            Single-agent, workflow, orchestration, and multi-agent patterns
03-context-and-rag/         Ingestion, chunking, retrieval, grounding, memory, and evaluation
04-prompts-and-outputs/      Prompt design, structured outputs, validation, and versioning
05-tools-and-mcp/            Tool contracts, authorization, idempotency, and MCP
06-evaluation/               Datasets, offline/online evaluation, regression, and human review
07-security/                 Identity, RBAC, secrets, injection, PII, and data boundaries
08-production/               Reliability, tracing, monitoring, deployment, lifecycle, and cost
09-case-studies/             Sanitised project evidence and implementation retrospectives
10-patterns/                 Reusable architecture, reliability, security, and evaluation patterns
11-anti-patterns/            Repeated failure modes and unsafe designs
12-reference-architectures/  End-to-end reusable production designs
decisions/                   Architecture Decision Records
docs/workflows/              Cross-lifecycle engineering and delivery practices
weekly-digests/              Time-stamped research and change summaries
evals/                       Retrieval and answer-behaviour specifications
schema/                      Machine-readable metadata schemas
scripts/                     Repository validation and maintenance tools
templates/                   Standard page, case-study, pattern, ADR, and digest templates
.github/                     Pull-request and CI quality controls
```

Empty directories should not be created merely for appearance. Add a directory when its first validated page is ready.

## Entry points

```text
README.md          Human overview
AGENTS.md          AI retrieval and authoring contract
GPT_USAGE.md       User guidance for GPT-assisted problem solving
catalog.yaml       Machine-readable knowledge index
SOURCE_POLICY.md   Evidence and metadata policy
GOVERNANCE.md      Review, publication, and lifecycle process
```

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
Canonical guide or reference architecture
```

A case study records what happened in a specific project. A pattern states a reusable solution and its trade-offs. An ADR records why one option was chosen over alternatives. A reference architecture combines several current patterns into an end-to-end design. These content types must not be collapsed into a single “best practice” page.

## Retrieval layers

```text
Primary canonical page
        ↓
Decision context from accepted ADRs
        ↓
Supporting evidence from case studies
        ↓
Recent-change records only when requested
```

`catalog.yaml` defines the retrieval role and priority for each indexed page. Weekly digests are not default grounding. Deprecated, superseded, archived, experimental, and unverified pages are excluded by default.

## Current validated content

### Practice guides

- [Specification-Driven AI Coding and Harness Engineering](docs/workflows/specification-driven-ai-coding.md)
- [Agent Capability Containment](07-security/agent-capability-containment.md)
- [SDK Version and Default Control](08-production/sdk-version-and-default-control.md)

### Case studies

- [Bounded AI Workflow for Enterprise Accounts Payable Automation](09-case-studies/enterprise-accounts-payable-automation.md)

### Patterns

- [Bounded Document Automation Workflow](10-patterns/bounded-document-automation-workflow.md)

### Decisions

- [ADR-001: Use a Bounded Workflow Over an Autonomous Agent](decisions/ADR-001-use-bounded-workflow-over-autonomous-agent.md)

### Research records

- [AI Engineering Weekly Digest — 2026-07-30](weekly-digests/2026/2026-07-30.md)

## Machine and quality assets

- [Knowledge catalog](catalog.yaml)
- [Catalog schema](schema/catalog.schema.json)
- [Content validator](scripts/validate_content.py)
- [Retrieval evaluation cases](evals/retrieval-cases.yaml)
- [Content-quality workflow](.github/workflows/content-quality.yml)
- [Pull-request review template](.github/pull_request_template.md)

## Initial content priorities

1. Rules vs deterministic workflow vs RAG vs agent decision framework.
2. Structured outputs, validation, retry, and abstention.
3. RAG ingestion, rapid update, retrieval, reranking, and separate retrieval/generation evaluation.
4. Tool contracts, permissions, idempotency, human approval, and MCP.
5. Production observability, reliability, recovery, and cost controls.
6. Prompt-injection, data-poisoning, identity, and agent capability containment.
7. Project-to-playbook publication workflow and additional sanitised case studies.
8. Microsoft AI-103 objective mapping.
9. Anthropic architecture and developer-certification mapping.
10. OpenAI current API, Agents SDK, evaluation, and production implementation patterns.
11. Executable retrieval and answer evaluations against representative work questions.
