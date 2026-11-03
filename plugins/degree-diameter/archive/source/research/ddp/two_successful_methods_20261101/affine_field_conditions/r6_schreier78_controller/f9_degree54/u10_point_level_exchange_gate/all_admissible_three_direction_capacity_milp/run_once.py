import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[name]='1'
import time
START=time.process_time();WALL=time.time()
import resource
resource.setrlimit(resource.RLIMIT_CPU,(20,21))
import itertools,json,math,warnings
from pathlib import Path
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
D=Path(__file__).resolve().parent;BASE=D.parents[1]
P=json.loads((BASE/'PARAMETERS.json').read_text());CTRL=P['controller'];NB=list(map(set,CTRL))
interface=json.loads((D.parent/'fixed_support_max_capacity_lp/ALL_ADMISSIBLE_AFFINE_INTERFACE.json').read_text())
RET=interface['retained'];U=interface['all_admissible'];n=len(U);index={u:i for i,u in enumerate(U)}
assert RET==[31,59,60,72] and n==15 and 64 in U and 71 in U
triples=[]
for target in range(78):
 for sources in itertools.combinations([u for u in U if target in NB[u]],3):
  darts=[]
  for u in sources:
   p=CTRL[u].index(target);q=P['inverse_ports'][p]
   darts.append(dict(source=u,source_port=p,target_port=q,chart_index=P['dart_chart_index'][u][p],noise_direction=P['directions'][q]))
  assert len({d['target_port'] for d in darts})==3
  triples.append(dict(target=target,sources=list(sources),actual_darts=darts,rank3='inherited accepted conic certificate, not recomputed'))
assert len(triples)==7
A=[];lo=[];hi=[]
for v in range(78):
 fixed=sum(81 for u in RET if v in NB[u]);assert fixed<=81
 row=[0]*(3*n)
 for u in U:row[index[u]]=int(v in NB[u])
 A.append(row);lo.append(-np.inf);hi.append(81-fixed)
for j,u in enumerate(U):
 for sw,coefficient,lower,upper in [(n+j,-81,-np.inf,0),(n+j,-1,0,np.inf),(2*n+j,-61,-np.inf,20),(2*n+j,-21,0,np.inf)]:
  row=[0]*(3*n);row[j]=1;row[sw]=coefficient;A.append(row);lo.append(lower);hi.append(upper)
for tr in triples:
 row=[0]*(3*n)
 for u in tr['sources']:row[index[u]]=1;row[n+index[u]]=8
 A.append(row);lo.append(-np.inf);hi.append(97)
 row=[0]*(3*n)
 for u in tr['sources']:row[2*n+index[u]]=1
 A.append(row);lo.append(-np.inf);hi.append(2)
model=dict(scope='count necessarymodel for arbitrary centerpointsets, fixedretained4; noWrestriction',retained=RET,all_admissible=U,
 variables=3*n,integer_weights=n,binary_positive_indicators=n,binary_large_indicators=n,
 target_capacity_rows=78,actual_rank3_triples=triples,rows=len(A),
 constraints=['w<=81y','w>=y','w<=20+61z','w>=21z','triple sumw+8sumy<=97','triple sumz<=2'],
 objective='maximize324+sumw',threads=1,time_limit_wall_seconds=16,total_CPU_budget=20,
 rank_revalidation=0,solver_calls=1,old_pointpool_MIP_restarted=False)
(D/'MODEL.json').write_text(json.dumps(model,indent=2)+'\n')
before=time.process_time()
with warnings.catch_warnings(record=True) as caught:
 warnings.simplefilter('always')
 sol=milp(c=np.r_[-np.ones(n),np.zeros(2*n)],integrality=np.ones(3*n),
  bounds=Bounds(np.zeros(3*n),np.r_[np.full(n,81),np.ones(2*n)]),
  constraints=LinearConstraint(np.array(A,dtype=float),np.array(lo),np.array(hi)),
  options={'time_limit':16.0,'threads':1,'presolve':True,'mip_rel_gap':0.0})
solvercpu=time.process_time()-before
def number(x):
 if x is None:return None
 v=float(x);return v if math.isfinite(v) else str(v)
