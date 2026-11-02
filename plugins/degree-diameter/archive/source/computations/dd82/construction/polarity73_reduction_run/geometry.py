"""GF(8) orthogonal polarity ambient graph; no deletion search or solver."""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def multiply(a, b):
    """GF(2)[t]/(t^3+t+1); integers encode polynomial coefficients."""
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 11
    return result


def dot(x, y):
    return multiply(x[0], y[0]) ^ multiply(x[1], y[1]) ^ multiply(x[2], y[2])


def main():
    out_json, out_edges = HERE / 'geometry.json', HERE / 'geometry.edges'
    assert not out_json.exists() and not out_edges.exists(), 'Preserve prior ambient diagnostic'
    # The cubic has no GF(2) root and is therefore irreducible. Check the
    # concrete arithmetic used by this small generator directly as well.
    assert all(any(multiply(a, b) == 1 for b in range(1, 8)) for a in range(1, 8))
    assert all(multiply(a, b) == multiply(b, a) for a in range(8) for b in range(8))
    points = [(1, a, b) for a in range(8) for b in range(8)]
    points += [(0, 1, a) for a in range(8)] + [(0, 0, 1)]
    assert len(points) == len(set(points)) == 73
    edges = [(a, b) for a, b in combinations(range(73), 2) if dot(points[a], points[b]) == 0]
    neighbors = [set() for _ in points]
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    absolute = {a for a, point in enumerate(points) if dot(point, point) == 0}
    assert absolute == {a for a, p in enumerate(points) if p[0] ^ p[1] ^ p[2] == 0}
    nucleus = points.index((1, 1, 1))
    outside = set(range(73)) - absolute - {nucleus}
    assert len(absolute) == 9 and len(outside) == 63 and nucleus not in absolute
    assert neighbors[nucleus] == absolute
    assert all(not (neighbors[a] & absolute) for a in absolute)
    fibers = {a: neighbors[a] - {nucleus} for a in absolute}
    assert all(len(row) == 7 for row in fibers.values())
    assert set().union(*fibers.values()) == outside
    assert sum(map(len, fibers.values())) == len(outside)
    parent = {x: a for a, row in fibers.items() for x in row}
    assert all(neighbors[x] & absolute == {parent[x]} for x in outside)
    assert all(not (neighbors[x] & fibers[parent[x]]) for x in outside)
    assert all(len(neighbors[x] & row) == int(a != parent[x])
               for x in outside for a, row in fibers.items())
    degree_counts = Counter(map(len, neighbors))
    assert degree_counts == {8: 9, 9: 64} and len(edges) == 324
    common_histogram = Counter(len(neighbors[a] & neighbors[b]) for a, b in combinations(range(73), 2))
    bad = [(a, b) for a, b in combinations(range(73), 2)
           if b not in neighbors[a] and not (neighbors[a] & neighbors[b])]
    assert max(common_histogram) == 1 and not bad
    triangles = {a: sum(y in neighbors[x] for x, y in combinations(sorted(neighbors[a]), 2))
                 for a in range(73)}
    assert all(triangles[a] == 0 for a in absolute | {nucleus})
    assert all(triangles[x] == 4 for x in outside)
    induced = {x: neighbors[x] & outside for x in outside}
    assert all(len(row) == 8 for row in induced.values())
    assert all(len(neighbors[y] & induced[x]) == 1 for x in outside for y in induced[x])
    induced_bad = [(x, y) for x, y in combinations(sorted(outside), 2)
                   if y not in induced[x] and not (induced[x] & induced[y])]
    assert len(induced_bad) == 189
    assert induced_bad == [(x, y) for x, y in combinations(sorted(outside), 2) if parent[x] == parent[y]]
    record = dict(status='VERIFIED_AMBIENT_GEOMETRY_ONLY', target_graph=False,
        field='GF(2)[t]/(t^3+t+1), bit-polynomial representation',
        n=73, edges=len(edges), degree_histogram=dict(degree_counts),
        common_neighbor_histogram=dict(common_histogram), max_common_neighbors=1,
        uncovered_original_pairs=len(bad), original_triangles=sum(triangles.values()) // 3,
        absolute_vertices=sorted(absolute), nucleus=nucleus, outside_vertices=sorted(outside),
        fibers={a: sorted(row) for a, row in sorted(fibers.items())},
        triangles_per_vertex=triangles, points=points,
        outside_induced_n=63, outside_induced_edges=sum(map(len, induced.values())) // 2,
        outside_induced_degree=8, fiber_count=9, fiber_size=7,
        all_between_fiber_blocks_perfect_matchings=True,
        outside_induced_bad_pairs=len(induced_bad),
        outside_induced_bad_pairs_are_exactly_same_fiber_pairs=True,
        deletion_sets_tested=0, solver_calls=0,
        scope='A 73-point degree9 ambient graph, not a degree8 construction or an order63 exclusion')
    out_edges.write_text(f'73 {len(edges)}\n' + ''.join(f'{a} {b}\n' for a, b in edges))
    out_json.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({key: record[key] for key in ('status', 'n', 'edges', 'degree_histogram',
        'max_common_neighbors', 'original_triangles', 'outside_induced_bad_pairs', 'solver_calls')}, indent=2))


if __name__ == '__main__':
    main()
