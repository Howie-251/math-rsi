"""Complete seven scalar rows for r9 minimum blue13 and the final sink row.
No H, source-coloring or negative-layout enumeration.
"""
import json,time
from pathlib import Path
D=Path(__file__).resolve().parent;t0=time.process_time();rows=[];tails=[]
for delta in range(5,8):
 for u in range(2):
  for c in range(3):
   if delta+2*u+c>7:continue
   t=9-delta-3*u-c
   if t<0:continue
   red_low_upper=9-13+delta
   low_sink_upper=red_low_upper-1
   sink_min=2+u+c
   high_sink_min=max(0,sink_min-low_sink_upper)
   if u==0:high_kappa_min=5-t
   else:
    assert (delta,u,c,t)==(5,1,0,1)
    for bh in range(2):
     for a in range(35):
      if max(0,a-2)**2<=2*(1-bh):assert a<=3-bh
    high_kappa_min=2
   forced_cross=high_sink_min*high_kappa_min
   row=dict(delta=delta,u=u,c=c,N=[13+u,t,10+c-t,11-u-c],
            red_low_upper=red_low_upper,sink_min=sink_min,
            high_sink_min=high_sink_min,high_kappa_min=high_kappa_min,
            forced_cross=forced_cross,total_cross=2*c,
            scalar_excluded=forced_cross>2*c)
   rows.append(row)
   if not row['scalar_excluded']:tails.append((delta,u,c,t))
assert len(rows)==7 and tails==[(7,0,0,2)]
shape=[]
for a in range(7):
 for bh in range(3):
  if 2*a+bh==5 and a*(a-1)<=2*(2-bh):shape.append((a,bh,6-a-bh))
assert shape==[(2,1,3)]
# The same-source swap of a degree-six sink with a degree-(6+s) private neighbor.
cut_rows=[]
for s in range(20):
 delta_new=7-s;c_new=2*s
 permitted=delta_new+c_new<=7
 assert permitted==(s==0)
 cut_rows.append(dict(s=s,delta_new=delta_new,c_new=c_new,permitted=permitted))
out=dict(status='PASS',scope=__doc__,scalar_rows=rows,
         remaining_scalar=tails[0],low_sink_shape=shape[0],swap_degree_rows=cut_rows,
         conclusion='Final scalar is excluded by the indexed two-sink owner exchange in BLUE13_R9_OWNER_EXCHANGE.md',
         cpu_seconds=time.process_time()-t0)
(D/'CHECK_BLUE13_R9.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='swap_degree_rows'},indent=2))
