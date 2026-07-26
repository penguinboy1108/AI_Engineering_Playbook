# Playbook Map

The repository is organized by engineering lifecycle rather than by vendor. Vendor guidance is cited inside each topic so that patterns remain comparable and portable.

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
decisions/                 Architecture Decision Records
weekly-digests/             Time-stamped research and change summaries
templates/                  Standard page, ADR, and digest templates
```

## Initial content priorities

1. Source policy and governance.
2. Rules vs deterministic workflow vs agent decision framework.
3. Structured outputs, validation, retry, and abstention.
4. RAG design and separate retrieval/generation evaluation.
5. Tool security, permissions, and human approval.
6. Production observability, reliability, and cost controls.
7. Microsoft AI-103 objective mapping.
8. Anthropic architecture and developer certification mapping.
9. OpenAI Responses API and Agents SDK implementation patterns.

Empty directories should not be created merely for appearance. Add a directory when its first validated page is ready.