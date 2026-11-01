"""21-point M35 complete minimum-center double domains and targeted small triple domains."""
from pathlib import Path
import sys,itertools,time,json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb34/round01/high-math')]
from pilot import double,triple,json_value
from subset_position_dp import SubsetEngine

def solve(ns,s):
 eng=SubsetEngine(21,s,ns);z=eng.verify(eng.solve());z['strict']=z['bound']<1;return z

def main():
 st=time.time();out=[]
 for d in (6,7,8):
  for b in range(d,min(35,175-20*d)+1):
   for c in range(1,min(d,4*d-19)+1):
    ns=double(21,d,b,c)
    if min(ns.values())<0:continue
    z=solve(ns,2);z.update(degrees=[d,b],codegree=c);out.append(z)
  rr=[r for r in out if r['degrees'][0]==d];print('double center',d,'cases',len(rr),'strict',sum(r['strict'] for r in rr),'unit residual',[r['degrees'][1] for r in rr if r['codegree']==1 and not r['strict']],flush=True)
 (HERE/'DOUBLES.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n')
 tri=[]
 for ds,cap in [([6,6,6],3),([6,7,7],3),([7,7,7],3),([7,8,8],3),([8,8,8],4)]:
  for ps in itertools.product(range(1,cap+1),repeat=3):
   if list(ps)!=sorted(ps):continue
   if any(sum(c-1 for ij,c in zip(itertools.combinations(range(3),2),ps) if i in ij)>4*d-20 for i,d in enumerate(ds)):continue
   for t in range(min(ps)+1):
    ns=triple(21,ds,ps,t)
    if min(ns.values())<0:continue
    z=solve(ns,3);z.update(degrees=ds,codegrees=ps,triple=t);tri.append(z)
  rr=[r for r in tri if r['degrees']==ds];print('triple',ds,'cases',len(rr),'strict',sum(r['strict'] for r in rr),'unit',[(r['triple'],str(r['bound'])) for r in rr if r['codegrees']==[1,1,1]],flush=True)
 (HERE/'TRIPLES.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=False,scope_note='Equal-degree triples complete up to labels within codegree cap; mixed tuples are sorted-codegree diagnostic samples only.',cases=tri,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
if __name__=='__main__':main()
