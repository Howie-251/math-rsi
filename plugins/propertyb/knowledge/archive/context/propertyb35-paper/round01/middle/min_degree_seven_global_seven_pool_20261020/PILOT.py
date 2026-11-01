from pathlib import Path
from itertools import combinations
from math import comb,ceil
import json,time
P=Path(__file__).resolve().parent;R=P.parents[4];start=time.process_time()
pairs=json.loads((R/'context/propertyb35-paper/round01/twentyone-high/DOUBLES.json').read_text())['cases']
allowed={D:sorted({z['codegree'] for z in pairs if z['degrees']==[7,D] and not z['strict']}) for D in range(13,19)}
patterns=[(13,18,18),(14,17,18),(15,16,18),(15,17,17),(16,16,17)]
rows=[]
for ds in patterns:
 domain=[];before=0;byc={}
 for c01 in range(1,min(ds[0],ds[1])+1):
  for c02 in range(1,min(ds[0],ds[2])+1):
   for c12 in range(1,min(ds[1],ds[2])+1):
    cs=(c01,c02,c12)
    L=[4*ds[0]-c01-c02,4*ds[1]-c01-c12,4*ds[2]-c02-c12]
    if any(not 18*min(allowed[D])<=l<=18*max(allowed[D]) for D,l in zip(ds,L)):continue
    for t in range(min(cs)+1):
     mu=[35-sum(ds)+sum(cs)-t,ds[0]-c01-c02+t,ds[1]-c01-c12+t,c01-t,ds[2]-c02-c12+t,c02-t,c12-t,t]
     if min(mu)<0:continue
     assert sum(mu)==35 and all(sum(n for m,n in enumerate(mu) if m>>j&1)==D for j,D in enumerate(ds))
     before+=1
     # Two high points17/18 force every low to meet each three times.
     # Shared trace low count T=3c-t since only one other non-low remains.
     shared=[];ok=True
     for i,j in combinations(range(3),2):
      if min(ds[i],ds[j])<17:continue
      c={(0,1):c01,(0,2):c02,(1,2):c12}[(i,j)]
      T=3*c-t;neither=35-ds[i]-ds[j]+c
      assert T>=2*c
      if not (18+T<=5*neither):ok=False
      shared.append({'points':[i,j],'degrees':[ds[i],ds[j]],'codegree':c,'T_actual_low_triples':T,'neither_original_edges':neither,'bound':ceil((18+5*(ds[i]+ds[j]-35))/3)})
     if not ok:continue
     domain.append({'pair_codegrees':cs,'triple':t,'high_trace_counts':mu,'low_high_codegree_sums':L,'shared':shared})
 domaincs=[r['pair_codegrees'] for r in domain]
 rows.append({'high_degrees':ds,'after_independent_degree_rows':before,'after_shared_pool':len(domain),'pair_codegree_ranges':[[min(c[i] for c in domaincs),max(c[i] for c in domaincs)] for i in range(3)],'domain':domain})
res={'status':'COMPLETE_A18_SHARED_HIGH_TRACE_NECESSARY_DOMAIN','scope':'nonB H21/35simple5/paircover/min7; use old gates Delta<=18 and actual lambda7,D sets. a7=18 leaves exactly3 high points. Exact high trace reconstruction and same low pool shared edges. Not H classification or a coloring proof.','a7_upper':18,'actual_a18_high_degree_types':patterns,'rows':rows,'cpu_seconds':time.process_time()-start}
assert res['cpu_seconds']<10
(P/'RESULT.json').write_text(json.dumps(res,indent=2)+'\n')
print('CPU',res['cpu_seconds'])
for r in rows:print({k:v for k,v in r.items() if k!='domain'})
