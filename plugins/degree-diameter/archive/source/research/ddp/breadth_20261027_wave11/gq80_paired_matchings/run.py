"""One complete, unsymmetrized W(3,3) paired-matching feasibility MILP."""
import os
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import resource
resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
import json
import sys
import time
import warnings
from itertools import product, combinations
from pathlib import Path

started_cpu = time.process_time()
started_wall = time.perf_counter()
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'aris_repo/tools'))
from capture_filter import screen
import numpy as np
import scipy
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

def save(name, data):
    text = json.dumps(data, indent=2) + '\n'
    # Screen prose values, not numeric constraint IDs such as 429 or 503.
    def prose(x):
        if isinstance(x,str): return [x]
        if isinstance(x,dict): return [s for v in x.values() for s in prose(v)]
        if isinstance(x,(list,tuple)): return [s for v in x for s in prose(v)]
        return []
    assert not screen('\n'.join(prose(data)))
    (HERE/name).write_text(text)

def normalize(x):
    lead = next(a for a in x if a)
    return tuple(a * pow(lead, -1, 3) % 3 for a in x)

def omega(x, y):
    return (x[0]*y[1]-x[1]*y[0]+x[2]*y[3]-x[3]*y[2]) % 3

points = sorted({normalize(x) for x in product(range(3), repeat=4) if any(x)})
point_id = {p:i for i,p in enumerate(points)}
line_set = set()
for u,v in combinations(points, 2):
    if omega(u,v) == 0:
        line_set.add(tuple(sorted({point_id[normalize(tuple((a*u[k]+b*v[k])%3 for k in range(4)))]
                                  for a,b in product(range(3), repeat=2) if a or b})))
lines = sorted(line_set)
N = len(points)
point_lines = [{j for j,l in enumerate(lines) if p in l} for p in range(N)]
closed_p = [{j for j,v in enumerate(points) if omega(u,v)==0} for u in points]
closed_l = [{j for j,m in enumerate(lines) if set(l)&set(m)} for l in lines]
assert N == len(lines) == 40
assert all(len(l)==4 for l in lines) and all(len(x)==4 for x in point_lines)
assert all(len(x)==13 for x in closed_p+closed_l)
assert all(len(c[i]&c[j])==4 for c in (closed_p,closed_l) for i,j in combinations(range(N),2))
assert all(sum(p in closed_p[u] for p in l)==1 for u in range(N) for l in lines if u not in l)
incidence = [(p,N+j) for j,l in enumerate(lines) for p in l]
assert len(incidence)==160
save('geometry.json',dict(field=3,dimension=4,symplectic_form='x0*y1-x1*y0+x2*y3-x3*y2 mod3',
                          vertex_encoding='points0..39; lines40..79',points=points,lines=lines,
                          point_incident_lines=[sorted(x) for x in point_lines],
                          incidence_edge_count=160,closed_collinearity_size=13,
                          closed_collinearity_pair_intersection=4,graph_BFS_performed=False))
(HERE/'incidence.edges').write_text('80 160\n'+''.join(f'{u} {v}\n' for u,v in incidence))

variables = []
edge_id = {}
for side in (0,1):
    for u,v in combinations(range(N),2):
        edge_id[side,u,v] = len(variables)
        variables.append(dict(side='point' if side==0 else 'line',u=u,v=v))

def eid(side,u,v):
    return edge_id[side,min(u,v),max(u,v)]

degree_rows = [dict(side=side,vertex=u,vars=[eid(side,u,v) for v in range(N) if v!=u])
               for side in (0,1) for u in range(N)]
cover_rows = []
for side,closed,opposite_neighbors in [(0,closed_p,point_lines),(1,closed_l,[set(l) for l in lines])]:
    for x,y in combinations(range(N),2):
        if y in closed[x]:
            continue
        own = {eid(side,x,z) for z in closed[y]} | {eid(side,y,z) for z in closed[x]}
        relay = {eid(1-side,l,m) for l in opposite_neighbors[x] for m in opposite_neighbors[y]}
        assert len(own)==25 and len(relay)==16 and not (own&relay)
        cover_rows.append(dict(side=side,x=x,y=y,own_vars=sorted(own),relay_vars=sorted(relay),vars=sorted(own|relay)))
assert len(variables)==1560 and len(degree_rows)==80 and len(cover_rows)==1080
assert sum(r['side']==0 for r in cover_rows)==540
model = dict(schema='all_simple_internal_edges_binary_v1',objective='zero, feasibility only',
             variable_count=1560,degree_equality_count=80,far_pair_cover_count=1080,
             cover_clause_variable_count=41,preassigned_edges=[],symmetry_constraints=[],
             variables=variables,degree_equations=degree_rows,far_pair_covers=cover_rows,
             degree_rhs=1,cover_lower_bound=1,variable_domain='binary')
