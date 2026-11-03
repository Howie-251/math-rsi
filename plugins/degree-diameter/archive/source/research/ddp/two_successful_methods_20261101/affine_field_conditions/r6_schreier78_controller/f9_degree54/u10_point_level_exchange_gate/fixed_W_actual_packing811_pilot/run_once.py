import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[key]='1'
import time
START=time.process_time();WALL=time.time()
import resource
resource.setrlimit(resource.RLIMIT_CPU,(60,61))
import csv,itertools,json,math,warnings
from pathlib import Path
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix,vstack
D=Path(__file__).resolve().parent;BASE=D.parents[1]
P=json.loads((BASE/'PARAMETERS.json').read_text())
INTER=json.loads((D.parent/'fixed_support_max_capacity_lp/ALL_ADMISSIBLE_AFFINE_INTERFACE.json').read_text())
RET=[31,59,60,72];ALLOW=[16,17,30,32,35,42,43,44,45,58,61,64,71,73,74]
assert INTER['retained']==RET and INTER['all_admissible']==ALLOW
CTRL=P['controller'];MU=P['field']['multiplication'];MATS=P['matrices'];CH=P['dart_chart_index'];INV=P['inverse_ports'];DIR=P['directions']
ADD=[[(a%3+b%3)%3+3*((a//3+b//3)%3) for b in range(9)] for a in range(9)]
NEG=[(-a%3)+3*(-(a//3)%3) for a in range(9)]
def add(a,b):return ADD[a][b]
def dot(a,b):
 r=0
 for x,y in zip(a,b):r=ADD[r][MU[x][y]]
 return r
def pins(u,x):
 out=[]
 for p,v in enumerate(CTRL[u]):
  M=MATS[CH[u][p]];y=[dot(row,x) for row in M];noise=DIR[INV[p]]
  for t in range(9):
   q=[ADD[y[k]][MU[t][noise[k]]] for k in range(3)]
   out.append(729*v+q[0]+9*q[1]+81*q[2])
 out.sort()
 assert len(out)==len(set(out))==54
 return out
def det(cols):
 value=0
 for perm in itertools.permutations(range(3)):
  term=1
  for r,c in enumerate(perm):term=MU[term][cols[c][r]]
  if sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2:term=NEG[term]
  value=ADD[value][term]
 return value
def jnum(x):
 if x is None:return None
 y=float(x);return y if math.isfinite(y) else str(y)
phase='generate_fixed_pool';solver_cpu=None;result=None
try:
 pool=[];fixed=[];variables=[];fixedpin={}
 for u in sorted(RET+ALLOW):
  for a in range(9):
   for b in range(9):
    x=[a,b,MU[4][a]];n=pins(u,x);label=729*u+x[0]+9*x[1]+81*x[2]
    assert label not in n
    c=dict(pool_index=len(pool),controller=u,plane_index=9*a+b,a=a,b=b,x2=x[2],source_label=label,pins=n,retained=u in RET)
    pool.append(c)
    if u in RET:
     fixed.append(c)
     for v in n:assert v not in fixedpin;fixedpin[v]=label
    else:variables.append(c)
 assert len(fixed)==324 and len(variables)==1215 and len(fixedpin)==17496
 occupied=sorted({v for u in RET for v in CTRL[u]})
 assert len(occupied)==24 and all(sum(v//729==t for v in fixedpin)==729 for t in occupied)
 actualallow=[u for u in range(78) if u not in RET and not(set(CTRL[u])&set(occupied))]
 assert actualallow==ALLOW
 for i,c in enumerate(variables):c['variable']=i
 with (D/'ALL_CANDIDATE_CENTERS.tsv').open('w') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(['pool_index','controller','plane_index','a','b','x2','source_label','retained','variable'])
  for c in pool:w.writerow([c[k] if k!='variable' else c.get(k,-1) for k in ['pool_index','controller','plane_index','a','b','x2','source_label','retained','variable']])
 with (D/'ALL_CANDIDATE_PIN_ROWS.tsv').open('w') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(['pool_index','source_label',*[f'pin{i}' for i in range(54)]])
  for c in pool:w.writerow([c['pool_index'],c['source_label'],*c['pins']])
 directions=[]
 for u in [17,35,74]:
  p=CTRL[u].index(48);directions.append(DIR[INV[p]])
 determinant=det(directions);assert determinant==6
 phase='assemble_actual_pin_MIP'
 pinrows={}
 for j,c in enumerate(variables):
  for v in c['pins']:pinrows.setdefault(v,[]).append(j)
 rows=[];cols=[];data=[];ub=[];lb=[]
 for row,(pin,js) in enumerate(sorted(pinrows.items())):
  rows.extend([row]*len(js));cols.extend(js);data.extend([1.0]*len(js));lb.append(-np.inf);ub.append(1-int(pin in fixedpin))
 npinrows=len(ub);nv=len(variables);nvar=nv+3
 # Required residual cardinality.
 row=len(ub);rows.extend([row]*nv);cols.extend(range(nv));data.extend([1.0]*nv);lb.append(487);ub.append(np.inf)
 for k,u in enumerate([17,35,74]):
  row=len(ub)
  for j,c in enumerate(variables):
   if c['controller']==u:rows.append(row);cols.append(j);data.append(1.0)
  rows.append(row);cols.append(nv+k);data.append(-61.0);lb.append(-np.inf);ub.append(20)
 row=len(ub);rows.extend([row]*3);cols.extend([nv,nv+1,nv+2]);data.extend([1.0]*3);lb.append(-np.inf);ub.append(2)
 A=coo_matrix((np.array(data),(np.array(rows,dtype=np.int32),np.array(cols,dtype=np.int32))),shape=(len(ub),nvar)).tocsc()
 model=dict(scope='retained4 completeW planes plus all15 admissible fixedW pools, including64/71',retained=RET,admissible=ALLOW,
  fixed_centers=324,candidate_variables=nv,auxiliary_binaries=3,total_variables=nvar,
  actual_pin_constraints=npinrows,matrix_rows=len(ub),matrix_nonzeros=int(A.nnz),minimum_variable_centers=487,minimum_total_centers=811,
  target48_sources=[17,35,74],actual_noise_directions=directions,actual_direction_determinant=determinant,
  valid_cut='w_u<=20+61*z_u for u17,35,74; sumz<=2',
  cut_proof='../THREE_DIRECTION_NOTE.md; pairwise-disjoint fullF9 line families have product<=20^3',
  objective='zero: feasibility, not maximum cardinality',time_limit_wall_seconds=44,solver_CPU_ceiling=45,total_CPU_budget=60,threads=1,
  oldfield_revalidation=0,source_edgefiles_read=0,solver_calls_planned=1)
 (D/'MODEL.json').write_text(json.dumps(model,indent=2)+'\n')
 (D/'HANDLE.json').write_text(json.dumps(dict(pid=os.getpid(),phase='one_milp',CPU_budget_seconds=60,solver_time_limit_wall_seconds=44,single_worker=True),indent=2)+'\n')
 phase='one_fixed_pool_milp';before=time.process_time()
 with warnings.catch_warnings(record=True) as caught:
  warnings.simplefilter('always')
  sol=milp(c=np.zeros(nvar),integrality=np.ones(nvar),bounds=Bounds(np.zeros(nvar),np.ones(nvar)),
   constraints=LinearConstraint(A,np.array(lb),np.array(ub)),options={'time_limit':44.0,'threads':1,'presolve':True,'mip_rel_gap':0.0})
 solver_cpu=time.process_time()-before
 rawx=None if sol.x is None else sol.x.tolist()
 (D/'SOLVER_RETURN.json').write_text(json.dumps(dict(status=int(sol.status),message=sol.message,success=bool(sol.success),
  x=rawx,mip_dual_bound=jnum(getattr(sol,'mip_dual_bound',None)),mip_gap=jnum(getattr(sol,'mip_gap',None)),
  mip_node_count=jnum(getattr(sol,'mip_node_count',None)),solver_CPU_seconds=solver_cpu,
  dual_bound_meaning='zero feasibility objective, not maximum-center bound',warnings=[str(w.message) for w in caught]),indent=2)+'\n')
 result=dict(status='UNKNOWN_TIME_OR_UNSUPPORTED_P3',P3='fixedW retained4 pool has at least811 actual disjoint-fullN54 centers',
  scipy_status=int(sol.status),solver_message=sol.message,solver_CPU_seconds=solver_cpu,
  mip_dual_bound=jnum(getattr(sol,'mip_dual_bound',None)),mip_gap=jnum(getattr(sol,'mip_gap',None)),
  mip_node_count=jnum(getattr(sol,'mip_node_count',None)),dual_bound_is_max_center_bound=False,
  fixed_controllers=RET,admissible_variable_controllers=ALLOW,all19_controller_pool=sorted(RET+ALLOW),
  fixed_centers=324,candidate_center_pool=1539,variable_centers=1215,minimum_total_centers=811,
  fixed_occupied_target_fibers=occupied,fixed_distinct_pins=len(fixedpin),actual_pin_constraints=npinrows,
  cut_used=True,target48_direction_determinant=determinant,solver_calls=1,
  candidate_x_returned=sol.x is not None,packing_incumbent_verified=False,
  known_accepted_baseline810_inherited_not_revalidated=True,new_graphs=0,old_edgefiles_read=0,
  whole_layer_optimum_searches=0,field_law_or_old_rank_checks=0,new_single_direction_determinants=1,
  BFS_runs=0,Lean_runs=0,eta_or_phase_or_seed_or_retained_changes=0)
 if sol.x is not None:
  phase='independent_dictionary_pin_check';rounded=np.rint(sol.x).astype(int)
  residual=float(np.max(np.abs(sol.x-rounded)));chosen=[c for j,c in enumerate(variables) if rounded[j]]
  result['returned_integrality_residual']=residual
  if residual<1e-6 and all(x in [0,1] for x in rounded) and len(chosen)>=487:
   selected=sorted(fixed+chosen,key=lambda c:(c['controller'],c['plane_index']))
   ownerdict={};collision=None
   for c in selected:
    for pin in c['pins']:
     if pin in ownerdict:collision=[pin,ownerdict[pin],c['source_label']];break
     ownerdict[pin]=c['source_label']
    if collision:break
   assert collision is None,('literal_pin_collision',collision)
   assert len(ownerdict)==54*len(selected)
   assert all(any(c['controller']==u and c['plane_index']==j for c in selected) for u in RET for j in range(81))
   with (D/'SELECTED_CENTERS.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['j','controller','plane_index','a','b','x2','source_label'])
    for j,c in enumerate(selected):w.writerow([j,*[c[k] for k in ['controller','plane_index','a','b','x2','source_label']]])
   with (D/'SELECTED_ORDERED_PINS.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['j','source_label',*[f'pin{i}' for i in range(54)]])
    for j,c in enumerate(selected):w.writerow([j,c['source_label'],*c['pins']])
   counts={str(u):sum(c['controller']==u for c in selected) for u in sorted(RET+ALLOW)}
   result.update(status='PASS_ACTUAL_FIXED_W_PACKING_AT_LEAST811',packing_incumbent_verified=True,
    total_selected_centers=len(selected),selected_variable_centers=len(chosen),distinct_actual_source_pins=len(ownerdict),
    max_source_pin_load=1,actual_layer_center_counts=counts,auxiliary_switches=rounded[nv:].tolist(),
    source_coordinates_and_ordered_pins_saved=True,P3_supported=True,
    new_graph_production_authorized=False)
  else:result.update(status='UNKNOWN_NO_VALID_INTEGER_INCUMBENT',P3_supported=False)
 elif sol.status==2:
  result.update(status='INFEASIBLE_FIXED_RETAINED4_W_POOL_SOLVER_SCALE',P3_supported=False,
   closure_scope='only this fixedretained4 and all19W controller pool with accepted logicalcut; numericalMIP evidence, not a field/family/global nonexistence proof')
 else:result.update(P3_supported=False,closure_scope='UNKNOWN; no family exclusion')
 result['warnings']=[str(w.message) for w in caught]
 result['all_processes_terminal']=True;result['total_CPU_seconds']=time.process_time()-START
 assert solver_cpu<45 and result['total_CPU_seconds']<60
 (D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 terminal=dict(status=result['status'],single_worker=True,all_processes_terminal=True,
  total_CPU_seconds=time.process_time()-START,solver_CPU_seconds=solver_cpu,wall_seconds=time.time()-WALL,
  total_CPU_budget=60,solver_CPU_budget=45,solver_calls=1,no_automatic_continuation=True,
  measurement_boundary='Single process imports, fixedpool genuineN54 generation, sparse pin model with verified three-direction cut, one boundedmilp, dictionary incumbent check if present, aggregation. Interactive authoring excluded.')
 (D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
 (D/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',all_processes_terminal=True,solver_calls=1),indent=2)+'\n')
 print(json.dumps(dict(terminal=terminal,result=result),indent=2))
except Exception as error:
 record=dict(status='FAILED_OR_UNKNOWN_NO_CONTINUATION',phase=phase,error=str(error),total_CPU_seconds=time.process_time()-START,
  solver_CPU_seconds=solver_cpu,all_processes_terminal=True,no_automatic_continuation=True)
 (D/'RESULT.json').write_text(json.dumps(record,indent=2)+'\n')
 (D/'TERMINAL.json').write_text(json.dumps(record,indent=2)+'\n')
 raise
