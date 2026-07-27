---
id: ADR-001
title: Use a bounded workflow over an autonomous agent for defined, consequential document processing
status: accepted
last_verified: 2026-07-27
source_priority: official-plus-project-evidence
---

# ADR-001: Use a Bounded Workflow Over an Autonomous Agent

## Context

Enterprise document-processing systems often have variable inputs but a known business sequence: ingest, extract, retrieve source-system records, validate, decide, and create a downstream artifact. Some stages benefit from language-model interpretation, but policy, permissions, source-of-truth checks, and consequential actions must remain predictable.

A public case study in this repository showed the same pattern in accounts-payable automation: model-assisted extraction and matching were valuable, but broad autonomy was not necessary and would have increased cost, latency, and risk.

## Decision drivers

- Consequential downstream action
- Known business process and state transitions
- Need for auditability and reproducibility
- Source-system authority
- Stage-level evaluation
- Bounded permissions and blast radius
- Cost and latency control

## Options considered

### A. Single large model call

**Advantages:** minimal orchestration.

**Disadvantages:** mixes extraction, retrieval assumptions, policy, and action; difficult to inspect, validate, and evaluate.

### B. Autonomous tool-using agent

**Advantages:** adapts its plan and tool sequence.

**Disadvantages:** unnecessary autonomy for a defined process; higher non-determinism, cost, and compounding-error risk.

### C. Code-controlled modular workflow

**Advantages:** explicit stages, typed contracts, deterministic gates, checkpointing, and controlled tool permissions.

**Disadvantages:** more orchestration and domain-validation code.

## Decision

Choose Option C by default for defined, consequential document-processing workflows. Use model calls inside bounded stages where they provide measurable value. Introduce a dynamic agent only for genuinely open-ended subtasks that cannot be expressed as a stable workflow and that have testable success criteria and safe tool boundaries.

## Rationale

Anthropic's official guidance recommends starting with the simplest architecture and differentiates predefined workflows from agents that dynamically direct their own process. Microsoft's multimodal content-processing reference architecture similarly demonstrates explicit ingestion, processing, schema mapping, quality checks, and human validation. The project evidence showed that fixed stage boundaries made failure analysis and risk control practical.

## Consequences

### Positive

- Predictable state and stopping conditions
- Easier stage-level evaluation
- Lower blast radius
- Better retry and checkpoint semantics
- Clear source-of-truth and human-review boundaries
- Easier cost attribution and optimisation

### Negative

- More explicit orchestration code
- New business categories may require workflow changes
- Poorly designed contracts can still propagate ambiguity
- The design may be less flexible for truly novel tasks

## Required guardrails

- Treat model output as untrusted until validated.
- Keep durable business rules outside prompts.
- Retrieve authoritative records before model reasoning.
- Use typed stage contracts and explicit terminal statuses.
- Bound retries and distinguish transient from business failures.
- Put consequential writes behind deterministic validation and approval.
- Persist checkpoints and idempotency state.
- Maintain stage-level and end-to-end evaluation datasets.

## Exceptions

A dynamic agent can be justified when all of the following are true:

- the required sequence cannot be predicted in advance;
- the model must decide among tools or investigations dynamically;
- success criteria are objective enough to evaluate;
- the environment is sandboxed or the tools are tightly scoped;
- the higher cost and latency are justified by measured improvement;
- humans remain in control of high-impact actions.

## Evidence

| Evidence label | Source | What it supports | Last verified |
|---|---|---|---|
| Official recommendation | https://www.anthropic.com/engineering/building-effective-agents | Prefer simple composable patterns; workflows for well-defined tasks; agents for open-ended tasks | 2026-07-27 |
| Reference architecture | https://learn.microsoft.com/en-us/azure/architecture/ai-ml/idea/multi-modal-content-processing | Explicit document-processing pipeline, quality controls, and human validation | 2026-07-27 |
| Project evidence | [Enterprise Accounts Payable Automation](../09-case-studies/enterprise-accounts-payable-automation.md) | Bounded stages exposed the gap between extraction and end-to-end business correctness | 2026-07-27 |

## Revisit conditions

- A genuinely open-ended stage repeatedly defeats a fixed workflow.
- A dynamic agent shows statistically and operationally meaningful improvement on a representative holdout set.
- New platform controls materially reduce the agent's blast radius.
- Business policy permits broader autonomy.
- The downstream action becomes safely reversible and observable.
