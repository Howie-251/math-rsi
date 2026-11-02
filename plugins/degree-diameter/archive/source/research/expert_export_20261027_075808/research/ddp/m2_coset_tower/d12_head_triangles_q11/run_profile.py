from pathlib import Path
import json, math, os, resource, subprocess, time
HERE=Path(__file__).resolve().parent
prep=json.loads((HERE/'prepare.terminal.json').read_text())
assert prep['status']=='PREPARED' and not (HERE/'profile.terminal.json').exists()
prior=prep['CPU_seconds'];remaining=60-prior-1
assert remaining>0
def cpu():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
def cap():
 lim=math.ceil(remaining);resource.setrlimit(resource.RLIMIT_CPU,(lim,lim))
start=cpu();wall=time.monotonic();args=[str(HERE/'profile'),str(HERE),str(remaining)]
with (HERE/'profile.log').open('w') as out:
 proc=subprocess.Popen(args,stdout=out,stderr=subprocess.STDOUT,preexec_fn=cap)
 run={'status':'RUNNING','pid':proc.pid,'driver_pid':os.getpid(),'worker_count':1,
      'planned_cells':192,'one_sample_per_cell':True,'prior_CPU_seconds':prior,
      'process_CPU_budget_seconds':remaining,'cumulative_CPU_budget_seconds':60,'command':args}
 (HERE/'profile.run.json').write_text(json.dumps(run,indent=2)+'\n')
 print(json.dumps(run),flush=True);code=proc.wait()
assert code==0,f'exit {code}; no automatic restart'
t=json.loads((HERE/'profile.terminal.json').read_text());run.update({'status':t['status'],'running':False,'exit_code':0,'next_cell_id':t['next_cell_id']});(HERE/'profile.run.json').write_text(json.dumps(run,indent=2)+'\n')
summary={'status':t['status'],'actual_cells_scored':t['next_cell_id'],'planned_cells':192,
 'scope':'one sample per approved HH color cell; no complete family exclusion',
 'preparation_compile_CPU_seconds':prior,'profile_driver_CPU_seconds':cpu()-start,
 'cumulative_CPU_seconds':prior+cpu()-start,'CPU_limit_seconds':60,'wall_seconds':time.monotonic()-wall,
 'worker_count':1,'restarts':0,'all_samples_three_complete_BFS':True,'no_BB_filter':True,
 'independent_final':'parent-owned, pending for exactly one final saved best graph',
 'independent_final_CPU_accounted_separately':True}
(HERE/'terminal.json').write_text(json.dumps({'status':t['status'],'summary':summary,'details':'profile.terminal.json'},indent=2)+'\n')
print(json.dumps(summary,indent=2));print(json.dumps(t['stats'],indent=2))
