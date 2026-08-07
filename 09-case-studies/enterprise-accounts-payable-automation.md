---
id: bounded-document-automation-case-study
title: Bounded AI Workflow for Enterprise Accounts Payable Automation
status: current
content_type: case-study
document_status: current
evidence_status: project-validated
product_lifecycle: mixed
last_verified: 2026-07-27
next_review_due: 2026-10-27
review_frequency: quarterly
canonical_for:
  - bounded-document-automation
retrieval:
  default_grounding: true
  priority: 70
  role: supporting-evidence
vendors:
  - microsoft
  - anthropic
  - openai
topics:
  - document-processing
  - workflow-orchestration
  - structured-output
  - human-in-the-loop
  - evaluation
  - erp-integration
confidentiality: sanitised-public
supersedes: []
superseded_by: []
---

# Case Study: Bounded AI Workflow for Enterprise Accounts Payable Automation

## Executive summary

A completed enterprise project automated part of an accounts-payable invoice workflow by combining document extraction, email context, supplier and purchase-order retrieval, model-assisted line matching, deterministic financial validation, ERP payload construction, and human review.

The system did **not** give an autonomous agent broad authority over financial processing. The business path was known in advance, so code controlled the workflow while models handled bounded interpretation tasks. Every model output was treated as an untrusted proposal until it passed schema, arithmetic, referential, and policy checks against source-system data.

The downstream action was deliberately reversible: the system prepared and parked a transaction for AP verification rather than automatically completing final financial posting. On the internal evaluation set, header extraction exceeded 90%, while full line-item automation was materially lower. Purchase-order matching was also the dominant model-cost stage.

These results supported a production strategy based on staged metrics, deterministic candidate reduction, explicit block reasons, and selective automation coverage. The figures are rounded project evidence and must not be treated as a universal benchmark.

Detailed organisation, supplier, dataset, financial-rule, source-code, and implementation information remains in a private worklog.

## Problem and business context

Invoices arrived through email in many layouts and quality levels. Staff needed to:

- extract document type, dates, currency, totals, purchase-order references, and line items;
- identify the correct supplier and organisational context;
- retrieve valid purchase orders, items, and receipts from an ERP;
- distinguish standard purchasing from service-style purchasing;
- allocate lines without exceeding remaining values or policy limits;
- handle freight and unplanned costs consistently;
- construct a valid downstream payload;
- stop and explain cases that could not be processed safely.

This was not only an OCR problem. The difficult work was reconciling untrusted documents and emails with authoritative ERP data and finance policy.

## Scope and constraints

### In scope

- Email and PDF ingestion
- Header and line extraction
- Supplier resolution
- Purchase-order and receipt retrieval
- Bounded semantic matching
- Structured output and deterministic validation
- Reversible ERP preparation or parking
- Human review and explicit block reasons
- Batch evaluation, checkpointing, tracing, and cost analysis

### Out of scope

- Unrestricted database or ERP access for the model
- Inventing missing suppliers, POs, items, or receipts
- Treating model confidence as financial approval
- Automatically posting every apparently successful case
- Publishing production documents, source code, or organisation-specific policy

### Key constraints

- Financial errors have asymmetric consequences.
- Source-system records must outrank document inference.
- Supplier and document formats have a long tail.
- The system must remain auditable and recoverable.
- Evaluation must separate extraction quality from end-to-end business correctness.
- Human-review capacity is limited, so automation coverage and risk must be balanced.

## Why a workflow instead of an autonomous agent

The overall process had a predictable sequence and hard policy gates. This made a bounded workflow more appropriate than an agent that dynamically chose its own plan.

```text
Known business sequence
+ bounded model tasks
+ authoritative retrieval
+ typed validation
+ human approval
```

Current Anthropic agent guidance distinguishes predefined workflows from agents that dynamically direct their own process and recommends starting with the simplest architecture that meets the need. The project evidence supported that approach: modular model-assisted stages were useful, but broad autonomy was not required.

## Architecture

```mermaid
flowchart TB
    A[Invoice email and attachments] --> B[Normalise input]
    B --> C[Extract header and lines]
    B --> D[Extract email evidence]
    C --> E[Resolve supplier candidates]
    D --> E
    E --> F[Retrieve ERP PO item and receipt records]
    F --> G[Deterministic candidate reduction]
    G --> H[Bounded model-assisted matching]
    H --> I[Schema arithmetic and referential validation]
    I --> J{Policy gate}
    J -->|Safe| K[Build validated ERP payload]
    K --> L[Park reversible transaction]
    J -->|Uncertain or blocked| M[Human review]
```

### Trust boundaries

```mermaid
flowchart LR
    U[Untrusted document and email] --> X[Extraction and normalisation]
    X --> M[Model proposal]
    S[ERP source-of-truth records] --> V[Deterministic validation]
    M --> V
    V -->|Approved proposal| A[Bounded downstream action]
    V -->|Insufficient evidence| H[Human review]
```

