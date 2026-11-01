from pathlib import Path
from itertools import permutations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;start=time.process_time();f=json.loads((P/'FIXED_RESULT.json').read_text());s=json.loads((P/'CLEAN_RESULT.json').read_text());lookup={(tuple(z['traces']),tuple(z['attachments'])):i for i,z in enumerate(f['cases'])};sid={(tuple(z['traces']),tuple(z['attachments'])):i for i,z in enumerate(f['nonstrict'])};star={(z['source'],z['degree_z'],tuple(z['s'])):i for i,z in enumerate(s['cases'])}
perms=list(permutations(range(5)));auts={}
def image(v,p):
 a=[0]*5
 for i,x in enumerate(v):a[p[i]]=x
 return tuple(a)
def mapmask(m,p):return sum(1<<p[i] for i in range(5) if m>>i&1)
for z in f['nonstrict']:
 tr=tuple(z['traces'])
 if tr not in auts:auts[tr]=[p for p in perms if tuple(sorted(mapmask(m,p) for m in tr))==tr]
source_closed={};remaining=[];receipts=[]
for source,z in enumerate(f['nonstrict']):
 tr=tuple(z['traces']);aa=z['attachments'];fivecert=None
 for p in auts[tr]:
  target=f['cases'][lookup[(tr,image(aa,p))]]
  if target['strict']:fivecert={'permutation':p,'target_attachments':target['attachments'],'target_positions':target['positions'],'bound':target['bound']};break
 if fivecert:source_closed[source]={'reason':'five_transport','certificate':fivecert};continue
 failures=[]
 for zz in [x for x in s['cases'] if x['source']==source]:
  cert=None
  for p in auts[tr]:
   ts=sid[(tr,image(aa,p))];target=s['cases'][star[(ts,zz['degree_z'],image(zz['s'],p))]]
   if target['strict']:
    # K point relabeling and z fixed must move the actual35 trace counts together.
    dest=Counter()
    for m,n in zz['counts'].items():m=int(m);dest[(mapmask(m>>1,p)<<1)|(m&1)]+=n
    assert +dest==+Counter({int(m):n for m,n in target['counts'].items()})
    cert={'source':source,'degree_z':zz['degree_z'],'s':zz['s'],'permutation':p,'target_source':ts,'target_positions':target['positions'],'bound':target['bound']};break
  if cert:receipts.append(cert)
  else:failures.append(zz)
 if not failures:source_closed[source]={'reason':'all_clean_stars_after_transport'}
 else:remaining.append({'source':source,**{k:z[k] for k in ['traces','attachments','F_degrees','clean_lower','clean_degree_upper','outside_excess_above7']},'failed_stars':failures})
r={'status':'COMPLETE_ACTUAL_F_AUTOMORPHISM_TRANSPORT','scope':'No new layouts/counts. Actual F relabeling preserving three trace multiset; transports attachments, z star,35trace counts and point positions together. Not H automorphism.','closed_sources':source_closed,'remaining_sources':len(remaining),'remaining_stars':sum(len(z['failed_stars']) for z in remaining),'rows':remaining,'transport_certificates':receipts,'cpu_seconds':time.process_time()-start}
(P/'TRANSPORT_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print('CPU',r['cpu_seconds'],'closed',list(source_closed),'remain',r['remaining_sources'],r['remaining_stars'])
for z in remaining:print(z['source'],z['traces'],z['attachments'],z['F_degrees'],'clean',z['clean_lower'],'left',len(z['failed_stars']),Counter(x['degree_z'] for x in z['failed_stars']))
