#!/usr/bin/env python3
"""Validate the playbook catalog and repository content.

The initial validator deliberately focuses on high-value invariants:
- catalog schema and unique identifiers;
- canonical retrieval roles;
- catalog paths and front-matter dates;
- weekly digests excluded from default grounding;
- replacement links for deprecated/superseded entries;
- internal Markdown links;
- obvious secret material.

It does not make network requests. External source freshness is a human/research
workflow concern and should not make pull-request checks flaky.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.yaml"
SCHEMA_PATH = ROOT / "schema" / "catalog.schema.json"

INTERNAL_LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:)([^)]+)\)")
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "Azure storage connection string": re.compile(r"DefaultEndpointsProtocol=https?;", re.I),
}

LEGACY_CURRENT_STATUSES = {
    "current",
    "validated",
    "accepted",
    "project-validated",
    "validated-project-case-study",
}


def normalise_dates(value: Any) -> Any:
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalise_dates(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalise_dates(item) for item in value]
    return value


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return normalise_dates(yaml.safe_load(handle))


def load_json(path: Path) -> Any:
    import json

    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def parse_front_matter(path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    closing = text.find("\n---\n", 4)
    if closing == -1:
        return None
    data = yaml.safe_load(text[4:closing]) or {}
    return normalise_dates(data)


def validate_catalog(catalog: dict[str, Any], errors: list[str], warnings: list[str]) -> None:
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(catalog), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "catalog"
        errors.append(f"catalog schema: {location}: {error.message}")

    entries = catalog.get("entries", [])
    ids: set[str] = set()
    paths: set[str] = set()
    canonical_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for entry in entries:
        entry_id = entry.get("id", "<missing-id>")
        entry_path = entry.get("path", "")

        if entry_id in ids:
            errors.append(f"duplicate catalog id: {entry_id}")
        ids.add(entry_id)

        if entry_path in paths:
            errors.append(f"duplicate catalog path: {entry_path}")
        paths.add(entry_path)

        file_path = ROOT / entry_path
        if not file_path.is_file():
            errors.append(f"catalog path does not exist: {entry_path}")
            continue

        retrieval = entry.get("retrieval", {})
        if entry.get("content_type") == "digest" and retrieval.get("default_grounding") is not False:
            errors.append(f"weekly digest must not be default grounding: {entry_id}")

        if entry.get("document_status") in {"deprecated", "superseded"} and not entry.get("superseded_by"):
            errors.append(f"{entry_id} is {entry.get('document_status')} but has no superseded_by entry")

        for topic in entry.get("canonical_for", []):
            canonical_groups[topic].append(entry)

        if entry.get("metadata_source") == "front-matter":
            front_matter = parse_front_matter(file_path)
            if front_matter is None:
                errors.append(f"catalog expects front matter but none was found: {entry_path}")
                continue

            if front_matter.get("last_verified") != entry.get("last_verified"):
                errors.append(
                    f"last_verified mismatch for {entry_path}: "
                    f"front matter={front_matter.get('last_verified')} catalog={entry.get('last_verified')}"
                )

            source_status = front_matter.get("status")
            if entry.get("document_status") == "current" and source_status not in LEGACY_CURRENT_STATUSES:
                warnings.append(
                    f"legacy status mapping needs review for {entry_path}: status={source_status!r}"
                )

    for topic, grouped_entries in canonical_groups.items():
        current_defaults = [
            entry
            for entry in grouped_entries
            if entry.get("document_status") == "current"
            and entry.get("retrieval", {}).get("default_grounding") is True
        ]
        primaries = [
            entry for entry in current_defaults if entry.get("retrieval", {}).get("role") == "primary"
        ]
        if current_defaults and len(primaries) != 1:
            ids_for_topic = ", ".join(entry.get("id", "?") for entry in current_defaults)
            errors.append(
                f"canonical topic {topic!r} must have exactly one current default primary; "
                f"found {len(primaries)} among [{ids_for_topic}]"
            )

        priorities = [entry.get("retrieval", {}).get("priority", 0) for entry in current_defaults]
        if primaries and priorities and primaries[0].get("retrieval", {}).get("priority", 0) < max(priorities):
            errors.append(f"primary entry does not have the highest priority for canonical topic {topic!r}")


def validate_internal_links(errors: list[str]) -> None:
    for markdown_path in ROOT.rglob("*.md"):
        if ".git" in markdown_path.parts:
            continue
        text = markdown_path.read_text(encoding="utf-8")
        for raw_target in INTERNAL_LINK_RE.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or target.startswith("#") or "<" in target or ">" in target:
                continue
            resolved = (markdown_path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"internal link escapes repository: {markdown_path.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken internal link: {markdown_path.relative_to(ROOT)} -> {target}")


def scan_for_obvious_secrets(errors: list[str]) -> None:
    text_suffixes = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label} found in {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not CATALOG_PATH.is_file():
        errors.append("catalog.yaml is missing")
    if not SCHEMA_PATH.is_file():
        errors.append("schema/catalog.schema.json is missing")

    if not errors:
        catalog = load_yaml(CATALOG_PATH)
        validate_catalog(catalog, errors, warnings)

    validate_internal_links(errors)
    scan_for_obvious_secrets(errors)

    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Content validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Content validation passed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
