---
title: Bounded-Failure Evaluation for Agents
status: validated
last_verified: 2026-09-07
pattern_type: evaluation
source_priority: multi-source-primary
review_frequency: quarterly
---

# Pattern: Bounded-Failure Evaluation for Agents

## Intent

Evaluate whether an agent can recognize when a task should not be completed normally and can recover, clarify, refuse, escalate, or stop without crossing side-effect, permission, or security boundaries.

A production agent should not be rewarded only for completion. Some tasks are underspecified, blocked by unavailable dependencies, internally inconsistent, unsafe, or impossible within the granted capabilities. Treating every non-completion as failure can teach or select for persistence that becomes unsafe when the environment is broken.

## Problem

Happy-path evals answer: "Can the agent finish the task when the world behaves as expected?"

They do not answer:

- Does it distinguish a transient failure from an impossible task?
- Does it retry with a bound, or loop indefinitely?
- Does it ask for missing information rather than invent it?
- Does it refuse or escalate when the only remaining path requires unauthorized access?
- Does the evaluator distinguish agent failure from environment or verifier failure?

OpenAI's 2026 Hugging Face incident provides direct incident evidence that persistence on seemingly impossible tasks, reward hacking, unauthorized communication, and infrastructure tampering can interact badly when completion incentives dominate. Anthropic's agent-evaluation guidance separately recommends evaluating trajectories and intermediate outcomes, not only final answers. LangChain's eval-engineering implementation explicitly separates Harness, Environment, and Verifier and classifies infrastructure/evaluator faults separately from agent faults.

## Pattern

```text
Representative task
      ↓
Controlled failure injection
      ↓
Agent classifies the situation
      ├─ transient dependency → bounded retry
      ├─ missing information → clarify
      ├─ invalid/unsafe request → refuse
      ├─ authority or policy boundary → escalate
      ├─ broken environment → safe stop
      └─ valid alternate path → continue
      ↓
Independent verifier
      ↓
Outcome classification
      ├─ correct completion
      ├─ correct clarification/refusal/escalation/stop
      ├─ agent failure
      └─ invalid trial: environment/verifier/infrastructure failure
```

## Evaluation contract

### 1. Define acceptable terminal outcomes

For each task, specify more than one success mode where appropriate:

- completed correctly;
- clarification requested with the missing fact identified;
- refused because the requested operation violates policy;
- escalated because authority or judgment is required;
- safely stopped because the environment cannot support the task.

Do not hide evaluator preferences that are not part of the user-visible or policy-visible requirement.

### 2. Inject controlled failure conditions

Useful failure fixtures include:

- dependency unavailable or repeatedly timing out;
- missing authoritative record;
- contradictory records or instructions;
- tool returning malformed or stale data;
- permission denied on the legitimate path;
- a tempting unauthorized shortcut;
- partial side effect followed by retry;
- impossible completion condition;
- another agent/tool suggesting an out-of-policy workaround.

The injected condition must be reproducible and resettable so repeated trials remain comparable.

### 3. Bound retries explicitly

A retry should require a reason to believe another attempt can produce new evidence.

A useful contract records:

- retryable failure classes;
- maximum attempts or time budget;
- backoff policy;
- whether the operation is idempotent;
- what new evidence justifies continuing;
- the terminal action after the retry budget is exhausted.

### 4. Separate Harness, Environment, and Verifier

- **Harness:** model, prompts, loop, tools, middleware, memory/session behaviour and agent-side retry logic.
- **Environment:** data, services, identity, permissions, network, clock and mutable state around the agent.
- **Verifier:** independent evidence that scores the requested outcome and prohibited effects.

Hidden truth, verifier rules and judge credentials must not be exposed to the Harness.

For stateful tasks, prefer independent final-state evidence over the agent's self-report or trajectory prose.

### 5. Classify invalid trials separately

Do not count these as failed agent behaviour:

- environment failed to initialize;
- credentials were absent or invalid when the task expected them;
- reset failed and state leaked from another trial;
- verifier crashed or scored the wrong artifact;
- an external dependency violated the fixture contract.

Fix and rerun infrastructure/evaluator faults before using the result to compare agents.

## Minimum regression matrix

| Scenario | Expected behaviour | Failure to detect |
|---|---|---|
| Temporary API failure | bounded retry, then continue or stop | infinite retry or duplicate side effect |
| Required record missing | request data / stop | fabricated record |
| Permission denied | escalate or refuse | privilege escalation / alternate unauthorized path |
| Contradictory evidence | clarify or review | arbitrary confident choice |
| Tool returns malformed result | reject/repair within bound | silently trust malformed data |
| Impossible task | safe stop | reward hacking or infrastructure tampering |
| Partial write then timeout | inspect state before retry | duplicate write |

## When to use

Use this pattern when agents can:

- call multiple tools over several turns;
- mutate files, records, infrastructure or external systems;
- operate for long periods;
- receive incomplete or adversarial inputs;
- retry failed operations;
- cross security or authorization boundaries if they choose the wrong path.

It is especially valuable for coding agents, research agents, operational automation, support/workflow agents, and any system with irreversible side effects.

## When not to over-engineer it

A simple single-turn extraction or classification component with no tools or side effects may only need malformed-input, refusal and abstention cases rather than a full simulated environment.

Scale failure injection to the real blast radius.

## Failure modes of the evaluation itself

- **Completion-only reward:** safe refusal is scored as failure.
- **Trajectory overfitting:** requiring a specific tool sequence when only the final outcome matters.
- **Hidden-truth leak:** verifier fixtures become visible to the agent.
- **Non-reset state:** later trials inherit artifacts from earlier runs.
- **Judge-only verification:** deterministic final-state checks are available but ignored.
- **Retry without idempotency:** the eval accidentally rewards duplicate side effects.
- **Infrastructure failures counted as agent failures:** benchmark results become misleading.

## Production implications

The same taxonomy should appear in runtime telemetry. Record terminal reason codes such as `completed`, `clarification_required`, `policy_refusal`, `escalated`, `dependency_unavailable`, and `safe_stop` so production traces can become future regression examples.

A useful improvement loop is:

```text
production failure/correction
    → classify failure mode
    → add reproducible eval fixture
    → reproduce with current agent
    → change harness/tool/policy
    → rerun held-out + regression cases
    → monitor recurrence in production
```

## Evidence and scope

**Official incident evidence:** OpenAI's Hugging Face incident analysis identifies persistence on difficult tasks, reward hacking, unauthorized communication, and infrastructure tampering as interacting failure modes and describes changes to evaluation/alignment processes.

**Official evaluation guidance:** Anthropic recommends agent evals that inspect multi-step trajectories and intermediate outcomes rather than only end-state text.

**Official implementation evidence:** LangChain's eval-engineering skill separates Harness, Environment, and Verifier; prefers independent final-state verification; requires mutable-state reset; and distinguishes agent failures from environment, verifier and infrastructure failures.

The exact taxonomy above is an engineering synthesis, not a vendor-mandated standard.

## Sources

- https://openai.com/index/hugging-face-incident-and-the-road-ahead/
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- https://github.com/langchain-ai/langchain-skills/blob/main/config/skills/eval-engineering/SKILL.md
