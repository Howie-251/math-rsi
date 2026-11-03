"""Compile only. This preparation does not run the parameter gate."""
import json
from pathlib import Path
import resource
import subprocess
from time import process_time, perf_counter

root=Path(__file__).resolve().parent
start=process_time(); wall=perf_counter(); before=resource.getrusage(resource.RUSAGE_CHILDREN)
with (root/'compile.stdout').open('w') as out,(root/'compile.stderr').open('w') as err:
    run=subprocess.run(['g++','-O3','-std=c++17','gate.cpp','-o','gate'],cwd=root,stdout=out,stderr=err)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
child=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
symbolic=json.loads((root/'SYMBOLIC_IDENTITY_RESULT.json').read_text())['CPU_seconds']
prep=process_time()-start
result={'status':'PREPARED_WAITING_ROOT_PUBLIC77_GATE' if run.returncode==0 else 'COMPILE_FAILED',
        'compile_exit_code':run.returncode,'compile_CPU_seconds':child,'preparation_wrapper_CPU_seconds':prep,
        'symbolic_CPU_seconds':symbolic,'accounted_CPU_seconds':symbolic+child+prep,
        'wall_seconds':perf_counter()-wall,'CPU_budget_seconds':20,
        'parameter_gate_executed':False,'running':False,'active_processes':[]}
(root/'PREPARATION.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result));raise SystemExit(run.returncode)
