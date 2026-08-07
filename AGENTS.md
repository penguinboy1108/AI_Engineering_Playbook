# AI Engineering Playbook Agent Contract

This file defines how an AI assistant should retrieve, interpret, and present knowledge from this repository.

## Default response language

- Answer the user in Simplified Chinese unless the user requests another language.
- Preserve important English technical terms such as RAG, MCP, eval, structured outputs, and harness engineering.
- Explain an English term in Chinese when it first appears if that improves clarity.
- Do not maintain a second full Chinese copy of every canonical page. Translate and synthesise at answer time.

## Repository purpose

Use this repository as a source of engineering evidence and reusable design ideas when solving real work problems. It is not a substitute for current product documentation, organisation-specific policy, legal advice, or security approval.

## Retrieval order

Retrieve evidence in this order:

1. Current canonical playbook guides.
2. Current reusable patterns and accepted ADRs.
3. Current sanitised case studies as supporting project evidence.
4. Weekly digests only when the question concerns recent changes, research history, or why a durable page changed.
5. Deprecated, superseded, archived, experimental, and unverified content only when explicitly relevant to history, migration, comparison, or open research.

Use `catalog.yaml` as the machine-readable index. Prefer entries where:

- `document_status: current`;
- `retrieval.default_grounding: true`;
- `retrieval.role: primary`;
- `last_verified` is recent enough for the claim;
- the topic matches the user's problem.

When multiple pages share a `canonical_for` value, retrieve the `primary` page first. Use `decision-context` and `supporting-evidence` pages only to explain rationale, trade-offs, or project evidence. Do not fill the context window with near-duplicate pages.

## Evidence rules

- Distinguish `official`, `reference-architecture`, `project-validated`, `engineering-inference`, `experimental`, and `unverified` evidence.
- Never present an engineering inference as a vendor requirement.
- Never present a case-study result as a universal benchmark.
- Include the relevant repository path, document status, evidence status, and `last_verified` date for important recommendations.
- Recheck current official sources before relying on fast-changing claims about APIs, SDKs, models, service names, lifecycle status, pricing, certification scope, or product defaults.
- Prefer current product documentation over certification material and old weekly digests.
- When authoritative evidence is insufficient, say so and abstain from inventing a best practice.

## Answer contract

For a substantial engineering question, prefer this structure:

1. Recommended decision.
2. Why it fits the stated constraints.
3. Implementation outline.
4. Failure modes, security boundaries, and when not to use it.
5. Playbook evidence with repository paths.
6. Items that require current official verification or organisation-specific confirmation.

Use concise answers for simple questions. Do not force the full structure when it adds no value.

## Current-information boundary

This repository records when content was last verified; it does not guarantee that a vendor product is still unchanged. For fast-changing claims:

1. Read the relevant canonical page.
2. Check its `last_verified` date and product lifecycle.
3. Verify the claim against a current official source.
4. Explain any conflict between the repository and the current source.
5. Propose a playbook update rather than silently using stale guidance.

## Confidentiality and public-repository rules

- Treat this repository as public.
- Do not add employer, customer, supplier, tenant, account, document, internal endpoint, credential, or proprietary policy details without explicit publication approval.
- Do not copy raw private worklog content into this repository.
- Project-derived content must be sanitised, rounded where appropriate, and reviewed before publication.
- Do not expose secrets or personal data in prompts, examples, logs, traces, commits, issues, or pull requests.

## Repository modification rules

- Automated research and AI-authored changes must use a branch and draft pull request.
- Do not merge directly into `main`.
- Preserve old decisions through deprecation or supersession links; do not silently rewrite history.
- Update `catalog.yaml`, `CHANGELOG.md`, and `DEPRECATIONS.md` when applicable.
- Run `python scripts/validate_content.py` before declaring a content change complete.
- Do not weaken validation or remove evidence requirements merely to make checks pass.

## Completion evidence

A repository update is not complete until the change report identifies:

- files added, changed, moved, or removed;
- validation results;
- source and evidence classification;
- confidentiality review result;
- unresolved factual or lifecycle questions;
- whether a human still needs to review or merge the draft pull request.
