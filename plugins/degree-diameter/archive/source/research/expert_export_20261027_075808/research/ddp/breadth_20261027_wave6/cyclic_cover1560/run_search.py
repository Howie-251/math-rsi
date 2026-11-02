"""Run only the authorized2x2000 profile, accounting for all preparation CPU."""

import json
import math
from pathlib import Path
import resource
import subprocess
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "context/DD_PORTFOLIO_START_20261026/baselines/d6_D3_known.edges"


def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def main():
    started, wall, children = time.process_time(), time.monotonic(), child_cpu()
    capacity = json.loads((HERE / "capacity.json").read_text())
    assert capacity["status"] == "ALL14400_FORM_CAPACITIES_PASS"
    prep = capacity["CPU_seconds"] + capacity["earlier_self_capacity_CPU_seconds"]
    subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "search.cpp"), "-o", str(HERE / "search")], check=True)
    after_compile = child_cpu()
    compile_cpu = after_compile - children
    remaining = 20 - prep - compile_cpu - (time.process_time() - started)
    hard = max(1, math.floor(remaining - 0.1))
    internal = max(0.1, hard - 1.0)

    def limit():
        resource.setrlimit(resource.RLIMIT_CPU, (hard, hard))

    with (HERE / "production.log").open("w") as output:
        completed = subprocess.run([str(HERE / "search"), str(HERE), str(SOURCE), str(internal)],
                                   stdout=output, stderr=subprocess.STDOUT, preexec_fn=limit)
    rfile = HERE / "search_result.json"
    d = json.loads(rfile.read_text()) if rfile.exists() else {"status": "SEARCH_PROCESS_TERMINATED_PARTIAL_UNKNOWN"}
    d.update({"process_returncode": completed.returncode, "source": str(SOURCE.relative_to(ROOT)),
              "base_BFS_reused": "context/DD_PORTFOLIO_START_20261026/validation/d6_D3_bfs.json",
              "capacity_CPU_seconds_including_self_pretest": prep,
              "compile_CPU_seconds": compile_cpu, "search_process_CPU_seconds": child_cpu() - after_compile,
              "driver_CPU_seconds": time.process_time() - started,
              "total_CPU_seconds_including_all_prep_compile_search": prep + child_cpu() - children + time.process_time() - started,
              "wall_seconds_for_compile_search": time.monotonic() - wall,
              "total_CPU_budget_seconds": 20, "search_process_CPU_hard_limit_seconds": hard,
              "voltage_profile_started": True, "workers": 1, "restarts": 0,
              "new_lower_bounds": 0, "pending": ["root_unique_best_cover_all_source_BFS"],
              "scope": "Only ordinary C13 covers of this fixed120 source; one tree gauge, exactly two fixed voltage starts and at most2000 proposals each."})
    (HERE / "terminal.json").write_text(json.dumps(d, indent=2) + "\n")
    print(json.dumps(d, indent=2))


if __name__ == "__main__":
    main()
