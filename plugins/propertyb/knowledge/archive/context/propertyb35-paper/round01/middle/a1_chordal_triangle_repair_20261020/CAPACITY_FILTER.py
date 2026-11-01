#!/usr/bin/env python3
"""Exact scalar filtration only, using frozen threshold-majorant values."""
from pathlib import Path
from fractions import Fraction as F
import json,time
P=Path(__file__).resolve().parent
st=time.process_time()
old=json.loads((P.parent/'a1_middle_wedge_capacity_20261020/GRAPH_PILOT.json').read_text())
vals={int(k):v for k,v in old['threshold_Pmax'].items()}
assert set(vals)==set(range(397,547))
rows=[];counts={'moment_profiles':0,'old594_survivors':0,'new198_survivors':0}; changes=[]
for tau in range(141):
 for n4 in range(9):
  for n3 in range(max(0,(140+tau-6*n4)//3+1)):
   n=[87+tau-n3-3*n4,368-2*tau+3*n3+8*n4,140+tau-3*n3-6*n4,n3,n4]
   if min(n)<0 or not 397<=n[1]<=546:continue
   counts['moment_profiles']+=1
   outcomes=[]
   for constant in (594,198):
    threshold=F(vals[n[1]]); linear=F(132*n[1]+constant,5)
    bound=min(threshold,linear); remaining=bound
    caps=[33*n[0],26*n[1]+339,24*n[2],13*n[3],4*n[4]]
    C=[F(0)]*5
    for j in range(4,-1,-1):
     C[j]=min(remaining,caps[j]);remaining-=C[j]
    L=sum(v*w for v,w in zip(C,(36,120,330,792,1716)))/2+3432*n[1]
    row=dict(n=n,tau=tau,P_bound=str(bound),threshold=str(threshold),linear=str(linear),C=list(map(str,C)),L=str(L),survives=L>=2722720)
    outcomes.append(row)
   if outcomes[0]['survives']:counts['old594_survivors']+=1
   if outcomes[1]['survives']:
    counts['new198_survivors']+=1;rows.append(outcomes[1])
   if outcomes[0]['survives'] and not outcomes[1]['survives']:changes.append(dict(old=outcomes[0],new=outcomes[1]))
assert counts['new198_survivors']<=counts['old594_survivors']
result=dict(scope='complete integer moment relaxation; C3<=13*n3, conditional original n4<=8, threshold bound frozen from earlier independent recurrence; not H realization',
imports='N34<=3 and n4<=8 supplied/root checked; no new cross-family review asserted',counts=counts,removed=changes,survivors=rows,
minimum_high_pairs=min((r['n'][3]+r['n'][4] for r in rows),default=None),minimum_n3=min((r['n'][3] for r in rows),default=None),maximum_tau=max((r['tau'] for r in rows),default=None),
minimum_high_witness=min(rows,key=lambda r:(r['n'][3]+r['n'][4],r['tau'])) if rows else None,cpu_seconds=time.process_time()-st)
P.joinpath('CAPACITY_FILTER.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('survivors','removed')},indent=2))
