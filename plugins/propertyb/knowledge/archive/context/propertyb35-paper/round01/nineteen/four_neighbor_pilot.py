"""Complete residual four-unit-neighbour trace domain after prior local strict rules."""
from pathlib import Path
import sys,json,itertools,time
ROOT=Path(__file__).resolve().parents[4];sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(Path(__file__).parent)]
from pilot import evaluate,json_value
HERE=Path(__file__).parent

def partitions(xs):
 if not xs:yield [];return
 a,*rest=xs
 for p in partitions(rest):
  yield [(a,)]+p
  for i in range(len(p)):yield p[:i]+[tuple(sorted((a,)+p[i]))]+p[i+1:]

def canonical(p):return tuple(sorted(tuple(sorted(b)) for b in p))
def main():
 start=time.time();prior=json.loads((HERE/'UNIT_STAR_PILOT.json').read_text())['profiles']
 fails={(tuple(z['degrees'][1:]),canonical(z['partition']),z['t']) for z in prior if not z['strict']}
 fails.discard(((8,8,8),canonical([(0,),(1,),(2,)]),1)) # strict neighbour 222,t1 triple
 poss=set()
 for k in range(1,16):
  for xp in range(5):
   others=list(range(k,k+5));x=others.pop(xp)
   for q in itertools.permutations(others):poss.add((x,)+q)
 for q in [(1,2,7,12,13),(1,5,8,11,15),(1,6,10,14,19)]:poss.update(itertools.permutations(q))
 poss=sorted(poss);out=[]
 triples=list(itertools.combinations(range(4),3))
 for ds in [(8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9),(9,9,9,10)]:
  for p in partitions(list(range(4))):
   options=[]
   for tr in triples:
    restricted=canonical([tuple(tr.index(i) for i in b if i in tr) for b in p if any(i in tr for i in b)])
    options.append([t for t in range(4) if (tuple(ds[i] for i in tr),restricted,t) in fails])
   if any(not q for q in options):continue
   for ts in itertools.product(*options):
    for q in range(min(ts)+1):
     f={0:35,1:8}|{1<<(i+1):ds[i] for i in range(4)}
     for m in range(1,16):
      inds=[i for i in range(4) if m>>i&1]
      f[(m<<1)|1]=int(any(all(i in b for i in inds) for b in p))
      if len(inds)==2:f[m<<1]=2 if min(ds[i] for i in inds)==8 else 3
     for tr,t in zip(triples,ts):f[sum(1<<(i+1) for i in tr)]=t
     f[30]=q
     ns={}
     for m in sorted(range(32),key=int.bit_count,reverse=True):ns[m]=f.get(m,0)-sum(n for k,n in ns.items() if k&m==m)
     if min(ns.values())<0:continue
     z=min((evaluate(19,ns,po) for po in poss),key=lambda x:x['bound'])
     out.append(dict(degrees=[8,*ds],partition=p,triples=ts,quadruple=q,bound=z['bound'],strict=z['strict'],positions=z['positions'],counts=ns))
 print('profiles',len(out),'strict',sum(z['strict'] for z in out),'elapsed',time.time()-start)
 for z in out:
  if not z['strict']:print('FAIL',z['degrees'],z['partition'],z['triples'],z['quadruple'],str(z['bound']),z['positions'])
 (HERE/'FOUR_NEIGHBOR_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=time.time()-start,layout_count=len(poss),profiles=out)),indent=2)+'\n')
if __name__=='__main__':main()
