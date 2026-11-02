"""The single authorized CaDiCaL call; never retries/reencodes."""
from pathlib import Path
import subprocess,sys,resource,time,json,datetime
resource.setrlimit(resource.RLIMIT_CPU,(10,75))
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[3];CADICAL=ROOT/'.tools/lean-4.24.0-linux/bin/cadical'
assert CADICAL.is_file()
START=time.monotonic();CSTART=time.process_time();DEADLINE=START+75

def child_cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime

def cap(n):
 def apply():resource.setrlimit(resource.RLIMIT_CPU,(n,n))
 return apply

def save(n,x):(OUT/n).write_text(json.dumps(x,indent=2)+'\n')
command=[str(CADICAL),'-t','60',str(OUT/'model.cnf')];c0=child_cpu();wall0=time.monotonic()
with (OUT/'cadical.log').open('w') as log:
 proc=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,preexec_fn=cap(65))
 save('RUN_HANDLE.json',{'status':'RUNNING_SINGLE_AUTHORIZED_SOLVER','PID':proc.pid,'command':command,'started_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'solver_calls_started':1,'solver_seconds_argument':60,'child_CPU_hard_seconds':65,'solver_wait_wall_guard_seconds':70,'whole_driver_wall_guard_seconds':75,'worker_count':1,'proof_logging':False})
 wallguard=False
 try:code=proc.wait(timeout=min(70,max(.1,DEADLINE-time.monotonic()-.2)))
 except subprocess.TimeoutExpired:wallguard=True;proc.kill();code=proc.wait()
solver_cpu=child_cpu()-c0;solver_wall=time.monotonic()-wall0;stdout=(OUT/'cadical.log').read_text();lines=stdout.splitlines();returned=[s for s in lines if s.startswith('s ')]
sat=code==10 and 's SATISFIABLE' in lines;unsat=code==20 and 's UNSATISFIABLE' in lines
r={'status':'RAW_UNSAT_UNPROVED_NO_GRAPH' if unsat else 'SOLVER_UNKNOWN_NO_WITNESS','solver_returned_status_lines':returned,'solver_exit_code':code,'solver_calls':1,'proof_logging':False,'mathematical_nonexistence_claim':False,'actual_n':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,'candidate_graphs':0,'positive_verified':False,'solver_CPU_seconds':solver_cpu,'solver_wall_seconds':solver_wall,'solver_wall_guard_triggered':wallguard,'source_global_D6_BFS':0,'source_radius4_cache_traversals':126,'matching_source_scope':'directprimaryLCF126+C7equivariantperfectmatching+girth>=6 only'}
if sat:
 r['status']='SAT_MODEL_AWAITING_LITERAL_CHECK';rem=DEADLINE-time.monotonic()-.2
 if rem>=.1:
  d0=child_cpu();decode0=time.monotonic()
  with (OUT/'decode.log').open('w') as log:
   try:decode=subprocess.run([sys.executable,str(OUT/'decode_model.py'),str(OUT/'cadical.log')],stdout=log,stderr=subprocess.STDOUT,preexec_fn=cap(10),timeout=min(10,rem));r['decode_exit_code']=decode.returncode
   except subprocess.TimeoutExpired:r['decode_exit_code']=None;r['decode_wall_guard_triggered']=True
  r['decode_CPU_seconds']=child_cpu()-d0;r['decode_wall_seconds']=time.monotonic()-decode0
  if r['decode_exit_code']==0:
   r['status']='SAT_LITERAL_D4_PRODUCER_PENDING_PARENT';r['candidate_graphs']=1;r['positive_verified']=True;r['actual_n']=126;r['actual_D']=4;r['actual_m']=252;r['actual_degree']=4;r['newroot_representative_R4_checks']=18;r['newgraph_all126_R4_BFS']=0;r['candidate_parameters']='CANDIDATE_PARAMETERS.json';r['candidate_edges']='candidate126.edges'
prep=json.loads((OUT/'PREPARATION_RESULT.json').read_text());cache=json.loads((OUT/'SOURCE_CACHE_RESULT.json').read_text())
r['execution_receipt']={'command':command,'PID':proc.pid,'completed':True,'solver_CPU_hard_seconds':65,'driver_CPU_soft_seconds':10,'driver_CPU_hard_seconds':75,'solver_wait_wall_seconds':70,'whole_driver_wall_seconds':75,'aggregate_budget_seconds':90,'prep_worker_CPU_seconds':prep['execution_receipt']['worker_process_CPU_seconds'],'prep_driver_CPU_seconds':prep['execution_receipt']['driver_CPU_seconds'],'source_cache_body_CPU_seconds':cache['CPU_seconds'],'solver_and_decoder_child_CPU_seconds':child_cpu()-c0,'driver_CPU_seconds':time.process_time()-CSTART,'actual_driver_wall_seconds':time.monotonic()-START,'historical_iso8CPU_separate':True,'workers':1,'live_handle':None}
r['execution_receipt']['measured_counted_CPU_seconds']=sum([r['execution_receipt'][k] for k in ['prep_worker_CPU_seconds','prep_driver_CPU_seconds','source_cache_body_CPU_seconds','solver_and_decoder_child_CPU_seconds','driver_CPU_seconds']])
for name in ['RESULT.json','terminal.json']:save(name,r)
save('RUN_HANDLE.json',{'status':'COMPLETE','PID':proc.pid,'solver_exit_code':code,'solver_status':r['status'],'solver_calls_started':1,'live_handle':None,'command':command,'solver_CPU_seconds':solver_cpu,'solver_wall_seconds':solver_wall})
print(json.dumps(r),flush=True)
