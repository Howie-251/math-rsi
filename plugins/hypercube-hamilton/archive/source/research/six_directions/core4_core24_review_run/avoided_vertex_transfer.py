"""N11/N12/Z9 construction for the canonical Z10 class. Not exhaustive Q6."""
import json
import random
import time
from collections import Counter
from pathlib import Path
import networkx as nx
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csc_matrix
from single_bridge_probe import random_maximum, verify
from split_transfer import local_path
from unbalanced_transfer import edge, path_edges, half_layers

ROOT = Path(__file__).resolve().parent
A = set(range(0, 64, 2))
B = set(range(1, 64, 2))


def cycle_on(vertices, matching, seconds=8):
    vertices = sorted(vertices)
    allowed = sorted({edge(a, b) for a in vertices for b in vertices
                      if a < b and (a ^ b).bit_count() == 1} | set(matching))
    rows = np.array([[float(v in e) for e in allowed] for v in vertices])
    lo = np.array([float(e in matching) for e in allowed])
    matrices, lower, upper = [rows], [2.] * len(vertices), [2.] * len(vertices)
    start = time.monotonic()
    while time.monotonic() - start < seconds:
        result = milp(np.zeros(len(allowed)), integrality=np.ones(len(allowed)),
                      bounds=Bounds(lo, np.ones(len(allowed))),
                      constraints=LinearConstraint(csc_matrix(np.vstack(matrices)), lower, upper),
                      options={'time_limit': max(.01, seconds - time.monotonic() + start)})
        if result.x is None:
            return {'status': 'SOLVER_INFEASIBLE' if result.status == 2 else 'UNKNOWN'}
        if max(abs(result.x - np.round(result.x))) > 1e-6:
            return {'status': 'UNKNOWN'}
        chosen = np.round(result.x).astype(int)
        assert np.all(rows @ chosen == 2) and np.all(chosen >= lo)
        graph = nx.Graph()
        graph.add_nodes_from(vertices)
        graph.add_edges_from(e for e, use in zip(allowed, chosen) if use)
        components = list(nx.connected_components(graph))
        if len(components) == 1:
            cyc = [vertices[0], min(graph[vertices[0]])]
            while True:
                nxt = next(v for v in graph[cyc[-1]] if v != cyc[-2])
                if nxt == cyc[0]:
                    break
                cyc.append(nxt)
            assert len(cyc) == len(vertices) and set(cyc) == set(vertices)
            return dict(status='FOUND', cycle=cyc)
        for component in components:
            matrices.append(np.array([[float(set(e) <= component) for e in allowed]]))
            lower.append(-np.inf)
            upper.append(len(component) - 1)
    return {'status': 'UNKNOWN'}


def complete_without_half(f, free):
    """The constructive three branches of N12, plus the forced size-two case."""
    free = sorted(free)
    directions = {a ^ b for a, b in f if (a ^ b).bit_count() == 1}
    pairs = [edge(a, b) for a, b in zip(free[::2], free[1::2])]
    if len(free) == 2 or len(directions) >= 2:
        return pairs
    if len(directions) == 1:
        direction = next(iter(directions))
        while any(a ^ b == direction for a, b in pairs):
            index = next(i for i, (a, b) in enumerate(pairs) if a ^ b == direction)
            other = next(i for i in range(len(pairs)) if i != index)
            x, y = pairs[index]
            p, q = pairs[other]
            pairs[index], pairs[other] = edge(x, p), edge(y, q)
        return pairs
    left, pairs = set(free), []
    while True:
        candidate = next(((a, b) for a in sorted(left) for b in sorted(left)
                          if a < b and (a ^ b).bit_count() != 1), None)
        if candidate is None:
            break
        pairs.append(candidate)
        left.difference_update(candidate)
    assert len(left) in (0, 2)
    if left:
        pairs.append(tuple(sorted(left)))
    return pairs


