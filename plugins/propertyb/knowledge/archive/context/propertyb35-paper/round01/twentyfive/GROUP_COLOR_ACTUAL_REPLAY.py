"""Independent closed-form replay of all 252 orbit first moments for the actual H.
E(r)= product term + symmetric 221 term + monochromatic whole-group term.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from math import comb,prod
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();src=json.loads((P/'GROUP_COLOR_ACTUAL_CHECK.json').read_text());values=[]
for row in src['expectations']:
 r=row['red_counts'];b=[5-x for x in r]
 one=Q(prod(r)+prod(b),625)
 two=Q(sum(comb(c[i],2)*comb(c[j],2)*sum(c[k] for k in range(5) if k not in (i,j)) for c in (r,b) for i,j in combinations(range(5),2)),600)
 whole=sum(x in (0,5) for x in r);total=one+two+whole
 assert total==Q(row['expected_monochromatic_edges'])
 values.append((total,r,one,two,whole))
minimum=min(v[0] for v in values);best=[dict(red_counts=r,rainbow_11111_contribution=str(one),composition_221_contribution=str(two),whole_group_contribution=whole,total=str(total)) for total,r,one,two,whole in values if total==minimum]
assert minimum==Q(229,200) and len(best)==2
out=dict(scope=__doc__,orbit_count=252,all_values_equal=True,minimum=str(minimum),minimizers=best,elapsed_seconds=time.perf_counter()-st)
(P/'GROUP_COLOR_ACTUAL_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
