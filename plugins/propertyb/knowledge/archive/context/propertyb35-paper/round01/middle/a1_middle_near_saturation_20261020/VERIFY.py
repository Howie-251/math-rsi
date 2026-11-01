"""Degree-first independent near-saturation domain and35-original-index replay."""
from pathlib import Path
from itertools import product
import json,importlib.util,time
P=Path(__file__).resolve().parent;st=time.process_time();j=json.loads((P/'RESULT.json').read_text());assert j['complete']
CROSS=[5,9,6,10];TRI=[7,11,13,14];keys=set()
for ds in product((7,8,9),repeat=4):
 if ds.count(7)>1:continue
 for aa in product(range(5),repeat=4):
  if not 14<=sum(aa)<=16:continue
  cross=dict(zip(CROSS,aa));rem={m:4-v for m,v in cross.items()}
  # Sum cross spare capacity<=2: a quad consumes4, two triple
  # occurrences consume4. Thus no quad and at most one triple.
  for triple in (None,*TRI):
   if triple is not None and any(rem[m]<1 for m in CROSS if m&triple==m):continue
   for A,B in product(range(1,4),repeat=2):
    ns=[0]*16;ns[3]=A;ns[12]=B
    for m,n in cross.items():ns[m]=n
    if triple is not None:ns[triple]=1
    for i in range(4):ns[1<<i]=ds[i]-sum(v for m,v in enumerate(ns) if m>>i&1)
    if min(ns)<0:continue
    if any(sum(v for m,v in enumerate(ns) if m&p==p)>4 for p in (3,5,9,6,10,12)):continue
    ns[0]=35-sum(ns)
    if ns[0]<0:continue
    assert [sum(v for m,v in enumerate(ns) if m>>i&1) for i in range(4)]==list(ds)
    keys.add(tuple(ns))
assert keys=={tuple(q) for q in j['labeled_keys']} and len(keys)==167
# Rebuild the marked-pair group by independent side swaps and part swap.
perms=set()
for x,y,z in product((0,1),repeat=3):
 A=[0,1][::(-1 if x else 1)];B=[2,3][::(-1 if y else 1)];p=(B+A) if z else (A+B);perms.add(tuple(p))
assert len(perms)==8
def image(ns,p):
 im=[0]*16
 for m,v in enumerate(ns):im[sum(1<<p[i] for i in range(4) if m>>i&1)]=v
 return tuple(im)
def ds(ns):return tuple(sum(v for m,v in enumerate(ns) if m>>i&1) for i in range(4))
reps={min((ds(a),a) for a in (image(ns,p) for p in perms))[1] for ns in keys}
assert reps=={tuple(q) for q in j['representative_keys']} and len(reps)==34
assert reps=={tuple(r['counts'].get(str(m),0) for m in range(16)) for r in j['cases']}
q=importlib.util.spec_from_file_location('independent35',P.parents[1]/'twentyone-delta5/replay.py');m=importlib.util.module_from_spec(q);q.loader.exec_module(m)
vv=[m.verify(r) for r in j['cases']];assert max(vv)<1
out={'status':'PASS','scope':__doc__,'labels':len(keys),'marked_group_order':8,'orbits':len(reps),'maximum_bound':str(max(vv)),'cross_count_by_label':{str(t):sum(sum(ns[q] for q in CROSS)==t for ns in keys) for t in (14,15,16)},'profiles_expanded_to35':len(vv),'ordered_distinct_original_pairs_per_profile':1190,'cpu_seconds':time.process_time()-st}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
