#!/usr/bin/env python3
"""Recompile and consume the E38 structural core; never claims old-layer replay."""
import argparse
import json
import os
import platform
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent


def main():
    if not __debug__:
        raise SystemExit("The original geometric checker requires Python assertions. Run without -O or PYTHONOPTIMIZE.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="New empty output directory, outside the frozen inputs")
    args = parser.parse_args()
    out = args.output.resolve()
    if out == ROOT or ROOT in out.parents:
        raise SystemExit("Use an output directory outside this evidence archive")
    if out.exists() and any(out.iterdir()):
        raise SystemExit("Output must be empty")
    out.mkdir(parents=True, exist_ok=True)
    compiler = os.environ.get("CXX", "c++")
    commands = []

    def run(argv, cwd, display):
        start = time.monotonic()
        result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
        commands.append({"command": display, "exit_code": result.returncode,
                         "wall_seconds": round(time.monotonic() - start, 6)})
        if result.returncode:
            raise RuntimeError(f"Command failed: {display}; exit {result.returncode}")

    start = time.monotonic()
    for part in ("high", "mid"):
        (out / part).mkdir()
    for rel in ("high/FACE19_EXHAUSTIVE", "mid/INDEPENDENT_RAW_FACES"):
        run([compiler, "-O3", "-std=c++17", str(ROOT / "source" / (rel + ".cpp")),
             "-o", str(out / rel)], out,
            f"$CXX -O3 -std=c++17 source/{rel}.cpp -o $OUTPUT/{rel}")
    run([str(out / "high/FACE19_EXHAUSTIVE")], out / "high",
        "cd $OUTPUT/high && ./FACE19_EXHAUSTIVE")
    for r in range(6, 10):
        run([str(out / "mid/INDEPENDENT_RAW_FACES"), f"R{r}", str(r)], out / "mid",
            f"cd $OUTPUT/mid && ./INDEPENDENT_RAW_FACES R{r} {r}")

    # Preserve the original consumer intact. Its second part consumes historical
    # E36 payloads absent from the lite source package. Execute only the explicitly
    # separated, original geometric consumer, as the upstream lite entry does.
    consumer = ROOT / "source/mid/INDEPENDENT_CONSUMER.py"
    text = consumer.read_text(encoding="utf-8")
    cut = text.index("\nbindings=")
    relocated = out / "mid/INDEPENDENT_CONSUMER.py"
    shutil.copyfile(consumer, relocated)
    exec(compile(text[:cut], "INDEPENDENT_CONSUMER.py (geometry prefix)", "exec"),
         {"__file__": str(relocated), "__name__": "__main__"})
    checks = []
    rels = ["high/FACE19_ALL.jsonl", "high/FACE19_COMPATIBLE.jsonl", "high/FACE19_RESULT.json"]
    rels += [f"mid/R{r}_{suffix}" for r in range(6, 10)
             for suffix in ("RAW.bin", "RESULT.json", "BAD.jsonl")]
    for rel in rels:
        frozen = (ROOT / "expected" / rel).read_bytes()
        actual = (out / rel).read_bytes()
        if rel.endswith(".jsonl"):
            equal = [json.loads(x) for x in frozen.splitlines()] == [json.loads(x) for x in actual.splitlines()]
        elif rel.endswith(".json"):
            equal = json.loads(frozen) == json.loads(actual)
        else:
            equal = frozen == actual
        if not equal:
            raise RuntimeError(f"Archived output differs: {rel}")
        checks.append({"path": rel, "equal_entities": equal,
                       "equal_bytes": frozen == actual})
    geometry = json.loads((out / "mid/AUTHOR_GEOMETRY_CONSUMED.json").read_text())
    assert geometry["status"] == "PASS"
    assert geometry["author_actual_pairs_consumed"] == 7608
    assert geometry["weighted_all_raw_pairs"] == 18237120
    version = subprocess.run([compiler, "--version"], capture_output=True, text=True, check=True)
    report = {
        "status": "PASS", "scope": "E38_STRUCTURAL_CORE_ONLY",
        "full_R7_historical_dependency_replay": False,
        "old_E36_and_earlier_payloads": "not_replayed; some intentionally omitted in the supplied lite package",
        "system": {"os": platform.system(), "release": platform.release(),
                   "machine": platform.machine(), "python": platform.python_version(),
                   "compiler": version.stdout.splitlines()[0]},
        "commands": commands,
        "consumer": "original INDEPENDENT_CONSUMER.py, prefix before bindings= only",
        "geometry": geometry,
        "archived_output_comparisons": checks,
        "wall_seconds": round(time.monotonic() - start, 6),
    }
    (out / "REPLAY_RESULT.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("PASS: 35360 faces; 7608 orbit-representative pairs; 18237120 weighted raw pairs.")
    print("Scope: E38 structural core only; historical R7 dependencies not replayed.")


if __name__ == "__main__":
    main()
