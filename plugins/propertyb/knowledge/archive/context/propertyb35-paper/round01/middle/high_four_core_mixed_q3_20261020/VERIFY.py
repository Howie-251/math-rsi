"""Independent complete inclusive four-core domain and actual35-index replay."""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,permutations,product
from fractions import Fraction as F
import json,importlib.util,time
P=Path(__file__).resolve().parent;PM=[sum(1<<i for i in p) for p in combinations(range(4),2)];TM=[7,11,13,14]
st=time.process_time();j=json.loads((P/'RESULT.json').read_text());assert j['complete']
expected=set(combinations_with_replacement((8,9),4));assert {tuple(q['degrees']) for q in j['jobs']}==expected
summ=[]
for ds in sorted(expected):
 job=next(q for q in j['jobs'] if tuple(q['degrees'])==ds);keys=set()
 for q in (3,4):
  for cc in product(range(q,5),repeat=6):
   C=dict(zip(PM,cc))
   if any(sum(v-1 for p,v in C.items() if p>>i&1)>4*ds[i]-20 for i in range(4)):continue
   for vv in product(*(range(q,min(C[p] for p in PM if p&t==p)+1) for t in TM)):
    I=dict(zip(TM,vv));ns=[0]*16;ns[15]=q
    for t,v in I.items():ns[t]=v-q
    for p,c in C.items():ns[p]=c-sum(v for t,v in I.items() if t&p==p)+q
    for i in range(4):ns[1<<i]=ds[i]-sum(v for p,v in C.items() if p>>i&1)+sum(v for t,v in I.items() if t>>i&1)-q
    ns[0]=35-sum(ds)+sum(cc)-sum(vv)+q
    if min(ns)<0:continue
    assert sum(ns)==35;keys.add(tuple(ns))
 assert keys=={tuple(z) for z in job['label_keys']}
 # Independently move each old atom to its permuted new atom.
 mm=[]
 for p in permutations(range(4)):
  if any(ds[p[i]]!=ds[i] for i in range(4)):continue
  mm.append([sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)])
 reps=set()
 for ns in keys:
  ims=[]
  for mp in mm:
   im=[0]*16
   for m,v in enumerate(ns):im[mp[m]]=v
   ims.append(tuple(im))
  reps.add(min(ims))
 assert reps=={tuple(z) for z in job['representative_keys']}
 saved={tuple(r['counts'].get(str(m),0) for m in range(16)) for r in j['cases'] if tuple(r['degrees'])==ds}
 assert saved==reps
 summ.append({'degrees':ds,'labels':len(keys),'orbits':len(reps),'group_order':len(mm)})
q=importlib.util.spec_from_file_location('independent35',P.parents[1]/'twentyone-delta5/replay.py');m=importlib.util.module_from_spec(q);q.loader.exec_module(m)
vals=[m.verify(r) for r in j['cases']];assert len(vals)==135 and max(vals)<1
for a in summ:
 vv=[v for r,v in zip(j['cases'],vals) if tuple(r['degrees'])==tuple(a['degrees'])];a['maximum_bound']=str(max(vv))
out={'status':'PASS','scope':__doc__,'complete_degree_spectra':len(expected),'labels':sum(a['labels'] for a in summ),'orbits':len(vals),'maximum_bound':str(max(vals)),'ordered_distinct_pairs_per_case':1190,'results':summ,'cpu_seconds':time.process_time()-st}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
