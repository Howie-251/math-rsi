"""Exact trace-budget and actual signed-count check for the six non-pure inventories.
No higher-trace slot enumeration or exterior edge enumeration.
"""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
inventories=sorted((6-2*n3-3*n4,n3,n4) for n4 in range(3) for n3 in range(4) if 6-2*n3-3*n4>=0)
assert len(inventories)==7
rows=[]
def add(inv,degree,k,s,gate,forbidden=0,comment=''):
 n2,n3,n4=inv;N=33-n2-n3-n4;m=degree-2-k-s;neg3=n2-s;B=N-m
 assert 0<=s<=n2 and 0<=m and 0<=B<=28
 if gate=='five_A':assert m<=5 and neg3<=4 and forbidden==0
 elif gate=='five_B_twoT':assert m<=5 and neg3<=2 and forbidden==1 and 4-forbidden>=3
 elif gate=='five_size_at_least2':assert m<=5 and neg3==0 and forbidden<=2 and 4-forbidden>=2
 elif gate=='six_fourT':assert m==6 and neg3==4 and B==22
 else:raise AssertionError(gate)
 rows.append(dict(inventory=inv,P1total=N,selected_degree=degree,higher_hits=k,P2degree=s,positive4=m,negative3=neg3,negative4=B,forbidden_upper=forbidden,gate=gate,comment=comment))
for s in range(5):add((4,1,0),8,1,s,'five_A')
for s in range(1,5):add((4,1,0),9,1,s,'five_A',comment='only T={h,a,b}')
add((4,1,0),9,1,0,'six_fourT',comment='unique exceptional triple')
for s in range(4):add((3,0,1),8,1,s,'five_A')
add((0,0,2),8,2,0,'five_A')
add((0,0,2),8,1,0,'five_B_twoT',1,'forbid missed four-trace singleton')
for s in range(2):
 add((1,1,1),8,2,s,'five_A')
 add((1,1,1),8,1,s,'five_B_twoT',1,'forbid missed triple endpoint')
for s in range(3):
 add((2,2,0),8,2,s,'five_A')
 add((2,2,0),8,1,s,'five_B_twoT',1,'forbid missed triple endpoint')
 add((2,2,0),9,2,s,'five_A',comment='both traces={h,a,b}')
for k in [1,2,3]:add((0,3,0),8,k,0,'five_size_at_least2',3-k,'forbid one endpoint of each missed triple')
add((0,3,0),9,3,0,'five_A',comment='all traces={h,a,b}')
assert len(rows)==33
out=dict(passed=True,scope=__doc__,complete_inventory_list=inventories,nonpure_count_interfaces=len(rows),private_negative_four_max=max(z['negative4'] for z in rows),actual_outer_occurrence_bound=7,pure_case='canonical pure-pair theorem, separately replayed',interfaces=rows)
(P/'HIGH_TRACE_CALLER_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='interfaces'},indent=2))
