#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as F
import json,subprocess,time,resource
P=Path(__file__).resolve().parent
start=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
j=json.loads(P.joinpath('SIMPLE_CHAIN_RESULT.json').read_text());verified=[]
frozen=json.loads((P.parent/'a1_chordal_triangle_repair_20261020/CAPACITY_FILTER.json').read_text())
assert len(j['profiles'])==25 and {(tuple(r['n']),r['tau']) for r in j['profiles']}=={(tuple(r['n']),r['tau']) for r in frozen['survivors']}
assert len(j['records'])==19 and {(r['e'],r['n4_cap']) for r in j['records']}=={(595-r['n'][1],r['n'][4]) for r in frozen['survivors']}
# Independently recover the full old-moment relaxation and the frozen25 keys.
old=json.loads((P.parent/'a1_middle_wedge_capacity_20261020/GRAPH_PILOT.json').read_text())
complete=[];moment_count=0
for tau in range(141):
 for t in range(9):
  for n3 in range(max(0,(140+tau-6*t)//3+1)):
   n=[87+tau-n3-3*t,368-2*tau+3*n3+8*t,140+tau-3*n3-6*t,n3,t]
   if min(n)<0 or not 397<=n[1]<=546:continue
   moment_count+=1
   rem=F(old['threshold_Pmax'][str(n[1])]);cs=[F(0)]*5
   capacities=[33*n[0],26*n[1]+339,24*n[2],13*n[3],4*n[4]]
   for a in reversed(range(5)):cs[a]=min(capacities[a],rem);rem-=cs[a]
   L=sum(c*w for c,w in zip(cs,(36,120,330,792,1716)))/2+3432*n[1]
   if L>=2722720:complete.append((tuple(n),tau))
assert moment_count==21615 and len(complete)==25
assert set(complete)=={(tuple(r['n']),r['tau']) for r in j['profiles']}
for r in j['records']:
 v=json.loads(subprocess.check_output(['/tmp/a1_simple_chain_frequency',str(r['e']),str(r['n4_cap'])],text=True))
 assert v['bound']==r['bound'],(r,v)
 q=r['q'];assert q==sorted(q,reverse=True) and sum(q)==2*r['e'] and q.count(0)<=3 and min(q)>=2
 assert q[0]+q.count(1)+q.count(0)<=50 and q[0]+q[1]<=r['e']-49+2*r['n4_cap']
 verified.append(v)
for p in j['profiles']:
 n=p['n'];r=p['modes'][0];rem=F(r['P_bound']);C=[F(0)]*5
 assert rem==min(F(r['DP_bound']),F(old['threshold_Pmax'][str(n[1])]))

 for a,cap in reversed(list(enumerate((33*n[0],26*n[1]+339,24*n[2],13*n[3],4*n[4])))):
  C[a]=min(cap,rem);rem-=C[a]
 L=sum(c*w for c,w in zip(C,(36,120,330,792,1716)))/2+3432*n[1]
 assert list(map(str,C))==r['C'] and str(L)==r['L'] and (L>=2722720)==r['survives']
remaining=[r for r in j['profiles'] if r['modes'][0]['survives']]
assert len(remaining)==1 and remaining[0]['n']==[33,523,0,31,8] and remaining[0]['tau']==1
assert j['after_actual_quad_tau_coupling']==0
# Applies the separately proved actual-H coupling, not a degree-sequence theorem.
assert remaining[0]['n'][4]==8 and remaining[0]['tau']<3
c=resource.getrusage(resource.RUSAGE_CHILDREN)
out=dict(status='PASS',moment_domain_profiles=moment_count,frozen_profiles=len(complete),after_degree_DP=1,after_actual_quad_tau_coupling=0,scope='independent degree-frequency DP versus fixed-maximum layer DP with direct-color allq>=2 gate, all19(e,n4), all25 rational allocations; original25 key completeness independently checked',records=verified,cpu_seconds=time.process_time()-start+c.ru_utime+c.ru_stime-c0.ru_utime-c0.ru_stime)
P.joinpath('SIMPLE_CHAIN_VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'}))
