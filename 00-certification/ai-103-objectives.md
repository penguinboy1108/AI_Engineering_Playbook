---
status: current
last_verified: 2026-08-09
source_priority: official
vendors:
  - microsoft
review_frequency: monthly
applies_to:
  - certification
  - azure
  - production
---

# AI-103 Objective Map

## Verification status

**[Official exam blueprint]**

The current Microsoft study guide is titled **Exam AI-103: Developing AI Apps and Agents on Azure** and states that the skills measured are effective **April 16, 2026**.

This page is a navigation and evidence map, not a substitute for the official study guide. Re-check the official guide before using percentages or detailed objectives for exam planning.

Official source:

- https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103

## Current domains

| Domain | Weight | Playbook relevance |
|---|---:|---|
| Plan and manage an Azure AI solution | 25–30% | Identity, network controls, deployment, monitoring, governance, responsible AI |
| Implement generative AI and agentic solutions | 30–35% | RAG, agents, tools, workflows, evaluation, memory, Foundry SDKs and connectors |
| Implement computer vision solutions | 15–20% | Image analysis, OCR, multimodal processing and vision applications |
| Implement natural language processing solutions | 15–20% | Language analysis, speech, translation and conversational workloads |
| Implement information extraction solutions | 10–15% | Search, grounding, enrichment, document extraction and Content Understanding |

## High-value objective clusters

### Plan and manage Azure AI solutions

Track practical evidence for:

- selecting suitable Azure AI and Microsoft Foundry services;
- identity, RBAC, secrets and network isolation;
- responsible AI, content safety and governance;
- trace logging, provenance and approval workflows;
- deployment, monitoring, evaluation and cost control.

### Build generative applications and agents

Track practical evidence for:

- deploying and consuming language, code and multimodal models;
- implementing RAG and grounded generation;
- designing deterministic workflows, tool-augmented flows and multistep reasoning pipelines;
- evaluating fabrication, relevance, quality and safety;
- defining agent roles, goals, tool schemas, memory and conversation tracking;
- connecting APIs, search, knowledge stores and custom functions.

### Build retrieval and extraction pipelines

Track practical evidence for:

- semantic, hybrid and vector search;
- OCR, layout analysis and field extraction;
- enrichment and ingestion pipelines;
- structured or Markdown representations for downstream reasoning;
- connecting retrieval to workflows and agent tools.

## Evidence mapping rules

For each objective, retain three distinct kinds of evidence:

1. **Official knowledge** — current Microsoft documentation and learning material.
2. **Hands-on evidence** — a lab, prototype or production implementation.
3. **Decision evidence** — an ADR, evaluation, incident lesson or trade-off analysis showing why the design was chosen.

Do not treat a single vendor tutorial as proof of production readiness. Production evidence should also cover security, reliability, evaluation, observability and cost.

## Lifecycle caveat

The exam blueprint can remain stable while the underlying Microsoft Foundry products, SDKs and portal experiences change. Therefore:

- use this page to track exam scope;
- use `DEPRECATIONS.md` for product lifecycle;
- verify SDK and service names against current Microsoft documentation before implementation;
- mark classic, preview, deprecated and retirement-announced products explicitly.

## Monthly verification checklist

- [ ] Confirm the effective date shown in the official study guide.
- [ ] Confirm domain names and percentages.
- [ ] Check whether objectives reference renamed Foundry services or SDKs.
- [ ] Check migration and retirement notices for services used in linked labs.
- [ ] Update `last_verified` only after reviewing the official page.
