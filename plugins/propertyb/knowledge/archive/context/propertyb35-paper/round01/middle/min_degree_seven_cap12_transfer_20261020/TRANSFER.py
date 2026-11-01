"""Exact cap12 caller projection and complete scalar rerun only for newly covered old-nonstrict spectra."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from math import comb
import json,time,argparse
P=Path(__file__).resolve().parent;B=P.parent;st=time.process_time();ap=argparse.ArgumentParser();ap.add_argument('--profile',action='store_true');arg=ap.parse_args()
old=json.loads((B/'min_degree_seven_gamma_four_low_excess_diagnostic_20261020/RESULT.json').read_text());pairs=json.loads((B/'min_degree_seven_low_excess_strong_pairs_20261020/RESULT.json').read_text());ok=set(pairs['nonB_all_lambda_le4_spectrum_ids'])
known={tuple(q['quad']) for q in json.loads((B/'c13_remaining_actual_quads_20261020/ALL_RESULT.json').read_text())['quad_support']}
assert json.loads((P/'QUAD8888_RESULT.json').read_text())['nonstrict']==[]
projection=[]
for j in old['jobs']:
 if j['spectrum_id'] not in ok:continue
 qs=sorted(set(combinations(j['degrees'],4)));covered=[];missing=[]
 for q in qs:
  reason=''
  if q in known:reason='existing32-selected-quad-classification'
  elif q.count(7)>=3:reason='same-side-seven-pair-empty'
  elif q==(8,8,8,8):reason='new-single-quad-8888'
  elif q==(9,10,10,10) and j['a7']>=5:reason='existing-seven-pool-at-least5'
  elif q==(10,10,10,10) and j['a7']==9 and j['a8']==0:reason='existing-S2-two-shared-column-orbits'
  if reason:covered.append({'quad':q,'reason':reason})
  else:missing.append(q)
 projection.append({'spectrum_id':j['spectrum_id'],'degrees':j['degrees'],'a7':j['a7'],'a8':j['a8'],'e':j['e'],'old_scalar_strict':j['all_strict'],'all_actual_selected_quads':qs,'covered':covered,'missing':missing,'cap12_ready':not missing})
(P/'PROJECTION.json').write_text(json.dumps(projection,indent=2)+'\n')
ids=[r['spectrum_id'] for r in projection if r['cap12_ready'] and not r['old_scalar_strict']]
print('PROJECTION',len(projection),'READY',sum(j['cap12_ready'] for j in projection),'NEW',ids,flush=True)
if arg.profile:ids=ids[:1]
def box(n):
 z=2*n;g,r=divmod(z,30);q,s=divmod(r,5)
 return 360*g+(r*r-s*(q+1)**2-(5-s)*q*q)//2
results=[]
for j in old['jobs']:
 if j['spectrum_id'] not in ids:continue
 ds=j['degrees'];W=sum(comb(d,2) for d in ds);coef=(sum(sorted(ds)[-6:])-6)//2;rowlo=max(0,4*(max(ds)-10));flags=Counter()
 for d in ds:flags[d]+=comb(d,2)
 costs={}
 for n1 in range(397,526):
  rem=n1;cost=0
  for d,num in sorted(flags.items()):take=min(rem,num);rem-=take;cost+=take*d
  assert not rem;costs[n1]=cost
 count=0;fails=[];maximum=-1;witness=None
 for tau in range(rowlo,141):
  for t in range((140+tau)//6+1):
   lo=max(0,(397-W+280+2*tau-8*t+2)//3);hi=min((525-W+280+2*tau-8*t)//3,(140+tau-6*t)//3,735-W+tau-3*t)
   for m in range(lo,hi+1):
    n1=W-280-2*tau+3*m+8*t;n2=140+tau-3*m-6*t;n0=735-W+tau-m-3*t;n=(n0,n1,n2,m,t);count+=1
    caps=[33*n0,35*n1-costs[n1],coef*n2,12*m,4*t];rem=box(n1);v=6864*n1;allocation=[0]*5
    for k,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
     take=min(caps[k],rem);rem-=take;allocation[k]=take;v+=w*take
    if v>maximum:maximum=v;witness={'n':n,'tau':tau,'P':box(n1),'caps':caps,'allocation':allocation,'twice_L':v}
    if v>=5445440:fails.append({'n':n,'tau':tau,'twice_L':v})
    if count%4096==0:assert time.process_time()-st<18
 assert count==j['complete_domain']
 results.append({'spectrum_id':j['spectrum_id'],'degrees':ds,'W':W,'S6':sum(sorted(ds)[-6:]),'row_tau_lower':rowlo,'complete_domain':count,'all_strict':not fails,'survivors':fails,'maximum_twice_L':maximum,'margin':5445440-maximum,'maximum_witness':witness})
 print('SCALAR',j['spectrum_id'],'KEYS',count,'FAILS',len(fails),'MAX',maximum,'CPU',time.process_time()-st,flush=True)
out={'status':'PROFILE_ONE_COMPLETE_SPECTRUM' if arg.profile else 'COMPLETE_SELECTED_NEW_CAP12_SPECTRA','scope':__doc__,'explicit_conditions':['H21/M35/simple5/paircover/minimum degree exactly7','e=summax(d-9,0)<=4','all pointpair codegrees<=4 from strong-pair projection','Gamma minimum degree4 supplied by caller','C3<=12n3 proved for all actual selected quads by projection','same scalar caps and moment domain as source99, only C3 changed13 to12'],'excluded_unique_pair5_spectrum_ids':pairs['spectra_with_unexcluded_pairs'],'full_lambda4_spectrum_count':len(projection),'cap12_ready_ids':[r['spectrum_id'] for r in projection if r['cap12_ready']],'newly_tested_ids':ids,'jobs':results,'total_domain':sum(r['complete_domain'] for r in results),'strict_spectra':sum(r['all_strict'] for r in results),'threshold_twice_L':5445440,'cpu_seconds':time.process_time()-st}
(P/('PROFILE.json' if arg.profile else 'RESULT.json')).write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],'STRICT',out['strict_spectra'],'TOTALCPU',out['cpu_seconds'])
