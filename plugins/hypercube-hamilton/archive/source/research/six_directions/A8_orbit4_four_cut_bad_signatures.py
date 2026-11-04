from pathlib import Path
from itertools import combinations
import json
R=Path(__file__).resolve().parent
H={0,1,2,4,15,23,27,29};covered=set(range(32))-H
rows=[]
for bit,Y,ob,kind in [(2,{3,6},(10,18),'T15'),(4,{5,6},(12,20),'T15'),(8,{9,10,12},(8,24),'T63'),(16,{17,18,20},(16,24),'T63')]:
 B={x for x in range(32) if x&bit};S=Y|set(ob);forbidden=[];allowed=[]
 for a,b in combinations(sorted(covered),2):
  bad=False
  if bool(a&bit)!=bool(b&bit):
   end=a if a&bit else b
   if end not in S:bad=True
  elif a in B:
   if (a in Y and b not in S) or (b in Y and a not in S):bad=True
  (forbidden if bad else allowed).append([a,b])
 rows.append(dict(cut_bit=bit,B_original_holes=sorted(H&B),bridge_vertices=sorted(Y),obstruction_edge=ob,special_vertices=sorted(S),local_extension=kind,nonfixed_bad_rule='all crossing B ports lie in S, and every internally matched bridge vertex has its partner in S',allowed_original_edges=allowed,forbidden_original_edges=forbidden,allowed_count=len(allowed),forbidden_count=len(forbidden)))
(R/'A8_orbit4_four_cut_bad_signatures.json').write_text(json.dumps(dict(status='EXACT_FIXED_BRIDGE_TEMPLATE_FAILURE_SIGNATURES_PROOF_PENDING_REVIEW',holes=sorted(H),forbidden_vertex=0,covered=sorted(covered),rows=rows,full_a8_proved=False),indent=2)+'\n')
print([(r['cut_bit'],r['allowed_count'],r['forbidden_count']) for r in rows])
