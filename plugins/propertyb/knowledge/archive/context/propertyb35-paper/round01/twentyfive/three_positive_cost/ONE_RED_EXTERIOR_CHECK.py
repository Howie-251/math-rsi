"""Exact numerical branches of the two direct signed-set lemmas and G partition caller.
No positive-set classification, H enumeration, or solver.
"""
from itertools import product
from math import prod
from pathlib import Path
import json
P=Path(__file__).resolve().parent
checks={
'A_disjoint5':(4**5,4*4**2+28*4),
'A_x_hits3':(4**2,4),
'A_remaining3_disjoint':(4**3,4*4+14-2),
'A_switch_disjoint':(3*3*4,14-2-4),
'B_disjoint5':(3**5,4**2+28*4),
'B_x_hits3':(3**2,1),
'B_y_hits2':(3,1),
'B_remaining3_disjoint':(3**3,4+14-2)
}
assert all(a>b for a,b in checks.values())
for sizes in product([3,4],repeat=5):assert prod(sizes)>=243>128
for sizes in product([3,4],repeat=3):assert prod(sizes)>=27>16
partitions=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2)]
rows=[]
for pp in partitions:
 rest=list(pp);rest.remove(max(pp));n1=rest.count(3);n2=rest.count(2);n3=rest.count(1)
 assert n1==0 and n2<=1 and n3<=4 and (n2==0 or n3<=1)
 rows.append(dict(partition=pp,negative1=n1,negative2=n2,negative3=n3,lemma='B' if n2 else 'A'))
out=dict(passed=True,scope=__doc__,strict_counts={k:dict(candidates=a,bad_upper=b,gap=a-b) for k,(a,b) in checks.items()},positive_size_patterns_B=32,partition_cases=rows)
(P/'ONE_RED_EXTERIOR_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(passed=True,strict_numeric_branches=len(checks),partition_cases=len(rows))))
