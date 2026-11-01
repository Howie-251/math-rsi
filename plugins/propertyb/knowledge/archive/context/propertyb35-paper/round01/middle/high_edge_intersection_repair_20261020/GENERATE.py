"""Complete four-lock high-intersection domains; no whole-H search."""
from pathlib import Path
from itertools import combinations, product
from fractions import Fraction
import sys,json,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb34/round01/high-math')]
from subset_position_dp import SubsetEngine
from pilot import json_value, double
PAIRS=list(combinations(range(4),2));PM=[sum(1<<i for i in p) for p in PAIRS];TM=[7,11,13,14]
def p_domain():
 for ds in ([7,8,8,8],[7,8,8,9],[7,8,9,9],[7,9,9,9]):
  caps=[3 if i==0 and ds[j]==8 else 4 for i,j in PAIRS]
  for q in range(2,min(caps)+1):
   for tt in product(range(3),repeat=4):
    rem=[caps[k]-q-sum(v for m,v in zip(TM,tt) if m&p==p) for k,p in enumerate(PM)]
    if min(rem)<0:continue
    for pp in product(*(range(r+1) for r in rem)):
     ns={15:q,**dict(zip(TM,tt)),**dict(zip(PM,pp))}
     singles=[ds[i]-sum(n for m,n in ns.items() if m>>i&1) for i in range(4)]
     if min(singles)<0:continue
     codegrees=[q+sum(v for m,v in zip(TM,tt) if m&p==p)+pp[k] for k,p in enumerate(PM)]
     if any(sum(c-1 for ij,c in zip(PAIRS,codegrees) if i in ij)>4*ds[i]-20 for i in range(4)):continue
     ns.update({1<<i:v for i,v in enumerate(singles)});ns[0]=35-sum(ns.values())
     assert ns[0]>=0
     yield list(ds),ns

def solve(ds,ns,params=None):
 e=SubsetEngine(21,4,ns);z=e.verify(e.solve())
 return dict(degrees=ds,counts=ns,positions=z['positions'],bound=z['bound'],strict=z['bound']<1,
             quota_losses=[r['loss'] for r in z['certificates']],parameters=params)

def main():
 st=time.process_time();xx=[]
 for a,b,c in product(range(3),repeat=3):
  for t in range(min(a,b,c)+1):
   ns={15:2,1:4,2:6-a-b+t,4:6-a-c+t,8:6-b-c+t,6:a-t,10:b-t,12:c-t,14:t,0:11+a+b+c-t}
   xx.append(solve([6,8,8,8],ns,[a,b,c,t]))
 out=[];counts={};bad=[]
 for ds,ns in p_domain():
  out.append(solve(ds,ns));key=','.join(map(str,ds));counts[key]=counts.get(key,0)+1
  if not out[-1]['strict']:bad.append(len(out)-1)
  assert time.process_time()-st<100,'explicit CPU ceiling'
 # Existing 7/8,7/9,8/8,8/9 source pair gates are frozen; add missing 9/9 c5..9.
 extra=[]
 for c in range(5,10):
  ns=double(21,9,9,c);e=SubsetEngine(21,2,ns);z=e.verify(e.solve())
  extra.append(dict(degrees=[9,9],codegree=c,counts=ns,positions=z['positions'],bound=z['bound'],strict=z['bound']<1,quota_losses=[r['loss'] for r in z['certificates']]))
 result=dict(scope=__doc__,complete=True,x_cases=xx,p_cases=out,extra_pair_gates=extra,
  p_counts_by_degrees=counts,p_nonstrict_ids=bad,x_max=max(r['bound'] for r in xx),p_max=max(r['bound'] for r in out),cpu_seconds=time.process_time()-st)
 (HERE/'RESULT.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
 print(json.dumps({k:str(v) for k,v in result.items() if k not in ['x_cases','p_cases','extra_pair_gates']}))
if __name__=='__main__':main()
