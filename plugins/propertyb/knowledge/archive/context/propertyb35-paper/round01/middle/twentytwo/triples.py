"""M35 v22 unit star (7,8,8): all 15 nonnegative codegree/triple inputs."""
from pathlib import Path
import sys
HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parent))
from pilot import *
from refine_twenty_avoided import evaluate_avoided
HERE=Path(__file__).parent
start=time.time();out=[]
for c in range(1,9):
 for t in range(2):
  ns=triple(22,[7,8,8],(1,1,c),t)
  if min(ns.values())<0:continue
  opts=[]
  for k in range(7,15):
   for pos in permutations(range(k,k+3)):
    z=evaluate(22,ns,pos);opts.append(z)
  win=min(opts,key=lambda z:z['bound'])
  if not win['strict']:
   for pos in [tuple(win['positions'])]+list({p for k in range(8,14) for p in permutations(range(k,k+3))}):
    z=evaluate_avoided(22,ns,pos)
    if z['bound']<win['bound']:win=z
    if win['strict']:break
  win['codegrees']=[1,1,c];win['triple']=t
  out.append(win);print(c,t,win['bound'],win['positions'],flush=True)
(HERE/'UNIT_TRIPLES.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=time.time()-start,cases=out)),indent=2)+'\n')
print('seconds',time.time()-start)
