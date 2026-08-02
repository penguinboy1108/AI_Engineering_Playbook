# Specification-Driven AI Coding and Harness Engineering

> Status: initial practice guide  
> Last verified: 2026-07-31  
> Scope: AI-assisted software delivery, coding agents, and production-oriented agentic development

## Purpose

AI coding increases implementation speed, but it also increases the speed at which unclear assumptions can become working, well-structured, and still incorrect software.

This guide defines a lightweight control system for turning product intent into verifiable implementation evidence. It does not require a large PRD or full BDD suite for every change. The amount of specification and testing should be proportional to business risk, uncertainty, and blast radius.

## Responsibility model

| Artifact or practice | Primary responsibility | Question it answers |
|---|---|---|
| PRD or feature brief | Product intent and scope | Are we building the right capability? |
| Acceptance criteria and BDD examples | Observable business behaviour | What must users and external systems observe? |
| Technical design or ADR | Architecture and constraints | How should the capability fit the system? |
| TDD and automated tests | Deterministic implementation correctness | Does the code satisfy its contract and resist regression? |
| AI evaluations | Probabilistic system quality | Does the model or agent behave well across representative cases? |
| Harness engineering | Execution control and evidence | Can an agent make safe, incremental, recoverable progress? |

The practical chain is:

```text
Intent and scope
  -> concrete examples
  -> observable acceptance behaviour
  -> technical constraints
  -> small implementation tasks
  -> tests and evaluations
  -> completion evidence
  -> human review
```

## Risk-based delivery tiers

Avoid forcing every task through the same amount of process.

| Tier | Typical change | Minimum specification | Minimum verification |
|---|---|---|---|
| Small | Copy change, simple mapping, low-risk configuration | Ticket or short task statement | Focused test or direct verification |
| Medium | New API, workflow, integration, or user-facing feature | Mini PRD, concrete examples, technical notes | Unit and integration tests plus acceptance verification |
| High risk | Financial rules, permissions, state machines, data migration, autonomous actions, regulated decisions | Full requirements, BDD examples, design review, threat model, rollback plan | Layered tests, security checks, evaluations, human approval, release gates |

Escalate the tier when any of the following increases:

- ambiguity or unresolved business rules;
- financial, privacy, security, or compliance impact;
- production blast radius;
- irreversible data or infrastructure changes;
- model autonomy or tool permissions;
- dependence on nondeterministic AI output.

## Recommended implementation flow

### 1. Normalise the request

Before coding, convert the request into a small feature brief:

```markdown
## Problem
Who is affected and what problem exists?

## Goal
What outcome should improve?

## In scope
What capability will be delivered?

## Out of scope
What should not be added in this change?

## Business rules
Which rules are already decided?

## Open questions
Which decisions still require a human owner?

## Non-functional requirements
Security, privacy, performance, reliability, auditability, observability, and cost.
```

The agent may identify missing information and propose options. It must not silently convert unresolved business questions into implementation decisions.

### 2. Turn requirements into concrete examples

Use examples to clarify each important rule before implementation. BDD is primarily a discovery and shared-understanding practice; Gherkin is optional.

A compact example format is often enough:

```markdown
Rule: Only authorised users can view invoice diagnostics.

Example: Authorised user views a failed invoice
- Given an authorised operations user
- And an invoice failed during PO matching
- When the user requests diagnostics
- Then the latest processing status is shown
- And internal stack traces are not exposed

Example: Unauthorised access
- Given a user without diagnostic permission
- When the user requests diagnostics
- Then access is denied
- And the attempt is audited
```

Prefer observable outcomes over UI implementation details or database internals.

### 3. Define technical constraints

For medium and high-risk changes, record the minimum technical design needed to prevent architectural drift:

- affected components and boundaries;
- public API, event, schema, or file contracts;
- identity and permission model;
- data ownership and retention;
- failure, retry, timeout, and idempotency behaviour;
- observability and audit requirements;
- deployment, rollback, and compatibility considerations;
- explicit non-goals.

Use an ADR when a decision is difficult to reverse or has multiple credible alternatives.

### 4. Build a traceable test plan

Map each requirement or example to the cheapest reliable verification layer.

| Concern | Preferred evidence |
|---|---|
| Pure business rule, calculation, mapping, or state transition | Unit test, often test-first |
| Database, queue, API, identity, or external contract | Integration or contract test |
| User-visible business outcome | API-level or BDD acceptance test |
| Critical end-to-end journey | Small number of E2E tests |
| LLM extraction, classification, routing, or agent behaviour | Versioned evaluation dataset and rubric |
| Security boundary | Authorisation tests, negative tests, and security scanning |
| Operational behaviour | Telemetry, failure injection, recovery test, and runbook verification |

