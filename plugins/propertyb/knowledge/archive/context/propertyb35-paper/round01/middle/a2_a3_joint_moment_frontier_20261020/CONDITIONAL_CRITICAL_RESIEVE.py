"""CONDITIONAL critical import s_F>=5, on frozen t<=13 re-sieve domain only."""
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();rows=[z for z in json.loads((P/'RESIEVE_SURVIVORS.json').read_text()) if z['n'][4]<=13];assert len(rows)==6953
jobs=json.loads((P/'RESULT.json').read_text())['jobs']
def f(s):
 q,b=divmod(s,5)
 return (s*s-(5-b)*q*q-b*(q+1)**2)//2
assert (f(5),f(6),f(31))==(10,14,384)
result=[];infeasible=0
for old in rows:
 mass=2*old['n'][1]
 if not 175<=mass<=1085:infeasible+=1;continue
 v=mass-175;a,b=divmod(v,26)
 assert 0<=a<=35 and (a<35 or b==0)
 critical=a*f(31)+(f(5+b)+(34-a)*f(5) if a<35 else 0)
 budget=min(old['P'],critical);C=[0]*5;rem=budget
 for j in range(4,-1,-1):C[j]=min(rem,old['C_caps'][j]);rem-=C[j]
 L2=sum(c*w for c,w in zip(C,(36,120,330,792,1716)))+6864*old['n'][1]
 if L2>=5445440:result.append({**old,'old_cap31_P':old['P'],'critical_box_P':critical,'P':budget,'C':C,'twice_L':L2,'margin':(L2-5445440)//2})
def summarize(rr):
 out={'survivors':len(rr),'distinct_moment_keys':len({(tuple(r['n']),r['tau']) for r in rr})}
 if rr:out.update({'n4_range':[min(r['n'][4] for r in rr),max(r['n'][4] for r in rr)],'tau_range':[min(r['tau'] for r in rr),max(r['tau'] for r in rr)],'n1_range':[min(r['n'][1] for r in rr),max(r['n'][1] for r in rr)],'closest_witness':min(rr,key=lambda r:(r['margin'],r['tau'],r['n'][4])),'minimum_high_witness':min(rr,key=lambda r:(r['n'][3]+r['n'][4],r['tau'],r['n'][4]))})
 return out
byjob=[]
for job in jobs:
 key=job['unique_degree_key'];rr=[r for r in result if r['unique_degree_key']==key]
 byjob.append({'unique_degree_key':key,'a':job['a'],'b':job['b'],'partition':job['partition'],'W':job['W'],'e':job['e'],**summarize(rr)})
out={'scope':__doc__,'import_not_established_here':'n4<=13 paper candidate plus old<=34/low-degree local import forcing35-edge H edge-critical and singleton graph degree>=5','source_keys':len(rows),'box_infeasible_keys':infeasible,'jobs':byjob,**summarize(result),'cpu_seconds':time.process_time()-st}
(P/'CONDITIONAL_CRITICAL_RESIEVE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');(P/'CONDITIONAL_CRITICAL_SURVIVORS.json').write_text(json.dumps(result,indent=2)+'\n')
print('SUMMARY',out['survivors'],out['distinct_moment_keys'],out.get('n4_range'),out.get('tau_range'),out.get('closest_witness'),out['cpu_seconds'])
for j in byjob:print(j['a'],j['b'],j['partition'],j['survivors'],j.get('closest_witness',{}).get('margin'))