def construct(matching, v, preferred_b=None):
    m = {edge(*e) for e in matching}
    assert set(range(64)) - {q for e in m for q in e} == {0, 3, 13, 49}
    assert v in A and v.bit_count() % 2 == 1
    mate = {a: b for e in m for a, b in (e, e[::-1])}
    h = mate[v]
    star = (m - {edge(v, h)}) | {edge(0, h)}
    ma = {e for e in star if set(e) <= A}
    mb = {e for e in star if set(e) <= B}
    cross = star - ma - mb
    cross_map = {a: b for e in cross for a, b in (e, e[::-1]) if a in A}
    xa = set(cross_map)
    assert len(xa) % 2 == 1
    am = {a: b for e in ma for a, b in (e, e[::-1])}
    candidates = [preferred_b] if preferred_b in (12, 48) else []
    candidates += [b for b in (12, 48) if b not in candidates]
    chosen = None
    for b in candidates:
        k = am[b]
        f = ma - {edge(b, k)}
        if half_layers(f, A, range(1, 6)):
            continue
        completion = complete_without_half(f, xa | {k})
        tb = f | set(completion)
        if half_layers(tb, A, range(1, 6)):
            continue
        a = next(q for e in completion if k in e for q in e if q != k)
        d = set(completion) - {edge(a, k)}
        chosen = b, k, a, d, tb
        break
    assert chosen is not None, 'Z10 guarantees one candidate'
    b, k, a, d, tb = chosen
    la = ma | d
    result = cycle_on(A - {v, b}, tb)
    if result['status'] != 'FOUND':
        return dict(status='UNKNOWN_A', v=v, solver=result)
    c0 = result['cycle']
    pos = c0.index(a)
    step = -1 if c0[(pos + 1) % len(c0)] == k else 1
    assert c0[(pos - step) % len(c0)] == k
    ka = [c0[(pos + step*j) % len(c0)] for j in range(len(c0))] + [b]
    assert ka[-2] == k and la <= path_edges(ka)
    forest = path_edges(ka) - d
    adj = {q: [] for q in ka}
    for p, q in forest:
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
        ends = [b ^ 1 if q == b else cross_map[q] for q in (p[0], p[-1])]
        transferred.append([ends[0]] + p + [ends[1]])
    assert seen == A - {v}
    rp = {edge(p[0], p[-1]): p for p in transferred}
    lb = mb | set(rp)
    w = b ^ 1
    t = next(q for q in (13, 49) if q != w)
    assert B - {q for e in lb for q in e} == {3, t}
    result = local_path(6, 0, 1, sorted(lb), 3, 1)
    if result['status'] != 'FOUND':
        return dict(status='UNKNOWN_B', v=v, solver=result)
    cb = result['path']
    cyc = [cb[0]]
    for p, q in zip(cb, cb[1:] + cb[:1]):
        segment = rp.get(edge(p, q), [p, q])
        if segment[0] != p:
            segment = segment[::-1]
        assert segment[-1] == q
        cyc += segment[1:]
    assert cyc[-1] == cyc[0]
    cyc.pop()
    assert len(cyc) == 63 and set(cyc) == set(range(64)) - {v}
    pos = cyc.index(0)
    step = -1 if cyc[(pos + 1) % len(cyc)] == h else 1
    assert cyc[(pos - step) % len(cyc)] == h
    path = [cyc[(pos + step*j) % len(cyc)] for j in range(len(cyc))] + [v]
    verify(6, sorted(m), 0, v, path)
    return dict(status='FOUND', n=6, u=0, v=v, h=h, matching=sorted(m),
                M_star=sorted(star), cross_star=sorted(cross), b=b, k=k, a=a,
                D=sorted(d), T_b=sorted(tb), C_A0=c0, K_A=ka,
                transferred_paths=transferred, L_B=sorted(lb), C_B=cb,
                C_global=cyc, path=path,
                branch=('single' if len(cross) == 1 else 'multiple') +
                       ('_target_cross' if h in B else '_target_internal'))


def main():
    rng = random.Random(20261110)
    core = json.loads((ROOT/'unbalanced_four_hole_core.json').read_text(encoding='utf8'))
    tasks = [(core['matching'], v) for v in sorted(A) if v.bit_count() % 2 == 1]
    for _ in range(20):
        m = random_maximum(6, {0, 3, 13, 49}, rng)
        assert len(m) == 30
        tasks.append((m, rng.choice([q for q in A if q.bit_count() % 2 == 1])))
    for port in (4, 8, 16, 32, 62):
        ma = [edge(2*a, 2*b) for a, b in random_maximum(5, {0, port >> 1}, rng)]
        mb = [edge(2*a+1, 2*b+1) for a, b in random_maximum(
            5, {q >> 1 for q in (3, 13, 49, port ^ 1)}, rng)]
        m = ma + [(port, port ^ 1)] + mb
        assert len(m) == 30
        tasks.extend([(m, port), (m, 2)])
    out = []
    for index, (m, v) in enumerate(tasks):
        c = construct(m, v)
        out.append(dict(c, sample=index))
        (ROOT/'avoided_vertex_results.json').write_text(json.dumps(
            {'scope': 'canonical hole geometry, bounded constructed samples; not exhaustive Q6',
             'cases': out}, indent=2), encoding='utf8')
        print(index, v, c['status'], c.get('branch'), flush=True)
    print(dict(Counter(c.get('branch', c['status']) for c in out)))


if __name__ == '__main__':
    main()