- Documents and emails are untrusted inputs.
- Model outputs are untrusted until validated.
- ERP data is authoritative for suppliers, POs, items, receipts, and financial values.
- The model receives bounded candidates rather than unrestricted system access.
- The automated action is reversible and subject to human verification.

## Business logic

Durable rules were separated from prompt wording.

| Rule | Type | Evidence source | Failure action |
|---|---|---|---|
| Document and credit-note classification | Mixed | Document evidence plus approved mapping | Review unsupported or ambiguous cases |
| Supplier resolution | Hierarchical | Valid PO relationship, trusted email evidence, exact or normalised match, bounded ranking | Unresolved state |
| PO validity | Deterministic | ERP | Block invalid references |
| Item and receipt candidate set | Deterministic retrieval | ERP | Block when required evidence is absent |
| Ambiguous line matching | Probabilistic inside bounded candidates | Document plus ERP candidates | Validate or review |
| Totals and remaining value | Deterministic | Document arithmetic and ERP values | Block on mismatch or exceedance |
| Service and receipt behaviour | Deterministic policy | Approved purchasing rules | Block or approved exception path |
| Freight treatment | Contextual rule | Invoice structure and PO policy | Prevent omission or double count |
| Downstream action | Deterministic policy | Risk boundary | Park only; review uncertainty |

### Evidence hierarchy

```text
Authoritative ERP record
> approved deterministic business rule
> exact document or email evidence
> bounded model inference
> unsupported assumption
```

The model could rank or map valid candidates; it could not create source-system facts.

## Implementation history

### Phase 1: broad automation goal

The initial design targeted both header extraction and detailed PO line allocation.

### Phase 2: modular pipeline

The solution separated document extraction, email enrichment, supplier resolution, PO retrieval and matching, validation, and payload construction. Structured intermediate state made stage-level testing possible.

### Phase 3: evidence-driven controls

Historical testing showed a large performance difference between header extraction and full line-item automation. The design added or strengthened:

- deterministic supplier and PO shortcuts;
- hard matches before semantic ranking;
- remaining-value and service-policy checks;
- explicit unsupported and blocked statuses;
- park-first behaviour;
- checkpointed batch results;
- per-stage token and failure analysis.

### Phase 4: selective production boundary

The system delivered useful preparation automation without pretending that every invoice was equally automatable. High-confidence cases proceeded to a reversible downstream state; difficult cases retained human ownership.

## Evaluation

### Dataset approach

The internal evaluation set used historical invoice emails and attachments across multiple purchasing and document categories. It included recurring suppliers and long-tail cases. Exact composition is private.

### Stage-level metrics

The evaluation separated:

1. header field extraction;
2. supplier resolution;
3. PO retrieval and validation;
4. line and receipt matching;
5. payload validity;
6. end-to-end business outcome;
7. manual-review, blocked, and unsupported outcomes.

### Rounded results

- Header extraction exceeded 90% on the internal set.
- Full end-to-end automation was materially lower than header-only extraction.
- Purchase-order matching consumed the majority of model context and cost.
- Long-tail suppliers and special purchasing cases caused disproportionate failures.

### Why one accuracy number was insufficient

A correct invoice number and total do not prove that the selected supplier, PO, receipt, line allocation, tax treatment, or downstream payload is correct. Production evaluation therefore needs both stage metrics and consequence-aware business metrics, especially the false-auto-accept rate.

## Security, safety, and governance

- Restrict model access to bounded inputs and candidate records.
- Keep ERP mutation behind application-controlled tools and validation.
- Use least privilege and managed identity where the current platform supports it.
- Store secrets outside prompts, source code, and committed configuration.
- Redact documents, emails, suppliers, and model or tool payloads from logs and traces unless explicitly required and protected.
- Treat document and email content as possible prompt-injection input; do not allow it to redefine system policy or tool permissions.
- Require human approval for consequential or uncertain actions.
- Version prompts, schemas, rules, models, and evaluation datasets.

## Reliability and observability

The project used persistent per-document result records to support:

- checkpoint and resume;
- explicit terminal status;
- stage-output inspection;
- token and cost analysis;
- failure-category aggregation;
- comparison across prompt, rule, and model versions.

A production implementation should also include correlation IDs, bounded retries, timeout and backoff, idempotent downstream writes, dead-letter or quarantine paths, and redacted end-to-end tracing.

## What worked

- Modular typed stages instead of one opaque prompt
- Retrieval from the source system before reasoning
- Deterministic shortcuts before model matching
- Explicit financial and policy gates
- Reversible downstream action
- Stage-level evaluation and failure taxonomy
- Checkpointed batch processing

## What failed or underperformed

