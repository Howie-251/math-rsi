from pathlib import Path
import json,itertools
R=Path('.');base=json.loads((R/'r4_boundary_blocking_3_5_1.json').read_text());proof=json.loads((R/'r4_inverse_blockers_3_5_1_verification.json').read_text());assert proof['status']=='PASS'
byc={}
for row in base['reports']:
 byc.setdefault(row['c'],set()).update(frozenset(tuple(e) for e in item['matching']) for item in row['items'] if item['blocking_pairing'] is None)
reports=[]
for c in (4,6,8,10,12):
 ss=[]
 for target in ((3,5),(3,9),(5,9)):
  for p in itertools.permutations(range(4)):
   tr=lambda v:sum(((v>>i)&1)<<p[i] for i in range(4))
   if tr(1)==1 and {tr(3),tr(5)}==set(target):break
  else:raise AssertionError(target)
  ss.append({frozenset(tuple(sorted((tr(a),tr(b)))) for a,b in F) for F in byc[c]})
 joint=set.intersection(*ss)
 rows=[]
 for line in (R/f't15_core1_route_B{c}.txt').read_text().splitlines():
  
  if not line.strip():continue
  q=list(map(int,line.split()));rows.append(frozenset(tuple(q[i:i+2]) for i in range(0,len(q),2)))
 assert len(rows)==len(set(rows)) and set(rows)==joint
 reports.append({'c':c,'joint_residual_B':len(joint),'B_list_checked':True})
(R/'t15_core1_joint_B_verification.json').write_text(json.dumps({'status':'PASS','canonical_dependency':'r4_inverse_blockers_3_5_1_verification.json','reports':reports},indent=2));print(reports)
