"""Independent stdlib verification of saved recut path/transfer witnesses."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
V = set(range(64))


def edges(seq, cycle=False):
    pairs = list(zip(seq, seq[1:]))
    if cycle:
        pairs.append((seq[-1], seq[0]))
    return {tuple(sorted(p)) for p in pairs}


def matching(raw):
    p = {tuple(sorted(e)) for e in raw}
    assert len(p) == len(raw)
    assert all(a != b for a, b in p)
    assert len({q for e in p for q in e}) == 2*len(p)
    return p


def halves(p, face, cut):
    return [(j, parity) for j in range(6) if j != cut for parity in (0, 1)
            if {tuple(sorted((x, x ^ (1 << j)))) for x in face
                if not x & (1 << j) and x.bit_count() % 2 == parity} <= p]


def sequence(seq, vertices, required, cycle=False):
    assert len(seq) == len(vertices) and set(seq) == vertices
    es = edges(seq, cycle)
    assert required <= es
    assert all((a ^ b).bit_count() == 1 or (a, b) in required for a, b in es)
    return es


def check(c):
    assert c['status'] == 'FOUND'
    u, v, h, cut = (c[k] for k in ('u', 'v', 'h', 'cut'))
    m = matching(c['matching'])
    assert all((a ^ b).bit_count() == 1 for a, b in m)
    holes = V - {q for e in m for q in e}
    assert holes == set(c['holes']) and len(holes) == 4 and u in holes
    assert (u.bit_count()-v.bit_count()) % 2 == 1
    assert tuple(sorted((v, h))) in m
    star = matching(c['M_star'])
    assert star == m - {tuple(sorted((v, h)))} | {tuple(sorted((u, h)))}
    a_side = {q for q in V if (q >> cut) & 1 == (v >> cut) & 1}
    b_side = V - a_side
    ma = {e for e in star if set(e) <= a_side}
    mb = {e for e in star if set(e) <= b_side}
    cross = star - ma - mb
    assert cross == matching(c['cross_star']) and len(cross) >= 9
    assert not halves(ma, a_side, cut)
    old_cut = c['initial_cut']
    old_a = {q for q in V if (q >> old_cut) & 1 == (v >> old_cut) & 1}
    old_ma = {e for e in star if set(e) <= old_a}
    old_h = halves(old_ma, old_a, old_cut)
    assert any(j == cut for j, _ in old_h)
    a, b, k = (c[q] for q in ('a', 'b', 'k'))
    d = matching(c['D'])
    tb = matching(c['T_b'])
    bk, ak = tuple(sorted((b, k))), tuple(sorted((a, k)))
    assert bk in ma and tb == (ma - {bk}) | d | {ak}
    assert not halves(tb, a_side, cut)
    sequence(c['C_A0'], a_side - {v, b}, tb, cycle=True)
    ka = c['K_A']
    assert ka[0] == a and ka[-1] == b
    kae = sequence(ka, a_side - {v}, ma | d)
    segs = c['transferred_paths']
    assert len({q for p in segs for q in p[1:-1]}) == sum(len(p)-2 for p in segs)
    assert {q for p in segs for q in p[1:-1]} == a_side - {v}
    assert all(p[0] in b_side and p[-1] in b_side for p in segs)
    assert len({q for p in segs for q in (p[0], p[-1])}) == 2*len(segs)
    transferred = set().union(*(edges(p) for p in segs))
    bridge = tuple(sorted((b, b ^ (1 << cut))))
    assert transferred == (kae-d) | cross | {bridge}
    r = {tuple(sorted((p[0], p[-1]))) for p in segs}
    lb = matching(c['L_B'])
    assert lb == mb | r
    cb = sequence(c['C_B'], b_side, lb, cycle=True)
    global_edges = sequence(c['C_global'], V-{v}, star, cycle=True)
    assert global_edges == (cb-r) | transferred
    pe = sequence(c['path'], V, m)
    assert c['path'][0] == u and c['path'][-1] == v
    assert pe == global_edges - {tuple(sorted((u, h)))} | {tuple(sorted((h, v)))}


if __name__ == '__main__':
    raw = (ROOT/'recut_results.json').read_bytes()
    data = json.loads(raw)
    for c in data['cases']:
        check(c)
    result = dict(status='PASS', verified=len(data['cases']),
                  scope=data['scope'], input_sha256=hashlib.sha256(raw).hexdigest(),
                  full_p6_proved=False, exhaustive_q6=False)
    (ROOT/'recut_verification.json').write_text(json.dumps(result, indent=2), encoding='utf8')
    print(json.dumps(result, indent=2))
