"""One bounded profile of the recovered S_TOUCH base, with LRAT output.
Run from the ar4math root. This is not a formal graph exclusion.
"""
import importlib.util
import json
import os
from pathlib import Path
import resource
import subprocess
import time

root = Path(__file__).resolve().parents[3]
archive = root / "context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929"
out = root / "computations/dd82/n62/s_touch_certificate_profile"
out.mkdir(parents=True, exist_ok=True)
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
spec = importlib.util.spec_from_file_location("archived_n62_ab", archive / "code/n62/n62_ab_cnf.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
data = module.load_manifest(archive / "theory/n62/n62_root_templates.json")
template = next(t for t in data["templates"] if t["id"] == "S_TOUCH")
started = time.monotonic()
record = module.generate_case(template, out, write_cnf=True)
generation_seconds = time.monotonic() - started
cnf = out / record["cnf"]
proof = out / "S_TOUCH.lrat"
cmd = [str(root / ".tools/lean-4.24.0-linux/bin/cadical"), "--lrat", "--no-binary", "-t", "10", str(cnf), str(proof)]
def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (20, 21))
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (256 * 1024**2, 256 * 1024**2))
started = time.monotonic()
with (out / "solver.log").open("w") as log:
    try:
        result = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT, timeout=25, preexec_fn=limits)
        exit_code = result.returncode
        status = {10:"SAT_CANDIDATE", 20:"RAW_UNSAT_WITH_UNCHECKED_LRAT", 0:"UNKNOWN"}.get(exit_code, "PROCESS_FAILURE")
    except subprocess.TimeoutExpired:
        exit_code, status = None, "WALL_TIMEOUT"
report = dict(case="S_TOUCH", purpose="Profile fresh proof output for one recovered base; no historical equality or graph nonexistence claimed",
              cpu_affinity_count=1, solver_wall_budget_seconds=10, outer_wall_limit_seconds=25,
              generation_seconds=generation_seconds, solver_seconds=time.monotonic()-started,
              variables=record["variables"], clauses=record["clauses"], cnf_bytes=cnf.stat().st_size,
              proof_bytes=proof.stat().st_size if proof.exists() else 0,
              exit_code=exit_code, status=status, proof_checked=False, lean_bridge=False,
              command=cmd)
(out / "profile.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))

