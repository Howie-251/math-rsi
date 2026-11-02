#!/usr/bin/env python3
"""One bounded batch of the 55 prescribed LPs, with exact rational certificates."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import time
START=time.process_time()
import resource
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
import json,itertools,warnings
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
HERE=Path(__file__).resolve().parent
PARAM=json.loads((HERE.parent/'PARAMETERS.json').read_text())
OLD=json.loads((HERE.parent/'controller_open_n_packing/SUMMARY.json').read_text())
CTRL=PARAM['controller']; NB=list(map(set,CTRL)); U=OLD['actual_selected_U']
assert U==[31,32,44,45,59,60,61,72,73,74]
# Bind only the saved small table to the already accepted same controller, not new geometry checks.
assert CTRL==json.loads((HERE.parent.parent/'PARAMETERS.json').read_text())['controller']
assert len(set().union(*(NB[u] for u in U)))==60
ROWS=[]; WARN=[]
def frac(x): return Q(float(x)).limit_denominator(100000)
def s(q): return str(q)
def save(name,obj): (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
for r in (1,2):
    for rem_tuple in itertools.combinations(U,r):
        if time.process_time()-START>18:
            save('RESULT.json',{'status':'UNKNOWN_CPU_PREFIX','completed':ROWS,'cpu_seconds':time.process_time()-START})
            raise SystemExit('UNKNOWN_CPU_PREFIX')
        rem=list(rem_tuple); kept=[u for u in U if u not in rem]
        occupied=set().union(*(NB[u] for u in kept))
        free=[v for v in range(78) if v not in occupied]
        allowed=[i for i in range(78) if i not in kept and not NB[i]&occupied]
        A=np.array([[int(v in NB[i]) for i in allowed] for v in free],dtype=float)
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            sol=linprog(-np.ones(len(allowed)),A_ub=A,b_ub=np.ones(len(free)),bounds=(0,1),method='highs',options={'threads':1})
        WARN.extend(str(w.message) for w in caught)
        assert sol.success,(rem,sol.message)
        primal=[frac(x) for x in sol.x]
        dualrows=[frac(-y) for y in sol.ineqlin.marginals]
        dualbounds=[frac(-z) for z in sol.upper.marginals]
        assert all(0<=x<=1 for x in primal)
        assert all(sum(primal[j] for j,i in enumerate(allowed) if v in NB[i])<=1 for v in free)
        assert all(y>=0 for y in dualrows+dualbounds)
        assert all(sum(dualrows[k] for k,v in enumerate(free) if v in NB[i])+dualbounds[j]>=1 for j,i in enumerate(allowed))
        optimum=sum(primal,Q(0)); upper=sum(dualrows+dualbounds,Q(0))
        assert optimum==upper
        assert optimum>=r # restored removed planes always feasible
        row={'removed':rem,'retained':kept,'occupied_target_fibers':sorted(occupied),'free_target_fibers':free,
             'admissible_controllers':allowed,'admissible_count':len(allowed),
             'additional_normalized_optimum':s(optimum),'additional_center_capacity':s(81*optimum),
             'baseline_additional_centers':81*r,'center_gap':s(81*(optimum-r)),
             'total_center_capacity':s(81*(len(kept)+optimum)),
             'primal_normalized':{str(i):s(x) for i,x in zip(allowed,primal) if x},
             'primal_center_weights':{str(i):s(81*x) for i,x in zip(allowed,primal) if x},
             'dual_target_multipliers':{str(v):s(y) for v,y in zip(free,dualrows) if y},
             'dual_upper_bound_multipliers':{str(i):s(z) for i,z in zip(allowed,dualbounds) if z},
             'exact_fraction_certificate_PASS':True,'linprog_iterations':int(sol.nit)}
        ROWS.append(row)
        save('LP_CASES.json',ROWS)
BEST=max(ROWS,key=lambda row:(Q(row['center_gap']),-len(row['removed']),-row['admissible_count']))
allowed=BEST['admissible_controllers']; support=list(map(int,BEST['primal_normalized']))
def dart(i,v):
    p=CTRL[i].index(v); c=PARAM['dart_chart_index'][i][p]; q=PARAM['inverse_ports'][p]
    return {'source_controller':i,'target_controller':v,'source_port':p,'source_port_name':PARAM['ports'][p],
            'target_port':q,'target_port_name':PARAM['ports'][q],'chart_index':c,'chart_id':PARAM['chart_ids'][c],
            'matrix':PARAM['matrices'][c],'noise_direction':PARAM['directions'][q],
            'literal_affine_map':'y=M*x+t*noise_direction; t in F9; GF9 is F3[w]/(w^2+1), a+3b encodes a+bw',
            'source_plane_parameterization':'x=(a,b,4*a), a,b in F9; partial centers need not stay in this plane'}
conflicts=[]
for i,j in itertools.combinations(allowed,2):
    common=sorted(NB[i]&NB[j])
    if common:
        conflicts.append({'controllers':[i,j],'shared_target_fibers':common,
                          'interfaces':[{'target':v,'left':dart(i,v),'right':dart(j,v)} for v in common]})
adj={i:set() for i in support}
for e in conflicts:
    i,j=e['controllers']
    if i in adj and j in adj: adj[i].add(j);adj[j].add(i)
# Only inspect the small positive support for an induced odd cycle; no packing re-solve.
cycle=None
for length in range(3,min(len(support),11)+1,2):
    def seek(path,start):
        if len(path)==length:
            if start not in adj[path[-1]]: return None
            E={(min(path[k],path[(k+1)%length]),max(path[k],path[(k+1)%length])) for k in range(length)}
            if all(((min(a,b),max(a,b)) in E)==(b in adj[a]) for a,b in itertools.combinations(path,2)): return path
            return None
        for nxt in sorted(adj[path[-1]]):
            if nxt>start and nxt not in path:
                out=seek(path+[nxt],start)
                if out: return out
        return None
    for start in support:
        cycle=seek([start],start)
        if cycle: break
    if cycle: break
interface={'status':'NECESSARY_CAPACITY_INTERFACE_ONLY','case':BEST,'positive_support':support,
           'induced_odd_cycle':cycle,'conflict_edges':conflicts,
           'all_admissible_darts':[dart(i,v) for i in allowed for v in CTRL[i]],
           'free_target_constraints':[{'target':v,'controllers':[i for i in allowed if v in NB[i]],'rhs_centers':81} for v in BEST['free_target_fibers']],
           'retained_planes':{'controllers':BEST['retained'],'center_weight_each':81,'plane':'(a,b,4*a)'},
           'actual_point_sets_constructed':False,'field_and_chart_revalidation':False}
save('BEST_INTERFACE.json',interface)
summary={'status':'ALL_55_SMALL_LPS_EXACTLY_CERTIFIED','single_removals':10,'double_removals':45,
         'positive_gap_cases':sum(Q(r['center_gap'])>0 for r in ROWS),
         'single_removal_optima':sorted(set(r['additional_center_capacity'] for r in ROWS if len(r['removed'])==1),key=Q),
         'double_removal_optima':sorted(set(r['additional_center_capacity'] for r in ROWS if len(r['removed'])==2),key=Q),
         'prediction_P1_supported':all(Q(r['additional_center_capacity'])<=81 for r in ROWS if len(r['removed'])==1),
         'prediction_P2_supported':any(Q(r['additional_center_capacity'])>162 for r in ROWS if len(r['removed'])==2),
         'best':BEST,'induced_odd_cycle':cycle,'CPU_budget_seconds':20,'total_CPU_seconds':time.process_time()-START,
         'warnings':sorted(set(WARN)),'actual_point_sets_constructed':0,'new_graphs':0,'BFS_runs':0,'Lean_runs':0,
         'whole_layer_packing_searches':0,'large_graph_files_read':0,'all_processes_terminal':True}
save('RESULT.json',summary)
save('TERMINAL.json',{'status':summary['status'],'exit_code':0,'total_CPU_seconds':time.process_time()-START,'all_processes_terminal':True})
print(json.dumps({k:v for k,v in summary.items() if k!='best'},ensure_ascii=False))
print('BEST',json.dumps({k:BEST[k] for k in ['removed','admissible_controllers','additional_center_capacity','center_gap','total_center_capacity','primal_center_weights']},ensure_ascii=False))
