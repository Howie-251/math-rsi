"""Bounded explicit-witness search for the same440 three-neighbour unit-star inputs."""
from pathlib import Path
import sys,random
HERE=Path(__file__).parent;sys.path[:0]=[str(HERE.parent),str(HERE.parent/'twentytwo')]
from pilot import *
from refine_twenty_avoided import evaluate_avoided
from multilock import pair_weight,position_context
HERE=Path(__file__).parent
start=time.time();rng=random.Random(62120261019);old=json.loads((HERE/'STAR_THREE.json').read_text())['cases'];out=[]
for idx,r in enumerate(old):
 if r['strict']:out.append(r);continue
 ns={int(t):n for t,n in r['counts'].items()};win=r|{'bound':Q(r['bound'])}
 for j in range(1500):
  pos=tuple(rng.sample(range(1,21),4));z=evaluate(20,ns,pos)
  if z['bound']<win['bound']:win=z
  if win['strict']:break
 if not win['strict']:
  z=evaluate_avoided(20,ns,tuple(win['positions']))
  if z['bound']<win['bound']:win=z
 win.update(neighbor_degrees=r['neighbor_degrees'],neighbor_codegrees=r['neighbor_codegrees'],center_partition=r['center_partition'],neighbor_triple=r['neighbor_triple'])
 out.append(win);engine.cache_clear();pair_weight.cache_clear();position_context.cache_clear()
 print(idx,r['neighbor_degrees'],r['bound'],'->',win['bound'],win['positions'],j+1,flush=True)
(HERE/'STAR_THREE_REFINED.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('strict',sum(r['strict'] for r in out),'of',len(out),'seconds',time.time()-start)
