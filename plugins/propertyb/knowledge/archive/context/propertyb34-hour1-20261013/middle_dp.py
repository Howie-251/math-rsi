"""Reuse six-lock position DP to refine retained middle-vertex profile witnesses."""
from pathlib import Path
from fractions import Fraction
import sys,json,time
HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'high-math'))
from position_dp import solve,json_value
start=time.perf_counter();out=[]
for source,field,s in [('MIDDLE_TRIPLE_RESULTS.json','cases',3),('MIDDLE_FOUR_RESULTS.json','profiles',4)]:
 data=json.loads((HERE/source).read_text())
 for i,x in enumerate(data[field]):
  if Fraction(x['bound'])<1:continue
  counts={int(k):v for k,v in x['counts'].items() if v}
  # This rank order uses the old retained assignment to avoid needlessly
  # losing a label order already known to be useful.
  order=sorted(range(s),key=lambda j:x['positions'][j]);rank={j:i for i,j in enumerate(order)}
  c={sum(1<<rank[j] for j in range(s) if t&(1<<j)):n for t,n in counts.items()}
  r=solve(x.get('v',22),c,s)
  out.append(dict(source=source,index=i,old_bound=x['bound'],**r))
  print(source,i,x.get('pairs',x.get('sizes')),x.get('triple',x.get('group')),x['bound'],'->',r['bound'],r['positions'],flush=True)
  if time.perf_counter()-start>150:raise RuntimeError('150s diagnostic budget')
(HERE/'MIDDLE_DP_RESULTS.json').write_text(json.dumps(json_value(dict(scope='Global increasing placements for each retained label rank only; no full relabeling claim.',elapsed_seconds=time.perf_counter()-start,results=out)),indent=2)+'\n')
