"""M35 v20 four degree7 vertices with all six codegrees exactly2.
Inclusive high intersection domain and exact recovered inventories.
"""
from pathlib import Path
import sys
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE.parent))
from pilot import *
from refine_twenty_avoided import evaluate_avoided
HERE=Path(__file__).parent
start=time.time();out=[]
for ts in product(range(3),repeat=4):
 for q in range(min(ts)+1):
  I={1<<i:7 for i in range(4)};I.update({sum(1<<i for i in S):2 for S in combinations(range(4),2)});I.update(dict(zip((7,11,13,14),ts)));I[15]=q
  ns={}
  for t in sorted(I,key=int.bit_count,reverse=True):ns[t]=I[t]-sum(n for u,n in ns.items() if u&t==t)
  ns[0]=35-sum(ns.values())
  if min(ns.values())<0:continue
  win=None
  for k in (9,8,10,7,11):
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
  win.update(triples=ts,four=q);out.append(win);print(ts,q,win['bound'],flush=True)
(HERE/'FOUR_SEVENS.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('done',len(out),'strict',sum(r['strict'] for r in out),'max',max(r['bound'] for r in out),'seconds',time.time()-start)
