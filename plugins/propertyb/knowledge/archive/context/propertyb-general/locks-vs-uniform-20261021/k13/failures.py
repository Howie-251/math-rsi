import json,time
from pathlib import Path
from scan import *
from propertyB_k10_k11_certified import FixedCertificate
out=[];start=time.monotonic()
for m in (9600,9580,9570,9564):
 x=json.loads((OUT/f'M{m}-screen.json').read_text());v=x['uncovered_v'];cal=FixedCertificate(K,m);row={'M':m,'v':v,'candidate_domain':[min(x['candidate_v']),max(x['candidate_v'])],'screen_seconds':x['wall_seconds'],'modes':{}}
 for mode in ('none','one','two','three'):
  ps=parameters(m,v,mode)
  if ps is None:
   if mode=='two':
    bad=next(d for d in range(CEIL(v-1,KM1),K*m//v+1) if 2*(v-1)-KM1*d<=0);row['modes'][mode]={'unavailable':True,'d':bad,'s_d':2*(v-1)-KM1*bad}
   if mode=='three':
    vals=[(2*KM1*((D+1)*v-K*m)-(KM1*(D+1)-v+2)**2,D,(D+1)*v-K*m) for D in range(CEIL(v-1,KM1),m+1) if (D+1)*v>K*m]
    b=max(vals);row['modes'][mode]={'unavailable':True,'D_domain':[CEIL(v-1,KM1),m],'max_strict_difference':b[0],'at_D':b[1],'Z':b[2]}
   continue
  chosen=ps[-2:] if mode=='three' else ps[-1:];rr=[]
  for p in chosen:
   z=cal.unlocked(v) if mode=='none' else getattr(cal,mode)(v,*p)
   rr.append({'profile':p,'z':z,'gap':S-z})
  row['modes'][mode]=rr
 out.append(row);print(json.dumps(row),flush=True)
(OUT/'FAILURE_WITNESSES.json').write_text(json.dumps({'rows':out,'wall_seconds':time.monotonic()-start},indent=2))
