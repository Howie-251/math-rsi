"""Probe the existing six-seven degree profiles at 22/23 vertices."""
from pathlib import Path
from fractions import Fraction
from itertools import permutations
import sys,json,time
HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'high-math'))
from position_dp import solve,json_value
from multilock import Profile,rows,total_bound
from pure_quota import certificate
source=json.loads((HERE/'high-math/V24_NO_SIX_CERTIFICATES.json').read_text())
start=time.perf_counter();out=[]
for v in (22,23):
 for x in source['results']:
  counts={int(t):n for t,n in x['counts'].items() if n}
  order=sorted(range(6),key=lambda i:x['positions'][i]);rank={j:i for i,j in enumerate(order)}
  counts={sum(1<<rank[j] for j in range(6) if t&(1<<j)):n for t,n in counts.items()}
  result=solve(v,counts,6)
  out.append(dict(v=v,group=x['group'],extra=x['extra'],**result))
  print(v,x['group'],x['extra'],result['bound'],result['positions'],flush=True)
  if time.perf_counter()-start>150:raise RuntimeError('150s profile budget')
(HERE/'MIDDLE_SIX_RESULTS.json').write_text(json.dumps(json_value(dict(scope='The complete 46 inherited local orbits, at each v22/23; optimize positions at the inherited rank order only. Selection not proved for general inputs.',elapsed_seconds=time.perf_counter()-start,results=out)),indent=2)+'\n')
