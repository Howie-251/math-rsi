from pathlib import Path
from math import comb
import json,time
P=Path(__file__).resolve().parent;start=time.process_time();d=json.loads((P/'RESULT.json').read_text())
allowed={13:[1,2,3,4],14:[1,2,3,4],15:[2,3,4],16:[2,3,4],17:[3],18:[3]}
mins={};maxs={}
for D,cs in allowed.items():
 lo={0:0};hi={0:0}
 for _ in range(18):
  a={};b={}
  for s,v in lo.items():
   for c in cs:a[s+c]=min(a.get(s+c,10**9),v+comb(c-1,2))
  for s,v in hi.items():
   for c in cs:b[s+c]=max(b.get(s+c,-1),v+comb(c-1,2))
  lo,hi=a,b
 mins[D],maxs[D]=lo,hi
rows=[]
for row in d['rows']:
 ds=row['high_degrees'];out=[]
 for z in row['domain']:
  base=sum(comb(c-1,2) for c in z['pair_codegrees']);L=z['low_high_codegree_sums']
  lower=base+sum(mins[D][s] for D,s in zip(ds,L));upper=base+sum(maxs[D][s] for D,s in zip(ds,L))
  out.append({'pair_codegrees':z['pair_codegrees'],'triple':z['triple'],'tau_lower':lower,'tau_upper':upper})
 rows.append({'high_degrees':ds,'minimum_tau':min(z['tau_lower'] for z in out),'maximum_tau':max(z['tau_upper'] for z in out),'minimum_witness':min(out,key=lambda z:z['tau_lower']),'all_bounds':out})
r={'status':'COMPLETE_ACTUAL_SHARED_SEVEN_HIGH_TAU_CAPACITIES','scope':'a7=18: seven/seven lambda<=2 contributes tau0; all tau is seven/high plus three high pairs. Exact18-point marginal DP over old allowed lambda sets; minima/maxima independently relax shared low point identities, hence safe bounds, not H feasibility.','rows':rows,'cpu_seconds':time.process_time()-start}
(P/'TAU_POOL_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print('CPU',r['cpu_seconds'])
for z in rows:print({k:v for k,v in z.items() if k!='all_bounds'})
