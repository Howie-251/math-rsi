"""Fresh single-worker r1 batch, cumulative 60 CPU seconds, no restart."""
from pathlib import Path
import json, math, os, resource, subprocess, time
HERE=Path(__file__).resolve().parent
prep=json.loads((HERE/'prepare.terminal.json').read_text())
assert prep['status']=='PREPARED_AND_PREFLIGHT_MATCHED'
assert not (HERE/'production.terminal.json').exists(), 'Do not restart completed or budget-limited processes'
assert prep['branch_counts_match_independent_r1_extension'] and prep['original_BB_inputs']==230496
prior=prep['cpu_seconds']; remaining=60-prior-1
assert remaining>0
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
      'preflight_is_not_prefix':True,'prior_CPU_seconds':prior,'process_CPU_limit_seconds':remaining,
      'cumulative_CPU_limit_seconds':60,'command':args},indent=2)+'\n')
    print(json.dumps({'pid':proc.pid,'remaining_CPU_seconds':remaining}),flush=True)
    code=proc.wait()
assert code==0,f'exit {code}; no automatic restart'
t=json.loads((HERE/'production.terminal.json').read_text())
summary={'status':t['status'],'parameter':{'q':7,'r':1,'c':3},
 'full_normalized_scope':28894320,'quotient_rejected_inputs':28663824,'quotient_pass_inputs':230496,
 'original_BB_evaluated':t['counts']['original_BB_evaluated'],'original_BB_pass':t['counts']['original_BB_pass'],
 'preparation_compile_preflight_CPU_seconds':prior,'production_driver_CPU_seconds':cpu()-start,
 'cumulative_CPU_seconds':prior+cpu()-start,'CPU_budget_seconds':60,
 'math_scope_computations_accounted_separately':True,'wall_seconds':time.monotonic()-wall,
 'worker_count':1,'restarts':0,'independent_best':'parent-owned; pending',
 'one_minBB_fallback_scored':t['one_minBB_fallback_scored'],
 'root_and_layer_statistics_population':'original BB survivors only; fallback separately labelled',
 'preflight_is_not_enumeration_prefix':True}
(HERE/'production.summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps({'status':summary['status'],'production_summary':summary,
 'production_terminal':'production.terminal.json'},indent=2)+'\n')
print(json.dumps(summary,indent=2));print(json.dumps(t['counts'],indent=2))
