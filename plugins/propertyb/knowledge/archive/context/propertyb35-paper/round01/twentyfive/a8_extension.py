"""All one-matching-pair extensions of the two eight-unit residuals.
Uses actual trace splitting, multiplicities, and lambda target (2,1,...,1).
Exact enumeration and corrected probability bounds; no hypergraph enumeration.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
P=Path(__file__).resolve().parent;R=P.parents[3];S=R/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True
sys.path[:0]=[str(S),str(R/'computations'),str(R/'computations/propertyb33/round01')]
from bare_layout import BareLayout
from multilock import Profile,json_value
from pure_quota import certificate

def extend(ns,n,special):
    types=sorted(t for t,c in ns.items() if t and c and t.bit_count()<=4)
    target=[1]*n;target[special]=2;seen=set()
    def rec(rem,picked):
        if not any(rem):
            key=tuple(sorted(picked))
            if key in seen:return
            seen.add(key)
            nc=dict(ns);b=1<<n
            for t in picked:
                nc[t]-=1;nc[t|b]=nc.get(t|b,0)+1
            sing=7-len(picked)
            if sing<0 or ns.get(0,0)<sing:return
            nc[b]=sing;nc[0]=ns.get(0,0)-sing
            yield {t:c for t,c in nc.items() if c}
            return
        i=next(i for i,x in enumerate(rem) if x)
        for t in types:
            if not t>>i&1 or picked.count(t)>=ns[t]:continue
            inds=[j for j in range(n) if t>>j&1]
            if all(rem[j] for j in inds):
                rr=list(rem)
                for j in inds:rr[j]-=1
                yield from rec(rr,picked+[t])
    yield from rec(target,[])

def bound(ns,engines):
    best=None
    for eng in engines:
        bare,abc=eng.bound(ns,True);p=Profile(25,5,eng.pos,ns)
        losses={eng.pos[i]:certificate(p,i)['loss'] for i in range(len(eng.pos))}
        val=sum((min(a,b,c-losses.get(k,Q())) for k,(a,b,c) in enumerate(abc,1)),Q())
        if best is None or val<best['bound']:best=dict(bound=val,bare=bare,positions=eng.pos,losses=losses)
    return best
if __name__=='__main__':
    st=time.perf_counter();src=json.loads((P/'UNIT8_SCREEN.json').read_text())
    engines=[BareLayout(25,range(a,a+9)) for a in range(1,18)]
    out=[];parents=[]
    for parent in src['results']:
        if not parent['feasible'] or Q(parent['bound'])<1:continue
        ns={int(t):c for t,c in parent['counts'].items()};seen=set()
        for special in range(8):
            count=0
            for nc in extend(ns,8,special):
                count+=1;key=tuple(sorted(nc.items()))
                if key in seen:continue
                seen.add(key)
                z=bound(nc,engines)
                out.append(dict(parent=parent['base'],special=special,counts=nc,**z))
            parents.append(dict(parent=parent['base'],special=special,extensions=count))
    summary=dict(scope=__doc__,parents=parents,extensions=len(out),strict=sum(r['bound']<1 for r in out),residual=sum(r['bound']>=1 for r in out),maximum=max((r['bound'] for r in out),default=Q()),elapsed_seconds=time.perf_counter()-st)
    (P/'A8_EXTENSION.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n')
    print(json.dumps(json_value(summary),indent=2))
