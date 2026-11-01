"""Full moment-domain refinement for the 81 actual all-codegree<=4 low-excess spectra.
Uses the existing generic cap13 theorem (e<=4) and stronger proven cap12 callers
where their complete actual quad projection is available. No new lock layouts.
"""
from pathlib import Path
from collections import Counter
from itertools import product
from math import comb
import json,time

P=Path(__file__).resolve().parent
M=P.parent.parent/'middle'
start=time.process_time()
old=json.loads((M/'min_degree_seven_gamma_four_low_excess_diagnostic_20261020/RESULT.json').read_text())
strong=json.loads((M/'min_degree_seven_low_excess_strong_pairs_20261020/RESULT.json').read_text())
cap12=json.loads((M/'min_degree_seven_cap12_transfer_20261020/RESULT.json').read_text())
ids=set(strong['nonB_all_lambda_le4_spectrum_ids'])
cap12ids=set(cap12['cap12_ready_ids'])
assert len(ids)==81
def f(s):
 a,r=divmod(s,5)
 return (s*s-r*(a+1)**2-(5-r)*a*a)//2
box={n:360*(2*n//30)+f(2*n%30) for n in range(397,526)}
four=[(sum(comb(x-1,2) for x in t),sum(t)) for t in product(range(1,5),repeat=4)]
g={t:max(v for c,v in four if c<=t) for t in range(141)}
lmax={t:max(x for x in range(1,5) if comb(x-1,2)<=t) for t in range(141)}
assert [g[t] for t in range(5)]==[8,9,10,11,12]
jobs=[]
for source in old['jobs']:
 sid=source['spectrum_id']
 if sid not in ids:continue
 ds=source['degrees'];W=sum(comb(d,2) for d in ds)
 D2=sorted(ds)[-2];coef=(sum(sorted(ds)[-6:])-6)//2
 costs={};mult=Counter(ds)
 for n in range(397,526):
  rem=n;v=0
  for d,k in sorted(mult.items()):
   take=min(rem,k*comb(d,2));v+=d*take;rem-=take
  assert rem==0
  costs[n]=v
 count=0;survivors=[];maxv=-1;witness=None
 for tau in range(max(0,4*max(ds)-40),141):
  c3=min(12 if sid in cap12ids else 13,g[tau])
  for t in range((140+tau)//6+1):
   low=max(0,(397-W+280+2*tau-8*t+2)//3)
   high=min((525-W+280+2*tau-8*t)//3,(140+tau-6*t)//3,735-W+tau-3*t)
   c4=min(4*t,3*t+(D2-4)*(tau//3),2*t+(D2-3)*tau,lmax[tau]*t)
   for m in range(low,high+1):
    n1=W-280-2*tau+3*m+8*t
    n2=140+tau-3*m-6*t;n0=735-W+tau-m-3*t
    caps=(33*n0,35*n1-costs[n1],coef*n2,c3*m,c4)
    rem=box[n1];v=6864*n1
    for j,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
     x=min(caps[j],rem);v+=x*w;rem-=x
    count+=1
    z={'n':[n0,n1,n2,m,t],'tau':tau,'C3coef':c3,'caps':caps,'twice_L':v}
    if v>maxv:maxv=v;witness=z
    if v>=5445440:survivors.append(z)
  assert time.process_time()-start<20,'CPU limit; partial output not a proof'
 assert count==source['complete_domain']
 jobs.append({'id':sid,'degrees':ds,'complete_domain':count,'cap12_available':sid in cap12ids,
              'max_twice_L':maxv,'max_witness':witness,'survivors':survivors,
              'survivor_count':len(survivors),'strict':not survivors})
 print(sid,count,len(survivors),flush=True)
result={'status':'COMPLETE_CONDITIONAL_REFINED81','scope':__doc__,'hypotheses':['exact21/35/paircover/minpoint7','e<=4','actualGamma min4','alllambda<=4','generic cap13 and explicit cap12 caller imports'],
        'new_analytic_lemma':'PROOF.md','g4_values':[g[t] for t in range(13)],
        'spectra':len(jobs),'strict':sum(j['strict'] for j in jobs),
        'survivor_count':sum(j['survivor_count'] for j in jobs),'all_survivors_saved':True,
        'jobs':jobs,'cpu_seconds':time.process_time()-start}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('RESULT',result['spectra'],result['strict'],result['survivor_count'],result['cpu_seconds'])
