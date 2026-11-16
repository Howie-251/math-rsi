"""Two bounded runtime/import diagnostics, never compile the research module."""
from pathlib import Path
import json
import os
import resource
import subprocess
import time

P = Path(__file__).resolve().parent
AR = next(p for p in P.parents if p.name=='ar4math')
LEAN = AR/'.tools/lean-4.24.0-linux/bin/lean'
lp = json.loads((AR/'research/ddp/expert15_20261114/d5_resume_20261115/d12_n42403/formal/BUILD_ATTEMPT_2.json').read_text())['LEAN_PATH']
results = []
for name, source, seconds in [('Init', '#check Nat\nexample (n : Nat) : n = n := rfl\n', 12),
                               ('RingImport', 'import Mathlib.Tactic.Ring\n#check CommRing\n', 60)]:
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(3,3))
        resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    try:
        run = subprocess.run([str(LEAN),'-j1','--stdin'],input=source,text=True,
                             capture_output=True,cwd=AR/'formal',timeout=seconds,
                             preexec_fn=limits,env={**os.environ,'LEAN_PATH':lp})
        result = dict(stage=name,exit_code=run.returncode,stdout=run.stdout,stderr=run.stderr,
                      status='PASS' if run.returncode==0 else 'FAILED')
    except subprocess.TimeoutExpired as exc:
        result = dict(stage=name,status='TIMEOUT',stdout=str(exc.stdout or ''),stderr=str(exc.stderr or ''))
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result.update(child_CPU=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                  wall=time.monotonic()-start,CPU_cap=3,wall_cap=seconds)
    results.append(result)
    (P/'IMPORT_DIAGNOSTIC.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    if result['status']!='PASS':
        break
