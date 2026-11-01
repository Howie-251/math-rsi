from pathlib import Path
from collections import Counter
from itertools import combinations_with_replacement
import json,time
P=Path(__file__).resolve().parent;R=P.parents[4];start=time.process_time();base=json.loads((P/'RESULT.json').read_text())
old=R/'context/propertyb35-paper/round01/twentyone-high';pairs=json.loads((old/'DOUBLES.json').read_text())['cases'];triples=json.loads((old/'TRIPLES.json').read_text())['cases']
full=json.loads((P.parent/'generic_high_degree_pair_gates_20261020/FULL.json').read_text())['cases']
excluded={(tuple(x['degrees']),x['codegree']) for x in pairs+full if x['strict']}
certs=[{k:x[k] for k in ['degrees','codegrees','triple','counts','positions','bound','certificates','independent_ABC']} for x in triples if x['degrees']==[7,7,7] and 3 in x['codegrees']]
assert len(certs)==16
D19=[{k:x[k] for k in ['degrees','codegree','positions','bound','certificates']} for x in pairs if x['degrees'][0]==7 and x['degrees'][1]>=19]
assert {(tuple(x['degrees']),x['codegree']) for x in D19}=={((7,D),c) for D in range(19,36) for c in range(max(1,D-28),8)}
rows=[]
for s in base['all_spectra']:
 if s['e']<=4:continue
 ct=Counter(s['degrees']);allowed={}
 for u,v in combinations_with_replacement(sorted(ct),2):
  if u==v and ct[u]<2:continue
  allowed[(u,v)]=[c for c in range(max(1,u+v-35),min(u,v)+1) if ((u,v),c) not in excluded and not (u==v==7 and ct[7]>=3 and c>=3)]
 reasons=[];profile=[]
 for d,m in sorted(ct.items()):
  lo=hi=0;empty=False
  for h,n in sorted(ct.items()):
   n-=h==d
   if n<=0:continue
   a=allowed[tuple(sorted((d,h)))]
   if not a:empty=True;break
   lo+=n*(min(a)-1);hi+=n*(max(a)-1)
  target=4*d-20
  if empty or not lo<=target<=hi:reasons.append({'degree':d,'required_repeat':target,'lower_repeat':None if empty else lo,'upper_repeat':None if empty else hi,'empty_pair_domain':empty})
  if d==7:profile.append({'seven_row_repeat':8,'minimum_from_degree_classes':None if empty else lo,'maximum_from_degree_classes':None if empty else hi})
 rows.append({'degrees':s['degrees'],'e':s['e'],'Delta':s['Delta'],'excluded':bool(reasons),'reasons':reasons,'seven_row':profile})
rem=[r for r in rows if not r['excluded']]
res={'status':'COMPLETE_OLD_GATE_CLASS_ROW_PROJECTION','scope':'e>4 integer spectra; old DOUBLES strict gates + generic FULL strict gates; if a7>=3 use actual777 gate to cap low-pair2; all class rows retain exact4d-20 repeat. This is a necessary test, not H classification.','input_spectra':len(rows),'excluded_by_at_least_one_row_or_empty_pair':sum(r['excluded'] for r in rows),'remaining':len(rem),'remaining_e_range':[min(r['e'] for r in rem),max(r['e'] for r in rem)],'remaining_Delta_range':[min(r['Delta'] for r in rem),max(r['Delta'] for r in rem)],'seven_row_minimum_maximum_among_remaining':max(r['seven_row'][0]['minimum_from_degree_classes'] for r in rem),'all_high_D_degree7_pair_certificate_keys':len(D19),'D_ge19_certificates':D19,'complete_777_codegree3_certificates':certs,'rows':rows,'cpu_seconds':time.process_time()-start}
assert res['cpu_seconds']<2
(P/'ROW_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items() if k not in ['rows','D_ge19_certificates','complete_777_codegree3_certificates']})
