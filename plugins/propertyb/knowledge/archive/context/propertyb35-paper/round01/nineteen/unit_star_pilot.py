"""Complete tiny actual unit-star trace domain, not a whole-hypergraph search."""
from pathlib import Path
import sys,json,itertools,time
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'));sys.path.insert(0,str(Path(__file__).parent))
from pilot import evaluate,json_value
from quick import from_intersections
HERE=Path(__file__).parent
parts=[[(0,),(1,),(2,)],[(0,1),(2,)],[(0,2),(1,)],[(1,2),(0,)],[(0,1,2)]]

def profile(ds,part,t):
 f={0:35,1:8}|{1<<(i+1):d for i,d in enumerate(ds)}
 for i in range(3):f[1|(1<<(i+1))]=1
 for i,j in itertools.combinations(range(3),2):
  m=(1<<(i+1))|(1<<(j+1));f[m]=2 if min(ds[i],ds[j])==8 else 3
  f[m|1]=int(any(i in b and j in b for b in part))
 f[14]=t;f[15]=int(len(part)==1)
 ns={}
 for m in sorted(range(16),key=int.bit_count,reverse=True):ns[m]=f.get(m,0)-sum(n for q,n in ns.items() if q&m==m)
 return ns

def main():
 start=time.time();out=[]
 poss=set()
 for startpos in range(1,17):
  for p in itertools.permutations(range(startpos,startpos+4)):poss.add(p)
 for q in [(1,2,11,12),(1,7,12,13),(1,5,11,15),(1,6,12,18)]:poss.update(itertools.permutations(q))
 poss=sorted(poss)
 for ds in [(8,8,8),(8,8,9),(8,9,9),(9,9,9),(9,9,10)]:
  for part in parts:
   for t in range(4):
    ns=profile(ds,part,t)
    if min(ns.values())<0:continue
    z=min((evaluate(19,ns,p) for p in poss),key=lambda x:x['bound'])
    out.append(dict(degrees=[8,*ds],partition=part,t=t,bound=z['bound'],strict=z['strict'],positions=z['positions'],counts=ns))
 print('profiles',len(out),'strict',sum(z['strict'] for z in out),'elapsed',time.time()-start)
 for ds in [(8,8,8),(8,8,9),(8,9,9),(9,9,9),(9,9,10)]:
  r=[z for z in out if z['degrees']==[8,*ds]]
  print(ds,'strict',sum(z['strict'] for z in r),'/',len(r),'fails',[(z['partition'],z['t'],str(z['bound']),z['positions']) for z in r if not z['strict']])
 (HERE/'UNIT_STAR_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=time.time()-start,layout_count=len(poss),profiles=out)),indent=2)+'\n')
if __name__=='__main__':main()
