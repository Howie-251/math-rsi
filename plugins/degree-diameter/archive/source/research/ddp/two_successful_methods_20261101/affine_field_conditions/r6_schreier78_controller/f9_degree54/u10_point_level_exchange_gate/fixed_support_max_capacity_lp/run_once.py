#!/usr/bin/env python3
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import time
START=time.process_time()
import resource
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
import json,itertools,warnings
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import linprog
HERE=Path(__file__).resolve().parent
P=json.loads((HERE.parent.parent/'PARAMETERS.json').read_text());CTRL=P['controller'];NB=list(map(set,CTRL))
M=json.loads((HERE.parent/'minimum_plane_change_milp/RESULT.json').read_text())
retained=M['retained_U'];assert retained==[31,59,60,72]
variables=[int(i) for i in M['support_weights'] if int(i) not in retained]
occupied=set().union(*(NB[i] for i in retained));free=[v for v in range(78) if v not in occupied]
admissible=[i for i in range(78) if i not in retained and not NB[i]&occupied]
assert set(variables)<=set(admissible)
A=np.array([[int(v in NB[i]) for i in variables] for v in free],dtype=float)
with warnings.catch_warnings(record=True) as caught:
 warnings.simplefilter('always')
 sol=linprog(-np.ones(len(variables)),A_ub=A,b_ub=np.ones(len(free)),bounds=(0,1),method='highs',options={'threads':1})
assert sol.success,sol.message
q=lambda x:Q(float(x)).limit_denominator(100000)
x=[q(t) for t in sol.x];y=[q(-t) for t in sol.ineqlin.marginals];z=[q(-t) for t in sol.upper.marginals]
assert all(0<=t<=1 for t in x) and all(t>=0 for t in y+z)
assert all(sum(x[j] for j,i in enumerate(variables) if v in NB[i])<=1 for v in free)
assert all(sum(y[k] for k,v in enumerate(free) if v in NB[i])+z[j]>=1 for j,i in enumerate(variables))
assert sum(x,Q(0))==sum(y+z,Q(0))
weights={i:81 for i in retained};weights.update({i:81*t for i,t in zip(variables,x) if t})
integer_weights={i:int(w) for i,w in weights.items()};integer_weights={i:w for i,w in integer_weights.items() if w}
integer_loads=[sum(w for i,w in integer_weights.items() if v in NB[i]) for v in range(78)]
assert max(integer_loads)<=81
opt=sum(weights.values(),Q(0)); residual=sum(x,Q(0))*81
result={'status':'ONE_FIXED_SUPPORT_LP_EXACT_PRIMAL_DUAL_PASS','retained':retained,'optimized_original_mip_support':variables,
        'all_admissible_controllers_under_retained4':admissible,'admissible_excluded_by_fixed_support':sorted(set(admissible)-set(variables)),
        'normalized_primal':{str(i):str(t) for i,t in zip(variables,x) if t},
        'rational_center_weights':{str(i):str(w) for i,w in weights.items()},
        'residual_capacity':str(residual),'total_capacity':str(opt),'total_integer_upper_bound_in_this_support':int(opt),
        'center_gap_over810':str(opt-810),'coordinatewise_floor_integer_weights':{str(i):w for i,w in integer_weights.items()},
        'floor_integer_total':sum(integer_weights.values()),'floor_integer_gap':sum(integer_weights.values())-810,
        'floor_integer_target_loads':integer_loads,
        'dual_targets_normalized':{str(v):str(t) for v,t in zip(free,y) if t},
        'dual_variable_bounds_normalized':{str(i):str(t) for i,t in zip(variables,z) if t},
        'exact_rational_certificate_PASS':True,'prediction_strictly_above811_supported':opt>811,
        'solver_calls':1,'new_MIP_calls':0,'BFS_Lean_graphs':0,'warnings':[str(w.message) for w in caught]}
def dart(i,v):
 p=CTRL[i].index(v);c=P['dart_chart_index'][i][p];ip=P['inverse_ports'][p]
 return {'source':i,'target':v,'source_port':p,'source_port_name':P['ports'][p],'target_port':ip,
         'target_port_name':P['ports'][ip],'chart_index':c,'chart_id':P['chart_ids'][c],
         'matrix':P['matrices'][c],'noise_direction':P['directions'][ip],
         'actual_affine_map':'y=M*x+t*noise_direction, t in F9'}
edges=[]
for i,j in itertools.combinations(admissible,2):
 common=sorted(NB[i]&NB[j])
 if common:edges.append({'controllers':[i,j],'shared_targets':common,
                        'interfaces':[{'target':v,'left':dart(i,v),'right':dart(j,v)} for v in common]})
interface={'status':'ALL_ADMISSIBLE_PAIR_ACTUAL_AFFINE_INTERFACES_SAVED','retained':retained,
           'all_admissible':admissible,'LP_support':variables,'positive_LP_support':sorted(i for i in weights if i not in retained),
           'pair_conflicts':edges,'all_admissible_darts':[dart(i,v) for i in admissible for v in CTRL[i]],
           'all_target_constraints':[{'target':v,'controllers':[i for i in admissible if v in NB[i]],'capacity':81} for v in free],
           'field':P['field'],'original_plane':'W={(a,b,4*a)}; all coefficients in genuine F9, not Z9',
           'actual_center_sets_generated':False,'needed_next':'Choose actual center subsets; for each shared target v require corresponding affine line unions disjoint simultaneously. Counts alone do not imply this.'}
(HERE/'ALL_ADMISSIBLE_AFFINE_INTERFACE.json').write_text(json.dumps(interface,ensure_ascii=False,indent=2)+'\n')
result['total_CPU_seconds']=time.process_time()-START;result['all_processes_terminal']=True
(HERE/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(HERE/'TERMINAL.json').write_text(json.dumps({'status':result['status'],'total_CPU_seconds':result['total_CPU_seconds'],'all_processes_terminal':True},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='floor_integer_target_loads'},ensure_ascii=False))
