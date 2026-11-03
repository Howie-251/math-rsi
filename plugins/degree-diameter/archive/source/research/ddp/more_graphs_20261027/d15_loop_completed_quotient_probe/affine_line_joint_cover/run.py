"""Joint affine-line point-cover CEG; cached balls only, no blockmask columns."""
import os,time,resource
START=time.process_time();WALL=time.monotonic()
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
import json,pathlib,subprocess,math
import numpy as np
from support_loader import load_source,point_support
P=pathlib.Path(__file__).resolve().parent
ROOT=pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
BASE=ROOT/'research/ddp/more_graphs_20261027'
cr=resource.getrusage(resource.RUSAGE_CHILDREN);C0=cr.ru_utime+cr.ru_stime
pred=json.loads((P/'PREDICTION.json').read_text());assert pred['status']=='FROZEN_BEFORE_JOINT_POINT_SUPPORT_OR_MODEL';assert not(P/'RESULT.json').exists()
carry=pred['budget']['carried_interface_CPU_seconds']
CAD=ROOT/'.tools/lean-4.24.0-linux/bin/cadical';assert CAD.exists()
resource.setrlimit(resource.RLIMIT_CPU,(15,130))
def childcpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime-C0
def used():return carry+time.process_time()-START+childcpu()
def save(name,obj):(P/name).write_text(json.dumps(obj,indent=2)+'\n')
def export(spec,pins):
 n,m,D=spec['n'],spec['m'],spec['D'];out=P/'candidate';out.mkdir(exist_ok=True);graph=out/f'graph_d15_D{D}_n{n+1}.edges'
 if n==15552:
  source=BASE/'d15_D4_current15552/source15552.header.edges';degrees={v:0 for v in pins};pinset=set(pins);written=0
  with source.open()as old,graph.open('w')as new:
   assert tuple(map(int,next(old).split()))==(n,m);new.write(f'{n+1} {m+len(pins)}\n')
   for line in old:
    if line.strip():
     a,b=map(int,line.split());written+=1
     if a in pinset:degrees[a]+=1
     if b in pinset:degrees[b]+=1
     new.write(line)
   for v in pins:new.write(f'{v} {n}\n')
  assert written==m
 else:
  source=BASE/'d15_D5_current102060_source/monotone_R4_cover/source.csr.u32le.bin';data=np.fromfile(source,dtype='<u4');assert tuple(map(int,data[:2]))==(n,2*m)
  offsets=data[2:n+3];neighbors=data[n+3:];assert len(neighbors)==2*m and int(offsets[-1])==2*m
  degrees={v:int(offsets[v+1]-offsets[v]) for v in pins};written=0
  with graph.open('w')as new:
   new.write(f'{n+1} {m+len(pins)}\n')
   for u in range(n):
    for v in neighbors[int(offsets[u]):int(offsets[u+1])]:
     if u<int(v):new.write(f'{u} {int(v)}\n');written+=1
   for v in pins:new.write(f'{v} {n}\n')
  assert written==m
 assert all(degrees[v]==14 for v in pins)
 return str(graph.relative_to(ROOT)),degrees
