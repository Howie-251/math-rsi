"""Restore actual signed counts and exact theorem interfaces for all matching/attachment parameters.
Reads only saved multigraph vectors; no source proof/model import, outer edge search or solver.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
P=Path(__file__).resolve().parent;source=json.loads((P/'SELECTOR_REPLAY.json').read_text());pairs=list(combinations(range(6),2));hist=Counter();out=[]
for row in source['records']:
 d=[8]*6;d[row['nine']]=9;mm=row['multiplicities'];s=[sum(z for ij,z in zip(pairs,mm) if i in ij) for i in range(6)];u=[d[i]-(2 if i<4 else 1)-s[i] for i in range(6)]
 assert sum(mm)==6 and sum(u)==27 and max(s[:4])<=1
 if 'star' in row:
  q=row['star'];p=next(v for v in range(4) if v!=row['nine']);blue={p,q}
 else:blue=set(row['blue'])
 assert len(blue)==2
 assert all(0<len(set(range(6))-{missing}&blue)<5 for missing in [4,5])
 pos4=sum(u[v] for v in blue);pos3=sum(z for ij,z in zip(pairs,mm) if set(ij)<=blue);neg3=sum(z for ij,z in zip(pairs,mm) if not set(ij)&blue);neg4=27-pos4
 if pos3==0 and neg3==0:
  assert pos4<=8 and neg4<=27;gate='eight_four_zeroT'
 elif pos3==0:
  assert pos4==8 and neg3==1 and neg4==19;gate='eight_four_oneT_eighteen'
 elif pos4+pos3<=7:
  assert pos3==1 and pos4==6 and neg3==0 and neg4==21;gate='seven_mixed_zeroT'
 else:
  assert pos4==7 and pos3==1 and neg3==0 and neg4==20 and row['nine']==row['star'];gate='eight_mixed_eighteen'
 hist[gate]+=1;out.append(dict(nine=row['nine'],blue=sorted(blue),positive4=pos4,positive3=pos3,negative3=neg3,negative4=neg4,gate=gate))
assert len(out)==276 and dict(hist)=={'eight_four_zeroT':230,'seven_mixed_zeroT':3,'eight_mixed_eighteen':1,'eight_four_oneT_eighteen':42}
# The separate high-C-degree single-blue interface: all possible center spectra/degrees.
single=[]
for d in [8,9]:
 for s in range(2,7):
  m=d-2-s
  if m<0:continue
  assert m<=5 and 6-s<=4 and 27-m<=28
  single.append(dict(degree=d,P2degree=s,positive4=m,negative3=6-s,negative4=27-m))
result=dict(passed=True,scope=__doc__,matching_attachment_states=len(out),by_gate=dict(hist),single_blue_interfaces=single,outer_ground_size=18,actual_outer_occurrence_bound=7,records=out)
(P/'PURE_PAIR_FINAL_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['records','single_blue_interfaces']},indent=2))