dual=number(getattr(sol,'mip_dual_bound',None))
result=dict(status='UNKNOWN_BOUNDED_NECESSARY_COUNT_MODEL',scipy_status=int(sol.status),solver_message=sol.message,
 success=bool(sol.success),mip_dual_bound_min_objective=dual,
 total_center_solver_upper_bound=None if dual is None or isinstance(dual,str) else 324-dual,
 mip_gap=number(getattr(sol,'mip_gap',None)),mip_node_count=number(getattr(sol,'mip_node_count',None)),
 solver_CPU_seconds=solvercpu,solver_calls=1,actual_rank3_triples=triples,retained=RET,all_admissible=U,
 model_does_not_restrict_W_or_eta=True,actual_centerpacking_constructed=False,
 large_graph_reads_or_generation=0,BFS_runs=0,Lean_runs=0,field_or_allrank_checks=0,
 old_wholelayeropt_searches=0,new729pointpool_enumeration=0,
 warnings=[str(w.message) for w in caught])
if sol.x is not None:
 rounded=np.rint(sol.x).astype(int);assert np.max(np.abs(sol.x-rounded))<1e-6
 w=rounded[:n].tolist();y=rounded[n:2*n].tolist();z=rounded[2*n:].tolist()
 assert all(0<=a<=81 for a in w) and all(a in [0,1] for a in y+z)
 assert all(y[j]==int(w[j]>0) and z[j]==int(w[j]>=21) for j in range(n))
 weights={u:81 for u in RET};weights.update({u:w[index[u]] for u in U})
 targetloads=[sum(weights.get(u,0) for u in range(78) if v in NB[u]) for v in range(78)]
 assert max(targetloads)<=81
 triplechecks=[]
 profiles=[(a,b,c,b*c,a*(9-c),(9-a)*(9-b)) for a,b,c in itertools.product(range(1,9),repeat=3)]
 for tr in triples:
  counts=[weights[u] for u in tr['sources']]
  assert sum(counts)<=97-8*sum(int(v>0) for v in counts) and sum(v>=21 for v in counts)<=2
  row=dict(target=tr['target'],sources=tr['sources'],counts=counts,allpositive=all(counts))
  if all(counts):
   feasible=[p for p in profiles if all(counts[i]<=p[3+i] for i in range(3))]
   row.update(projection_profiles_checked=512,projection_support_feasible=bool(feasible),
    feasible_profile_count=len(feasible),first_profile=None if not feasible else dict(a=feasible[0][0],b=feasible[0][1],c=feasible[0][2],caps=list(feasible[0][3:])))
  else:row.update(projection_profiles_checked=0,projection_support_feasible=None,reason='threepositive512profilecheck not applicable tozero family')
  triplechecks.append(row)
 total=324+sum(w)
 result.update(status='OPTIMAL_NECESSARY_THREE_DIRECTION_COUNT_MODEL' if sol.status==0 else 'INCUMBENT_ONLY_NECESSARY_COUNT_MODEL',
  total_center_incumbent=total,residual_center_incumbent=sum(w),incumbent_above810=total>810,
  all_weights={str(u):weights.get(u,0) for u in range(78)},positive_weights={str(u):v for u,v in weights.items() if v},
  positive_indicator=y,large_indicator=z,exact_integer_model_feasibility_PASS=True,targetloads=targetloads,
  projection_profile_checks=triplechecks,unsupported_threeway_targets=[x['target'] for x in triplechecks if x['projection_support_feasible'] is False],
  no_further_solver_after_profile_check=True,upper_bound_le810_at_solver_scale=bool(isinstance(result['total_center_solver_upper_bound'],(int,float)) and result['total_center_solver_upper_bound']<=810+1e-6))
 (D/'WEIGHT_VECTOR.json').write_text(json.dumps(dict(total=total,weights=result['all_weights'],targetloads=targetloads,projection_profiles=triplechecks),indent=2)+'\n')
result['total_CPU_seconds']=time.process_time()-START;result['all_processes_terminal']=True
assert result['total_CPU_seconds']<20
(D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
terminal=dict(status=result['status'],single_worker=True,all_processes_terminal=True,
 total_CPU_seconds=time.process_time()-START,solver_CPU_seconds=solvercpu,wall_seconds=time.time()-WALL,
 CPU_budget_seconds=20,solver_calls=1,no_automatic_continuation=True,
 measurement_boundary='Single new necessarycountmodel, imports/actualtriplebinding/oneMIP/exactinteger and512scalarprofiles/aggregation. No pointpool or oldgraph checks; interactive authoring excluded.')
(D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(dict(terminal=terminal,result={k:v for k,v in result.items() if k not in ['all_weights','targetloads','actual_rank3_triples']}),indent=2))
