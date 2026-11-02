#!/usr/bin/env python3
import time
START=time.process_time()
import collections,csv,json,os,re,resource,subprocess,traceback
from pathlib import Path
HERE=Path(__file__).resolve().parent;SEEDED=HERE.parent;AVAILABLE=SEEDED.parent;PLANE=AVAILABLE.parent
ROOT=next(p for p in HERE.parents if(p/'research-wiki').is_dir())
SOLVER=ROOT/'.tools/lean-4.24.0-linux/bin/cadical'
PRIOR=71.065033579;PREP=.5;CAP=120.;N=16416;WIDTH=2052;FULL=(1<<N)-1
resource.setrlimit(resource.RLIMIT_CPU,(24,24))
def save(name,x):(HERE/name).write_text(json.dumps(x,indent=2)+'\n')
def union(pins,masks):
 out=0
 for p in pins:out|=masks[p]
 return out
def setbits(m):
 while m:
  b=m&-m;yield b.bit_length()-1;m^=b
def childlimit():resource.setrlimit(resource.RLIMIT_CPU,(20,20))
assert not(HERE/'ATTEMPT.json').exists(),'oneauthorizedSATattemptonly'
packet=dict(status='PREPARING_FIXED_RESIDUAL_SAT',driver_pid=os.getpid(),prior_case_CPU_seconds=PRIOR,
 new_preparation_CPU_seconds=PREP,wholecase_CPU_cap_seconds=CAP,native_hardCPU=20,parent_hardCPU=24)
