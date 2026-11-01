#!/usr/bin/env python3
"""Check local inline Markdown link targets in MathRSI's maintained docs.

This optional development helper ignores URLs, anchors, fenced examples and
external source paths. It checks file existence, not anchors or proof validity.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    files = [root / "README.md", root / "AGENTS.md"]
    for directory in ("base", "plugins", "docs"):
        files.extend(sorted((root / directory).rglob("*.md")))
    errors = []
    checked = 0
    for source in files:
        if not source.is_file():
            errors.append(f"Missing document: {source.relative_to(root)}")
            continue
        text = source.read_text(encoding="utf-8")
        text = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", text,
                      flags=re.MULTILINE | re.DOTALL)
        for target in re.findall(r"\]\(([^\n)]+)\)", text):
            target = target.strip().removeprefix("<").removesuffix(">")
            parts = urlsplit(target)
            if parts.scheme or not parts.path:
                continue
            path = Path(unquote(parts.path))
            if path.is_absolute():
                continue
            destination = (source.parent / path).resolve()
            if not destination.is_relative_to(root):
                continue
            checked += 1
            if not destination.exists():
                errors.append(f"{source.relative_to(root)} -> {target}")
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {len(files)} documents and {checked} local link targets; "
          f"{len(errors)} missing.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
