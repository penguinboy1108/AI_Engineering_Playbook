# Governance

## Goals

The playbook should remain current, auditable, practical, safe to publish, and reliable as grounding material for project design and AI-assisted answers.

The repository is governed as a knowledge system rather than a folder of notes. Human-readable pages, machine metadata, retrieval rules, evaluation cases, and change history must remain aligned.

## Knowledge lifecycle

```text
Research current primary sources
        ↓
Classify the finding
        ↓
Record time-sensitive research in a weekly digest
        ↓
Promote durable guidance only when justified
        ↓
Update canonical page, pattern, ADR, or case study
        ↓
Update catalog, changelog, and deprecation registry
        ↓
Run validation and retrieval checks
        ↓
Open a draft pull request
        ↓
Human review and merge
```

Automated research and AI-authored changes must never merge directly into `main`.

## Change classes

Every review cycle should classify findings as:

- `added`: a new capability, pattern, or source.
- `changed`: existing guidance needs revision.
- `superseded`: a newer recommendation replaces older guidance.
- `deprecated`: an API, SDK, model, service, or pattern is no longer recommended or supported.
- `retirement-announced`: an official end date has been announced.
- `needs-validation`: important but not sufficiently verified or tested.
- `no-action`: noteworthy information that does not change durable guidance.

## Content roles

### Canonical guide or pattern

The current default recommendation for a stable topic. It should use `retrieval.role: primary` and have the highest priority for its `canonical_for` topic.

### ADR

Explains why a decision was made, what alternatives were considered, and what would trigger reconsideration. It supports a canonical page with `decision-context` rather than replacing the page.

### Case study

Records sanitised project evidence, limitations, and outcomes. It supports a canonical page with `supporting-evidence` and must not be treated as a universal benchmark.

### Weekly digest

A time-stamped research record. It must use `default_grounding: false` and should be retrieved only for recent-change, research-history, or promotion questions.

### Private worklog

Raw project history, experiments, failures, and organisation-specific evidence. It is not default grounding and must pass sanitisation review before publication.

## Machine-readable governance

`catalog.yaml` is the retrieval source of truth. The catalog records content type, document status, evidence status, product lifecycle, verification dates, canonical topics, retrieval role, priority, and supersession relationships.

The schema is defined in `schema/catalog.schema.json`.

A canonical topic must have exactly one current default-grounding `primary` entry. Related ADR and case-study entries may share the topic only as decision context or supporting evidence.

## Review cadence

- Weekly: official release notes, documentation changes, engineering blogs, important papers, and selected repositories.
- Monthly: verify core fast-changing pages, links, SDK names, API lifecycle, model defaults, preview/GA status, and certification scope.
- Quarterly: repository-wide audit, archive stale content, refresh certification mapping, review information architecture, and inspect retrieval-eval coverage.
- On change: review any page affected by a model, SDK, service, security boundary, or organisation policy update.

`next_review_due` should be recorded in the catalog. An overdue date is a review signal; it does not automatically prove the content is wrong.

## Pull request requirements

Each update PR should include:

- what changed and why;
- change classification;
- primary sources and verification dates;
- evidence label;
- affected canonical topics and files;
- production impact;
- migration or rollback considerations;
- confidentiality and sanitisation review;
- validation results;
- unresolved factual or lifecycle questions.

Use `.github/pull_request_template.md`.

## Approval policy

The repository owner reviews and merges changes.

High-impact recommendations involving identity, security, privacy, financial processing, regulated decisions, irreversible actions, production autonomy, or publication of project evidence require explicit human approval.

A passing workflow is necessary but not sufficient. Automated checks cannot determine whether a source was interpreted correctly or whether sanitisation is adequate.

## Content lifecycle

Do not silently delete old guidance.

When guidance changes:

1. update the replacement page;
2. mark the old page `deprecated` or `superseded`;
3. set `superseded_by` in the catalog;
4. link the old and new pages;
5. add a registry entry when an external product lifecycle changed;
6. preserve enough history to explain previous architecture decisions.

Archive content only when it no longer provides useful migration, decision, or historical context.

## Deprecation evidence

A deprecation or retirement entry requires an official lifecycle notice, official product page, or official migration guide that clearly identifies the affected item and effective date.

Community discussions and search snippets may trigger investigation, but they must remain `needs-validation` until official evidence is found.

## RAG and GPT usage policy

When this repository is indexed or retrieved:

- follow `AGENTS.md`;
- use `catalog.yaml` to select current canonical content;
- prefer `primary` pages over duplicate supporting pages;
- exclude digests, deprecated, superseded, archived, experimental, and unverified pages from default grounding;
- return repository paths, status, evidence type, and verification date;
- answer in Simplified Chinese by default while preserving important English terms;
- verify fast-changing vendor claims against current official sources;
- allow abstention when evidence is incomplete;
- evaluate retrieval quality separately from generated-answer quality.

Connecting GitHub does not make an answer automatically grounded. The assistant must actually retrieve the relevant files and apply the repository contract.

## Retrieval evaluation

`evals/retrieval-cases.yaml` defines representative questions and expected retrieval behaviour.

Add or update an eval case when:

- a new canonical topic is added;
- multiple pages could compete for the same query;
- a digest or historical page could incorrectly outrank durable guidance;
- a project metric could be generalised incorrectly;
- current official verification is required;
- a real user query exposed a retrieval or answer failure.

The initial eval file is a specification. Future automation may execute it against a selected retrieval stack and model, but its expected paths and forbidden behaviours are already reviewable.

## Validation

Run:

```bash
python scripts/validate_content.py
```

The GitHub workflow validates pull requests and pushes to `main`. It checks catalog schema, unique IDs and paths, canonical roles, file existence, front-matter verification dates, digest exclusion, internal links, supersession metadata, and obvious secret material.

External-link freshness and factual interpretation remain human/research responsibilities because network-dependent checks can be flaky and a successful HTTP response does not prove that a claim is supported.

## Language policy

English is the canonical repository language for technical content and source mapping. GPT should normally present answers and update summaries in Simplified Chinese.

Maintain stable translations in `GLOSSARY.zh-CN.md` rather than duplicating every page in two languages. This reduces drift and duplicate retrieval results.

## Public-repository safety

Before publishing project-derived material:

- remove employer, customer, supplier, tenant, account, and internal-system identifiers;
- remove raw documents, messages, personal data, secrets, and private URLs;
- generalise confidential policy and thresholds;
- round metrics where exact values are sensitive;
- distinguish historical implementation from current recommendation;
- confirm that public sources support the reusable recommendation;
- complete the PR sanitisation checklist.
