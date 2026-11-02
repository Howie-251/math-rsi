"""One bounded gate run, only after root supplies the actual public gate path."""
import json
from pathlib import Path
import resource
import subprocess
import sys
from time import process_time, perf_counter

root=Path(__file__).resolve().parent
assert len(sys.argv)==2, 'Pass the actual root-cleared public degree77 gate document.'
public=Path(sys.argv[1]).resolve()
assert public.is_file()
assert not (root/'RESULT.json').exists(), 'This single-run batch already has a result.'
prep=json.loads((root/'PREPARATION.json').read_text())
assert prep['compile_exit_code']==0
remaining=20-prep['accounted_CPU_seconds']
assert remaining>0.5
def limit():
    hard=max(1,int(remaining))
    resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))
start=process_time();wall=perf_counter();before=resource.getrusage(resource.RUSAGE_CHILDREN)
try:
    with (root/'gate.stdout').open('w') as out,(root/'gate.stderr').open('w') as err:
        run=subprocess.run(['./gate',str(remaining-0.25)],cwd=root,stdout=out,stderr=err,
                           preexec_fn=limit,timeout=30)
    exit_code=run.returncode
except subprocess.TimeoutExpired:
    exit_code='wall_timeout'
after=resource.getrusage(resource.RUSAGE_CHILDREN)
child=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
wrapper=process_time()-start
if exit_code==0:
    result=json.loads((root/'gate.stdout').read_text())
else:
    result={'status':'UNKNOWN_GATE_PROCESS_STOP','search_complete':False,'found':False}
result.update({'exit_code':exit_code,'public_gate_document':str(public),
               'preparation_CPU_seconds':prep['accounted_CPU_seconds'],
               'gate_process_CPU_seconds':child,'run_wrapper_CPU_seconds':wrapper,
               'accounted_CPU_seconds':prep['accounted_CPU_seconds']+child+wrapper,
               'run_wall_seconds':perf_counter()-wall,'CPU_budget_seconds':20,
               'workers':1,'running':False,'active_processes':[]})
(root/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
