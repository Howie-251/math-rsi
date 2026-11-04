"""Construct Z9 after arbitrary coordinate recuts. Witnesses, not exhaustion."""
import json
import random
from pathlib import Path

from avoided_vertex_transfer import complete_without_half, cycle_on
from single_bridge_probe import random_maximum, verify
from split_transfer import local_path
from unbalanced_transfer import edge, path_edges, half_layers

ROOT = Path(__file__).resolve().parent
V = set(range(64))


def construct(matching, u, v, cut):
    m = {edge(*p) for p in matching}
    holes = V - {q for p in m for q in p}
    assert len(holes) == 4 and u in holes and v not in holes
    assert u.bit_count() % 2 == 0 and v.bit_count() % 2 == 1
    z = next(q for q in holes - {u} if q.bit_count() % 2 == 0)
    odd = sorted(holes - {u, z})
    mate = {a: b for p in m for a, b in (p, p[::-1])}
    h = mate[v]
    star = m - {edge(v, h)} | {edge(u, h)}
    side = (v >> cut) & 1
    a_side = {q for q in V if (q >> cut) & 1 == side}
    b_side = V - a_side
    assert {z, *odd} <= b_side
    ma = {p for p in star if set(p) <= a_side}
    mb = {p for p in star if set(p) <= b_side}
    cross = star - ma - mb
    cross_map = {a: b for p in cross for a, b in (p, p[::-1]) if a in a_side}
    xa = set(cross_map)
    am = {a: b for p in ma for a, b in (p, p[::-1])}
    coordinates = [i for i in range(6) if i != cut]
    chosen = None
    for w in odd:
        b = w ^ (1 << cut)
        if b not in am:
            continue
        k = am[b]
        f = ma - {edge(b, k)}
        if half_layers(f, a_side, coordinates):
            continue
        completion = set(complete_without_half(f, xa | {k}))
        tb = f | completion
        if half_layers(tb, a_side, coordinates):
            continue
        a = next(q for p in completion if k in p for q in p if q != k)
        d = completion - {edge(a, k)}
        chosen = w, b, k, a, d, tb
        break
    if chosen is None:
        return dict(status='NO_Z9_CONDITION', cut=cut, u=u, v=v)
    w, b, k, a, d, tb = chosen
    result = cycle_on(a_side - {v, b}, tb)
    if result['status'] != 'FOUND':
        return dict(status='UNKNOWN_A', cut=cut, u=u, v=v, solver=result)
    c0 = result['cycle']
    pos = c0.index(a)
    step = -1 if c0[(pos + 1) % len(c0)] == k else 1
    assert c0[(pos - step) % len(c0)] == k
    ka = [c0[(pos + step*j) % len(c0)] for j in range(len(c0))] + [b]
    adj = {q: [] for q in ka}
    for p, q in path_edges(ka) - d:
        adj[p].append(q)
        adj[q].append(p)
    assert {q for q in ka if len(adj[q]) == 1} == xa | {b}
    seen, transferred = set(), []
    for start in sorted(q for q in ka if len(adj[q]) == 1):
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
        ends = [w if q == b else cross_map[q] for q in (p[0], p[-1])]
        transferred.append([ends[0]] + p + [ends[1]])
    assert seen == a_side - {v}
    rp = {edge(p[0], p[-1]): p for p in transferred}
    lb = mb | set(rp)
    t = next(q for q in odd if q != w)
    assert b_side - {q for p in lb for q in p} == {z, t}
    neighbor = z ^ (1 << next(i for i in range(6) if i != cut))
    result = local_path(6, cut, 1-side, sorted(lb), z, neighbor)
    if result['status'] != 'FOUND':
        return dict(status='UNKNOWN_B', cut=cut, u=u, v=v, solver=result)
    cb = result['path']
    cyc = [cb[0]]
    for p, q in zip(cb, cb[1:] + cb[:1]):
        segment = rp.get(edge(p, q), [p, q])
        if segment[0] != p:
            segment = segment[::-1]
        cyc += segment[1:]
    assert cyc[-1] == cyc[0]
    cyc.pop()
    pos = cyc.index(u)
    step = -1 if cyc[(pos + 1) % len(cyc)] == h else 1
    assert cyc[(pos - step) % len(cyc)] == h
    path = [cyc[(pos + step*j) % len(cyc)] for j in range(len(cyc))] + [v]
    verify(6, sorted(m), u, v, path)
    return dict(status='FOUND', u=u, v=v, h=h, cut=cut, holes=sorted(holes),
                matching=sorted(m), M_star=sorted(star), cross_star=sorted(cross),
                b=b, k=k, a=a, D=sorted(d), T_b=sorted(tb), C_A0=c0, K_A=ka,
                transferred_paths=transferred, L_B=sorted(lb), C_B=cb,
                C_global=cyc, path=path)


def planted_obstacle(extra_cross_pairs=()):
    """Initial cut 0 fails E3 with direction 2; cut 2 must remove it."""
    rng = random.Random(20261112 + len(extra_cross_pairs))
    holes = {0, 3, 25, 41}
    ports = {4, *(q for p in extra_cross_pairs for q in p)}
    assert not ({q ^ 1 for q in ports} & holes), 'A cross edge must avoid the B holes'
    ma = {edge(q, q ^ 4) for q in range(0, 64, 2)
          if not q & 4 and q != 0 and q not in ports and q ^ 4 not in ports}
    cross = {edge(q, q ^ 1) for q in ports}
    missing_b = {q >> 1 for q in {3, 25, 41} | {q ^ 1 for q in ports}}
    mb = {edge(2*a+1, 2*b+1) for a, b in random_maximum(5, missing_b, rng)}
    m = ma | cross | mb
    assert len(m) == 30 and V - {q for p in m for q in p} == holes
    return m


def main():
    out = []
    for pairs in ((), ((10, 14),), ((10, 14), (18, 22))):
        m = planted_obstacle(pairs)
        for v in (4, 28, 44):
            first = construct(m, 0, v, 0)
            assert first['status'] == 'NO_Z9_CONDITION', first
            result = construct(m, 0, v, 2)
            out.append(dict(result, initial_cut=0, initial_status=first['status']))
            (ROOT/'recut_results.json').write_text(json.dumps(dict(
                scope='Nine planted E3 obstructions resolved by E2/Z11; not exhaustive Q6',
                cases=out), indent=2), encoding='utf8')
            print(len(out), v, result['status'], flush=True)


if __name__ == '__main__':
    main()
