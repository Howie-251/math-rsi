"""Complete small unit-lock clique decompositions by vertex extension and exact canonicalization.

Refinement narrows bijections only by isomorphism invariants; all bijections
within the resulting cells are tested. No heuristic isomorphism decisions.
"""
from pathlib import Path
from itertools import permutations,product,combinations
from collections import defaultdict
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;ROOT=HERE.parents[3]

def canonical(blocks,n,extra=None,with_perm=False):
 big=tuple(sorted(t for t in blocks if t.bit_count()>=3));extra=extra or [0]*n
 def colors_of(sigs):
  dic={a:j for j,a in enumerate(sorted(set(sigs)))};return [dic[a] for a in sigs]
 colors=colors_of([(extra[i],)+tuple(sum(bool(t&(1<<i)) and t.bit_count()==k for t in big) for k in (3,4,5)) for i in range(n)])
 while True:
  sigs=[(colors[i],tuple(sorted((t.bit_count(),tuple(sorted(colors[j] for j in range(n) if j!=i and t&(1<<j)))) for t in big if t&(1<<i)))) for i in range(n)]
  new=colors_of(sigs)
  if len(set(new))==len(set(colors)):colors=new;break
  colors=new
 cells=[tuple(i for i in range(n) if colors[i]==c) for c in sorted(set(colors))]
 dest=[];offset=0
 for cell in cells:dest.append(tuple(range(offset,offset+len(cell))));offset+=len(cell)
 best=None;bestperm=None
 for orders in product(*(permutations(cell) for cell in cells)):
  p=[0]*n
  for order,ds in zip(orders,dest):
   for a,b in zip(order,ds):p[a]=b
  key=tuple(sorted(sum(1<<p[i] for i in range(n) if t&(1<<i)) for t in big))
  if best is None or key<best:best=key;bestperm=p
 return (best,bestperm) if with_perm else best

def fullblocks(big,n):
 used=set();out=list(big)
 for t in big:
  for i,j in combinations([i for i in range(n) if t&(1<<i)],2):
   assert (i,j) not in used;used.add((i,j))
 out.extend((1<<i)|(1<<j) for i,j in combinations(range(n),2) if (i,j) not in used)
 return tuple(sorted(out))

def extend(big,n):
 blocks=[t for t in fullblocks(big,n) if t.bit_count()<=4];b=1<<n
 def rec(start,used,picked):
  yield tuple(sorted([t for t in big if t not in picked]+[t|b for t in picked]))
  for j in range(start,len(blocks)):
   t=blocks[j]
   if not t&used:yield from rec(j+1,used|t,picked+(t,))
 yield from rec(0,0,())

def main():
 start=time.perf_counter();old=ROOT/'context/propertyb34-hour1-20261013/high-math/MIXED_SIX_v24_low6_badnone.json'
 source=json.loads(old.read_text())['results'];level={canonical(tuple(int(t) for t in x['counts'] if int(t).bit_count()>=3),6) for x in source}
 budget=float(sys.argv[1]) if len(sys.argv)>1 else 180;levels=[]
 for n in (6,7,8):
  nxt=set();raw=0;done=0
  for big in sorted(level):
   for e in extend(big,n):nxt.add(canonical(e,n+1));raw+=1
   done+=1
   if time.perf_counter()-start>budget:
    result=dict(n=n+1,complete=False,parent_orbits=len(level),parents_processed=done,raw_extensions=raw,orbits=[list(z) for z in sorted(nxt)],elapsed=time.perf_counter()-start)
    (HERE/f'UNIT_CATALOGUE_{n+1}.json').write_text(json.dumps(result,indent=2)+'\n');print('BUDGET',n+1,len(nxt),raw,done,len(level),flush=True);return
  result=dict(n=n+1,complete=True,parent_orbits=len(level),parents_processed=done,raw_extensions=raw,orbits=[list(z) for z in sorted(nxt)],elapsed=time.perf_counter()-start)
  (HERE/f'UNIT_CATALOGUE_{n+1}.json').write_text(json.dumps(result,indent=2)+'\n');print(n+1,'orbits',len(nxt),'raw',raw,'seconds',time.perf_counter()-start,flush=True)
  level=nxt

if __name__=='__main__':main()
