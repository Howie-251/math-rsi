"""One longer cold-start certificate attempt after the ten-second cost profile.
Uses the same freshly generated S_TOUCH base; binary LRAT reduces output volume.
No learned solver state is imported. A non-UNSAT trace is only partial output.
"""
from pathlib import Path
import json
import os
import resource
import subprocess
import time

root=Path(__file__).resolve().parents[3]
base=root/"computations/dd82/n62/s_touch_certificate_profile"
out=root/"computations/dd82/n62/s_touch_binary_120s"
out.mkdir(exist_ok=True)
os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
cnf=base/"cnf/S_TOUCH.cnf"
proof=out/"S_TOUCH.lrat"
cmd=[str(root/".tools/lean-4.24.0-linux/bin/cadical"),"--lrat","-t","120",str(cnf),str(proof)]
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(140,141))
    resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE,(512*1024**2,512*1024**2))
started=time.monotonic()
with (out/"solver.log").open("w") as log:
    try:
        p=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,timeout=150,preexec_fn=limits)
        code=p.returncode
        status={10:"SAT_CANDIDATE",20:"RAW_UNSAT_WITH_UNCHECKED_LRAT",0:"UNKNOWN"}.get(code,"PROCESS_FAILURE")
    except subprocess.TimeoutExpired:
        code,status=None,"OUTER_WALL_TIMEOUT"
report=dict(status=status,exit_code=code,seconds=time.monotonic()-started,cpu_count=1,
    solver_wall_budget_seconds=120,outer_wall_limit_seconds=150,proof_format="binary LRAT",
    memory_limit_bytes=4*1024**3,output_file_limit_bytes=512*1024**2,
    proof_bytes=proof.stat().st_size if proof.exists() else 0,source_cnf=str(cnf),
    cold_start=True,learned_state_imported=False,proof_checked=False,lean_graph_bridge=False,
    rationale="One explicitly longer run justified by measured ten-second cost; not a mass historical queue rerun",command=cmd)
(out/"result.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))

