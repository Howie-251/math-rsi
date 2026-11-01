"""Bounded local checks of unmodified Argus Lean checker, not a platform run."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
ARGUS = PROJECT / "ref/software/Argus"
LEAN = PROJECT / ".tools/elan/toolchains/leanprover--lean4---v4.24.0/bin/lean"
sys.path[:0] = [str(HERE / "deps"), str(ARGUS)]
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
os.environ["ELAN_HOME"] = str(PROJECT / ".tools/elan")
os.environ["PATH"] = str(LEAN.parent) + os.pathsep + os.environ.get("PATH", "")
os.environ["ARGUS_SKILL_HOME"] = str(HERE / "isolated-argus-home")
SOURCES = HERE / "sources"
SOURCES.mkdir(exist_ok=True)
os.environ["LEAN_PATH"] = str(SOURCES)

from argus.tools.lean_check import run_lean_check


def command(args: list[str]) -> dict:
    result = subprocess.run(args, cwd=SOURCES, capture_output=True, text=True, timeout=45)
    return dict(command=args, exit_code=result.returncode, stdout=result.stdout, stderr=result.stderr)


def write(name: str, source: str) -> Path:
    path = SOURCES / name
    path.write_text(source, encoding="utf-8")
    return path


fixtures = {
    "Clean.lean": "theorem clean_target : True := by trivial\n#print axioms clean_target\n",
    "DefinitionOnly.lean": "def Target : Prop := False\n#check Target\n",
    "LocalAxiom.lean": "axiom unproved : False\ntheorem bad : False := unproved\n",
    "LocalSorry.lean": "theorem unfinished : False := by sorry\n",
    "ImportedAxiom.lean": "import AxiomDependency\ntheorem imported_bad : False := dependency_axiom\n#print axioms imported_bad\n",
    "ImportedSorry.lean": "import SorryDependency\ntheorem imported_unfinished : False := dependency_sorry\n#print axioms imported_unfinished\n",
}
builds = []
for name, content in {
    "AxiomDependency.lean": "axiom dependency_axiom : False\n",
    "SorryDependency.lean": "theorem dependency_sorry : False := by sorry\n",
}.items():
    source = write(name, content)
    result = command([str(LEAN), "-o", str(source.with_suffix(".olean")), str(source)])
    builds.append(result)
    if result["exit_code"]:
        raise RuntimeError(result)

results = {}
for name, source in fixtures.items():
    results[name] = run_lean_check(write(name, source), lean_bin=str(LEAN), timeout_seconds=30)
    print(name, results[name]["status"], results[name]["audit_exit_code"], flush=True)

record = {
    "scope": "Unmodified Argus run_lean_check and Lean auditor, direct Lean 4.24.0; no platform, agent, or external model run",
    "argus_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ARGUS, text=True).strip(),
    "lean_version": command([str(LEAN), "--version"]),
    "dependency_builds": builds,
    "checks": results,
}
(HERE / "probe-results.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
