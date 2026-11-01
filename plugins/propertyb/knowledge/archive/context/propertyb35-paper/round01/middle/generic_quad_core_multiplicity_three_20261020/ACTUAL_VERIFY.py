"""Independent recursive subset partitions, exact x-star projection and original35-index zero-quota replay."""
from pathlib import Path
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
st=time.process_time();a=json.loads((P/'ACTUAL_A3_PARTITIONS.json').read_text());original=json.loads((P/'FULL_RESULT.json').read_text())['nonstrict']
def partition(mask):
 if not mask:yield ();return
 bit=mask&-mask;rest=mask^bit;sub=rest
 while True:
  for tail in partition(rest^sub):yield (bit|sub,)+tail
  if not sub:break
  sub=(sub-1)&rest
allparts=list(partition(15));assert len(allparts)==15
expected=set();by=[]
for sid,c in enumerate(original):
 old=c['counts'];count=0
 for blocks in allparts:
  if old[0]<6-len(blocks) or any(old[t]<1 for t in blocks):continue
  # Add x to its six actual edges; derive all non-x traces after this selection.
  ns=[0]*32
  for t,n in enumerate(old):
   picked=blocks.count(t) if t else 6-len(blocks)
   assert picked<=n;ns[2*t]=n-picked;ns[2*t+1]=picked
  assert sum(ns)==35 and sum(ns[m] for m in range(32) if m&1)==6
  assert all(sum(ns[m] for m in range(32) if m&(1<<i) and m&1)==1 for i in range(1,5))
  assert [sum(ns[2*t]+ns[2*t+1] for t in range(16) if t>>i&1) for i in range(4)]==[10]*4
  expected.add((sid,tuple(ns)));count+=1
 by.append(count)
saved={(c['source_id'],tuple(c['counts'])) for c in a['cases']};assert saved==expected and len(saved)==23
values=[]
for c in a['cases']:
 assert c['mode']=='zero'
 stubs=[frozenset(i+1 for i in range(5) if m>>i&1) for m,n in enumerate(c['counts']) for _ in range(n)];assert len(stubs)==35
 rows=independent_rows(21,tuple(c['positions']),stubs)
 v=sum((min(r['A'],r['B'],r['C']) for r in rows),Fraction());assert v==Fraction(c['bound']) and v<1;values.append(v)
out=dict(status='PASS',scope=__doc__,partition_universe=15,actual_cases_by_residual=by,total_actual_cases=23,maximum_bound=str(max(values)),zero_quota=True,original_edge_indices=35,ordered_distinct_edge_pairs=1190,rows=23*21,cpu_seconds=time.process_time()-st)
(P/'ACTUAL_VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
