"""S5 trace-domain and exact scalar thresholds; no H/set-family search."""
from itertools import combinations_with_replacement,permutations
from math import comb
from pathlib import Path
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def C(n,k):return comb(n,k) if 0<=k<=n else 0
masks=[t for t in range(32) if t.bit_count() in (0,2,3,4)]
assert len(masks)==26
pairs=list(combinations_with_replacement(masks,2));assert len(pairs)==351
perms=list(permutations(range(5)))
def move(t,p):return sum(1<<p[i] for i in range(5) if t>>i&1)
def canon(ts):return min(tuple(sorted(move(t,p) for t in ts)) for p in perms)
classes={}
for ts in pairs:classes.setdefault(canon(ts),[]).append(ts)
weights=[]
for r in range(8,17):weights.append((r,C(16,r),C(12,r-4),C(12,r),C(8,r-8)))
def extra(t,v,r):
 j=t.bit_count()
 if j==0:return C(11,r-5)+C(11,r)
 if t>>v&1:return 0
 return C(11+j,r)
def risk(ts,v,c,r):
 _,D,R,B,J=next(x for x in weights if x[0]==r)
 return c*R+(32-c)*B-max(c-1,0)*J+sum(extra(t,v,r) for t in ts)
rows=[]
for ts,orbit in sorted(classes.items()):
 mins=[];details=[]
 for v in range(5):
  bad=[c for c in range(33) if all(risk(ts,v,c,r)>=D for r,D,*_ in weights)]
  assert not bad or bad==list(range(bad[0],33)),(ts,v,bad)
  k=bad[0] if bad else 33;mins.append(k)
  # At a<=k-1 one common sample is enough because each fixed-r risk has nonnegative slope here.
  best=min((risk(ts,v,k-1,r)/D,r) for r,D,*_ in weights) if k else None
  certs=[]
  for c in range(k):
   avail=[(risk(ts,v,c,r),D,r) for r,D,*_ in weights if risk(ts,v,c,r)<D]
   assert avail
   num,den,r=min(avail,key=lambda z:(z[0]/z[1],z[2]));certs.append([c,r,num,den])
  details.append({'v':v,'exception_occ':sum(t>>v&1 for t in ts),'k_non_strict':k,'strict_certificates':certs})
 rows.append({'traces':ts,'sizes':[t.bit_count() for t in ts],'intersection_size':(ts[0]&ts[1]).bit_count(),'orbit_size':len(orbit),'k':mins,'sum_k':sum(mins),'details':details})
assert sum(x['orbit_size'] for x in rows)==351
weak=[x for x in rows if x['sum_k']<=32]
print('orbits',len(rows),'weak',[(x['sizes'],x['intersection_size'],x['k'],x['sum_k']) for x in weak])
assert len(weak)==3 and all(x['sum_k']==32 for x in weak)
for row in rows:
 assert row['sum_k']>=32
 if row['sum_k']==32:
  d=[1+row['k'][v]+sum(t>>v&1 for t in row['traces']) for v in range(5)]
  row['forced_original_degrees']=d;assert max(d)==11
 else:assert row['sum_k']>32
# Stronger direct check with degree bound10: every legal singleton allocation has a repaired anchor.
# Since failure requires each a_v>=k_v, feasibility just needs all k<=caps and sum k<=32.
for row in rows:
 cap=[9-sum(t>>v&1 for t in row['traces']) for v in range(5)]
 assert sum(row['k'])>32 or any(k>u for k,u in zip(row['k'],cap))
out={'status':'PASS_EXACT_TRACE_THRESHOLD','scope':__doc__,'labeled_trace_pairs':351,'S5_orbits':len(rows),'weights_r8_to16':weights,'rows':rows,'non_strict_weak_orbits':weak,'degree10_all_covered':True,'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print('CPU',out['cpu_seconds'])
