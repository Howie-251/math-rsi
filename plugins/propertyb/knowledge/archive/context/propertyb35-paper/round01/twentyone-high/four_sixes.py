"""Complete actual four-degree6 input after pairwise codegree2 is forced by every three-degree6 view."""
from pathlib import Path
import itertools,json,time
import sys
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb34/round01/high-math')]
from subset_position_dp import SubsetEngine
from multilock import json_value
HERE=Path(__file__).parent

def main():
 st=time.time();out=[];trip=list(itertools.combinations(range(4),3))
 for ts in itertools.product(range(3),repeat=4):
  for q in range(min(ts)+1):
   inc={0:35}|{1<<i:6 for i in range(4)}|{(1<<i)|(1<<j):2 for i,j in itertools.combinations(range(4),2)}|{sum(1<<i for i in T):t for T,t in zip(trip,ts)}|{15:q}
   ns={m:sum((-1)**(u.bit_count()-m.bit_count())*v for u,v in inc.items() if u&m==m) for m in range(16)}
   if min(ns.values())<0:continue
   eng=SubsetEngine(21,4,ns);z=eng.verify(eng.solve());z.update(degrees=[6]*4,triples=ts,four=q,strict=z['bound']<1);out.append(z)
 (HERE/'FOUR_SIXES.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('domain',len(out),'strict',sum(z['strict'] for z in out),'max',max(z['bound'] for z in out),'seconds',time.time()-st)
 for z in out:
  if not z['strict']:print(z['triples'],z['four'],z['bound'])
if __name__=='__main__':main()
