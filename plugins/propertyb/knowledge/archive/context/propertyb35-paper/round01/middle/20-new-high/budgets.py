"""Complete integer degree-spectrum necessary domains and Caro-Wei guarantees.
No claim that retained spectra are realizable by pair-covering five-uniform H.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import ceil
from collections import Counter
import json,time
HERE=Path(__file__).parent

def partitions(total,maxlen,maxpart,lo=1):
 if total==0:yield ();return
 if not maxlen:return
 for a in range(lo,min(total,maxpart)+1):
  for rest in partitions(total-a,maxlen-1,maxpart,a):yield (a,)+rest

def cw(degrees,D):
 L=[d for d in degrees if d<=D];r=len(L)
 if not r:return 0,Q(),Q()
 excess=sum(4*d-19 for d in L);twoe=min(r*(r-1),2*(excess//2))
 avg=Q(r*r,r+twoe);individual=sum((Q(1,min(r-1,4*d-19)+1) for d in L),Q())
 return ceil(max(avg,individual)),avg,individual

def main():
 start=time.time();groups=[]
 for delta,budget,partsmax in [(7,35,19),(8,15,20)]:
  out=[]
  for ps in partitions(budget,partsmax,35-delta):
   ds=[delta]*(20-len(ps))+[delta+a for a in ps]
   assert len(ds)==20 and min(ds)==delta and sum(ds)==175
   vals=[(D,*cw(ds,D)) for D in range(delta,max(ds)+1)]
   thresholds={str(s):next((D for D,g,a,b in vals if g>=s),None) for s in (2,3)}
   out.append(dict(histogram=dict(Counter(ds)),cw_threshold=thresholds,max_cw_guarantee=max(g for D,g,a,b in vals)))
  group=dict(delta=delta,degree_excess_budget=budget,spectrum_count=len(out),unit_pair_threshold_counts=dict(Counter(r['cw_threshold']['2'] for r in out)),unit_triple_threshold_counts=dict(Counter(r['cw_threshold']['3'] for r in out)),spectra=out)
  groups.append(group)
 result=dict(scope=__doc__,groups=groups,elapsed_seconds=time.time()-start)
 (HERE/'DEGREE_BUDGETS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(dict(elapsed_seconds=result['elapsed_seconds'],groups=[{k:v for k,v in r.items() if k!='spectra'} for r in groups]),indent=2))
if __name__=='__main__':main()
