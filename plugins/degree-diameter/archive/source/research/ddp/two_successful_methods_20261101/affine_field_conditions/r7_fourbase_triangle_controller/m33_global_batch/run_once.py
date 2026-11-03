"""One compile and one bounded global batch; no automatic retry."""
import json
from pathlib import Path
import resource
import subprocess
from time import process_time,perf_counter

root=Path(__file__).resolve().parent
assert not (root/'RESULT.json').exists(),'This one-shot batch already has a result.'
start=process_time();wall=perf_counter();receipts=[]
def child_run(name,args,limit=None):
    before=resource.getrusage(resource.RUSAGE_CHILDREN);t=perf_counter()
    def cap():
        seconds=max(1,int(limit));resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
    with (root/(name+'.stdout')).open('w')as out,(root/(name+'.stderr')).open('w')as err:
        try:
            r=subprocess.run(args,cwd=root,stdout=out,stderr=err,preexec_fn=cap if limit else None,timeout=60)
            code=r.returncode
        except subprocess.TimeoutExpired:code='wall_timeout'
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    receipts.append({'stage':name,'exit_code':code,'CPU_seconds':cpu,'wall_seconds':perf_counter()-t})
    return code
code=child_run('compile',['g++','-O3','-std=c++17','search.cpp','-o','search'])
if code==0:
    used=sum(r['CPU_seconds']for r in receipts)+process_time()-start
    remaining=30-used
    assert remaining>1
    code=child_run('batch',['./search',str(remaining-0.5)],remaining)
    if code==0:result=json.loads((root/'batch.stdout').read_text())
    else:result={'status':'UNKNOWN_PROCESS_STOP','found':False,'family_exclusion':False,'search_complete':False}
else:result={'status':'COMPILE_FAILED','found':False,'family_exclusion':False,'search_complete':False}
result.update({'receipts':receipts,'wrapper_CPU_seconds':process_time()-start,
               'accounted_CPU_seconds':sum(r['CPU_seconds']for r in receipts)+process_time()-start,
               'wall_seconds':perf_counter()-wall,'CPU_budget_seconds':30,'workers':1,
               'running':False,'active_processes':[]})
if (root/'ATTEMPTS.bin').exists():
    actual=(root/'ATTEMPTS.bin').stat().st_size
    result['actual_attempt_file_bytes']=actual
    if code==0:assert actual==result['recorded_attempt_bytes']
(root/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
