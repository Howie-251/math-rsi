#!/usr/bin/env python3
"""Copy the six existing readers, adapting local links without re-rendering math.

From a clone: python3 case-studies/property-b/tools/package_readers.py --check
Maintainer: add --source /path/to/original/property-b/workspace to rebuild and
compare with the original files. This does not run any mathematical checker.
"""

import argparse
import html
import json
import os
from pathlib import Path
import re
import shutil
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit, urlunsplit


REPO = Path(__file__).resolve().parents[3]
CASE = REPO / "case-studies/property-b"
READERS = CASE / "readers"
ARCHIVE = REPO / "plugins/propertyb/knowledge/archive"
REPORT = REPO / "development/propertyb-case-20261102/PORTABILITY.json"
MANIFEST = READERS / "PORTABILITY_MANIFEST.json"
PAGES = (
    "PROPERTY_B_GENERAL_BOUND.html",
    "PROPERTY_B_GENERAL_LEAN.html",
    "PROPERTY_B_GENERAL_LEAN_PILOT.html",
    "M6_GE67.html",
    "M8_M9_IMPROVEMENTS.html",
    "K12_LOCK_COMPARISON.html",
)
ASSETS = ("delta.svg", "delta.png", "small.svg", "small.png", "overview.svg",
          "propertyb_bounds.pdf")
METADATA_SOURCES = (
    "context/propertyb-m6-67-progress-20261029/render/reader-source.md",
    "context/propertyb-small-updates-20261029/render-8-9/reader-source.md",
)
# Match only ordinary HTML href/src, leaving SVG xlink:href and all other bytes.
ATTR = re.compile(r"(?<![\w:-])(?:href|src)\s*=\s*([\"'])(.*?)\1", re.I)


def local_path(value):
    parsed = urlsplit(html.unescape(value))
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    return unquote(parsed.path)


def copy_file(source, destination, inventory):
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    inventory[str(destination.relative_to(REPO))] = {
        "source": str(source.relative_to(SOURCE)),
        "bytes": source.stat().st_size,
        "source_mtime_ns": source.stat().st_mtime_ns,
    }


def destination_for(path, inventory):
    if path in PAGES:
        return READERS / path
    if path.startswith("figures/propertyb_bounds/"):
        destination = CASE / "assets" / Path(path).name
        if not destination.is_file():
            raise ValueError(f"Asset not selected: {path}")
        return destination
    archived = ARCHIVE / path
    if archived.is_dir():
        # The original directory link now opens its actual review disposition.
        archived /= "DISPOSITION.md"
    if archived.is_file():
        return archived
    destination = READERS / ("sources" if "/" not in path else "evidence") / path
    source = SOURCE / path
    if not source.is_file():
        raise FileNotFoundError(source)
    copy_file(source, destination, inventory)
    return destination


def build():
    inventory = {}
    for name in ASSETS:
        copy_file(SOURCE / "figures/propertyb_bounds" / name,
                  CASE / "assets" / name, inventory)
    for path in METADATA_SOURCES:
        copy_file(SOURCE / path, READERS / "sources" / path, inventory)
    pages = {}
    for name in PAGES:
        source = SOURCE / name
        text = source.read_text()
        rewrites = {}

        def replace(match):
            value = match.group(2)
            path = local_path(value)
            if path is None:
                return match.group(0)
            destination = destination_for(path, inventory)
            parsed = urlsplit(html.unescape(value))
            portable = urlunsplit(("", "", os.path.relpath(destination, READERS),
                                    parsed.query, parsed.fragment))
            rewrites[value] = portable
            return match.group(0).replace(value, portable, 1)

        portable = ATTR.sub(replace, text)
        target = READERS / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(portable)
        shutil.copystat(source, target)
        pages[name] = {"source": name, "source_bytes": source.stat().st_size,
                       "source_mtime_ns": source.stat().st_mtime_ns,
                       "rewrites": rewrites}
    manifest = {"format": 1, "method": "href/src-only adaptation; no re-rendering",
                "pages": pages, "copied_files": inventory,
                "directory_link_mapping": {
                    "context/propertyb-general-lean-pilot/reviews/C":
                    "plugins/propertyb/knowledge/archive/context/"
                    "propertyb-general-lean-pilot/reviews/C/DISPOSITION.md"}}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = set()
        self.svgs = 0
        self.math = 0
        self.runtime = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.ids.update([values["id"]] if "id" in values else [])
        self.svgs += tag == "svg"
        self.math += tag == "mjx-container"
        for key in ("href", "src"):
            if values.get(key):
                self.refs.append(values[key])
                if key == "src" and urlsplit(values[key]).scheme in ("http", "https"):
                    self.runtime.append(values[key])


def check():
    manifest = json.loads(MANIFEST.read_text())
    results = []
    errors = []
    for name, info in manifest["pages"].items():
        page = READERS / name
        portable = page.read_text()
        document = Document()
        document.feed(portable)
        local_refs = 0
        for ref in document.refs:
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc:
                continue
            local_refs += 1
            target = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
            if not target.exists():
                errors.append(f"{name}: missing {ref}")
            elif target.suffix == ".html" and parsed.fragment:
                other = document
                if target != page:
                    other = Document()
                    other.feed(target.read_text())
                if unquote(parsed.fragment) not in other.ids:
                    errors.append(f"{name}: missing fragment {ref}")
        fidelity = "not rerun; requires original --source workspace"
        if SOURCE:
            reverse = {v: k for k, v in info["rewrites"].items()}
            restored = ATTR.sub(lambda m: m.group(0).replace(
                m.group(2), reverse.get(m.group(2), m.group(2)), 1), portable)
            if restored != (SOURCE / info["source"]).read_text():
                errors.append(f"{name}: non-link content differs from original")
            else:
                fidelity = "PASS: reversing recorded link rewrites restores exact original text"
        results.append({"reader": name, "bytes": page.stat().st_size,
                        "local_href_src_occurrences": local_refs,
                        "distinct_rewrites": len(info["rewrites"]),
                        "svg_elements": document.svgs,
                        "math_containers": document.math,
                        "remote_src": document.runtime, "fidelity": fidelity})
    for relative, info in manifest["copied_files"].items():
        target = REPO / relative
        if not target.is_file() or target.stat().st_size != info["bytes"]:
            errors.append(f"Missing or wrong size copied file: {relative}")
        elif SOURCE and target.read_bytes() != (SOURCE / info["source"]).read_bytes():
            errors.append(f"Copied file differs from original: {relative}")
    result = {"status": "PASS" if not errors else "FAIL", "pages": results,
              "copied_supporting_files": len(manifest["copied_files"]),
              "copied_supporting_bytes": sum(f["bytes"] for f in manifest["copied_files"].values()),
              "original_available": bool(SOURCE), "errors": errors,
              "scope": "Six promoted HTML pages and their direct href/src targets; "
              "not recursive historical Markdown/archive validation or mathematics verification."}
    if SOURCE:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return not errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--check", action="store_true", help="Validate without rebuilding")
    args = parser.parse_args()
    SOURCE = args.source.resolve() if args.source else None
    if not args.check:
        if SOURCE is None:
            parser.error("Rebuilding requires --source; clone validation uses --check")
        build()
    raise SystemExit(0 if check() else 1)
