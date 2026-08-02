# Changelog

All meaningful playbook changes are recorded here.

## Unreleased

### Added

- Repository source and evidence policy.
- Governance model for weekly, monthly, and quarterly maintenance.
- Templates for playbook entries, case studies, reusable patterns, and weekly digests.
- Deprecation registry.
- First sanitised project case study: bounded AI workflow for enterprise accounts-payable automation.
- First reusable architecture pattern: bounded document automation workflow.
- First architecture decision: prefer a bounded workflow over an autonomous agent for defined, consequential document processing.
- Project-to-playbook knowledge flow that separates private evidence, sanitised case studies, patterns, and ADRs.
- Weekly digest for 2026-07-30 covering Microsoft Foundry Local Agentic Retrieval, agent containment, SDK lifecycle controls, and official code-reading picks.
- Production security guidance for limiting agent blast radius through trust establishment, sandboxing, egress control, scoped identity, and policy-gated actions.
- Production reliability guidance for pinning rapidly evolving agent SDKs, making model defaults explicit, and regression-testing upgrades.
- Verified AI-103 objective map based on the official April 16, 2026 skills outline.
- Monthly verification report for 2026-08-02.
- Lifecycle records for Microsoft Foundry Agent Service classic and Microsoft Foundry Workflows.

### Changed

- Expanded the repository map to include case studies, patterns, and anti-patterns.
- Classified Microsoft Agentic Retrieval in Foundry Local as a targeted Preview option for edge, disconnected, and air-gapped RAG rather than a default managed-cloud architecture.
- Corrected the enterprise AP case study to remove an unsupported claim that OpenAI Evals would retire in 2026; the current official API reference continues to document `/v1/evals`.
- Refreshed agent containment guidance against current Anthropic engineering sources.
- Refreshed OpenAI Agents SDK lifecycle guidance and added sandbox/workspace boundary regression testing.
- Added feature-level GA/Preview cautions to the AI-103 mapping.

### Deprecated or retirement announced

- Microsoft Foundry Agent Service classic: retirement announced for 2027-03-31; migrate to the current generally available Foundry Agents Service.
- Microsoft Foundry Workflows: retirement announced for 2026-12-01; use Microsoft Agent Framework for new development.

### Needs validation

- Anthropic architecture and certification mapping.
- Wider OpenAI Responses API and Agents SDK implementation pages.
- Production checklists for identity, observability, reliability, networking, and cost.
- Project-validated evidence for the agent capability-containment pattern.
- Dedicated AI-103 implementation pages for computer vision, speech, text analysis, and Content Understanding.
