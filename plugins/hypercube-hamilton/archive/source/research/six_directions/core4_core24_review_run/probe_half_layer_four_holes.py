"""Structured K(Q5) falsification cases containing a complete half-layer."""
import json
import random
from pathlib import Path
from avoided_vertex_transfer import cycle_on

ROOT = Path(__file__).resolve().parent
rng = random.Random(20261116)
V = set(range(32))
out = []
for i in range(120):
    half = {(x, x ^ 1) for x in V if x % 2 == 0 and x.bit_count() % 2 == 0}
    rest = V-{q for e in half for q in e}
    ev = sorted(q for q in rest if q.bit_count() % 2 == 0)
    od = sorted(rest-set(ev))
    holes = rng.sample(ev, 2 if i < 60 else 1)+rng.sample(od, 2 if i < 60 else 3)
    free = sorted(rest-set(holes))
    rng.shuffle(free)
    m = sorted(half | {tuple(sorted(e)) for e in zip(free[::2], free[1::2])})
    forbidden = None if i < 60 else holes[-1]
    result = cycle_on(V-({forbidden} if forbidden is not None else set()), m, seconds=3)
    c = dict(case=i, matching=m, holes=sorted(holes), forbidden=forbidden, **result)
    out.append(c)
    (ROOT/'half_layer_four_hole_probe.json').write_text(json.dumps(dict(
        scope='Bounded structured half-layer falsification probes, not exhaustive',
        cases=out, full_p6_proved=False), indent=2), encoding='utf8')
    print(i, result['status'], flush=True)
    if result['status'] == 'SOLVER_INFEASIBLE':
        break
