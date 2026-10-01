---
status: current
last_verified: 2026-08-31
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
- retry, session or provider behaviour;
- provider configuration validation;
- persisted or replayable error state.

## Current verification snapshot

As verified on **2026-08-31**, the OpenAI Agents SDK release policy still uses modified semantic versioning in the form `0.Y.Z`:

- minor `Y` releases can include breaking changes to public non-beta interfaces;
- patch `Z` releases are intended for non-breaking changes, new features, private-interface changes and beta updates;
- the latest official release remains **`v0.22.0`**, published **2026-08-19**;
- `v0.22.0` tightens failure handling and data isolation: terminal function-tool output rejected by output guardrails is redacted from replayable and persisted SDK state; failed or incomplete non-streaming Responses raise `ModelBehaviorError`; usage accounting is isolated between independent `RunState` checkpoints; and conflicting provider configuration is rejected when `OpenAIProvider` is constructed with an explicit `openai_client`;
- applications that pass an explicit `openai_client` together with `organization` or `project` must move those values into the `AsyncOpenAI` client instead of supplying duplicate provider arguments;
- `v0.21.0` introduced the OpenAI Python v3 / HTTPX2 migration and provider-neutral deterministic testing utilities, so custom HTTP transports still require explicit migration review;
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
- session persistence and provider-specific retry behaviour;
- provider client, organization/project scope and custom HTTP transport.

When supplying an explicit OpenAI client, keep organization/project configuration on that client rather than duplicating it at the provider layer.

### Separate upgrade from deployment

An SDK upgrade should be a reviewed change with:

1. changelog and migration-note review;
2. lockfile diff;
3. unit and contract tests;
4. deterministic runtime tests where the SDK supports them;
5. recorded-agent regression evaluation;
6. provider/client configuration tests;
7. cost and latency comparison;
8. security-boundary review where sandbox, tools, MCP or persisted state changed;
9. canary or staged deployment;
10. rollback plan.

### Test failure and state semantics

Regression suites should cover:

- model refusal and malformed structured output;
- terminal Responses with `failed` or `incomplete` status;
- tool timeout, tool error and duplicate calls;
- output-guardrail rejection and whether sensitive terminal tool output persists or replays;
- MCP disconnect, reconnect and resource enumeration;
- cancellation, maximum turns and provider retries;
- handoff context and session-history preservation;
- duplicate or concurrent writes;
- interruption, approval and resume state;
- independent checkpoint usage/accounting isolation;
- sandbox path, symlink, archive, mount and resume safety;
- Realtime session and default-model behaviour;
- explicit-client provider configuration and custom HTTP transport compatibility.

### Capture runtime provenance

Each trace or execution record should include:

- application and SDK version;
- model identifier and effective settings;
- prompt and tool-schema version;
- evaluation or release identifier;
- provider/client configuration version where behaviour depends on custom transport or scope;
- sandbox, mount and policy configuration version where tools can modify state.

## Upgrade decision table

| Change type | Minimum response |
|---|---|
| Patch release | Review notes and run focused regression tests |
| Minor pre-1.0 release | Treat as potentially interface- or behaviour-breaking; run full regression and staged rollout |
| Default model change | Set model explicitly; compare quality, latency and cost |
| Tool, MCP or retry change | Re-run failure-path, reconnect, replay and idempotency tests |
| Runtime or HTTP transport change | Update CI/deployment image and custom-client integration tests |
| Refusal or structured-output change | Re-run safety, abstention and schema-recovery tests |
| Sandbox, mount or path change | Re-run traversal, symlink, credential, mount and grant-boundary tests |
| State, approval or persistence change | Re-run interruption, resume, replay, redaction and checkpoint-isolation tests |
| Provider configuration contract change | Validate explicit-client construction and reject ambiguous duplicate configuration |

## Validation checklist

- [ ] Production SDK and transitive dependencies are locked.
- [ ] Model and important model settings are explicit.
- [ ] Upgrade PRs link to official release notes.
- [ ] Behavioural evals cover success, failure and state-restoration paths.
- [ ] Deterministic SDK test utilities are used where they improve repeatability without replacing end-to-end provider tests.
- [ ] Provider/client configuration is explicit and covered by integration tests.
- [ ] Sandbox, mount, tool-boundary and persisted-state changes receive security regression tests.
- [ ] Cost and latency are compared before rollout.
- [ ] Traces include SDK, model, prompt, tool-schema and policy versions.
- [ ] A rollback path is tested.

## Sources

**[Official OpenAI SDK release policy and releases]**

- https://openai.github.io/openai-agents-python/release/
- https://github.com/openai/openai-agents-python/releases/tag/v0.22.0

## Scope note

The examples are based on the OpenAI Agents SDK, but the control pattern applies to any rapidly evolving agent framework or model abstraction layer.
