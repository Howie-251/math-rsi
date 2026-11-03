from pathlib import Path
import array,collections,json,os,re,resource,subprocess,time
D=Path(__file__).resolve().parent;ROOT=D.parents[6];os.chdir(D)
# The path is the previously used native binary; this is a metadata check, no API probe.
cadical=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math/.tools/lean-4.24.0-linux/bin/cadical')
prior=1.0;prep=1.0;cap=100.;start=time.process_time();wall=time.time();charges=[];native_rc=None
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
def write(name,obj):(D/name).write_text(json.dumps(obj,indent=2)+'\n')
def used():return prior+prep+sum(z['CPU'] for z in charges)+time.process_time()-start
def child(argv,log,cpulimit,walllimit,phase):
 before=resource.getrusage(resource.RUSAGE_CHILDREN)
 def bound():resource.setrlimit(resource.RLIMIT_CPU,(max(1,int(cpulimit)),max(2,int(cpulimit)+1)))
 with (D/log).open('w') as out:
  p=subprocess.Popen(argv,stdout=out,stderr=subprocess.STDOUT,preexec_fn=bound)
  write('DRIVER_HANDLE.json',{'phase':phase,'pid':p.pid,'argv':argv,'start_UTC':time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime()),'case_CPU_cap':cap,'prior_readgate_CPU':prior,'new_prep_charge':prep,'solver_calls_authorized':1})
  killed=False
  try:rc=p.wait(timeout=walllimit)
  except subprocess.TimeoutExpired:p.kill();rc=p.wait();killed=True
 after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
 charges.append({'phase':phase,'CPU':cpu,'exit':rc,'wall_hard_killed':killed,'argv':argv});return rc
