"""Small counterexample attacks for shared tau capacities, not a spectrum scan."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
from math import comb
from random import Random
import json,time

P=Path(__file__).resolve().parent;START=time.process_time()
vectors=list(product(range(1,5),repeat=4))
g4={tau:max(sum(z) for z in vectors if sum(comb(x-1,2) for x in z)<=tau) for tau in range(13)}
assert [g4[t] for t in range(5)]==[8,9,10,11,12]
row_cases=0
for a1 in range(21):
    for a2 in range(21-a1):
        for a3 in range(21-a1-a2):
            a4=20-a1-a2-a3
            total=a1+2*a2+3*a3+4*a4
            if total%4:continue
            d=total//4;rowtau=a3+3*a4;r=max(0,4*d-40)
            assert rowtau==4*d-40+a1+a4
            for off4,off3 in product(range(9),repeat=2):
                tau=rowtau+3*off4+off3
                assert a4+off4<=min(tau//3,tau-r)
                row_cases+=1

# Pair-covering actual simple5 examples on11 points: the quadratic-residue
# cyclic (11,5,2) design, then three distinct extra original edges. Reject
# codegree>4; no non-B property is assumed by the capacity lemmas.
base=[frozenset((i+x)%11 for x in (1,3,4,5,9)) for i in range(11)]
all_edges=[frozenset(z) for z in combinations(range(11),5)]
extra=[e for e in all_edges if e not in base]
rng=Random(20261020);examples=[]
for trial in range(200):
    edges=base+rng.sample(extra,3)
    deg=Counter(v for e in edges for v in e)
    lam=Counter(p for e in edges for p in combinations(sorted(e),2))
    if max(lam.values())>4:continue
    D2=sorted(deg.values(),reverse=True)[1]
    if D2<7:continue
    tau=sum(comb(x-1,2) for x in lam.values())
    h=Counter();C3=C4=n3=n4=0
    for i,j in combinations(range(len(edges)),2):
        G,J=edges[i],edges[j];intersection=G&J
        if len(intersection) not in (3,4):continue
        middles=0
        for F in edges:
            a=F&G;b=F&J
            if len(a)==len(b)==1 and a!=b:middles+=1
        if len(intersection)==3:
            n3+=1;C3+=middles
            cross=[lam[tuple(sorted((a,b)))] for a in G-J for b in J-G]
            local=sum(comb(x-1,2) for x in cross)
            assert local<=tau and middles<=sum(cross)
        else:
            n4+=1;C4+=middles
            uv=tuple(sorted((G|J)-intersection));h[uv]+=1
            assert middles<=lam[uv]
    for uv,number in h.items():
        u,v=uv
        assert number<=min(deg[u]-lam[uv],deg[v]-lam[uv])<=D2-lam[uv]
    assert sum(h.values())==n4
    a3=sum(x==3 for x in lam.values());a4=sum(x==4 for x in lam.values())
    assert tau==a3+3*a4
    # n11 version of the exact same row identity; n21 is checked above.
    r=max(0,4*max(deg.values())-2*(11-1))
    assert a4<=min(tau//3,tau-r)
    bounds=[4*n4,3*n4+(D2-4)*(tau//3),2*n4+(D2-3)*tau,
            3*n4+(D2-4)*min(tau//3,tau-r)]
    assert C4<=min(bounds)
    examples.append({'tau':tau,'degrees':sorted(deg.values()),'D2':D2,'n3':n3,'n4':n4,
                     'C3':C3,'C4':C4,'C4_bounds':bounds,'a4':a4,'r_general':r,
                     'h_nonzero':{str(k):v for k,v in h.items()}})
    if len(examples)==20:break
assert len(examples)==20
out={'status':'PASS_TINY_COUNTEREXAMPLE_ATTACKS','g4_tau0_to12':g4,
     'twenty_neighbor_row_and_offrow_abstract_cases':row_cases,
     'actual_H_examples':20,'actual_H_scope':'11points,14 distinct5edges,paircover,lambda<=4,D2>=7; capacity lemmas need no35edge/nonB hypothesis',
     'max_actual_C4':max(z['C4'] for z in examples),'examples':examples,
     'no_full_spectrum_or_H_search':True,'cpu_seconds':time.process_time()-START}
(P/'TINY_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='examples'})
