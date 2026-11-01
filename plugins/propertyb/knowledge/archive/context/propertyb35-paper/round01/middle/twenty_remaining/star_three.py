"""M35 v20 minimum degree6: three actual unit neighbours degree8/9.
Complete shared center-partition and inclusive triple domain, filtered only by
already strict projected (6,a,b) unit-star triples.
"""
from pathlib import Path
import sys
HERE=Path(__file__).parent;sys.path[:0]=[str(HERE.parent),str(HERE.parent/'twentytwo')]
from star_pilot import parts,recover
from pilot import *
from refine_twenty_avoided import evaluate_avoided
HERE=Path(__file__).parent
start=time.time();source=json.loads((HERE/'UNIT_PAIRS.json').read_text())['cases']
lookup={(tuple(r['degrees'][1:]),r['codegrees'][2],r['triple']):r['strict'] for r in source}
out=[];domain=[]
for ds in ((8,8,8),(8,8,9),(8,9,9),(9,9,9)):
 for ps in product(range(1,4),repeat=3):
  for part in parts(3):
   bad=False
   for (i,j),c in zip(combinations(range(3),2),ps):
    t=int(any(i in B and j in B for B in part))
    if lookup[(tuple((ds[i],ds[j])),c,t)]:bad=True;break
   if bad:continue
   for t in range(min(ps)+1):
    ns=recover(6,ds,ps,part,{7:t})
    if ns is None:continue
    r=dict(neighbor_degrees=ds,neighbor_codegrees=ps,center_partition=part,neighbor_triple=t,counts=ns);domain.append(r)
print('domain',len(domain),flush=True)
(HERE/'STAR_THREE_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=domain)),indent=2)+'\n')
for idx,r in enumerate(domain):
 ns=r['counts'];win=None
 for k in (8,9,7,10,6,11):
  for pos in permutations(range(k,k+4)):
   z=evaluate(20,ns,pos)
   if win is None or z['bound']<win['bound']:win=z
   if win['strict']:break
  if win['strict']:break
 if not win['strict']:
  for pos in [tuple(win['positions'])]+list({p for k in (8,9,10) for p in permutations(range(k,k+4))}):
   z=evaluate_avoided(20,ns,pos)
   if z['bound']<win['bound']:win=z
   if win['strict']:break
 win.update(r);out.append(win)
 print(idx,r['neighbor_degrees'],r['neighbor_codegrees'],r['center_partition'],r['neighbor_triple'],win['bound'],flush=True)
 if time.time()-start>175:break
(HERE/'STAR_THREE.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(domain),domain_size=len(domain),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('done',len(out),'strict',sum(r['strict'] for r in out),'domain',len(domain),'seconds',time.time()-start)