source_results=[];hit=None;calls=0
for n in [15552,102060]:
 if used()>127:break
 data=load_source(n);spec=data['spec'];lines=data['lines'];ids=data['ids'];words=data['words'];n=spec['n'];D=spec['D'];q=spec['bin_size'];neg=data['neg_local_offsets']
 L=len(lines);assert L==(2808 if n==15552 else 3510)
 assert len(ids)==(648 if n==15552 else 810)
 assert [x['line_id'] for x in lines]==list(range(L))
 assert {p for line in lines for p in line['pins']}==set(ids)
 assert all(len(set(line['pins']))==3 and [ids[i] for i in line['ball_row_indices']]==line['pins'] for line in lines)
 rowindex={p:i for i,p in enumerate(ids)}
 targets=set(data['initial_targets']);assert len(targets)==(1728 if n==15552 else 4620)
 initial_targets=sorted(targets);support_cache={}
 def support(t):
  if t not in support_cache:support_cache[t]=point_support(data,t)
  return support_cache[t]
 structural=[];countvars=L;table=[]
 for _ in lines:table.append(list(range(countvars+1,countvars+7)));countvars+=6
 for i,x in enumerate(range(1,L+1)):
  structural.append([-x,table[i][0]])
  if i:
   for j in range(6):structural.append([-table[i-1][j],table[i][j]])
   for j in range(1,6):structural.append([-x,-table[i-1][j-1],table[i][j]])
 structural.append([-table[-1][5]])
 source_cpu=0.;rounds=[];source_status='UNKNOWN_ROUND_LIMIT';sub=P/f'source{n}';sub.mkdir(exist_ok=True)
 save(f'source{n}/INITIAL_TARGETS.json',{'source_n':n,'target_count':len(targets),'targets':initial_targets,'all_raw_lines':L,'no_blockmask_dedup':True,'zero_blockmask_lines_preserved':True})
 for rnd in range(8):
  if time.process_time()-START>14.5 or used()>127:source_status='UNKNOWN_PREP_OR_AGGREGATE_BUDGET';break
  masks=sorted({support(t) for t in targets})
  cnf=sub/f'round{rnd:02d}.cnf';cover_literals=0
  with cnf.open('w')as f:
   f.write(f'p cnf {countvars} {len(masks)+len(structural)}\n')
   for mask in masks:
    row=[]
    while mask:
     bit=mask&-mask;v=bit.bit_length();assert 1<=v<=L;row.append(str(v));mask^=bit
    cover_literals+=len(row);f.write(' '.join(row)+' 0\n')
   for row in structural:f.write(' '.join(map(str,row))+' 0\n')
  remain=min(50.-source_cpu,130.-used()-2.)
  available=int(math.floor(remain))
  if available<2:source_status='UNKNOWN_SOURCE_SOLVER_BUDGET';break
  request=max(1,available-1);soft=hard=available
  model={'source_n':n,'D':D,'round':rnd,'all_line_variables':L,'selected_line_limit':5,'current_point_targets':len(targets),'unique_point_support_rows':len(masks),'variables':countvars,'clauses':len(masks)+len(structural),'cover_literals':cover_literals,'source_solver_CPU_used_before':source_cpu,'source_solver_CPU_remaining_before':50.-source_cpu,'CaDiCaL_requested_seconds':request,'OS_CPU_soft_hard':[soft,hard],'parent_prep_CPU':time.process_time()-START}
  save(f'source{n}/round{rnd:02d}_MODEL.json',model);save(f'source{n}/round{rnd:02d}_TARGETS.json',sorted(targets));print('MODEL_READY '+json.dumps(model),flush=True)
  if time.process_time()-START>14.5:source_status='UNKNOWN_PREP_CPU_LIMIT';break
  def limits():resource.setrlimit(resource.RLIMIT_CPU,(soft,hard));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
  out=sub/f'round{rnd:02d}.stdout';err=sub/f'round{rnd:02d}.stderr';before=childcpu();sw=time.monotonic()
  with out.open('w')as so,err.open('w')as se:
   proc=subprocess.Popen([str(CAD),'-t',str(request),str(cnf)],stdout=so,stderr=se,preexec_fn=limits);calls+=1
   save('LIVE_HANDLE.json',{'status':'RUNNING_JOINT_CEG_SOLVER','source_n':n,'round':rnd,'pid':proc.pid,'source_solver_CPU_before':source_cpu,'requested_seconds':request,'OS_limits':[soft,hard]});print('SOLVER_RUNNING '+json.dumps({'source_n':n,'round':rnd,'pid':proc.pid,'seconds':request}),flush=True)
   try:code=proc.wait(timeout=available+10)
   except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
  elapsed=childcpu()-before;source_cpu+=elapsed;text=out.read_text();row={**model,'solver_return_code':code,'solver_CPU_seconds':elapsed,'solver_wall_seconds':time.monotonic()-sw,'source_solver_CPU_used_after':source_cpu}
  if 's UNSATISFIABLE' in text:
   row['status']='SOLVER_UNSAT_NECESSARY_POINT_MODEL_UNCERTIFIED';rounds.append(row);source_status='SOLVER_UNSAT_COMPLETE_AT_MOST_FIVE_LINE_DOMAIN_UNCERTIFIED';save(f'source{n}/round{rnd:02d}_RESULT.json',row);break
  if 's SATISFIABLE' not in text:
   row['status']='UNKNOWN_NO_SAT_ASSIGNMENT';rounds.append(row);source_status='UNKNOWN_SOLVER_LIMIT';save(f'source{n}/round{rnd:02d}_RESULT.json',row);break
  values=[]
  for line in text.splitlines():
   if line.startswith('v '):values.extend(map(int,line[2:].split()))
  pos={v for v in values if v>0};selected=[line for line in lines if line['selector_variable'] in pos]
  assert len(selected)<=5
  chosen=sum(1<<line['line_id'] for line in selected);assert all(support(t)&chosen for t in targets)
  pins=sorted({p for line in selected for p in line['pins']});assert 0<len(pins)<=15 and all(p in rowindex for p in pins)
  selected_rows=[rowindex[p] for p in pins];covered=np.bitwise_or.reduce(words[selected_rows,:],axis=0)
  bits=np.unpackbits(np.asarray(covered,dtype='<u8').view(np.uint8),bitorder='little')[:n];missing=np.flatnonzero(bits==0)
  np.asarray(covered,dtype='<u8').tofile(sub/f'round{rnd:02d}_FULL_OR.u64le.bin')
  row.update(status='SAT_CANDIDATE_FULL_POINT_OR_CHECKED',selected_line_ids=[line['line_id'] for line in selected],selected_lines=selected,pins=pins,distinct_pins=len(pins),covered_target_count=int(bits.sum()),missing_target_count=len(missing),first_missing_target=int(missing[0]) if len(missing) else None)
  if not len(missing):
   graph,degrees=export(spec,pins)
   hit={'status':'PRODUCTION_FULL_CURRENT_POINT_COVER_AND_ACTUAL_DEGREE','source_n':n,'source_m':spec['m'],'source_D':D,'new_vertex':n,'new_n':n+1,'new_m':spec['m']+len(pins),'full_neighbor_set':pins,'selected_lines':selected,'line_count':len(selected),'new_vertex_degree':len(pins),'old_pin_degrees':[degrees[p] for p in pins],'max_degree':15,'complete_cached_radius':D-1,'complete_cached_targets':n,'all_old_edges_retained':True,'graph_file':graph,'new_graph_BFS':0,'source_allroot_BFS':0,'parent_pending':True}
   save('FIRST_HIT.json',hit);save('candidate/accepted_step.json',hit);row['status']='FIRST_FULL_COVER_HIT';rounds.append(row);save(f'source{n}/round{rnd:02d}_RESULT.json',row);source_status='FIRST_HIT_STOP';break
  first_by_fiber={}
  for t in missing:
   t=int(t);first_by_fiber.setdefault(t//q,t)
  added=[];counterexamples=[]
  for fiber,t in sorted(first_by_fiber.items()):
   opposite=fiber*q+neg[t%q];assert t not in targets and not(support(t)&chosen)
   newpair=[]
   for u in [t,opposite]:
    if u not in targets:targets.add(u);added.append(u);newpair.append(u)
   counterexamples.append({'fiber':fiber,'first_missing_target':t,'negative_target':opposite,'added_targets':newpair,'first_clause_excludes_current_assignment':True})
  assert added
  row.update(missing_fiber_count=len(first_by_fiber),added_target_count=len(added),added_targets=added,counterexamples=counterexamples,next_target_count=len(targets))
  rounds.append(row);save(f'source{n}/round{rnd:02d}_RESULT.json',row);save(f'source{n}/round{rnd:02d}_NEXT_TARGETS.json',sorted(targets))
  save('CEG_CURSOR.json',{'status':'SOURCE_HAS_VALID_NEW_POINT_CUTS','source_n':n,'next_round':rnd+1,'source_solver_CPU':source_cpu,'targets':sorted(targets),'rounds_complete':len(rounds)})
  print('VALID_POINT_CUTS '+json.dumps({'source_n':n,'round':rnd,'missing':len(missing),'missing_fibers':len(first_by_fiber),'added_targets':len(added),'next_targets':len(targets)}),flush=True)
  if rnd==7:source_status='UNKNOWN_EIGHT_ROUND_LIMIT'
 result={'source_n':n,'source_m':spec['m'],'D':D,'status':source_status,'all_raw_lines':L,'initial_point_targets':len(initial_targets),'final_point_targets':len(targets),'rounds':rounds,'solver_calls':len(rounds),'source_solver_CPU_seconds':source_cpu,'full_point_OR_candidate_checks':sum('pins' in x for x in rounds),'CNF_domain':'all raw affine free3lines, atmost5, jointpointcoverage','new_balls':0,'source_BFS':0}
 source_results.append(result);save(f'source{n}/RESULT.json',result);save('CHECKPOINT.json',{'sources':source_results,'aggregate_CPU_seconds':used(),'hit':hit});print('SOURCE_DONE '+json.dumps({k:result[k] for k in ['source_n','status','solver_calls','source_solver_CPU_seconds','full_point_OR_candidate_checks']}),flush=True)
 if hit:break
 del data,words,structural,table,support_cache
r={'status':'FIRST_HIT_STOP' if hit else 'TERMINAL_JOINT_FIVE_LINE_BATCH' if len(source_results)==2 else 'UNKNOWN_AGGREGATE_OR_PREP_BUDGET','sources':source_results,'first_hit':hit,'source_models_not_attempted':2-len(source_results),'solver_calls':calls,'candidate_graphs':int(hit is not None),'full_point_OR_candidate_checks':sum(x['full_point_OR_candidate_checks'] for x in source_results),'carried_interface_CPU_seconds':carry,'parent_CPU_seconds':time.process_time()-START,'children_CPU_seconds':childcpu(),'aggregate_CPU_seconds':used(),'wall_seconds':time.monotonic()-WALL,'new_balls':0,'source_allroot_BFS':0,'pending':[]}
save('RESULT.json',r);save('TERMINAL.json',{k:r[k] for k in ['status','solver_calls','aggregate_CPU_seconds','candidate_graphs','source_models_not_attempted','full_point_OR_candidate_checks','pending']});save('LIVE_HANDLE.json',{'status':'TERMINAL','pending':[]});print('FINAL '+json.dumps({k:r[k] for k in ['status','solver_calls','aggregate_CPU_seconds','candidate_graphs','full_point_OR_candidate_checks']}),flush=True)
