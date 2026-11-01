from fractions import Fraction as Q
from pathlib import Path
import json
P=Path(__file__).resolve().parent
assert Q(6,4)*Q(5,8)==Q(15,16)<1
counts={'small_overlap':(8,5),'B_disjoint':(243,2*16+28*4),'B_x3':(9,2),'B_y2':(3,2),'B_remaining3_disjoint':(27,2*4+14-2)}
assert all(a>b for a,b in counts.values())
assert all(10+(5-m)<=14 for m in range(1,6))
out=dict(passed=True,small_positive_bad_bound='15/16',strict_numeric_branches={k:dict(candidates=a,bad_upper=b) for k,(a,b) in counts.items()},two_triple_padding_max_occurrence=14)
(P/'FIVE_SMALL_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
