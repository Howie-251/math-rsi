"""Explore bounded edge changes of a valid 29-cycle; no universal A4 claim.

Delete k optional edges, then exhaust all short-edge reconnections of the
remaining path components and the two omitted vertices. Deleted edges may
be re-added, so exhaustion at k also excludes every repair with <= k changes.
"""
import itertools
import json
import random
import time
from pathlib import Path

import networkx as nx

ROOT = Path(__file__).resolve().parent


def edge(a, b):
    return tuple(sorted((a, b)))


def short(a, b):
    return (a ^ b).bit_count() == 1


def edges(c):
    return {edge(a, b) for a, b in zip(c, c[1:] + c[:1])}


def components(c, cuts):
    cuts = sorted(cuts)
    return [[c[j % len(c)] for j in range(i + 1, end + 1)]
            for i, end in zip(cuts, cuts[1:] + [cuts[0] + len(c)])]


def reconnect(paths, a, b):
    """Exact endpoint DFS; each retained path must appear in one orientation."""
    paths = paths + [[b]]
    options = []
    for p in paths:
        options.append([p] if len(p) == 1 else [p, p[::-1]])
    dead = set()

    def walk(mask, tail):
        if mask == 0:
            return [] if short(tail, a) else None
        state = mask, tail
        if state in dead:
            return None
        for i, opts in enumerate(options):
            if not mask & (1 << i):
                continue
            for p in opts:
                if not short(tail, p[0]):
                    continue
                suffix = walk(mask ^ (1 << i), p[-1])
                if suffix is not None:
                    return p + suffix
        dead.add(state)
        return None

    ans = walk((1 << len(paths)) - 1, a)
    return [a] + ans if ans is not None else None


def repair(c, f, a, b, k):
    optional = [i for i, x in enumerate(c)
                if edge(x, c[(i+1) % len(c)]) not in f]
    checked, viable = 0, 0
    for cuts in itertools.combinations(optional, k):
        checked += 1
        ps = components(c, cuts)
        ends = [p[0] for p in ps] + [p[-1] for p in ps]
        # Each omitted vertex needs two distinct neighbors in the final cycle.
        if any(len({x for x in ends + [b if q == a else a] if short(q, x)}) < 2
               for q in (a, b)):
            continue
        viable += 1
        ans = reconnect(ps, a, b)
        if ans is not None:
            assert len(ans) == 31 and len(set(ans)) == 31
            assert f <= edges(ans)
            assert all(short(*e) or e in f for e in edges(ans))
            assert len(edges(c) - edges(ans)) <= k
            return dict(status='FOUND', cycle=ans, cut_positions=list(cuts),
                        checked=checked, endpoint_viable=viable)
    return dict(status='EXHAUSTED', checked=checked, endpoint_viable=viable,
                cut_budget=k)


def sample(rng, a=0, b=31, v=1):
    """Generate a short forest with 13 edges and one two-edge path, then
    connect its 14 components by an arbitrary complete-graph matching."""
    vs = set(range(32)) - {a, b, v}
    while True:
        t = rng.choice(sorted(x for x in vs if x.bit_count() % 2 == b.bit_count() % 2))
        ns = [x for x in vs if short(x, t)]
        if len(ns) < 2:
            continue
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
    rng.shuffle(ps)
    ps = [p if rng.randrange(2) else p[::-1] for p in ps]
    f = {edge(p[-1], q[0]) for p, q in zip(ps, ps[1:] + ps[:1])}
    c = [x for p in ps for x in p]
    assert len(f) == 14 and len({x for e in f for x in e}) == 28
    assert set(range(32)) - {x for e in f for x in e} == {a, b, v, t}
    return dict(a=a, b=b, v=v, t=t, matching=sorted(f), cycle29=c)


def main():
    rng = random.Random(202611011)
    start = time.monotonic()
    cases = []
    for index in range(200):
        c = sample(rng, v=1 if index % 2 == 0 else 7)
        c['repair4'] = repair(c['cycle29'], set(map(tuple, c['matching'])), c['a'], c['b'], 4)
        cases.append(c)
        if c['repair4']['status'] == 'EXHAUSTED':
            print('first failed four-cut repair', index, flush=True)
            c['repair5'] = repair(c['cycle29'], set(map(tuple, c['matching'])), c['a'], c['b'], 5)
            break
    out = dict(scope='bounded repairs of explicitly constructed 29-cycles, not A4 exhaustion',
               full_p6_proved=False, a4_proved=False, seed=202611011,
               elapsed=time.monotonic()-start, cases=cases)
    (ROOT/'a4_local_repair_probe.json').write_text(json.dumps(out, indent=2), encoding='utf8')
    print(json.dumps(dict(cases=len(cases), elapsed=out['elapsed'],
                          last4=cases[-1]['repair4']['status'],
                          last5=cases[-1].get('repair5', {}).get('status'))))


if __name__ == '__main__':
    main()
