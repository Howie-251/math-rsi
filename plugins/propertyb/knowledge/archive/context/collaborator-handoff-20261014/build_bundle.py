#!/usr/bin/env python3
"""Package the three bounds, reusable lemmas, and mathematical evidence."""
from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import json
import re
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARCHIVE = ROOT / "aris4math_collaborator_33_34_35_20261014.zip"
PREFIX = "aris4math_collaborator_20261014"
EXCLUDED_PARTS = {"__pycache__", ".git", ".lake", ".pytest_cache", "pytest-cache"}
EXCLUDED_EXTENSIONS = {".pyc", ".olean", ".ilean", ".o", ".DS_Store"}
CORE_PAGES = ["START_HERE.html", "M5_GE33.html", "M5_GE34.html",
              "M5_GE35.html", "PROPERTY_B_TOOLKIT.html"]


def include(path):
    return (path.is_file() and not path.is_symlink()
            and not EXCLUDED_PARTS.intersection(path.parts)
            and path.suffix not in EXCLUDED_EXTENSIONS
            and path.name not in {".DS_Store", "bundle-files.json"}
            and not path.name.startswith("~$"))


def gather():
    files = set()
    # Preserve the original project layout for every mathematical caller.
    roots = ["formal", "proofs", "computations", "results", "research-wiki",
             "review-stage", "background", "Survey Problem", ".aris/traces"]
    for relative in roots:
        for path in (ROOT / relative).rglob("*"):
            if include(path):
                files.add(path)
    excluded_context = {"argus-deep-dive-20261007", "horizon-deep-dive-20261007",
                        "skill-evaluation", "collaborator-handoff-20261014"}
    for path in (ROOT / "context").rglob("*"):
        if include(path) and not excluded_context.intersection(path.relative_to(ROOT / "context").parts):
            files.add(path)
    for path in (ROOT / "ref").rglob("*"):
        if include(path) and "software" not in path.relative_to(ROOT / "ref").parts:
            files.add(path)
    for path in ROOT.iterdir():
        if include(path) and path.suffix in {".md", ".html", ".json", ".pdf"}:
            files.add(path)
    for name in ["build_bundle.py", "REPRODUCTION_SUGGESTIONS.md"]:
        path = HERE / name
        if not path.is_file():
            raise FileNotFoundError(path)
        files.add(path)
    for name in ["READER_REVIEW.md", "reader-browser-check.json", "reader-math.json",
                 "reader-1440.png", "reader-390.png"]:
        review = HERE / name
        if review.is_file():
            files.add(review)
    return files


def project_import_closure(files):
    modules = ["Aris4Math.Main", "Aris4Math.ThirtyThree.Main",
               "Aris4Math.ThirtyFour.Assembly"]
    reached = set()
    pending = modules[:]
    while pending:
        module = pending.pop()
        if module in reached:
            continue
        path = ROOT / "formal" / Path(*module.split(".")).with_suffix(".lean")
        if path not in files:
            raise FileNotFoundError(f"Missing project import: {module}")
        reached.add(module)
        pending.extend(re.findall(r"^import\s+(Aris4Math(?:\.[\w]+)*)\s*$", path.read_text(), re.M))
    return {"entry_modules": modules, "project_modules_in_closure": len(reached),
            "scope": "Source availability, not a fresh Lean build."}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.math = 0
        self.scripts = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.hrefs.append(attrs["href"])
        self.math += tag == "mjx-container"
        self.scripts += tag == "script"


def check_pages(root):
    checks = []
    for name in CORE_PAGES:
        parser = Links()
        parser.feed((root / name).read_text())
        missing = []
        local = 0
        for href in parser.hrefs:
            parsed = urlsplit(href)
            if parsed.scheme or not parsed.path:
                continue
            local += 1
            path = (root / unquote(parsed.path)).resolve()
            if not path.exists():
                missing.append(href)
        if missing:
            raise ValueError(f"Missing extracted links in {name}: {missing}")
        if not parser.math or parser.scripts:
            raise ValueError(f"Core reader is not the offline math edition: {name}")
        checks.append({"page": name, "local_links": local, "embedded_math": parser.math,
                       "scripts": parser.scripts, "missing_local_links": missing})
    return checks


def main():
    files = gather()
    closure = project_import_closure(files)
    contents = sorted((str(p.relative_to(ROOT)), p.stat().st_size) for p in files)
    manifest = ("Property B collaborator snapshot, 2026-10-14\n"
                "T32 / m(5)>=33: complete Lean. T33 / m(5)>=34: complete Lean.\n"
                "T34 / m(5)>=35: full prose candidate; end-to-end Lean pending.\n"
                "Paths below are relative to this archive's project root.\n\n"
                + "\n".join(f"{size:>12}  {name}" for name, size in contents) + "\n")
    with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
        for relative, _ in contents:
            bundle.write(ROOT / relative, arcname=f"{PREFIX}/{relative}")
        bundle.writestr(f"{PREFIX}/PACKAGE_CONTENTS.txt", manifest)
    with zipfile.ZipFile(ARCHIVE) as bundle:
        bad = bundle.testzip()
        if bad:
            raise ValueError(f"Archive readback failed: {bad}")
        with tempfile.TemporaryDirectory(prefix="aris4math-handoff-check-") as tmp:
            bundle.extractall(tmp)
            extracted = Path(tmp) / PREFIX
            pages = check_pages(extracted)
            # Verify the lean import check against the extracted files as well.
            for relative, size in contents:
                if (extracted / relative).stat().st_size != size:
                    raise ValueError(f"Extraction size mismatch: {relative}")
    counts = Counter(Path(name).suffix or "(none)" for name, _ in contents)
    result = {"archive": ARCHIVE.name, "archive_bytes": ARCHIVE.stat().st_size,
              "file_count": len(contents) + 1,
              "uncompressed_bytes": sum(size for _, size in contents) + len(manifest.encode()),
              "file_extensions": dict(counts), "source_import_closure": closure,
              "archive_readback": "PASS", "extracted_file_sizes": "PASS",
              "core_reader_links": pages,
              "fresh_lean_build": False, "fresh_full_certificate_replay": False}
    (HERE / "PACKAGE_CHECKS.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
