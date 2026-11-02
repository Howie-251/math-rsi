"""Independent small symmetry-reduced integer quotient check; no graph solver."""
import itertools
import json
import math
from collections import Counter
from pathlib import Path
from time import process_time

ROOT = Path(__file__).resolve().parent
start = process_time()
parts = [p for p in itertools.combinations_with_replacement(range(5), 5)
         if sum(p) == 8 and 17 <= sum(x*x for x in p) <= 22]
rows = sorted({p for part in parts for p in itertools.permutations(part)})
q = [[0]*6 for _ in range(6)]
counts = []
survivors = []

def visit(i):
    if i == 6:
        ok = all(q[a][b] + sum(q[a][k]*q[k][b] for k in range(6)) >= 10
                 for a in range(6) for b in range(a+1, 6))
        if ok:
            survivors.append([r[:] for r in q])
        return 1
    count = 0
    for row in rows:
        if any(row[j] != q[i][j] for j in range(i)):
            continue
        for j in range(i+1, 6):
            q[i][j] = q[j][i] = row[j-1]
        count += visit(i+1)
    return count

for part in parts:
    for j in range(1,6):
        q[0][j] = q[j][0] = part[j-1]
    count = visit(1)
    factor = math.factorial(5)
    for mult in Counter(part).values():
        factor //= math.factorial(mult)
    counts.append(dict(first_row=list(part), count=count,
                       row_permutations=factor, weighted_count=count*factor))

raw = json.loads((ROOT/'six_independent_fibers_quotients.json').read_text())
total = sum(c['weighted_count'] for c in counts)
assert raw['status'] == 'COMPLETE'
assert total == raw['row_compatible_labeled_matrices']
assert len(rows) == raw['row_patterns']
assert len(survivors) == raw['survivors'] == 0
result = dict(status='COMPLETE', method='sorted first row, exhaustive compatible rows',
              first_rows=counts, weighted_labeled_total=total,
              row_patterns=len(rows), survivors=survivors,
              cpu_seconds=process_time()-start)
(ROOT/'six_independent_fibers_quotients.check.json').write_text(
    json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
