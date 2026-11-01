"""All 61 pairs for one actual positive singleton trace per remaining group type.
The trace is selected deterministically by the smallest necessary pair domain.
This is not all 32 singleton domains and does not enumerate complete H.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import sys,json,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
src=json.loads((P/'GROUP5_TWO_EXTERNAL_STARS_PILOT.json').read_text());cache={(z['id'],tuple(z['P']),tuple(z['Q'])):z for z in src['results']};st=time.perf_counter();results=[];families=[]
for f in src['domain']:
 mu={int(t):c for t,c in f['mu'].items()};d=next(d for d in f['singleton_domains'] if d['T']==f['chosen_T']);T=d['T'];rr=[]
 for pair in d['pairs']:
  p=pair['P'];r=pair['Q'];key=f['id'],tuple(p),tuple(r)
  if key in cache:z=cache[key]
  else:
   ns=Counter()
   for t,c in mu.items():
    a=int(t in p) if t else 7-len(p);b=int(t in r) if t else 7-len(r);q=int(t==T)
    vals=[c-a-b+q,a-q,b-q,q];assert min(vals)>=0
    for mask,n in zip([t,t|32,t|64,t|96],vals):ns[mask]+=n
   ns={t:c for t,c in ns.items() if c};tm=time.perf_counter();eng=SubsetEngine(25,7,ns);zz=eng.verify(eng.solve());z=dict(id=f['id'],T=T,P=p,Q=r,dp_seconds=time.perf_counter()-tm,**zz)
  results.append(z);rr.append(z)
 residual=[dict(P=z['P'],Q=z['Q'],bound=z['bound']) for z in rr if Q(z['bound'])>=1];strict=len(rr)-len(residual)
 families.append(dict(id=f['id'],T=T,domain_pairs=len(rr),strict=strict,residual=residual,all_pairs_strict=not residual,minimum=min(Q(z['bound']) for z in rr),maximum=max(Q(z['bound']) for z in rr)))
 print(f['id'],'T',T,strict,'/',len(rr),'max',max(Q(z['bound']) for z in rr),flush=True)
summary=dict(scope=__doc__,complete_for_selected_traces=True,cases=len(results),strict=sum(Q(z['bound'])<1 for z in results),residual=sum(Q(z['bound'])>=1 for z in results),eliminated_group_ids=[f['id'] for f in families if f['all_pairs_strict']],elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_TWO_EXTERNAL_STARS_COMPLETE.json').write_text(json.dumps(json_value(dict(summary=summary,families=families,results=results)),indent=2)+'\n');print(json.dumps(summary,indent=2))
