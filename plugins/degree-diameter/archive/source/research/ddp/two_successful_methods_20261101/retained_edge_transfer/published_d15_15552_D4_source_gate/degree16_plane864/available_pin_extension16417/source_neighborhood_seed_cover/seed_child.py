#!/usr/bin/env python3
import time
START=time.process_time()
import array,collections,csv,json,math,os,resource,traceback
from pathlib import Path
HERE=Path(__file__).resolve().parent;AVAILABLE=HERE.parent;PLANE=AVAILABLE.parent
ROOT=next(p for p in HERE.parents if(p/'research-wiki').is_dir())
COOP=PLANE/'cooperative_fourblocker_repair16417'
LOCAL=PLANE.parent/'nonorbit_clone_interface/append_oneout_twoin_gate'
N=16416;OLD=15552;WIDTH=2052;FULL=(1<<N)-1
resource.setrlimit(resource.RLIMIT_CPU,(65,65))
phase='INPUT';prefix={}
def save(name,x):(HERE/name).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
def checkpoint(stage,**kw):save('CHECKPOINT.json',dict(stage=stage,pid=os.getpid(),CPU_sofar=time.process_time()-START,**kw))
def budget():
 if time.process_time()-START>=60:raise TimeoutError('softCPU60')
def union(pins,mapping):
 out=0
 for p in pins:out|=mapping[p]
 return out
def bits(mask):
 while mask:
  b=mask&-mask;yield b.bit_length()-1;mask^=b
def clean(v):
 if isinstance(v,(bool,int,str))or v is None:return v
 if isinstance(v,float):return v if math.isfinite(v)else str(v)
 return str(v)
