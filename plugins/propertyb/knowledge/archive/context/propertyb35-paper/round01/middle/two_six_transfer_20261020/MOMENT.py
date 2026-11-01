"""Two-six nine-spectrum complete moment domain, Gamma4..34 convex box; no critical import or T in new bound, cap13, and actual pointpair row tau."""
from pathlib import Path
from functools import lru_cache
from math import comb
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();THRESH=5445440

def partitions(n,lo=1):
 if n==0:yield ();return
 for a in range(lo,n+1):
  for b in partitions(n-a,a):yield (a,)+b

def f(s):
 a,b=divmod(s,5);return (s*s-(5-b)*a*a-b*(a+1)**2)//2
N1_RANGE=range(397,596)
def box(n1):
 X=2*(595-n1)-140
 if not 0<=X<=1050:return None
 a,b=divmod(X,30)
 return a*f(0)+(f(30-b)+(34-a)*f(30) if b else (35-a)*f(30))
def assign(caps,p,n1):
 cc=[0]*5;rem=p
 for j in range(4,-1,-1):cc[j]=min(rem,caps[j]);rem-=cc[j]
 return cc,6864*n1+sum(c*w for c,w in zip(cc,(36,120,330,792,1716)))
jobs=[];final=[];without_tau=[];total_domain=total_wedge=oldsurv=0
for a in (0,1):
 for b in range(8-2*a,10):
  e=2*a+b-8;h=19-a-b
  for part in partitions(e):
   ds=[6]*2+[7]*a+[8]*b+[9]*(h-len(part))+[9+x for x in part];assert len(ds)==21 and sum(ds)==175
   W=sum(comb(d,2) for d in ds);key=','.join(map(str,ds));rowlower=max(0,4*(max(ds)-10));cost={}
   for n1 in N1_RANGE:
    rem=n1;k=0
    for d in ds:
     q=min(rem,comb(d,2));k+=d*q;rem-=q
    assert rem==0;cost[n1]=k
   counts=Counter();max_admissible=None
   for tau in range(141):
    for t in range((140+tau)//6+1):
     aa,bb=divmod(2*t,35);wedge=(35-bb)*comb(aa,2)+bb*comb(aa+1,2)
     for m in range((140+tau-6*t)//3+1):
      n1=W-280-2*tau+3*m+8*t;n2=140+tau-3*m-6*t;n0=735-W+tau-m-3*t
      if min(n0,n1,n2)<0 or not 397<=n1<=595:continue
      counts['moments']+=1
      if 3*wedge>4*tau:continue
      counts['wedge']+=1
      if t>13:continue
      pb=box(n1)
      if pb is None:continue
      p=pb;caps=(33*n0,35*n1-cost[n1],(24+e//2)*n2,13*m,4*t);C,L=assign(caps,p,n1)
      z=dict(spectrum_key=key,a=a,b=b,partition=part,n=[n0,n1,n2,m,t],tau=tau,box_P=pb,P=p,C_caps=caps,C=C,twice_L=L)
      if L>=THRESH:counts['min4_cap13_survivors']+=1;without_tau.append(z)
      if tau<rowlower:continue
      counts['row_admissible']+=1
      if max_admissible is None or L>max_admissible['twice_L']:max_admissible=z
      if L>=THRESH:counts['final_survivors']+=1;final.append(z)
   jobs.append(dict(key=key,a=a,b=b,partition=part,e=e,degrees=ds,W=W,tau_row_lower=rowlower,counts=dict(counts),maximum_admissible=max_admissible))
   total_domain+=counts['moments'];total_wedge+=counts['wedge'];oldsurv+=counts['old_T_cap14_survivors']
   print(a,b,part,dict(counts),flush=True)
   assert time.process_time()-st<12,'15CPU task cutoff'
assert len(jobs)==9
out=dict(scope=__doc__,complete=True,jobs=jobs,total_moment_keys_with_spectrum=total_domain,total_after_wedge=total_wedge,new_min4_cap13_survivors=len(without_tau),final_survivors=len(final),a0_final=sum(z['a']==0 for z in final),a1_final=sum(z['a']==1 for z in final),threshold_twice=THRESH,cpu_seconds=time.process_time()-st)
(P/'MOMENT_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');(P/'MOMENT_SURVIVORS.json').write_text(json.dumps(final,indent=2)+'\n');(P/'MOMENT_BEFORE_ROW.json').write_text(json.dumps(without_tau,indent=2)+'\n');print('FINAL',{k:v for k,v in out.items() if k != 'jobs'},flush=True)
