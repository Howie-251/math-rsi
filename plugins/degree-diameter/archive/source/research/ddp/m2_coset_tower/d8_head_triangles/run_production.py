"""One exact original-BB batch after the completed quotient filter."""
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time
HERE=Path(__file__).resolve().parent
profile=json.loads((HERE/'terminal.json').read_text());prep=json.loads((HERE/'production.prepare.json').read_text())
assert profile['status']=='PROFILE_COMPLETE'
assert not (HERE/'production.terminal.json').exists(),'Do not restart a completed or budget-limited process.'
assert prep['actual_counts_match_independent_lift_file'] and prep['original_BB_inputs']==230496
prior=profile['cumulative_including_independent_CPU_seconds']+prep['cpu_seconds'];remaining=180-prior-1
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
def cap():
    n=max(1,math.ceil(remaining));resource.setrlimit(resource.RLIMIT_CPU,(n,n))
start=cpu();wall=time.monotonic();args=[str(HERE/'production'),'run',str(remaining),str(HERE)]
with (HERE/'production.log').open('w') as out:
    proc=subprocess.Popen(args,stdout=out,stderr=subprocess.STDOUT,preexec_fn=cap)
    (HERE/'production.run.json').write_text(json.dumps({'status':'RUNNING','pid':proc.pid,'driver_pid':os.getpid(),
      'worker_count':1,'full_scope':28894320,'original_BB_scope':230496,'start_filtered_cursor':0,
      'profile_is_not_prefix':True,'prior_CPU_seconds':prior,'process_CPU_limit_seconds':remaining,
      'cumulative_CPU_limit_seconds':180,'command':args},indent=2)+'\n')
    code=proc.wait()
assert code==0,f'exit {code}; no automatic restart'
t=json.loads((HERE/'production.terminal.json').read_text())
summary={'status':t['status'],'full_normalized_scope':28894320,
 'quotient_rejected_inputs':28663824,'quotient_pass_inputs':230496,
 'original_BB_evaluated':t['counts']['original_BB_evaluated'],
 'original_BB_pass':t['counts']['original_BB_pass'],
 'prior_CPU_seconds':prior,'new_preparation_compile_CPU_seconds':prep['cpu_seconds'],
 'production_driver_CPU_seconds':cpu()-start,'cumulative_CPU_seconds':prior+cpu()-start,
 'math_scope_computations_accounted_separately':True,'wall_seconds':time.monotonic()-wall,
 'worker_count':1,'restarts':0,'independent_best':'parent-owned; pending',
 'one_minBB_fallback_scored':t['one_minBB_fallback_scored'],
 'root_and_layer_statistics_population':'original BB survivors only; fallback separately labelled',
 'random_profile_is_not_prefix':True}
(HERE/'production.summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps({'status':summary['status'],'profile':profile,
 'production_summary':summary,'production_terminal':'production.terminal.json'},indent=2)+'\n')
print(json.dumps(summary,indent=2));print(json.dumps(t['counts'],indent=2))
