# Deprecation and Supersession Registry

Use this registry to prevent outdated APIs, SDKs, models, services and design patterns from remaining active grounding material.

## Evidence threshold

Add an active entry only when an official lifecycle notice, official product page, official release note or official migration guide clearly identifies the affected item, lifecycle status, date and supported migration path.

Community discussion or indirect evidence may trigger investigation but is not sufficient for an active entry.

## Active entries

### Azure OpenAI Assistants API (classic)

- Registry ID: azure-openai-assistants-api-2026-08-26
- Status: retirement-announced; retirement date passed, current operational status requires validation
- Vendor: Microsoft
- First recorded: 2026-08-09
- Effective or retirement date: 2026-08-26
- Last verified: 2026-08-31
- Replacement: Generally available Microsoft Foundry Agents Service; use Responses API directly for non-agentic inference where appropriate
- Official source: https://learn.microsoft.com/en-us/azure/foundry-classic/openai/concepts/assistants
- Migration impact: Inventory `/assistants`, `/threads` and `/runs` usage; migrate state, tools and evaluation coverage; verify region support for Responses API and current Foundry Agents before cutover.
- Notes: The documented retirement date has passed. Microsoft's current public documentation still presents the lifecycle notice as "will be retired on August 26, 2026" rather than explicitly confirming post-retirement service behaviour. Do not infer continued support or availability from stale wording; treat any remaining dependency as unsupported-risk work and validate the exact deployed surface immediately. This date is distinct from the retirement date for Foundry Agents (classic).

### Azure AI Inference beta SDK for current Microsoft Foundry Models

- Registry ID: azure-ai-inference-beta-sdk-2026-08-26
- Status: retirement-announced; retirement date passed, current operational status requires validation
- Vendor: Microsoft
- First recorded: 2026-08-09
- Effective or retirement date: 2026-08-26
- Last verified: 2026-08-31
- Replacement: Generally available OpenAI/v1 API with a stable OpenAI SDK
- Official source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/endpoints
- Migration impact: Replace beta SDK usage; verify endpoint, authentication, streaming, structured outputs, errors, telemetry, latency and cost.
- Notes: The current Foundry Models endpoint page still states that the Azure AI Inference beta SDK "will be retired on August 26, 2026", although that date has now passed. A separate classic migration page still mentions May 30, 2026 for the `azure-ai-inference` package. Treat the exact package and endpoint surface as the unit of lifecycle verification. Do not assume that a package continuing to install or an endpoint still responding means it remains supported.

### Microsoft Foundry Workflows visual experience

- Registry ID: microsoft-foundry-workflows-2026-12-01
- Status: retirement-announced
- Vendor: Microsoft
- First recorded: 2026-08-09
- Effective or retirement date: 2026-12-01
- Last verified: 2026-08-31
- Replacement: Microsoft Agent Framework for new workflow authoring
- Official source: https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow
- Migration impact: Do not start new production systems on the Preview visual workflow experience. Migrate orchestration logic, branching, human approvals and tests to supported code-first definitions before retirement.
- Notes: Microsoft currently states that after December 1, 2026 the visual designer and in-portal workflow execution are unsupported, while YAML-based workflow definitions can continue when deployed as hosted agents. Validate the exact migration path for each workload.

### Microsoft Foundry Agents (classic)

- Registry ID: microsoft-foundry-agents-classic-2027-03-31
- Status: retirement-announced
- Vendor: Microsoft
- First recorded: 2026-08-09
- Effective or retirement date: 2027-03-31
- Last verified: 2026-08-31
- Replacement: Generally available Microsoft Foundry Agents Service
- Official source: https://learn.microsoft.com/en-us/azure/foundry-classic/agents/whats-new
- Migration impact: New implementations should use the current service. Existing classic agents need API, SDK, identity, network, tool and regression review before cutover.
- Notes: Documentation marked `foundry-classic` must not be treated as the default implementation path.

### Microsoft Prompt Flow in Foundry and Azure Machine Learning

- Registry ID: microsoft-prompt-flow-2027-04-20
- Status: retirement-announced
- Vendor: Microsoft
- First recorded: 2026-08-09
- Effective or retirement date: 2027-04-20
- Last verified: 2026-08-31
- Replacement: Microsoft Agent Framework and supported deployment, evaluation and observability components
- Official source: https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/migrate-prompt-flow-to-agent-framework?view=azureml-api-2
- Migration impact: Prompt Flow is not recommended for new development. Inventory flows, evaluations, deployments and runtime images; rebuild and parity-test before migration.
- Notes: Microsoft states that Prompt Flow runtime images no longer receive updates, including security and package updates.

## Required repository updates

When an entry is added:

1. update affected pages and lifecycle wording;
2. update `catalog.yaml` where the item is referenced;
3. add migration and rollback considerations;
4. update `CHANGELOG.md`;
5. add a retrieval eval if stale guidance could still be selected.

## Investigations awaiting official evidence

### Azure OpenAI Assistants API post-retirement state

The documented retirement date of August 26, 2026 has passed, but the current official page still uses pre-retirement wording and does not explicitly describe post-retirement request behaviour. The repository therefore does not assert that the API is technically unavailable; it records that the supported lifecycle date has passed and affected workloads require immediate project-level validation and migration.

### Azure AI Inference lifecycle scope

Microsoft currently exposes different dates on current Foundry Models endpoint documentation and a classic migration page. The current endpoint page still states August 26, 2026 for the named beta SDK surface, while the classic migration guidance states May 30, 2026 for the `azure-ai-inference` package. Both dates have passed. Keep the discrepancy explicit and verify the exact package, API surface and endpoint used by each project before migration or support claims.
