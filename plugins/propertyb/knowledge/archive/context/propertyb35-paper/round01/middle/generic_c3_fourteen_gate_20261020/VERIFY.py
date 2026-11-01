"""Independent degree/inclusive-first domain; original35-index zero-quota replay."""
from pathlib import Path
from itertools import product
from fractions import Fraction
from collections import Counter
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
st=time.process_time();data=json.loads((P/'DOMAIN.json').read_text());result=json.loads((P/'RESULT.json').read_text());assert result['complete'];cross=(5,6,9,10);triangles=(7,11,13,14)
keys=set()
for d in product(range(7,14),repeat=4):
 if sum(max(x-9,0) for x in d)>4:continue
 for t in (0,*triangles):
  # Inclusive cross sum is14 for no triple; a triple spends exactly two.
  ccs=[x for x in product(range(2,5),repeat=4) if sum(x)==14+2*int(bool(t))]
  for crossvalues in ccs:
   for A,B in product(range(1,5),repeat=2):
    inc={3:A,12:B,**dict(zip(cross,crossvalues))};ns=[0]*16
    if t:ns[t]=1
    for m,c in inc.items():ns[m]=c-int(bool(t) and t&m==m)
    if ns[3]<1 or ns[12]<1:continue
    for i in range(4):ns[1<<i]=d[i]-sum(c for m,c in inc.items() if m>>i&1)+int(bool(t) and t>>i&1)
    ns[0]=35-sum(d)+sum(inc.values())-int(bool(t))
    if min(ns)<0:continue
    assert sum(ns)==35 and sum(ns[m] for m in cross)==14 and ns[15]==0
    keys.add(tuple(ns))
assert keys==set(map(tuple,data['labeled_keys'])) and len(keys)==7812
# Three independent binary choices give the full order8 marked group.
perms=set()
for a,b,c in product((0,1),repeat=3):
 L=(1,0) if a else (0,1);R=(3,2) if b else (2,3);perms.add(R+L if c else L+R)
assert len(perms)==8
reps=set()
for ns in keys:
 images=[]
 for p in perms:
  out=[0]*16
  for m,v in enumerate(ns):out[sum(1<<p[i] for i in range(4) if m>>i&1)]=v
  images.append(tuple(out))
 reps.add(min(images))
assert reps==set(map(tuple,data['representative_keys']))=={tuple(c['counts']) for c in result['cases']} and len(reps)==1144
values=[]
for c in result['cases']:
 assert c['mode']=='zero';ns=c['counts'];positions=tuple(c['positions']);assert len(set(positions))==4
 stubs=[frozenset(i+1 for i in range(4) if m>>i&1) for m,v in enumerate(ns) for _ in range(v)];assert len(stubs)==35
 assert tuple(sum(i+1 in s for s in stubs) for i in range(4))==tuple(c['degrees'])
 rows=independent_rows(21,positions,stubs);v=sum((min(r['A'],r['B'],r['C']) for r in rows),Fraction());assert v==Fraction(c['bound']) and v<1;values.append(v)
out=dict(status='PASS',scope=__doc__,labels=len(keys),marked_group_order=8,orbits=len(reps),maximum_bound=str(max(values)),zero_quota=True,original_edge_indices=35,ordered_distinct_edge_pairs_per_case=1190,rows_per_case=21,by_max_selected_degree=dict(Counter(max(c['degrees']) for c in result['cases'])),cpu_seconds=time.process_time()-st)
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
