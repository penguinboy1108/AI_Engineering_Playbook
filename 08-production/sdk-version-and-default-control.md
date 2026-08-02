---
status: current
last_verified: 2026-08-02
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
- sandbox or workspace safety behaviour.

## Current evidence

The OpenAI Agents SDK still uses `0.Y.Z` versioning. Its official release policy states that minor `Y` releases can include breaking changes to public, non-beta interfaces and recommends pinning when breaking changes are unacceptable.

The current changelog also demonstrates why explicit configuration matters. Recent minor releases have changed default models, surfaced refusals through a dedicated error path, changed MCP/tool failure behaviour, altered handoff semantics, and tightened sandbox path handling. A release can therefore change quality, cost, latency, security, or error handling even when application source code is unchanged.

## Required controls

### Pin dependencies

Use an exact version or controlled lockfile in deployed applications.

```text
openai-agents==0.Y.Z
```

Do not use an unconstrained dependency such as `>=0.Y` in a production service.

### Configure behaviour explicitly

Set the production model in configuration rather than relying on SDK defaults. Also make explicit any behaviour affecting quality or cost, including:

- reasoning effort;
- verbosity;
- temperature where supported;
- turn limits;
- timeout and retry policy;
- tool failure handling;
- refusal handling;
- handoff-history behaviour.

### Separate upgrade from deployment

An SDK upgrade should be a reviewed change with:

1. changelog and migration-note review;
2. lockfile diff;
3. unit and contract tests;
4. recorded-agent regression evaluation;
5. failure-path tests;
6. cost and latency comparison;
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
- sandbox path, archive, and symlink safety.

### Capture runtime provenance

Each trace or execution record should include:

- application version;
- SDK version;
- model identifier;
- effective model settings;
- prompt and tool-schema version;
- evaluation or release identifier.

Without provenance, a behaviour regression cannot be reliably attributed to code, model, prompt, SDK, or infrastructure changes.

## Upgrade decision table

| Change type | Minimum response |
|---|---|
| Patch release with bug fixes | Review notes and run focused regression tests |
| Minor pre-1.0 release | Treat as potentially breaking; run full regression and staged rollout |
| Default model change | Set model explicitly; compare quality, latency, and cost |
| Tool or MCP failure change | Re-run failure-path and retry tests |
| Runtime support change | Update CI matrix and deployment image |
| Refusal or structured-output change | Re-run safety, abstention, and schema-recovery tests |
| Sandbox or workspace change | Re-run path traversal, mount, archive, and permission-boundary tests |

## Anti-patterns

- Floating production dependencies
- Implicit default models or reasoning settings
- Happy-path-only upgrade testing
- Missing SDK/model provenance in traces
- Treating a non-breaking source change as proof of unchanged behaviour

## Validation checklist

- [ ] Production SDK and transitive dependencies are locked.
- [ ] Model and important model settings are explicit.
- [ ] Upgrade PRs link to official release notes.
- [ ] Behavioural evals cover success and failure paths.
- [ ] Cost and latency are compared before rollout.
- [ ] Traces include SDK, model, prompt, and tool-schema versions.
- [ ] Security boundaries are retested when sandbox or tool behaviour changes.
- [ ] A rollback path is tested.

## Source

**[Official OpenAI SDK release policy and changelog]**

- https://openai.github.io/openai-agents-python/release/

## Scope note

The examples are based on the OpenAI Agents SDK, but the control pattern applies to any rapidly evolving agent framework or model abstraction layer.