save('ATTEMPT.json',packet);save('HANDLE.json',packet)
child=None;ccpu=0.;solver_calls=0;result={};phase='INPUT_AND_CNF'
try:
 if not(SOLVER.is_file()and os.access(SOLVER,os.X_OK)):
  result=dict(status='UNKNOWN_EXISTING_CADICAL_NOT_EXECUTABLE_NO_INSTALL',solver_calls=0)
 else:
  mapping=json.loads((SEEDED/'RESIDUAL_COLUMN_ROW_MAPPING.json').read_text())
  frozen=json.loads((SEEDED/'FROZEN_TEMPLATE.json').read_text())
  assert frozen['source_center_v']==12312 and mapping['frozen_template_v']==12312
  seed=frozen['fixed_available_seed'];assert len(seed)==11
  cols=mapping['columns'];targets=mapping['initialhole_actual_targets'];nv=len(cols)
  assert nv==3771 and len(targets)==1744 and [c['column']for c in cols]==list(range(nv))
  pins=json.loads((AVAILABLE/'ALL_AVAILABLE_PINS.json').read_text())['available_actual_pin_labels'];masks={}
  with(AVAILABLE/'ALL4050_CLOSED_R3_SUPPORTS.bits').open('rb')as f:
   for p in pins:
    b=f.read(WIDTH);assert len(b)==WIDTH;masks[p]=int.from_bytes(b,'little')
   assert not f.read(1)
  seedcover=union(seed,masks);holes=FULL&~seedcover
  assert list(setbits(holes))==targets and holes==int(frozen['initial_hole_mask_hex'],16)
  rowindex={v:i for i,v in enumerate(targets)};clauses=[[]for _ in targets];varmap=[]
  for c,col in enumerate(cols):
   p=col['actual_representative'];assert p in masks
   residual=masks[p]&holes;assert residual
   for target in setbits(residual):clauses[rowindex[target]].append(c+1)
   varmap.append(dict(real_variable=c+1,actual_pin=p,equivalent_actual_pins=col['equivalent_actual_pins']))
  positive_literals=sum(map(len,clauses));emptyrows=sum(not c for c in clauses)
  aux=nv*5;cardcount=nv+(nv-1)*10+4;totalclauses=len(clauses)+cardcount
  def s(i,j):return nv+(i-1)*5+j
  cnf=HERE/'FIXED_V12312_COVER_ATMOST5.cnf';written=0
  with cnf.open('w')as f:
   f.write(f'p cnf {nv+aux} {totalclauses}\n')
   def emit(c):
    global written
    f.write(' '.join(map(str,c))+' 0\n');written+=1
   for c in clauses:emit(c)
   for j in range(2,6):emit([-s(1,j)])
   for i in range(1,nv+1):
    emit([-i,s(i,1)])
    if i>1:
     for j in range(1,6):emit([-s(i-1,j),s(i,j)])
     for j in range(2,6):emit([-i,-s(i-1,j-1),s(i,j)])
     emit([-i,-s(i-1,5)])
  assert written==totalclauses
  save('REAL_VARIABLE_TO_ACTUAL_PIN.json',dict(fixed_template_v=12312,seed=seed,columns=varmap,
   real_variables=nv,auxiliary_formula='s(i,j)=3771+(i-1)*5+j;i1..3771,j1..5'))
  save('CNF_MODEL.json',dict(template_v=12312,fixedseed=seed,real_variables=nv,auxiliary_variables=aux,
   total_variables=nv+aux,hole_OR_clauses=len(clauses),hole_positive_literals=positive_literals,empty_hole_OR_clauses=emptyrows,
   cardinality_clauses=cardcount,total_clauses=totalclauses,atmost_extras=5,allcurrenttargets=16416,
   residualrows_actualtargets='source_neighborhood_seed_cover/RESIDUAL_COLUMN_ROW_MAPPING.json',
   proof_logging=False,proof_checked=False,source_parse_or_ball_recomputation=0))
  phase='SOLE_NATIVE_SAT';cmd=[str(SOLVER),'-t','19',str(cnf)]
  with(HERE/'SAT_STDOUT.log').open('w')as out,(HERE/'SAT_STDERR.log').open('w')as err:
   child=subprocess.Popen(cmd,stdout=out,stderr=err,preexec_fn=childlimit)
   solver_calls=1;packet.update(status='ACTUAL_NATIVE_SAT_RUNNING',native_child_pid=child.pid,command=cmd)
   save('NATIVE_EXECUTION.json',dict(packet,proof_logged=False,proof_checked=False))
   save('HANDLE.json',packet)
   _,st,usage=os.wait4(child.pid,0);child.returncode=os.waitstatus_to_exitcode(st)
  ccpu=usage.ru_utime+usage.ru_stime
  stdout=(HERE/'SAT_STDOUT.log').read_text();stderr=(HERE/'SAT_STDERR.log').read_text()
  statuslines=[line for line in stdout.splitlines()if line.startswith('s ')]
  rawstatus=statuslines[-1]if statuslines else'NO_STATUS_LINE'
  stats={}
  for label in ['conflicts','decisions','propagations']:
   match=re.search(r'\b'+label+r':\s+(\d+)',stdout)
   stats[label]=int(match[1])if match else None
  result=dict(status='UNKNOWN_FIXED_V12312_SAT_NO_ATMOST5_WITNESS',raw_solver_status=rawstatus,
   native_return_code=child.returncode,solver_calls=1,native_actual_CPU_seconds=ccpu,
   native_stats=stats,CNF_variables=nv+aux,CNF_clauses=totalclauses,hole_OR_clauses=1744,
   true_pin_variables=3771,atmost_extras=5,proof_logged=False,proof_checked=False,
   fixed_template_v=12312,allcurrenttarget_count=16416,new_balls_sourceD4_field_Lean_ARIS=0,
   candidate_graphs_generated=0,new_graph_parameter_Lean_counts=[0,0,0],strict_mathematical_family_NO=False,
   next='STOP oneSAT,no secondsolver/seed/template')
  if child.returncode==20 and rawstatus=='s UNSATISFIABLE':
   result['status']='RAW_UNSAT_FIXED_V12312_ATMOST5_NO_CHECKED_PROOF_NOT_FULL_FAMILY_NO'
  if child.returncode==10 and rawstatus=='s SATISFIABLE':
   phase='SAT_ACTUAL_PIN_AND_WHOLE_COVER_HANDCHECK';assign={}
   for line in stdout.splitlines():
    if not line.startswith('v '):continue
    for tok in line.split()[1:]:
     lit=int(tok)
     if lit and abs(lit)<=nv:
      assert abs(lit)not in assign or assign[abs(lit)]==(lit>0)
      assign[abs(lit)]=lit>0
   assert len(assign)==nv
   chosen_vars=sorted(v for v,b in assign.items()if b);extras=[cols[x-1]['actual_representative']for x in chosen_vars]
   actualpins=sorted(set(seed)|set(extras))
   assert len(extras)<=5 and len(actualpins)<=16 and all(p in masks for p in actualpins)
   assert union(actualpins,masks)==FULL
   adj=[[]for _ in range(N)];edges=[]
   with(PLANE/'graph_d16_D4_n16416.edges').open()as f:
    assert tuple(map(int,next(f).split()))==(N,129240)
    for line in f:
     u,v=map(int,line.split());adj[u].append(v);adj[v].append(u);edges.append((u,v))
   degree=list(map(len,adj));assert all(degree[p]<16 for p in actualpins)
   depth=[-1]*N;parent=[-1]*N;q=[]
   for p in actualpins:depth[p]=0;parent[p]=p;q.append(p)
   for v in q:
    if depth[v]>=3:continue
    for w in adj[v]:
     if depth[w]<0:depth[w]=depth[v]+1;parent[w]=v;q.append(w)
   assert len(q)==N and max(depth)<=3
   with(HERE/'NEWROOT_ROUTES.tsv').open('w',newline='')as f:
    out=csv.writer(f,delimiter='\t');out.writerow(['actual_current_target','newroot_distance','actual_route'])
    for v in range(N):
     rev=[v]
     while depth[rev[-1]]:rev.append(parent[rev[-1]])
     route=[N]+list(reversed(rev));out.writerow([v,len(route)-1,','.join(map(str,route))])
   save('NEWROOT_PARENT_DEPTH.json',dict(pins=actualpins,parent=parent,depth=depth,current_n=N,new_label=N))
   graph=HERE/'graph_d16_D4_n16417.edges'
   with graph.open('w')as f:
    f.write(f'{N+1} {129240+len(actualpins)}\n')
    for u,v in edges:f.write(f'{u} {v}\n')
    for p in actualpins:f.write(f'{p} {N}\n')
   fd=[degree[v]+int(v in set(actualpins))for v in range(N)]+[len(actualpins)];assert max(fd)<=16
   save('PIN_SET.json',dict(actual_pin_labels=actualpins,extras=extras,real_true_variables=chosen_vars,
    fixedseed=seed,total_count=len(actualpins),allcurrent_R3_union=16416))
   save('PARAMETERS.json',dict(n=N+1,m=129240+len(actualpins),maxdegree=16,degree_histogram=dict(collections.Counter(fd)),
    all129240_oldcurrent_edges_preserved=True,newZ_label=N,pins=actualpins,template_v=12312,
    oldD4='INHERITED_ACCEPTED',newoldD4='actualcurrentR3coverplusoneedge',exactD4_lower='16417>Moore16D3=3857',
    fresh_acceptance='PENDING_ROOT',new_graph_parameter_Lean_counts=[0,0,0]))
   result.update(status='SAT_HANDCHECKED_ATMOST16_PIN_COVER_16417_CANDIDATE_PENDING_FRESH_ACCEPTANCE',
    actual_pin_labels=actualpins,actual_extra_count=len(extras),actual_total_pins=len(actualpins),actual_whole_cover=16416,
    candidate_graphs_generated=1,candidate_n=N+1,candidate_m=129240+len(actualpins),newroot_route_BFS=1,
    current_graph_parses_on_positive=1,fresh_acceptance='PENDING_ROOT')
except Exception as e:
 result.update(status='UNKNOWN_DIRECT_SAT_PROCESS_OR_HANDCHECK_FAILURE',phase=phase,error=str(e),traceback=traceback.format_exc(),
  solver_calls=solver_calls,candidate_graphs_generated=0,new_graph_parameter_Lean_counts=[0,0,0])
pcpu=time.process_time()-START
result.update(driver_pid=os.getpid(),native_child_pid=child.pid if child else None,
 actual_parent_CPU_seconds=pcpu,actual_native_child_CPU_seconds=ccpu,prior_case_CPU_seconds=PRIOR,
 new_preparation_CPU_seconds=PREP,wholecase_CPU_seconds=PRIOR+PREP+pcpu+ccpu,wholecase_CPU_cap_seconds=CAP,
 terminal=True,active_processes=0)
save('RESULT.json',result);save('TERMINAL.json',result);save('HANDLE.json',result);print(json.dumps(result),flush=True)
