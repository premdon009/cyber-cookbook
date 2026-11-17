"""Shared loader + validation for resources.yml."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
RESOURCES_FILE = ROOT / "resources.yml"

REQUIRED = ("name", "url", "category", "level", "cost", "platform", "team", "clone", "note")
COSTS = {"free", "freemium", "self-hosted"}
PLATFORMS = {"linux", "windows", "both", "web", "cloud", "any"}
TEAMS = {"red", "blue", "purple", "both", "ai"}
LEVELS = {f"L{i}" for i in range(6)}


def load() -> tuple[dict[str, str], list[dict[str, Any]]]:
    data = yaml.safe_load(RESOURCES_FILE.read_text(encoding="utf-8"))
    categories: dict[str, str] = data["categories"]
    resources: list[dict[str, Any]] = data["resources"]
    errors = validate(categories, resources)
    if errors:
        raise SystemExit("resources.yml is invalid:\n  " + "\n  ".join(errors))
    return categories, resources


def validate(categories: dict[str, str], resources: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for i, r in enumerate(resources):
        label = r.get("name", f"entry #{i}")
        for key in REQUIRED:
            if key not in r:
                errors.append(f"{label}: missing '{key}'")
        if label in seen:
            errors.append(f"{label}: duplicate name")
        seen.add(label)
        if r.get("category") not in categories:
            errors.append(f"{label}: unknown category {r.get('category')!r}")
        if r.get("cost") not in COSTS:
            errors.append(f"{label}: cost must be one of {sorted(COSTS)}")
        if r.get("platform") not in PLATFORMS:
            errors.append(f"{label}: platform must be one of {sorted(PLATFORMS)}")
        if r.get("team") not in TEAMS:
            errors.append(f"{label}: team must be one of {sorted(TEAMS)}")
        if r.get("level") not in LEVELS:
            errors.append(f"{label}: level must be L0..L5")
        if r.get("clone") and not r.get("repo"):
            errors.append(f"{label}: clone: true needs a repo")
    return errors
