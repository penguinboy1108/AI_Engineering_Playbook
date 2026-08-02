# Weekly Digests

Store one time-stamped digest per research cycle:

```text
weekly-digests/YYYY/YYYY-MM-DD.md
```

A digest is a research record, not automatically a permanent recommendation.

## Retrieval rules

Every digest must be represented in `catalog.yaml` with:

```yaml
content_type: digest
retrieval:
  default_grounding: false
  priority: 20
  role: recent-change-record
```

Use a digest only when the user asks about:

- recent changes;
- research history;
- why a durable page changed;
- findings that have not yet been promoted;
- no-action or needs-validation items.

Do not use a digest as the default answer for a stable production-design question when a current canonical page exists.

## Required classifications

Each digest must classify findings as:

- added;
- changed;
- superseded;
- deprecated or retirement announced;
- needs validation;
- no action.

## Promotion rule

Durable guidance should be promoted into the relevant guide, pattern, ADR, anti-pattern, or reference architecture only when evidence is strong enough.

Promotion requires:

1. a clearly supported recommendation;
2. current primary sources;
3. evidence classification;
4. stated applicability and non-applicability;
5. production, security, evaluation, and operational impact where relevant;
6. an update to `catalog.yaml` and `CHANGELOG.md`;
7. an update to `DEPRECATIONS.md` when lifecycle status changed;
8. a retrieval eval when the new page competes with existing pages.

The digest should link the durable page after promotion rather than duplicating the full recommendation indefinitely.

## Lifecycle claims

Do not classify an item as deprecated or retirement-announced based only on community discussion, search snippets, or indirect reports. Record it as `needs-validation` until an official lifecycle source is available.

Use [the weekly digest template](../templates/weekly-digest.md).
