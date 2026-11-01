"""Refine ALL saved 126 survivors of the complete81 moment run.
Other keys retain their previously strict (weaker) bound. No new layouts.
"""
from pathlib import Path
from math import comb
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
old=json.loads((P/'RESULT.json').read_text())
tab=json.loads((P/'HIGH_ROW_CHECK.json').read_text())
assert old['all_survivors_saved'] and old['survivor_count']==126
assert tab['status']=='PASS'
G={r['D']:r['G_D_tau0_through140'] for r in tab['tables']}
def h19(S):
 if not 19<=S<=76:return 10**9
 if S<=38:return 0
 if S<=57:return S-38
 return 19+2*(S-57)
def f(s):
 a,r=divmod(s,5)
 return (s*s-r*(a+1)**2-(5-r)*a*a)//2
jobs=[];total=0
for j in old['jobs']:
 ds=sorted(j['degrees']);D,D2=ds[-1],ds[-2];r=max(0,4*D-40)
 rowunion=min(comb(l-1,2)+h19(4*D-l)+h19(4*D2-l) for l in range(1,5))
 closed=[];survivors=[]
 for oldkey in j['survivors']:
  total+=1;z=dict(oldkey);tau=z['tau'];n=z['n'];t=n[4];m=n[3];n1=n[1]
  if tau<rowunion:
   closed.append({**z,'closure':'two_actual_high_rows','tau_required':rowunion});continue
  a4max=min(tau//3,tau-r)
  assert a4max>=0
  caps=list(z['caps'])
  caps[3]=min(caps[3],G[D][tau]*m)
  caps[4]=min(caps[4],3*t+(D2-4)*a4max)
  remaining=360*(2*n1//30)+f(2*n1%30);v=6864*n1
  for i,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
   take=min(remaining,caps[i]);remaining-=take;v+=w*take
  z.update(new_caps=caps,new_twice_L=v,high_row_C3=G[D][tau],a4_max=a4max,two_row_tau_lower=rowunion)
  assert v<=oldkey['twice_L']
  if v<5445440:closed.append({**z,'closure':'strict_improved_capacity'})
  else:survivors.append(z)
 jobs.append({'id':j['id'],'degrees':j['degrees'],'old_complete_domain':j['complete_domain'],
              'old_survivor_count':j['survivor_count'],'closed':closed,'survivors':survivors,
              'strict':not survivors})
assert total==126
out={'status':'COMPLETE_ALL126_SURVIVOR_REFINEMENT','scope':__doc__,
     'source81_full_domain':'RESULT.json','high_row_tables':'HIGH_ROW_CHECK.json',
     'root_full_source_already_strict_keys_not_rerun':True,
     'stronger_C4_lemma':'a4<=tau-max(0,4Delta-40)',
     'strict_spectrum_count':sum(j['strict'] for j in jobs),
     'survivors':sum(len(j['survivors']) for j in jobs),'jobs':jobs,'cpu_seconds':time.process_time()-start}
(P/'HIGH_ROW_FILTER_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['strict_spectrum_count'],out['survivors'],out['cpu_seconds'])
for j in jobs:
 if not j['strict']:print(j['id'],len(j['survivors']),j['survivors'][0])
