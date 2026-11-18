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
    files = [
        root / "README.md",
        root / "README.zh-CN.md",
        root / "CONTRIBUTING.md",
        root / "CONTRIBUTING.zh-CN.md",
        root / "AGENTS.md",
    ]
    files.extend([
        root / "case-studies/README.md",
        root / "development/README.md",
        root / "figures/mathrsi/README.md",
        root / "figures/mathrsi/media/README.md",
    ])
    files.extend(sorted((root / "examples").rglob("*.md")))
    # Case landing pages are maintained; copied historical proof sources retain
    # their original context and have a separate HTML portability check.
    for case in sorted((root / "case-studies").glob("*")):
        files.extend(sorted(case.glob("*.md")))
        reader_guide = case / "readers/README.md"
        if reader_guide.exists():
            files.append(reader_guide)
    for directory in [root / "docs", root / "mcp-servers", *sorted((root / "base/skills").glob("mathrsi-*"))]:
        files.extend(sorted(directory.rglob("*.md")))
    for domain in (root / "plugins").iterdir():
        files.extend(sorted((domain / "skills").rglob("*.md")))
        for directory in ("references", "examples"):
            files.extend(sorted((domain / directory).rglob("*.md")))
        for entry in (domain / "README.md", domain / "archive/README.md"):
            if entry.exists():
                files.append(entry)
        readme = domain / "knowledge/README.md"
        if readme.exists():
            files.append(readme)
    # Original historical documents are immutable snapshots, not maintained routes.
    # Bundled ARIS resource closure is tested separately by base/tests/smoke_bundle.py.
    errors = []
    checked = 0
    for source in files:
        if not source.is_file():
            errors.append(f"Missing document: {source.relative_to(root)}")
            continue
        text = source.read_text(encoding="utf-8")
        text = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", text,
                      flags=re.MULTILINE | re.DOTALL)
        text = re.sub(r"`[^`\n]*`", "", text)
        text = re.sub(r"\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)", "", text)
        text = re.sub(r"\$[^$\n]*\$", "", text)
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
                errors.append(f"Out-of-repository route: {source.relative_to(root)} -> {target}")
                continue
            checked += 1
            if not destination.exists():
                errors.append(f"{source.relative_to(root)} -> {target}")
    for folder in (root / ".agents", root / ".claude"):
        for alias in folder.rglob("*"):
            if alias.is_symlink() and (not alias.exists() or not alias.resolve().is_relative_to(root)):
                errors.append(f"Invalid skill alias: {alias.relative_to(root)}")
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {len(files)} documents and {checked} local link targets; "
          f"{len(errors)} missing.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
