"""Bounded diagnostic, conditional on lambda<=4, C3<=13n3 and minGamma4. No x-star n4<=13, threshold/critical/prefix/DP import."""
from pathlib import Path
from collections import Counter
from math import comb
import time,json
P=Path(__file__).resolve().parent;st=time.process_time();limit=10
THRESHOLD2=5445440
def partitions(n,lo=1):
 if n==0:yield ();return
 for k in range(lo,n+1):
  for t in partitions(n-k,k):yield (k,)+t
def f(s):return (s*s-(s%5)*(s//5+1)**2-(5-s%5)*(s//5)**2)//2
# Exact35 boxes 0<=s<=30 and sum2n1 by discrete convexity; table no graph-realizability claim.
Pbox={}
for n1 in range(397,526):
 a,b=divmod(2*n1,30);Pbox[n1]=a*f(30)+f(b)
spectra=[]
for e in range(7):
 for part in partitions(e):
  if len(part)>7-e:continue
  ds=[8]*(14+e)+[9]*(7-e-len(part))+[9+j for j in part]
  assert len(ds)==21 and sum(ds)==175 and ds.count(8)==14+e
  spectra.append((e,part,ds))
assert len(spectra)==15
jobs=[];partial=None
for specid,(e,part,ds) in enumerate(spectra):
 W=sum(comb(d,2) for d in ds);C2coef=(sum(sorted(ds)[-6:])-6)//2;rowlow=max(0,4*(max(ds)-10));capacity=Counter()
 for d in ds:capacity[d]+=comb(d,2)
 costs={}
 for n1 in range(397,526):
  rem=n1;value=0
  for d,c in sorted(capacity.items()):
   take=min(rem,c);rem-=take;value+=take*d
  assert rem==0;costs[n1]=value
 survivors=[];domain=0;maxL2=-1;maxkey=None
 for n1 in range(397,526):
  p=Pbox[n1]
  # No extra n4 bound: moment lambda<=4 gives tau<=140 and6t<=140+tau automatically.
  for t in range(47):
   mmax=min((W-n1-4*t)//3,(140+140-6*t)//3)
   if mmax<0:continue
   for m in range(mmax+1):
    num=W-280+3*m+8*t-n1
    if num%2:continue
    tau=num//2
    if not rowlow<=tau<=140:continue
    n2=(W-n1-3*m-4*t)//2;n0=595-n1-n2-m-t
    if min(n0,n2)<0:continue
    assert n2+3*m+6*t==140+tau and n1+2*n2+3*m+4*t==W
    domain+=1
    caps=[33*n0,35*n1-costs[n1],C2coef*n2,13*m,4*t]
    rem=p;allocation=[0]*5;L2=6864*n1
    for j,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
     take=min(rem,caps[j]);allocation[j]=take;rem-=take;L2+=take*w
    key=[n0,n1,n2,m,t,tau,L2]
    if L2>maxL2:maxL2=L2;maxkey={'key':key,'Ccaps':caps,'allocation':allocation,'P':p}
    if L2>=THRESHOLD2:survivors.append(key)
    if domain%4096==0 and time.process_time()-st>limit:
     partial={'spectrum_id':specid,'n1':n1,'t':t,'m':m,'partial_domain':domain,'partial_survivors':len(survivors)};break
   if partial:break
  if partial:break
 if partial:break
 jobs.append({'spectrum_id':specid,'e':e,'high_excess_partition':part,'degrees':ds,'W':W,'C2_coefficient':C2coef,'row_tau_min':rowlow,'complete_domain':domain,'strict_domain':domain-len(survivors),'survivor_count':len(survivors),'maximum_L2':maxL2,'maximum_L':f'{maxL2}/2','maximum_witness':maxkey,'n4_range':([min(z[4] for z in survivors),max(z[4] for z in survivors)] if survivors else None),'E_range':([min(595-z[1] for z in survivors),max(595-z[1] for z in survivors)] if survivors else None),'survivors':survivors})
 print('SPECTRUM',specid,'e',e,'part',part,'domain',domain,'survive',len(survivors),'n4',jobs[-1]['n4_range'],'E',jobs[-1]['E_range'],'CPU',time.process_time()-st,flush=True)
out={'status':'COMPLETE_CONDITIONAL_DIAGNOSTIC' if partial is None else 'CPU_PROFILE_PARTIAL','scope':__doc__,'assumptions':['21points,35simple5edges,paircover,all degree>=8','e=summax(d-9,0)0..6; all partitions with length<=7-e; degree>=9 count7-e, no exact9 requirement','all pointpair lambda<=4 (conditional)','all C3<=13n3 (conditional)','all Gamma degree>=4 (conditional)','row tau>=4(Delta-10), tau<=140, n1>=397','C0<=33n0,C1<=35n1-cheapest degree flag cost,C2<=floor((S6-6)/2)n2,C4<=4n4','same P shared35 boxes with0<=s<=30, no lower singleton5 bound'],'no_extra_n4_bound':True,'no_wedge_extra_bound':True,'no_graph_or_H_realizability_claim':True,'degree_spectra':len(spectra),'completed_spectra':len(jobs),'partial':partial,'jobs':jobs,'cpu_seconds':time.process_time()-st}
(P/'CONDITIONAL_SCALAR_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],'CPU',out['cpu_seconds'])
