# Playbook Map

The repository is organised by engineering lifecycle rather than by vendor. Vendor guidance is cited inside each topic so that patterns remain comparable and portable.

```text
00-certification/          Certification objectives and evidence mapping
01-problem-framing/        When to use rules, workflows, retrieval, or agents
02-architecture/           Single-agent, workflow, orchestration, and multi-agent patterns
03-context-and-rag/        Ingestion, chunking, retrieval, grounding, memory, and evaluation
04-prompts-and-outputs/     Prompt design, structured outputs, validation, and versioning
05-tools-and-mcp/           Tool contracts, authorization, idempotency, and MCP
06-evaluation/              Datasets, offline/online evaluation, regression, and human review
07-security/                Identity, RBAC, secrets, injection, PII, and data boundaries
08-production/              Reliability, tracing, monitoring, deployment, and cost
09-reference-architectures/ End-to-end reusable production designs
09-case-studies/            Sanitised project evidence and implementation retrospectives
10-patterns/                Reusable architecture, reliability, security, and evaluation patterns
11-anti-patterns/           Repeated failure modes and unsafe designs
decisions/                  Architecture Decision Records
weekly-digests/              Time-stamped research and change summaries
templates/                   Standard page, case-study, pattern, ADR, and digest templates
```

## Knowledge layers

```text
Official current guidance
        +
Sanitised project evidence
        ↓
Case study
        ↓
Reusable pattern / ADR / anti-pattern
        ↓
Production checklist and reference architecture
```

A case study records what happened in a specific project. A pattern states a reusable solution and its trade-offs. An ADR records why one option was chosen over alternatives. These content types must not be collapsed into a single “best practice” page.

## Initial content priorities

1. Source policy and governance.
2. Rules vs deterministic workflow vs agent decision framework.
3. Structured outputs, validation, retry, and abstention.
4. RAG design and separate retrieval/generation evaluation.
5. Tool security, permissions, and human approval.
6. Production observability, reliability, and cost controls.
7. Project-to-playbook publication workflow and case studies.
8. Microsoft AI-103 objective mapping.
9. Anthropic architecture and developer certification mapping.
10. OpenAI Responses API, Agents SDK, and current evaluation implementation patterns.

## Current validated content

### Case studies

- [Bounded AI Workflow for Enterprise Accounts Payable Automation](09-case-studies/enterprise-accounts-payable-automation.md)

### Patterns

- [Bounded Document Automation Workflow](10-patterns/bounded-document-automation-workflow.md)

### Decisions

- [ADR-001: Use a Bounded Workflow Over an Autonomous Agent](decisions/ADR-001-use-bounded-workflow-over-autonomous-agent.md)

Empty directories should not be created merely for appearance. Add a directory when its first validated page is ready.
