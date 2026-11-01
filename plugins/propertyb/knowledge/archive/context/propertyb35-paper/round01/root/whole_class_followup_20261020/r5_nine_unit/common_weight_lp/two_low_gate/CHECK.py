"""Complete four-lock pairbudget domain: degrees6,6,8,8; xy=4;
all other five pairs1. Ordinary ABC concrete-layout certificates only.
"""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[7]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from bare_layout import BareLayout
from independent_structure_bounds import independent_rows
pairs=list(combinations(range(4),2));bud=[4 if (i,j)==(2,3) else 1 for i,j in pairs]
large=[t for t in range(16) if t.bit_count()>=3]
start=time.process_time();domain=[];excluded=0
for bits in product([0,1],repeat=len(large)):
    ns={t:1 for t,v in zip(large,bits) if v}
    used=[sum(n for t,n in ns.items() if t>>i&1 and t>>j&1) for i,j in pairs]
    if any(u>b for u,b in zip(used,bud)):excluded+=1;continue
    for (i,j),b,u in zip(pairs,bud,used):
        if b-u:ns[(1<<i)|(1<<j)]=b-u
    degrees=[6,6,8,8]
    for i,d in enumerate(degrees):
        single=d-sum(n for t,n in ns.items() if t>>i&1)
        assert single>=0
        if single:ns[1<<i]=single
    empty=35-sum(ns.values());assert empty>=0
    if empty:ns[0]=empty
    assert sum(ns.values())==35
    assert [sum(n for t,n in ns.items() if t>>i&1) for i in range(4)]==degrees
    assert [sum(n for t,n in ns.items() if t>>i&1 and t>>j&1) for i,j in pairs]==bud
    domain.append({'large_traces':sorted(t for t,n in ns.items() if t.bit_count()>=3),'counts':ns})
assert len(domain)==7 and excluded==25
profiles=domain[:2] if 'profile' in sys.argv else domain
records=[]
for ident,z in enumerate(profiles):
    ns=z['counts'];tm=time.process_time()
    # Seed only already-used three-lock positions plus two neighboring
    # alternatives for the extra low. No new full position menu.
    old_positions=[(12,13,11,25),(13,12,11,25),(14,13,11,25),(10,13,11,25)]
    seed,seedpos=min((BareLayout(25,pos).bound(ns),pos) for pos in old_positions)
    eng=SubsetEngine(25,4,ns)
    for p in eng.inv:eng.inv[p]=(0,0,[])
    proposal=eng.solve();pos=proposal['positions']
    raw,abc=BareLayout(25,pos).bound(ns,with_rows=True)
    ir=independent_rows(25,pos,[frozenset(i+1 for i in range(4) if t>>i&1) for t,n in ns.items() for _ in range(n)])
    assert [(a['A'],a['B'],a['C']) for a in ir]==abc
    assert raw==proposal['bound']==sum((min(a,b,c) for a,b,c in abc),Q())
    assert raw<=seed
    records.append({'id':ident,**z,'positions':pos,'raw_bound':str(raw),'strict':raw<1,
       'seed_positions':seedpos,'seed_bound':str(seed),'independent_ABC':True,
       'raw_rows':[[str(v) for v in row] for row in abc],'CPU_seconds':time.process_time()-tm})
summary={'scope':__doc__,'complete_domain_profiles':len(domain),'large_mask_assignments':32,'pairbudget_exclusions':excluded,
         'complete_probability_run':len(records)==7,'processed':len(records),'strict':sum(z['strict'] for z in records),
         'all_strict':len(records)==7 and all(z['strict'] for z in records),'CPU_seconds':time.process_time()-start}
out={'summary':summary,'domain':domain,'records':records}
(P/('PROFILE.json' if len(records)<7 else 'RESULT.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(summary,indent=2))
print([(z['large_traces'],z['raw_bound'],z['positions']) for z in records])
