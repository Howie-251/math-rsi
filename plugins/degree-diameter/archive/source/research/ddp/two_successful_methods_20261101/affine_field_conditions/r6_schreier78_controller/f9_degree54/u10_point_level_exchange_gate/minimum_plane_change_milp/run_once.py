#!/usr/bin/env python3
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[name]='1'
import time
START=time.process_time()
import resource
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
import json,itertools,warnings
from pathlib import Path
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
HERE=Path(__file__).resolve().parent
P=json.loads((HERE.parent.parent/'PARAMETERS.json').read_text()); CTRL=P['controller']; NB=list(map(set,CTRL))
OLD=json.loads((HERE.parent/'RESULT.json').read_text())
assert OLD['status']=='ALL_55_SMALL_LPS_EXACTLY_CERTIFIED' and OLD['positive_gap_cases']==0
U=[31,32,44,45,59,60,61,72,73,74]
A=[]; lo=[];hi=[]
for v in range(78): A.append([int(v in NB[i]) for i in range(78)]+[0]*10);lo.append(-np.inf);hi.append(81)
for j,u in enumerate(U):
 r=[0]*88;r[u]=1;r[78+j]=81;A.append(r);lo.append(81);hi.append(np.inf)
A.append([1]*78+[0]*10);lo.append(811);hi.append(np.inf)
A.append([0]*78+[1]*10);lo.append(3);hi.append(np.inf)
input_record={'controller':CTRL,'U':U,'integer_w_bounds':[0,81],'binary_z_bounds':[0,1],
              'objective':'min sum z','target_constraints':'for each v sum_{i adjacent v} w_i<=81',
              'retained_constraints':'w_u+81*z_u>=81','total_centers_min':811,'proved_change_lower_bound':3,
              'time_limit_wall_seconds':16,'CPU_budget_seconds':20,'threads':1}
(HERE/'MODEL.json').write_text(json.dumps(input_record,indent=2)+'\n')
with warnings.catch_warnings(record=True) as caught:
 warnings.simplefilter('always')
 sol=milp(c=np.r_[np.zeros(78),np.ones(10)],integrality=np.ones(88),
          bounds=Bounds(np.zeros(88),np.r_[np.full(78,81),np.ones(10)]),
          constraints=LinearConstraint(np.array(A,dtype=float),np.array(lo),np.array(hi)),
          options={'time_limit':16,'threads':1,'mip_rel_gap':0.0,'presolve':True})
solver_cpu=time.process_time()-START
result={'status':'OPTIMAL_CAPACITY_MODEL' if sol.status==0 else 'UNKNOWN_SINGLE_BATCH_TERMINAL',
        'scipy_status':int(sol.status),'solver_message':sol.message,'success':bool(sol.success),
        'mip_dual_bound':None if getattr(sol,'mip_dual_bound',None) is None else float(sol.mip_dual_bound),
        'mip_gap':None if getattr(sol,'mip_gap',None) is None else float(sol.mip_gap),
        'mip_node_count':None if getattr(sol,'mip_node_count',None) is None else int(sol.mip_node_count),
        'solver_and_preparation_CPU_seconds':solver_cpu,'warnings':[str(w.message) for w in caught],
        'prediction_optimum3_supported':False,'new_graphs':0,'BFS_runs':0,'Lean_runs':0,
        'large_graphs_read':0,'whole_layer_packing_searches':0,'single_batch_only':True}
if sol.x is not None:
 rounded=np.rint(sol.x).astype(int)
 assert np.max(np.abs(sol.x-rounded))<1e-5
 w=rounded[:78].tolist();z=rounded[78:].tolist()
 assert all(0<=v<=81 for v in w) and all(v in (0,1) for v in z)
 loads=[sum(w[i] for i in range(78) if v in NB[i]) for v in range(78)]
 assert max(loads)<=81 and sum(w)>=811 and all(w[u]+81*z[j]>=81 for j,u in enumerate(U)) and sum(z)>=3
 retained=[u for j,u in enumerate(U) if not z[j]]; changed=[u for j,u in enumerate(U) if z[j]]
 support=[i for i,x in enumerate(w) if x]; outsiders=[i for i in support if i not in U]
 result.update(exact_integer_feasible_PASS=True,objective_changes=sum(z),total_center_capacity=sum(w),center_gap=sum(w)-810,
               retained_U=retained,changed_U=changed,active_new_controllers=outsiders,
               support_weights={str(i):w[i] for i in support},all_weights=w,target_loads=loads,
               prediction_optimum3_supported=bool(sol.status==0 and sum(z)==3))
 def dart(i,v):
  p=CTRL[i].index(v); c=P['dart_chart_index'][i][p]; q=P['inverse_ports'][p]
  return {'source_controller':i,'target_controller':v,'source_port':p,'source_port_name':P['ports'][p],
          'target_port':q,'target_port_name':P['ports'][q],'chart_index':c,'chart_id':P['chart_ids'][c],
          'matrix':P['matrices'][c],'noise_direction':P['directions'][q],
          'actual_affine_map':'y=M*x+t*noise_direction, t in F9','field':'F3[w]/(w^2+1); a+3b encodes a+bw'}
 residual=[i for i in support if i not in retained]
 conflicts=[]
 for i,j in itertools.combinations(residual,2):
  common=sorted(NB[i]&NB[j])
  if common: conflicts.append({'controllers':[i,j],'shared_target_fibers':common,
                              'actual_interfaces':[{'target':v,'left':dart(i,v),'right':dart(j,v)} for v in common]})
 interface={'scope':'necessary integer center counts only, no actual F9 point sets',
            'retained_full_planes':retained,'changed_U':changed,'residual_support':residual,
            'weights':{str(i):w[i] for i in residual},'conflict_edges':conflicts,
            'all_residual_darts':[dart(i,v) for i in residual for v in CTRL[i]],
            'residual_target_constraints':[{'target':v,'controllers':[i for i in residual if v in NB[i]],
                                           'weights':[w[i] for i in residual if v in NB[i]],
                                           'load':loads[v],'capacity':81} for v in sorted(set().union(*(NB[i] for i in residual)))],
            'actual_point_realization':False}
 (HERE/'CAPACITY_INTERFACE.json').write_text(json.dumps(interface,ensure_ascii=False,indent=2)+'\n')
result['total_CPU_seconds']=time.process_time()-START
result['all_processes_terminal']=True
(HERE/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(HERE/'TERMINAL.json').write_text(json.dumps({'status':result['status'],'scipy_status':int(sol.status),
              'total_CPU_seconds':result['total_CPU_seconds'],'all_processes_terminal':True},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('all_weights','target_loads')},ensure_ascii=False))
