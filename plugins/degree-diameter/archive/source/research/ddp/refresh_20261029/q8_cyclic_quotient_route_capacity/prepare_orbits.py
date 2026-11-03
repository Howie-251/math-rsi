#!/usr/bin/env python3
"""Canonicalize the already saved formal-route survivors under cube labels."""
from collections import Counter
from itertools import permutations
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent
start = time.process_time()
autos = []
for p in permutations(range(3)):
    for t in range(8):
        autos.append([t ^ sum(((l >> i) & 1) << p[i] for i in range(3)) for l in range(8)])
assert len({tuple(a) for a in autos}) == 48
orbits = {}
for line in (HERE / 'SURVIVING_QUOTIENTS.jsonl').read_text().splitlines():
    d = json.loads(line)
    images = []
    for a in autos:
        images.append(tuple(sorted((min(a[u], a[v]), max(a[u], a[v]), h)
                                   for u, v, symbol, h in d['quotient'])))
    key = min(images)
    if key not in orbits:
        orbits[key] = 0
    orbits[key] += 1
assert sum(orbits.values()) == 3189
rows = [dict(edges=k, labelled_count=n) for k, n in sorted(orbits.items())]
(HERE / 'CANONICAL_QUOTIENTS.json').write_text(json.dumps(rows, indent=2) + '\n')
with (HERE / 'canonical_quotients.txt').open('w') as f:
    f.write(str(len(rows)) + '\n')
    for row in rows:
        f.write(f"{len(row['edges'])} {row['labelled_count']}\n")
        for u, v, half in row['edges']:
            f.write(f'{u} {v} {half}\n')
result = dict(status='CUBE_AUT_CANONICALIZED', labelled_quotients=3189,
              cube_automorphisms=48, canonical_quotients=len(rows),
              orbit_sizes=dict(sorted(Counter(orbits.values()).items())),
              CPU_seconds=time.process_time()-start)
(HERE/'CANONICAL_RESULT.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
