"""Second full spectrum/moment generation (n1,n3,n4 parity), independent box knapsack, no threshold import."""
from pathlib import Path
from math import comb
from itertools import product
from collections import Counter
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();saved=json.loads((P/'RESULT.json').read_text())
old202=json.loads((P/'BEFORE_ROW202.json').read_text());old33=json.loads((P/'SURVIVORS33.json').read_text())
def F(s):
 b=[s//5+int(i<s%5) for i in range(5)]
 return sum(b[i]*b[j] for i in range(5) for j in range(i))
# Independent35-slot exact scalar optimization over q4..29, all sums.
kn=[0]
for slots in range(1,36):
 nxt=[-10**9]*(25*slots+1)
 for mass,previous in enumerate(kn):
  for r in range(26):
   value=previous+F(30-r)
   if value>nxt[mass+r]:nxt[mass+r]=value
 kn=nxt
for x,value in enumerate(kn):
 a,b=divmod(x,25);closed=a*F(5)+(F(30-b)+(34-a)*F(30) if b else (35-a)*F(30))
 assert value==closed
spectra={}
for a in (2,3):
 for hist in product(range(5),repeat=4):
  excess=sum((j+1)*v for j,v in enumerate(hist));b=11-2*a+excess
  if b>9:continue
  degrees=[6]+[7]*a+[8]*b+[9]*(20-a-b-sum(hist))
  for j,count in enumerate(hist):degrees.extend([10+j]*count)
  if len(degrees)!=21:continue
  assert sum(degrees)==175
  key=','.join(map(str,degrees));spectra[key]=degrees
assert len(spectra)==16 and set(spectra)=={j['key'] for j in saved['jobs']}
def key(z):return(z['spectrum_key'],tuple(z['n']),z['tau'])
res202={};res33={};jobs=[]
for sk,ds in sorted(spectra.items()):
 W=sum(d*(d-1)//2 for d in ds);e=sum(max(d-9,0) for d in ds);a=ds.count(7);b=ds.count(8);lower=max(0,4*(max(ds)-10));capacities=Counter()
 for d in ds:capacities[d]+=comb(d,2)
 costs={}
 for n1 in range(397,526):
  remaining=n1;cost=0
  for d,c in sorted(capacities.items()):take=min(remaining,c);remaining-=take;cost+=take*d
  assert remaining==0;costs[n1]=cost
 maxL=None;ct=Counter()
 for n1 in range(397,526):
  X=2*(595-n1)-140;p=kn[X]
  for t in range(14):
   quotient,remainder=divmod(2*t,35);wedge=(35-remainder)*comb(quotient,2)+remainder*comb(quotient+1,2)
   for m in range((W-n1-4*t)//3+1):
    numerator=W-280+3*m+8*t-n1
    if numerator%2:continue
    tau=numerator//2
    if not 0<=tau<=140 or 3*wedge>4*tau:continue
    n2=(W-n1-3*m-4*t)//2;n0=595-n1-n2-m-t
    if min(n0,n2)<0:continue
    assert sum([n0,n1,n2,m,t])==595 and n1+2*n2+3*m+4*t==W and n2+3*m+6*t==140+tau
    cap=(33*n0,35*n1-costs[n1],((sum(sorted(ds)[-6:])-6)//2)*n2,13*m,4*t)
    remaining=p;allocation=[0]*5
    for j in (4,3,2,1,0):allocation[j]=min(cap[j],remaining);remaining-=allocation[j]
    value=Fraction(sum(x*w for x,w in zip(allocation,(36,120,330,792,1716)))+6864*n1,2)
    z=dict(spectrum_key=sk,a=a,b=b,n=[n0,n1,n2,m,t],tau=tau,P=p,C_caps=list(cap),C=allocation,L=str(value),twice_L=int(2*value))
    if value>=2722720:res202[key(z)]=z
    if tau<lower:continue
    ct['row_admissible']+=1
    if maxL is None or value>Fraction(maxL['L']):maxL=z
    if value>=2722720:res33[key(z)]=z
 jobs.append(dict(key=sk,a=a,b=b,maximum_admissible=maxL,counts=dict(ct),survivors=sum(k[0]==sk for k in res33)))
assert set(res202)=={key(z) for z in old202} and len(res202)==202
assert set(res33)=={key(z) for z in old33} and len(res33)==33
for z in old202:
 v=res202[key(z)]
 assert v['P']==z['P'] and v['C_caps']==z['C_caps'] and v['C']==z['C'] and v['twice_L']==z['twice_L']
for j in jobs:
 old=next(r for r in saved['jobs'] if r['key']==j['key'])
 assert j['counts']['row_admissible']==old['counts']['row_admissible']
 assert j['maximum_admissible']['twice_L']==old['maximum_admissible']['twice_L']
 assert j['survivors']==old['counts'].get('final_survivors',0)
assert all(j['survivors']==0 for j in jobs if j['a']==2)
out=dict(status='PASS',scope=__doc__,full_spectra=16,independent_box_sum_states=len(kn),complete_box_only_survivors_before_row=len(res202),complete_box_only_survivors_after_row=len(res33),A2_survivors=0,A3_survivors=33,full202_keys_equal=True,full33_keys_equal=True,all_saved_allocations_equal=True,threshold_recurrence_needed_for_new_proof=False,jobs=jobs,cpu_seconds=time.process_time()-st)
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='jobs'}))
