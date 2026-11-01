"""Refine the true single-blue threshold to s_p>=2 for both degree8 and degree9.
Read the prior necessary multigraph inventory; no external-vertex enumeration.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
P=Path(__file__).resolve().parent;s=json.loads((P/'PURE_P2_PROFILE.json').read_text());pairs=list(combinations(range(6),2));results=[]
for case in s['cases']:
 nine=case['summary']['nine'];counts=Counter();remaining=[]
 for row in case['records']:
  good=[i for i in range(4) if row['P2degrees'][i]>=2]
  if good:counts['new_single_blue_A']+=1;continue
  if row['two_blue_zeroT']:counts['two_blue_zeroT']+=1;continue
  options=[]
  for blue in combinations(range(6),2):
   pos3=sum(z for ij,z in zip(pairs,row['multiplicities']) if all(v in blue for v in ij));neg3=sum(z for ij,z in zip(pairs,row['multiplicities']) if all(v not in blue for v in ij));pos4=sum(row['P1counts'][v] for v in blue)
   if pos3==0 and pos4<=8:options.append((neg3,pos4,blue))
  if not options:
   counts['mixed_positive_or_larger_remaining']+=1;remaining.append(dict(**row,blue=None));continue
  best=min(options);assert best[0]==1 and best[1]==8
  counts['eight_four_one_T_nineteen_B']+=1;remaining.append(dict(**row,blue=best[2]))
 results.append(dict(nine=nine,counts=dict(counts),residual_records=remaining))
out=dict(scope=__doc__,total_original=453,total_new_single=sum(z['counts'].get('new_single_blue_A',0) for z in results),total_zeroT=sum(z['counts'].get('two_blue_zeroT',0) for z in results),total_eight_four_gate=sum(z['counts'].get('eight_four_one_T_nineteen_B',0) for z in results),total_mixed_remaining=sum(z['counts'].get('mixed_positive_or_larger_remaining',0) for z in results),results=results)
(P/'REFINED_SELECTION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2));print([(z['nine'],z['counts']) for z in results])
