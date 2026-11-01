"""Degree7 unit-star bounded exact diagnosis; no whole-hypergraph enumeration."""
from pathlib import Path
from itertools import combinations,product
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[3]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'context/propertyb35-paper/round01/middle/twentytwo'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
def parts(n):
 def rec(i,blocks):
  if i==n:
   yield tuple(tuple(b) for b in blocks);return
  for b in range(len(blocks)):
   blocks[b].append(i);yield from rec(i+1,blocks);blocks[b].pop()
  yield from rec(i+1,blocks+[[i]])
 yield from rec(0,[])
def recover(center,ds,ps,partition,high):
 s=len(ds);ns={1: center-len(partition)}
 for B in partition:ns[1+sum(1<<(i+1) for i in B)]=1
 inc={1<<i:ds[i] for i in range(s)}
 inc.update({(1<<i)|(1<<j):c for (i,j),c in zip(combinations(range(s),2),ps)});inc.update(high)
 exact={}
 for t in sorted(range(1,1<<s),key=int.bit_count,reverse=True):
  exact[t]=inc[t]-sum(all(t>>i&1==0 or i in B for i in range(s)) for B in partition)-sum(n for u,n in exact.items() if u&t==t)
  if exact[t]<0:return None
 for t,n in exact.items():ns[t<<1]=n
 ns[0]=35-sum(ns.values())
 return ns if min(ns.values())>=0 else None
from multilock import json_value
if __name__=='__main__':
 start=time.time();out=[]
 for a,b in ((8,8),(8,9),(9,9),(8,10),(9,10),(10,10)):
  for c in range(1,min(a,b)+1):
   for part in parts(2):
    ns=recover(7,(a,b),(c,),part,{})
    if ns is None:continue
    eng=SubsetEngine(20,3,ns);z=eng.verify(eng.solve());z.update(degrees=[7,a,b],neighbor_codegree=c,partition=part,strict=z['bound']<1);out.append(z)
  print(a,b,'cases',len([r for r in out if r['degrees'][1:]==[a,b]]),'residual',[(r['neighbor_codegree'],r['partition'],str(r['bound'])) for r in out if r['degrees'][1:]==[a,b] and not r['strict']],flush=True)
 (HERE/'UNIT_TWO.json').write_text(json.dumps(json_value(dict(cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 print('seconds',time.time()-start)
