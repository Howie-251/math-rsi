"""Complete 888 triple-core domain, and optional actual-x star expansion; no H enumeration."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import sys,json,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb34/round01/high-math')]
from subset_position_dp import SubsetEngine
from pilot import json_value,triple

def solve(ds,ns,parameters):
 e=SubsetEngine(21,len(ds),ns);z=e.verify(e.solve())
 return dict(degrees=ds,parameters=parameters,counts=ns,positions=z['positions'],bound=z['bound'],
             strict=z['bound']<1,quota_losses=[c['loss'] for c in z['certificates']])

def stars(ns,margin):
 # Direct h_T recursion on all nonempty original G-trace slots; h_0 is recovered.
 caps=[ns.get(t,0) for t in range(8)]
 hh=[0]*8
 def rec(t,rem,total):
  if t==8:
   if any(rem):return
   h0=6-total
   if 0<=h0<=caps[0]:
    hh[0]=h0;yield tuple(hh)
   return
  members=[i for i in range(3) if t>>i&1]
  lim=min([caps[t],6-total]+[rem[i] for i in members])
  for value in range(lim+1):
   hh[t]=value
   nxt=list(rem)
   for i in members:nxt[i]-=value
   yield from rec(t+1,nxt,total+value)
 yield from rec(1,list(margin),0)

def main():
 st=time.process_time();core=[];low=[]
 for ps in product(range(2,5),repeat=3):
  for q in range(2,min(ps)+1):
   ns=triple(21,[8]*3,ps,q)
   if min(ns.values())<0:continue
   core.append(solve([8]*3,ns,dict(pairs=ps,triple=q)))
 for c in range(2,5):
  ns=triple(21,[6,8,8],[2,2,c],2)
  low.append(solve([6,8,8],ns,dict(pairs=[2,2,c],triple=2)))
 assert len(core)==36
 bad=[i for i,r in enumerate(core) if not r['strict']]
 domain=[]
 for sid in bad:
  ns=core[sid]['counts']
  for margin in product((1,2),repeat=3):
   hs=list(stars(ns,margin))
   domain.append(dict(source_id=sid,x_margins=margin,count=len(hs)))
 out=dict(scope=__doc__,complete_888_three_lock_domain=True,cases=core,nonstrict_ids=bad,
          low_xBB_cases=low,star_domain_counts=domain,total_star_candidates=sum(r['count'] for r in domain),
          cpu_seconds=time.process_time()-st)
 (HERE/'PILOT.json').write_text(json.dumps(json_value(out),indent=2)+'\n')
 print('888',len(core),'nonstrict',len(bad),'max',max(r['bound'] for r in core),flush=True)
 print('low xBB',[(r['parameters'],str(r['bound'])) for r in low],flush=True)
 print('all nonstrict star candidates',out['total_star_candidates'],'CPU',out['cpu_seconds'],flush=True)
if __name__=='__main__':main()
