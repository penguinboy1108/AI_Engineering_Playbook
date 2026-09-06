---
status: current
last_verified: 2026-09-07
source_priority: official
vendors:
  - openai
review_frequency: quarterly
applies_to:
  - production
  - agents
  - reliability
---

# SDK Version and Default Control

## Recommendation

**[Official release policy + engineering inference]**

Treat rapidly evolving agent SDKs and orchestration frameworks as behaviour-bearing runtime dependencies, not passive libraries. Pin deployed versions, configure important behaviour explicitly, and require regression evidence before upgrades.

The durable risk is not the version number itself. A dependency upgrade can silently change:

- default model or model settings;
- tool-call and error semantics;
- refusal and guardrail behaviour;
- retries, timeouts and cancellation;
- handoff and session history;
- checkpoint, resume and persistence behaviour;
- MCP transport or lifecycle;
- sandbox, path, mount or workspace rules;
- provider/client construction;
- tracing, redaction or replayable state;
- supported runtime or HTTP transport.

## Why this matters

The OpenAI Agents SDK currently documents `0.Y.Z` versioning in which minor versions may contain breaking changes to public non-beta interfaces. Its changelog has also repeatedly included changes to defaults, state handling, provider construction, sandboxing, MCP and error semantics.

This page intentionally does **not** track the latest point release. Point-in-time release facts belong in upgrade PRs, maintenance records and vendor changelogs. Canonical playbook guidance should remain useful after the next release ships.

Current OpenAI documentation also demonstrates why model defaults must be treated as configuration rather than architecture: an agent that does not specify a model inherits the SDK's current default, and that default can change independently of application source code.

## Required controls

### 1. Lock the deployed dependency graph

Use an exact version or a reviewed lockfile for production deployments.

```text
openai-agents==0.Y.Z
```

Avoid unconstrained ranges such as `>=0.Y` for deployed services when a minor update may alter public interfaces or behaviour.

Store the lockfile with the application and make dependency changes visible in code review.

### 2. Configure behaviour explicitly

Do not inherit behaviour that materially affects quality, cost, safety or state correctness when it can be configured explicitly.

Depending on the framework, make these explicit:

- model identifier;
- reasoning effort / verbosity and other material model settings;
- maximum turns;
- timeout and retry policy;
- tool failure handling;
- refusal and guardrail behaviour;
- handoff-history policy;
- session/checkpoint persistence;
- sandbox grants, mounts and workspace roots;
- provider/client and organization/project scope;
- transport or endpoint configuration.

### 3. Separate dependency upgrade from feature rollout

An SDK/framework upgrade should be a reviewable engineering change with:

1. official changelog and migration-note review;
2. lockfile diff;
3. unit and contract tests;
4. deterministic runtime tests where available;
5. behavioural regression evals;
6. provider/integration tests;
7. state and recovery tests;
8. security-boundary review when tools, sandboxes, MCP or persistence changed;
9. cost and latency comparison where relevant;
10. staged rollout and tested rollback.

Do not combine a framework upgrade, model migration, prompt rewrite and major feature change into one rollout unless the risk is intentionally accepted; doing so makes regressions difficult to attribute and rollback difficult to isolate.

### 4. Test failure and state semantics

Happy-path text output is insufficient for an agent runtime upgrade. Cover the boundaries the runtime owns.

Recommended regression groups:

- refusal and malformed structured output;
- terminal provider failures and incomplete responses;
- tool timeout, tool error and duplicate calls;
- MCP disconnect/reconnect and capability enumeration;
- cancellation and maximum-turn handling;
- retry and backoff behaviour;
- handoff context and session-history preservation;
- interruption, approval and resume state;
- independent checkpoint isolation;
- duplicate/concurrent writes and idempotency;
- persisted-state redaction and replay behaviour;
- sandbox path traversal, symlinks, archives, mounts and grants;
- provider/client construction and custom transport compatibility.

If the SDK exposes deterministic testing utilities, use them to improve repeatability, but do not let them replace integration tests across the real provider, authentication, transport and tool boundaries you depend on.

### 5. Capture runtime provenance

A trace or execution record should make a behaviour regression attributable.

Capture where appropriate:

- application build/version;
- SDK/framework and provider-client versions;
- model identifier and effective settings;
- prompt/instruction version;
- tool-schema and MCP-server version;
- policy/guardrail version;
- evaluation/release identifier;
- sandbox/workspace policy version.

Without provenance, a production regression may be impossible to separate among application code, prompt, model, SDK, provider or infrastructure changes.

## Upgrade decision table

| Change type | Minimum response |
|---|---|
| Patch release | Review notes and run focused regression tests |
| Pre-1.0 minor release | Treat as potentially breaking; run broad behavioural regression and staged rollout |
| Default model/settings change | Configure explicitly and compare quality, latency and cost |
| Tool/MCP/retry change | Re-run failure, reconnect, replay and idempotency tests |
| Runtime/transport change | Update CI/runtime image and integration tests |
| Refusal/structured-output change | Re-run safety, abstention and schema-recovery tests |
| Sandbox/path/mount change | Re-run traversal, credential and grant-boundary tests |
| State/approval/persistence change | Re-run interruption, resume, replay, redaction and checkpoint tests |
| Provider configuration change | Validate explicit-client construction and reject ambiguous configuration |

## Anti-patterns

### Tracking the latest SDK version as canonical knowledge

A version snapshot ages quickly and encourages monthly documentation churn without improving engineering decisions. Link to the vendor changelog at upgrade time instead.

### Floating runtime dependencies

A rebuild can change production behaviour without an application-code change.

### Implicit model defaults

A dependency release can alter quality, latency or cost even when the application did not intentionally migrate models.

### Happy-path-only upgrade tests

Agent-runtime regressions commonly appear in retries, interruption/resume, tool boundaries, persistence and error handling rather than in a one-turn success case.

### No provenance in traces

A regression cannot be reproduced or attributed reliably.

## Validation checklist

- [ ] Production dependencies are locked.
- [ ] Model and important behaviour-bearing settings are explicit.
- [ ] Upgrade PRs link to official release/migration notes.
- [ ] Behavioural evals cover success, failure and recovery paths.
- [ ] State/checkpoint semantics are tested when the runtime owns persistence.
- [ ] Provider/client and real integration boundaries are covered.
- [ ] Tool, sandbox and MCP changes receive security regression tests.
- [ ] Cost and latency are compared when they can materially change.
- [ ] Traces include enough provenance to attribute a regression.
- [ ] Rollback is possible and tested for consequential deployments.

## Sources

**[Official OpenAI SDK documentation]**

- https://openai.github.io/openai-agents-python/release/
- https://openai.github.io/openai-agents-python/models/

## Scope note

The examples are grounded in the OpenAI Agents SDK, but the control pattern applies to rapidly evolving agent frameworks, model abstraction layers and orchestration runtimes generally.
