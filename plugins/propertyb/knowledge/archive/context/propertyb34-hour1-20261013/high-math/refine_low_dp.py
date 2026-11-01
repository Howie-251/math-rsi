from pathlib import Path
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
from position_dp import solve
from multilock import json_value
start=time.perf_counter();out=[]
for src in sorted(Path(__file__).parent.glob('MIXED_SIX_v24_low*.json')):
 d=json.loads(src.read_text())
 if d['degrees'].count(6)>2:continue
 for x in d['results']:
  if Fraction(x['bound'])<1:continue
  order=sorted(range(6),key=lambda i:x['positions'][i]);perm=tuple(order.index(i) for i in range(6))
  counts={sum(1<<perm[i] for i in range(6) if int(t)&(1<<i)):n for t,n in x['counts'].items()}
  z=solve(24,counts,6);out.append(dict(source=src.name,group=x['group'],relabeling=perm,old_bound=x['bound'],**z));print(src.name,x['group'],x['bound'],'->',z['bound'],z['positions'],flush=True)
Path(__file__).with_name('LOW_POSITION_DP.json').write_text(json.dumps(json_value(dict(elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
