"""Explicit Z15/Z16 witnesses, including restoration of a long conflict edge."""
import json
import random
from pathlib import Path
from avoided_vertex_transfer import cycle_on, complete_without_half
from single_bridge_probe import random_maximum, verify
from unbalanced_transfer import edge, path_edges, half_layers

ROOT = Path(__file__).resolve().parent
V = set(range(64))


def construct(raw, v, cut, mode, preferred_bridge=None):
    m = {edge(*p) for p in raw}
    holes = V-{q for p in m for q in p}
    assert 0 in holes and len(holes) == 4 and v not in holes
    z = next(q for q in holes-{0} if q.bit_count() % 2 == 0)
    odd = sorted(holes-{0, z})
    mate = {a: b for p in m for a, b in (p, p[::-1])}
    h = mate[v]
    star = m-{edge(v, h)} | {edge(0, h)}
    a_side = {q for q in V if (q >> cut) & 1 == (v >> cut) & 1}
    b_side = V-a_side
    ma = {p for p in star if set(p) <= a_side}
    mb = {p for p in star if set(p) <= b_side}
    cross = star-ma-mb
    cross_map = {a: b for p in cross for a, b in (p, p[::-1]) if a in a_side}
    xa = set(cross_map)
    bm = {a: b for p in mb for a, b in (p, p[::-1])}
    if mode == 'Z15':
        assert z in b_side and set(odd) <= a_side
        candidates = [q ^ (1 << cut) for q in odd if q ^ (1 << cut) in bm]
        bridge = preferred_bridge if preferred_bridge in candidates else candidates[0]
        t = bridge ^ (1 << cut)
        free = sorted(xa | {t})
        d = {edge(a, b) for a, b in zip(free[::2], free[1::2])}
        la = ma | d
        result = cycle_on(a_side-{v}, la)
        if result['status'] != 'FOUND':
            return dict(status='UNKNOWN_A', solver=result)
        initial = result['cycle']
        initial_edges = path_edges(initial) | {edge(initial[-1], initial[0])}
        endmap = dict(cross_map, **{})
        endmap[t] = bridge
        conflict = bridge
        aux = dict(L_A=sorted(la), C_A=initial)
    else:
        assert mode == 'Z16' and z in a_side and set(odd) <= b_side
        assert len(xa) >= 2
        coords = [j for j in range(6) if j != cut]
        assert not half_layers(ma, a_side, coords)
        am = {a: b for p in ma for a, b in (p, p[::-1])}
        bridge = next(q ^ (1 << cut) for q in odd if q ^ (1 << cut) in am)
        k = am[bridge]
        f = ma-{edge(bridge, k)}
        completion = set(complete_without_half(f, xa | {z, k}))
        tb = f | completion
        assert not half_layers(tb, a_side, coords)
        a = next(q for p in completion if k in p for q in p if q != k)
        d = completion-{edge(a, k)}
        result = cycle_on(a_side-{v, bridge}, tb)
        if result['status'] != 'FOUND':
            return dict(status='UNKNOWN_A', solver=result)
        ca0 = result['cycle']
        pos = ca0.index(a)
        step = -1 if ca0[(pos+1) % len(ca0)] == k else 1
        assert ca0[(pos-step) % len(ca0)] == k
        initial = [ca0[(pos+step*j) % len(ca0)] for j in range(len(ca0))] + [bridge]
        initial_edges = path_edges(initial)
        endmap = dict(cross_map)
        endmap[bridge] = bridge ^ (1 << cut)
        endmap[z] = z ^ (1 << cut)
        conflict = z ^ (1 << cut)
        aux = dict(L_A=sorted(ma | d), K_A=initial, T_b=sorted(tb), C_A0=ca0, a=a, k=k)
    adj = {q: [] for q in initial}
    for a, b in initial_edges-d:
        adj[a].append(b)
        adj[b].append(a)
    assert {q for q in initial if len(adj[q]) == 1} == set(endmap)
    seen, transferred = set(), []
    for start in sorted(endmap):
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
        transferred.append([endmap[p[0]]] + p + [endmap[p[-1]]])
    assert seen == a_side-{v}
    rp = {edge(p[0], p[-1]): p for p in transferred}
    r = bm[conflict]
    s = next(q for p in rp if conflict in p for q in p if q != conflict)
    removed = edge(conflict, s)
    lb = mb-{edge(conflict, r)} | (set(rp)-{removed}) | {edge(r, s)}
    result = cycle_on(b_side-{conflict}, lb)
    if result['status'] != 'FOUND':
        return dict(status='UNKNOWN_B', solver=result)
    special = rp.pop(removed)
    if special[0] != conflict:
        special = special[::-1]
    rp[edge(r, s)] = [r] + special
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
    return dict(status='FOUND', mode=mode, u=0, v=v, h=h, cut=cut, z=z,
                holes=sorted(holes), matching=sorted(m), M_star=sorted(star),
                cross_star=sorted(cross), D=sorted(d), bridge=bridge,
                transferred_paths=transferred, conflict=conflict, r=r, s=s,
                L_B=sorted(lb), C_B=cb, C_global=cyc, path=path, **aux)


def main():
    tasks = []
    fixtures = json.loads((ROOT/'Z15_ALGEBRA_CHECKS.json').read_text(encoding='utf8'))
    for f in fixtures['fixtures']:
        tasks.append((f['M'], f['v'], 0, 'Z15', f['selected_b']))
    rng = random.Random(20261114)
    # An initial-cut half-layer survives, then becomes eight cross edges in cut 2.
    for z in (15, 23, 39, 51):
        holes = {0, z, 25, 41}
        if any((z ^ q).bit_count() == 1 for q in (25, 41)):
            continue
        ma = {edge(q, q ^ 4) for q in range(0, 64, 2) if not q & 4 and q != 0}
        mb = {edge(2*a+1, 2*b+1) for a, b in random_maximum(
            5, {q >> 1 for q in (z, 25, 41, 5)}, rng)}
        m = ma | mb | {(4, 5)}
        assert len(m) == 30 and V-{q for p in m for q in p} == holes
        if z & 4:
            tasks.extend((m, v, 2, 'Z16', None) for v in (4, 28, 44))
    out = []
    for m, v, cut, mode, bridge in tasks:
        result = construct(m, v, cut, mode, bridge)
        out.append(result)
        (ROOT/'conflict_cycle_results.json').write_text(json.dumps(dict(
            scope='Targeted Z15/Z16 actual cycle-expansion witnesses; not exhaustive Q6',
            cases=out), indent=2), encoding='utf8')
        print(len(out), mode, v, result['status'], flush=True)


if __name__ == '__main__':
    main()
