"""Independent35-slot [5,31] scalar re-sieve, complete frozen-key comparison."""
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();old=[z for z in json.loads((P/'RESIEVE_SURVIVORS.json').read_text()) if z['n'][4]<=13];new=json.loads((P/'CONDITIONAL_CRITICAL_SURVIVORS.json').read_text());summary=json.loads((P/'CONDITIONAL_CRITICAL_RESIEVE_RESULT.json').read_text())
def f(s):
 q,r=divmod(s,5);g=[q+int(i<r) for i in range(5)]
 return sum(g[i]*g[j] for i in range(5) for j in range(i+1,5))
def key(z):return(z['unique_degree_key'],tuple(z['n']),z['tau'])
expected={}
for z in old:
 mass=2*z['n'][1]
 if not 175<=mass<=1085:continue
 slots=[5]*35;left=mass-175
 for i in range(35):take=min(left,26);slots[i]+=take;left-=take
 assert left==0 and sum(slots)==mass and min(slots)>=5 and max(slots)<=31
 cap=sum(f(s) for s in slots);budget=min(z['P'],cap);rem=budget;C=[0]*5
 for j in (4,3,2,1,0):C[j]=min(rem,z['C_caps'][j]);rem-=C[j]
 L2=sum(w*c for w,c in zip((36,120,330,792,1716),C))+6864*z['n'][1]
 if L2>=5445440:expected[key(z)]=(cap,budget,C,L2)
assert len(old)==6953 and len(expected)==len(new)==5813 and set(expected)=={key(z) for z in new}
for z in new:assert expected[key(z)]==(z['critical_box_P'],z['P'],z['C'],z['twice_L'])
assert summary['survivors']==5813 and summary['distinct_moment_keys']==len({(tuple(z['n']),z['tau']) for z in new})==4032
for j in summary['jobs']:
 rr=[z for z in new if z['unique_degree_key']==j['unique_degree_key']]
 assert len(rr)==j['survivors'] and min(z['margin'] for z in rr)==j['closest_witness']['margin']
assert min(z['margin'] for z in new)==8
# Exact former closest source, now rejected.
mass=2*517;a,b=divmod(mass-175,26);cap=a*f(31)+f(5+b)+(34-a)*f(5);assert cap==12696
Lnew=2722722-(12720-cap)*60;assert Lnew==2721282<2722720
out={'status':'PASS','scope':__doc__,'source_keys':len(old),'same_all_survivor_keys':True,'survivors':len(new),'distinct_moment_keys':4032,'minimum_margin':8,'all16_spectra_still_nonempty':all(z['survivors']>0 for z in summary['jobs']),'former_closest_new_P':cap,'former_closest_new_L':Lnew,'cpu_seconds':time.process_time()-st}
(P/'CONDITIONAL_CRITICAL_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
