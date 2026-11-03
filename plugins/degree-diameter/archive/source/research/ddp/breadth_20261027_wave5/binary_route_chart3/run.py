"""One complete binary3-step chart profile; leave one saved candidate to root."""

import json
from pathlib import Path
import resource
import subprocess
import time


HERE = Path(__file__).resolve().parent


def child_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def limit():
    resource.setrlimit(resource.RLIMIT_CPU, (12, 12))


def main():
    began, wall, before = time.process_time(), time.monotonic(), child_cpu()
    subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "search.cpp"), "-o", str(HERE / "search")], check=True)
    after_compile = child_cpu()
    completed = subprocess.run([str(HERE / "search"), str(HERE)], preexec_fn=limit)
    result = json.loads((HERE / "search_result.json").read_text()) if (HERE / "search_result.json").exists() else {
        "status": "PROCESS_TERMINATED_INCOMPLETE"}
    result.update({
        "process_returncode": completed.returncode,
        "compile_CPU_seconds": after_compile - before,
        "search_process_CPU_seconds": child_cpu() - after_compile,
        "driver_CPU_seconds": time.process_time() - began,
        "total_CPU_seconds": child_cpu() - before + time.process_time() - began,
        "wall_seconds": time.monotonic() - wall,
        "worker_count": 1, "total_CPU_budget_seconds": 15,
        "search_process_CPU_hard_limit_seconds": 12, "restarts": 0,
        "best_candidate": "best_candidate.json",
        "independent_finite_calibration": "Reserved for root, one saved candidate all36 ranks and inverse relations.",
        "controller_search_performed": False, "BFS_performed": False,
        "large_lift_generated": False, "new_lower_bounds": 0,
    })
    (HERE / "terminal.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
