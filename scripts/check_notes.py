#!/usr/bin/env python3
"""Validate notes/ and practice/ before they are committed or published.

Checks front matter, file placement, relative links and images, SVG
well-formedness, and that no raw inbox material is tracked by git.
Standard library only. Exit code 1 on any error.

    python3 scripts/check_notes.py
"""

import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LIST = re.compile(r"^\[(.*)\]$")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

NOTE_REQUIRED = ["title", "subject", "summary", "tags", "status", "created", "updated"]
PRACTICE_REQUIRED = ["title", "subject", "kind", "summary", "tags", "difficulty", "created", "updated"]
ENUMS = {"status": {"learning", "confident"}, "kind": {"practice"}, "difficulty": {"easy", "medium", "hard"}}

errors = []


def error(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def front_matter(path, text):
    """Parse the simple `key: value` front matter these notes use."""
    if not text.startswith("---\n"):
        error(path, "missing front matter (must start with ---)")
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        error(path, "front matter is not closed with ---")
        return None, text
    data = {}
    for n, line in enumerate(text[4:end].splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            error(path, f"line {n}: expected 'key: value'")
            continue
        data[key.strip()] = value.split(" #")[0].strip()
    return data, text[end + 5:]


def check_fields(path, data, required, subject):
    for key in required:
        if not data.get(key):
            error(path, f"front matter needs '{key}'")
    for key in ("created", "updated"):
        if data.get(key) and not DATE.match(data[key]):
            error(path, f"'{key}' must be YYYY-MM-DD, got '{data[key]}'")
    if data.get("created") and data.get("updated") and data["updated"] < data["created"]:
        error(path, "'updated' is earlier than 'created'")
    for key in ("tags", "aliases", "related"):
        if data.get(key) and not LIST.match(data[key]):
            error(path, f"'{key}' must be a list like [a, b]")
    for key, allowed in ENUMS.items():
        if key in required and data.get(key) and data[key] not in allowed:
            error(path, f"'{key}' must be one of {sorted(allowed)}, got '{data[key]}'")
    if data.get("subject") and data["subject"] != subject:
        error(path, f"subject '{data['subject']}' does not match folder '{subject}'")


def check_links(path, body):
    for target in LINK.findall(body):
        if re.match(r"^(https?:|mailto:|#)", target):
            continue
        resolved = (path.parent / target.split("#")[0]).resolve()
        if not resolved.exists():
            error(path, f"broken link or image: {target}")


def main():
    files = sorted(ROOT.glob("notes/*/*.md")) + sorted(ROOT.glob("practice/*/*.md"))
    stray = [p for p in ROOT.glob("notes/**/*.md") if p.parent.parent != ROOT / "notes"]
    for p in stray:
        error(p, "notes must live directly in notes/<subject>/")
    for path in files:
        kind = path.parts[len(ROOT.parts)]
        subject = path.parent.name
        if not SLUG.match(subject):
            error(path, f"subject folder '{subject}' must be lowercase kebab-case")
        stem = path.stem
        if kind == "practice" and not re.match(r"^\d{3}-[a-z0-9-]+$", stem):
            error(path, "practice files must be named NNN-slug.md")
        if kind == "notes" and not SLUG.match(stem):
            error(path, "note files must be named with a kebab-case slug")
        data, body = front_matter(path, path.read_text(encoding="utf-8"))
        if data is not None:
            check_fields(path, data, NOTE_REQUIRED if kind == "notes" else PRACTICE_REQUIRED, subject)
        check_links(path, body)
    for svg in ROOT.glob("notes/*/assets/*.svg"):
        try:
            ET.parse(svg)
        except ET.ParseError as exc:
            error(svg, f"invalid SVG: {exc}")
    tracked = subprocess.run(["git", "ls-files", "inbox"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    for name in tracked:
        if name != "inbox/README.md":
            errors.append(f"{name}: raw inbox material must not be committed")
    if errors:
        print(f"{len(errors)} problem(s):")
        print("\n".join(f"  - {e}" for e in errors))
        return 1
    print(f"OK: {len(files)} files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
