---
status: current
last_verified: 2026-08-31
source_priority: official
vendors:
  - anthropic
review_frequency: quarterly
applies_to:
  - production
  - agents
  - security
---

# Agent Capability Containment

## Recommendation

**[Official recommendation + engineering synthesis]**

Protect agentic systems by limiting what the agent can technically access and change. Human approval remains useful for high-impact decisions, but repeated permission prompts must not be the primary security boundary.

Containment should survive:

- a mistaken approval;
- prompt injection;
- malicious repository or document content;
- model misinterpretation;
- tool-selection errors;
- compromised downstream data.

## Threat model

An agent may receive instructions or configuration from untrusted sources while holding access to:

- filesystems;
- shells and subprocesses;
- internal APIs;
- cloud identities;
- source repositories;
- network destinations;
- production or administrative operations.

The core risk is not only the probability of a bad action, but the maximum damage the agent is capable of causing.

## Control hierarchy

### 1. Establish trust before loading local behaviour

Treat repository files, workspace configuration, hooks, plugins, localhost listeners, and generated instructions as untrusted until the user or system has explicitly established trust.

Do not execute project-local hooks or parse behaviour-changing configuration before the trust decision.

### 2. Apply least-privilege identity

- Use workload identity or short-lived credentials where available.
- Separate read, write, approval, and administrative identities.
- Scope credentials to the minimum resources and operations.
- Do not expose broad tokens inside model-visible context.

### 3. Isolate filesystem and process access

- Make the default workspace read-only where practical.
- Permit writes only to explicit directories.
- Run generated code and shell commands in a sandbox or disposable environment.
- Block access to host secrets, credential stores, sockets, and unrelated mounts.
- Treat archive extraction, symlinks, and path traversal as security-sensitive operations.

### 4. Control network egress

- Deny network access by default for tools that do not require it.
- Allowlist destinations, ports, methods, and protocols.
- Route sensitive outbound requests through an auditable proxy or gateway.
- Prevent access to metadata services and internal control planes unless explicitly required.

### 5. Gate irreversible actions separately

Require a distinct policy decision for actions such as:

- sending external communications;
- deploying to production;
- deleting or overwriting durable data;
- modifying permissions;
- approving payments or claims;
- executing administrative changes.

Approval should display the proposed action, target, relevant diff or payload, and expected consequence—not merely a generic tool name.

### 6. Observe allowed and blocked behaviour

Record:

- requested tool and arguments;
- identity and policy decision;
- permitted and blocked resources;
- execution result;
- human override;
- correlation and trace identifiers.

Do not place secrets or unnecessary personal data in logs.

## Reference architecture

```mermaid
flowchart LR
    U[Untrusted input] --> G[Trust and policy gateway]
    G -->|Rejected| Q[Quarantine]
    G -->|Accepted| A[Agent runtime]
    A --> F[Filesystem sandbox]
    A --> N[Egress allowlist]
    A --> I[Scoped identity]
    A --> H[High-impact action gate]
    F --> X[Tool execution]
    N --> X
    I --> X
    H --> X
    X --> O[Trace and audit store]
```

## Action-level authorization and boundary verification

**[Engineering synthesis supported by official containment guidance and incident evidence]** Capability containment limits the maximum reachable blast radius; it does **not** prove that a specific reachable action is authorized. Before an external side effect, normalize the proposed action and check its **resource/destination, authenticated acting identity, operation, data scope, and applicable constraints** against policy facts independent of the actor's narrative. An accessible URL, inherited credential, listed tool, or successful connection is not authorization evidence.

A practical enforcement flow is:

```text
agent proposes action
  -> canonical action record (principal, resource, verb, payload class, run ID)
  -> independent policy decision: allow / deny / escalate
  -> constrained executor (no broader credentials than needed)
  -> receipt + policy decision + correlation ID in audit trail
```

The policy decision should be made at the actual execution boundary, not solely in a prompt or a self-review by the same agent. A separate reviewer can help with ambiguous cases, but deterministic authorization rules should not be delegated to a probabilistic reviewer.

**Test the deployed boundary, not merely its configuration:** run an allowed probe that must reach its intended endpoint and a denied probe that must not reach it. Correlate policy-decision telemetry with independently observed destination effects. A generic HTTP 403, DNS failure, or TLS error does not alone demonstrate that the intended policy enforced the denial. Repeat tests across alternate tools, redirects, and indirect paths that could reach the same side effect.

These are **engineering test recommendations**, not claims that any particular hosted egress preview is production-ready. Preview implementations must be separately assessed for production suitability.

### Additional validation cases

- [ ] A reachable but out-of-scope resource is denied even when the actor asserts it is authorized.
- [ ] An allowed destination with the wrong acting identity or forbidden payload is denied.
- [ ] Allowed and denied probes validate policy telemetry **and** independent destination receipts.
- [ ] Alternate tools and redirects cannot bypass the same action policy.
- [ ] Missing/ambiguous authorization fails closed or escalates without attempting the side effect.

**Evidence:** Anthropic's containment engineering analysis and real-world evaluation-environment incidents demonstrate the limits of relying on model interpretation and permissive environments; Microsoft's hosted-agent egress guidance illustrates separate destination controls and behavioural verification. The general action contract above is a cross-source engineering synthesis.

- https://www.anthropic.com/research/how-we-contain-claude
- https://www.anthropic.com/news/security
- https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/egress-control

## When to use

Apply this pattern whenever an agent can execute code, modify state, use credentials, call external services, or process instructions from sources outside the trusted control plane.

## When this is insufficient

Containment does not replace:

- secure tool implementation;
- input and output validation;
- prompt-injection defences;
- model and workflow evaluation;
- business authorization;
- data governance;
- incident response.

## Common anti-patterns

### Approval prompt as the only defence

Users become habituated to repeated prompts and may approve risky actions without reviewing the details.

### Full host access for convenience

A tool that can read the whole host, reach arbitrary network destinations, and inherit developer credentials creates an unnecessarily large blast radius.

### Trust after execution

Loading hooks, plugins, or project-local configuration before establishing workspace trust invalidates the later approval boundary.

### Broad shared credentials

A single credential that can read and write across development, test, and production makes policy enforcement and audit attribution difficult.

## Validation checklist

- [ ] Untrusted configuration cannot execute before trust is established.
- [ ] The agent has no implicit access to developer or host credentials.
- [ ] Filesystem write paths are explicit and testable.
- [ ] Network egress is denied or allowlisted.
- [ ] High-impact actions have a separate policy gate.
- [ ] Blocked actions are included in telemetry.
- [ ] Adversarial tests attempt path traversal, symlink escape, prompt injection, credential access, and unauthorized egress.
- [ ] The maximum credible blast radius is documented in the threat model.

## Sources

**[Official Anthropic engineering guidance]**

- https://www.anthropic.com/engineering/how-we-contain-claude
- https://www.anthropic.com/engineering/claude-code-sandboxing
- https://www.anthropic.com/engineering/claude-code-auto-mode

## Verification result — 2026-08-31

Anthropic's current containment guidance still supports the core recommendation: enforce hard capability boundaries across the agent environment, model layer, and external content/tool inputs, and do not rely on repeated human approval as the sole defence. The current engineering report continues to cite roughly 93% approval rates, while the sandboxing report states an 84% reduction in permission prompts in internal use. No change to the durable recommendation is required.

## Project evidence

None recorded yet. Add project-specific evidence only after sanitisation and validation.
