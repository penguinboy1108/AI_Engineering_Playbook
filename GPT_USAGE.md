# Using This Playbook with GPT

## Goal

This repository is designed to give GPT reliable engineering context and reusable ideas when a real project becomes difficult. The canonical knowledge remains in English so technical terminology and source mapping stay stable; GPT should normally explain the result to the user in Simplified Chinese.

## Recommended interaction

When asking GPT for help, name the repository and the concrete problem. A useful request is:

```text
Consult penguinboy1108/AI_Engineering_Playbook before answering.
Use current canonical pages first, then accepted ADRs and supporting case studies.
Exclude weekly digests unless I ask about recent changes.
Answer in Chinese, cite the repository paths used, distinguish official guidance from engineering inference, and verify fast-changing vendor claims against current official documentation.

My problem:
<describe the real system, constraints, symptoms, and desired outcome>
```

For architecture work, also provide:

- business consequence of failure;
- data sensitivity;
- systems of record;
- expected scale and latency;
- available human-review path;
- irreversible actions;
- current technology constraints;
- evidence already collected.

## Expected answer behaviour

A good answer should:

1. identify the current canonical page through `catalog.yaml`;
2. explain the recommendation in Chinese;
3. state when the recommendation does not apply;
4. distinguish vendor guidance, project evidence, and inference;
5. cite exact repository paths and verification dates;
6. recheck current official sources for fast-changing products;
7. surface uncertainty instead of filling gaps with plausible detail.

## Recent-update questions

For questions such as “What changed this week?” or “Do I need to update my design?”, GPT may use `weekly-digests/` but should still check whether each finding was promoted into a durable page.

A digest is a research record, not automatically a production recommendation.

## Worklog boundary

The private worklog may contain raw experiments, implementation history, failures, and organisation-specific evidence. It should not be used as default grounding.

Use it only when:

- the user explicitly asks about the historical project;
- the information is needed to diagnose a similar problem;
- confidentiality permits access;
- observations are clearly labelled as project-specific and unvalidated until promoted.

## Chinese terminology

Use `GLOSSARY.zh-CN.md` for stable translations. Do not translate product names, APIs, class names, configuration keys, or code identifiers unless an explanation is added separately.

## Important limitation

Connecting GitHub does not make every answer automatically grounded in this repository. The assistant still needs to retrieve the relevant files, apply `AGENTS.md`, and verify unstable claims. A plausible answer without retrieved evidence is not equivalent to a playbook-grounded answer.
