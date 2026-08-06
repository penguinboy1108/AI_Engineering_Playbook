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
- Weekly digest for 2026-08-06 covering Microsoft Agent Framework release progression, OpenAI Agents SDK state and boundary fixes, and the state-machine upgrade firewall pattern.
- Production security guidance for limiting agent blast radius through trust establishment, sandboxing, egress control, scoped identity, and policy-gated actions.
- Production reliability guidance for pinning rapidly evolving agent SDKs, making model defaults explicit, and regression-testing upgrades.

### Changed

- Expanded the repository map to include case studies, patterns, and anti-patterns.
- Clarified that OpenAI evaluation guidance must track current tooling rather than assume the legacy Evals platform remains permanent.
- Classified Microsoft Agentic Retrieval in Foundry Local as a targeted Preview option for edge, disconnected, and air-gapped RAG rather than a default managed-cloud architecture.

### Deprecated

- None.

### Needs validation

- Initial Microsoft AI-103 objective mapping.
- Anthropic architecture and certification mapping.
- Wider OpenAI Responses API and Agents SDK implementation pages.
- Production checklists for identity, observability, reliability, and cost.
- Project-validated evidence for the new agent capability-containment pattern.
- Release verification for OpenAI Agents SDK main-branch state, tracing, MCP, validation-redaction, and sandbox fixes reviewed on 2026-08-06.
- Package-level migration review before adopting Microsoft Agent Framework Python 1.13.0 or .NET 1.17.0.
