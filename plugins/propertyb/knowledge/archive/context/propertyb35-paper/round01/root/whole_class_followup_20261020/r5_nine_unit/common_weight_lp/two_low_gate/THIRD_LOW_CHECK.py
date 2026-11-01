"""Only the two actual forced five-lock profiles, no complete new catalogue.
Three degree6 low locks0,1,2; x/y locks3,4 degree8 and lambda4.
Selected T counts2 or3; other selected lows not on any xy common edge.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[7]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from bare_layout import BareLayout
from independent_structure_bounds import independent_rows
start=time.process_time();records=[]
for k in [2,3]:
    ns={3:1,5:1,6:1,24:4-k}
    for i in range(k):ns[24|(1<<i)]=1
    for i in range(k,3):ns[8|(1<<i)]=1;ns[16|(1<<i)]=1
    for i in range(5):
        d=6 if i<3 else 8
        n=d-sum(n for t,n in ns.items() if t>>i&1)
        assert n>=0
        if n:ns[1<<i]=n
    ns[0]=35-sum(ns.values());assert ns[0]>=0
    assert sum(ns.values())==35
    assert [sum(n for t,n in ns.items() if t>>i&1) for i in range(5)]==[6,6,6,8,8]
    assert all(sum(n for t,n in ns.items() if t>>i&1 and t>>j&1)==(4 if (i,j)==(3,4) else 1) for i,j in combinations(range(5),2))
    assert all((t&7).bit_count()<=2 for t in ns)
    tm=time.process_time();eng=SubsetEngine(25,5,ns)
    for p in eng.inv:eng.inv[p]=(0,0,[])
    w=eng.solve();pos=w['positions']
    raw,abc=BareLayout(25,pos).bound(ns,with_rows=True)
    ir=independent_rows(25,pos,[frozenset(i+1 for i in range(5) if t>>i&1) for t,n in ns.items() for _ in range(n)])
    assert raw==w['bound']==sum((min(a,b,c) for a,b,c in abc),Q())
    assert [(r['A'],r['B'],r['C']) for r in ir]==abc
    records.append({'selected_T_lows':k,'counts':ns,'positions':pos,'raw_bound':str(raw),'strict':raw<1,
                    'independent_raw_ABC':True,'CPU_seconds':time.process_time()-tm,'raw_rows':[[str(v) for v in z] for z in abc]})
out={'scope':__doc__,'complete_two_forced_profiles':True,'strict':sum(z['strict'] for z in records),
     'CPU_seconds':time.process_time()-start,'records':records}
(P/'THIRD_LOW_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
print([(z['selected_T_lows'],z['raw_bound'],z['positions']) for z in records])
