# Changelog

All meaningful playbook changes are recorded here.

## Unreleased

### Added

- Root `AGENTS.md` contract for retrieval order, Chinese answer behaviour, evidence handling, current-source verification, confidentiality, and repository modification.
- `GPT_USAGE.md` for using the repository as grounded context during real engineering problem solving.
- `GLOSSARY.zh-CN.md` for stable Chinese explanations without maintaining duplicate bilingual canonical pages.
- Machine-readable `catalog.yaml` with content, evidence, lifecycle, canonical-topic, retrieval-role, priority, and review metadata.
- JSON Schema for the knowledge catalog.
- Content validation script and GitHub Actions workflow.
- Pinned validation dependencies in `requirements-validation.txt`.
- Pull-request evidence, lifecycle, sanitisation, and validation checklist.
- Initial retrieval evaluation cases covering canonical selection, digest exclusion, project-evidence boundaries, current-source verification, and Chinese answers.

### Changed

- Standardised source policy around separate document, evidence, and product-lifecycle dimensions.
- Defined `catalog.yaml` as the retrieval source of truth during front-matter migration.
- Expanded governance for canonical pages, digests, worklogs, retrieval evals, publication safety, and deprecation evidence.
- Updated the repository map with unique directory numbers and machine-quality assets.
- Made quality-control and GPT-usage entry points visible from the README.
- Required official lifecycle evidence before adding deprecation or retirement entries.
- Standardised the accounts-payable case-study metadata and removed an unsupported product-lifecycle assertion in favour of implementation-time official verification.

### Deprecated

- None.

### Needs validation

- Migrate remaining legacy page front matter to the standard metadata model.
- Add an executable retrieval/evaluation runner for `evals/retrieval-cases.yaml` after selecting the indexing stack.
- Confirm branch-protection settings require the content-quality workflow before merge.
- Review remaining existing pages for unsupported or ambiguous lifecycle claims during the next source audit.

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
