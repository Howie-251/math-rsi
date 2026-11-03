from pathlib import Path
from collections import defaultdict,Counter
import json,time

P=Path(__file__).resolve().parent
t=time.process_time()
X=[[0,1,4,10],[0,2],[0,5],[0],[0]]
names=[f'alpha{i}' for i in range(5)]+[f'beta{k}' for k in range(5)]+[f'gamma{i}{k}' for i in range(1,5) for k in range(1,5)]
assert len(names)==26
zero=(0,)*26
def unit(j,sign):
    coeff=[0]*26
    if j is not None:coeff[j]=sign%17
    return tuple(coeff)
def gi(i,k):return 10+(i-1)*4+k-1 if i and k else None
def steps(layer,row,j):
    result=[]
    for sign in [-1,1]:
        result.append((layer,row,(j+(1 if layer==0 else 2)*sign)%5,unit((0 if layer==0 else 5)+row,sign),0))
    if layer==0:
        i=row
        for k in range(5):
            for c in X[(k-i)%5]:result.append((1,k,(j+i*k)%5,unit(gi(i,k),1),c))
    else:
        k=row
        for i in range(5):
            for c in X[(k-i)%5]:result.append((0,i,(j-i*k)%5,unit(gi(i,k),-1),-c%17))
    assert len(result)==12
    return result
def code(l,i,j):return 25*l+5*i+j
base=[]
for l in range(2):
    for i in range(5):
        for j in range(5):base.append(sorted({code(nl,k,v) for nl,k,v,coeff,c in steps(l,i,j)}))
assert all(len(row)==7 for row in base)
# Exact isomorphism to the independently checked old HS50 projection.
def old_vertex(l,i,j):return code(l,i,(j+(3*i*i if l==0 else -3*i*i))%5)
old=[set() for _ in range(50)]
for l in range(2):
    for i in range(5):
        for j in range(5):
            u=code(l,i,j)
            for sign in [-1,1]:old[u].add(code(l,i,(j+(1 if l==0 else 2)*sign)%5))
            for d in range(5):old[u].add(code(1-l,(i+(d if l==0 else -d))%5,(j+((-3*d*d) if l==0 else 3*d*d))%5))
mapping=[old_vertex(l,i,j) for l in range(2) for i in range(5) for j in range(5)]
assert sorted(mapping)==list(range(50))
assert all({mapping[v] for v in base[u]}==old[mapping[u]] for u in range(50))
records=[]
for layer in range(2):
    for index in range(5):
        frontier={(layer,index,0,zero,0)};allstates=set(frontier)
        for depth in range(3):
            nxt=set()
            for l,i,j,coeff,c in frontier:
                for nl,k,v,extra,constant in steps(l,i,j):
                    nxt.add((nl,k,v,tuple((a+b)%17 for a,b in zip(coeff,extra)),(c+constant)%17))
            allstates.update(nxt);frontier=nxt
        slots=defaultdict(set)
        for l,i,j,coeff,c in allstates:slots[l,i,j].add((coeff,c))
        root=code(layer,index,0);targets=[]
        for l in range(2):
            for i in range(5):
                for j in range(5):
                    forms=slots[l,i,j]
                    families=defaultdict(set)
                    for coeff,c in forms:families[coeff].add(c)
                    auto=any(len(row)==17 for row in families.values())
                    v=code(l,i,j)
                    kind='same' if v==root else 'adjacent' if v in base[root] else 'nonadjacent'
                    if kind!='nonadjacent':assert auto
                    targets.append(dict(target=[l,i,j],kind=kind,capacity=len(forms),automatic_constant_family=auto,
                                        forms=[dict(coeff=list(co),constant=c) for co,c in sorted(forms)]))
        minimum=min(row['capacity'] for row in targets)
        records.append(dict(root=[layer,index,0],minimum_capacity=minimum,
                            tight_slots=[row['target'] for row in targets if row['capacity']==minimum],
                            obstructed_slots=[row['target'] for row in targets if row['capacity']<17],slots=targets))
minimum=min(r['minimum_capacity'] for r in records)
out=dict(status='SYMBOLIC_CAPACITY_PASSES_NOT_EXISTENCE' if minimum>=17 else 'SYMBOLIC_CAPACITY_OBSTRUCTION_STOP',
         vertices=850,degree=12,base_vertices=50,variable_count=26,parameter_order=names,X_sets=X,
         cross_rule='U(i,j,z)--V(k,j+i*k,z+gamma_ik+c), c in X_(k-i)',
         gauge='gamma_0k=gamma_i0=0; free gamma_ik for i,k in 1..4',
         gauge_proof='A potential u_i on each U row and v_k on each V row changes gamma_ik to gamma_ik+u_i-v_k. Taking u_0=0, v_k=gamma_0k, u_i=gamma_00-gamma_i0 makes the zero row and zero column vanish. Internal alpha_i/beta_k are unchanged.',
         translation_proof='For common t in C5,w in C17, U(i,j,z)->U(i,j+t,z+w), V(k,l,z)->V(k,l+t,z+w) preserve every internal edge and l=j+i*k cross rule. The action is free and transitive on each of the ten row/layer sets of size 85, so these ten roots suffice for all 850 vertices.',
         source_projection_isomorphism=dict(verified_edge_by_edge=True,new_U_to_old='(i,j+3*i^2)',new_V_to_old='(k,l-3*k^2)',
             old_source='../hs850_branch_lift/SCREEN.json',diameter=2,girth=5,degree=7),
         roots=records,minimum_capacity=minimum,
         tight_root_targets=[dict(root=r['root'],targets=r['tight_slots']) for r in records if r['minimum_capacity']==minimum],
         self_and_adjacent_automatic_family_verified=True,
         CPU_seconds=time.process_time()-t,parameter_assignments_tested=0,graphs_generated=0,ordinary_BFS_performed=False)
(P/'SCREEN.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],'minimum',minimum,'CPU',out['CPU_seconds'])
for r in records:print(r['root'],'min',r['minimum_capacity'],'tight',r['tight_slots'],'fail',r['obstructed_slots'])
