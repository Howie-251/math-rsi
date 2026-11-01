"""Re-filter frozen35083 survivors with singleton-degree cap31; no new DP or H domain."""
from pathlib import Path
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();original=json.loads((P/'RESULT.json').read_text());rows=json.loads((P/'SURVIVORS.json').read_text());assert len(rows)==35083

def f(s):
 a,b=divmod(s,5)
 return (s*s-(5-b)*a*a-b*(a+1)**2)//2
assert f(31)==384
survivors=[];sum_excluded=0
for old in rows:
 n1=old['n'][1];total=2*n1
 if total>35*31:sum_excluded+=1;continue
 a,b=divmod(total,31);assert a+(b>0)<=35
 closed=a*f(31)+f(b);Pbound=min(old['P'],closed)
 rem=Pbound;C=[0]*5
 for j in range(4,-1,-1):C[j]=min(rem,old['C_caps'][j]);rem-=C[j]
 L2=sum(x*w for x,w in zip(C,(36,120,330,792,1716)))+6864*n1
 if L2>=5445440:survivors.append({**old,'old_P':old['P'],'closed_form_P':closed,'P':Pbound,'C':C,'twice_L':L2,'margin':(L2-5445440)//2})
assert len({(s['unique_degree_key'],tuple(s['n']),s['tau']) for s in survivors})==len(survivors)

def summarize(rr):
 out={'survivors':len(rr),'distinct_moment_keys':len({(tuple(z['n']),z['tau']) for z in rr})}
 if rr:
  out.update({'n4_range':[min(z['n'][4] for z in rr),max(z['n'][4] for z in rr)],'tau_range':[min(z['tau'] for z in rr),max(z['tau'] for z in rr)],'n1_range':[min(z['n'][1] for z in rr),max(z['n'][1] for z in rr)],'closest_witness':min(rr,key=lambda z:(z['margin'],z['tau'],z['n'][4])),'minimum_high_witness':min(rr,key=lambda z:(z['n'][3]+z['n'][4],z['tau'],z['n'][4]))})
 return out
modes=[]
for tcap in (None,25,13):
 selected=[r for r in survivors if tcap is None or r['n'][4]<=tcap]
 jobs=[]
 for oldjob in original['jobs']:
  k=oldjob['unique_degree_key'];rr=[z for z in selected if z['unique_degree_key']==k]
  jobs.append({'unique_degree_key':k,'a':oldjob['a'],'b':oldjob['b'],'partition':oldjob['partition'],'W':oldjob['W'],'e':oldjob['e'],**summarize(rr)})
 mode={'n4_cap':tcap,'import_scope':('minGamma3 only' if tcap is None else ('plus separately supplied generic deleted-star n4<=25 import' if tcap==25 else 'plus CONDITIONAL n4<=13, dependent on actual mixed four-core gate')),'jobs':jobs,**summarize(selected)}
 modes.append(mode)
 print('MODE',tcap,mode['survivors'],mode['distinct_moment_keys'],mode.get('n4_range'),mode.get('tau_range'),'closest',mode.get('closest_witness',{}).get('margin'),flush=True)
 for j in jobs:print(' ',j['a'],j['b'],j['partition'],j['survivors'],j.get('closest_witness',{}).get('margin'))
result={'scope':__doc__,'f31':f(31),'source_survivors':len(rows),'rejected_by_singleton_sum_cap':sum_excluded,'modes':modes,'cpu_seconds':time.process_time()-st}
(P/'RESIEVE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(P/'RESIEVE_SURVIVORS.json').write_text(json.dumps(survivors,indent=2)+'\n')
print('CPU',result['cpu_seconds'])
