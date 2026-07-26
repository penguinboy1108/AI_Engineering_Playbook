# Governance

## Goals

The playbook should remain current, auditable, practical, and safe to use as grounding material for project design and RAG-assisted answers.

## Update workflow

```text
Research current sources
        ↓
Classify changes
        ↓
Update weekly digest
        ↓
Update affected playbook pages
        ↓
Update CHANGELOG and DEPRECATIONS
        ↓
Open a draft pull request
        ↓
Human review and merge
```

Automated research must never merge directly into `main`.

## Change classes

Every weekly review should classify findings as:

- `added`: a new capability, pattern, or source.
- `changed`: existing guidance needs revision.
- `superseded`: a newer recommendation replaces an older one.
- `deprecated`: an API, SDK, model, service, or pattern is being retired.
- `needs-validation`: important but not yet sufficiently tested or documented.
- `no-action`: noteworthy news that does not change the playbook.

## Review cadence

- Weekly: official release notes, documentation changes, engineering blogs, important papers, and high-quality repositories.
- Monthly: verify core fast-changing pages, links, SDK names, API lifecycle, and preview/GA status.
- Quarterly: repository-wide audit, archive stale content, refresh certification mapping, and review information architecture.

## Pull request requirements

Each update PR should include:

- What changed.
- Why it matters.
- Primary sources.
- Affected files.
- Production impact.
- Migration or rollback considerations.
- Whether the change is official guidance, project evidence, or inference.
- Validation status.

## Approval policy

The repository owner reviews and merges changes. High-impact recommendations involving identity, security, privacy, financial processing, irreversible actions, or production autonomy require explicit human approval.

## Content lifecycle

Do not silently delete old guidance. Mark it as deprecated or superseded, link to the replacement, and preserve enough context to explain previous architectural decisions.

## RAG usage policy

When this repository is indexed for retrieval:

- Prefer `current`, authoritative, recently verified content.
- Exclude `deprecated`, `superseded`, and `unverified` content by default.
- Return citations, status, and verification date with retrieved evidence.
- Allow abstention when the evidence is incomplete.
- Evaluate retrieval quality separately from generated-answer quality.