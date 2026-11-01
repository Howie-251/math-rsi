"""All 245 admissible external-star extensions over the 18 no-full-G survivors.
Cached pilot cases are retained; all remaining six-lock inventories use the
established exact subset DP with its independent ABC replay.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3]
sys.dont_write_bytecode=True;sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
src=json.loads((P/'GROUP5_EXTERNAL_STAR_PILOT.json').read_text());cache={(z['id'],tuple(z['partition'])):z for z in src['results']};st=time.perf_counter();results=[];families=[]
for f in src['domain']:
 mu={int(t):c for t,c in f['mu'].items()};rr=[]
 for part in f['partitions']:
  if (f['id'],tuple(part)) in cache:z=cache[f['id'],tuple(part)]
  else:
   ns=Counter(mu)
   for t in part:ns[t]-=1;ns[t|32]+=1
   ns[0]-=7-len(part);ns[32]+=7-len(part);ns={t:c for t,c in ns.items() if c};assert min(ns.values())>=0
   eng=SubsetEngine(25,6,ns);tm=time.perf_counter();zz=eng.verify(eng.solve());z=dict(id=f['id'],partition=part,partition_size=len(part),dp_seconds=time.perf_counter()-tm,x_singleton_count=ns.get(32,0),x_certificate=zz['certificates'][5],**zz)
  results.append(z);rr.append(z)
 strict=sum(Q(z['bound'])<1 for z in rr);residual=[z['partition'] for z in rr if Q(z['bound'])>=1]
 families.append(dict(id=f['id'],partitions=len(rr),strict=strict,residual_partitions=residual,all_partitions_strict=not residual,minimum=min(Q(z['bound']) for z in rr),maximum=max(Q(z['bound']) for z in rr)))
 print(f['id'],'strict',strict,'/',len(rr),'max',max(Q(z['bound']) for z in rr),flush=True)
summary=dict(scope=__doc__,complete=True,cases=len(results),strict=sum(Q(z['bound'])<1 for z in results),residual=sum(Q(z['bound'])>=1 for z in results),all_strict_family_ids=[f['id'] for f in families if f['all_partitions_strict']],elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_EXTERNAL_STAR_COMPLETE.json').write_text(json.dumps(json_value(dict(summary=summary,families=families,results=results)),indent=2)+'\n');print(json.dumps(summary,indent=2))
