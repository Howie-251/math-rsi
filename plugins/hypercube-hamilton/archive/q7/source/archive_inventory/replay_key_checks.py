"""Replay the archived E16 S3 and S2 strong-column checkers offline."""

import argparse
from contextlib import redirect_stdout
from hashlib import file_digest
from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_loader
from io import StringIO
import json
import pathlib
from pathlib import Path, PureWindowsPath
import re
import sys
from unittest.mock import patch


HERE = Path(__file__).resolve().parent
SHA = re.compile(r"[0-9a-f]{64}")


def digest(path):
    with path.open("rb") as file:
        return file_digest(file, "sha256").hexdigest()


def archive_file(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"Path escapes archive: {relative}")
    return path


def digest_index(root):
    index = {}
    for name in ("dependency_bindings", "baseline", "source_map"):
        path = root / "archive_inventory" / f"{name}.jsonl"
        if path.is_file():
            with path.open(encoding="utf-8-sig") as stream:
                for line in stream:
                    entry = json.loads(line)
                    sha = entry.get("sha256")
                    relative = entry.get("archive_path")
                    if isinstance(sha, str) and isinstance(relative, str):
                        index.setdefault(sha.lower(), set()).add(relative)
    return index


def resolve_inputs(root, inputs, index):
    paths = {}
    for entry in inputs:
        reference, sha = entry["reference"], entry["sha256"]
        if not SHA.fullmatch(sha):
            raise ValueError(f"Invalid SHA-256 binding for {reference}")
        candidates = [entry["preferred_archive_path"], *sorted(index.get(sha, ()))]
        for relative in dict.fromkeys(candidates):
            path = archive_file(root, relative)
            if path.is_file() and digest(path) == sha:
                paths[reference.casefold()] = path
                break
        else:
            raise FileNotFoundError(f"Missing exact archived bytes for {reference} (SHA-256 {sha})")
    return paths


class FrozenModules(MetaPathFinder, Loader):
    def __init__(self, modules, historical_root, sources):
        self.modules = {PureWindowsPath(filename).stem: filename for filename in modules}
        self.historical_root = historical_root
        self.sources = sources

    def find_spec(self, fullname, path=None, target=None):
        if fullname in self.modules:
            return spec_from_loader(fullname, self)
        return None

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        self.execute(self.modules[module.__name__], module.__dict__)

    def execute(self, filename, namespace):
        logical = str(self.historical_root / filename)
        namespace["__file__"] = logical
        data = self.sources[filename.casefold()].read_bytes()
        exec(compile(data, logical, "exec"), namespace)


def replay(name, check, sources, source_root):
    checker = check["checker"]
    expected = json.loads(sources[check["reference_result"].casefold()].read_bytes())
    historical_root = PureWindowsPath(source_root)

    class BoundPath(PureWindowsPath):
        # Preserve original directory names used as literal manifest keys.
        # Every read is served by the hash-bound archive copy.
        def resolve(self):
            return self

        def bound_file(self):
            name = self.relative_to(historical_root) if self.is_relative_to(historical_root) else self
            key = name.as_posix().casefold()
            if key not in sources:
                raise FileNotFoundError(f"No frozen input binding for {key}")
            return sources[key]

        def read_bytes(self):
            return self.bound_file().read_bytes()

        def read_text(self, *args, **kwargs):
            return self.bound_file().read_text(*args, **kwargs)

        def stat(self):
            return self.bound_file().stat()

    loader = FrozenModules(check["modules"], historical_root, sources)
    args = [str(historical_root / checker), check["manifest_sha256"]]
    output = StringIO()
    if set(loader.modules) & sys.modules.keys():
        raise RuntimeError("A frozen checker module is already loaded")
    try:
        with patch.object(sys, "meta_path", [loader, *sys.meta_path]), patch.object(sys, "argv", args):
            with patch.object(pathlib, "Path", BoundPath), redirect_stdout(output):
                loader.execute(checker, {"__name__": "__main__"})
    finally:
        for name_in_module_cache in loader.modules:
            sys.modules.pop(name_in_module_cache, None)

    observed = json.loads(output.getvalue())
    cpu_seconds = observed.pop("cpu_seconds")
    expected.pop("cpu_seconds")
    if observed != expected or observed.get("verdict") != "PASS":
        raise ValueError(f"{name} output differs from the frozen independent-check result")
    return dict(check=name, verdict=observed["verdict"], bound_files=len(sources),
                checked_plans=observed["plans"], cpu_seconds=cpu_seconds,
                proof_sha256=observed["proof_sha256"],
                manifest_sha256=observed["manifest_sha256"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=HERE.parent)
    parser.add_argument("--check", action="append", choices=("S3", "S2_STRONG"))
    args = parser.parse_args()
    root = args.archive.resolve()
    manifest = json.loads((HERE / "key_check_inputs.json").read_bytes())
    checks = manifest["checks"]
    index = digest_index(root)
    results = []
    for name in args.check or ("S3", "S2_STRONG"):
        check = checks[name]
        sources = resolve_inputs(root, check["inputs"], index)
        results.append(replay(name, check, sources, manifest["historical_source_root"]))
    print(json.dumps({"checks": results}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
