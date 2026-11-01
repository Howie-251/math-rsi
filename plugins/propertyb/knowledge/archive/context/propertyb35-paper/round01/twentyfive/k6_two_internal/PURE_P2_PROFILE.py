"""Six-edge multigraph necessary domain for k6/two internal/pure P2.
No exterior vertices/edges or H enumeration. Only actual selectable center patterns are tested.
"""
from pathlib import Path
from itertools import combinations,combinations_with_replacement
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();pairs=list(combinations(range(6),2));ab=pairs.index((4,5));out=[]
for nine in [0,4]:
 degrees=[8]*6;degrees[nine]=9;c=[2]*4+[1]*2;records=[];not_covered=[]
 for extra in combinations_with_replacement(range(15),5):
  mm=[0]*15;mm[ab]=1
  for i in extra:mm[i]+=1
  ss=[sum(z for pair,z in zip(pairs,mm) if i in pair) for i in range(6)]
  singles=[degrees[i]-c[i]-ss[i] for i in range(6)]
  if min(singles)<0 or any(4*(degrees[i]-c[i])-ss[i]<18 for i in range(6)):continue
  good=[i for i in range(4) if (degrees[i]==8 and ss[i]>=2) or (degrees[i]==9 and ss[i]>=3)]
  if good:continue
  row=dict(multiplicities=mm,P2degrees=ss,P1counts=singles)
  blue_witness=None
  for blue in combinations(range(6),2):
   pos3=sum(z for pair,z in zip(pairs,mm) if all(i in blue for i in pair));neg3=sum(z for pair,z in zip(pairs,mm) if all(i not in blue for i in pair));pos4=sum(singles[i] for i in blue)
   if pos3==0 and neg3==0 and pos4<=8:
    blue_witness=dict(blue=blue,positive4=pos4,negative4=27-pos4);break
  row['two_blue_zeroT']=blue_witness
  if blue_witness is None:not_covered.append(row)
  records.append(row)
 summary=dict(nine=nine,no_good_single_center=len(records),two_blue_zeroT_covered=len(records)-len(not_covered),residual=len(not_covered))
 out.append(dict(summary=summary,records=records,first_residual=not_covered[:1]))
result=dict(scope=__doc__,summaries=[x['summary'] for x in out],elapsed_seconds=time.perf_counter()-st,cases=out)
(P/'PURE_P2_PROFILE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(summaries=result['summaries'],elapsed_seconds=result['elapsed_seconds']),indent=2));print('first residuals',json.dumps([z['first_residual'] for z in out],indent=2))
