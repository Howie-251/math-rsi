#!/usr/bin/env python3
"""Exact current-R3 supports, one greedy and at most one warm HiGHS cover run."""
import time
START=time.process_time()
import argparse,array,collections,csv,json,math,os,resource,traceback
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if(p/'research-wiki').is_dir())
SOURCE=HERE.parent/'graph_d16_D4_n16416.edges'
N=16416;M=129240;BYTES=(N+7)//8
def save(name,x):(HERE/name).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
def checkpoint(stage,**kw):
 x=dict(stage=stage,pid=os.getpid(),child_CPU_sofar=time.process_time()-START,**kw)
 save('CHECKPOINT.json',x);print(json.dumps(x),flush=True)
def clean(v):
 if isinstance(v,(bool,int,str))or v is None:return v
 if isinstance(v,float):return v if math.isfinite(v)else str(v)
 return str(v)
def union_for(chosen,masks):
 u=0
 for c in chosen:u|=masks[c]
 return u
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--hard-cpu',type=int,required=True);args=ap.parse_args()
 resource.setrlimit(resource.RLIMIT_CPU,(args.hard_cpu,args.hard_cpu))
 for name in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
  assert os.environ.get(name)=='1'
 checkpoint('PARSING_ACCEPTED_CURRENT_GRAPH_ONCE')
 adj=[[]for _ in range(N)];edges=[]
 with SOURCE.open()as f:
  assert tuple(map(int,next(f).split()))==(N,M)
  for line in f:
   if not line.strip():continue
   u,v=map(int,line.split());assert 0<=u<N and 0<=v<N and u!=v
   adj[u].append(v);adj[v].append(u);edges.append((u,v))
 assert len(edges)==M
 degree=list(map(len,adj));dh=collections.Counter(degree)
 assert dh=={14:126,15:3924,16:12366}
 pins=[v for v,d in enumerate(degree)if d<16];assert len(pins)==4050
 save('ALL_AVAILABLE_PINS.json',dict(current_graph=str(SOURCE.relative_to(ROOT)),current_n=N,current_m=M,
  available_actual_pin_labels=pins,available_current_degree_histogram=dict(sorted(collections.Counter(degree[v]for v in pins).items())),
  original15552_pin_count=sum(v<15552 for v in pins),current_clone_pin_count=sum(v>=15552 for v in pins),
  eligibility='currentdegree<16;bothoriginalandclones',source_literal_parse_count=1,
  old_D4_validity_BFS=0))
 masks=[];targets=[];seen=[0]*N;sizes=collections.Counter();all_union=0
 with(HERE/'ALL4050_CLOSED_R3_SUPPORTS.bits').open('wb')as bf,(HERE/'ALL4050_PIN_SUPPORT_PROFILE.tsv').open('w',newline='')as pf:
  out=csv.writer(pf,delimiter='\t');out.writerow(['pin_index','actual_pin_label','current_degree','current_role','closed_R3_size','byte_offset'])
  for i,pin in enumerate(pins):
   stamp=i+1;q=[pin];seen[pin]=stamp;lo=0;hi=1
   for depth in range(3):
    for j in range(lo,hi):
     for w in adj[q[j]]:
      if seen[w]!=stamp:seen[w]=stamp;q.append(w)
    lo=hi;hi=len(q)
   raw=bytearray(BYTES)
   for w in q:raw[w>>3]|=1<<(w&7)
   mask=int.from_bytes(raw,'little');assert mask.bit_count()==len(q)
   masks.append(mask);targets.append(array.array('I',q));sizes[len(q)]+=1;all_union|=mask
   bf.write(raw);out.writerow([i,pin,degree[pin],'original15552'if pin<15552 else'current_clone',len(q),i*BYTES])
   if(i+1)%512==0:checkpoint('EXACT_CURRENT_DEPTH3_SUPPORTS',roots_completed=i+1,roots_total=len(pins))
 full=(1<<N)-1
 save('SUPPORT_SCHEMA.json',dict(current_targets=N,eligible_pin_roots=len(pins),depth=3,
  bitset_file='ALL4050_CLOSED_R3_SUPPORTS.bits',bytes_per_row=BYTES,byte_order='little',
  target_bit_to_actual_label='identity0..16415',row_to_pin='ALL4050_PIN_SUPPORT_PROFILE.tsv',
  closed_ball=True,current_clone_targets_included=True,current_graph_parses=1,
  old_D4_validity_BFS=0,ordinary_allroot_validation=0,
  depth3_support_size_histogram=dict(sorted(sizes.items())),all_available_union_size=all_union.bit_count()))
 # Identical exact cover columns can use the leastactual availablepin, cost1 each.
 bymask={};unique=[];groups=[];raw_to_unique={}
 for i,mask in enumerate(masks):
  if mask not in bymask:bymask[mask]=len(unique);unique.append(i);groups.append([])
  c=bymask[mask];groups[c].append(pins[i]);raw_to_unique[i]=c
 umasks=[masks[i]for i in unique];ureps=[pins[i]for i in unique]
 save('COVER_COLUMN_MAPPING.json',dict(all_available_pins=4050,unique_columns=len(unique),
  representatives=ureps,columns=[dict(column=c,actual_representative=ureps[c],equivalent_actual_pins=g)for c,g in enumerate(groups)],
  justification='identicalclosedR3sets,cost1,currentdegreeeligible;duplicatechoicescannotimprovecover'))
 checkpoint('SUPPORTS_COMPLETE_GREEDY_START',eligible_pin_roots=4050,unique_columns=len(unique),all_available_union=all_union.bit_count())
 chosen=[];uncovered=full;steps=[]
 while uncovered:
  best=-1;gain=0
  for c,mask in enumerate(umasks):
   g=(mask&uncovered).bit_count()
   if g>gain:best=c;gain=g
  if best<0:break
  chosen.append(best);uncovered&=~umasks[best]
  steps.append(dict(actual_pin=ureps[best],gain=gain,remaining_targets=uncovered.bit_count()))
 before=chosen.copy();deleted=[]
 for c in reversed(before):
  trial=[j for j in chosen if j!=c]
  if union_for(trial,umasks)==full:chosen=trial;deleted.append(ureps[c])
 greedy=chosen.copy();greedy_cover=union_for(greedy,umasks)
 assert not uncovered or all_union!=full
 save('GREEDY_RESULT.json',dict(algorithm='one max-uncovered-gain pass,lexactualpin tie,one reverse redundantdeletionpass',
  before_redundancy_count=len(before),after_redundancy_count=len(greedy),actual_selected_pins=[ureps[c]for c in greedy],
  deleted_actual_pins=deleted,steps=steps,whole_current_coverage=greedy_cover.bit_count(),
  full_cover=greedy_cover==full,unique_column_domain=len(unique),all_available_domain=4050))
 checkpoint('GREEDY_COMPLETE',greedy_count=len(greedy),greedy_fullcover=greedy_cover==full)
 best=greedy.copy();solver_raw=None;solver_calls=0
 if greedy_cover==full and len(greedy)>16:
  # The only solver window: preserve current all16416 row universe.
  (HERE/'SOLVER_PRED.md').write_text('# Sole warm cover solve\n\nGreedy count '+str(len(greedy))+
   ' is an actual full-current-graph cover. Test whether this full4050-available-pin domain admits<=16 via one minsum binaryHiGHS window, warmstarting that cover. '+
   'All16416targets remain. Duplicate coverage columns only are quotiented with actualmapping. No new source parse, balls, seed or secondsolve. Best>16/rawNo/timeout stays no-hitUNKNOWN, notstrictNO.\n')
  checkpoint('IMPORTING_EXISTING_SINGLE_THREAD_HIGHS')
  import numpy as np
  import scipy.optimize._highspy._core as h
  p=len(unique);lengths=np.array([len(targets[i])for i in unique],dtype=np.int32)
  start=np.zeros(p+1,dtype=np.int32);np.cumsum(lengths,out=start[1:])
  indices=np.empty(int(start[-1]),dtype=np.int32)
  for c,rawi in enumerate(unique):indices[start[c]:start[c+1]]=np.frombuffer(targets[rawi],dtype=np.uint32)
  values=np.ones(indices.size,dtype=np.float64);warm=np.zeros(p,dtype=np.float64);warm[greedy]=1
  warm_rows=np.zeros(N,dtype=np.int32)
  for c in greedy:warm_rows[np.frombuffer(targets[unique[c]],dtype=np.uint32)]+=1
  assert bool(np.all(warm_rows>=1))
  lp=h.HighsLp();lp.num_col_=p;lp.num_row_=N
  lp.col_cost_=np.ones(p,dtype=np.float64);lp.col_lower_=np.zeros(p,dtype=np.float64);lp.col_upper_=np.ones(p,dtype=np.float64)
  lp.row_lower_=np.ones(N,dtype=np.float64);lp.row_upper_=np.full(N,h.kHighsInf,dtype=np.float64)
  lp.integrality_=[h.HighsVarType.kInteger]*p
  lp.a_matrix_.num_col_=p;lp.a_matrix_.num_row_=N;lp.a_matrix_.format_=h.MatrixFormat.kColwise
  lp.a_matrix_.start_=start;lp.a_matrix_.index_=indices;lp.a_matrix_.value_=values
  highs=h._Highs();assert highs.setOptionValue('threads',1)==h.HighsStatus.kOk
  pass_status=highs.passModel(lp);save('PASS_MODEL_RETURN.json',dict(status=str(pass_status)))
  assert pass_status==h.HighsStatus.kOk
  sol=h.HighsSolution();sol.col_value=warm.tolist();sol.row_value=warm_rows.astype(np.float64).tolist();sol.value_valid=True;sol.dual_valid=False
  warm_status=highs.setSolution(sol);save('WARM_START_RETURN.json',dict(status=str(warm_status),actual_pin_count=len(greedy),all16416rows_handchecked=True))
  assert warm_status==h.HighsStatus.kOk
  window=min(30.0,44.0-(time.process_time()-START))
  save('MODEL.json',dict(variables=p,all_actual_available_pins=4050,rows=N,nonzeros=int(indices.size),
   model='binaryminsum,exactcurrentclosedR3column,allcurrenttargetsrowlower1',
   no_oldgraph_subset_ignored=True,duplicate_column_actualmapping='COVER_COLUMN_MAPPING.json',
   threads=1,time_limit=max(0,window),warm_start_count=len(greedy),solver_calls_planned=1))
  if window>0:
   assert highs.setOptionValue('time_limit',window)==h.HighsStatus.kOk
   checkpoint('SOLE_HIGHS_COVER_RUN_ACTIVE',window_seconds=window,variables=p,rows=N,nnz=int(indices.size))
   solver_calls=1;ts=time.process_time();rs=highs.run();run_cpu=time.process_time()-ts
   info=highs.getInfo();ms=highs.getModelStatus();soln=highs.getSolution()
   solver_raw=dict(run_status=str(rs),model_status=str(ms),model_status_message=highs.modelStatusToString(ms),
    solver_CPU_seconds=run_cpu,value_valid=bool(soln.value_valid),window_seconds=window)
   for key in ['objective_function_value','mip_node_count','mip_dual_bound','mip_gap','primal_solution_status','num_primal_infeasibilities']:
    solver_raw[key]=clean(getattr(info,key,None))
   x=np.asarray(soln.col_value,dtype=np.float64);valid=bool(soln.value_valid)and x.size==p
   selected=[]
   if valid:
    rounded=np.rint(x).astype(np.int32);valid=bool(np.all(np.abs(x-rounded)<=1e-6)and np.all(rounded>=0)and np.all(rounded<=1))
    if valid:selected=np.flatnonzero(rounded).tolist();valid=union_for(selected,umasks)==full
   solver_raw['best_binary_actual_whole_union_handcheck']=valid
   solver_raw['handchecked_count']=len(selected)if valid else None
   save('RAW_SOLUTION.json',dict(**solver_raw,col_values=[clean(float(v))for v in x],
    handchecked_actual_pins=[ureps[c]for c in selected]if valid else None))
   if valid and len(selected)<len(best):best=selected
  else:solver_raw=dict(status='NOT_STARTED_INSUFFICIENT_CPU_LEFT_NO_RETRY')
 bestmask=union_for(best,umasks);bestpins=sorted(ureps[c]for c in best)
 save('BEST_COVER_PIN_SET.json',dict(actual_pin_labels=bestpins,count=len(bestpins),covered_current_targets=bestmask.bit_count(),
  full_current_cover=bestmask==full,maximum_allowed_for_extension=16,not_a_graph_if_count_above16=True))
 result=dict(status='UNKNOWN_NO_AT_MOST16_PIN_COVER_FOUND',current_graph=str(SOURCE.relative_to(ROOT)),
  current_n=N,current_m=M,current_graph_parses=1,available_pins=4050,exact_depth3_support_roots=4050,
  current_alltarget_universe=N,current_clone_targets_included=864,unique_support_columns=len(unique),
  greedy_count=len(greedy),best_handchecked_cover_count=len(bestpins),best_handchecked_cover_alltargets=(bestmask==full),
  solver_calls=solver_calls,solver_raw=solver_raw,new_graphs=0,new_graph_parameter_Lean_counts=[0,0,0],
  old_source_D4_validation_BFS_allroots_field_Lean_ARIS=0,newroot_route_multisource_BFS=0,
  scope='fixedaccepted16416,allcurrentdegree<16pins,exactclosedR3;onegreedy+onewarmcoverwindow',
  full_family_NO_claim=False,next='STOP no seed/secondsolve/repeatoldBFS')
 if bestmask==full and len(bestpins)<=16:
  assert len(bestpins)==len(set(bestpins))and all(degree[v]<16 for v in bestpins)
  checkpoint('FOUND_AT_MOST16_ACTUAL_COVER_WRITING_NEWROOT_ROUTES',pin_count=len(bestpins))
  # One new-root certificate, not an oldsourceD4 validation.
  depth=[-1]*N;parent=[-1]*N;q=[]
  for pin in bestpins:depth[pin]=0;parent[pin]=pin;q.append(pin)
  for v in q:
   if depth[v]>=3:continue
   for w in adj[v]:
    if depth[w]<0:depth[w]=depth[v]+1;parent[w]=v;q.append(w)
  assert len(q)==N and max(depth)<=3
  with(HERE/'NEWROOT_ALL16416_ROUTES.tsv').open('w',newline='')as f:
   out=csv.writer(f,delimiter='\t');out.writerow(['current_target_label','newroot_distance','actual_route'])
   for v in range(N):
    rev=[v]
    while depth[rev[-1]]>0:rev.append(parent[rev[-1]])
    route=[N]+list(reversed(rev));assert len(route)-1<=4
    out.writerow([v,len(route)-1,','.join(map(str,route))])
  save('NEWROOT_PARENT_DEPTH.json',dict(current_n=N,new_label=N,pins=bestpins,parent=parent,depth=depth,
   parent_scope='currentacceptedgrapholdedges;rootdepth0ispin,nonrootparentedgeanddepthdecrement',
   max_oldleg_depth=max(depth),all16416_current_targets_reached=True))
  graph=HERE/'graph_d16_D4_n16417.edges'
  with graph.open('w')as f:
   f.write(f'{N+1} {M+len(bestpins)}\n')
   for u,v in edges:f.write(f'{u} {v}\n')
   for pin in bestpins:f.write(f'{pin} {N}\n')
  newdegree=[degree[v]+int(v in set(bestpins))for v in range(N)]+[len(bestpins)]
  assert max(newdegree)<=16
  save('PIN_SET.json',dict(current_actual_pin_labels=bestpins,pin_current_degrees=[degree[v]for v in bestpins],
   pin_current_roles=['original15552'if v<15552 else'current_clone'for v in bestpins],
   pin_count=len(bestpins),actual_closedR3_union_bitset_hex=hex(bestmask),covered_current_targets=N,
   new_label=N,current_alltargets_verified=True))
  save('PARAMETERS.json',dict(source_current_graph=str(SOURCE.relative_to(ROOT)),source_n=N,source_m=M,
   graph=str(graph.relative_to(ROOT)),n=N+1,m=M+len(bestpins),max_degree=16,pin_labels=bestpins,
   all16416_old_vertices_and129240_edges_preserved=True,added_edges=len(bestpins),newpoint_label=N,
   newpoint_neighbourhood=bestpins,degree_histogram=dict(sorted(collections.Counter(newdegree).items())),
   current_source_D4='INHERITED_ACCEPTED_NOT_REVALIDATED',newold_D4='currentclosedR3coverplusoneedge',
   exactD4_lower='16417>Moore(16,3)=3857;notreuseoldnonD3witness',fresh_acceptance='PENDING_ROOT',
   new_graph_parameter_Lean_counts=[0,0,0]))
  result.update(status='FOUND_AT_MOST16_PIN_COVER_16417_CANDIDATE_PENDING_FRESH_ACCEPTANCE',new_graphs=1,
   candidate_n=N+1,candidate_m=M+len(bestpins),actual_pin_labels=bestpins,newroot_route_multisource_BFS=1,
   all_current_old_edges_preserved=M,fresh_acceptance='PENDING_ROOT')
 result['actual_child_process_CPU_seconds_sofar']=time.process_time()-START
 save('CHILD_RESULT.json',result);checkpoint('CHILD_TERMINAL',status=result['status'],best_pin_count=len(bestpins))
if __name__=='__main__':
 try:main()
 except Exception as e:
  save('CHILD_RESULT.json',dict(status='UNKNOWN_PROCESS_OR_INPUT_FAILURE_NO_RETRY',error=str(e),traceback=traceback.format_exc(),
   actual_child_process_CPU_seconds_sofar=time.process_time()-START,new_graphs=0,new_graph_parameter_Lean_counts=[0,0,0],
   old_source_D4_validation_BFS_field_Lean_ARIS=0,next='STOP preservefailureandCPU'))
  raise
