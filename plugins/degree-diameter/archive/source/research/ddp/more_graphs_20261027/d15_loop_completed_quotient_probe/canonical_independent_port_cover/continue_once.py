from pathlib import Path
from datetime import datetime,timezone
import json,time,resource,subprocess
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[4];CAD=ROOT/'.tools/lean-4.24.0-linux/bin/cadical';BASE=ROOT/'research/ddp/more_graphs_20261027'
start=time.process_time();r=resource.getrusage(resource.RUSAGE_CHILDREN);c0=r.ru_utime+r.ru_stime
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime-c0
pred0=json.loads((OUT/'PREDICTION.json').read_text());old=json.loads((OUT/'RESULT.json').read_text());assert all(x['status']=='UNKNOWN' for x in old['sources'])
pred={'timestamp_UTC':datetime.now(timezone.utc).isoformat(),'status':'ONE_BOUNDED_BUDGET_REASSESSMENT','reason':'Full canonical independent-pin question is directly derived from recoveredlinear charts. The symmetry-preserving domain is definitivelyUNSAT; independent domain removes that unnecessary restriction but original3s returnedUNKNOWN. A single adequate-budget solve tests whether symmetrybreaking yields a full graph; no new portorbits/model/seed is introduced.','unchanged_CNF':['model_15552.cnf','model_102060.cnf'],'solver_calls_per_source':1,'internal_time_seconds':25,'OS_CPU_soft_hard':[27,28],'aggregate_CPU_budget':60,'stop':'FirstSAT or bothcalls terminal. No automatic further timer renewal. Original3s output intact; UNKNOWN never exclusion.'}
(OUT/'CONTINUATION_PREDICTION.json').write_text(json.dumps(pred,indent=2)+'\n')
results=[]
for n in [15552,102060]:
 spec=next(x for x in pred0['sources'] if x['n']==n);cnf=OUT/f'model_{n}.cnf';assert cnf.exists()
 def limits():resource.setrlimit(resource.RLIMIT_CPU,(27,28));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
 before=cpu();wall=time.monotonic();stdout=OUT/f'continuation_{n}.stdout';stderr=OUT/f'continuation_{n}.stderr'
 with stdout.open('w') as so,stderr.open('w') as se:
  proc=subprocess.Popen([str(CAD),'-t','25',str(cnf)],stdout=so,stderr=se,preexec_fn=limits)
  (OUT/'CONTINUATION_HANDLE.json').write_text(json.dumps({'status':'RUNNING','n':n,'pid':proc.pid})+'\n');print(json.dumps({'status':'RUNNING','n':n,'pid':proc.pid}),flush=True)
  try:code=proc.wait(timeout=35)
  except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
 text=stdout.read_text();status='UNKNOWN';pins=[]
 if 's UNSATISFIABLE' in text:status='UNSAT_RESTRICTED_CANONICAL_INDEPENDENT_MODEL'
 elif 's SATISFIABLE' in text:
  pos=set()
  for l in text.splitlines():
   if l.startswith('v '):pos.update(v for v in map(int,l[2:].split()) if v>0)
  pins=sorted(v for g in spec['groups'] if g['variable'] in pos for v in g['pins']);assert 0<len(pins)==len(set(pins))<=15
  status='SAT_LITERAL_NEIGHBOR_SET_PENDING_CACHE_RECHECK'
  (OUT/f'HIT_{n}.json').write_text(json.dumps({'status':status,'source_n':n,'source_D':spec['D'],'target_n':n+1,'full_neighbor_set':pins,'new_graph_exported':False},indent=2)+'\n')
 result={'n':n,'D':spec['D'],'status':status,'return_code':code,'solver_CPU_seconds':cpu()-before,'wall_seconds':time.monotonic()-wall,'pins':pins};results.append(result);print(json.dumps(result),flush=True)
 if pins:break
res={'status':'TERMINAL_BOUNDED_CONTINUATION','sources':results,'aggregate_CPU_seconds':cpu()+time.process_time()-start,'pending_sources':[n for n in [15552,102060] if not any(r['n']==n for r in results)],'new_graphs':0,'new_balls':0,'source_BFS':0}
(OUT/'CONTINUATION_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');(OUT/'CONTINUATION_HANDLE.json').write_text(json.dumps({'status':'TERMINAL','pending':res['pending_sources']})+'\n');print(json.dumps(res),flush=True)
