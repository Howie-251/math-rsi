"""Investigate E3 on full 31-cycles with one auxiliary distance-three edge.

Exact local cut/reconnect search only; no claim of exhausting E3 inputs.
"""
import itertools
import json
import random
import time

import networkx as nx

from probe_a4_local_repair import ROOT, edge, short, edges, components


def join_cycle(ps):
    first, rest = ps[0], ps[1:]
    target = first[0]
    options = [[p] if len(p) == 1 else [p, p[::-1]] for p in rest]
    dead = set()

    def walk(mask, tail):
        if not mask:
            return [] if short(tail, target) else None
        state = mask, tail
        if state in dead:
            return None
        for i, opts in enumerate(options):
            if not mask & (1 << i):
                continue
            for p in opts:
                if short(tail, p[0]):
                    suffix = walk(mask ^ (1 << i), p[-1])
                    if suffix is not None:
                        return p + suffix
        dead.add(state)
        return None

    ans = walk((1 << len(rest)) - 1, first[-1])
    return first + ans if ans is not None else None


def eliminate(c, f, aux, k):
    bad = next(i for i, x in enumerate(c) if edge(x, c[(i+1) % len(c)]) == aux)
    optional = [i for i, x in enumerate(c)
                if edge(x, c[(i+1) % len(c)]) not in f | {aux}]
    checked = 0
    for cuts in itertools.combinations(optional, k):
        checked += 1
        ps = components(c, [bad] + list(cuts))
        ans = join_cycle(ps)
        if ans is not None:
            assert len(ans) == 31 and set(ans) == set(c)
            assert f <= edges(ans) and aux not in edges(ans)
            assert all(short(*e) or e in f for e in edges(ans))
            return dict(status='FOUND', cycle=ans, checked=checked,
                        deleted_old_edges=len(edges(c)-edges(ans)),
                        optional_cut_budget=k, cut_positions=sorted([bad]+list(cuts)))
    return dict(status='EXHAUSTED', optional_cut_budget=k, checked=checked)


def sample(rng, a=0, b=7, v=1):
    vs = set(range(32)) - {v}
    while True:
        t = rng.choice(sorted(x for x in vs - {b} if x.bit_count() % 2))
        ns = [x for x in vs if short(x, t)]
        x, y = rng.sample(ns, 2)
        left = vs - {x, t, y}
        g = nx.Graph()
        g.add_nodes_from(left)
        g.add_weighted_edges_from((p, q, rng.random()) for p in sorted(left)
                                 for q in sorted(left) if p < q and short(p, q))
        pm = nx.max_weight_matching(g, maxcardinality=True)
        if len(pm) * 2 == len(left):
            break
    ps = [[x, t, y]] + [list(e) for e in sorted(edge(*e) for e in pm)]
    pa = next(p for p in ps if a in (p[0], p[-1]))
    pb = next(p for p in ps if b in (p[0], p[-1]))
    assert pa is not pb
    rest = [p for p in ps if p is not pa and p is not pb]
    rng.shuffle(rest)
    rest = [p if rng.randrange(2) else p[::-1] for p in rest]
    ps = [pa if pa[-1] == a else pa[::-1], pb if pb[0] == b else pb[::-1]] + rest
    f = {edge(p[-1], q[0]) for p, q in zip(ps, ps[1:] + ps[:1])} - {edge(a, b)}
    c = [x for p in ps for x in p]
    assert len(f) == 14 and len({x for e in f for x in e}) == 28
    assert set(range(32)) - {x for e in f for x in e} == {a, b, v, t}
    return dict(a=a, b=b, v=v, t=t, matching=sorted(f), cycle_with_aux=c)


def main():
    rng = random.Random(202611015)
    start = time.monotonic()
    cases = []
    for index in range(500):
        c = sample(rng, v=(1, 11, 31)[index % 3])
        f, aux = set(map(tuple, c['matching'])), edge(c['a'], c['b'])
        c['eliminate3'] = eliminate(c['cycle_with_aux'], f, aux, 3)
        cases.append(c)
        if c['eliminate3']['status'] == 'EXHAUSTED':
            c['eliminate4'] = eliminate(c['cycle_with_aux'], f, aux, 4)
            break
    out = dict(scope='E3 local repair search, not full input enumeration',
               seed=202611015, elapsed=time.monotonic()-start, cases=cases,
               a4_proved=False, full_p6_proved=False)
    (ROOT/'a4_edge_elimination_probe.json').write_text(json.dumps(out, indent=2), encoding='utf8')
    print(json.dumps(dict(cases=len(cases), elapsed=out['elapsed'],
                         last3=cases[-1]['eliminate3']['status'],
                         last4=cases[-1].get('eliminate4', {}).get('status'))))


if __name__ == '__main__':
    main()
