from star_pilot import *
import random
HERE=Path(__file__).parent
start=time.time();rng=random.Random(20261019);old=json.loads((HERE/'STAR_THREE.json').read_text());out=[]
for idx,r in enumerate(old['cases']):
 ns={int(t):n for t,n in r['counts'].items()};win=r|{'bound':Q(r['bound'])}
 if not r['strict']:
  poses=[tuple(r['positions'])]+[tuple(rng.sample(range(1,23),4)) for _ in range(1500)]
  for j,pos in enumerate(poses):
   z=evaluate(22,ns,pos)
   if z['bound']<win['bound']:win=z
   if win['strict']:break
  if not win['strict']:
   z=evaluate_avoided(22,ns,tuple(win['positions']))
   if z['bound']<win['bound']:win=z
  engine.cache_clear()
  from multilock import pair_weight,position_context
  pair_weight.cache_clear();position_context.cache_clear()
  print(idx,r['neighbor_codegrees'],r['center_partition'],r['neighbor_triple'],r['bound'],'->',win['bound'],win['positions'],j+1,flush=True)
 win.update(neighbor_codegrees=r['neighbor_codegrees'],center_partition=r['center_partition'],neighbor_triple=r['neighbor_triple'])
 out.append(win)
(HERE/'STAR_THREE_REFINED.json').write_text(json.dumps(json_value(dict(scope='Bounded noncontiguous layout search for same 13 complete unit-star inputs; random search only discovers explicit rational witnesses',cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('strict',sum(r['strict'] for r in out),'of',len(out),'seconds',time.time()-start)
