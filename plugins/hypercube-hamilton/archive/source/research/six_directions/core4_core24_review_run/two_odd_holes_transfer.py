"""Z14 arbitrary-port-pairing construction, with explicit cycle certificates."""
import json
import random
from pathlib import Path

from avoided_vertex_transfer import cycle_on
from single_bridge_probe import random_maximum, verify
from unbalanced_transfer import edge, path_edges

ROOT = Path(__file__).resolve().parent
V = set(range(64))


def construct(matching, v, cut):
    m = {edge(*p) for p in matching}
    holes = V - {q for p in m for q in p}
    assert 0 in holes and len(holes) == 4
    assert v.bit_count() % 2 == 1 and v not in holes
    z = next(q for q in holes-{0} if q.bit_count() % 2 == 0)
    odds = sorted(holes-{0, z})
    mate = {a: b for p in m for a, b in (p, p[::-1])}
    h = mate[v]
    star = m - {edge(v, h)} | {edge(0, h)}
    side = (v >> cut) & 1
    a_side = {q for q in V if (q >> cut) & 1 == side}
    b_side = V - a_side
    assert z in b_side and len(set(odds) & a_side) == 1
    ma = {p for p in star if set(p) <= a_side}
    mb = {p for p in star if set(p) <= b_side}
    cross = star - ma - mb
    cross_map = {a: b for p in cross for a, b in (p, p[::-1]) if a in a_side}
    xa = sorted(cross_map)
    assert len(xa) % 2 == 0
    if not xa:
        return dict(status='FIVE_DIRECTION_BRANCH', v=v, cut=cut)
    d = {edge(a, b) for a, b in zip(xa[::2], xa[1::2])}
    la = ma | d
    result = cycle_on(a_side-{v}, la)
    if result['status'] != 'FOUND':
        return dict(status='UNKNOWN_A', v=v, cut=cut, solver=result)
    ca = result['cycle']
    forest = path_edges(ca) | {edge(ca[-1], ca[0])}
    forest -= d
    adj = {q: [] for q in ca}
    for a, b in forest:
        adj[a].append(b)
        adj[b].append(a)
    assert {q for q in ca if len(adj[q]) == 1} == set(xa)
    seen, transferred = set(), []
    for start in xa:
        if start in seen:
            continue
        p = [start]
        while True:
            nxt = [q for q in adj[p[-1]] if len(p) == 1 or q != p[-2]]
            if not nxt:
                break
            assert len(nxt) == 1
            p.append(nxt[0])
        seen.update(p)
        transferred.append([cross_map[p[0]]] + p + [cross_map[p[-1]]])
    assert seen == a_side-{v}
    rp = {edge(p[0], p[-1]): p for p in transferred}
    lb = mb | set(rp)
    result = cycle_on(b_side, lb)
    if result['status'] != 'FOUND':
        return dict(status='UNKNOWN_B', v=v, cut=cut, solver=result)
    cb = result['cycle']
    cyc = [cb[0]]
    for a, b in zip(cb, cb[1:]+cb[:1]):
        p = rp.get(edge(a, b), [a, b])
        if p[0] != a:
            p = p[::-1]
        cyc += p[1:]
    assert cyc[-1] == cyc[0]
    cyc.pop()
    pos = cyc.index(0)
    step = -1 if cyc[(pos+1) % len(cyc)] == h else 1
    assert cyc[(pos-step) % len(cyc)] == h
    path = [cyc[(pos+step*j) % len(cyc)] for j in range(len(cyc))] + [v]
    verify(6, sorted(m), 0, v, path)
    return dict(status='FOUND', u=0, v=v, h=h, z=z, cut=cut, holes=sorted(holes),
                matching=sorted(m), M_star=sorted(star), cross_star=sorted(cross),
                D=sorted(d), L_A=sorted(la), C_A=ca, transferred_paths=transferred,
                L_B=sorted(lb), C_B=cb, C_global=cyc, path=path,
                root_side='A' if 0 in a_side else 'B',
                artificial_cross=edge(0, h) in cross)


def main():
    rng = random.Random(20261113)
    out = []
    for holes in ({0, 63, 7, 56}, {0, 3, 28, 31}, {0, 3, 13, 49}):
        m = random_maximum(6, holes, rng)
        assert len(m) == 30
        z = next(q for q in holes-{0} if q.bit_count() % 2 == 0)
        w, t = sorted(holes-{0, z})
        targets = [v for v in range(64) if v.bit_count() % 2 == 1 and v not in holes
                   and (v ^ z) & (w ^ t)]
        for v in targets:
            cut = next(i for i in range(6) if ((v ^ z) & (w ^ t)) & (1 << i))
            c = construct(m, v, cut)
            out.append(c)
            (ROOT/'two_odd_holes_results.json').write_text(json.dumps(dict(
                scope='Z14 constructions for three matchings, eligible targets; not exhaustive Q6',
                cases=out), indent=2), encoding='utf8')
            print(len(out), sorted(holes), v, c['status'], flush=True)


if __name__ == '__main__':
    main()
