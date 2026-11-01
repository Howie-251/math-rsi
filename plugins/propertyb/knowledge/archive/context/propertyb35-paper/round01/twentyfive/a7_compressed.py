"""Exact symmetry-compressed a7 two-matching extensions.
Only checked automorphisms of the actual labelled unit7 inventory are used.
The first extra vertex is kept fixed when normalizing old labels; the second
special partner ranges over stabilizer orbits distinct from the first partner.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
import sys,json,time
P=Path(__file__).resolve().parent;R=P.parents[3];S=R/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True
sys.path[:0]=[str(P),str(S),str(R/'computations'),str(R/'computations/propertyb33/round01')]
from a8_extension import extend
from bare_layout import BareLayout
from multilock import Profile,json_value
from pure_quota import certificate

def action(ns,p):
    n=len(p)
    return tuple(sorted((sum(1<<p[i] for i in range(n) if t>>i&1)+(t&~((1<<n)-1)),c) for t,c in ns.items()))

def representative_labels(labels,autos):
    seen=set()
    for x in labels:
      if x in seen:continue
      yield x
      seen.update(p[x] for p in autos)

def find_bound(ns,n):
    best=None
    for a in sorted(range(1,27-n),key=lambda a:abs(a-(26-n)/2)):
        eng=engines[n][a];bare,abc=eng.bound(ns,True);p=Profile(25,5,eng.pos,ns)
        losses={eng.pos[i]:certificate(p,i)['loss'] for i in range(n)}
        val=sum((min(x,y,z-losses.get(k,Q())) for k,(x,y,z) in enumerate(abc,1)),Q())
        if best is None or val<best['bound']:best=dict(bound=val,bare=bare,positions=eng.pos,losses=losses)
        if val<1:return best
    return best
engines={n:{a:BareLayout(25,range(a,a+n)) for a in range(1,27-n)} for n in (8,9)}
st=time.perf_counter();sources=json.loads((P/'UNIT7_SCREEN.json').read_text())['results']
stage1=[];stage2=[];parents=[]
for source in sources:
    if not source['feasible'] or Q(source['bound'])<1:continue
    ns={int(t):c for t,c in source['counts'].items()};key=tuple(sorted(ns.items()))
    autos=[p for p in permutations(range(7)) if action(ns,p)==key]
    for special1 in representative_labels(range(7),autos):
        g=[p for p in autos if p[special1]==special1];seen1=set();raw1=raw2=0
        for nc in extend(ns,7,special1):
            raw1+=1;k1=tuple(sorted(nc.items()))
            if k1 in seen1:continue
            seen1.update(action(nc,p) for p in g)
            z=find_bound(nc,8);id1=len(stage1)
            stage1.append(dict(parent=source['base'],special=special1,counts=nc,orbit_group_size=len(g),**z))
            if z['bound']<1:continue
            stabilizer=[p for p in g if action(nc,p)==k1]
            for special2 in representative_labels([i for i in range(7) if i!=special1],stabilizer):
                g2=[p for p in stabilizer if p[special2]==special2];seen2=set()
                for nd in extend(nc,8,special2):
                    raw2+=1;k2=tuple(sorted(nd.items()))
                    if k2 in seen2:continue
                    seen2.update(action(nd,p) for p in g2)
                    stage2.append(dict(parent=id1,special=special2,counts=nd,orbit_group_size=len(g2),**find_bound(nd,9)))
        parents.append(dict(parent=source['base'],special=special1,source_automorphisms=len(autos),first_partner_stabilizer=len(g),raw_stage1=raw1,raw_stage2=raw2))
        print('parent',source['base'],special1,'raw',raw1,raw2,'orbits',len(stage1),len(stage2),'sec',time.perf_counter()-st,flush=True)
summary=dict(scope=__doc__,complete=True,parents=parents,stage1_orbits=len(stage1),stage1_strict=sum(z['bound']<1 for z in stage1),stage2_orbits=len(stage2),stage2_strict=sum(z['bound']<1 for z in stage2),stage2_residual=sum(z['bound']>=1 for z in stage2),maximum_stage2=max((z['bound'] for z in stage2),default=Q()),elapsed_seconds=time.perf_counter()-st)
(P/'A7_COMPRESSED.json').write_text(json.dumps(json_value(dict(summary=summary,stage1=stage1,stage2=stage2)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
