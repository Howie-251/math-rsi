from pathlib import Path
from fractions import Fraction as F
import json,time
P=Path(__file__).resolve().parent
j=json.loads((P.parent/'a1_middle_wedge_capacity_20261020/GRAPH_PILOT.json').read_text());assert j['C3_multiplier']==15 and j['conditional_n4_upper']==11
st=time.process_time();out=[]
for k in range(15,-1,-1):
 surv=[]
 for q in j['survivors']:
  n=q['n'];p=F(q['P_bound']);U=[33*n[0],26*n[1]+339,24*n[2],k*n[3],4*n[4]];C=[F(0)]*5
  for a in range(4,-1,-1):C[a]=min(p,U[a]);p-=C[a]
  L=sum(v*w for v,w in zip(C,(36,120,330,792,1716)))/2+3432*n[1]
  if L>=2722720:surv.append({'n':n,'tau':q['tau'],'P_bound':q['P_bound'],'C':[str(v) for v in C],'L':str(L)})
 if k==13:
  extra={'scope':'same complete cheap relaxation with actual near-saturation cap13, not H realization','survivors':surv,'count':len(surv),'minimum_high_pairs':min(q['n'][3]+q['n'][4] for q in surv),'minimum_n3':min(q['n'][3] for q in surv),'minimum_high_witness':min(surv,key=lambda q:(q['n'][3]+q['n'][4],q['tau']))}
  (P/'RESIDUAL_CAP13.json').write_text(json.dumps(extra,indent=2)+'\n')
 out.append({'hypothetical_C3_cap':k,'survivors':len(surv),'first_survivor':surv[0] if surv else None})
result={'scope':'hypothetical-cap diagnostic only; complete by monotonic filtering of all219 prior15-cap survivors','n4_cap':11,'results':out,'cpu_seconds':time.process_time()-st}
(P/'TARGET.json').write_text(json.dumps(result,indent=2)+'\n');print([(q['hypothetical_C3_cap'],q['survivors']) for q in out])
