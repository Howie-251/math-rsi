"""One fixed504-layer construction and at most2x2000 global cubic-H switches."""

import json
import math
from pathlib import Path
import resource
import subprocess
import time


HERE = Path(__file__).resolve().parent


def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def main():
    started, wall, children = time.process_time(), time.monotonic(), child_cpu()
    subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "search.cpp"), "-o", str(HERE / "search")], check=True)
    after_compile = child_cpu()
    hard = max(1, math.floor(20 - (after_compile - children) - (time.process_time() - started) - 0.1))
    internal = max(0.1, hard - 1.0)

    def limit():
        resource.setrlimit(resource.RLIMIT_CPU, (hard, hard))

    with (HERE / "production.log").open("w") as log:
        process = subprocess.Popen([str(HERE / "search"), str(HERE), str(internal)],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   text=True, bufsize=1, preexec_fn=limit)
        for line in process.stdout:
            log.write(line)
            log.flush()
            print(line, end="", flush=True)
        code = process.wait()
    result_file = HERE / "search_result.json"
    d = json.loads(result_file.read_text()) if result_file.exists() else {"status": "PROCESS_TERMINATED_PARTIAL_UNKNOWN"}
    d.update({"process_returncode": code, "compile_CPU_seconds": after_compile - children,
              "search_process_CPU_seconds": child_cpu() - after_compile,
              "driver_CPU_seconds": time.process_time() - started,
              "total_CPU_seconds_including_compile": child_cpu() - children + time.process_time() - started,
              "wall_seconds": time.monotonic() - wall, "total_CPU_budget_seconds": 20,
              "search_process_CPU_hard_limit_seconds": hard, "workers": 1, "restarts": 0,
              "initial_H_rule": "Seven36cycles on round-robin disjoint K7 label triples, plus independent12-line perfectmatching for each label.",
              "all378_H_edges_free_for_crossgroup_swaps": True,
              "positive_guarantees": ["all A-A distance<=4", "samecell A-C distance<=3", "C-C with intersecting edge labels distance<=4", "samecell C-C distance<=4 even for disjoint labels", "base layers connected independently of H"],
              "ordinary_final_BFS_performed": False,
              "new_lower_bounds": 0, "pending": ["root_unique_final_all504_source_BFS"]})
    (HERE / "terminal.json").write_text(json.dumps(d, indent=2) + "\n")
    print(json.dumps(d, indent=2))


if __name__ == "__main__":
    main()
