"""Conditional min7-exact/e<=4 full-degree-spectrum preflight, minGamma4/lambda<=4/C3cap13 assumed; not a coloring proof."""
from pathlib import Path
from collections import Counter
from math import comb
import time,json,argparse
P=Path(__file__).resolve().parent;st=time.process_time();ap=argparse.ArgumentParser();ap.add_argument('--profile',action='store_true');arg=ap.parse_args();limit=2 if arg.profile else 18

def partitions(n,lo=1):
 if not n:yield ();return
 for v in range(lo,n+1):
  for t in partitions(n-v,v):yield(v,)+t
def f(s):
 a,r=divmod(s,5)
 return (s*s-r*(a+1)**2-(5-r)*a*a)//2
spectra=[]
for e in range(5):
 for a7 in range(1,22):
  a8=14+e-2*a7;high=21-a7-a8
  if a8<0 or high<0:continue
  for part in partitions(e):
   if len(part)>high:continue
   ds=[7]*a7+[8]*a8+[9]*(high-len(part))+[9+j for j in part]
   assert len(ds)==21 and min(ds)==7 and sum(ds)==175
   assert 2*a7+a8==14+e and sum(max(d-9,0) for d in ds)==e
   spectra.append({'spectrum_id':len(spectra),'a7':a7,'a8':a8,'e':e,'part':part,'degrees':ds})
assert len(spectra)==99 and len({tuple(s['degrees']) for s in spectra})==99
B={n:360*(2*n//30)+f(2*n%30) for n in range(397,526)}
alljobs=[];partial=None
for job in spectra:
 ds=job['degrees'];W=sum(comb(d,2) for d in ds);coef=(sum(sorted(ds)[-6:])-6)//2;rowlo=max(0,4*(max(ds)-10));flags=Counter()
 for v in ds:flags[v]+=comb(v,2)
 costs={}
 for n1 in range(397,526):
  rem=n1;c=0
  for v,num in sorted(flags.items()):take=min(rem,num);rem-=take;c+=take*v
  assert rem==0;costs[n1]=c
 domain=0;strict=0;survivors=0;maxL=-1;maximum=None;nrange=[[10**9,-1] for j in range(5)];taur=[10**9,-1];Er=[10**9,-1];Lr=[10**9,-1];sample=[];by_t=Counter();by_E=Counter()
 for tau in range(rowlo,141):
  for t in range((140+tau)//6+1):
   lo=max(0,(397-W+280+2*tau-8*t+2)//3)
   hi=min((525-W+280+2*tau-8*t)//3,(140+tau-6*t)//3,735-W+tau-3*t)
   for m in range(lo,hi+1):
    n1=W-280-2*tau+3*m+8*t;n2=140+tau-3*m-6*t;n0=735-W+tau-m-3*t
    domain+=1
    caps=[33*n0,35*n1-costs[n1],coef*n2,13*m,4*t];rem=B[n1];v=6864*n1;allocation=[0]*5
    for j,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
     take=min(caps[j],rem);rem-=take;allocation[j]=take;v+=w*take
    if v>maxL:maxL=v;maximum={'n':[n0,n1,n2,m,t],'tau':tau,'twice_L':v,'P':B[n1],'caps':caps,'allocation':allocation}
    if v<5445440:strict+=1
    else:
     survivors+=1;E=595-n1;by_t[t]+=1;by_E[E]+=1;nv=(n0,n1,n2,m,t)
     for i,x in enumerate(nv):nrange[i][0]=min(x,nrange[i][0]);nrange[i][1]=max(x,nrange[i][1])
     taur[0]=min(tau,taur[0]);taur[1]=max(tau,taur[1]);Er[0]=min(E,Er[0]);Er[1]=max(E,Er[1]);Lr[0]=min(v,Lr[0]);Lr[1]=max(v,Lr[1])
     if len(sample)<5:sample.append({'n':nv,'tau':tau,'twice_L':v})
    if domain%4096==0 and time.process_time()-st>limit:
     partial={'spectrum':job,'resume_after':{'tau':tau,'n4':t,'n3':m},'domain_prefix':domain,'strict_prefix':strict,'survivor_prefix':survivors};break
   if partial:break
  if partial:break
 if partial:break
 out={**job,'W':W,'S6':sum(sorted(ds)[-6:]),'C2_coefficient':coef,'row_tau_lower':rowlo,'complete_domain':domain,'strict_count':strict,'survivor_count':survivors,'all_strict':not survivors,'maximum_twice_L':maxL,'maximum_witness':maximum,'survivor_n_ranges':nrange if survivors else None,'survivor_tau_range':taur if survivors else None,'survivor_E_range':Er if survivors else None,'survivor_twice_L_range':Lr if survivors else None,'survivors_by_n4':dict(by_t),'survivors_by_E':dict(by_E),'first5_survivor_keys':sample}
 alljobs.append(out);print('SPECTRUM',job['spectrum_id'],'e/a7/a8',job['e'],job['a7'],job['a8'],'part',job['part'],'domain',domain,'survivors',survivors,'CPU',time.process_time()-st,flush=True)
 if arg.profile:break
status='PROFILE_ONE_FULL_SPECTRUM' if arg.profile and not partial else 'COMPLETE_CONDITIONAL99_SPECTRA' if len(alljobs)==len(spectra) else 'CPU_BOUNDED_PARTIAL'
res={'status':status,'scope':__doc__,'assumptions':['H21/M35/simple5/paircover/minimumdegree exactly7','e=summax(d-9,0)<=4','all pointpair lambda<=4 is explicit condition','all Gamma degree>=4 is explicit condition','C3<=13n3 is explicit condition; generic c14local gate applies when upstream paircap supplied','sameP convex35 boxes0..30; C0<=33n0,C1<=35n1-Kd,C2<=floor((actualS6-6)/2)n2,C4<=4n4','0<=tau<=140, rowtau>=max(0,4Delta-40),397<=n1<=525'],'no_implicit_Delta9':True,'no_critical_or_T_or_prefix_or_extra_n4_or_wedge':True,'integer_threshold_twice_L':5445440,'full_spectrum_count':len(spectra),'completed_spectra':len(alljobs),'strict_spectrum_count':sum(j['all_strict'] for j in alljobs),'mixed_spectrum_count':sum(not j['all_strict'] for j in alljobs),'completed_moment_keys':sum(j['complete_domain'] for j in alljobs),'total_completed_survivors':sum(j['survivor_count'] for j in alljobs),'partial_current_spectrum':partial,'uncompleted_spectra':spectra[len(alljobs):] if len(alljobs)<len(spectra) else [],'jobs':alljobs,'cpu_seconds':time.process_time()-st}
(P/('PROFILE.json' if arg.profile else 'RESULT.json')).write_text(json.dumps(res,indent=2)+'\n');print(status,'COMPLETED',len(alljobs),'STRICT',res['strict_spectrum_count'],'CPU',res['cpu_seconds'])
