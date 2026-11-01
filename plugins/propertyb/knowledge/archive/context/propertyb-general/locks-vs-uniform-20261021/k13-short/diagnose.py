import json,time
from pathlib import Path
from layout_certified import LayoutCertificate,FixedCertificate,S,CEIL
OUT=Path(__file__).resolve().parent
start=time.process_time();wall=time.monotonic();rows=[]
# A fixed finite grid, centered at (floor(v/2), floor(v/2)+1).
gaps=(1,3,5,9,17,33,49,65,97,129)
shifts=(-16,-8,-4,0,4,8,16)
targets=[(9544,972,81,81),(9564,813,68,68),(9564,813,68,153),(9564,972,81,81),(9564,972,81,128),(9564,1050,88,88),(9564,1218,102,102)]
for m,v,d,e in targets:
 sd=2*(v-1)-12*d;B=max(d,(13*m-v*d)//sd+d) if sd>0 else None
 assert sd>0 and d<=e<=B
 a0=FixedCertificate(13,m).two(v,d,e)
 assert LayoutCertificate(13,m,(v//2,v//2+1)).two(v,d,e)==a0
 rr=[]
 for gap in gaps:
  for shift in shifts:
   if time.process_time()-start>155:break
   a=v//2+shift-gap//2;b=a+gap
   if a<1 or b>v:continue
   z=LayoutCertificate(13,m,(a,b)).two(v,d,e)
   rr.append({'positions':[a,b],'gap':gap,'shift':shift,'z':z,'margin':S-z})
  if time.process_time()-start>155:break
 best=min(rr,key=lambda r:r['z']);row={'M':m,'v':v,'d':d,'e':e,'d0':CEIL(v-1,12),'minimum_degree_upper':13*m//v,'s_d':sd,'B_d':B,'central_z':a0,'best':best,'layout_count':len(rr),'layouts':rr}
 rows.append(row);print('TWO',m,v,d,e,'central',a0,'best',best,'layouts',len(rr),'cpu',round(time.process_time()-start,3),flush=True)
 if time.process_time()-start>155:break
# One-lock placement does not require a codegree-one partner.
ones=[]
for m,v,d in [(9564,813,152),(9564,813,68),(9544,972,81),(9564,972,81)]:
 if time.process_time()-start>155:break
 rr=[]
 for shift in (-32,-16,-8,-4,-2,-1,0,1,2,4,8,16,32):
  pos=v//2+shift;z=LayoutCertificate(13,m,(pos,)).one(v,d);rr.append({'position':pos,'shift':shift,'z':z,'margin':S-z})
 row={'M':m,'v':v,'d':d,'central_z':next(r['z'] for r in rr if r['shift']==0),'best':min(rr,key=lambda r:r['z']),'layouts':rr};ones.append(row);print('ONE',row['M'],v,d,'best',row['best'],flush=True)
res={'k':13,'S':S,'two':rows,'one':ones,'cpu_seconds':time.process_time()-start,'wall_seconds':time.monotonic()-wall,'full_certificate':False,'grid_gaps':gaps,'grid_shifts':shifts,'complete_requested_grid':len(rows)==len(targets) and all(r['layout_count']==70 for r in rows)}
(OUT/'DIAGNOSIS.json').write_text(json.dumps(res,indent=2));print('DONE cpu',res['cpu_seconds'],'wall',res['wall_seconds'],flush=True)
