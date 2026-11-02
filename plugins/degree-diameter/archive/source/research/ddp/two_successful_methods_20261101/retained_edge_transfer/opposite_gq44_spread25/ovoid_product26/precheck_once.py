#!/usr/bin/env python3
"""Fixed Q and full-N packing precheck; reads source but constructs no candidate."""
import collections
import itertools
import json
from pathlib import Path
import resource
import time

OUT=Path(__file__).resolve().parent
SRC=OUT.parent
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
START=time.process_time()

def write(name,value):
    (OUT/name).write_text(json.dumps(value,indent=2)+'\n')

params=json.loads((SRC/'PARAMETERS.json').read_text())
fields=json.loads((SRC/'FIELD_TABLES.json').read_text())
M4=fields['GF4']['multiplication']
M16=fields['GF16']['multiplication']
TRACE=fields['GF16']['trace_GF16_to_GF4']
points=params['points']
lines=[row['points'] for row in params['lines']]
spread=params['spread_line_labels']
owner=params['point_spread_owner']
assert len(points)==len(lines)==85 and len(spread)==17

def quadratic(x):
    u0,u1,v0,v1=x
    return M4[u0][u0]^M4[u0][v1]^M4[2][M4[v1][v1]]^M4[u1][v0^v1]

def form(x,y):
    xu,xv=x[0]+4*x[1],x[2]+4*x[3]
    yu,yv=y[0]+4*y[1],y[2]+4*y[3]
    return TRACE[M16[xu][yv]^M16[xv][yu]]

vectors=list(itertools.product(range(4),repeat=4))
assert all(quadratic(tuple(M4[a][z] for z in x))==M4[M4[a][a]][quadratic(x)]
           for a in range(4) for x in vectors)
assert all(quadratic(tuple(a^b for a,b in zip(x,y)))^quadratic(x)^quadratic(y)==form(x,y)
           for x in vectors for y in vectors)
ovoid=[p for p,x in enumerate(points) if quadratic(x)==0]
assert len(ovoid)==17, ('ovoid size',len(ovoid),ovoid)
assert all(form(points[p],points[q])!=0 for p,q in itertools.combinations(ovoid,2))
line_ovoid=[[p for p in line if p in ovoid] for line in lines]
assert all(len(hit)==1 for hit in line_ovoid)
assert sorted(owner[p] for p in ovoid)==list(range(17))

# Read only the already produced literal graph. No BFS/distance check here.
with (SRC/'graph_d25_D3_n7242.edges').open() as stream:
    n,m=map(int,next(stream).split())
    assert (n,m)==(7242,90525)
    adj=[set() for _ in range(n)]
    rows=0
    for text in stream:
        a,b=map(int,text.split())
        adj[a].add(b)
        adj[b].add(a)
        rows+=1
    assert rows==m

centers=[]
load=[0]*7242
flag_cases=[]
raw_load=[0]*7225
for p in ovoid:
    for j,l in enumerate(spread):
        center=85*p+l
        pins=sorted(adj[center])
        assert len(pins)==25
        raw_pins=sorted(85*q+k for q in lines[l] for k in params['point_incident_lines'][p])
        assert len(raw_pins)==len(set(raw_pins))==25
        for u in raw_pins:
            raw_load[u]+=1
        is_flag=p in lines[l]
        if is_flag:
            bonus=7225+owner[p]
            assert center in raw_pins
            assert set(pins)==(set(raw_pins)-{center})|{bonus}
            flag_cases.append({'point':p,'spread_index':j,'spread_line':l,
                               'center':center,'deleted_raw_self_neighbor':center,
                               'added_bonus_neighbor':bonus,'owner':owner[p]})
        else:
            assert set(pins)==set(raw_pins)
        for u in pins:
            load[u]+=1
        centers.append({'index':len(centers),'point':p,'spread_index':j,'spread_line':l,
                        'old_center_label':center,'is_incident_flag':is_flag,
                        'source_full_neighborhood_ordered':pins,'raw_neighborhood_ordered':raw_pins})
assert len(centers)==289 and len({r['old_center_label'] for r in centers})==289
assert raw_load==[1]*7225
assert len(flag_cases)==17
assert sorted(row['owner'] for row in flag_cases)==list(range(17))
assert max(load)==1
covered=[u for u,c in enumerate(load) if c]
missing=[u for u,c in enumerate(load) if not c]
expected_missing=sorted(row['center'] for row in flag_cases)
assert len(covered)==7225 and len(missing)==17 and missing==expected_missing
assert all(load[u]==1 for u in range(7225,7242))
CPU=time.process_time()-START
write('OVOID_GEOMETRY_CHECK.json',{
    'quadratic_formula':'u0^2+u0*v1+w*v1^2+u1*(v0+v1), w=GF4code2',
    'homogeneity_checks':len(vectors)*4,'homogeneous_quadratic':True,
    'polar_equals_B_checks':len(vectors)**2,'polar_equals_B':True,
    'ovoid_point_ids':ovoid,'ovoid_point_coordinates':[points[p] for p in ovoid],
    'ovoid_size':17,'distinct_ovoid_pairs_checked':136,'ovoid_pair_B_nonzero':True,
    'line_to_unique_ovoid_point':[hit[0] for hit in line_ovoid],
    'line_once_checks':85,'ovoid_once_per_line':True,
    'frozen_spread_line_labels':spread,'ovoid_spread_owners':[owner[p] for p in ovoid]})
write('ORDERED_CENTERS.json',{'order':'ascending ovoid point ID outer; frozen spread index0..16 inner',
    'center_label':'85*point+line','neighbor_order':'ascending source vertex labels',
    'source_edge_table':'../graph_d25_D3_n7242.edges','centers':centers})
write('NEIGHBOR_MULTIPLICITY.json',{'vertex_label_order':'0..7241','multiplicity':load,
    'raw_old_vertex_multiplicity':raw_load,
    'multiplicity_histogram':dict(sorted(collections.Counter(load).items())),
    'union_size':len(covered),'maximum_degree_load':max(load),'pairwise_disjoint':True,
    'missing_vertices':missing})
write('FLAG_EXCEPTIONS.json',{'flag_cases':flag_cases,'expected_missing_chosen_flag_centers':expected_missing,
    'actual_missing_vertices':missing,'each_bonus_owner_used_once':True})
result={'status':'PASS_FIXED_OVOID_PRODUCT_PACKING_AWAIT_ROOT_GRAPH_RELEASE',
    'source_n':7242,'source_m':90525,'source_degree':25,
    'ovoid_size':17,'spread_lines':17,'centers':289,'full_neighborhood_size':25,
    'pairwise_disjoint':True,'maximum_vertex_degree_load':1,
    'union_size':7225,'missing_size':17,'missing_exactly_chosen_flag_centers':True,
    'capacity_bound_floor_source_n_over_fullN_size':289,
    'capacity_bound_scope':'fixed7242source full25neighborhood vertex-load<=1 only; notN26optimality',
    'conditional_candidate_prediction':{'n':7531,'m':97750,'degree_histogram':{'25':306,'26':7225}},
    'candidate_generated':False,'R3_checks':0,'source_BFS_runs':0,'solver_calls':0,'Lean_calls':0,
    'CPU_seconds':CPU,'worker_count':1,'further_numerical_work_running':False}
write('PRECHECK_RESULT.json',result)
print(json.dumps(result,indent=2))
