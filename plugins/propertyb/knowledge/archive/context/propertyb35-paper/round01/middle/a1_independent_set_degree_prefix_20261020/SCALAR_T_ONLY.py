#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as F
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
values=json.loads((P.parent/'a1_middle_wedge_capacity_20261020/GRAPH_PILOT.json').read_text())['threshold_Pmax']
existing=json.loads((P.parent/'a1_chordal_triangle_repair_20261020/CAPACITY_FILTER.json').read_text())['survivors']
expected={(tuple(r['n']),r['tau']) for r in existing};survivors=[];count=0
for tau in range(141):
 for t in range(9):
  for n3 in range(max(0,(140+tau-6*t)//3+1)):
   n=[87+tau-n3-3*t,368-2*tau+3*n3+8*t,140+tau-3*n3-6*t,n3,t]
   if min(n)<0 or not 397<=n[1]<=546:continue
   count+=1;rem=F(values[str(n[1])]);C=[F(0)]*5
   for a,cap in reversed(list(enumerate((33*n[0],26*n[1]+339,24*n[2],13*n[3],4*n[4])))):
    C[a]=min(cap,rem);rem-=C[a]
   L=sum(c*w for c,w in zip(C,(36,120,330,792,1716)))/2+3432*n[1]
   if L>=2722720:survivors.append(dict(n=n,tau=tau,P_bound=values[str(n[1])],C=list(map(str,C)),L=str(L)))
keys={(tuple(r['n']),r['tau']) for r in survivors}
result=dict(scope='complete original moment relaxation using threshold T only, no linear P upper bound',moment_profiles=count,survivor_count=len(survivors),same_frozen25=keys==expected,extra_keys=[dict(n=list(n),tau=tau) for n,tau in sorted(keys-expected)],missing_keys=[dict(n=list(n),tau=tau) for n,tau in sorted(expected-keys)],survivors=survivors,cpu_seconds=time.process_time()-start)
P.joinpath('SCALAR_T_ONLY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='survivors'}))
