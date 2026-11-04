"""Bounded experiments, never an exhaustive proof. Independent witness checks inline.

Minimize the number of crossing edges with degree constraints and lazy cycle cuts.
Only integer, independently checked Hamilton paths are accepted as witnesses.
"""
import json, random, time
from pathlib import Path
import numpy as np
import networkx as nx
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csc_matrix

ROOT = Path(__file__).resolve().parent

def cube_edges(n):
    return [(a, a ^ (1 << k)) for a in range(1 << n)
            for k in range(n) if not a & (1 << k)]

def verify(n, matching, u, v, path, allowed_long=()):
    assert len(path) == 1 << n and set(path) == set(range(1 << n))
    assert path[0] == u and path[-1] == v
    edges = {tuple(sorted(e)) for e in zip(path, path[1:])}
    extra={tuple(sorted(e)) for e in allowed_long}
    assert all((a ^ b).bit_count() == 1 or (a,b) in extra for a, b in edges)
    assert {tuple(sorted(e)) for e in matching} <= edges

def solve(n, matching, u, v, cut, seconds=8, crossing_limit=None, allowed_long=()):
    size = 1 << n
    edges = cube_edges(n)
    edges += [tuple(sorted(e)) for e in allowed_long if tuple(sorted(e)) not in edges]
    count = len(edges)
    lookup = {e: j for j, e in enumerate(edges)}
    lo, hi = np.zeros(count), np.ones(count)
    for edge in matching:
        lo[lookup[tuple(sorted(edge))]] = 1
    rows = np.zeros((size, count))
    for j, (a, b) in enumerate(edges):
        rows[a, j] = rows[b, j] = 1
    degree = np.full(size, 2.)
    degree[u] = degree[v] = 1
    costs = np.array([float((a ^ b) == (1 << cut)) for a, b in edges])
    matrices = [rows]
    lbs, ubs = list(degree), list(degree)
    if crossing_limit is not None:
        matrices.append(costs[None, :]); lbs.append(0); ubs.append(crossing_limit)
    start = time.monotonic()
    rounds = 0
    while time.monotonic() - start < seconds:
        rounds += 1
        result = milp(costs, integrality=np.ones(count), bounds=Bounds(lo, hi),
                      constraints=LinearConstraint(csc_matrix(np.vstack(matrices)), lbs, ubs),
                      options={'time_limit': max(.01, seconds-time.monotonic()+start),
                               'mip_rel_gap': 0})
        if result.x is None:
            return {'status': 'SOLVER_INFEASIBLE' if result.status == 2 else 'UNKNOWN',
                    'rounds': rounds, 'solver_status': int(result.status)}
        if max(abs(result.x-np.round(result.x))) > 1e-6:
            return {'status': 'UNKNOWN', 'rounds': rounds}
        chosen = np.round(result.x).astype(int)
        assert np.array_equal(rows @ chosen, degree)
        assert np.all(chosen >= lo) and np.all(chosen <= hi)
        if crossing_limit is not None:
            assert costs @ chosen <= crossing_limit
        graph = nx.Graph(); graph.add_nodes_from(range(size))
        graph.add_edges_from(edge for j, edge in enumerate(edges) if chosen[j])
        components = list(nx.connected_components(graph))
        if len(components) == 1:
            path = [u]
            while path[-1] != v:
                nxt = [z for z in graph[path[-1]] if len(path) == 1 or z != path[-2]]
                assert len(nxt) == 1
                path.append(nxt[0])
            verify(n, matching, u, v, path, allowed_long)
            return {'status': 'FOUND', 'path': path, 'crossings': int(costs @ chosen),
                    'solver_optimal': result.status == 0, 'rounds': rounds}
        for component in components:
            if u in component:
                continue
            row = np.array([float(a in component and b in component) for a,b in edges])
            matrices.append(row[None, :]); lbs.append(-np.inf); ubs.append(len(component)-1)
    return {'status': 'UNKNOWN', 'rounds': rounds}

def random_maximum(n, holes, rng):
    graph = nx.Graph()
    graph.add_nodes_from(set(range(1 << n))-set(holes))
    graph.add_weighted_edges_from((a,b,rng.random()) for a,b in cube_edges(n)
                                 if a not in holes and b not in holes)
    return sorted(tuple(sorted(e)) for e in nx.max_weight_matching(graph, maxcardinality=True))

def main():
    rng = random.Random(20261101)
    cases = []
    # All sampled layers are maximum subject to their listed forbidden vertices.
    # Vary the even crossing endpoint, forced extra holes, and endpoint type.
    for index in range(96):
        w = rng.choice([z for z in range(1,32) if z.bit_count()%2 == 0])
        forbidden_a = {0,w}
        forbidden_b = {w}
        if index % 3 == 1:
            forbidden_a |= set(rng.sample(range(32), 3))
        if index % 3 == 2:
            forbidden_b |= set(rng.sample(range(32), 3))
        ma = random_maximum(5, forbidden_a, rng)
        mb = random_maximum(5, forbidden_b, rng)
        matching = ma + [(a+32,b+32) for a,b in mb] + [(w,w+32)]
        even = [z for z in range(32) if z.bit_count()%2 == 0]
        target = w+32 if index%4 == 0 else rng.choice([z for z in even if z != w])+32
        result = solve(6,matching,0,target,5,seconds=5,crossing_limit=3)
        case = {'n':6,'u':0,'v':target,'matching':matching,'cut':5,'w':w,**result}
        cases.append(case)
        (ROOT/'single_bridge_probe.json').write_text(json.dumps(cases,indent=2),encoding='utf8')
        print(index,len(matching),target,result['status'],result.get('crossings'),flush=True)
    print(json.dumps({s:sum(c['status']==s for c in cases)
                      for s in ['FOUND','UNKNOWN','SOLVER_INFEASIBLE']}))

if __name__ == '__main__':
    main()
