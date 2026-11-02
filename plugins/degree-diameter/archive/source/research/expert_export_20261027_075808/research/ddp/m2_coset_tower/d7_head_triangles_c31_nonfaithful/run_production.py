"""One authorized worker: compile, one calibration, then the exact bounded run."""
import json
import math
import os
import resource
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUDGET = 120.0
EARLIER_COMPILE_CHARGE = 1.0  # Conservative CPU charge; failed attempt wall time was 0.3385 s.


def cpu():
    own = resource.getrusage(resource.RUSAGE_SELF)
    children = resource.getrusage(resource.RUSAGE_CHILDREN)
    return own.ru_utime + own.ru_stime + children.ru_utime + children.ru_stime


assert not (HERE / "production.terminal.json").exists(), "No automatic restart"
start = cpu()
wall = time.monotonic()
before = cpu()
compile_result = subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "production.cpp"),
                                 "-o", str(HERE / "production")], capture_output=True, text=True)
compile_cpu = cpu() - before
(HERE / "compile.log").write_text(compile_result.stdout + compile_result.stderr)
assert compile_result.returncode == 0, compile_result.stderr
before = cpu()
calibration = subprocess.run([str(HERE / "production"), "calibrate", str(HERE)],
                             capture_output=True, text=True)
calibration_cpu = cpu() - before
(HERE / "calibration.log").write_text(calibration.stdout + calibration.stderr)
assert calibration.returncode == 0, calibration.stderr
cal = json.loads((HERE / "calibration.json").read_text())
assert cal["pointwise_BH_distance_comparisons"] == 6696
assert cal["original_and_quotient_BB_masks_equal"] and cal["all_465_BB_targets_match_BFS"]
prior = EARLIER_COMPILE_CHARGE + cpu() - start
remaining = BUDGET - prior - 2.0
assert remaining > 0
preparation = {"status": "PREPARED_AND_ONE_CALIBRATION_PASSED",
               "compile_CPU_seconds": compile_cpu, "calibration_CPU_seconds": calibration_cpu,
               "preparation_recorded_CPU_seconds": prior - EARLIER_COMPILE_CHARGE,
               "preparation_budget_accounted_CPU_seconds": prior,
               "production_CPU_limit_seconds": remaining,
               "earlier_failed_compile_conservative_CPU_charge": EARLIER_COMPILE_CHARGE,
               "cumulative_CPU_budget_seconds": BUDGET, "worker_count": 1,
               "quotient_key_scope": 405000, "original_lift_scope": 3240000,
               "actual_calibration_original_graphs": 1, "actual_calibration_quotient_graphs": 1}
(HERE / "production.prepare.json").write_text(json.dumps(preparation, indent=2) + "\n")
print(json.dumps(preparation), flush=True)


def cap():
    bound = math.ceil(remaining + 1)
    resource.setrlimit(resource.RLIMIT_CPU, (bound, bound))


args = [str(HERE / "production"), "run", str(HERE), str(remaining)]
with (HERE / "production.log").open("w") as logfile:
    proc = subprocess.Popen(args, stdout=logfile, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {"status": "RUNNING", "pid": proc.pid, "driver_pid": os.getpid(),
           "worker_count": 1, "command": args, "budget_CPU_seconds": BUDGET,
           "preparation_budget_accounted_CPU_seconds": prior, "production_CPU_limit_seconds": remaining}
    (HERE / "production.run.json").write_text(json.dumps(run, indent=2) + "\n")
    print(json.dumps(run), flush=True)
    returncode = proc.wait()
assert returncode == 0, f"Production exited {returncode}; no automatic restart"
terminal = json.loads((HERE / "production.terminal.json").read_text())
run.update(status=terminal["status"], running=False, exit_code=returncode,
           next_cursor=terminal["next_cursor"])
(HERE / "production.run.json").write_text(json.dumps(run, indent=2) + "\n")
summary = {"status": terminal["status"], "worker_count": 1, "restarts": 0,
           "quotient_key_scope": 405000, "covered_original_lift_scope": 3240000,
           "counts": terminal["counts"], "next_cursor": terminal["next_cursor"],
           "preparation_recorded_CPU_seconds": prior - EARLIER_COMPILE_CHARGE,
           "preparation_budget_accounted_CPU_seconds": prior, "compile_CPU_seconds": compile_cpu,
           "calibration_CPU_seconds": calibration_cpu,
           "measured_recorded_CPU_seconds": cpu() - start,
           "budget_accounted_CPU_seconds": EARLIER_COMPILE_CHARGE + cpu() - start,
           "earlier_failed_compile_conservative_CPU_charge": EARLIER_COMPILE_CHARGE,
           "CPU_budget_seconds": BUDGET, "wall_seconds": time.monotonic() - wall,
           "independent_final_check": "parent-owned, not run here",
           "original_unexpanded_lifts_not_reported_as_BFS": True}
(HERE / "production.summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2), flush=True)
