"""One authorized production process, starting at a new enumeration cursor zero."""
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time
HERE=Path(__file__).resolve().parent
profile=json.loads((HERE/'terminal.json').read_text())
prepared=json.loads((HERE/'production.prepare.json').read_text())
assert profile['status']=='PROFILE_COMPLETE'
assert not (HERE/'production.terminal.json').exists(), 'Never restart a completed or budget-stopped production.'
assert json.loads((HERE/'production.BB_calibration.json').read_text())['exact_mask_matches']==1200
prior=profile['cumulative_including_independent_CPU_seconds']+prepared['cpu_seconds']
remaining=360-prior-1
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
def cap():
    n=max(1,math.ceil(remaining));resource.setrlimit(resource.RLIMIT_CPU,(n,n))
start=cpu();wall=time.monotonic();args=[str(HERE/'production'),'run',str(remaining),str(HERE)]
with (HERE/'production.log').open('w') as output:
    proc=subprocess.Popen(args,stdout=output,stderr=subprocess.STDOUT,preexec_fn=cap)
    (HERE/'production.run.json').write_text(json.dumps({'status':'RUNNING','pid':proc.pid,'driver_pid':os.getpid(),
      'worker_count':1,'scope_total':76384728,'start_cursor':0,'profile_is_not_prefix':True,
      'prior_CPU_seconds':prior,'process_CPU_limit_seconds':remaining,'cumulative_CPU_limit_seconds':360,
      'command':args},indent=2)+'\n')
    code=proc.wait()
assert code==0,f'production process exited {code}; no restart'
terminal=json.loads((HERE/'production.terminal.json').read_text())
# The reused profile writer labels a branch by cursor//200. Production has
# different contiguous branch/anchor intervals; correct only that display label.
metadata=json.loads((HERE/'production.metadata.json').read_text())
best=json.loads((HERE/'production.best.json').read_text())
branch=next(x for x in metadata['branches'] if x['cursor_start']<=best['cursor']<x['cursor_end'])
anchor=next(x for x in metadata['anchors'] if x['cursor_start']<=best['cursor']<x['cursor_end'])
old_label=best['branch']
best.update(branch=branch['branch'],anchor_id=anchor['anchor_id'],anchor_index=anchor['anchor_index'])
best['output_label_correction']={'former_profile_branch_label':old_label,
 'method':'Exact production.metadata cursor intervals; no graph or score change.'}
(HERE/'production.best.json').write_text(json.dumps(best,indent=2)+'\n')
summary={'status':terminal['status'],'prior_CPU_seconds':prior,
 'profile_and_independent_CPU_seconds':profile['cumulative_including_independent_CPU_seconds'],
 'new_preparation_compile_CPU_seconds':prepared['cpu_seconds'],
 'production_driver_CPU_seconds':cpu()-start,'cumulative_CPU_seconds':prior+cpu()-start,
 'wall_seconds':time.monotonic()-wall,'worker_count':1,'scope_total':76384728,
 'processed':terminal['next_cursor'],'statistics_population':'root/layer metrics cover BB survivors only',
 'independent_best':'parent-owned; pending','production_terminal':'production.terminal.json',
 'random_profile_is_not_prefix':True,'restarts':0}
(HERE/'production.summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps({'status':summary['status'],'profile':profile,
 'production_summary':summary,'production_terminal':'production.terminal.json'},indent=2)+'\n')
print(json.dumps(summary,indent=2))
print(json.dumps(terminal['counts'],indent=2))
