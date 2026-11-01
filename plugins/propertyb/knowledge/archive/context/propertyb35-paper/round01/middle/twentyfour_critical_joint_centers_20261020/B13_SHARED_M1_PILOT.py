#!/usr/bin/env python3
"""Tiny necessary integer-state pilot for global-minimum-b13 low actualG; no H, layout, or LP search."""
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;start=time.process_time();jobs=[]
for eps in [0,1]:
 for e in range(3):
  for N2 in range(3):
   N3=6-e-2*N2;N4=21-N2-N3;w=2*(N2+N3)-7
   if N3<0 or N2+N3<4 or 7-e-eps<0:continue
   # Blue private edges are unique, and source centers with exactly oneN4 cannot lose>N2 private owners.
   degree_excess=[0]*4+[eps];families=[]
   for t in degree_excess:
    rows=[]
    for a in range(7+t):
     for b in range(min(6+t,N2)+1):
      for c in range(min(6+t,N3)+1):
       m=6+t-a-b-c;k=a+2*b+3*c+4*m-13
       if not(1<=m<=N4 and 0<=k<=w):continue
       if m==1 and 2*a>N2:continue
       rows.append((a,b,c,m,k))
    families.append(rows)
   dp={(0,0,0,0,0):[]}
   for rows in families:
    nd={}
    for old,used in dp.items():
     for row in rows:
      key=tuple(x+y for x,y in zip(old,row))
      if key[0]>52 or key[1]>3*N2 or key[2]>2*N3 or key[3]>N4 or key[4]>w:continue
      nd.setdefault(key,used+[row])
    dp=nd
   qlo=22-(4*(7-e-eps))//3
   feasible=[{'totals':k,'G_rows':v} for k,v in dp.items() if k[0]>=qlo]
   jobs.append({'G_excess':eps,'blue_excess':e,'N':[13,N2,N3,N4],'cross_excess':w,'G_private_occurrences_lower':qlo,'center_type_counts':list(map(len,families)),'necessary_states_after_no_good_m1_filter':len(feasible),'first_state':feasible[0] if feasible else None,'all_states':feasible})
assert time.process_time()-start<3
out={'status':'COMPLETE_TINY_NECESSARY_STATE_PILOT','scope':__doc__,'jobs':jobs,'cpu_seconds':time.process_time()-start}
(P/'B13_SHARED_M1_PILOT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'jobs':[{k:v for k,v in j.items() if k!='all_states'} for j in jobs]},indent=2))
