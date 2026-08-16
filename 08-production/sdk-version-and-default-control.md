---
status: current
last_verified: 2026-08-16
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
- supported runtime versions;
- MCP session behaviour;
- sandbox path or materialisation rules;
- retry, session or provider behaviour.

## Current verification snapshot

As verified on **2026-08-16**, the OpenAI Agents SDK release policy still uses modified semantic versioning in the form `0.Y.Z`:

- minor `Y` releases can include breaking changes to public non-beta interfaces;
- patch `Z` releases are intended for non-breaking changes, new features, private-interface changes and beta updates;
- the latest official GitHub release is `v0.21.0`, published 2026-08-15;
- `v0.21.0` adds provider-neutral deterministic testing utilities for Agent, Sandbox, Realtime and Voice workflows, OpenAI Python v3 compatibility, and additional hardening around interruption snapshots, recursive approvals, MCP lifecycle isolation, retry backoff, sandbox path grants and sensitive-error redaction;
- earlier recent releases changed default models, refusal handling, sandbox boundaries, runtime support, MCP behaviour and handoff behaviour.

The exact latest version is a point-in-time observation, not a durable recommendation. Re-check the official release page before every upgrade.

## Required controls

### Pin dependencies

Use an exact version or a controlled lockfile in deployed applications.

```text
openai-agents==0.Y.Z
```

Do not use an unconstrained dependency such as `>=0.Y` in a production service.

### Configure behaviour explicitly

Set the production model and behaviour-bearing options in configuration rather than relying on SDK defaults, including:

- reasoning effort and verbosity;
- turn limits, timeout and retry policy;
- tool failure and refusal handling;
- handoff-history behaviour;
- Realtime transport and model;
- sandbox grants, mounts and materialisation roots;
- session persistence and provider-specific retry behaviour.

### Separate upgrade from deployment

An SDK upgrade should be a reviewed change with:

1. changelog and migration-note review;
2. lockfile diff;
3. unit and contract tests;
4. deterministic runtime tests where the SDK supports them;
5. recorded-agent regression evaluation;
6. cost and latency comparison;
7. security-boundary review where sandbox, tools or MCP changed;
8. canary or staged deployment;
9. rollback plan.

### Test failure and state semantics

Regression suites should cover:

- model refusal and malformed structured output;
- tool timeout, tool error and duplicate calls;
- MCP disconnect, reconnect and resource enumeration;
- cancellation, maximum turns and provider retries;
- handoff context and session-history preservation;
- duplicate or concurrent writes;
- interruption, approval and resume state;
- sandbox path, symlink, archive, mount and resume safety;
- Realtime session and default-model behaviour.

### Capture runtime provenance

Each trace or execution record should include:

- application and SDK version;
- model identifier and effective settings;
- prompt and tool-schema version;
- evaluation or release identifier;
- sandbox, mount and policy configuration version where tools can modify state.

## Upgrade decision table

| Change type | Minimum response |
|---|---|
| Patch release | Review notes and run focused regression tests |
| Minor pre-1.0 release | Treat as potentially interface- or behaviour-breaking; run full regression and staged rollout |
| Default model change | Set model explicitly; compare quality, latency and cost |
| Tool, MCP or retry change | Re-run failure-path, reconnect, replay and idempotency tests |
| Runtime support change | Update CI matrix and deployment image |
| Refusal or structured-output change | Re-run safety, abstention and schema-recovery tests |
| Sandbox, mount or path change | Re-run traversal, symlink, credential, mount and grant-boundary tests |
| State or approval change | Re-run interruption, resume, replay and checkpoint-isolation tests |

## Validation checklist

- [ ] Production SDK and transitive dependencies are locked.
- [ ] Model and important model settings are explicit.
- [ ] Upgrade PRs link to official release notes.
- [ ] Behavioural evals cover success, failure and state-restoration paths.
- [ ] Deterministic SDK test utilities are used where they improve repeatability without replacing end-to-end provider tests.
- [ ] Sandbox, mount and tool-boundary changes receive security regression tests.
- [ ] Cost and latency are compared before rollout.
- [ ] Traces include SDK, model, prompt, tool-schema and policy versions.
- [ ] A rollback path is tested.

## Sources

**[Official OpenAI SDK release policy and releases]**

- https://openai.github.io/openai-agents-python/release/
- https://github.com/openai/openai-agents-python/releases

## Scope note

The examples are based on the OpenAI Agents SDK, but the control pattern applies to any rapidly evolving agent framework or model abstraction layer.
