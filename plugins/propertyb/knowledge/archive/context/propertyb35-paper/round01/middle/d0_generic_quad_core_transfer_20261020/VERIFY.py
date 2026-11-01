"""Inclusive-moment Mobius completeness and independent35-index quota replay."""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path.insert(0,str(P.parents[1]/'twentyone-delta5'))
from replay import verify
st=time.process_time();data=json.loads((P/'RESULT.json').read_text());assert data['complete']
expected={(6,)+(7,)*r+(8,)*(3-r) for r in range(4)}
assert {tuple(j['degree']) for j in data['jobs']}==expected
pairs=[sum(1<<i for i in p) for p in combinations(range(4),2)]
triples=[sum(1<<i for i in p) for p in combinations(range(4),3)]
summary=[]
for job in data['jobs']:
 d=job['degree'];keys=set()
 for u,v,w in product(range(2,5),repeat=3):
  co={3:2,5:2,9:2,6:u,10:v,12:w}
  for nonxtriple in range(2,min(u,v,w)+1):
   ins={7:2,11:2,13:2,14:nonxtriple};ns={15:2}
   for m in triples:ns[m]=ins[m]-2
   for m in pairs:ns[m]=co[m]-sum(I for T,I in ins.items() if T&m==m)+2
   for i in range(4):ns[1<<i]=d[i]-sum(c for m,c in co.items() if m>>i&1)+sum(I for T,I in ins.items() if T>>i&1)-2
   ns[0]=35-sum(d)+sum(co.values())-sum(ins.values())+2
   if min(ns.values())<0:continue
   assert sum(ns.values())==35
   keys.add(tuple(ns.get(m,0) for m in range(16)))
 assert keys==set(map(tuple,job['complete_keys'])) and len(keys)==36
 assert keys=={tuple(z['counts'].get(str(m),0) for m in range(16)) for z in job['cases']}
 vals=[verify(z) for z in job['cases']];assert all(v<1 for v in vals)
 summary.append({'degree':d,'complete_inventory_keys':len(keys),'maximum_bound':str(max(vals))})
out={'status':'PASS','scope':__doc__,'job_set_exact':True,'profiles':144,'stubs_per_profile':35,'ordered_distinct_original_pairs_per_profile':1190,'rows_per_profile':21,'jobs':summary,'cpu_seconds':time.process_time()-st}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
