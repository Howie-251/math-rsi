# Independent finite Brown check

The following Python program reads the fixed edge list directly. It does not
import or execute the submitted C++ program. It first enumerates the possible
external members of the dominating set block by block. It then forces the
absolute vertices not already dominated by those external members. Finally it
searches only the remaining absolute and internal vertices, using ordinary
Python sets. The upper bound used is `slots * largest individual new coverage`,
not the submitted program's sum of the largest gains. Branches use disjoint
first-dominator choices; the same elementary cover argument certifies that
every possible completion is retained.

Run from the project root with the command recorded in `PROOF_AUDIT.json`.
The program writes only `INDEPENDENT_CHECK.json` in this audit directory.

```python
from pathlib import Path
from itertools import combinations, product
from time import perf_counter, process_time
import json, resource

wall_start, cpu_start = perf_counter(), process_time()
root = Path('computations/dd82/construction')
rows = [tuple(map(int, x.split())) for x in (root / 'brown57.edges').read_text().splitlines()]
assert rows[0] == (57, 224)
edge_list = rows[1:]
assert len(edge_list) == len(set(edge_list)) == 224
assert all(0 <= u < v < 57 for u, v in edge_list)
V = set(range(57))
adj = {v: set() for v in V}
for u, v in edge_list:
    adj[u].add(v)
    adj[v].add(u)
closed = {v: adj[v] | {v} for v in V}
C = {v for v in V if len(adj[v]) == 7}
I = {v for v in V - C if not adj[v] & C}
E = V - C - I
assert (len(C), len(I), len(E)) == (8, 21, 28)
assert all(len(adj[v]) == 8 for v in V - C)
assert all(adj[v] <= E for v in C)
assert all(len(adj[v] & C) == 2 and len(adj[v] & I) == 3 for v in E)
assert all(len(adj[v] & I) == len(adj[v] & E) == 4 for v in I)
triangles = [frozenset((u, v, w)) for u, v, w in combinations(sorted(V), 3)
             if v in adj[u] and w in adj[u] and w in adj[v]]
iii = [t for t in triangles if t <= I]
iee = [t for t in triangles if len(t & I) == 1 and len(t & E) == 2]
assert len(triangles) == 56 and (len(iii), len(iee)) == (14, 42)
assert all(sum(v in t for t in iii) == sum(v in t for t in iee) == 2 for v in I)
assert all(len(adj[u] & adj[v]) <= 1 for u, v in edge_list)
families = [f for f in combinations(iii, 6) if len(set().union(*f)) == 18]
assert len(families) == 14
records = []
for family_id, family in enumerate(families, 1):
    omitted = I - set().union(*family)
    assert frozenset(omitted) in iii
    H = [{m} | (adj[m] & E) for m in sorted(omitted)]
    groups = list(map(set, family)) + H
    union = set()
    for group in groups:
        assert not union & group
        union |= group
    assert not union & C
    allowed = C | union
    assert len(allowed) == 41
    group_of = {v: group for group in groups for v in group}
    external_options = []
    for block in H:
        ext = sorted(block & E)
        choices = [set()] + [{v} for v in ext]
        choices += [{u, v} for u, v in combinations(ext, 2) if v in adj[u]]
        assert len(block) == 5 and len(choices) == 7
        assert sum(v in adj[u] for u, v in combinations(sorted(block), 2)) == 6
        external_options.append(choices)
    nodes = 0
    external_cases = 0
    solutions = []

    def can_add(v, chosen):
        block = group_of.get(v)
        if block is None:
            return True
        present = chosen & block
        return len(present) < 2 and (not present or present <= adj[v])

    def visit(chosen, available, covered):
        global nodes
        nodes += 1
        slots = 8 - len(chosen)
        if slots == 0:
            if covered == V:
                solutions.append(sorted(chosen))
            return
        if len(available) < slots:
            return
        uncovered = V - covered
        if uncovered:
            max_gain = max((len(closed[v] & uncovered) for v in available), default=0)
            if slots * max_gain < len(uncovered):
                return
            choices = min((closed[u] & available for u in uncovered), key=lambda x: (len(x), sorted(x)))
            if not choices:
                return
        else:
            choices = available.copy()
        remaining = available.copy()
        for v in sorted(choices):
            remaining.remove(v)
            child = chosen | {v}
            child_avail = {w for w in remaining if can_add(w, child)}
            visit(child, child_avail, covered | closed[v])

    for pieces in product(*external_options):
        selected_external = set().union(*pieces)
        external_cases += 1
        externally_covered = set().union(*(closed[v] for v in selected_external))
        forced_absolute = C - externally_covered
        chosen = selected_external | forced_absolute
        if len(chosen) > 8:
            continue
        available = {v for v in (C | I) - chosen if can_add(v, chosen)}
        covered = set().union(*(closed[v] for v in chosen))
        visit(chosen, available, covered)
    assert external_cases == 343
    assert not solutions
    records.append({'family': family_id, 'III_triangles': [sorted(t) for t in family],
                    'omitted_III': sorted(omitted), 'external_cases': external_cases,
                    'nodes': nodes, 'dominating_8_sets': len(solutions)})
result = {'status': 'PASS', 'method': 'external-subset decomposition plus Python-set exact cover search',
          'scope': 'All 14 constrained pre-deletion Brown domination problems only',
          'families': 14, 'external_cases_total': sum(x['external_cases'] for x in records),
          'nodes_total': sum(x['nodes'] for x in records), 'dominating_8_sets': 0,
          'records': records, 'wall_seconds': perf_counter() - wall_start,
          'cpu_seconds': process_time() - cpu_start,
          'peak_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'single_process': True, 'sat_solver_calls': 0}
out = Path('reviews/dd82/proof-checker-transport-a6-butterfly-20261011/INDEPENDENT_CHECK.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'records'}))
```
