"""M35 v20 degree6 center unit to two neighbours of degree8/9."""
from pathlib import Path
import sys
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE.parent))
from pilot import *
from refine_twenty_avoided import evaluate_avoided
HERE=Path(__file__).parent
start=time.time();out=[]
for a,b in ((8,8),(8,9),(9,9)):
 for c in range(1,a+1):
  for t in range(2):
   ns=triple(20,[6,a,b],(1,1,c),t)
   if min(ns.values())<0:continue
   win=None
   for k in range(6,14):
    for pos in permutations(range(k,k+3)):
     z=evaluate(20,ns,pos)
     if win is None or z['bound']<win['bound']:win=z
   if not win['strict']:
    for pos in [tuple(win['positions'])]+list({p for k in range(7,13) for p in permutations(range(k,k+3))}):
     z=evaluate_avoided(20,ns,pos)
     if z['bound']<win['bound']:win=z
     if win['strict']:break
   win.update(degrees=[6,a,b],codegrees=[1,1,c],triple=t);out.append(win)
   print(a,b,c,t,win['bound'],win['positions'],flush=True)
(HERE/'UNIT_PAIRS.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('seconds',time.time()-start)