- Large PO candidate contexts increased cost and ambiguity.
- Repeated model calls did not fix missing source-system evidence.
- Header quality could create false confidence about end-to-end readiness.
- A universal prompt did not solve the supplier and document long tail.
- Business rules embedded only in prompts were harder to govern and test.

## Reusable knowledge

- [Bounded Document Automation Workflow](../10-patterns/bounded-document-automation-workflow.md)
- [ADR-001: Use a bounded workflow over an autonomous agent](../decisions/ADR-001-use-bounded-workflow-over-autonomous-agent.md)

Additional patterns supported by the case:

- deterministic-first candidate reduction;
- evidence hierarchy and source-system grounding;
- confidence-and-policy-gated human review;
- draft or park before commit;
- stage-level evaluation;
- failure-aware retry.

## Best-practice mapping

| Project decision | Evidence label | Current primary source | Alignment or gap |
|---|---|---|---|
| Use fixed orchestration with bounded model stages | Official recommendation plus project evidence | Anthropic, *Building effective agents* | Aligns with workflows for well-defined tasks and adding complexity only when justified |
| Event-driven document extraction, schema mapping, quality checks, and human validation | Reference architecture | Microsoft Azure Architecture Center, multimodal content processing | Strong conceptual alignment; the historical project used its own implementation stack |
| Use document extraction as one component of a larger processing pipeline | Official product guidance | Microsoft Document Intelligence documentation | OCR alone did not solve ERP matching and policy |
| Run quality and safety evaluation against datasets | Official recommendation | Microsoft Foundry evaluation guidance | A current implementation should formalise versioned evaluation runs and gates |
| Constrain outputs with schemas and validate before action | Official recommendation | OpenAI structured outputs guidance | Deterministic business validation remains required beyond schema compliance |
| Expand evaluation data with discovered edge cases | Official recommendation | OpenAI evaluation best practices | Aligns with adding long-tail failures and human corrections to regression suites |
| Evaluate multi-step behaviour and intermediate failures | Official recommendation | Anthropic agent-evaluation guidance | Applicable even when the system is a workflow rather than an autonomous agent |

## How to build it today

A new implementation should preserve the pattern but re-evaluate products and APIs:

1. Select the current generally available document-processing service that best matches the document types and data boundary.
2. Use event-driven orchestration with explicit state, idempotency, retry policy, quarantine, and human-review queues.
3. Use structured outputs for model contracts, followed by deterministic domain validation.
4. Retrieve and reduce ERP candidates before semantic matching.
5. Build an evaluation dataset and stage-level graders before broadening automation coverage.
6. Verify the current evaluation APIs, SDKs, product names, and lifecycle directly from official documentation before implementation; do not encode a long-lived architecture around an assumed interface or unverified retirement claim.
7. Redact sensitive input and output from tracing and logs by default.
8. Expand from park or draft to more autonomous action only after business-approved risk assessment and strong false-auto-accept evidence.

## Publication and sanitisation record

- Organisation and customer identifiers removed: yes
- Supplier-specific details removed or generalised: yes
- Internal endpoints and account identifiers removed: yes
- Raw documents and messages removed: yes
- Confidential thresholds and rules generalised: yes
- Metrics rounded where appropriate: yes
- Detailed evidence retained only in private worklog: yes

## Limitations and open questions

- The case does not publish underlying documents, prompts, source code, or supplier-specific rules.
- Rounded project results cannot be compared directly with other organisations or datasets.
- The internal evaluation should be formalised with immutable dataset manifests and versioned holdouts before making stronger benchmark claims.
- A future implementation should test whether improved deterministic retrieval can reduce the expensive matching stage enough to change the architecture.
- All product and lifecycle claims require re-verification at implementation time.

## Sources

| ID | Source | Evidence | Supports | Checked on | Lifecycle/version |
|---|---|---|---|---|---|
| SRC-001 | https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/multi-modal-content-processing | reference-architecture | Document-processing pipeline and human validation | 2026-07-27 | Recheck before implementation |
| SRC-002 | https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0 | official | Document extraction capability | 2026-07-27 | Recheck service boundary and API version |
| SRC-003 | https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app | official | Dataset-based evaluation | 2026-07-27 | Recheck current tooling |
| SRC-004 | https://www.anthropic.com/engineering/building-effective-agents | official | Workflow versus agent selection | 2026-07-27 | Current at verification date |
| SRC-005 | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | official | Multi-step and intermediate evaluation | 2026-07-27 | Current at verification date |
| SRC-006 | https://developers.openai.com/api/docs/guides/structured-outputs | official | Structured output contracts | 2026-07-27 | Recheck current API guidance |
| SRC-007 | https://developers.openai.com/api/docs/guides/evaluation-best-practices | official | Evaluation best practices | 2026-07-27 | Recheck current tooling |
