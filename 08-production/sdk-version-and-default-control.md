---
status: current
last_verified: 2026-08-09
source_priority: official
vendors:
  - openai
review_frequency: monthly
applies_to:
  - production
  - agents
  - reliability
---

# SDK Version and Default Control

## Recommendation

**[Official release policy + engineering inference]**

Treat rapidly evolving pre-1.0 agent SDKs as behaviour-bearing dependencies, not passive libraries. Pin versions, configure models and reasoning behaviour explicitly, and require regression evidence before upgrades.

A production deployment should not silently change because an SDK release changes:

- the default model;
- reasoning effort or verbosity;
- refusal handling;
- tool error propagation;
- handoff history;
- synchronous execution semantics;
- supported runtime versions;
- MCP session behaviour;
- sandbox path or materialisation rules.

## Current verification snapshot

As verified on **2026-08-09**, the OpenAI Agents SDK release documentation still uses modified semantic versioning in the form `0.Y.Z`:

- minor `Y` releases may include breaking changes to public non-beta interfaces;
- patch `Z` releases are intended for non-breaking changes;
- the official changelog currently includes releases through `0.18.0`;
- `0.18.0` changed the default Realtime model to `gpt-realtime-2.1` without an interface-breaking change;
- recent minor releases also changed sandbox boundaries, runtime support, MCP behaviour, handoff behaviour and model defaults.

The exact latest version is a point-in-time observation, not a durable recommendation. Always re-check the official changelog before upgrading.

## Why this matters

Even when an API remains source-compatible, a changed model default or error path can alter quality, latency, cost, retries, security boundaries and user-visible outcomes.

A minor version may be used for a default change even when no public interface is broken. Therefore, do not assume that "no breaking API change" means "no behavioural change."

## Required controls

### Pin dependencies

Use an exact version or a controlled lockfile in deployed applications.

```text
openai-agents==0.Y.Z
```

Do not use an unconstrained dependency such as `>=0.Y` in a production service.

### Configure models explicitly

Set the production model in configuration rather than relying on SDK defaults.

Also make explicit any behaviour that affects quality or cost, including:

- reasoning effort;
- verbosity;
- temperature where supported;
- turn limits;
- timeout and retry policy;
- tool failure handling;
- handoff-history behaviour;
- Realtime transport and model;
- sandbox grants and materialisation roots.

### Separate upgrade from deployment

An SDK upgrade should be a reviewed change with:

1. changelog and migration-note review;
2. lockfile diff;
3. unit and contract tests;
4. recorded-agent regression evaluation;
5. cost and latency comparison;
6. security-boundary review where sandbox, tools or MCP changed;
7. canary or staged deployment;
8. rollback plan.

### Test failure semantics

Regression suites should explicitly cover:

- model refusal;
- malformed structured output;
- tool timeout and tool error;
- MCP disconnect and reconnection;
- maximum-turn handling;
- cancellation;
- handoff context;
- duplicate or concurrent writes;
- sandbox path, symlink and archive safety;
- Realtime session and default-model behaviour where applicable.

### Capture runtime provenance

Each trace or execution record should include:

- application version;
- SDK version;
- model identifier;
- effective model settings;
- prompt and tool-schema version;
- evaluation or release identifier;
- sandbox or policy configuration version where tools can modify state.

Without provenance, a behaviour regression cannot be reliably attributed to code, model, prompt, SDK, policy or infrastructure changes.

## Upgrade decision table

| Change type | Minimum response |
|---|---|
| Patch release with bug fixes | Review notes, run focused regression tests |
| Minor pre-1.0 release | Treat as potentially interface- or behaviour-breaking; run full regression and staged rollout |
| Default model change | Set model explicitly; compare quality, latency and cost |
| Tool or MCP failure change | Re-run failure-path, reconnect and retry tests |
| Runtime support change | Update CI matrix and deployment image |
| Refusal or structured-output change | Re-run safety, abstention and schema-recovery tests |
| Sandbox or path-boundary change | Re-run path traversal, symlink, mount and grant-boundary tests |

## Anti-patterns

### Floating production dependencies

A rebuild can produce different runtime behaviour without a source-code change.

### Implicit default model

A library update can change model quality, cost, latency and reasoning behaviour.

### Happy-path-only upgrade testing

Most agent regressions appear in tool errors, refusals, retries, handoffs, state restoration, Realtime sessions and sandbox boundaries rather than simple single-turn responses.

### No version data in traces

Operational incidents become difficult to reproduce or compare.

## Validation checklist

- [ ] Production SDK and transitive dependencies are locked.
- [ ] Model and important model settings are explicit.
- [ ] Upgrade PRs link to official release notes.
- [ ] Behavioural evals cover success and failure paths.
- [ ] Sandbox and tool-boundary changes receive security regression tests.
- [ ] Cost and latency are compared before rollout.
- [ ] Traces include SDK, model, prompt, tool-schema and policy versions.
- [ ] A rollback path is tested.

## Source

**[Official OpenAI SDK release policy and changelog]**

- https://openai.github.io/openai-agents-python/release/

## Scope note

The examples are based on the OpenAI Agents SDK, but the control pattern applies to any rapidly evolving agent framework or model abstraction layer.
