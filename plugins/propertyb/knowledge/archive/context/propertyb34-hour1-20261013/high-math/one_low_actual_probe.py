from pathlib import Path
from itertools import permutations
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
from position_dp_actual import solve
from multilock import json_value
from mixed_six import trans
start=time.perf_counter();out=[]
src=json.loads(Path(__file__).with_name('MIXED_SIX_v24_low1_badnone.json').read_text());x=next(x for x in src['results'] if Fraction(x['bound'])>=1);ns={int(t):n for t,n in x['counts'].items()}
for slot in ((1,3),(3,5)):
 seen=set();best=None
 for perm in permutations(range(6)):
  counts={trans(t,perm):n for t,n in ns.items()};st=tuple(sorted(trans(t,perm) for t in slot));key=tuple(sorted(counts.items())),st
  if key in seen:continue
  seen.add(key);z=solve(24,counts,6,{perm[0]:st})
  if best is None or z['bound']<best['bound']:best=dict(relabeling=perm,**z)
  if z['bound']<1:break
 out.append(dict(original_slot=slot,orders_tried=len(seen),**best));print(slot,best['bound'],best['positions'],len(seen),flush=True)
Path(__file__).with_name('ONE_LOW_UNIT_ACTUAL.json').write_text(json.dumps(json_value(dict(scope='Two symmetry classes of actual unique bad slot, all-pair unit six-lock profile with one low and five high.',elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
