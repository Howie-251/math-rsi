"""Exactly the authorized two structure-aware starts; no source BFS."""

import json
import math
from pathlib import Path
import resource
import subprocess
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "research/ddp/m1_degree5_transfer/rithwik650_source.edges"
DISTANCES = HERE.parent / "shortcut_matching_scout/source650_distances.u8"


def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def main():
    started, wall, before = time.process_time(), time.monotonic(), child_cpu()
    subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "search.cpp"), "-o", str(HERE / "search")], check=True)
    compiled = child_cpu()
    hard = max(1, math.floor(20 - (compiled - before) - (time.process_time() - started) - 0.1))
    internal = max(0.1, hard - 1.0)

    def limit():
        resource.setrlimit(resource.RLIMIT_CPU, (hard, hard))

    with (HERE / "production.log").open("w") as log:
        process = subprocess.Popen([str(HERE / "search"), str(HERE), str(SOURCE), str(DISTANCES), str(internal)],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                   bufsize=1, preexec_fn=limit)
        for line in process.stdout:
            log.write(line)
            log.flush()
            print(line, end="", flush=True)
        code = process.wait()
    file = HERE / "search_result.json"
    result = json.loads(file.read_text()) if file.exists() else {"status": "PROCESS_TERMINATED_PARTIAL_UNKNOWN"}
    result.update({"process_returncode": code, "compile_CPU_seconds": compiled - before,
        "search_process_CPU_seconds": child_cpu() - compiled,
        "driver_CPU_seconds": time.process_time() - started,
        "total_CPU_seconds_including_compile_prep_search": child_cpu() - before + time.process_time() - started,
        "wall_seconds": time.monotonic() - wall, "total_CPU_budget_seconds": 20,
        "search_process_CPU_hard_limit_seconds": hard, "workers": 1, "restarts": 0,
        "source": str(SOURCE.relative_to(ROOT)), "distance_cache": str(DISTANCES.relative_to(ROOT)),
        "initial0_rule": "C25-equivariant13rowpairs: head-leaf, five block-leaf, seven remaining leaf-leaf; prefer oldD5 shifts.",
        "initial1_rule": "One oldD5 random greedy matching, length3 augmenting matching-edge repair; single-shuffle nonedge fallback only on failure.",
        "formal_switches_may_break_all_initial_restrictions": True,
        "score_includes_two_matching_edge_paths": True, "source_modified": False,
        "new_lower_bounds": 0, "pending": ["root_unique_final_all650_source_BFS"]})
    (HERE / "terminal.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()
