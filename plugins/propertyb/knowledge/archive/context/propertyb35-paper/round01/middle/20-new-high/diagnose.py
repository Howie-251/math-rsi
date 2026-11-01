"""M35 v20 delta7/8 first small exact pair/triple and actual selection diagnosis.
Only bounded local inventories and explicit position witnesses, no full H enumeration.
"""
from pathlib import Path
from itertools import product,permutations
import sys,time,json
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE.parent))
from pilot import *
from refine_twenty_avoided import evaluate_avoided
HERE=Path(__file__).parent
start=time.time();pairs=[];triples=[]
for a,b in ((7,7),(7,8),(8,8),(7,9),(8,9),(9,9),(7,10),(8,10),(9,10),(10,10)):
 for c in range(1,min(a,b)+1):
  ns=double(20,a,b,c)
  z=best(20,ns,True);z.update(degrees=[a,b],codegree=c);pairs.append(z)
  print('pair',a,b,c,z['bound'],flush=True)
for d in (7,8):
 for ps in product(range(1,4 if d==7 else 5),repeat=3):
  if sorted(ps)!=list(ps):continue
  for t in range(min(ps)+1):
   ns=triple(20,[d]*3,ps,t)
   if min(ns.values())<0:continue
   win=None
   for k in range(6,14):
    for pos in permutations(range(k,k+3)):
     z=evaluate(20,ns,pos)
     if win is None or z['bound']<win['bound']:win=z
   if not win['strict']:
    z=evaluate_avoided(20,ns,tuple(win['positions']))
    if z['bound']<win['bound']:win=z
   win.update(degrees=[d]*3,codegrees=ps,triple=t);triples.append(win)
   print('triple',d,ps,t,win['bound'],flush=True)
output=dict(scope=__doc__,pairs=pairs,triples=triples,elapsed_seconds=time.time()-start)
(HERE/'DIAGNOSIS.json').write_text(json.dumps(json_value(output),indent=2)+'\n')
print('seconds',time.time()-start)
