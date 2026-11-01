"""Exact small integer star/count domain only; no original-H search."""
import itertools
import json
import time
from pathlib import Path
started = time.process_time()
r = 7
stars = [u for u in itertools.product(range(7), repeat=4)
         if sum(u) == 6 and u[2]+2*u[3]-u[0] == 0
         and 4*u[2]+5*u[3] <= 7]
assert stars == [(0,6,0,0),(1,4,1,0),(2,3,0,1)]
rows = []
for counts in itertools.product(range(8), repeat=3):
    if sum(counts) != r:
        continue
    inc = [sum(q*u[j] for q,u in zip(counts,stars)) for j in range(4)]
    if any(v % (j+1) for j,v in enumerate(inc)):
        continue
    n = [v//(j+1) for j,v in enumerate(inc)]
    n = [35-sum(n)]+n
    if n[0] < 0:
        continue
    assert sum(n) == 35
    assert sum(j*n[j] for j in range(5)) == 42
    assert sum(j*(j-1)//2*n[j] for j in range(5)) == 21
    rows.append({'A_B_C_counts':counts,'n0_to_n4':n})
assert len(rows) == 5
assert {(x['A_B_C_counts'][2],x['A_B_C_counts'][1]) for x in rows} == {(0,0),(0,3),(0,6),(4,0),(4,3)}
result = {'scope':'Only exact necessary integer six-star and incidence inventory. The actual-H exclusions are paper proofs in REPORT.md; no H/coloring enumeration.',
          'stars_a1_to_a4':stars,'inventory_count':len(rows),'inventories':rows,
          'cpu_seconds':time.process_time()-started}
Path(__file__).with_name('RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',len(stars),'stars',len(rows),'inventories; CPU',result['cpu_seconds'])
