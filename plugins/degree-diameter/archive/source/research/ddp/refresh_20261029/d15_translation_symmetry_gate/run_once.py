#!/usr/bin/env python3
"""Exact GF3 kernel and literal freeport orbits, once; no graph/BFS/solver."""
from collections import Counter,defaultdict
import json
import os
from pathlib import Path
import resource
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
TABLE=ROOT/'research/ddp/more_graphs_20261027/d15_loop_completed_quotient_probe/affine_relation_recovery/source15552_AFFINE_RELATIONS.json'
FREE=HERE.parent/'d15_D4_K2_route_gate/FREE_ORDER.txt'
START=time.process_time();WALL=time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU,(15,16))

def save(name,obj):(HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
assert not (HERE/'HANDLE.json').exists(),'This unique kernel calculation has already started.'
save('HANDLE.json',dict(status='RUNNING_EXACT_TRANSLATION_KERNEL',pid=os.getpid(),running=True,CPU_budget=15))
print(json.dumps(dict(status='RUNNING_EXACT_TRANSLATION_KERNEL',pid=os.getpid())),flush=True)
table=json.loads(TABLE.read_text())
assert table['complete'] and table['n']==15552 and table['m']==116316
assert table['dimension']==4 and table['bin_size']==81 and table['controller_count']==192
arcs=table['arcs'];assert len(arcs)==960
targets=defaultdict(list)
for arc in arcs:targets[arc['from']].append(arc['to'])
assert all(len(targets[u])==len(set(targets[u]))==5 for u in range(192))

# Rows have two disjoint bit planes: coefficients 1 and 2 respectively.
# The complete sparse equations are saved before elimination.
rows=[];equations=[]
for eid,arc in enumerate(arcs):
    u,v=arc['from'],arc['to'];B=arc['B'];direction=arc['v']
    p=next(i for i,x in enumerate(direction) if x%3)
    assert p==arc['pivot']
    vp=direction[p]%3
    for i in range(4):
        if i==p:continue
        coeff=defaultdict(int)
        for j in range(4):
            coeff[4*u+j]+=(vp*B[i][j]-direction[i]*B[p][j])
        coeff[4*v+i]-=vp
        coeff[4*v+p]+=direction[i]
        coeff={j:c%3 for j,c in coeff.items() if c%3}
        one=sum(1<<j for j,c in coeff.items() if c==1)
        two=sum(1<<j for j,c in coeff.items() if c==2)
        rows.append((one,two))
        equations.append(dict(arc=eid,source=u,target=v,pivot=p,quotient_coordinate=i,
                              coefficients=sorted([j,c] for j,c in coeff.items())))
assert len(rows)==2880
save('INPUT_AND_EQUATIONS.json',dict(table=str(TABLE),free_ports=str(FREE),field=3,
    variable_count=768,row_count=2880,variable_index='4*controller+coordinate',
    unique_target_bins_per_controller=5,equations=equations))
original=rows[:]

def add(a,b):
    a1,a2=a;b1,b2=b
    az=~(a1|a2);bz=~(b1|b2)
    return ((a1&bz)|(az&b1)|(a2&b2), (a2&bz)|(az&b2)|(a1&b1))

pivots=[];rank=0
for col in range(768):
    bit=1<<col
    pivot=next((i for i in range(rank,len(rows)) if (rows[i][0]|rows[i][1])&bit),None)
    if pivot is None:continue
    rows[rank],rows[pivot]=rows[pivot],rows[rank]
    if rows[rank][1]&bit:rows[rank]=rows[rank][::-1]
    positive=rows[rank];negative=positive[::-1]
    for i in range(len(rows)):
        if i==rank:continue
        one,two=rows[i]
        if one&bit:rows[i]=add(rows[i],negative)
        elif two&bit:rows[i]=add(rows[i],positive)
    pivots.append(col);rank+=1
assert all(a==b==0 for a,b in rows[rank:])
free_columns=[j for j in range(768) if j not in set(pivots)]
basis=[];basis_planes=[]
for col in free_columns:
    x=[0]*768;x[col]=1
    bit=1<<col
    for r,pivot in enumerate(pivots):
        coefficient=1 if rows[r][0]&bit else (2 if rows[r][1]&bit else 0)
        x[pivot]=(-coefficient)%3
    one=sum(1<<i for i,c in enumerate(x) if c==1)
    two=sum(1<<i for i,c in enumerate(x) if c==2)
    for a,b in original:
        dot=(a&one).bit_count()+(b&two).bit_count()-(a&two).bit_count()-(b&one).bit_count()
        assert dot%3==0
    basis.append(x);basis_planes.append((one,two))
assert len(basis)==768-rank
save('KERNEL_BASIS.json',dict(field=3,rank=rank,dimension=len(basis),pivots=pivots,
    free_columns=free_columns,basis_vectors=basis,
    convention='Each row is768 GF3 coefficients in controller-major order; all coefficient combinations are allowed',
    all_basis_vectors_verified_against_all_original_rows=True))
print(json.dumps(dict(stage='KERNEL_COMPLETE',pid=os.getpid(),rank=rank,dimension=len(basis),
                      CPU_seconds=time.process_time()-START)),flush=True)

def span_basis(vectors):
    result=[]
    for v in vectors:
        v=v[:]
        for p,b in result:
            c=v[p]
            if c:v=[(a-c*z)%3 for a,z in zip(v,b)]
        p=next((i for i,c in enumerate(v) if c),None)
        if p is None:continue
        inv=1 if v[p]==1 else 2
        v=[c*inv%3 for c in v]
        result.append((p,v));result.sort()
    return [v for p,v in result]

def full_span(basis):
    vectors=[(0,0,0,0)]
    for b in basis:
        old=vectors
        vectors=[tuple((a+c*z)%3 for a,z in zip(v,b)) for v in old for c in range(3)]
    assert len(set(vectors))==3**len(basis)
    return vectors

digits=[tuple((x//(3**i))%3 for i in range(4)) for x in range(81)]
def shift(x,h):return sum(((a+b)%3)*3**i for i,(a,b) in enumerate(zip(digits[x],h)))
ports=list(map(int,FREE.read_text().split()))
assert len(ports)==len(set(ports))==648
portset=set(ports);byfiber=defaultdict(set)
for v in ports:byfiber[v//81].add(v%81)
projection=[];orbits=[]
for u in range(192):
    image_basis=span_basis([x[4*u:4*u+4] for x in basis])
    image=full_span(image_basis)
    original_offsets=byfiber.get(u,set())
    entry=dict(controller=u,projection_rank=len(image_basis),image_basis=image_basis,
               image_subspace_size=len(image),free_port_count=len(original_offsets),free_orbit_ids=[])
    remaining=set(original_offsets)
    while remaining:
        x=min(remaining)
        orbit={shift(x,h) for h in image}
        assert len(orbit)==len(image) and orbit<=original_offsets and orbit<=remaining
        oid=len(orbits)
        orbits.append(dict(orbit=oid,controller=u,representative=81*u+x,
            old_labels=sorted(81*u+y for y in orbit),size=len(orbit)))
        entry['free_orbit_ids'].append(oid)
        remaining-=orbit
    projection.append(entry)
assert sum(o['size'] for o in orbits)==648
for x in basis:
    for v in ports:
        u,a=divmod(v,81)
        assert 81*u+shift(a,x[4*u:4*u+4]) in portset
save('FIBER_PROJECTIONS.json',dict(controller_count=192,fibers=projection))
save('FREE_PORT_ORBITS.json',dict(ports=648,orbit_count=len(orbits),orbits=orbits,
    automorphism_group='All synchronized fiber translations in saved KERNEL_BASIS; projected shifts are not independent across fibers',
    orbit_representatives=[o['representative'] for o in orbits]))
nontrivial=any(o['size']>1 for o in orbits)
result=dict(status='NONTRIVIAL_FREEPORT_TRANSLATION_ACTION' if nontrivial else 'NO_NONTRIVIAL_FREEPORT_TRANSLATION_ACTION',
    pid=os.getpid(),source_n=15552,source_m=116316,controllers=192,fiber_dimension=4,
    equations=2880,unknowns=768,rank=rank,kernel_dimension=len(basis),
    translation_group_order=3**len(basis),all_arcs=960,unique_target_bins_per_controller=5,
    all_basis_equations_checked=True,deleted_virtual_loops_preserved=True,
    all_fiber_projection_rank_histogram=dict(sorted(Counter(p['projection_rank'] for p in projection).items())),
    free_fiber_count=len(byfiber),free_fiber_size_histogram=dict(sorted(Counter(map(len,byfiber.values())).items())),
    free_fiber_projection_rank_histogram=dict(sorted(Counter(projection[u]['projection_rank'] for u in byfiber).items())),
    literal_free_ports=648,free_port_orbit_count=len(orbits),free_port_orbit_size_histogram=dict(sorted(Counter(o['size'] for o in orbits).items())),
    freeport_transitive=len(orbits)==1,
    K2_symmetry_reduction_supported=nontrivial,
    safe_single_anchor_disjunction=('At least one selected A or B port belongs to the union of one representative from each actual orbit; one common global translation only' if nontrivial else 'No nontrivial port-selector reduction from this translation group'),
    fixed_A0_justified=False,independent_fiber_translations_claimed=False,
    CPU_seconds=time.process_time()-START,wall_seconds=time.monotonic()-WALL,CPU_budget=15,
    literal_source_graph_reads=0,graph_exports=0,BFS_runs=0,solver_calls=0,running=False,pending=[])
assert result['CPU_seconds']<15
for name in ['RESULT.json','TERMINAL.json','HANDLE.json']:save(name,result)
print(json.dumps(result),flush=True)
