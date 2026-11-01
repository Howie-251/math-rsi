from pathlib import Path
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path[:0]=[str(P.parent),str(ROOT/'context/propertyb34/round01/high-math')]
from subset_position_dp import SubsetEngine
from pilot import json_value
st=time.process_time();j=json.loads((P/'PROFILE.json').read_text());out=[]
for q,ns0 in enumerate(j['representatives']):
 ns={m:n for m,n in enumerate(ns0) if n}
 e=SubsetEngine(21,4,ns);z=e.verify(e.solve())
 out.append(dict(id=q,counts=ns,positions=z['positions'],bound=z['bound'],strict=z['bound']<1))
 if time.process_time()-st>7.0:break
result={'complete':len(out)==len(j['representatives']),'tested_orbits':len(out),'total_orbits':len(j['representatives']),'strict':sum(q['strict'] for q in out),'cpu_seconds':time.process_time()-st,'cases':out}
(P/'FOUR_LOCK.json').write_text(json.dumps(json_value(result),indent=2)+'\n');print({k:v for k,v in result.items() if k!='cases'})
