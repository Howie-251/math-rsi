from pathlib import Path
from collections import Counter,defaultdict,deque
import json,time

P=Path(__file__).resolve().parent
t=time.process_time()
MOD=17
X=[[0,1,4,10],[0,2],[0,5],[0],[0]]
assert set((a-b)%17 for row in X for a in row for b in row)==set(range(17))
# Parameters are alpha,beta,gamma1,gamma2,gamma3,gamma4; gamma0 is zero.
def moves(layer):
    ans=[]
    for sign in [-1,1]:
        coeff=[0]*6;coeff[layer]=sign%17
        ans.append((layer,0,(1 if layer==0 else 2)*sign%5,tuple(coeff),0))
    for k,row in enumerate(X):
        for c in row:
            sign=1 if layer==0 else -1
            coeff=[0]*6
            if k:coeff[k+1]=sign%17
            ans.append((1-layer,sign*k%5,sign*((-3*k*k)%5)%5,tuple(coeff),sign*c%17))
    return ans
M=[moves(0),moves(1)]
assert all(len(row)==12 for row in M)
def base_moves(layer):
    return sorted({(l,x,y) for l,x,y,coeff,c in M[layer]})
base=[set() for _ in range(50)]
def code(l,x,y):return l*25+x*5+y
for l in range(2):
    for x in range(5):
        for y in range(5):
            u=code(l,x,y)
            for nl,dx,dy in base_moves(l):base[u].add(code(nl,(x+dx)%5,(y+dy)%5))
assert all(len(row)==7 for row in base)
assert all(u!=v and u in base[v] for u,row in enumerate(base) for v in row)
hist=Counter();diameter=0
for root in range(50):
    dist=[-1]*50;dist[root]=0;queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in base[u]:
            if dist[v]<0:dist[v]=dist[u]+1;queue.append(v)
    assert min(dist)>=0;hist.update(dist);diameter=max(diameter,max(dist))
assert diameter==2
# No triangles or 4-cycles, plus an explicit pentagon from U internal steps.
assert all(not base[u]&base[v] for u,row in enumerate(base) for v in row)
assert all(len(base[u]&base[v])<=1 for u in range(50) for v in range(u+1,50))
assert all(code(0,0,(y+1)%5) in base[code(0,0,y)] for y in range(5))
root_records=[]
for layer in [0,1]:
    frontier={(layer,0,0,(0,)*6,0)};allstates=set(frontier)
    raw_counts=[]
    for depth in range(1,4):
        nxt=set()
        for l,x,y,coeff,c in frontier:
            for nl,dx,dy,extra,constant in M[l]:
                nxt.add((nl,(x+dx)%5,(y+dy)%5,tuple((a+b)%17 for a,b in zip(coeff,extra)),(c+constant)%17))
        raw_counts.append(len(nxt));allstates.update(nxt);frontier=nxt
    slots=defaultdict(set)
    for l,x,y,coeff,c in allstates:slots[l,x,y].add((coeff,c))
    root=code(layer,0,0);records=[]
    for l in range(2):
        for x in range(5):
            for y in range(5):
                forms=slots[l,x,y]
                buckets=defaultdict(set)
                for coeff,c in forms:buckets[coeff].add(c)
                automatic=any(len(v)==17 for v in buckets.values())
                baseid=code(l,x,y)
                kind='same' if baseid==root else 'adjacent' if baseid in base[root] else 'nonadjacent'
                if kind!='nonadjacent':assert automatic
                records.append(dict(target=[l,x,y],kind=kind,distinct_complete_mod17_affine_forms=len(forms),
                                    automatic_full_constant_family=automatic,
                                    forms=[dict(coeff=list(coeff),constant=c) for coeff,c in sorted(forms)]))
    minimum=min(r['distinct_complete_mod17_affine_forms'] for r in records)
    root_records.append(dict(root=[layer,0,0],full_walk_depth_form_counts=raw_counts,all_depth_deduplicated_forms=len(allstates),
                             minimum_capacity=minimum,tight_slots=[r['target'] for r in records if r['distinct_complete_mod17_affine_forms']==minimum],
                             obstructed_slots=[r['target'] for r in records if r['distinct_complete_mod17_affine_forms']<17],
                             target_kind_histogram=dict(Counter(r['kind'] for r in records)),slots=records))
out=dict(status='SYMBOLIC_CAPACITY_PASSES_NOT_EXISTENCE' if all(not r['obstructed_slots'] for r in root_records) else 'SYMBOLIC_CAPACITY_OBSTRUCTION_STOP',
         group='F5^2 x C17',parameter_order=['alpha','beta','gamma1','gamma2','gamma3','gamma4'],X_sets=X,
         gamma0=0,vertices=850,degree=12,
         base=dict(vertices=50,degree_histogram={7:50},simple=True,edges=175,diameter=diameter,girth=5,
                   all_root_BFS_sources=50,ordered_distance_histogram=dict(hist)),
         cross_return_constant_differences=sorted({(a-b)%17 for row in X for a in row for b in row}),
         roots=root_records,CPU_seconds=time.process_time()-t,actual_parameter_assignments_tested=0,
         lift_BFS_performed=False,full_graph_generated=False,
         translation_proof='For any h in F5^2 x C17, U_g->U_(g+h) and V_g->V_(g+h) preserve all internal displacements and all U_g--V_(g+s) edges. Translations act transitively on each layer. Thus roots U_0 and V_0 cover all vertices, without requiring a layer-swapping automorphism.')
(P/'SCREEN.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],'CPU',out['CPU_seconds'])
for r in root_records:print('root',r['root'],'min',r['minimum_capacity'],'tight',r['tight_slots'],'obstructed',r['obstructed_slots'])
