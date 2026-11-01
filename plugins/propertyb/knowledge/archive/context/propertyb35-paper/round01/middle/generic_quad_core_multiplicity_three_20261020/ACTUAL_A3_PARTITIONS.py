"""Same real degree-six unit star joins the four10 residual views; no free promotion."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(P.parent)]
from subset_position_dp import SubsetEngine
from pilot import json_value
st=time.process_time();data=json.loads((P/'FULL_RESULT.json').read_text());res=data['nonstrict'];assert len(res)==4 and all(c['degrees']==[10]*4 for c in res)
# Restricted growth words generate set partitions once.
def rec(word):
 if len(word)==4:
  yield tuple(sum(1<<i for i,a in enumerate(word) if a==b) for b in range(max(word)+1));return
 for b in range(max(word)+2):yield from rec(word+[b])
parts=sorted(rec([0]));assert len(parts)==15
cases=[];jobs=[]
for sid,c in enumerate(res):
 old=c['counts'];keys=set()
 for blocks in parts:
  if any(old[t]<1 for t in blocks) or old[0]<6-len(blocks):continue
  ns={m<<1:v for m,v in enumerate(old) if v}
  for t in blocks:ns[t<<1]-=1;ns[(t<<1)|1]=1
  ns[1]=6-len(blocks);ns[0]=old[0]-ns[1];ns={m:v for m,v in ns.items() if v}
  assert sum(ns.values())==35
  assert [sum(v for m,v in ns.items() if m>>i&1) for i in range(5)]==[6,10,10,10,10]
  key=tuple(ns.get(m,0) for m in range(32));keys.add(key)
  e=SubsetEngine(21,5,ns);orig=e.inv.copy();e.inv={p:(0,0,[]) for p in orig};z=e.solve();mode='zero'
  if z['bound']>=1:e.inv=orig;z=e.solve();mode='nested_total_pure'
  cases.append(dict(source_id=sid,blocks=blocks,counts=key,positions=z['positions'],mode=mode,bound=z['bound'],strict=z['bound']<1))
 jobs.append(dict(source_id=sid,old_counts=old,actual_partition_count=len(keys)))
out=dict(scope=__doc__,partition_universe=15,jobs=jobs,cases=cases,case_count=len(cases),nonstrict=[c for c in cases if not c['strict']],maximum_bound=max(c['bound'] for c in cases),cpu_seconds=time.process_time()-st)
(P/'ACTUAL_A3_PARTITIONS.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print(json_value({k:v for k,v in out.items() if k not in ('cases','nonstrict')}));print('NONSTRICT',len(out['nonstrict']))
