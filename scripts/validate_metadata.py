"""Validate a minimal normalized metadata example using the standard library.

This is an offline prototype, not a CurseForge API client or raw-response schema.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


def validate(payload):
    errors = []
    if not isinstance(payload, dict):
        return ["The document must be a JSON object."]
    if payload.get("schema_version") != "0.1":
        errors.append("schema_version must be '0.1'.")
    if not isinstance(payload.get("synthetic"), bool):
        errors.append("synthetic must be true or false.")

    def check_text(record, field, label):
        value = record.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{label}.{field} must be a non-empty string.")
            return None
        return value

    def check_time(record, label):
        value = check_text(record, "observed_at", label)
        if value is None:
            return
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed.utcoffset() is None:
                raise ValueError("timezone required")
        except ValueError:
            errors.append(f"{label}.observed_at must be an ISO 8601 timestamp with a timezone.")

    def records(field):
        value = payload.get(field)
        if not isinstance(value, list):
            errors.append(f"{field} must be a list.")
            return []
        return value

    project_ids = set()
    for index, project in enumerate(records("projects")):
        label = f"projects[{index}]"
        if not isinstance(project, dict):
            errors.append(f"{label} must be an object.")
            continue
        project_id = check_text(project, "project_id", label)
        if project_id is not None:
            if project_id in project_ids:
                errors.append(f"{label}.project_id is duplicated: {project_id}")
            project_ids.add(project_id)
        check_text(project, "name", label)
        source = check_text(project, "source", label)
        if payload.get("synthetic") is True and source != "synthetic":
            errors.append(f"{label}.source must be 'synthetic' in a synthetic document.")
        check_time(project, label)
        count = project.get("download_count")
        if "download_count" not in project:
            errors.append(f"{label}.download_count is required; use null if unavailable.")
        elif count is not None and (type(count) is not int or count < 0):
            errors.append(f"{label}.download_count must be a non-negative integer or null.")

    for index, relation in enumerate(records("relations")):
        label = f"relations[{index}]"
        if not isinstance(relation, dict):
            errors.append(f"{label} must be an object.")
            continue
        for field in ("source_project_id", "target_project_id"):
            endpoint = check_text(relation, field, label)
            if endpoint is not None and endpoint not in project_ids:
                errors.append(f"{label}.{field} is absent from projects: {endpoint}")
        check_text(relation, "relation_type", label)
        check_time(relation, label)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to a normalized metadata JSON document")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"Cannot read input: {error}", file=sys.stderr)
        return 2
    errors = validate(payload)
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, indent=2))
        return 1
    print(json.dumps({
        "valid": True,
        "synthetic": payload["synthetic"],
        "projects": len(payload["projects"]),
        "relations": len(payload["relations"]),
        "note": "Structural validation only; this does not establish research validity."
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
