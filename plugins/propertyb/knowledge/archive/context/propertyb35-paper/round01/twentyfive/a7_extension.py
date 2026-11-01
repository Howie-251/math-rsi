"""Complete conditional two-matching-pair extension screen of unit7 residues.
First added vertex matches one original label; second matches a different
original label and is unit with the first added vertex. Stop branches strict
at eight locks; all remaining actual extensions go to nine locks.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
P=Path(__file__).resolve().parent;R=P.parents[3];S=R/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True
sys.path[:0]=[str(P),str(S),str(R/'computations'),str(R/'computations/propertyb33/round01')]
from a8_extension import extend
from bare_layout import BareLayout
from multilock import Profile,json_value
from pure_quota import certificate

def find_bound(ns,n):
    best=None
    for a in sorted(range(1,27-n),key=lambda a:abs(a-(26-n)/2)):
        eng=engines[n][a]
        bare,abc=eng.bound(ns,True);p=Profile(25,5,eng.pos,ns)
        losses={eng.pos[i]:certificate(p,i)['loss'] for i in range(n)}
        val=sum((min(x,y,z-losses.get(k,Q())) for k,(x,y,z) in enumerate(abc,1)),Q())
        if best is None or val<best['bound']:best=dict(bound=val,bare=bare,positions=eng.pos,losses=losses)
        if val<1:return best
    return best
engines={n:{a:BareLayout(25,range(a,a+n)) for a in range(1,27-n)} for n in (8,9)}
st=time.perf_counter();sources=json.loads((P/'UNIT7_SCREEN.json').read_text())['results']
stage1=[];stage2=[];parents=[];cache={8:{},9:{}};budget=240
for source in sources:
    if not source['feasible'] or Q(source['bound'])<1:continue
    ns={int(t):c for t,c in source['counts'].items()}
    for special1 in range(7):
        count1=count2=0
        for nc in extend(ns,7,special1):
            count1+=1;key=tuple(sorted(nc.items()))
            if key not in cache[8]:cache[8][key]=find_bound(nc,8)
            z=cache[8][key]
            id1=len(stage1);stage1.append(dict(parent=source['base'],special=special1,counts=nc,**z))
            if z['bound']<1:continue
            for special2 in range(7):
                if special2==special1:continue
                for nd in extend(nc,8,special2):
                    count2+=1;key2=tuple(sorted(nd.items()))
                    if key2 not in cache[9]:cache[9][key2]=find_bound(nd,9)
                    stage2.append(dict(parent=id1,special=special2,counts=nd,**cache[9][key2]))
        parents.append(dict(parent=source['base'],special=special1,stage1=count1,stage2=count2))
        print('parent',source['base'],special1,count1,count2,'elapsed',time.perf_counter()-st,flush=True)
        if time.perf_counter()-st>budget:break
    if time.perf_counter()-st>budget:break
complete=len(parents)==sum(r['feasible'] and Q(r['bound'])>=1 for r in sources)*7
summary=dict(scope=__doc__,complete=complete,parents=parents,stage1=len(stage1),stage1_strict=sum(z['bound']<1 for z in stage1),stage2=len(stage2),stage2_strict=sum(z['bound']<1 for z in stage2),stage2_residual=sum(z['bound']>=1 for z in stage2),maximum_stage2=max((z['bound'] for z in stage2),default=Q()),elapsed_seconds=time.perf_counter()-st)
(P/'A7_EXTENSION.json').write_text(json.dumps(json_value(dict(summary=summary,stage1=stage1,stage2=stage2)),indent=2)+'\n')
print(json.dumps(json_value(summary),indent=2))