save('model.json',model)
save('constraint_schema.json',{k:v for k,v in model.items() if k not in ('variables','degree_equations','far_pair_covers')} | dict(
    full_model='model.json',
    cover_rule='for far x,y: own edges x-z(z in C[y]) or y-z(z in C[x]); opposite edges l-m(l in I[x],m in I[y])',
    exactness='Only same-side far pairs need repair. Matching-only paths reduce to length0/1; routes with two incidence edges are precisely own-internal-first, own-internal-last, or opposite-internal-middle.'))

row_ids=[];col_ids=[]
all_rows = [r['vars'] for r in degree_rows+cover_rows]
for i,vs in enumerate(all_rows):
    row_ids.extend([i]*len(vs)); col_ids.extend(vs)
A = coo_matrix((np.ones(len(row_ids)),(row_ids,col_ids)),shape=(1160,1560)).tocsc()
lb = np.ones(1160)
ub = np.r_[np.ones(80),np.full(1080,np.inf)]
save('terminal.json',dict(status='RUNNING_SINGLE_MILP',solver_time_limit_seconds=15,
                          process_hard_CPU_seconds=20,solver_threads=1,production_calls=1,
                          model='model.json',incumbent_exported=False,graph_BFS_count=0))
solver_wall0=time.perf_counter();solver_cpu0=time.process_time()
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter('always')
    result = milp(c=np.zeros(1560),integrality=np.ones(1560),bounds=Bounds(0,1),
                  constraints=LinearConstraint(A,lb,ub),
                  options=dict(time_limit=15.0,threads=1,presolve=True,disp=True))
solver_wall=time.perf_counter()-solver_wall0;solver_cpu=time.process_time()-solver_cpu0
incumbent = result.x is not None
output=dict(scipy_version=scipy.__version__,solver_status=int(result.status),solver_message=str(result.message),
            solver_success=bool(result.success),incumbent_reported=incumbent,
            solver_wall_seconds=solver_wall,solver_CPU_seconds=solver_cpu,
            solver_warnings=[str(w.message) for w in caught],
            mip_node_count=getattr(result,'mip_node_count',None),mip_gap=getattr(result,'mip_gap',None),
            objective=getattr(result,'fun',None),production_calls=1,graph_BFS_count=0)
if incumbent:
    rounded=np.rint(result.x).astype(int)
    assert np.max(np.abs(rounded-result.x))<1e-5
    assert np.all(rounded>=0) and np.all(rounded<=1)
    values=A@rounded
    assert np.all(values[:80]==1) and np.all(values[80:]>=1)
    chosen=[i for i,v in enumerate(rounded) if v]
    assert len(chosen)==40
    factors=[[] for _ in range(2)]
    for i in chosen:
        v=variables[i];side=0 if v['side']=='point' else 1
        factors[side].append([v['u'],v['v']])
    assert all(len(f)==20 for f in factors)
    edges=sorted(incidence+[(u+side*N,v+side*N) for side,f in enumerate(factors) for u,v in f])
    assert len(edges)==len(set(edges))==200
    degrees=[0]*80
    for u,v in edges: degrees[u]+=1;degrees[v]+=1
    assert set(degrees)=={5}
    (HERE/'candidate.edges').write_text('80 200\n'+''.join(f'{u} {v}\n' for u,v in edges))
    save('candidate.matchings.json',dict(point_matching=factors[0],line_matching=factors[1],
                                        selected_variable_ids=chosen,all_80_degree_equalities_pass=True,
                                        all_1080_exact_cover_constraints_pass=True,
                                        cover_clause_minimum=int(min(values[80:])),n=80,m=200,degree=5,
                                        graph_BFS_performed=False))
    status='FEASIBLE_EXACT_COVER_INCUMBENT_AWAITS_ROOT_ALL_SOURCE_BFS'
elif result.status==2:
    status='RAW_SOLVER_INFEASIBLE_NO_CERTIFICATE'
else:
    status='UNKNOWN_NO_INCUMBENT_WINDOW_CLOSED'
output['status']=status
save('result.json',output)
save('terminal.json',dict(status=status,target_Delta=5,target_D=3,savedL=72,hypothetical_n=80,
                          actual_n=80 if incumbent else None,actual_D=None,ordinary_bad_unordered_pairs=None,
                          incumbent_exported=incumbent,solver_status=int(result.status),solver_message=str(result.message),
                          solver_time_limit_seconds=15,process_hard_CPU_seconds=20,solver_threads=1,
                          solver_wall_seconds=solver_wall,solver_CPU_seconds=solver_cpu,
                          total_CPU_seconds=time.process_time()-started_cpu,
                          total_wall_seconds=time.perf_counter()-started_wall,
                          production_calls=1,graph_BFS_count=0,new_lower_bounds=0,
                          pending=['root_unique_all80_source_BFS'] if incumbent else [],
                          scope='One complete unsymmetrized 1560-binary MILP; no restart, extra seed, or extension. Raw infeasible is not a certified theorem.'))
print(json.dumps(output,indent=2),flush=True)
