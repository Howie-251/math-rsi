"""Independent certificate check; reuses only stdlib witness predicates."""
import hashlib
import json
from collections import Counter
from pathlib import Path
from verify_recut import edges, matching, sequence

ROOT = Path(__file__).resolve().parent
V = set(range(64))


def check(c):
    assert c['status'] == 'FOUND'
    u, v, h, cut = (c[k] for k in ('u', 'v', 'h', 'cut'))
    m = matching(c['matching'])
    assert all((a ^ b).bit_count() == 1 for a, b in m)
    holes = V - {q for e in m for q in e}
    assert holes == set(c['holes']) and len(holes) == 4 and u in holes
    assert u.bit_count() % 2 == 0 and v.bit_count() % 2 == 1
    assert tuple(sorted((v, h))) in m
    star = matching(c['M_star'])
    assert star == m - {tuple(sorted((v, h)))} | {tuple(sorted((u, h)))}
    a_side = {q for q in V if (q >> cut) & 1 == (v >> cut) & 1}
    b_side = V-a_side
    ma = {e for e in star if set(e) <= a_side}
    mb = {e for e in star if set(e) <= b_side}
    cross = star-ma-mb
    assert cross == matching(c['cross_star']) and len(cross) >= 2 and len(cross) % 2 == 0
    xa = {q for e in cross for q in e if q in a_side}
    xb = {q for e in cross for q in e if q in b_side}
    d = matching(c['D'])
    assert {q for e in d for q in e} == xa
    la = matching(c['L_A'])
    assert la == ma | d
    a_holes = a_side - {q for e in la for q in e}
    assert len(a_holes) == 2 and v in a_holes
    assert all(q.bit_count() % 2 == 1 for q in a_holes)
    cae = sequence(c['C_A'], a_side-{v}, la, cycle=True)
    segs = c['transferred_paths']
    assert len({q for p in segs for q in p[1:-1]}) == sum(len(p)-2 for p in segs)
    assert {q for p in segs for q in p[1:-1]} == a_side-{v}
    assert {q for p in segs for q in (p[0], p[-1])} == xb
    assert len(xb) == 2*len(segs)
    transferred = set().union(*(edges(p) for p in segs))
    assert transferred == (cae-d) | cross
    r = {tuple(sorted((p[0], p[-1]))) for p in segs}
    lb = matching(c['L_B'])
    assert lb == mb | r
    b_holes = b_side - {q for e in lb for q in e}
    assert len(b_holes) == 2 and {q.bit_count() % 2 for q in b_holes} == {0, 1}
    cb = sequence(c['C_B'], b_side, lb, cycle=True)
    ge = sequence(c['C_global'], V-{v}, star, cycle=True)
    assert ge == (cb-r) | transferred
    pe = sequence(c['path'], V, m)
    assert c['path'][0] == u and c['path'][-1] == v
    assert pe == ge - {tuple(sorted((u, h)))} | {tuple(sorted((h, v)))}


if __name__ == '__main__':
    raw = (ROOT/'two_odd_holes_results.json').read_bytes()
    data = json.loads(raw)
    for c in data['cases']:
        check(c)
    result = dict(status='PASS', verified=len(data['cases']), scope=data['scope'],
                  root_sides=dict(Counter(c['root_side'] for c in data['cases'])),
                  artificial_cross=sum(c['artificial_cross'] for c in data['cases']),
                  input_sha256=hashlib.sha256(raw).hexdigest(),
                  full_p6_proved=False, exhaustive_q6=False)
    (ROOT/'two_odd_holes_verification.json').write_text(json.dumps(result, indent=2), encoding='utf8')
    print(json.dumps(result, indent=2))
