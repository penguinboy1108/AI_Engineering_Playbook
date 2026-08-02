---
status: current
last_verified: 2026-08-02
source_priority: official
vendors:
  - microsoft
review_frequency: monthly
applies_to:
  - certification
  - ai-103
---

# AI-103 Objective Map

## Current exam identity

- Certification: Azure AI Apps and Agents Developer Associate
- Exam: AI-103 — Developing AI Apps and Agents on Azure
- Skills measured version: April 16, 2026
- Official study guide last updated: April 14, 2026
- Exam language currently listed: English
- Exam duration currently listed: 120 minutes

This page is a navigation and evidence map, not a substitute for the official study guide. Recheck the official source before booking or sitting the exam.

## Skills at a glance

| Domain | Weight |
|---|---:|
| Plan and manage an Azure AI solution | 25–30% |
| Implement generative AI and agentic solutions | 30–35% |
| Implement computer vision solutions | 10–15% |
| Implement text analysis solutions | 10–15% |
| Implement information extraction solutions | 10–15% |

## Playbook mapping

### Plan and manage an Azure AI solution

Study and practise:

- Foundry service and model selection
- deployment options and CI/CD
- quotas, scaling, rate limits, and cost
- monitoring, drift, grounding quality, and index health
- managed identity, keyless credentials, private networking, and role policies
- safety filters, guardrails, auditing, provenance, and approval workflows

Relevant playbook areas:

- `07-security/`
- `08-production/`
- future Microsoft Foundry deployment and identity pages

### Implement generative AI and agentic solutions

Study and practise:

- RAG and grounding
- workflows, tool-augmented flows, and multistep pipelines
- model and application evaluation
- Foundry SDK and connector integration
- agent roles, goals, tools, memory, orchestration, and monitoring
- autonomous or semiautonomous workflows with safeguards
- tracing, token analytics, latency, and hybrid rules/LLM systems

Relevant playbook areas:

- `02-architecture/`
- `03-context-and-rag/`
- `04-prompts-and-outputs/`
- `05-tools-and-mcp/`
- `06-evaluation/`
- `07-security/agent-capability-containment.md`
- `08-production/sdk-version-and-default-control.md`

### Implement computer vision solutions

Study and practise:

- image and video generation and editing
- multimodal visual understanding
- captions, visual question answering, and accessibility descriptions
- Content Understanding image/video pipelines
- visual safety, indirect prompt injection, watermarking, and policy controls

Status in this repository: needs dedicated implementation and safety pages.

### Implement text analysis solutions

Study and practise:

- entity, topic, summary, and structured JSON extraction
- sentiment, tone, safety, and sensitive-content detection
- translation and speech workflows
- domain-specific extraction and summarisation

Status in this repository: partly covered by structured-output and document-workflow patterns; dedicated Azure service pages remain to be added.

### Implement information extraction solutions

Study and practise:

- ingestion and indexing for documents and multimodal content
- semantic, hybrid, and vector search
- enrichment skills
- OCR and RAG ingestion
- Content Understanding and structured/Markdown representations
- direct integration of retrieval with workflows and agent tools

Relevant playbook areas:

- `03-context-and-rag/`
- `09-case-studies/enterprise-accounts-payable-automation.md`
- `10-patterns/bounded-document-automation-workflow.md`

## Lifecycle cautions

- Microsoft Foundry Agent Service (classic) is announced for retirement on 2027-03-31. Use the current generally available Foundry Agents Service for new development.
- Microsoft Foundry Workflows is listed as Preview and announced for retirement on 2026-12-01. Microsoft directs new development to Microsoft Agent Framework.
- Many individual Foundry tools, memory, workflow, monitoring, and agent-control features can have different GA/Preview status. Verify the label of the exact feature used in a lab or project.

See `DEPRECATIONS.md` for tracked lifecycle items.

## Verification checklist

Before using this map for exam preparation:

- [ ] The study guide still says “Skills measured as of April 16, 2026”.
- [ ] Domain weights are unchanged.
- [ ] The certification page still lists the same exam language and duration.
- [ ] Labs do not rely on retired classic services or Foundry Workflows.
- [ ] Each Preview feature is clearly marked and has a production-safe alternative where needed.

## Official sources

- Study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103
- Certification page: https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/
- Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/foundry/
- Foundry GA matrix: https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability
