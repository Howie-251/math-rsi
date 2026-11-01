"""Five real G degree7 locks plus one real degree6 low lock.
Rebind exactly245 old stored layouts, raw ABC only, no DP or new positions.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
from collections import Counter
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[6]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from bare_layout import BareLayout
from independent_structure_bounds import independent_rows
OLD=ROOT/'context/propertyb35-paper/round01/twentyfive'
old=json.loads((OLD/'GROUP5_EXTERNAL_STAR_COMPLETE.json').read_text())
cat=json.loads((OLD/'GROUP5_CATALOGUE.json').read_text())
mu_by_id={z['id']:{int(t):n for t,n in z['counts'].items()} for z in cat['representatives']}
assert old['summary']['complete'] and len(old['results'])==245
parts=[()]
for i in range(5):
    nxt=[]
    for pp in parts:
        nxt.append(tuple(sorted(pp+(1<<i,))))
        for k,t in enumerate(pp):
            nxt.append(tuple(sorted(pp[:k]+pp[k+1:]+(t|(1<<i),))))
    parts=sorted(set(nxt))
parts.remove((31,));assert len(parts)==51
def serial(x):
    if isinstance(x,Fraction):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x
start=time.process_time();rows=[];layoutcache={}
limit=5 if 'profile' in sys.argv else 245
for z in old['results'][:limit]:
    mu=mu_by_id[z['id']];pp=tuple(sorted(z['partition']))
    ns={int(t):n for t,n in z['counts'].items()}
    assert ns.get(32,0)==7-len(pp)>=2
    ns[32]-=1;ns[0]=ns.get(0,0)+1
    restored={}
    for t,n in mu.items():
        xcount=int(t in pp) if t else 6-len(pp)
        assert 0<=xcount<=n
        if n-xcount:restored[t]=n-xcount
        if xcount:restored[t|32]=xcount
    assert ns==restored
    assert sum(ns.values())==35
    assert all(sum(n for t,n in ns.items() if t>>i&1)==(7 if i<5 else 6) for i in range(6))
    assert all(sum(n for t,n in ns.items() if t>>i&1 and t>>j&1)==(2 if j<5 else 1) for i,j in combinations(range(6),2))
    p=tuple(z['positions'])
    if p not in layoutcache:layoutcache[p]=BareLayout(25,p)
    bound,ABC=layoutcache[p].bound(ns,with_rows=True)
    stubs=[frozenset(i+1 for i in range(6) if t>>i&1) for t,n in ns.items() for _ in range(n)]
    ir=independent_rows(25,p,stubs)
    assert [(v['A'],v['B'],v['C']) for v in ir]==ABC
    assert sum((min(a,b,c) for a,b,c in ABC),Fraction())==bound
    rows.append({'id':z['id'],'partition':pp,'counts':ns,'positions':p,'raw_bound':bound,'strict':bound<1,'independent_raw_ABC':True,'raw_rows':ABC})
families=[]
for ident in sorted({z['id'] for z in rows}):
    rr=[z for z in rows if z['id']==ident]
    if limit==245:
        expected={pp for pp in parts if all(mu_by_id[ident].get(t,0) for t in pp) and mu_by_id[ident].get(0,0)>=6-len(pp)}
        assert {z['partition'] for z in rr}==expected
    families.append({'id':ident,'partitions':len(rr),'strict':sum(z['strict'] for z in rr),
                     'residual_partitions':[z['partition'] for z in rr if not z['strict']],
                     'minimum':min(z['raw_bound'] for z in rr),'maximum':max(z['raw_bound'] for z in rr)})
out={'scope':'Only the18 no-full-G inventories in the old245 exact partition domain, with actual sixth-lock degree6; fixed old positions, noquota/noDP.',
     'complete_245':limit==245,'cases':len(rows),'strict':sum(z['strict'] for z in rows),'residual':sum(not z['strict'] for z in rows),
     'full_G_ids_not_covered':[23,24,25,26],'CPU_seconds':time.process_time()-start,'families':families,'records':rows}
(P/('PROFILE.json' if limit<245 else 'RESULT.json')).write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps(serial({k:v for k,v in out.items() if k not in ['families','records']}),indent=2),flush=True)
print([(z['id'],z['strict'],z['partitions'],str(z['minimum']),str(z['maximum'])) for z in families],flush=True)
