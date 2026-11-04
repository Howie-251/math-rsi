"""Construct Z6/Z7 witnesses. Bounded solvers supply paths, never proof of coverage."""
import json
import random
from collections import Counter
from pathlib import Path
from split_transfer import local_path
from single_bridge_probe import random_maximum, verify

ROOT = Path(__file__).resolve().parent


def edge(a, b):
    return tuple(sorted((a, b)))


def path_edges(path):
    return {edge(a, b) for a, b in zip(path, path[1:])}


def half_layers(matching, vertices, coordinates):
    present = {edge(*e) for e in matching}
    return [(j, parity) for j in coordinates for parity in (0, 1)
            if {edge(a, a ^ (1 << j)) for a in vertices
                if not a & (1 << j)
                and (a & ~(1 << j)).bit_count() % 2 == parity} <= present]


def prepare_core(matching, chosen_odd_hole=None, odd_holes=(13, 49), choose_root_pair=False):
    m = [edge(*e) for e in matching]
    assert set(range(64)) - {q for e in m for q in e} == {0, 3, *odd_holes}
    assert len(m) == 30 and all((a ^ b).bit_count() == 1 for a, b in m)
    ma = [e for e in m if all(q % 2 == 0 for q in e)]
    mb = [e for e in m if all(q % 2 == 1 for q in e)]
    cross = [e for e in m if e[0] ^ e[1] == 1]
    xa = sorted(q for e in cross for q in e if q % 2 == 0)
    free = xa + [0]
    ev = sorted(q for q in free if q.bit_count() % 2 == 0)
    od = sorted(q for q in free if q.bit_count() % 2 == 1)
    assert len(ev) == len(od)
    auxiliary = [edge(a, b) for a, b in zip(ev, od)]
    if choose_root_pair:
        assert len(xa) >= 3
        ma_mate = {a: b for e in ma for a, b in (e, e[::-1])}
        forbidden = 2 ^ ma_mate[2]
        partner = next(a for a in od if a != forbidden)
        auxiliary = [edge(0, partner)] + [edge(a, b) for a, b in
                    zip([a for a in ev if a != 0], [b for b in od if b != partner])]
    pa = ma + auxiliary
    mate = {a: b for e in pa for a, b in (e, e[::-1])}
    options = []
    for t in odd_holes:
        c, d = 2, t ^ 1
        compressed = [e for e in pa if c not in e and d not in e]
        compressed.append(edge(mate[c], mate[d]))
        obstacles = half_layers(compressed, range(0, 64, 2), range(1, 6))
        options.append(dict(t=t, d=d, half_layers=obstacles))
    eligible = [o for o in options if not o['half_layers']]
    assert eligible, 'E1/Z7 would be contradicted'
    choice = next((o for o in eligible if o['t'] == chosen_odd_hole), eligible[0])
    t, d = choice['t'], choice['d']
    w = next(q for q in odd_holes if q != t)
    result = local_path(6, 0, 0, pa, 2, d)
    if result['status'] != 'FOUND':
        return dict(status='UNKNOWN_A', solver=result)
    ka = result['path']
    adj = {q: [] for q in ka}
    for a, b in path_edges(ka) - set(auxiliary):
        adj[a].append(b)
        adj[b].append(a)
    assert {q for q in ka if len(adj[q]) == 1} == set(xa) | {0, 2, d}
    seen, transferred = set(), []
    for start in sorted(q for q in ka if len(adj[q]) == 1):
        if start in seen:
            continue
        p = [start]
        while True:
            following = [q for q in adj[p[-1]] if len(p) == 1 or q != p[-2]]
            if not following:
                break
            assert len(following) == 1
            p.append(following[0])
        seen.update(p)
        if p[0] != 0:
            p = [p[0] ^ 1] + p
        if p[-1] != 0:
            p += [p[-1] ^ 1]
        transferred.append(p)
    assert seen == set(ka)
    prefix = next(p if p[0] == 0 else p[::-1]
                  for p in transferred if 0 in (p[0], p[-1]))
    q = prefix[-1]
    assert q == t or q.bit_count() % 2 == 0
    rp = {edge(p[0], p[-1]): p for p in transferred if 0 not in (p[0], p[-1])}
    lb = mb + list(rp)
    assert len(lb) == 15 and len({a for e in lb for a in e}) == 30
    assert set(range(1, 64, 2)) - {a for e in lb for a in e} == {q, w}
    return dict(status='PREPARED', matching=m, u=0, t=t, w=w, q=q,
                endpoint_choices=options, D=auxiliary, P_A=pa, K_A=ka,
                transferred_paths=transferred, prefix=prefix, L_B=lb)


def finish(prepared, v):
    assert prepared['status'] == 'PREPARED'
    assert v % 2 == 1 and v.bit_count() % 2 == 1
    assert v not in (3, prepared['w'], prepared['t'])
    q = prepared['q']
    result = local_path(6, 0, 1, prepared['L_B'], q, v)
    if result['status'] != 'FOUND':
        return dict(status='UNKNOWN_B', v=v, solver=result)
    kb = result['path']
    rp = {edge(p[0], p[-1]): p for p in prepared['transferred_paths']
          if 0 not in (p[0], p[-1])}
    final = list(prepared['prefix'])
    for a, b in zip(kb, kb[1:]):
        p = rp.get(edge(a, b), [a, b])
        if p[0] != a:
            p = p[::-1]
        assert p[-1] == b
        final += p[1:]
    verify(6, prepared['matching'], 0, v, final)
    return dict(prepared, status='FOUND', v=v, K_B=kb, path=final)


def main():
    rng = random.Random(20261108)
    saved = json.loads((ROOT / 'unbalanced_four_hole_core.json').read_text(encoding='utf8'))
    matchings = [saved['matching']]
    for _ in range(19):
        m = random_maximum(6, {0, 3, 13, 49}, rng)
        assert len(m) == 30
        matchings.append(m)
    out = []
    for index, m in enumerate(matchings):
        prepared = prepare_core(m, (13, 49)[index % 2])
        if prepared['status'] != 'PREPARED':
            out.append(dict(prepared, sample=index))
            continue
        targets = [v for v in range(1, 64, 2)
                   if v.bit_count() % 2 == 1 and v not in (13, 49)] if index == 0 else [61]
        for v in targets:
            result = finish(prepared, v)
            out.append(dict(result, sample=index))
            (ROOT / 'unbalanced_transfer_results.json').write_text(
                json.dumps({'scope': '20 fixed/random matchings of one hole geometry; not exhaustive',
                            'cases': out}, indent=2), encoding='utf8')
            print(index, v, result['status'], 'q=', prepared['q'], flush=True)
    print(dict(Counter(c['status'] for c in out)), flush=True)


if __name__ == '__main__':
    main()
