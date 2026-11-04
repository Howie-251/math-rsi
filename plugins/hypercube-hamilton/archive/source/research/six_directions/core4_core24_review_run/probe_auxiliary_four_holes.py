"""Falsification probe for stronger K(Q5) four-hole cycle obligations; not proof."""
import json
import random
from collections import Counter
from pathlib import Path
from avoided_vertex_transfer import cycle_on

ROOT = Path(__file__).resolve().parent
rng = random.Random(20261115)
V = set(range(32))
ev = [x for x in V if x.bit_count() % 2 == 0]
od = sorted(V-set(ev))


def pair(points):
    points = list(points)
    rng.shuffle(points)
    return [tuple(sorted(e)) for e in zip(points[::2], points[1::2])]


def one(case, holes, forbidden=None):
    left = V-set(holes)
    kind = case % 3
    if kind == 0:
        m = pair(left)
    elif kind == 1:
        a, b = sorted(left & set(ev)), sorted(left & set(od))
        m = []
        if len(a) % 2:
            m = [(a.pop(), b.pop())]
        m += pair(a)+pair(b)
    else:
        a, b = sorted(left & set(ev)), sorted(left & set(od))
        rng.shuffle(a)
        rng.shuffle(b)
        m = list(zip(a[:min(len(a), len(b))], b[:min(len(a), len(b))]))
        m += pair(a[len(m):])+pair(b[len(m):])
    assert len(m) == 14 and len({q for e in m for q in e}) == 28
    result = cycle_on(V-({forbidden} if forbidden is not None else set()), m, seconds=3)
    return dict(case=case, matching=m, holes=sorted(holes), forbidden=forbidden,
                family=('arbitrary', 'mostly_same_parity', 'mostly_bipartite')[kind], **result)


out = []
for i in range(90):
    if i < 45:
        holes = rng.sample(ev, 2)+rng.sample(od, 2)
        forbidden = None
    else:
        holes = rng.sample(ev, 1)+rng.sample(od, 3)
        forbidden = holes[-1]
    c = one(i, holes, forbidden)
    out.append(c)
    (ROOT/'auxiliary_four_hole_probe.json').write_text(json.dumps(dict(
        scope='90 bounded random K(Q5) four-hole falsification probes, not exhaustive',
        cases=out, full_p6_proved=False), indent=2), encoding='utf8')
    print(i, c['status'], 'avoid' if forbidden is not None else 'spanning', flush=True)
    if c['status'] == 'SOLVER_INFEASIBLE':
        print('Candidate obstruction requires independent rigorous certification', flush=True)
        break
print(dict(Counter(c['status'] for c in out)))
