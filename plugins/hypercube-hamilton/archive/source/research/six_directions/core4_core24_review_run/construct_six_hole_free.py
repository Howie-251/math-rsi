"""Explicit witnesses for the six free-endpoint transfer branches.

Local MILPs supply the individual A4/K4 calls; they do not prove A4.
"""
import json
import random
from collections import Counter

from construct_six_hole_clustered import edge, path_edges, orient, expand, cut_circle
from avoided_vertex_transfer import cycle_on
from single_bridge_probe import random_maximum, verify
from split_transfer import local_path
from six_hole_geometry_census import ROOT


def construct(raw, u, v, i, rng):
    m = set(map(tuple, raw))
    holes = set(range(64)) - {x for e in m for x in e}
    assert u in holes and v in holes
    aa = {x for x in range(64) if ((x ^ v) >> i) & 1 == 0}
    bb = set(range(64)) - aa
    evens = holes - {x for x in holes if x.bit_count() % 2} - {u}
    assert len(evens & aa) == len(evens & bb) == 1
    z, q = next(iter(evens & aa)), next(iter(evens & bb))
    other_odd = {x for x in holes if x.bit_count() % 2} - {v}
    kshape = len(other_odd & aa)
    ma = {e for e in m if set(e) <= aa}
    mb = {e for e in m if set(e) <= bb}
    cross = m - ma - mb
    assert cross
    xa = {x for e in cross for x in e if x in aa}
    xb = {x for e in cross for x in e if x in bb}
    mb_mate = {a: b for e in mb for a, b in (e, e[::-1])}
    start_a = u if u in aa else rng.choice(sorted(x for x in xa if x.bit_count() % 2 == 0))
    bridge_a = None
    if kshape == 0:
        bridge_a = z
    elif kshape == 2:
        bridge_a = rng.choice(sorted(w for w in other_odd if w ^ (1 << i) in mb_mate))
    y = bridge_a ^ (1 << i) if bridge_a is not None else None
    if y is not None:
        assert y in mb_mate
    free = (xa - {start_a}) if u in bb else set(xa)
    if bridge_a is not None:
        free.add(bridge_a)
    free = sorted(free)
    rng.shuffle(free)
    d = {edge(a, b) for a, b in zip(free[::2], free[1::2])}
    assert 2*len(d) == len(free)
    la = ma | d
    ra = local_path(6, i, (v >> i) & 1, sorted(la), start_a, v)
    if ra['status'] != 'FOUND':
        return dict(status='UNKNOWN_A')
    ka = ra['path']
    forest = (path_edges(ka) - d) | cross
    if y is not None:
        forest.add(edge(bridge_a, y))
    adj = {}
    for a, b in forest:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    endpoints_b = xb | ({y} if y is not None else set())
    endpoints = endpoints_b | {v} | ({u} if u in aa else set())
    assert {x for x, ns in adj.items() if len(ns) == 1} == endpoints
    seen, segments = set(), []
    for start in sorted(endpoints):
        if start in seen:
            continue
        p = [start]
        while True:
            ns = [x for x in adj[p[-1]] if len(p) == 1 or x != p[-2]]
            if not ns:
                break
            assert len(ns) == 1
            p.append(ns[0])
        seen.update(p)
        segments.append(p)
    assert seen == set(adj)
    tv = orient(next(p for p in segments if v in (p[0], p[-1])), v)[::-1]
    tu = orient(next(p for p in segments if u in (p[0], p[-1])), u) if u in aa else None
    middle = [p for p in segments if v not in (p[0], p[-1])
              and (u in bb or u not in (p[0], p[-1]))]
    repl = {edge(p[0], p[-1]): p for p in middle}
    rr = set(repl)
    start_b, end_b = (u if u in bb else tu[-1]), tv[0]
    base = dict(matching=sorted(m), holes=sorted(holes), u=u, v=v, cut=i,
                root_side='A' if u in aa else 'B', shape=kshape, bridge_a=bridge_a, y=y,
                D=sorted(d), K_A=ka, transferred_paths=segments, R=sorted(rr), T_u=tu, T_v=tv)
    if y is None:
        fb = mb | rr
        aux = edge(start_b, end_b)
        lb = fb | {aux}
        rb = cycle_on(bb, lb)
        if rb['status'] != 'FOUND':
            return dict(base, status='UNKNOWN_B')
        kb = cut_circle(rb['cycle'], start_b, end_b)
        mode = 'NC_full_circle'
        base.update(F_B=sorted(fb), L_B=sorted(lb), auxiliary_edge=aux, C_B=rb['cycle'])
    elif y in (start_b, end_b):
        lb = mb | rr
        b = next(x for x in (start_b, end_b) if x != y)
        if kshape == 0 and u in aa:
            mate = mb_mate[y]
            tb = (lb - {edge(y, mate)}) | {edge(mate, b)}
            rb = cycle_on(bb - {y}, tb)
            if rb['status'] != 'FOUND':
                return dict(base, status='UNKNOWN_B')
            kb = cut_circle(rb['cycle'], b, mate) + [y]
            kb = orient(kb, start_b)
            mode = 'A4_terminal_rotation'
            base.update(L_B=sorted(lb), T_B=sorted(tb), C_B=rb['cycle'], terminal_mate=mate)
        else:
            rb = local_path(6, i, 1-((v >> i) & 1), sorted(lb), b, y)
            if rb['status'] != 'FOUND':
                return dict(base, status='UNKNOWN_B')
            kb = orient(rb['path'], start_b)
            mode = 'K4_terminal_path' if kshape == 0 else 'N10_terminal_path'
            base.update(L_B=sorted(lb))
    else:
        mate = mb_mate[y]
        segment = next(p for e, p in repl.items() if y in e)
        dd = segment[-1] if segment[0] == y else segment[0]
        fb = (mb - {edge(y, mate)}) | (rr - {edge(y, dd)}) | {edge(mate, dd)}
        aux = edge(start_b, end_b)
        lb = fb | {aux}
        rb = cycle_on(bb - {y}, lb)
        if rb['status'] != 'FOUND':
            return dict(base, status='UNKNOWN_B')
        kb = cut_circle(rb['cycle'], start_b, end_b)
        repl.pop(edge(y, dd))
        repl[edge(mate, dd)] = [mate] + orient(segment, y)
        mode = 'A4_conflict_circle' if kshape == 0 else 'N14_conflict_circle'
        base.update(F_B=sorted(fb), L_B=sorted(lb), auxiliary_edge=aux,
                    C_B=rb['cycle'], repair_edge=edge(mate, dd))
    middle_path = expand(kb, repl)
    full = middle_path if u in bb else tu + middle_path[1:]
    full += tv[1:]
    verify(6, sorted(m), u, v, full)
    return dict(base, K_B=kb, path=full, mode=mode, status='FOUND')


def main():
    rng = random.Random(202611018)
    cases = []
    for odd_holes, target in [((13, 22, 41), 22), ((13, 22, 41), 13), ((13, 21, 37), 13)]:
        for u in (5, 6):
            for trial in range(3):
                m = random_maximum(6, {0, 3, u, *odd_holes}, rng)
                assert len(m) == 29
                result = construct(m, u, target, 0, rng)
                cases.append(dict(trial=trial, **result))
                print(result.get('shape'), result.get('root_side'), trial, result['status'], result.get('mode'), flush=True)
    out = dict(scope='six free-endpoint branch constructions, not exhaustive and not A4 proof',
               cases=cases, a4_proved=False, full_p6_proved=False)
    (ROOT/'six_hole_free_transfer_results.json').write_text(json.dumps(out, indent=2), encoding='utf8')
    print(json.dumps(dict(statuses=dict(Counter(c['status'] for c in cases)),
                         modes=dict(Counter(c.get('mode') for c in cases))), indent=2))


if __name__ == '__main__':
    main()
