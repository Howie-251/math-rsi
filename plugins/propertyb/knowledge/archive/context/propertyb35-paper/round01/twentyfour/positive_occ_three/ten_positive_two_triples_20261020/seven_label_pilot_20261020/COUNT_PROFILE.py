"""Exact labelled graph count by symmetric residual-capacity polynomial DP; no graph list, no LP."""
from functools import cache
from collections import Counter
from itertools import product
from pathlib import Path
import json,time
START=time.process_time();transitions=0
@cache
def counts(cap):
 global transitions
 if len(cap)<=1:return (1,)
 first=cap[0];remaining=cap[1:];out=Counter()
 def star(k,left,vec):
  global transitions
  if k==len(remaining):
   transitions+=1
   degree=sum(vec);residual=tuple(sorted((r-m for r,m in zip(remaining,vec)),reverse=True))
   for e,n in enumerate(counts(residual)):out[e+degree]+=n
   return
  for m in range(min(left,remaining[k])+1):star(k+1,left-m,vec+[m])
 star(0,first,[])
 return tuple(out[e] for e in range(max(out)+1))
assert counts((4,)*4)[3]==56
assert counts((4,)*5)[3]==220
result=counts((4,)*7)
selected={e:result[e] for e in range(11,15)}
out=dict(PASS=True,scope=__doc__,labelled_counts_by_E=selected,total_labelled=sum(selected.values()),
         all_cap4_seven_label_counts=list(result),memo_states=counts.cache_info().currsize,
         star_transitions=transitions,cpu_seconds=time.process_time()-START,
         graph_key_list_generated=False,orbit_count_computed=False)
(Path(__file__).resolve().parent/'COUNT_PROFILE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
