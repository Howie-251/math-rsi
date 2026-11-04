"""Construct explicit S9 witnesses using local solvers, not universal A4.

The mathematical S9 proof is conditional on A4. Solver FOUND witnesses are
checked globally and cannot discharge the universal A4 hypothesis.
"""
import json
import random
from collections import Counter

from avoided_vertex_transfer import cycle_on
from single_bridge_probe import random_maximum, verify
from split_transfer import local_path
from six_hole_geometry_census import ROOT, TABLE


def edge(a, b):
    return tuple(sorted((a, b)))


def path_edges(p):
    return {edge(a, b) for a, b in zip(p, p[1:])}


def orient(p, start):
    assert start in (p[0], p[-1])
    return p if p[0] == start else p[::-1]


def expand(p, replacement):
    out = [p[0]]
    for a, b in zip(p, p[1:]):
        segment = orient(replacement.get(edge(a, b), [a, b]), a)
        assert segment[-1] == b
        out.extend(segment[1:])
    return out


def cut_circle(c, a, b):
    at = c.index(a)
    direction = -1 if c[(at+1) % len(c)] == b else 1
    p = [c[(at+direction*j) % len(c)] for j in range(len(c))]
    assert p[-1] == b
    return p


def construct(m, u, v, i, rng):
    m = set(map(tuple, m))
    a_side = {x for x in range(64) if ((x ^ v) >> i) & 1 == 0}
    b_side = set(range(64)) - a_side
    holes = set(range(64)) - {x for e in m for x in e}
    odd_holes = sorted(x for x in holes if x.bit_count() % 2)
    other_even = sorted(holes - set(odd_holes) - {u})
    assert set(odd_holes) <= a_side and len(set(other_even) & a_side) == 1
    q = next(x for x in other_even if x in b_side)
    ma = {e for e in m if set(e) <= a_side}
    mb = {e for e in m if set(e) <= b_side}
    cross = m - ma - mb
    xa = {x for e in cross for x in e if x in a_side}
    xb = {x for e in cross for x in e if x in b_side}
    mb_mate = {a: b for e in mb for a, b in (e, e[::-1])}
    choices = [w for w in odd_holes if w ^ (1 << i) in mb_mate]
    w = rng.choice(choices)
    y = w ^ (1 << i)
    start_a = u if u in a_side else rng.choice(sorted(x for x in xa if x.bit_count() % 2 == 0))
    free = sorted((xa - {start_a}) | {w}) if u in b_side else sorted(xa | {w})
    rng.shuffle(free)
    d = {edge(x, z) for x, z in zip(free[::2], free[1::2])}
    la = ma | d
    ra = local_path(6, i, (v >> i) & 1, sorted(la), start_a, v)
    if ra['status'] != 'FOUND':
        return dict(status='UNKNOWN_A')
    ka = ra['path']
    forest = (path_edges(ka) - d) | cross | {edge(w, y)}
    adj = {}
    for x, z in forest:
        adj.setdefault(x, []).append(z)
        adj.setdefault(z, []).append(x)
    expected = xb | {y, v} | ({u} if u in a_side else set())
    assert {x for x, ns in adj.items() if len(ns) == 1} == expected
    assert all(len(ns) in (1, 2) for ns in adj.values())
    seen, segments = set(), []
    for x in sorted(expected):
        if x in seen:
            continue
        p = [x]
        while True:
            options = [z for z in adj[p[-1]] if len(p) == 1 or z != p[-2]]
            if not options:
                break
            assert len(options) == 1
            p.append(options[0])
        seen.update(p)
        segments.append(p)
    assert seen == set(adj)
    tv = orient(next(p for p in segments if v in (p[0], p[-1])), v)[::-1]
    tu = orient(next(p for p in segments if u in (p[0], p[-1])), u) if u in a_side else None
    middle = [p for p in segments if p is not None and v not in (p[0], p[-1])
              and (u in b_side or u not in (p[0], p[-1]))]
    replacement = {edge(p[0], p[-1]): p for p in middle}
    rmatch = set(replacement)
    end_v = tv[0]
    start_b = u if u in b_side else tu[-1]
    base = dict(matching=sorted(m), u=u, v=v, cut=i, holes=sorted(holes),
                root_side='B' if u in b_side else 'A', target_is_cross_port=v in xa,
                w=w, y=y, D=sorted(d), K_A=ka, transferred_paths=segments,
                R=sorted(rmatch), T_v=tv, T_u=tu)
    if y in (start_b, end_v):
        lb = mb | rmatch
        root = start_b if u in b_side else next(x for x in (start_b, end_v) if x != y)
        rb = local_path(6, i, 1-((v >> i) & 1), sorted(lb), root, y)
        if rb['status'] != 'FOUND':
            return dict(base, status='UNKNOWN_B')
        kb = orient(rb['path'], start_b)
        mode = base['root_side'] + '_terminal_y'
        base.update(L_B=sorted(lb), K_B=kb)
    else:
        k = mb_mate[y]
        yp = next(p for e, p in replacement.items() if y in e)
        dd = yp[-1] if yp[0] == y else yp[0]
        fb = (mb - {edge(y, k)}) | (rmatch - {edge(y, dd)}) | {edge(k, dd)}
        aux = edge(start_b, end_v)
        lb = fb | {aux}
        assert aux not in fb
        rb = cycle_on(b_side - {y}, lb)
        if rb['status'] != 'FOUND':
            return dict(base, status='UNKNOWN_B')
        kb = cut_circle(rb['cycle'], start_b, end_v)
        replacement.pop(edge(y, dd))
        replacement[edge(k, dd)] = [k] + orient(yp, y)
        mode = base['root_side'] + '_conflict_y'
        base.update(F_B=sorted(fb), L_B=sorted(lb), auxiliary_edge=aux,
                    C_B=rb['cycle'], K_B=kb, repair_edge=edge(k, dd))
    middle_expanded = expand(kb, replacement)
    full = middle_expanded if u in b_side else tu + middle_expanded[1:]
    full += tv[1:]
    verify(6, sorted(m), u, v, full)
    return dict(base, status='FOUND', mode=mode, path=full)


def main():
    rng = random.Random(202611017)
    cases = []
    for name, w in TABLE.items():
        r = w[0] & 3
        target = 4 if r == 0 else 1
        for u in ([12, 10] if r == 0 else [5, 6]):
            for trial in range(2):
                m = random_maximum(6, {0, 3, u, *w}, rng)
                assert len(m) == 29
                result = construct(m, u, target, 1 if r == 0 and u == 10 else 0, rng)
                cases.append(dict(type=name, trial=trial, **result))
                print(name, u, trial, result['status'], result.get('mode'), result.get('target_is_cross_port'), flush=True)
    out = dict(scope='S9 constructive examples, not proof of A4 or exhaustive matchings',
               cases=cases, a4_proved=False, full_p6_proved=False)
    (ROOT/'six_hole_clustered_results.json').write_text(json.dumps(out, indent=2), encoding='utf8')
    print(json.dumps(dict(statuses=dict(Counter(c['status'] for c in cases)),
                          modes=dict(Counter(c.get('mode') for c in cases))), indent=2))


if __name__ == '__main__':
    main()
