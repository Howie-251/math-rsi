"""Bounded color-state pilot on ONE already explicit colorable pair-cover H24.
No hypergraph is generated or enumerated. Seek balanced unique minimum-degree bad edge with no repairing swap.
"""
from pathlib import Path
from itertools import combinations
import json,random,time
HERE=Path(__file__).parent;source=HERE.parent/'pairing_global/COUNTEREXAMPLE.json';r=json.loads(source.read_text());edges=r['edges'];em=[sum(1<<i for i in e) for e in edges];deg=r['degrees'];full=(1<<24)-1;rng=random.Random(20261021);st=time.time();unique=0;lowunique=0;best=100;answer=None;trials=0
for trials in range(1,100001):
 if time.time()-st>8:break
 mask=sum(1<<i for i in rng.sample(range(24),12));bad=[i for i,m in enumerate(em) if mask&m in (0,m)]
 if len(bad)!=1:continue
 unique+=1;e=edges[bad[0]]
 if any(deg[x]!=7 for x in e):continue
 lowunique+=1
 if mask&em[bad[0]]==0:mask^=full
 B=[y for y in range(24) if not mask>>y&1];counts=[];zero=False
 for x in e:
  for y in B:
   mm=mask^(1<<x)^(1<<y);f=sum(mm&m in (0,m) for m in em);counts.append(f)
   if f==0:zero=True;break
  if zero:break
 if not zero:
  answer=dict(red_mask=mask,red_vertices=[i for i in range(24) if mask>>i&1],blue_vertices=B,unique_bad_edge_id=bad[0],unique_bad_edge=e,bad_edge_degree_sum=sum(deg[x] for x in e),swap_bad_counts=counts);break
 best=min(best,sum(counts))
result=dict(scope=__doc__,source=str(source),hypergraphs_tested=1,trials=trials,unique_states=unique,minimum_degree_unique_states=lowunique,found=answer is not None,witness=answer,elapsed_seconds=time.time()-st);(HERE/'CONTROL_PILOT.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k not in ('witness','source')})
