# Deprecation and Supersession Registry

Use this registry to prevent outdated APIs, SDKs, models, services, and design patterns from remaining active grounding material.

## Evidence threshold

Add an active entry only when an official lifecycle notice, official product page, official release note, or official migration guide clearly identifies:

- the affected product, API, SDK, model, service, or pattern;
- the lifecycle status;
- the effective or retirement date when applicable;
- the supported replacement or migration path when available.

A community discussion, search result, indirect statement, or missing UI element may trigger investigation but is not sufficient evidence for an active deprecation entry.

Unconfirmed lifecycle information belongs in a weekly digest or pull request under `needs-validation`.

## Entry template

```markdown
## Item name

- Registry ID:
- Status: deprecated | superseded | retirement-announced | retired
- Vendor:
- First recorded:
- Effective or retirement date:
- Last verified:
- Replacement:
- Official source:
- Migration impact:
- Affected playbook pages:
- Catalog entries updated:
- Notes:
```

## Required repository updates

When an entry is added:

1. update affected pages and their lifecycle wording;
2. update `catalog.yaml` document or product lifecycle fields;
3. set `superseded_by` where durable guidance was replaced;
4. add migration and rollback considerations;
5. update `CHANGELOG.md`;
6. add or update a retrieval eval if stale guidance could still be selected.

## Active entries

## Microsoft Foundry Agents (classic)

- Registry ID: microsoft-foundry-agents-classic-2027-03-31
- Status: retirement-announced
- Vendor: Microsoft
- First recorded: 2026-08-09
- Effective or retirement date: 2027-03-31
- Last verified: 2026-08-09
- Replacement: Generally available Microsoft Foundry Agents Service
- Official source: https://learn.microsoft.com/en-us/training/modules/intro-ai-agent-service-security-controls/
- Migration impact: New implementations should use the current Foundry Agents Service. Existing classic agents require migration planning, API and SDK review, regression evaluation, identity and network-control verification, and production cutover before retirement.
- Affected playbook pages: AI-103 learning material, future Foundry agent implementation pages, weekly digests that reference classic agents
- Catalog entries updated: none yet
- Notes: Documentation pages marked `foundry-classic` must not be treated as the default implementation path.

## Microsoft Prompt Flow in Foundry and Azure Machine Learning

- Registry ID: microsoft-prompt-flow-2027-04-20
- Status: retirement-announced
- Vendor: Microsoft
- First recorded: 2026-08-09
- Effective or retirement date: 2027-04-20
- Last verified: 2026-08-09
- Replacement: Microsoft Agent Framework and supported deployment/observability components
- Official source: https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/migrate-prompt-flow-to-agent-framework?view=azureml-api-2
- Migration impact: Prompt Flow is no longer recommended for new development. Existing YAML, evaluations and deployment behaviour should be inventoried, rebuilt, parity-tested and migrated. Prompt Flow runtime images are no longer receiving package or security updates according to Microsoft documentation.
- Affected playbook pages: future workflow orchestration, evaluation and deployment guidance
- Catalog entries updated: none yet
- Notes: Preserve historical project evidence, but mark Prompt Flow-specific implementation instructions as migration-only rather than current default guidance.

## Azure AI Inference beta SDK for current Microsoft Foundry Models

- Registry ID: azure-ai-inference-beta-sdk-2026-08-26
- Status: retirement-announced
- Vendor: Microsoft
- First recorded: 2026-08-09
- Effective or retirement date: 2026-08-26
- Last verified: 2026-08-09
- Replacement: Generally available OpenAI/v1 API with a stable OpenAI SDK
- Official source: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/endpoints
- Migration impact: Replace Azure AI Inference beta SDK usage, verify endpoint and authentication changes, pin the supported OpenAI SDK, and regression-test model invocation, streaming, structured output, errors, telemetry, latency and cost.
- Affected playbook pages: future Microsoft Foundry model-consumption and SDK guidance
- Catalog entries updated: none yet
- Notes: Microsoft classic documentation may show a different lifecycle date for older classic surfaces. This entry uses the current Foundry Models documentation and must not be generalized to every classic package without checking the exact product page.

## Investigations awaiting official evidence

None.
