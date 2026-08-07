---
id: ADR-NNN
title: Decision title
content_type: adr
document_status: draft
evidence_status: unverified
product_lifecycle: not-applicable
last_verified: "YYYY-MM-DD"
next_review_due: "YYYY-MM-DD"
review_frequency: quarterly
canonical_for: []
retrieval:
  default_grounding: false
  priority: 0
  role: decision-context
vendors: []
topics: []
supersedes: []
superseded_by: []
---

# ADR-NNN: Decision title

- Decision date: YYYY-MM-DD
- Decision owners:
- Related canonical pages:
- Related case studies:

## Context

Describe the business goal, technical constraints, risk level, data sensitivity, expected scale, operational environment, systems of record, and consequences of failure.

## Decision drivers

- 

## Options considered

Include credible alternatives, including a deterministic non-AI implementation where applicable.

### Option A

**Advantages:**

**Disadvantages:**

### Option B

**Advantages:**

**Disadvantages:**

## Decision

State the selected approach precisely, including scope and explicit non-goals.

## Evidence

| Evidence label | Source ID or project reference | What it supports | Checked on |
|---|---|---|---|
| | | | |

Separate official requirements, official recommendations, reference architectures, project measurements, and engineering inferences.

## Consequences

### Positive

- 

### Negative

- 

### Risks and mitigations

| Risk | Consequence | Mitigation | Owner |
|---|---|---|---|
| | | | |

## Security and human control

State identity, permissions, trust boundaries, approval points, irreversible actions, audit requirements, fallback behaviour, and maximum credible blast radius.

## Reliability and recovery

State timeout, retry classification, idempotency, checkpoint, rollback, partial-failure, and recovery requirements.

## Evaluation and success criteria

Define measurable acceptance, safety, business, latency, cost, and regression criteria.

## Observability and provenance

State required logs, traces, metrics, correlation IDs, redaction, and version information.

## Revisit triggers

List changes that should cause this decision to be reviewed, such as API retirement, model or SDK change, cost threshold, failure rate, new regulation, changed business policy, or stronger evaluation evidence.

## Supersession

When replaced:

1. change `document_status` to `superseded`;
2. set `superseded_by` in front matter and `catalog.yaml`;
3. link the new ADR;
4. explain migration and rollback;
5. preserve this ADR as historical decision context.

## Sources

| ID | Source | Evidence | Supports | Checked on | Lifecycle/version |
|---|---|---|---|---|---|
| SRC-001 | Current primary source | official | Specific decision driver | YYYY-MM-DD | |
