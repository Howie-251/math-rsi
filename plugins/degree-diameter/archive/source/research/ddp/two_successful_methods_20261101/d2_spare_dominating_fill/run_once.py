"""One worker, one producer, one independent checker, total CPU budget 30s."""
from pathlib import Path
from datetime import datetime, timezone
import subprocess
import resource
import time
import json
import sys

BASE = Path(__file__).resolve().parent


def cpu_children():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime


def main():
    start_cpu = time.process_time()
    start_child_cpu = cpu_children()
    start_wall = time.monotonic()
    phases = []
    status = "PASS"
    for name in ("generate_q4_once.py","verify_literal_once.py"):
        before = cpu_children()
        result = subprocess.run([sys.executable,str(BASE/name)],cwd=BASE,
                                text=True,capture_output=True,timeout=30)
        phases.append({"script":name,"exit_code":result.returncode,
                       "actual_child_CPU_seconds":cpu_children()-before})
        (BASE/(name+".stdout")).write_text(result.stdout)
        (BASE/(name+".stderr")).write_text(result.stderr)
        print(result.stdout,end="")
        if result.returncode != 0:
            status = "FAIL"
            break
    total_cpu = cpu_children()-start_child_cpu+time.process_time()-start_cpu
    assert total_cpu < 30
    terminal = {"status":status,"terminal":True,
        "finished_utc":datetime.now(timezone.utc).isoformat(),"phases":phases,
        "actual_total_CPU_seconds":total_cpu,"wall_seconds":time.monotonic()-start_wall,
        "CPU_budget_seconds":30,"workers":1,
        "source_graphs_generated":1,"final_graphs_generated":1,
        "old_D2_graphs_regenerated":0,"old_D2_BFS_roots":0,
        "source_q4_BFS_roots":0,"final_q4_BFS_roots":22,
        "solver_calls":0,"Lean_runs":0,"continuation_scheduled":False,
        "scope":"one classical calibration; inherited odd-q obstruction only"}
    (BASE/"TERMINAL.json").write_text(json.dumps(terminal,indent=2)+"\n")
    print(json.dumps(terminal))
    assert status == "PASS"


if __name__ == "__main__":
    main()
