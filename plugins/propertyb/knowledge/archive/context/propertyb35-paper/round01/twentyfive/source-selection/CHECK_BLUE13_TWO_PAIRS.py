"""Three scalar rows for r8 minimum-blue13, plus the low-owner bound.
No H, source-coloring or negative-layout enumeration.
"""
from pathlib import Path
import json,time
D=Path(__file__).resolve().parent;t0=time.process_time()
rows=[]
for delta in range(6,8):
 for u in range(4):
  for c in range(4):
   if delta+2*u+c>7:continue
   t=9-delta-3*u-c
   assert t>=0 and u==0
   nonlow_sink_min_cross=5-t
   assert nonlow_sink_min_cross>2*c
   red_low_upper=8-13+delta  # e_B>=0; equality only e_B=0.
   red_low_lower=1+c+2     # at least one low in G, and >=1+c+ell low sinks.
   assert red_low_lower>red_low_upper
   rows.append(dict(delta=delta,u=u,c=c,N=[13,t,10+c-t,11-c],
                    nonlow_sink_min_cross=nonlow_sink_min_cross,total_cross_excess=2*c,
                    red_low_upper=red_low_upper,red_low_lower=red_low_lower))
assert len(rows)==3
# Scalar identity behind the general owner lemma; ell is |G intersect low|.
owner_rows=[]
for u in range(4):
 for c in range(4):
  for ell in range(1,6):
   N4=11-u-c
   sinks_min=1+u+c+ell
   assert N4==12-sinks_min+ell
   owner_rows.append(dict(u=u,c=c,ell=ell,N4=N4,sinks_min=sinks_min))
out=dict(status='PASS',scope=__doc__,r8_rows=rows,
         general_owner_scalar_rows=len(owner_rows),
         conclusion='r8 cannot have global minimum blue13; combined with earlier r<=7, r<=8 has b<=12',
         cpu_seconds=time.process_time()-t0)
(D/'CHECK_BLUE13_TWO_PAIRS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
