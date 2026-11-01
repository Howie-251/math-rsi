"""M=35 exact small-lock domain pilot; never enumerates full hypergraphs."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,permutations,product
from functools import lru_cache
from math import ceil
import sys,json,time
ROOT=Path(__file__).resolve().parents[4]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01'),str(ROOT/'context/propertyb34/round01/high-math')]
from multilock import Profile,rows,total_bound,json_value
from pure_quota import certificate
from bare_layout import BareLayout
HERE=Path(__file__).parent
@lru_cache(None)
def engine(v,pos):return BareLayout(v,pos)
def evaluate(v,ns,pos,detail=False):
 p=Profile(v,5,pos,ns)
 cs=[certificate(p,i) for i in range(len(pos))]
 bare,rr=engine(v,tuple(pos)).bound(ns,True)
 value=sum((min(a,b,c-cs[pos.index(k)]['loss']) if k in pos else min(a,b,c) for k,(a,b,c) in enumerate(rr,1)),Q())
 out=dict(v=v,M=35,counts=ns,positions=pos,bound=value,strict=value<1,quotas=cs)
 if detail:
  rr2=rows(p,deductions={pos[i]:c['loss'] for i,c in enumerate(cs)})
  assert total_bound(rr2)==value
  assert all((r['A'],r['B'],r['C'])==abc for r,abc in zip(rr2,rr))
  out['rows']=rr2;out['independent_ordered_pair_check']=True
 return out

def layouts(v,s,full=False):
 if s==1:return [(i,) for i in range(1,v+1)]
 if full:return list(permutations(range(1,v+1),s)) if s==2 else list(combinations(range(1,v+1),s))
 pos=set()
 for start in range(1,v-s+2):
  p=tuple(range(start,start+s));pos.add(p)
  if s==2:pos.add(p[::-1])
 for a in (1,2,3,v):
  for b in range(v//2-2,v//2+4):
   if s==2 and a!=b:pos.add((a,b));pos.add((b,a))
 return sorted(pos)
def best(v,ns,full=False):
 s=max(ns).bit_length()
 candidates=layouts(v,s,full)
 z=min((evaluate(v,ns,p) for p in candidates),key=lambda z:z['bound'])
 out=evaluate(v,ns,z['positions'],True);out['tested_layout_count']=len(candidates);out['full_layout_search']=full
 return out

def double(v,a,b,c):return {0:35-a-b+c,1:a-c,2:b-c,3:c}
def triple(v,d,pairs,t):
 a,b,c=pairs;x,y,z=d
 return {0:35-x-y-z+a+b+c-t,1:x-a-b+t,2:y-a-c+t,4:z-b-c+t,3:a-t,5:b-t,6:c-t,7:t}

def main():
 start=time.time();singles=[];doubles=[];triples=[]
 for v in range(19,25):
  for d in range(ceil((v-1)/4),175//v+1):
   z=best(v,{0:35-d,1:d});z['degree']=d;singles.append(z);print('single',v,d,z['bound'],flush=True)
 for v in range(19,25):
  d0=ceil((v-1)/4)
  for a in range(d0,175//v+1):
   unit=2*(v-1)-4*a
   if unit<=0:continue
   # Minimum-degree center; outside its guaranteed unit neighbours other degrees >=a.
   bmax=a+(175-v*a)//unit
   for b in range(a,bmax+1):
    z=best(v,double(v,a,b,1));z['degrees']=[a,b];z['codegree']=1;z['unit_partner_upper']=bmax
    if z['bound']>=1:z=best(v,double(v,a,b,1),True)|{'degrees':[a,b],'codegree':1,'unit_partner_upper':bmax}
    doubles.append(z);print('unit',v,a,b,z['bound'],flush=True)
 # Highest new degree centers, strong pair and small triplet domains.
 for v,d in [(19,8),(19,9),(20,7),(20,8),(21,7),(21,8),(22,6),(22,7),(23,6),(23,7),(24,6),(24,7)]:
  for c in range(2,d+1):
   z=best(v,double(v,d,d,c));z.update(degrees=[d,d],codegree=c)
   doubles.append(z);print('samepair',v,d,c,z['bound'],flush=True)
 for v,d,limit in [(19,8,2),(19,9,3),(20,8,3),(21,8,3)]:
  for a,b,c in combinations(range(1,limit+3),3):pass
  for ps in combinations(range(1,limit+3),3):pass
  for ps in product(range(1,limit+1),repeat=3):
   if sorted(ps)!=list(ps):continue
   for t in range(min(ps)+1):
    ns=triple(v,[d]*3,ps,t)
    if min(ns.values())<0:continue
    z=best(v,ns);z.update(degrees=[d]*3,codegrees=ps,triple=t)
    triples.append(z);print('triple',v,d,ps,t,z['bound'],flush=True)
 out=dict(scope=__doc__,elapsed_seconds=time.time()-start,singles=singles,doubles=doubles,triples=triples)
 (HERE/'PILOT.json').write_text(json.dumps(json_value(out),indent=2)+'\n')
 print('elapsed',time.time()-start,flush=True)
if __name__=='__main__':main()
