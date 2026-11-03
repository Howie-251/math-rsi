from pathlib import Path
import json,math,os,re,resource,subprocess,time
D=Path(__file__).resolve().parent;os.chdir(D);prior=64.297950855;prep=.5;cap=100.;start=time.process_time();wall=time.time();charges=[];calls=0;sourceparse=0;newbfs=0
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
cadical=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math/.tools/lean-4.24.0-linux/bin/cadical')
def save(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
def used():return prior+prep+sum(c['CPU'] for c in charges)+time.process_time()-start
def child(argv,log,cpulimit,walllimit,phase):
 before=resource.getrusage(resource.RUSAGE_CHILDREN)
 def bound():resource.setrlimit(resource.RLIMIT_CPU,(max(1,int(cpulimit)),max(2,int(cpulimit)+1)))
 with (D/log).open('w') as out:
  p=subprocess.Popen(argv,stdout=out,stderr=subprocess.STDOUT,preexec_fn=bound)
  save('DRIVER_HANDLE.json',{'phase':phase,'pid':p.pid,'argv':argv,'start_UTC':time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime()),'prior_CPU':prior,'newprep':prep,'casecap':cap})
  killed=False
  try:rc=p.wait(timeout=walllimit)
  except subprocess.TimeoutExpired:p.kill();rc=p.wait();killed=True
 after=resource.getrusage(resource.RUSAGE_CHILDREN);charges.append({'phase':phase,'CPU':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,'exit':rc,'wall_hard_killed':killed});return rc
status='UNKNOWN_PREPARATION';native_time=None;native_rc=None
try:
 assert cadical.is_file() and os.access(cadical,os.X_OK)
 rc=child(['python',str(D/'run_assignment_once.py')],'ASSIGNMENT_STDOUT.log',9,18,'ONLY_HIGHS_ASSIGNMENT_WINDOW_5SEC')
 if rc:raise RuntimeError('ASSIGNMENT_EXECUTION_FAILURE')
 assignment=json.loads((D/'ASSIGNMENT_RESULT.json').read_text())
 if not assignment['eligible']:status='UNKNOWN_STOP_NO_ELIGIBLE_ASSIGNMENT'
 else:
  rc=child(['python',str(D/'build_shift_once.py')],'BUILD_SHIFT.log',4,10,'BUILD_FIXED_SIGMA_EXACT_SHIFT_CNF')
  if rc:raise RuntimeError('SHIFT_BUILD_FAILURE')
  # Reserve actual positive binding and allroot suite; unused budget never authorizes a second window.
  native_time=min(20,int(math.floor(cap-used()-8)))
  if native_time<1:status='UNKNOWN_BLOCKED_BY_CASE_BUDGET_NO_SAT_START'
  else:
   calls=1;native_rc=child([str(cadical),'-t',str(native_time),str(D/'FIXED_SIGMA_SHIFT.cnf')],'SAT_STDOUT.log',native_time+2,native_time+10,'ONLY_FIXED_SIGMA_SHIFT_CADICAL_WINDOW')
   stdout=(D/'SAT_STDOUT.log').read_text(errors='replace');lines=[l for l in stdout.splitlines() if l.startswith('s ')];stats={}
   for k in ['conflicts','decisions','propagations','restarts']:
    h=re.findall(r'^c\s+'+k+r':\s*([0-9,]+)',stdout,re.M);stats[k]=int(h[-1].replace(',','')) if h else None
   save('NATIVE_EXECUTION.json',{'argv':[str(cadical),'-t',str(native_time),str(D/'FIXED_SIGMA_SHIFT.cnf')],'return_code':native_rc,'status_lines':lines,'statistics':stats,'raw_comment_UNKNOWN':'c UNKNOWN' in stdout,'proof_logged':False,'proof_checked':False,'solver_calls':1})
   if native_rc==10 and 's SATISFIABLE' in lines:
    from positive_candidate import produce
    produce(stdout);sourceparse=1
    remain=cap-used()-1
    if remain<1:raise RuntimeError('NO_POSITIVE_BFS_BUDGET')
    rc=child([str(D.parent/'build_model'),str(max(.1,remain-1)),'--verify',str(D/'candidate1368.edges')],'CANDIDATE_BFS.log',remain,20,'POSITIVE_CANDIDATE_ALL1368_ROOTS')
    if rc:raise RuntimeError('POSITIVE_CANDIDATE_BFS_FAILURE')
    newbfs=1368;status='FOUND1368_PENDING_FRESH_ACCEPTANCE'
   elif native_rc==20 and 's UNSATISFIABLE' in lines:status='RAW_UNSAT_ONLY_FROZEN_SIGMA_UNCHECKED_NOT_K19_NO'
   else:status='UNKNOWN_SINGLE_FIXED_SIGMA_SHIFT_WINDOW'
except Exception as e:status='UNKNOWN_EXECUTION_OR_BINDING_FAILURE';save('EXECUTION_ERROR.json',{'error':str(e),'charges':charges,'CPU_sofar':used()})
finally:
 r={'status':status,'terminal':True,'prior_case_CPU':prior,'newprep':prep,'charges':charges,'parent_actual_CPU':time.process_time()-start,'cumulative_case_CPU':used(),'CPU_cap':cap,'assignment_HiGHS_windows':1,'fixed_sigma_SAT_windows':calls,'configured_SAT_seconds':native_time,'native_return_code':native_rc,'source_parse_count':sourceparse,'candidate_BFS_roots':newbfs,'old_DP_sourceD4_BFS_field_Lean_paid_runs':0,'new_graph_parameter_Lean':[0,0,0],'full_K19_family_verdict':'UNKNOWN_NOT_EXCLUDED','original_full60window_repeated':False,'second_sigma_or_seed':False,'automatic_continuation':False}
 for file,key in [('ASSIGNMENT_RESULT.json','assignment'),('SHIFT_MODEL_RESULT.json','shiftmodel'),('NATIVE_EXECUTION.json','native')]:
  if (D/file).exists():r[key]=json.loads((D/file).read_text())
 save('RESULT.json',r);save('TERMINAL.json',{'status':status,'terminal':True,'cumulative_case_CPU':r['cumulative_case_CPU'],'CPU_cap':cap,'SAT_calls':calls,'native_return_code':native_rc,'full_K19_family_verdict':'UNKNOWN_NOT_EXCLUDED','wall_seconds':time.time()-wall,'stop':True});print(json.dumps(r,indent=2),flush=True)
