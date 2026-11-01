#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as F
import json,subprocess,time,resource
P=Path(__file__).resolve().parent
start=time.process_time();children0=resource.getrusage(resource.RUSAGE_CHILDREN)
source=P.parent/'a1_chordal_triangle_repair_20261020/CAPACITY_FILTER.json'
j=json.loads(source.read_text());assert len(j['survivors'])==25
old=json.loads((P.parent/'a1_middle_wedge_capacity_20261020/GRAPH_PILOT.json').read_text())
es=sorted({(595-r['n'][1],r['n'][4]) for r in j['survivors']})
records={}
for mode in (0,):
 for e,t in es:
  r=json.loads(subprocess.check_output(['/tmp/a1_degree_prefix_dp',str(e),str(mode),'3',str(t)],text=True))
  q=r['q'];assert q[0]<=e-60+2*t and q[12]<=e-61+2*t;assert len(q)==35 and q==sorted(q,reverse=True) and sum(q)==2*e
  assert q.count(0)<=3 and q[1]<=29 and (not mode or q[0]<=29)
  def lower(N):
   return max(0,N-21,(8*N*(N-21)-105*t+83)//84,(8*N*(N-21)+188)//189,(152*N*(N-21)-2037*t+1427)//1428)
  assert all(sum(q[:i])<=e+i*(i-1)//2-lower(35-i) for i in range(1,36))
  def f(s):
   a,b=divmod(s,5);return (s*s-(5-b)*a*a-b*(a+1)*(a+1))//2
  assert sum(f(34-v) for v in q)==r['bound']
  records[(mode,e,t)]=r
profiles=[]
for r in j['survivors']:
 n=r['n'];e=595-n[1];modes=[]
 for mode in (0,):
  D=records[mode,e,n[4]]['bound'];T=F(old['threshold_Pmax'][str(n[1])]);linear=F(132*n[1]+198,5)
  bound=F(min(D,T,linear));remaining=bound;C=[F(0)]*5
  caps=[33*n[0],26*n[1]+339,24*n[2],13*n[3],4*n[4]]
  for a in range(4,-1,-1):C[a]=min(remaining,caps[a]);remaining-=C[a]
  L=sum(v*w for v,w in zip(C,(36,120,330,792,1716)))/2+3432*n[1]
  modes.append(dict(mode=mode,DP_bound=D,P_bound=str(bound),previous_P_bound=r['P_bound'],C=list(map(str,C)),L=str(L),survives=L>=2722720))
 profiles.append(dict(n=n,tau=r['tau'],e=e,modes=modes))
children=resource.getrusage(resource.RUSAGE_CHILDREN)
result=dict(scope='degree-sequence relaxation only, not graph or H existence',domain='25 frozen previous scalar survivors; all actual (e,n4) keys; exact DP with all35 centered plus principal-trace/independent-set prefix inequalities, nonincrease, sum2e, isolates<=3',
mode0='accepted T33 critical-core q2<=29 import',strong_prefix='centered principal Gram bound 1428 e(S)+2037 n4(S)>=152N(N-21), using each exact original n4 and q1<=E-60+2t,q13<=E-61+2t; q2<=29 only, no T34 conditional dependency',
records=[records[k] for k in sorted(records)],profiles=profiles,
remaining={str(mode):sum(r['modes'][mode]['survives'] for r in profiles) for mode in (0,)},
cpu_seconds=time.process_time()-start+children.ru_utime+children.ru_stime-children0.ru_utime-children0.ru_stime)
P.joinpath('DEGREE_CUT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('records','profiles')},indent=2))
print([(r['e'],r['n4_cap'],r['allcritical'],r['bound']) for r in result['records']])
print('survivors',[(r['n'],r['tau'],[m['L'] for m in r['modes']]) for r in profiles if any(m['survives'] for m in r['modes'])])
