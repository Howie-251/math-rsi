"""Three actual unit-neighbours of degree7 center at v22 M35.
Chosen minimum-weight triple among >=14 degree8 unit neighbours has W<=1.
"""
from pathlib import Path
from itertools import product,combinations,permutations
import sys
HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parent))
from pilot import *
from refine_twenty_avoided import evaluate_avoided
HERE=Path(__file__).parent

def parts(n):
 def rec(i,blocks):
  if i==n:
   yield tuple(tuple(b) for b in blocks);return
  for b in range(len(blocks)):
   blocks[b].append(i);yield from rec(i+1,blocks);blocks[b].pop()
  yield from rec(i+1,blocks+[[i]])
 yield from rec(0,[])
def recover(center,ds,ps,partition,high):
 s=len(ds);size=1<<(s+1);ns={}
 for B in partition:ns[1+sum(1<<(i+1) for i in B)]=1
 ns[1]=center-len(partition)
 inc={1<<i:ds[i] for i in range(s)}
 inc.update({(1<<i)|(1<<j):c for (i,j),c in zip(combinations(range(s),2),ps)})
 inc.update(high)
 exact={}
 for t in sorted(range(1,1<<s),key=int.bit_count,reverse=True):
  rhs=inc[t]-sum(1 for B in partition if all(i in B for i in range(s) if t>>i&1))
  exact[t]=rhs-sum(n for u,n in exact.items() if u&t==t)
  if exact[t]<0:return None
 for t,n in exact.items():ns[t<<1]=n
 ns[0]=35-sum(ns.values())
 return ns if min(ns.values())>=0 else None

def main():
 start=time.time();out=[]
 for ps in [(1,1,1),(1,1,2)]:
  for part in parts(3):
   for t in range(min(ps)+1):
    ns=recover(7,[8]*3,ps,part,{7:t})
    if ns is None:continue
    win=None
    for k in range(7,15):
     for pos in permutations(range(k,k+4)):
      z=evaluate(22,ns,pos)
      if win is None or z['bound']<win['bound']:win=z
      if win['strict']:break
     if win['strict']:break
    if not win['strict']:
     for pos in [tuple(win['positions'])]+list({p for k in range(8,14) for p in permutations(range(k,k+4))}):
      z=evaluate_avoided(22,ns,pos)
      if z['bound']<win['bound']:win=z
      if win['strict']:break
    win.update(neighbor_codegrees=ps,center_partition=part,neighbor_triple=t)
    out.append(win);print(ps,part,t,win['bound'],win['positions'],flush=True)
 (HERE/'STAR_THREE.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 print('profiles',len(out),'strict',sum(r['strict'] for r in out),'seconds',time.time()-start)
if __name__=='__main__':main()
