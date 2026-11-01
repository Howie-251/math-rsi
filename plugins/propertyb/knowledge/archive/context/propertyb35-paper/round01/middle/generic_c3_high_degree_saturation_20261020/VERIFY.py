"""Independent degree-first complete domain and35-index zero-deduction injection replay."""
from pathlib import Path
from itertools import product
from fractions import Fraction
from collections import Counter
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
st=time.process_time();data=json.loads((P/'RESULT.json').read_text());assert data['complete_probability'];cross=(5,6,9,10);keys=set()
for degree in product(range(8,14),repeat=4):
 if sum(max(d-9,0) for d in degree)>4:continue
 for deficit in (None,*cross):
  for sides in product(range(1,5),repeat=2):
   ns=[0]*16;ns[3],ns[12]=sides
   for m in cross:ns[m]=4-int(m==deficit)
   for i in range(4):ns[1<<i]=degree[i]-sum(v for m,v in enumerate(ns) if m>>i&1)
   if min(ns)<0:continue
   ns[0]=35-sum(ns)
   if ns[0]<0:continue
   keys.add(tuple(ns))
assert keys==set(map(tuple,data['labeled_keys'])) and len(keys)==1303
# Build the group from side flips and optional interchange, not permutations filter.
perms=set()
for a,b,c in product((0,1),repeat=3):
 L=(1,0) if a else (0,1);R=(3,2) if b else (2,3)
 perms.add(R+L if c else L+R)
assert len(perms)==8
def im(ns,p):
 out=[0]*16
 for m,v in enumerate(ns):out[sum(1<<p[i] for i in range(4) if m>>i&1)]=v
 return tuple(out)
reps={min(im(ns,p) for p in perms) for ns in keys}
assert reps==set(map(tuple,data['representative_keys']))
assert reps=={tuple(c['counts']) for c in data['cases']} and len(reps)==183
vals=[]
for c in data['cases']:
 ns=tuple(c['counts']);position=tuple(c['positions']);assert len(set(position))==4
 stubs=[frozenset(i+1 for i in range(4) if m&(1<<i)) for m,v in enumerate(ns) for _ in range(v)]
 assert len(stubs)==35
 degree=tuple(sum(i+1 in t for t in stubs) for i in range(4));assert degree==tuple(c['degrees'])
 rows=independent_rows(21,position,stubs)
 val=sum((min(r['A'],r['B'],r['C']) for r in rows),Fraction())
 assert val==Fraction(c['bound']) and val<1
 vals.append(val)
out={'status':'PASS','scope':__doc__,'labeled_keys':len(keys),'marked_pair_group_order':len(perms),'representatives':len(reps),'cross_total_counts':dict(Counter(sum(ns[m] for m in cross) for ns in keys)),'maximum_bound':str(max(vals)),'zero_deductions':True,'original_edge_indices_per_case':35,'ordered_distinct_original_pairs_per_case':1190,'rows_per_case':21,'cpu_seconds':time.process_time()-st}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