status='UNKNOWN_PREPARATION';sat_calls=0;source_parses=0;newroot_bfs=0
try:
 if not(cadical.is_file() and os.access(cadical,os.X_OK)):raise RuntimeError('EXISTING_CADICAL_NOT_EXECUTABLE')
 rc=child(['python',str(D/'convert_cache.py')],'CONVERT.log',3,10,'CONVERT_OLD_CACHE_NO_DP')
 if rc:raise RuntimeError('CACHE_CONVERSION_FAILED')
 rc=child(['g++','-O2','-std=c++17',str(D/'build_model.cpp'),'-o',str(D/'build_model')],'COMPILE.log',5,15,'COMPILE')
 if rc:raise RuntimeError('COMPILE_FAILED')
 buildremaining=20-(used()-prior)
 rc=child([str(D/'build_model'),str(max(.1,buildremaining-1))],'BUILD.log',buildremaining,30,'BUILD_EXACT_POINT_CNF')
 if rc:raise RuntimeError('BUILD_FAILED_OR_BUDGET')
 build=json.loads((D/'BUILD_RESULT.json').read_text());assert build['clauses']==172800 and build['total_variables']==73800
 remaining=cap-used()-10
 if remaining<61:raise RuntimeError('INSUFFICIENT_REMAINING_CPU_FOR_SINGLE_WINDOW')
 sat_calls=1
 native_rc=child([str(cadical),'-t','60',str(D/'K19_EXACT_POINT.cnf')],'SAT_STDOUT.log',min(65,remaining),80,'ONLY_CADICAL_WINDOW')
 stdout=(D/'SAT_STDOUT.log').read_text(errors='replace')
 s_lines=[s for s in stdout.splitlines() if s.startswith('s ')]
 stat={}
 for key in ['conflicts','decisions','propagations','restarts']:
  hits=re.findall(r'^c\s+'+key+r':\s*([0-9,]+)',stdout,re.M)
  stat[key]=int(hits[-1].replace(',','')) if hits else None
 write('NATIVE_EXECUTION.json',{'argv':[str(cadical),'-t','60',str(D/'K19_EXACT_POINT.cnf')],'return_code':native_rc,'s_status_lines':s_lines,'statistics':stat,'solver_calls':1,'proof_logging':False,'proof_checked':False,'charges':charges})
 if native_rc==10 and any(s=='s SATISFIABLE' for s in s_lines):
  positives=set()
  for line in stdout.splitlines():
   if line.startswith('v '):
    for x in map(int,line[2:].split()):
     if 1<=x<=24624:positives.add(x)
  selected=[];sigma={};shifts={}
  for x in sorted(positives):
   r,s_t=divmod(x-1,36*19);s,t=divmod(s_t,19)
   if r in sigma:raise RuntimeError('SAT_ORIGINAL_ROW_NOT_EXACTLY_ONE')
   sigma[r]=s;shifts[r]=t;selected.append([r,s,t,x])
  assert set(sigma)==set(range(36)) and set(sigma.values())==set(range(36)) and len(selected)==36 and shifts[0]==0
  A=array.array('I');A.frombytes((D/'A_EXACT_LENGTH0_3.u32').read_bytes());MASK=(1<<19)-1
  def rot(a,t):return ((a<<t)|(a>>(19-t)))&MASK
  sums={}
  def sumset(a,b):
   if not a or not b:return 0
   key=(min(a,b),max(a,b))
   if key in sums:return sums[key]
   z=0
   while a:
    bit=a&-a;a-=bit;z|=rot(b,bit.bit_length()-1)
   sums[key]=z;return z
  cover=[]
  for i in range(36):
   for j in range(36):
    z=0
    for r in range(36):
     bmask=0;s=sigma[r]
     for a in range(4):
      for b in range(4-a):bmask|=sumset(A[(a*36+i)*36+r],A[(b*36+s)*36+j])
     z|=rot(bmask,shifts[r])
    if z!=MASK:raise RuntimeError('SAT_INDEPENDENT_ACTUAL_POINT_COVER_FAILURE')
    cover.append(z)
  write('INDEPENDENT_INTEGER_COVER_CHECK.json',{'status':'ALL24624_ACTUAL_POINTS_PASS','selected_original_variables':selected,'sigma':[sigma[r] for r in range(36)],'shifts':[shifts[r] for r in range(36)],'semantic_check':'recomputedMinkowskiunionsfromA_notCNF_orB','point_obligations':24624,'target_masks':cover})
  # Source format inherited from run_gate_once.py: comments/blank lines + raw edge pairs, no NM header.
  source=ROOT/'research/ddp/m1_sources/graph_7_4_n684.txt';old=set()
  with source.open() as f:
   for line in f:
    if not line.strip() or line.startswith('#'):continue
    u,v=map(int,line.split());assert 0<=u<684 and 0<=v<684 and u!=v;old.add(tuple(sorted((u,v))))
  source_parses=1;assert len(old)==2394
  deg=collections.Counter(v for e in old for v in e);assert len(deg)==684 and set(deg.values())=={7}
  def nu(r,k):return 342*(r//18)+9*((r%2)+2*k)+(r%18)//2
  M=[]
  for r in range(36):
   for k in range(19):M.append([nu(r,k),nu(sigma[r],(k+shifts[r])%19)])
  assert len({u for u,v in M})==len({v for u,v in M})==684
  final=old|{(u+684,v+684) for u,v in old}|{tuple(sorted((u,v+684))) for u,v in M}
  assert len(final)==5472
  with (D/'candidate1368.edges').open('w') as f:
   f.write('1368 5472\n')
   for u,v in sorted(final):f.write(f'{u} {v}\n')
  write('MATCHING684.json',M)
  write('PARAMETERS.json',{'n':1368,'m':5472,'degree':8,'target_D':4,'sigma':[sigma[r] for r in range(36)],'shifts':[shifts[r] for r in range(36)],'source_literal':str(source.relative_to(ROOT)),'source_format':'comments_blank_and_headerless_edgepairs','source_old_edges_preserved_eachcopy':2394,'matching_edges':684,'source_parse_count':1,'sourceD4validity_BFS':0,'status':'SEMANTIC_COVER_PASS_PENDING_PRODUCER_BFS_AND_FRESH'})
  remain=cap-used()-1
  if remain<2:raise RuntimeError('NO_BUDGET_FOR_POSITIVE_CANDIDATE_BFS')
  rc=child([str(D/'build_model'),str(max(.1,remain-1)),'--verify',str(D/'candidate1368.edges')],'CANDIDATE_BFS.log',remain,20,'POSITIVE_CANDIDATE_ALLROOT_BFS')
  if rc:raise RuntimeError('POSITIVE_CANDIDATE_BFS_FAILED')
  newroot_bfs=1368;status='FOUND1368_ALL_ROOTS_PASS_PENDING_FRESH_ACCEPTANCE'
 elif native_rc==20 and any(s=='s UNSATISFIABLE' for s in s_lines):status='RAW_UNSAT_UNCHECKED_K19_EXACT_POINT_MODEL'
 else:status='UNKNOWN_SINGLE_CADICAL_WINDOW'
except Exception as e:
 write('EXECUTION_ERROR.json',{'error':str(e),'case_CPU_sofar':used(),'charges':charges});status='UNKNOWN_EXECUTION_OR_BINDING_FAILURE'
finally:
 result={'status':status,'terminal':True,'prior_readgate_CPU':prior,'new_prep_charge':prep,'charges':charges,'parent_actual_CPU':time.process_time()-start,'cumulative_case_CPU':used(),'CPU_cap':cap,'solver_calls':sat_calls,'native_return_code':native_rc,'source_literal_parse_count':source_parses,'old_endpoint_DP_repeated':0,'sourceD4validity_BFS':0,'old_H233928_repeated':0,'candidate_allroot_BFS':newroot_bfs,'source_field_Lean_ARIS_runs':0,'new_graph_parameter_Lean_count':[0,0,0],'formal_negative_family_verdict':'UNRESOLVED_UNLESS_ROOT_SEPARATELY_ACCEPTS_CHECKED_EVIDENCE','automatic_continuation':False}
 if (D/'BUILD_RESULT.json').exists():result['model']=json.loads((D/'BUILD_RESULT.json').read_text())
 if (D/'NATIVE_EXECUTION.json').exists():result['native']=json.loads((D/'NATIVE_EXECUTION.json').read_text())
 write('RESULT.json',result);write('TERMINAL.json',{'status':status,'terminal':True,'cumulative_case_CPU':result['cumulative_case_CPU'],'CPU_cap':cap,'solver_calls':sat_calls,'sourceD4validity_BFS':0,'native_return_code':native_rc,'wall_seconds':time.time()-wall,'stop':True})
 print(json.dumps(result,indent=2),flush=True)
