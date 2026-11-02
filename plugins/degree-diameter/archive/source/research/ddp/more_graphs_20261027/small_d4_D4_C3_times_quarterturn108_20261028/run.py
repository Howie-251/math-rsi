from pathlib import Path
import subprocess,resource,json,time
out=Path(__file__).resolve().parent;start=time.process_time();before=resource.getrusage(resource.RUSAGE_CHILDREN)
with (out/'worker.log').open('w') as log:
 try:r=subprocess.run(['python',str(out/'search.py')],stdout=log,stderr=subprocess.STDOUT,timeout=60);code=r.returncode
 except subprocess.TimeoutExpired:code='WALL_TIMEOUT'
after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
if code==0:result=json.loads((out/'WORKER_RESULT.json').read_text())
else:
 cases=(out/'CASES.jsonl').read_text().splitlines() if (out/'CASES.jsonl').exists() else [];result={'status':'UNKNOWN_AFTER_PROCESS_LIMIT','processed':len(cases),'untested':3066-len(cases),'hits':int((out/'HIT.json').exists()),'actual_global_D':None}
result.update({'receipt':{'exit_code':code,'worker_process_CPU_seconds':cpu,'driver_CPU_seconds':time.process_time()-start,'worker_CPU_hard_limit_seconds':14,'aggregate_CPU_budget_seconds':15,'compile_CPU_seconds':0,'workers':1},'live_handle':None});(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(out/'terminal.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
