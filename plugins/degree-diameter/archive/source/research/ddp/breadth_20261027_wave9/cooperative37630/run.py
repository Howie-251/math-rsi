"""Exactly two deterministic cooperative starts; two coordinate sweeps maximum."""

import json
import math
from pathlib import Path
import resource
import subprocess
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "research/ddp/breadth_20261027_wave4/pencil_source/deg11_diam5_n37628.txt"
OLD = ROOT / "research/ddp/breadth_20261027_wave4/record37628_single_extension/result.json"


def children_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def main():
    began, wall, before = time.process_time(), time.monotonic(), children_cpu()
    old = json.loads(OLD.read_text())["best_neighbors"]
    assert len(old) == 11
    (HERE / "old_best_pins.txt").write_text("11\n" + " ".join(map(str, old)) + "\n")
    subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "search.cpp"), "-o", str(HERE / "search")], check=True)
    compiled = children_cpu()
    hard = max(1, math.floor(30 - (compiled - before) - (time.process_time() - began) - 0.1))
    internal = max(0.1, hard - 1)

    def limit():
        resource.setrlimit(resource.RLIMIT_CPU, (hard, hard))

    with (HERE / "production.log").open("w") as log:
        process = subprocess.Popen([str(HERE / "search"), str(HERE), str(SOURCE),
                                    str(HERE / "old_best_pins.txt"), str(internal)],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   text=True, bufsize=1, preexec_fn=limit)
        for line in process.stdout:
            log.write(line)
            log.flush()
            print(line, end="", flush=True)
        code = process.wait()
    file = HERE / "search_result.json"
    d = json.loads(file.read_text()) if file.exists() else {"status": "PROCESS_TERMINATED_PARTIAL_UNKNOWN"}
    d.update({"process_returncode": code, "compile_CPU_seconds": compiled - before,
        "native_CPU_seconds_including_source_prep": children_cpu() - compiled,
        "driver_CPU_seconds": time.process_time() - began,
        "total_CPU_seconds_including_prep_compile_search": children_cpu() - before + time.process_time() - began,
        "wall_seconds": time.monotonic() - wall, "total_CPU_budget_seconds": 30,
        "native_CPU_hard_limit_seconds": hard, "workers": 1, "restarts": 0,
        "source": str(SOURCE.relative_to(ROOT)), "old_single_pin_source": str(OLD.relative_to(ROOT)),
        "old_D5_evidence": "Author published README/Zenodo23653049 plus Comellas D5 entry; author/table raw rows already compared equal in pencil_source/SOURCE_NOTES.md. No local full-source D5 BFS is claimed here.",
        "scope": "Two adjacent new vertices, each at most10 old pins, sharing only old deficit>=2; exactly the two prescribed deterministic initializations and at most2 complete coordinate sweeps per start.",
        "new_lower_bounds": 0, "pending": ["root_independent_degree_and_two_new_root_full_BFS"]})
    (HERE / "terminal.json").write_text(json.dumps(d, indent=2) + "\n")
    print(json.dumps(d, indent=2), flush=True)


if __name__ == "__main__":
    main()
