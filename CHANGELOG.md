# Changelog

All meaningful playbook changes are recorded here.

## Unreleased

### Added

- Verified AI-103 objective map using the April 16, 2026 official exam blueprint.
- Monthly verification reports for 2026-08-09, 2026-08-16, 2026-08-24, and 2026-08-31.
- Lifecycle registry entries for Azure OpenAI Assistants API (classic), the current Foundry Models Azure AI Inference beta SDK surface, Foundry Workflows, Foundry Agents (classic), and Prompt Flow.
- Root `AGENTS.md` contract for retrieval order, Chinese answer behaviour, evidence handling, current-source verification, confidentiality, and repository modification.
- `GPT_USAGE.md` for using the repository as grounded context during real engineering problem solving.
- `GLOSSARY.zh-CN.md` for stable Chinese explanations without maintaining duplicate bilingual canonical pages.
- Machine-readable `catalog.yaml` with content, evidence, lifecycle, canonical-topic, retrieval-role, priority, and review metadata.
- JSON Schema for the knowledge catalog.
- Content validation script and GitHub Actions workflow.
- Pinned validation dependencies in `requirements-validation.txt`.
- Pull-request evidence, lifecycle, sanitisation, and validation checklist.
- Initial retrieval evaluation cases covering canonical selection, digest exclusion, project-evidence boundaries, current-source verification, and Chinese answers.
- Weekly digest for 2026-08-06 covering Microsoft Agent Framework release progression, OpenAI Agents SDK state and boundary fixes, and the state-machine upgrade firewall pattern.

### Changed

- Reverified AI-103 objectives, Anthropic agent-containment guidance, and OpenAI Agents SDK release status on 2026-08-31.
- Confirmed the latest official OpenAI Agents SDK release remains `v0.22.0` (2026-08-19); no new SDK migration claim was added.
- Updated Microsoft lifecycle wording after the documented 2026-08-26 retirement dates for Azure OpenAI Assistants API (classic) and the current Foundry Models Azure AI Inference beta-SDK surface passed. Because official pages still use future-tense retirement wording, the registry now marks current operational status as requiring validation instead of guessing availability.
- Reverified Foundry Workflows (2026-12-01), Foundry Agents classic (2027-03-31), and Prompt Flow (2027-04-20) lifecycle dates on 2026-08-31.
- Retained the Azure AI Inference lifecycle scope discrepancy between current Foundry Models documentation and classic migration guidance.
- Refreshed the OpenAI Agents SDK production-control page through official release `v0.22.0` (2026-08-19), including explicit-client provider configuration, persisted-state redaction, terminal Response failure handling, and checkpoint usage isolation.
- Corrected AI-103 domain weights to the current official 25–30%, 30–35%, and three 10–15% domains.
- Standardised source policy around separate document, evidence, and product-lifecycle dimensions.
- Defined `catalog.yaml` as the retrieval source of truth during front-matter migration.
- Expanded governance for canonical pages, digests, worklogs, retrieval evals, publication safety, and deprecation evidence.
- Updated the repository map with unique directory numbers and machine-quality assets.
- Made quality-control and GPT-usage entry points visible from the README.
- Required official lifecycle evidence before adding deprecation or retirement entries.
- Standardised the accounts-payable case-study metadata and removed an unsupported product-lifecycle assertion in favour of implementation-time official verification.

### Deprecated

- Azure OpenAI Assistants API (classic): documented retirement date 2026-08-26 has passed; official page has not yet been refreshed to an explicit post-retirement status.
- Azure AI Inference beta SDK for the current Foundry Models endpoint surface: documented retirement date 2026-08-26 has passed; exact package/endpoint support state requires validation because Microsoft documentation exposes differing lifecycle dates across surfaces.
- Microsoft Foundry Workflows visual experience, retiring 2026-12-01.
- Microsoft Foundry Agents (classic), retiring 2027-03-31.
- Prompt Flow in Microsoft Foundry and Azure Machine Learning, retiring 2027-04-20.

### Needs validation

- Synchronise new certification and monthly-verification entries into `catalog.yaml` during metadata migration.
- Reconcile `catalog.yaml` review metadata with refreshed front-matter verification dates; the catalog is not updated in the 2026-08-31 pass because its existing metadata migration is incomplete.
- Confirm post-retirement operational behaviour for Azure OpenAI Assistants API (classic) and the named Azure AI Inference beta-SDK surface; do not infer continued support from endpoints or packages that may still respond/install.
- Migrate remaining legacy page front matter to the standard metadata model.
- Add an executable retrieval/evaluation runner for `evals/retrieval-cases.yaml` after selecting the indexing stack.
- Confirm branch-protection settings require the content-quality workflow before merge.
- Review remaining existing pages for unsupported or ambiguous lifecycle claims during the next source audit.
- Package-level migration review before adopting Microsoft Agent Framework releases.
- Verify exact Azure AI Inference retirement dates against the precise package and endpoint surface used by each existing project because current and classic Microsoft pages expose different dates.

## 2026-08-02

### Added

- Repository source and evidence policy.
- Governance model for weekly, monthly, and quarterly maintenance.
- Templates for playbook entries, case studies, reusable patterns, and weekly digests.
- Deprecation registry.
- First sanitised project case study: bounded AI workflow for enterprise accounts-payable automation.
- First reusable architecture pattern: bounded document automation workflow.
- First architecture decision: prefer a bounded workflow over an autonomous agent for defined, consequential document processing.
- Project-to-playbook knowledge flow separating private evidence, sanitised case studies, patterns, and ADRs.
- Weekly digest for 2026-07-30 covering Microsoft Foundry Local Agentic Retrieval, agent containment, SDK lifecycle controls, and official code-reading picks.
- Production security guidance for limiting agent blast radius through trust establishment, sandboxing, egress control, scoped identity, and policy-gated actions.
- Production reliability guidance for pinning rapidly evolving agent SDKs, making model defaults explicit, and regression-testing upgrades.
- Specification-Driven AI Coding and Harness Engineering practice guide.

### Changed

- Expanded the repository map to include case studies, patterns, and anti-patterns.
- Recorded that evaluation guidance must track current official tooling rather than assume a product name or interface remains permanent.
- Classified Microsoft Agentic Retrieval in Foundry Local as a targeted Preview option for edge, disconnected, and air-gapped RAG rather than a default managed-cloud architecture.

### Deprecated

- None.

### Needs validation

- Initial Microsoft AI-103 objective mapping.
- Anthropic architecture and certification mapping.
- Wider OpenAI API and Agents SDK implementation pages.
- Production checklists for identity, observability, reliability, and cost.
- Project-validated evidence for the agent capability-containment pattern.
