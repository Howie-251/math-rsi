"""One finite five-case exact-cover batch using only verified hypergraph symmetry."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
 os.environ[name]='1'
import resource,time,json,sys,warnings
from pathlib import Path
from datetime import datetime,timezone
resource.setrlimit(resource.RLIMIT_CPU,(120,120))
start=time.process_time();wall=time.perf_counter()
HERE=Path(__file__).resolve().parent;EXACT=HERE.parent;BASE=EXACT.parent;ROOT=HERE.parents[5]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen

def save(path,value):
 def texts(x):
  if isinstance(x,str):return[x]
  if isinstance(x,dict):return[s for z in x.values() for s in texts(z)]
  if isinstance(x,(tuple,list)):return[s for z in x for s in texts(z)]
  return[]
 assert not screen('\n'.join(texts(value)))
 path.write_text(json.dumps(value,indent=2)+'\n')
assert not (HERE/'terminal.json').exists(),'This finite batch already has a terminal file'
save(HERE/'PREDICTION.json',dict(status='FROZEN_BEFORE_SOLVERS',timestamp=datetime.now(timezone.utc).isoformat(),
 hypothesis='Verified five-orbit symmetry may make some exact10-pin branch tractable; feasibility remains open until checked.',
 source_n=33397,target_n=33398,target_Delta=10,target_D=5,processing_order=[4,3,2,1,0],
 reason='Most excluded columns first; original lossless branch conditions unchanged.',
 scope='Exactly the five verified-orbit cases; no extra fixed pin or assumed group symmetry.',
 budgets='One worker, hard120CPU total, production soft113CPU, each case at most about25CPU; at most one LP and one MIP per case, first complete incumbent stops.'))
import numpy as np
from scipy.optimize import linprog,milp,Bounds,LinearConstraint
from scipy.sparse import csr_matrix,vstack
meta=json.loads((EXACT/'model.json').read_text());pins=meta['pins'];C=364;N=33397;R=26117
assert len(pins)==C and meta['source_n']==N and meta['unique_cover_rows']==R
raw=(EXACT/'unique_cover_rows.u8.bin').read_bytes();assert len(raw)==R*46
U=np.unpackbits(np.frombuffer(raw,dtype=np.uint8).reshape(R,46),axis=1,bitorder='little')[:,:C]
assert np.all(U.sum(axis=1)>0)
cases=json.loads((EXACT/'symmetry_g2_root/orbit_cases.json').read_text())['cases'];assert len(cases)==5
results=[];hit=None
save(HERE/'terminal.json',dict(status='RUNNING_FIVE_CASE_BATCH',completed_cases=[],MIP_calls=0,incumbent=False))

def check_hit(selected,caseid):
 global hit
 selected=sorted(map(int,selected));assert len(selected)<=10 and len(set(selected))==len(selected)
 # Independent recheck against all33397 targets in the original364-ball matrix.
 W=(N+63)//64;fullraw=(BASE/'degree10_radius4.u64.bin').read_bytes();assert len(fullraw)==C*W*8
 union=0
 for c in selected:union |= int.from_bytes(fullraw[c*W*8:(c+1)*W*8],'little')
 assert (union&((1<<N)-1))==((1<<N)-1)
 deg=[0]*N
 with (BASE/'degree10_source.edges').open() as f:
  n,m=map(int,next(f).split());assert (n,m)==(N,166425)
  for line in f:
   u,v=map(int,line.split());deg[u]+=1;deg[v]+=1
 chosen=[pins[c] for c in selected];assert all(deg[p]<10 for p in chosen)
 hit=dict(case=caseid,selected_columns=selected,pins=chosen,source_n=N,target_n=N+1,new_vertex=N,
   new_vertex_degree=len(chosen),old_pin_degrees=[deg[p] for p in chosen],source_edges_retained=True,
   all33397_original_R4_targets_covered=True,missing_targets=[],source_file=str((BASE/'degree10_source.edges').relative_to(ROOT)),
   independent_cover_recheck='Original364candidate by33397target bounded-radius matrix; not reduced model alone.',
   graph_generated=False,root_fullgraph_verification_pending=True)
 save(HERE/'hit.json',hit)
 print('HIT '+json.dumps(hit),flush=True)

for caseid in [4,3,2,1,0]:
 if time.process_time()-start>109:
  results.append(dict(case=caseid,status='NOT_STARTED_TOTAL_WINDOW',incumbent=False));continue
 tcase=time.process_time();case=cases[caseid];out=HERE/f'case{caseid}';out.mkdir(exist_ok=True)
 zeros=set(case['all_earlier_orbit_columns_fixed_zero']);ones={case['representative_column_fixed_one']};assert not(zeros&ones)
 forced=[];reason=None;active_rows=np.arange(R);free=np.array([],dtype=int);B=None
 while True:
  if len(ones)>10:reason='MORE_THAN10_FORCED_PINS';break
  covered=U[:,sorted(ones)].any(axis=1)
  active_rows=np.flatnonzero(~covered)
  if not len(active_rows):B=np.empty((0,0),dtype=np.uint8);free=np.array([],dtype=int);break
  free=np.array(sorted(set(range(C))-zeros-ones),dtype=int)
  B=U[np.ix_(active_rows,free)]
  sizes=B.sum(axis=1);empty=np.flatnonzero(sizes==0)
  if len(empty):reason='UNCOVERED_ROW_WITH_NO_ALLOWED_COLUMN';emptyrow=int(active_rows[empty[0]]);break
  singles=np.flatnonzero(sizes==1)
  newones={int(free[np.flatnonzero(B[j])[0]]) for j in singles}
  if not newones:break
  for c in sorted(newones):
   jr=next(int(j) for j in singles if B[j,np.searchsorted(free,c)])
   forced.append(dict(column=c,pin=pins[c],because_original_unique_row=int(active_rows[jr])))
  ones |= newones
 if reason:
  res=dict(case=caseid,status='EXACT_PREPROCESS_INFEASIBLE',reason=reason,
    empty_original_unique_row=emptyrow if reason=='UNCOVERED_ROW_WITH_NO_ALLOWED_COLUMN' else None,
    initial_zero_columns=sorted(zeros),selected_columns=sorted(ones),singleton_forcing=forced,
    CPU_seconds=time.process_time()-tcase,LP_calls=0,MIP_calls=0,incumbent=False)
  save(out/'RESULT.json',res);results.append(res);print('CASE '+json.dumps({k:v for k,v in res.items() if k not in ['initial_zero_columns','selected_columns','singleton_forcing']}),flush=True);continue
 if not len(active_rows):
  check_hit(ones,caseid);res=dict(case=caseid,status='EXACT_PREPROCESS_FEASIBLE',incumbent=True,LP_calls=0,MIP_calls=0,CPU_seconds=time.process_time()-tcase);save(out/'RESULT.json',res);results.append(res);break
 # Variables with no coefficient can be set0 without loss for a <= cardinality model.
 useful=B.any(axis=0);dropped=free[~useful].tolist();free=free[useful];B=B[:,useful]
 packed=np.packbits(B,axis=1,bitorder='little');unique,idx=np.unique(packed,axis=0,return_index=True)
 redU=np.unpackbits(unique,axis=1,bitorder='little')[:,:len(free)];redrows=active_rows[idx];A=csr_matrix(redU,dtype=float)
 (out/'rows.u8.bin').write_bytes(unique.tobytes())
 remaining=10-len(ones)
 model=dict(case=caseid,initial_fixed_zero_columns=sorted(zeros),fixed_one_columns=sorted(ones),
 singleton_forcing=forced,inactive_columns_fixed_zero=dropped,free_columns=free.tolist(),free_pin_vertices=[pins[i] for i in free],
 original_remaining_rows=len(active_rows),deduplicated_remaining_rows=len(redrows),row_bytes=unique.shape[1],
 row_layout='Little bitorder over free_columns',representative_original_unique_rows=redrows.tolist(),remaining_pin_cap=remaining,
 row_file='rows.u8.bin',equivalence='Satisfied rows removed; fixed columns substituted; singleton rows force their only available variable; zero columns may be omitted under an upper cardinality bound; equal rows deduplicated.')
 save(out/'model.json',model)
 elapsed=time.process_time()-start;remaining_cases=5-len(results);allocation=min(25.,max(1.,(113.-elapsed)/remaining_cases))
 case_deadline=min(tcase+allocation,start+113.)
 lp_limit=max(.05,min(8.,case_deadline-time.process_time()-2.5));t=time.process_time()
 with warnings.catch_warnings(record=True) as warns:
  warnings.simplefilter('always')
  lp=linprog(np.ones(len(free)),A_ub=-A,b_ub=-np.ones(len(redrows)),bounds=(0,None),method='highs',options={'time_limit':lp_limit,'threads':1})
 lpdata=dict(status=int(lp.status),message=str(lp.message),remaining_objective=None if lp.fun is None else float(lp.fun),
 total_objective=None if lp.fun is None else len(ones)+float(lp.fun),CPU_seconds=time.process_time()-t,time_limit=lp_limit,
 warnings=[str(w.message) for w in warns])
 save(out/'LP_result.json',lpdata)
 strict=False
 if lp.status==0:
  weights=np.floor(np.maximum(0,-lp.ineqlin.marginals)*1000000).astype(np.int64)
  loads=np.asarray(A.T@weights).reshape(-1).astype(np.int64);den=max(1000000,int(loads.max(initial=0)));total=int(weights.sum());strict=total>remaining*den
  if strict:
   save(out/'integer_dual.json',dict(denominator=den,total_row_weight=total,fixed_one_count=len(ones),remaining_pin_cap=remaining,
     strictly_excludes_remaining_cap=True,weighted_reduced_rows=[[int(i),int(w)] for i,w in enumerate(weights) if w],per_free_column_loads=loads.tolist(),
     proof='For every remaining cover sumweights<=sum(columnload*x)<=denominator*sum(x). The displayed integers exceed the remaining cap.'))
 if strict:
  status='EXACT_INTEGER_DUAL_INFEASIBLE';mr=None
 elif lp.status==2:
  status='RAW_LP_INFEASIBLE_NO_TRUSTED_CERTIFICATE';mr=None
 elif lp.status!=0:
  status='LP_UNKNOWN_NO_MIP';mr=None
 elif lp.fun>remaining+1e-7:
  status='FLOAT_LP_BOUND_EXCLUDES_NO_INTEGER_CERTIFICATE';mr=None
 elif case_deadline-time.process_time()<1.5:
  status='NO_MIP_CASE_WINDOW';mr=None
 else:
  limit=max(.1,case_deadline-time.process_time()-2.);M=vstack([A,np.ones((1,len(free)))],format='csc');t=time.process_time()
  save(HERE/'terminal.json',dict(status='RUNNING_CASE_MIP',case=caseid,completed_cases=[x['case'] for x in results],incumbent=False))
  print('START_MIP '+json.dumps(dict(case=caseid,LP_total=lpdata['total_objective'],time_limit=limit,free_columns=len(free),rows=len(redrows))),flush=True)
  with warnings.catch_warnings(record=True) as warns:
   warnings.simplefilter('always')
   ans=milp(np.zeros(len(free)),integrality=np.ones(len(free)),bounds=Bounds(0,1),
      constraints=LinearConstraint(M,np.r_[np.ones(len(redrows)),-np.inf],np.r_[np.full(len(redrows),np.inf),remaining]),
      options={'threads':1,'time_limit':limit,'presolve':True,'disp':False})
  mr=dict(status=int(ans.status),message=str(ans.message),CPU_seconds=time.process_time()-t,time_limit=limit,
     incumbent=ans.x is not None,node_count=getattr(ans,'mip_node_count',None),dual_bound=getattr(ans,'mip_dual_bound',None),
     warnings=[str(w.message) for w in warns]);save(out/'MIP_result.json',mr)
  if ans.x is not None:
   x=np.rint(ans.x).astype(int);assert np.max(abs(ans.x-x))<1e-5 and np.all((x==0)|(x==1))
   assert np.all(A@x>=1) and x.sum()<=remaining
   check_hit(ones|set(free[np.flatnonzero(x)].tolist()),caseid);status='FEASIBLE_FULL_COVER_VERIFIED_AWAIT_ROOT'
  else:status='RAW_MIP_INFEASIBLE_NO_TRUSTED_CERTIFICATE' if ans.status==2 else 'MIP_UNKNOWN_NO_INCUMBENT'
 res=dict(case=caseid,status=status,LP=lpdata,LP_calls=1,MIP_calls=int(mr is not None),MIP=mr,incumbent=hit is not None,
   initial_zero_count=len(zeros),fixed_one_count=len(ones),free_columns=len(free),reduced_rows=len(redrows),
   case_CPU_seconds=time.process_time()-tcase)
 save(out/'RESULT.json',res);results.append(res);print('CASE '+json.dumps(res),flush=True)
 if hit is not None:break
final=dict(status='FEASIBLE_FULL_COVER_FOUND_AWAIT_ROOT' if hit is not None else 'FIVE_CASE_BATCH_FINISHED_NO_INCUMBENT',
 incumbent=hit is not None,pins=None if hit is None else hit['pins'],cases=results,
 LP_calls=sum(r['LP_calls'] for r in results),MIP_calls=sum(r['MIP_calls'] for r in results),
 all_five_cases_processed=len(results)==5,whole_family_excluded=False,
 scope='Only this one authorized batch of the five proven symmetry cases; any UNKNOWN case leaves whole-family feasibility open.',
 total_CPU_seconds=time.process_time()-start,total_wall_seconds=time.perf_counter()-wall,
 workers=1,solver_threads=1,new_BFS=0,new_graphs=0)
save(HERE/'RESULT.json',final);save(HERE/'terminal.json',final);print('FINAL '+json.dumps(final),flush=True)
