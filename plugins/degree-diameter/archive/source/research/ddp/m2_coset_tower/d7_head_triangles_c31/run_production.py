from pathlib import Path
import json, math, os, resource, subprocess, time
HERE=Path(__file__).resolve().parent
prep=json.loads((HERE/'production.prepare.json').read_text())
assert prep['status']=='READY' and prep['actual_scope']==18829360
assert not (HERE/'production.terminal.json').exists(), 'No automatic restart'
prior=2.805399+prep['preparation_compile_calibration_CPU_seconds'];remaining=360-prior-1
assert remaining>0
def cpu():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
def cap():
 lim=math.ceil(remaining);resource.setrlimit(resource.RLIMIT_CPU,(lim,lim))
start=cpu();wall=time.monotonic();args=[str(HERE/'production'),'run',str(HERE),str(remaining)]
with (HERE/'production.log').open('w') as out:
 proc=subprocess.Popen(args,stdout=out,stderr=subprocess.STDOUT,preexec_fn=cap)
 run={'status':'RUNNING','pid':proc.pid,'driver_pid':os.getpid(),'worker_count':1,
      'parent_marked_scope':35305050,'actual_safe16_scope':18829360,'new_cursor':0,
      'profile_is_not_prefix':True,'prior_CPU_seconds':prior,'process_CPU_budget_seconds':remaining,
      'cumulative_CPU_budget_seconds':360,'command':args}
 (HERE/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
 print(json.dumps(run),flush=True)
 code=proc.wait()
assert code==0,f'process exit {code}; do not restart automatically'
t=json.loads((HERE/'production.terminal.json').read_text())
run.update({'status':t['status'],'exit_code':code,'running':False,'next_cursor':t['next_cursor']})
(HERE/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
summary={'status':t['status'],'parent_marked_scope':35305050,'safe_16_anchor_scope':18829360,
 'actual_HH_inputs_checked':t['counts']['HH_legal_inputs_checked'],'BB_pass':t['counts']['BB_pass'],
 'prior_shared_profiles_CPU_seconds':2.805399,'new_preparation_CPU_seconds':prep['preparation_compile_calibration_CPU_seconds'],
 'production_driver_CPU_seconds':cpu()-start,'cumulative_CPU_seconds':prior+cpu()-start,
 'CPU_budget_seconds':360,'independent_final_CPU_accounted_separately':True,
 'wall_seconds':time.monotonic()-wall,'worker_count':1,'restarts':0,
 'independent_final':'parent-owned; pending for only this final production graph',
 'profile_was_not_prefix':True,'root_statistics_population':'BB survivors only',
 'one_minBB_fallback_scored':t['one_minBB_fallback_scored']}
(HERE/'production.summary.json').write_text(json.dumps(summary,indent=2)+'\n')
profile=json.loads((HERE/'terminal.json').read_text())
(HERE/'terminal.json').write_text(json.dumps({'status':t['status'],'profile_history':profile,
 'production_summary':summary,'details':'production.terminal.json'},indent=2)+'\n')
print(json.dumps(summary,indent=2));print(json.dumps(t['counts'],indent=2))
