"""One necessary local five-eight-degree profile; not a full hypergraph witness.
Exact all-order/all-position pure-quota DP and independent fixed witness replay.
"""
from pathlib import Path
from itertools import combinations
import sys,json
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
ns={sum(1<<i for i in S):2 for S in combinations(range(5),2)};ns[0]=15
eng=SubsetEngine(20,5,ns);z=eng.solve();z=eng.verify(z)
assert str(z['bound'])=='773/715'
z.update(scope=__doc__,method='minimum over all labelled orders and positions for total+nested pure quotas only',actual_H_not_constructed=True)
(HERE/'TIGHT_FIVE_EIGHT.json').write_text(json.dumps(json_value(z),indent=2)+'\n')
print(z['bound'],z['positions'])
