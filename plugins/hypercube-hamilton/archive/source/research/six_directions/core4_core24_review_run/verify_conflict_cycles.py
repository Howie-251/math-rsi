"""Independent stdlib check of complete Z15/Z16 conflict-expansion witnesses."""
import hashlib
import json
from collections import Counter
from pathlib import Path
from verify_recut import edges, matching, sequence, halves

ROOT = Path(__file__).resolve().parent
V = set(range(64))


def check(c):
    assert c['status'] == 'FOUND'
    u, v, h, cut = (c[k] for k in ('u', 'v', 'h', 'cut'))
    m = matching(c['matching'])
    assert all((a ^ b).bit_count() == 1 for a, b in m)
    holes = V-{q for e in m for q in e}
    assert len(holes) == 4 and holes == set(c['holes']) and u in holes
    assert u.bit_count() % 2 == 0 and v.bit_count() % 2 == 1
    vh, uh = tuple(sorted((v, h))), tuple(sorted((u, h)))
    assert vh in m
    star = matching(c['M_star'])
    assert star == m-{vh} | {uh}
    a_side = {q for q in V if (q >> cut) & 1 == (v >> cut) & 1}
    b_side = V-a_side
    ma = {e for e in star if set(e) <= a_side}
    mb = {e for e in star if set(e) <= b_side}
    cross = star-ma-mb
    assert cross == matching(c['cross_star'])
    xa = {q for e in cross for q in e if q in a_side}
    xb = {q for e in cross for q in e if q in b_side}
    d, la = matching(c['D']), matching(c['L_A'])
    assert la == ma | d
    z, bridge, conflict, r, s = (c[k] for k in ('z', 'bridge', 'conflict', 'r', 's'))
    if c['mode'] == 'Z15':
        assert z in b_side and len(xa) % 2 == 1
        assert {q for e in d for q in e} == xa | {bridge ^ (1 << cut)}
        free_a = a_side-{q for e in la for q in e}
        assert len(free_a) == 2 and v in free_a
        assert all(q.bit_count() % 2 == 1 for q in free_a)
        ae = sequence(c['C_A'], a_side-{v}, la, cycle=True)
        bridges = {tuple(sorted((bridge, bridge ^ (1 << cut))))}
    else:
        assert c['mode'] == 'Z16' and z in a_side and len(xa) >= 2
        assert not halves(ma, a_side, cut)
        a, k = c['a'], c['k']
        bk, ak = tuple(sorted((bridge, k))), tuple(sorted((a, k)))
        assert bk in ma
        tb = matching(c['T_b'])
        assert tb == ma-{bk} | d | {ak} and not halves(tb, a_side, cut)
        sequence(c['C_A0'], a_side-{v, bridge}, tb, cycle=True)
        assert c['K_A'][0] == a and c['K_A'][-1] == bridge
        ae = sequence(c['K_A'], a_side-{v}, la)
        bridges = {tuple(sorted((q, q ^ (1 << cut)))) for q in (z, bridge)}
    segs = c['transferred_paths']
    assert len({q for p in segs for q in p[1:-1]}) == sum(len(p)-2 for p in segs)
    assert {q for p in segs for q in p[1:-1]} == a_side-{v}
    assert len({q for p in segs for q in (p[0], p[-1])}) == 2*len(segs)
    assert all(p[0] in b_side and p[-1] in b_side for p in segs)
    transferred = set().union(*(edges(p) for p in segs))
    assert transferred == (ae-d) | cross | bridges
    rr = {tuple(sorted((p[0], p[-1]))) for p in segs}
    assert ({q for e in rr for q in e} & {q for e in mb for q in e}) == {conflict}
    cr, cs, rs = (tuple(sorted(p)) for p in ((conflict, r), (conflict, s), (r, s)))
    assert cr in mb and cs in rr and len({conflict, r, s}) == 3
    lb = matching(c['L_B'])
    assert lb == (mb-{cr}) | (rr-{cs}) | {rs}
    free_b = b_side-{q for e in lb for q in e}
    assert len(free_b) == 2 and conflict in free_b
    assert len({q.bit_count() % 2 for q in free_b}) == 1
    be = sequence(c['C_B'], b_side-{conflict}, lb, cycle=True)
    ge = sequence(c['C_global'], V-{v}, star, cycle=True)
    assert ge == be-(rr-{cs})-{rs} | {cr} | transferred
    pe = sequence(c['path'], V, m)
    assert c['path'][0] == u and c['path'][-1] == v
    assert pe == ge-{uh} | {vh}
    return cr == uh


if __name__ == '__main__':
    raw = (ROOT/'conflict_cycle_results.json').read_bytes()
    data = json.loads(raw)
    restored_long = sum(check(c) for c in data['cases'])
    result = dict(status='PASS', verified=len(data['cases']), scope=data['scope'],
                  modes=dict(Counter(c['mode'] for c in data['cases'])),
                  conflict_edge_is_hu=restored_long,
                  input_sha256=hashlib.sha256(raw).hexdigest(),
                  full_p6_proved=False, exhaustive_q6=False)
    (ROOT/'conflict_cycle_verification.json').write_text(json.dumps(result, indent=2), encoding='utf8')
    print(json.dumps(result, indent=2))
