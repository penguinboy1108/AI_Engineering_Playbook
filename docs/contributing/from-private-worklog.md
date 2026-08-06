# Extracting Public Guidance from a Private Worklog

## Purpose

The private `AI_Engineering_Worklog` preserves project evidence, periodic work records, decisions, failures, outcomes, and organisation-specific context. This public repository contains only sanitised, reusable AI engineering guidance.

Private evidence can motivate and support a playbook entry, but it must not be copied directly into this repository.

## Content boundary

| Private worklog | Public playbook |
|---|---|
| Chronological and project-specific | Durable and problem-oriented |
| May include AI and non-AI work | Focused on reusable AI engineering guidance |
| Records what happened, including incomplete work | Publishes reviewed conclusions and limitations |
| May contain safe private organisational context | Removes confidential and identifying details |
| Supports reporting, CVs, interviews, and reflection | Supports future system design and engineering practice |

## Promotion path

```text
periodic log or project evidence
              ↓
private playbook-candidate record
              ↓
identify the general problem and candidate lesson
              ↓
sanitise project-specific and confidential context
              ↓
verify technical claims against current primary sources
              ↓
choose public content type
              ↓
draft, review, and publish through a pull request
```

## Choose the correct public content type

### Case study

Use a case study when the value comes from a sanitised account of what happened in one implementation, including context, constraints, choices, evaluation, results, and lessons.

### Pattern

Use a pattern when the guidance describes a recurring problem, a reusable solution, its forces, consequences, applicability, and failure modes.

### ADR

Use an ADR when the durable lesson is primarily a choice between alternatives and the reasoning behind that choice.

### Anti-pattern

Use an anti-pattern when repeated project evidence shows an attractive but harmful approach, why it fails, warning signs, and safer alternatives.

### Workflow, checklist, or playbook entry

Use these when the main value is a repeatable operating or implementation procedure rather than a single architecture pattern.

A single private source may produce more than one public artifact, but each artifact should have one clear purpose.

## Extraction procedure

### 1. State the general problem

Remove organisation and product names. Describe the class of system, users, constraints, and risk that make the lesson relevant.

### 2. Separate evidence from interpretation

Identify:

- directly observed project facts;
- measured results;
- estimates or stakeholder impressions;
- engineering judgement inferred from the evidence;
- claims that require external verification.

Do not present one project outcome as universal proof.

### 3. Sanitise

Remove or generalise:

- organisation, customer, supplier, member, employee, and stakeholder identifiers;
- internal URLs, endpoints, environment names, repository names, and system identifiers;
- credentials, secrets, connection details, and security-sensitive architecture;
- confidential policies, business rules, financial data, or proprietary decision logic;
- raw documents, payloads, screenshots, or conversations;
- metrics that are confidential or too identifying.

Where exact numbers are unsafe, use ranges, ratios, normalised values, or qualitative evidence only when this does not mislead the reader.

### 4. Verify technical guidance

For fast-changing technical claims, use current primary sources and add the required evidence label and `last_verified` date.

Project experience can support implementation judgement, but it does not replace official documentation for API behaviour, security controls, product availability, limits, or current platform capabilities.

### 5. Preserve uncertainty and limitations

Include:

- what the evidence does and does not establish;
- applicability conditions;
- known trade-offs;
- failure modes and operational risks;
- circumstances where another approach is preferable;
- unresolved questions or missing evaluation.

### 6. Draft independently of private links

The public entry must be understandable without access to the private repository. Do not include private URLs or wording that implies readers can inspect private evidence.

### 7. Review before publication

Confirm that:

- the content type is appropriate;
- confidential or identifying details are removed;
- claims are proportionate to the evidence;
- current technical claims are sourced;
- applicability and limitations are explicit;
- the entry follows the relevant template;
- changelog, map, ADR, deprecation, or related pages are updated when required.

## Evidence language

Prefer precise language:

- **Observed:** directly seen in the project.
- **Measured:** supported by a defined metric or evaluation.
- **Estimated:** based on a stated assumption or approximation.
- **Inferred:** an engineering conclusion drawn from evidence.
- **Recommended:** guidance proposed after combining evidence, constraints, and primary sources.

Avoid language such as “always,” “guarantees,” or “best practice” unless the scope and source justify it.

## Example transformation

Private record:

> A specific automation failed because a stale local file was reused after an expected save step did not complete. The issue was diagnosed by comparing the refreshed row count with the expected source data.

Possible public lesson:

> File-based automation should validate freshness, path, naming, and expected record counts before downstream refresh or ingestion. Treat successful command execution as insufficient evidence that the intended input artifact was created.

The public lesson preserves the engineering value while removing the organisation, user, path, and dataset details.

## Relationship to non-AI work

The private worklog may contain valuable non-AI engineering evidence. Promote it into this repository only when it materially informs AI system design, evaluation, security, reliability, data handling, automation boundaries, human review, or production operations.

General software engineering achievements that do not add AI-specific guidance should remain in the private worklog or another suitable portfolio or engineering knowledge base.
