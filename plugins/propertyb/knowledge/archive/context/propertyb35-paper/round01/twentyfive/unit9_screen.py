"""Exact bounded screen: complete existing nine-unit catalogue, M35 degree7.
The source catalogue's completeness proof is an imported obligation, not reproved here.
Only consecutive layouts (17 translations), no new trace enumeration.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
P=Path(__file__).resolve().parent
R=P.parents[3]
S=R/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True
sys.path[:0]=[str(S),str(R/'computations'),str(R/'computations/propertyb33/round01')]
from unit_catalogue import fullblocks
from bare_layout import BareLayout
from multilock import Profile,json_value
from pure_quota import certificate
start=time.perf_counter()
source=json.loads((S/'UNIT_CATALOGUE_9.json').read_text())
engines=[BareLayout(25,range(a,a+9)) for a in range(1,18)]
results=[]
for idx,big in enumerate(source['orbits']):
    bs=fullblocks(big,9)
    inc=[sum(bool(t>>i&1) for t in bs) for i in range(9)]
    single=[7-j for j in inc]
    empty=35-len(bs)-sum(single)
    if min(single+[empty])<0:
        results.append(dict(base=idx,feasible=False,empty=empty,single=single))
        continue
    ns={**{t:1 for t in bs},**{1<<i:z for i,z in enumerate(single) if z},0:empty}
    best=None
    for eng in engines:
        value,abc=eng.bound(ns,True)
        prof=Profile(25,5,eng.pos,ns)
        losses={eng.pos[i]:certificate(prof,i)['loss'] for i in range(9)}
        corrected=sum((min(a,b,c-losses.get(k,Q())) for k,(a,b,c) in enumerate(abc,1)),Q())
        if best is None or corrected<best['bound']:
            best=dict(bound=corrected,bare=value,positions=eng.pos,losses=losses)
    results.append(dict(base=idx,feasible=True,large=big,counts=ns,**best))
    if idx and idx%50==0:print(idx,'elapsed',time.perf_counter()-start,flush=True)
feasible=[r for r in results if r['feasible']]
summary=dict(scope=__doc__,source=str((S/'UNIT_CATALOGUE_9.json').relative_to(R)),source_complete=source['complete'],catalogue=len(results),feasible=len(feasible),strict=sum(r['bound']<1 for r in feasible),residual=sum(r['bound']>=1 for r in feasible),maximum=max(r['bound'] for r in feasible),elapsed_seconds=time.perf_counter()-start)
(P/'UNIT9_SCREEN.json').write_text(json.dumps(json_value(dict(summary=summary,results=results)),indent=2)+'\n')
print(json.dumps(json_value(summary),indent=2))
