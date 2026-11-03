from pathlib import Path
import json,os,resource,subprocess,time
out=Path(__file__).resolve().parent
assert not (out/'run.json').exists(),'One fixed-source production; no automatic restart.'
def cpu():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();wall=time.monotonic()
with (out/'compile.log').open('w') as f:
 subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=out,stdout=f,stderr=subprocess.STDOUT,check=True)
prep=cpu()-start;remaining=180-prep-1
assert remaining>0
metadata={'source':'../best.edges','source_verified_n':172,'degree':7,'target_D':3,
 'source_bad_pairs':258,'maximum_complete_rounds':30,'fixed_start_count':1,
 'moves':'choose two disjoint edges; replace by either perfect matching of their four endpoints if both added edges are absent',
 'scoring':'exact all172root radius3 bitset unions; partial ordered deficit >=2*strictbound safely prunes nonimprovements',
 'symmetry_assumed':False,'calibration':'first actual legal candidate exact score compared with ordinary full172root BFS once',
 'CPU_budget_seconds':180,'preparation_CPU_seconds':prep,'production_CPU_limit_seconds':remaining,'worker_count':1}
(out/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
with (out/'production.log').open('w') as f:
 process=subprocess.Popen([str(out/'search'),str(out),str(out.parent/'best.edges'),str(remaining)],stdout=f,stderr=subprocess.STDOUT)
 run={'running':True,'status':'RUNNING','pid':process.pid,'driver_pid':os.getpid(),'worker_count':1,'CPU_budget_seconds':180,'preparation_CPU_seconds':prep}
 (out/'run.json').write_text(json.dumps(run,indent=2)+'\n')
 code=process.wait()
run.update(running=False,exit_code=code,total_recorded_CPU_seconds=cpu()-start,wall_seconds=time.monotonic()-wall)
if code==0:
 terminal=json.loads((out/'terminal.json').read_text());run['status']=terminal['status']
else:run['status']='PROCESS_ERROR'
(out/'run.json').write_text(json.dumps(run,indent=2)+'\n')
print(json.dumps(run,indent=2))
