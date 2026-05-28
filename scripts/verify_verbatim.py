#!/usr/bin/env python3
"""Check whether a restructured draft stays verbatim to the source transcript."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FENCE_RE = re.compile(r"```.*?```", re.S)
DELETE_RE = re.compile(r"~~.*?~~", re.S)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+")
TABLE_RE = re.compile(r"^\s*\|.*\|\s*$")
LIST_MARKER_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
TIME_LABEL_RE = re.compile(r"^\s*\*\*\([^)]*\)\s*【[^】]+】\*\*\s*")


def normalize(text: str) -> str:
    text = text.replace("\ufeff", "")
    text = re.sub(r"\s+", "", text)
    text = text.replace("“", "\"").replace("”", "\"")
    text = text.replace("‘", "'").replace("’", "'")
    return text


def strip_markdown(line: str) -> str:
    line = MD_LINK_RE.sub(r"\1", line)
    line = re.sub(r"`([^`]+)`", r"\1", line)
    line = re.sub(r"^\s*>\s?", "", line)
    line = LIST_MARKER_RE.sub("", line)
    line = TIME_LABEL_RE.sub("", line)
    line = line.replace("**", "").replace("__", "")
    return line.strip()


def candidate_lines(markdown: str) -> list[tuple[int, str]]:
    markdown = FENCE_RE.sub("", markdown)
    markdown = DELETE_RE.sub("", markdown)
    out: list[tuple[int, str]] = []

    for lineno, raw in enumerate(markdown.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        if HEADING_RE.match(line) or TABLE_RE.match(line):
            continue
        if line.startswith("|-") or line.startswith("---"):
            continue
        line = strip_markdown(line)
        if not line:
            continue
        if line.endswith("：") or line.endswith(":"):
            continue
        if len(normalize(line)) < 4:
            continue
        out.append((lineno, line))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify that draft lines can be found verbatim in the source transcript."
    )
    parser.add_argument("--source", required=True, help="Original transcript text/markdown file")
    parser.add_argument("--draft", required=True, help="Restructured draft markdown file")
    args = parser.parse_args()

    source_path = Path(args.source).expanduser().resolve()
    draft_path = Path(args.draft).expanduser().resolve()
    if not source_path.exists():
        raise SystemExit(f"Source not found: {source_path}")
    if not draft_path.exists():
        raise SystemExit(f"Draft not found: {draft_path}")

    source_text = normalize(source_path.read_text(encoding="utf-8"))
    misses: list[tuple[int, str]] = []
    checked = 0

    for lineno, line in candidate_lines(draft_path.read_text(encoding="utf-8")):
        checked += 1
        if normalize(line) not in source_text:
            misses.append((lineno, line))

    print(f"checked_lines={checked}")
    print(f"missing_lines={len(misses)}")
    for lineno, line in misses:
        print(f"[line {lineno}] {line}")

    return 1 if misses else 0


if __name__ == "__main__":
    raise SystemExit(main())
