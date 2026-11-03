import json
import os
from pathlib import Path
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
start = time.process_time()
children = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime + resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime
def cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() - start + r.ru_utime + r.ru_stime - children

checkpoint = {"status": "MATRIX_VALID_IMPLEMENTED_ACTUAL_PRODUCER_STARTED", "pid": os.getpid(), "budget_total_CPU_seconds": 5, "matrix_validity": "MATRIX_VALIDITY.json", "actual_controls_executed": 0}
(HERE / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n")
compiled = subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "probe.cpp"), "-o", str(HERE / "probe")], capture_output=True, text=True)
(HERE / "compile.log").write_text(compiled.stdout + compiled.stderr)
compiled.check_returncode()
compile_cpu = cpu()
remaining = max(0, 5 - compile_cpu - 0.015)
run = subprocess.run([str(HERE / "probe"), str(HERE), str(remaining)], capture_output=True, text=True)
(HERE / "run.log").write_text(run.stdout + run.stderr)
run.check_returncode()
result = json.loads((HERE / "NATIVE_RESULT.json").read_text())
result.update({"target_Delta": 6, "target_D": 10, "savedL": 1394189, "field_q": 53, "compile_and_driver_before_native_CPU_seconds": compile_cpu, "total_parent_and_child_CPU_seconds": cpu(), "ordinary_bad_unordered_pairs": None, "BFS_scope": "One complete identity BFS per tested new Cayley model; connected Cayley symmetry gives exact global diameter", "controls_scope": "Exactly the two frozen alpha matrices and fixed B=(0,1), C=(0,2), no further vector or field search"})
(HERE / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
(HERE / "checkpoint.json").write_text(json.dumps({"status": result["status"], "actual_controls_executed": result["controls_evaluated"], "controls_unattempted": result["controls_unattempted"], "total_CPU_seconds": result["total_parent_and_child_CPU_seconds"]}, indent=2) + "\n")
print(run.stdout, end="")
print(json.dumps({"status": result["status"], "total_CPU_seconds": result["total_parent_and_child_CPU_seconds"]}))
