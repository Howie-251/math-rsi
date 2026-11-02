"""Run p31 then p43 once, sharing a 60 CPU second budget; stop both on true D5."""
from pathlib import Path
import json, math, os, resource, subprocess, time
HERE=Path(__file__).resolve().parent
prep=json.loads((HERE/'profile.prepare.json').read_text())
assert not (HERE/'profiles.summary.json').exists(), 'No automatic restart'
prior=prep['CPU_seconds']
def cpu():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();wall=time.monotonic();completed=[]
for spec in prep['parameters']:
 folder=HERE.parent/spec['directory'];assert not (folder/'profile.terminal.json').exists()
 used=prior+cpu()-start;remaining=60-used-1
 if remaining<=0:break
 def cap():
  lim=max(1,math.ceil(remaining));resource.setrlimit(resource.RLIMIT_CPU,(lim,lim))
 args=[str(HERE/'profile'),str(folder),str(remaining)];before=cpu()
 with (folder/'profile.log').open('w') as out:
  proc=subprocess.Popen(args,stdout=out,stderr=subprocess.STDOUT,preexec_fn=cap)
  run={'status':'RUNNING','pid':proc.pid,'driver_pid':os.getpid(),'p':spec['p'],
       'worker_count':1,'shared_CPU_limit':60,'prior_cumulative_CPU_seconds':used,
       'process_CPU_budget':remaining,'planned_samples':spec['samples'],'command':args}
  (folder/'profile.run.json').write_text(json.dumps(run,indent=2)+'\n')
  print(json.dumps({'p':spec['p'],'pid':proc.pid,'remaining_CPU_seconds':remaining}),flush=True)
  code=proc.wait()
 assert code==0,f'process exit {code}; do not restart'
 term=json.loads((folder/'profile.terminal.json').read_text())
 run.update({'status':term['status'],'exit_code':code,'running':False,'next_cursor':term['next_cursor']})
 (folder/'profile.run.json').write_text(json.dumps(run,indent=2)+'\n')
 summary={'p':spec['p'],'status':term['status'],'scored_samples':term['next_cursor'],
  'parameter_driver_CPU_seconds':cpu()-before,'cumulative_shared_CPU_seconds':prior+cpu()-start,
  'scope':'authorized stratified sample only; not complete family enumeration',
  'full_family_exclusion_claimed':False,'BB_filtering_used':False,
  'independent_final':'parent-owned, pending; no independent preflight requested'}
 (folder/'terminal.json').write_text(json.dumps({'status':term['status'],'summary':summary,
    'details':'profile.terminal.json'},indent=2)+'\n')
 completed.append(summary)
 print(json.dumps({'parameter_complete':summary,'stats':term['stats']},indent=2),flush=True)
 if term['status']!='PROFILE_COMPLETE':break
result={'status':'BOTH_PROFILES_COMPLETE' if len(completed)==2 and all(c['status']=='PROFILE_COMPLETE' for c in completed) else 'STOPPED_WITH_SAVED_CURSOR_OR_CANDIDATE',
 'preparation_and_compile_CPU_seconds':prior,'profile_driver_CPU_seconds':cpu()-start,
 'cumulative_CPU_seconds':prior+cpu()-start,'wall_seconds':time.monotonic()-wall,
 'CPU_budget_seconds':60,'worker_count':1,'restarts':0,'parameters':completed,
 'independent_final_checks_accounted_separately':True}
(HERE/'profiles.summary.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
