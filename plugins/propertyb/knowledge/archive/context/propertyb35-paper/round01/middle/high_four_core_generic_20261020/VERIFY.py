"""Independent inclusive-moment / occurrence-partition domains and35-stub replay."""
from pathlib import Path
from itertools import combinations,permutations,product
from fractions import Fraction as F
import importlib.util,json,time
P=Path(__file__).resolve().parent
PM=[sum(1<<i for i in p) for p in combinations(range(4),2)];TM=[7,11,13,14]
images=[]
for p in permutations(range(4)):
 images.append([sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)])
def image(h,mp):
 z=[0]*16
 for m,v in enumerate(h):z[mp[m]]=v
 return tuple(z)
def canon(h):return min(image(h,mp) for mp in images)
st=time.process_time();keys=set()
for q in range(2,5):
 for cc in product(range(q,5),repeat=6):
  C=dict(zip(PM,cc))
  if any(sum(v-1 for m,v in C.items() if m>>i&1)>12 for i in range(4)):continue
  ranges=[range(q,min(C[m] for m in PM if m&t==m)+1) for t in TM]
  for vals in product(*ranges):
   I=dict(zip(TM,vals));ns=[0]*16;ns[15]=q
   for t,v in I.items():ns[t]=v-q
   for p,c in C.items():ns[p]=c-sum(v for t,v in I.items() if t&p==p)+q
   for i in range(4):ns[1<<i]=8-sum(v for p,v in C.items() if p>>i&1)+sum(v for t,v in I.items() if t>>i&1)-q
   ns[0]=3+sum(cc)-sum(vals)+q
   if min(ns)<0:continue
   assert sum(ns)==35;keys.add(tuple(ns))
profile=json.loads((P/'PROFILE.json').read_text());reps={tuple(z) for z in profile['representatives']}
assert len(keys)==2119 and {canon(k) for k in keys}==reps and len(reps)==174
four=json.loads((P/'FOUR_LOCK.json').read_text());assert four['complete']
assert {tuple(r['counts'].get(str(m),0) for m in range(16)) for r in four['cases']}==reps
ext=json.loads((P/'EXTENDED.json').read_text())
def partitions(xs):
 if not xs:yield [];return
 x=xs[0]
 for pp in partitions(xs[1:]):
  yield [[x]]+pp
  for j in range(len(pp)):
   if x not in pp[j] and len(pp[j])<4:yield pp[:j]+[[x]+pp[j]]+pp[j+1:]
for dom in ext['domain']:
 r=next(q for q in four['cases'] if q['id']==dom['source_id']);ns=[r['counts'].get(str(m),0) for m in range(16)];hs=set()
 for role in range(16):
  occ=list(range(4))+[i for i in range(4) if role>>i&1]
  for blocks in partitions(occ):
   if len(blocks)>6:continue
   h=[0]*16;h[0]=6-len(blocks)
   for b in blocks:h[sum(1<<v for v in b)]+=1
   if h[15]>1 or any(h[m]>ns[m] for m in range(16)):continue
   hs.add(tuple(h))
 assert hs=={tuple(q) for q in dom['labeled_h_keys']}
 group=[mp for mp in images if image(ns,mp)==tuple(ns)]
 hr={min(image(h,mp) for mp in group) for h in hs}
 assert hr=={tuple(q) for q in dom['representative_h_keys']}
 actual={tuple(q['center_counts']) for q in ext['cases'] if q['source_id']==dom['source_id']}
 assert actual==hr
# Different actual ordered-index implementation, no discovery/DP imports.
q=importlib.util.spec_from_file_location('expanded35',P.parents[1]/'twentyone-delta5/replay.py');m=importlib.util.module_from_spec(q);q.loader.exec_module(m)
values=[m.verify(r) for r in four['cases']];vext=[m.verify(r) for r in ext['cases']]
assert sum(v<1 for v in values)==172 and len(vext)==36 and max(vext)<1
out={'status':'PASS','scope':__doc__,'four_labels':len(keys),'four_orbits':len(reps),'four_strict':172,'four_strict_max':str(max(v for v in values if v<1)),'four_residual_values':[str(v) for v in values if v>=1],'center_label_counts':[len(d['labeled_h_keys']) for d in ext['domain']],'center_orbit_counts':[len(d['representative_h_keys']) for d in ext['domain']],'five_max':str(max(vext)),'expanded35_profiles':210,'ordered_distinct_pairs_per_profile':1190,'cpu_seconds':time.process_time()-st}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
