# Deprecation and Supersession Registry

Use this registry to prevent outdated APIs, SDKs, models, services, and design patterns from remaining active grounding material.

## Entry template

```markdown
## Item name

- Status: deprecated | superseded | retirement-announced
- Vendor:
- First recorded:
- Effective or retirement date:
- Last verified:
- Replacement:
- Official source:
- Migration impact:
- Affected playbook pages:
- Notes:
```

## Active entries

## Microsoft Foundry Agent Service (classic)

- Status: retirement-announced
- Vendor: Microsoft
- First recorded: 2026-08-02
- Effective or retirement date: 2027-03-31
- Last verified: 2026-08-02
- Replacement: Generally available Microsoft Foundry Agents Service
- Official source: https://learn.microsoft.com/en-us/azure/foundry-classic/agents/whats-new
- Migration impact: Existing classic agents should be inventoried and migrated using Microsoft's current migration guidance before retirement. New projects should not start on the classic service.
- Affected playbook pages: Future Microsoft Foundry implementation pages and certification examples
- Notes: Documentation and examples must distinguish the classic portal/service from the current Foundry Agents Service.

## Microsoft Foundry Workflows

- Status: retirement-announced
- Vendor: Microsoft
- First recorded: 2026-08-02
- Effective or retirement date: 2026-12-01
- Last verified: 2026-08-02
- Replacement: Microsoft Agent Framework for new development
- Official source: https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability
- Migration impact: Do not select Foundry Workflows for new production development. Review existing workflow assets for migration and verify the current Agent Framework guidance before implementation.
- Affected playbook pages: Future workflow orchestration and Microsoft Foundry architecture pages
- Notes: The Foundry general-availability matrix currently lists Workflows as Preview and explicitly states the retirement date.

## Rejected lifecycle claim: OpenAI Evals retirement in 2026

- Status: superseded-unverified-claim
- Vendor: OpenAI
- First recorded: 2026-08-02
- Effective or retirement date: Not applicable
- Last verified: 2026-08-02
- Replacement: Current OpenAI Evals API and evaluation guidance
- Official source: https://platform.openai.com/docs/api-reference/evals
- Migration impact: Remove statements claiming a 2026 Evals retirement unless OpenAI publishes an authoritative lifecycle announcement.
- Affected playbook pages: `09-case-studies/enterprise-accounts-payable-automation.md`, `CHANGELOG.md`
- Notes: The current official API reference continues to document `/v1/evals`. This registry entry preserves the correction history; it is not a vendor deprecation announcement.