def main():
 global phase,prefix
 raw=(LOCAL/'ALL15552_CENTER_BLOCKING_PROFILES.tsv').read_text()
 if'\t'not in raw.splitlines()[0]:raw=raw.replace('\\t','\t')
 templates=[r for r in csv.DictReader(raw.splitlines(),delimiter='\t')if int(r['selected_role_or_minus1'])<0 and int(r['zero_residual_neighbours'])==4]
 assert templates
 pinlist=json.loads((AVAILABLE/'ALL_AVAILABLE_PINS.json').read_text())['available_actual_pin_labels'];pinmasks={}
 with(AVAILABLE/'ALL4050_CLOSED_R3_SUPPORTS.bits').open('rb')as f:
  for p in pinlist:
   b=f.read(WIDTH);assert len(b)==WIDTH;pinmasks[p]=int.from_bytes(b,'little')
  assert not f.read(1)
 oldR3=[]
 with(COOP/'CURRENT_OLDSOURCE15552_R3.bits').open('rb')as f:
  for _ in range(OLD):
   b=f.read(WIDTH);assert len(b)==WIDTH;oldR3.append(int.from_bytes(b,'little'))
  assert not f.read(1)
 adj=[[]for _ in range(N)];edges=[]
 with(PLANE/'graph_d16_D4_n16416.edges').open()as f:
  assert tuple(map(int,next(f).split()))==(N,129240)
  for line in f:
   u,v=map(int,line.split());adj[u].append(v);adj[v].append(u);edges.append((u,v))
 degree=list(map(len,adj));assert len(edges)==129240 and set(pinlist)=={v for v in range(N)if degree[v]<16}
 records=[];winner=None;frozen=None;phase='SOURCE_SEEDED_GREEDY'
 outstream=(HERE/'ALL_TEMPLATE_GREEDY_RECORDS.jsonl').open('w')
 for ti,row in enumerate(templates):
  budget();v=int(row['source_center']);prefix={'template_index':ti,'source_center_v':v}
  Nv=sorted(w for w in adj[v]if w<OLD);blocked=sorted(w for w in Nv if degree[w]==16);seed=sorted(set(Nv)-set(blocked))
  assert len(blocked)==4 and len(Nv)==int(row['source_degree']) and all(p in pinmasks for p in seed)
  assert union(Nv,{p:oldR3[p]for p in Nv})==FULL
  assert all(pinmasks[p]==oldR3[p]for p in seed)
  seedcover=union(seed,pinmasks);holes=FULL&~seedcover;categories={}
  for pattern in range(16):
   cm=holes
   for j,p in enumerate(blocked):cm&=oldR3[p]if pattern>>j&1 else FULL^oldR3[p]
   categories[pattern]=cm
  assert categories[0]==0 and sum(m.bit_count()for m in categories.values())==holes.bit_count()
  uncovered=holes;extras=[];steps=[]
  while uncovered:
   budget();best=None;gain=0
   for p in pinlist:
    g=(pinmasks[p]&uncovered).bit_count()
    if g>gain:best=p;gain=g
   assert best is not None and gain>0
   repaired=pinmasks[best]&uncovered;extras.append(best);uncovered&=~pinmasks[best]
   steps.append(dict(actual_extra_pin=best,current_role='original15552'if best<OLD else'current_clone',
    gain=gain,remaining_holes=uncovered.bit_count(),repaired_actual_target_mask_hex=hex(repaired),
    repaired_initial_hole_category_hist={hex(k):(cm&repaired).bit_count()for k,cm in categories.items()if cm&repaired}))
  before=extras.copy();deleted=[]
  for p in reversed(before):
   trial=[q for q in extras if q!=p]
   if seedcover|union(trial,pinmasks)==FULL:extras=trial;deleted.append(p)
  chosen=sorted(set(seed)|set(extras));actualcover=union(chosen,pinmasks);assert actualcover==FULL
  rec=dict(template_index=ti,source_center_v=v,original_source_Nv=Nv,blocked_current_degree16_pins=blocked,
   fixed_available_seed=seed,seed_size=len(seed),initial_hole_count=holes.bit_count(),initial_hole_mask_hex=hex(holes),
   hole_category_bit_order=blocked,hole_category_histogram={hex(k):cm.bit_count()for k,cm in categories.items()},
   greedy_steps=steps,extra_before_redundancy_count=len(before),extra_pins=extras,deleted_redundant_extras=deleted,
   actual_complete_pin_labels=chosen,total_pin_count=len(chosen),actual_wholecurrent_union_count=actualcover.bit_count())
  records.append(rec);outstream.write(json.dumps(rec)+'\n');outstream.flush()
  if frozen is None or(len(chosen),v)<(frozen['total_pin_count'],frozen['source_center_v']):frozen=rec
  if len(chosen)<=16:winner=chosen;break
  if(ti+1)%32==0:checkpoint('GREEDY_TEMPLATES_ACTIVE',completed=ti+1,total=len(templates),best_total=frozen['total_pin_count'])
 outstream.close()
 save('TEMPLATE_GREEDY_SUMMARY.json',dict(actual_template_domain=len(templates),expected_saved_hist_count=162,
  templates_processed=len(records),all_templates_greedy_completed=len(records)==len(templates),
  total_pin_count_histogram=dict(collections.Counter(r['total_pin_count']for r in records)),
  seed_size_histogram=dict(collections.Counter(r['seed_size']for r in records)),
  best_template_v=frozen['source_center_v'],best_total_count=frozen['total_pin_count'],
  greedy_passes_per_template=1,extra_redundancy_passes_per_template=1,nonewballs=True))
 solver_calls=0;solver_raw=None;bestpins=winner or frozen['actual_complete_pin_labels']
 if winner is None:
  phase='FROZEN_RESIDUAL_MODEL';budget();save('FROZEN_TEMPLATE.json',frozen)
  (HERE/'SOLVER_PRED.md').write_text('# Sole residual solve\n\nFreezev='+str(frozen['source_center_v'])+
   ', fixedseed='+str(frozen['seed_size'])+', extrasbudget='+str(16-frozen['seed_size'])+
   '. Onlyinitialholes are rows; allavailableextras remain, empty/duplicate residualcolumns mapped. One20sminextras HiGHS warmstart, no secondtemplate/window.\n')
  seed=frozen['fixed_available_seed'];holes=int(frozen['initial_hole_mask_hex'],16)
  targets=list(bits(holes));rowindex={v:i for i,v in enumerate(targets)}
  groups={};columns=[];reps=[];pincol={}
  for p in pinlist:
   m=pinmasks[p]&holes
   if not m:continue
   if m not in groups:groups[m]=len(columns);columns.append(m);reps.append(p)
   pincol[p]=groups[m]
  maps=[[]for _ in columns]
  for p,c in pincol.items():maps[c].append(p)
  save('RESIDUAL_COLUMN_ROW_MAPPING.json',dict(initialhole_actual_targets=targets,allavailable_domain=4050,
   columns=[dict(column=i,actual_representative=reps[i],equivalent_actual_pins=maps[i])for i in range(len(columns))],
   seed_actual_pins=seed,frozen_template_v=frozen['source_center_v']))
  checkpoint('IMPORTING_EXISTING_HIGHS_FOR_ONE_RESIDUAL_WINDOW',rows=len(targets),columns=len(columns))
  import numpy as np
  import scipy.optimize._highspy._core as h
  p=len(columns);r=len(targets);lengths=np.array([m.bit_count()for m in columns],dtype=np.int32)
  start=np.zeros(p+1,dtype=np.int32);np.cumsum(lengths,out=start[1:])
  indices=np.empty(int(start[-1]),dtype=np.int32)
  for c,m in enumerate(columns):indices[start[c]:start[c+1]]=[rowindex[v]for v in bits(m)]
  warm=np.zeros(p,dtype=np.float64)
  for q in frozen['extra_pins']:warm[pincol[q]]=1
  warmrows=np.zeros(r,dtype=np.int32)
  for c in np.flatnonzero(warm):warmrows[indices[start[c]:start[c+1]]]+=1
  assert bool(np.all(warmrows>=1))
  lp=h.HighsLp();lp.num_col_=p;lp.num_row_=r;lp.col_cost_=np.ones(p);lp.col_lower_=np.zeros(p);lp.col_upper_=np.ones(p)
  lp.row_lower_=np.ones(r);lp.row_upper_=np.full(r,h.kHighsInf);lp.integrality_=[h.HighsVarType.kInteger]*p
  lp.a_matrix_.num_col_=p;lp.a_matrix_.num_row_=r;lp.a_matrix_.format_=h.MatrixFormat.kColwise
  lp.a_matrix_.start_=start;lp.a_matrix_.index_=indices;lp.a_matrix_.value_=np.ones(indices.size)
  hs=h._Highs();assert hs.setOptionValue('threads',1)==h.HighsStatus.kOk
  passed=hs.passModel(lp);assert passed==h.HighsStatus.kOk
  sol=h.HighsSolution();sol.col_value=warm.tolist();sol.row_value=warmrows.astype(float).tolist();sol.value_valid=True;sol.dual_valid=False
  warmstatus=hs.setSolution(sol);assert warmstatus==h.HighsStatus.kOk
  window=min(20.,57.-(time.process_time()-START))
  save('RESIDUAL_MODEL.json',dict(rows=r,allcurrent_targets=16416,deleted_seed_covered_rows=16416-r,
   available_extra_domain=4050,nonempty_unique_columns=p,nonzeros=int(indices.size),seed_size=len(seed),
   maximum_extra_budget=16-len(seed),warm_extra_count=int(warm.sum()),time_limit=max(0,window),threads=1,
   passModel=str(passed),setSolution=str(warmstatus),one_model_only=True))
  if window>0:
   assert hs.setOptionValue('time_limit',window)==h.HighsStatus.kOk
   checkpoint('ACTUAL_SOLE_RESIDUAL_HIGHS_RUNNING',frozen_v=frozen['source_center_v'],rows=r,columns=p,window=window)
   solver_calls=1;t=time.process_time();rs=hs.run();scpu=time.process_time()-t
   info=hs.getInfo();ms=hs.getModelStatus();s=hs.getSolution();x=np.asarray(s.col_value)
   valid=bool(s.value_valid)and x.size==p;chosen=[]
   if valid:
    rounded=np.rint(x).astype(np.int32);valid=bool(np.all(np.abs(x-rounded)<=1e-6)and np.all(rounded>=0)and np.all(rounded<=1))
    if valid:chosen=np.flatnonzero(rounded).tolist();actualpins=sorted(set(seed)|{reps[c]for c in chosen});valid=union(actualpins,pinmasks)==FULL
   solver_raw=dict(run_status=str(rs),model_status=str(ms),message=hs.modelStatusToString(ms),solver_CPU_seconds=scpu,
    value_valid=bool(s.value_valid),actual_wholecurrent_handcheck=valid,handchecked_extra_count=len(chosen)if valid else None)
   for key in ['objective_function_value','mip_node_count','mip_dual_bound','mip_gap','num_primal_infeasibilities']:solver_raw[key]=clean(getattr(info,key,None))
   save('RAW_RESIDUAL_SOLUTION.json',dict(**solver_raw,col_values=[clean(float(v))for v in x],
    handchecked_actual_pin_labels=actualpins if valid else None))
   if valid and len(actualpins)<len(bestpins):bestpins=actualpins
   if valid and len(actualpins)<=16:winner=actualpins
  else:solver_raw=dict(status='NOT_STARTED_CPU_LEFT_INSUFFICIENT_NO_RETRY')
 result=dict(status='UNKNOWN_NO_AT_MOST16_SOURCE_SEEDED_COVER_FOUND',actual_template_domain=len(templates),
  templates_greedy_processed=len(records),best_total_pin_count=len(bestpins),best_actual_pins=bestpins,
  best_actual_wholecurrent_union_count=union(bestpins,pinmasks).bit_count(),
  frozen_template_v=frozen['source_center_v'],solver_calls=solver_calls,solver_raw=solver_raw,
  source_current_graph_input_parses=1,new_balls=0,old_sourceD4_BFS_field_Lean_ARIS=0,
  newroot_route_BFS=0,candidate_graphs_generated=0,new_graph_parameter_Lean_counts=[0,0,0],
  scope='allactual4-blockedslotunselectedsourceNvseeds+onegreedy each,onefrozenresidualwindow;notfullfamilyNO',
  next='STOP finalCcase,no secondv/seed/solver')
 if winner is not None:
  phase='POSITIVE_GRAPH_AND_ROUTES';budget();chosen=sorted(set(winner));assert len(chosen)<=16 and all(degree[p]<16 for p in chosen)
  assert union(chosen,pinmasks)==FULL
  d=[-1]*N;parent=[-1]*N;q=[]
  for p in chosen:d[p]=0;parent[p]=p;q.append(p)
  for v in q:
   if d[v]>=3:continue
   for w in adj[v]:
    if d[w]<0:d[w]=d[v]+1;parent[w]=v;q.append(w)
  assert len(q)==N and max(d)<=3
  with(HERE/'NEWROOT_ROUTES.tsv').open('w',newline='')as f:
   out=csv.writer(f,delimiter='\t');out.writerow(['actual_oldtarget','newroot_distance','actual_route'])
   for v in range(N):
    rev=[v]
    while d[rev[-1]]:rev.append(parent[rev[-1]])
    route=[N]+list(reversed(rev));out.writerow([v,len(route)-1,','.join(map(str,route))])
  save('NEWROOT_PARENT_DEPTH.json',dict(pins=chosen,parent=parent,depth=d,maxdepth=max(d),allcurrent_targets=N,new_label=N))
  graph=HERE/'graph_d16_D4_n16417.edges'
  with graph.open('w')as f:
   f.write(f'{N+1} {129240+len(chosen)}\n')
   for u,v in edges:f.write(f'{u} {v}\n')
   for p in chosen:f.write(f'{p} {N}\n')
  degs=[degree[v]+int(v in set(chosen))for v in range(N)]+[len(chosen)];assert max(degs)<=16
  save('PIN_SET.json',dict(actual_pin_labels=chosen,count=len(chosen),current_degrees=[degree[p]for p in chosen],
   actual_wholecurrent_closedR3_cover=16416,allavailable=True))
  save('PARAMETERS.json',dict(n=N+1,m=129240+len(chosen),maxdegree=16,degree_histogram=dict(collections.Counter(degs)),
   source_current_graph=str((PLANE/'graph_d16_D4_n16416.edges').relative_to(ROOT)),all129240oldedges_preserved=True,
   newZ_label=N,pin_labels=chosen,sourceguided_template_v=frozen['source_center_v'],
   trueD4_interface='inheritedoldD4+actualcurrentR3cover+oneedge',exactD4_lower='16417>Moore16D3=3857',
   fresh_acceptance='PENDING_ROOT',new_graph_parameter_Lean_counts=[0,0,0]))
  result.update(status='FOUND_SOURCE_SEEDED_AT_MOST16_COVER_16417_PENDING_FRESH_ACCEPTANCE',candidate_graphs_generated=1,
   actual_pin_labels=chosen,candidate_n=N+1,candidate_m=129240+len(chosen),newroot_route_BFS=1)
 save('CHILD_RESULT.json',result);checkpoint('CHILD_TERMINAL',status=result['status'],best_total=len(bestpins))
if __name__=='__main__':
 try:main()
 except Exception as e:
  save('CHILD_RESULT.json',dict(status='UNKNOWN_SOURCE_SEEDED_PROCESS_OR_BUDGET_FAILURE',phase=phase,first_unfinished_prefix=prefix,
   error=str(e),traceback=traceback.format_exc(),candidate_graphs_generated=0,new_graph_parameter_Lean_counts=[0,0,0],next='STOP noautomaticretry'))
  raise