Do not use coverage percentage as the sole quality target. Prefer stable tests that protect important behaviour over large suites of brittle tests.

### 5. Decompose work into independently verifiable tasks

The agent should implement one reviewable unit at a time, for example:

```text
1. Define or confirm the contract.
2. Add tests for the approved behaviour.
3. Implement domain logic.
4. Integrate storage or external services.
5. Expose the API, event, or UI path.
6. Run acceptance verification.
7. Update documentation and operational artifacts.
```

Each task should have:

- a bounded file or component scope;
- a stated requirement or scenario;
- a verification command or observable result;
- an explicit completion condition;
- no unresolved high-impact decision.

### 6. Use test-first development selectively

Strict TDD is most valuable where errors are expensive or rules are easy to express deterministically:

- money and billing calculations;
- permissions and policy evaluation;
- state machines and workflow transitions;
- matching, validation, and mapping rules;
- retry, deduplication, and idempotency logic;
- date, time-zone, and boundary behaviour.

For simple DTOs, framework glue, generated code, and low-risk configuration, implementation followed by focused verification may be more efficient.

When an agent claims to have used TDD, the harness should preserve evidence that the new test failed for the expected reason before the implementation was added. Generating implementation and passing tests in one unobserved step is not strong evidence of test-driven development.

### 7. Require completion evidence

An agent must not declare success based only on code inspection or a plausible explanation.

A completion report should look like:

```yaml
requirements:
  FEATURE-001: verified
  FEATURE-002: verified

checks:
  build: passed
  unit_tests: 128 passed
  integration_tests: 21 passed
  acceptance_tests: 6 passed
  security_scan: no new high-severity findings
  evals: quality threshold met

documentation:
  updated: true

assumptions: []
limitations:
  - Previous processing attempts are not exposed in this release.

unresolved_risks: []
```

The exact fields can vary, but the evidence must be tied to the approved scope and observable behaviour.

## Harness engineering implementation

Harness engineering is the design of the environment, constraints, feedback loops, state, and tools that enable an agent to perform reliable work. A useful harness has six layers.

### 1. Context harness

Make the repository legible to agents without loading every document into every prompt.

Recommended assets:

- root `AGENTS.md` or equivalent repository instructions;
- repository map and ownership boundaries;
- indexed PRDs, feature briefs, ADRs, and runbooks;
- test and evaluation guidance;
- known constraints and prohibited operations;
- commands for build, test, lint, local run, and environment setup.

Use progressive disclosure:

```text
Repository rules
  -> relevant feature specification
  -> relevant architecture decision
  -> relevant code and tests
  -> additional context only when needed
```

### 2. Planning harness

Require a structured plan before code changes for medium and high-risk work.

```yaml
task:
  requirement_ids:
    - FEATURE-001

scope:
  modify:
    - src/FeatureService
    - tests/FeatureService.Tests
  do_not_modify:
    - authentication
    - database_schema

risks:
  - sensitive fields may be returned

tests:
  - FeatureServiceTests
  - FeatureApiTests

open_questions: []
```

If `open_questions` contains an unresolved business, security, or irreversible design decision, implementation should stop at analysis or proposal stage.

### 3. Execution harness

Constrain how the agent changes the repository and external systems:

- bounded tasks and small diffs;
- explicit writable paths where practical;
- least-privilege tools and credentials;
- no direct production changes by default;
- no test deletion, weakening, or skipping merely to obtain a green build;
- separate approval for schema, infrastructure, permission, and destructive changes;
- checkpoints before high-impact operations;
- reversible commits or patches.

### 4. Feedback harness

Expose reality through tools rather than relying on model confidence:

- compiler and type checker;
- lint and formatting checks;
- unit, integration, contract, and acceptance tests;
- security and dependency scanning;
- browser or API verification;
- runtime logs, traces, and metrics;
- evaluation datasets and graders for AI behaviour;
- human review for intent, risk acceptance, and subjective quality.

Use the narrowest fast feedback during implementation, followed by broader gates before completion.

### 5. State and recovery harness

Long-running work must survive context limits, agent restarts, tool failures, and partial completion.

Maintain a compact checkpoint artifact:

```markdown
## Current objective

## Completed

## Files changed

## Verification results

## Failed attempts and causes

## Remaining work

## Open questions and risks

## Recommended next action
```

