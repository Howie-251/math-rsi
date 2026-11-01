"""Independent frozen-domain scalar re-sieve check, without a graph-degree optimizer."""
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();old=json.loads((P/'SURVIVORS.json').read_text());saved=json.loads((P/'RESIEVE_SURVIVORS.json').read_text());report=json.loads((P/'RESIEVE_RESULT.json').read_text())
def f(s):
 q,r=divmod(s,5)
 return sum(x*y for i,x in enumerate([q+int(j<r) for j in range(5)]) for y in [q+int(j<r) for j in range(i+1,5)])
def key(z):return (z['unique_degree_key'],tuple(z['n']),z['tau'])
assert len(old)==35083 and len({key(z) for z in old})==35083
expected={};sum_excluded=0
for z in old:
 mass=2*z['n'][1]
 if mass>1085:sum_excluded+=1;continue
 # Construct an extremal35-slot list by repeated saturation instead of divmod.
 slots=[];left=mass
 for _ in range(35):s=min(left,31);slots.append(s);left-=s
 assert left==0 and sum(slots)==mass
 closed=sum(f(s) for s in slots);budget=min(closed,z['P']);remaining=budget;chosen=[0]*5
 for j in (4,3,2,1,0):chosen[j]=min(remaining,z['C_caps'][j]);remaining-=chosen[j]
 L2=sum(w*c for w,c in zip((36,120,330,792,1716),chosen))+6864*z['n'][1]
 if L2>=5445440:expected[key(z)]=(closed,budget,chosen,L2)
assert len(saved)==len(expected)==20995 and {key(z) for z in saved}==set(expected)
for z in saved:
 closed,budget,chosen,L2=expected[key(z)]
 assert (z['closed_form_P'],z['P'],z['C'],z['twice_L'])==(closed,budget,chosen,L2)
for mode in report['modes']:
 rr=[z for z in saved if mode['n4_cap'] is None or z['n'][4]<=mode['n4_cap']]
 assert len(rr)==mode['survivors']
 assert len({(tuple(z['n']),z['tau']) for z in rr})==mode['distinct_moment_keys']
 assert min(z['margin'] for z in rr)==mode['closest_witness']['margin']==2
 for j in mode['jobs']:
  q=[z for z in rr if z['unique_degree_key']==j['unique_degree_key']]
  assert len(q)==j['survivors'] and min(z['margin'] for z in q)==j['closest_witness']['margin']
assert sum_excluded==report['rejected_by_singleton_sum_cap']==1990
out={'status':'PASS','f_values_checked':{str(s):f(s) for s in (0,11,31)},'frozen_source_keys':len(old),'rejected_by_sum_cap':sum_excluded,'same_full_survivor_keys':True,'modes':[{'n4_cap':m['n4_cap'],'survivors':m['survivors'],'distinct_moment_keys':m['distinct_moment_keys'],'minimum_margin':m['closest_witness']['margin']} for m in report['modes']],'cpu_seconds':time.process_time()-st}
(P/'RESIEVE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
