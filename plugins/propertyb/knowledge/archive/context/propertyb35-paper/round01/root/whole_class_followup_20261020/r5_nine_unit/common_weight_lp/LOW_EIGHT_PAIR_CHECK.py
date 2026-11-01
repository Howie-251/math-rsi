"""Exactly four actual three-lock profiles: d=(6,8,8), zx=zy=1,
xy=c in{4,5}, inclusive triple t in{0,1}. Ordinary ABC, no quotas.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[6]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from bare_layout import BareLayout
from independent_structure_bounds import independent_rows
start=time.process_time();records=[]
for c in [4,5]:
    for t in [0,1]:
        ns={k:n for k,n in {7:t,3:1-t,5:1-t,6:c-t,1:4+t,2:7-c+t,4:7-c+t,0:15+c-t}.items() if n}
        assert sum(ns.values())==35
        assert [sum(n for u,n in ns.items() if u>>i&1) for i in range(3)]==[6,8,8]
        assert [sum(n for u,n in ns.items() if u>>i&1 and u>>j&1) for i,j in combinations(range(3),2)]==[1,1,c]
        eng=SubsetEngine(25,3,ns)
        # Set every optional quota lower bound to zero. This intentionally
        # weakens to ordinary C; it asserts no property of the actual H.
        for p in eng.inv:eng.inv[p]=(0,0,[])
        tm=time.process_time();w=eng.solve();pos=w['positions']
        raw,abc=BareLayout(25,pos).bound(ns,with_rows=True)
        ir=independent_rows(25,pos,[frozenset(i+1 for i in range(3) if u>>i&1) for u,n in ns.items() for _ in range(n)])
        assert [(z['A'],z['B'],z['C']) for z in ir]==abc
        assert raw==w['bound']==sum((min(a,b,c) for a,b,c in abc),Q())
        records.append({'lambda_xy':c,'triple_inclusive':t,'counts':ns,'positions':pos,'raw_bound':str(raw),
                        'strict':raw<1,'independent_raw_ABC':True,'raw_rows':[[str(v) for v in z] for z in abc],'CPU_seconds':time.process_time()-tm})
out={'scope':__doc__,'complete_four_profiles':True,'all_strict':all(z['strict'] for z in records),'strict':sum(z['strict'] for z in records),
     'CPU_seconds':time.process_time()-start,'records':records}
(P/'LOW_EIGHT_PAIR_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
