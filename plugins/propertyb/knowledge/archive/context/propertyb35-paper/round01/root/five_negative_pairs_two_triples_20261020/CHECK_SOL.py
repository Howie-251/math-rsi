from itertools import combinations, combinations_with_replacement, product
from fractions import Fraction
from pathlib import Path
import json
import time

start=time.process_time()
edges=list(combinations(range(8),2)) # f,g plus up to six other endpoints
cases={'v0':0,'v1_fg':0,'v1_no_fg':0,'v2':0,'v3':0}
false_claim_examples=[]
total=0
for size in range(4):
    for K in combinations_with_replacement(edges,size):
        total+=1
        deg=[sum(i in e for e in K) for i in (0,1)]
        f,g=(0,1) if deg[0]<=deg[1] else (1,0)
        v=min(deg)
        fg=tuple(sorted((f,g)))
        if v==0:
            cases['v0']+=1
        elif v==1 and fg in K:
            cases['v1_fg']+=1
        elif v==1:
            assert sum(g in e for e in K)>=1
            assert any(g in e and f not in e for e in K)
            assert sum(f not in e and g not in e for e in K)<=1
            cases['v1_no_fg']+=1
        elif v==2:
            assert fg in K
            neighbors={j for e in K if f in e for j in e if j!=f}
            assert g in neighbors and len(neighbors-{g})<=1
            remaining=[e for e in K if not(set(e)&neighbors)]
            assert all(f not in e for e in remaining) and len(remaining)<=1
            bad=[e for e in K if f not in e and g not in e]
            if bad: false_claim_examples.append([list(e) for e in K])
            cases['v2']+=1
        else:
            assert v==3 and len(K)==3 and all(e==fg for e in K)
            cases['v3']+=1

assert [[0,1],[0,1],[2,3]] in false_claim_examples
geometry=[]
for r in (2,3):
    for size in range(r+1):
        F=set(range(size))
        subsets=[set(c) for k in range(size+1) for c in combinations(F,k)]
        for Uf,Vf in product(subsets,repeat=2):
            a,b=4-len(Uf),4-len(Vf)
            if a*b>5-r+min(2,5-r): continue
            if r==2: assert size==2 and Uf==Vf==F and a==b==2
            elif not(Uf&Vf): assert sorted((a,b))==[1,4] and size==3
            geometry.append([r,size,sorted(Uf),sorted(Vf),a,b])

loss_candidates=[]
for da,db in product(range(3),repeat=2):
    if da+db>2:continue
    candidates=(3-da)*(3-db)*2
    assert candidates>=6
    loss_candidates.append([da,db,candidates])
assert Fraction(24)+Fraction(31,2)*5+Fraction(13,4)*2==108<256
strict=[(16,7),(9,6),(9,5),(9,4),(4,3),(9,2),(6,2)]
assert all(a>b for a,b in strict)
result={'status':'PASS_AFTER_LOCAL_PROOF_CORRECTION','K_total':total,'K_cases':cases,
        'false_intermediate_claim_examples':false_claim_examples,'F_geometry':geometry,
        'AB_losses':loss_candidates,'strict_comparisons':strict,
        'cpu_seconds':time.process_time()-start,
        'scope':'<=3 indexed pair graphs, F intersections, and two-point loss scalars only'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('F_geometry','false_intermediate_claim_examples')}))
