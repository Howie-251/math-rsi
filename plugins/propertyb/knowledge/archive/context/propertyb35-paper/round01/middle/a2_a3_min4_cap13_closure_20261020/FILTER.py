"""Fresh16-spectrum complete moment domain, Gamma4..29 convex box, cap13, and actual pointpair row tau."""
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
@lru_cache(None)
def T(n,m,r):
 if not 0<=m<=n*(n-1)//2:return -10**12
 if n==0:return 0
 return max(f(r)+T(n-1,m,r),f(n-1+r)+T(n-1,m-n+1,r+1))
TT={n:T(35,n,0) for n in range(397,596)}
def box(n1):
 X=2*(595-n1)-140
 if not 0<=X<=875:return None
 a,b=divmod(X,25)
 return a*f(5)+(f(30-b)+(34-a)*f(30) if b else (35-a)*f(30))
def assign(caps,p,n1):
 cc=[0]*5;rem=p
 for j in range(4,-1,-1):cc[j]=min(rem,caps[j]);rem-=cc[j]
 return cc,6864*n1+sum(c*w for c,w in zip(cc,(36,120,330,792,1716)))
jobs=[];final=[];without_tau=[];total_domain=total_wedge=oldsurv=0
for a in (2,3):
 for b in range(11-2*a,10):
  e=2*a+b-11;h=20-a-b
  for part in partitions(e):
   ds=[6]+[7]*a+[8]*b+[9]*(h-len(part))+[9+x for x in part];assert len(ds)==21 and sum(ds)==175
   W=sum(comb(d,2) for d in ds);key=','.join(map(str,ds));rowlower=max(0,4*(max(ds)-10));cost={}
   for n1 in TT:
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
      oldcaps=(33*n0,35*n1-cost[n1],(24+e//2)*n2,14*m,4*t)
      _,oldL=assign(oldcaps,TT[n1],n1)
      if oldL>=THRESH:counts['old_T_cap14_survivors']+=1
      if t>13:continue
      pb=box(n1)
      if pb is None:continue
      p=min(TT[n1],pb);caps=(33*n0,35*n1-cost[n1],(24+e//2)*n2,13*m,4*t);C,L=assign(caps,p,n1)
      z=dict(spectrum_key=key,a=a,b=b,partition=part,n=[n0,n1,n2,m,t],tau=tau,T_P=TT[n1],box_P=pb,P=p,C_caps=caps,C=C,twice_L=L)
      if L>=THRESH:counts['min4_cap13_survivors']+=1;without_tau.append(z)
      if tau<rowlower:continue
      counts['row_admissible']+=1
      if max_admissible is None or L>max_admissible['twice_L']:max_admissible=z
      if L>=THRESH:counts['final_survivors']+=1;final.append(z)
   jobs.append(dict(key=key,a=a,b=b,partition=part,e=e,degrees=ds,W=W,tau_row_lower=rowlower,counts=dict(counts),maximum_admissible=max_admissible))
   total_domain+=counts['moments'];total_wedge+=counts['wedge'];oldsurv+=counts['old_T_cap14_survivors']
   print(a,b,part,dict(counts),flush=True)
   assert time.process_time()-st<12,'15CPU task cutoff'
assert len(jobs)==16
out=dict(scope=__doc__,complete=True,jobs=jobs,total_moment_keys_with_spectrum=total_domain,total_after_wedge=total_wedge,old_T_cap14_survivors=oldsurv,new_min4_cap13_survivors=len(without_tau),final_survivors=len(final),A2_final=sum(z['a']==2 for z in final),A3_final=sum(z['a']==3 for z in final),threshold_twice=THRESH,threshold_table=TT,cpu_seconds=time.process_time()-st)
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');(P/'SURVIVORS33.json').write_text(json.dumps(final,indent=2)+'\n');(P/'BEFORE_ROW202.json').write_text(json.dumps(without_tau,indent=2)+'\n');print('FINAL',{k:v for k,v in out.items() if k not in ('jobs','threshold_table')},flush=True)