The checkpoint should record facts and evidence, not a long narrative of the agent's reasoning.

### 6. Governance harness

Keep human ownership explicit for decisions such as:

- product scope and business rules;
- security and permission models;
- data retention and privacy policy;
- public contract changes;
- production release and rollback decisions;
- destructive or irreversible actions;
- risk acceptance;
- high-impact autonomous decisions.

Agents may analyse, recommend, implement approved decisions, and collect evidence. They should not silently become the decision owner.

## Definition of Ready

Before medium or high-risk implementation begins:

- [ ] The user problem and desired outcome are clear.
- [ ] In-scope and out-of-scope behaviour are recorded.
- [ ] Important business rules have concrete examples.
- [ ] High-impact ambiguities are resolved or explicitly blocked.
- [ ] Security, privacy, permission, and audit needs are considered.
- [ ] External contracts and dependencies are identified.
- [ ] Technical constraints and non-goals are documented.
- [ ] Verification and evaluation methods are defined.
- [ ] The work is decomposed into reviewable tasks.

## Definition of Done

Before an agent or team declares the change complete:

- [ ] Approved acceptance criteria have been checked individually.
- [ ] Relevant build, test, lint, and type checks pass.
- [ ] AI behaviour meets the agreed evaluation threshold where applicable.
- [ ] Security and negative-path checks are complete for changed boundaries.
- [ ] No unrelated scope expansion is hidden in the diff.
- [ ] Assumptions, limitations, and unresolved risks are reported.
- [ ] Documentation, operational guidance, and checkpoints are updated.
- [ ] A human has reviewed intent-sensitive or high-risk decisions.

## Agent operating contract

A repository-level instruction file can include the following compact contract:

```markdown
## Before coding

1. Read the relevant requirement, examples, and design decisions.
2. Identify the requirement IDs and exact scope.
3. Report unresolved high-impact questions; do not invent business rules.
4. Produce a bounded plan and identify verification evidence.

## During coding

1. Work in independently verifiable increments.
2. Use test-first development for critical deterministic logic.
3. Do not modify unrelated files or public contracts without approval.
4. Do not weaken tests or controls merely to make checks pass.
5. Run focused checks after meaningful changes.
6. Save a checkpoint when work spans sessions or contexts.

## Before completion

1. Run the required quality gates.
2. Verify acceptance criteria one by one.
3. Map changes and tests to requirements.
4. Report assumptions, limitations, risks, and evidence.
5. Never claim completion from code generation alone.
```

## Anti-patterns

Avoid these common failures:

- giving an agent a vague PRD and asking it to build the entire feature in one pass;
- treating BDD as only a Gherkin syntax exercise;
- generating tests after implementation and calling the result TDD without observing a failing test;
- testing only happy paths;
- mocking away the integration boundary that actually carries the risk;
- allowing the agent to expand scope because an addition appears useful;
- using context length as a substitute for repository structure;
- relying on self-reported success without tool evidence;
- running long tasks without checkpoints or recovery instructions;
- using an elaborate multi-agent harness when a deterministic workflow is sufficient.

## Adoption approach

Introduce this workflow incrementally:

1. Add a repository instruction file and verification commands.
2. Add lightweight feature briefs with scope and concrete examples.
3. Add Definition of Ready and Definition of Done gates.
4. Require structured plans and completion evidence for medium-risk work.
5. Add checkpoint artifacts for long-running tasks.
6. Add evaluation datasets for nondeterministic AI components.
7. Add stronger permissions, approvals, and release gates only where risk justifies them.
8. Periodically remove harness complexity that is no longer load-bearing.

The target is not maximum process. The target is the smallest reliable system that keeps intent, implementation, evidence, and human ownership aligned.

## Primary sources

- OpenAI, **Harness engineering: leveraging Codex in an agent-first world**: https://openai.com/index/harness-engineering/
- Anthropic, **Effective harnesses for long-running agents**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic, **Harness design for long-running application development**: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Cucumber, **Behaviour-Driven Development**: https://cucumber.io/docs/bdd/
- Cucumber, **Example Mapping**: https://cucumber.io/docs/bdd/example-mapping/
- Cucumber, **Gherkin reference**: https://cucumber.io/docs/gherkin/reference/
- Microsoft Azure Well-Architected Framework, **Architecture strategies for testing**: https://learn.microsoft.com/azure/well-architected/operational-excellence/testing
- Microsoft Azure Well-Architected Framework, **Design review checklist for Operational Excellence**: https://learn.microsoft.com/azure/well-architected/operational-excellence/checklist
