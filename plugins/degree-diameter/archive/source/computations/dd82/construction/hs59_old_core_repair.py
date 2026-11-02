#!/usr/bin/env python3
"""Bounded exact old-core screening; no attachments or auxiliary graph search.

First check the seven requested D={(50,55),(14,q)},
A={(9,14),(38,55),(14,55)} cases. Then run ONE predefined repair family:
keep A={(38,55)}, fix the first deletion (50,55), and vary the second
deletion over the other 174 HS edges. Pin one CPU and stop within 10 CPU s.
Every label written is an original 60-vertex label; old vertex IDs need not
be consecutive. The full saved input graph has compressed 59-vertex labels.
"""
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
import json
import os
import resource
import time

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'twin59_neutral_component_run'
OUT = HERE / 'hs59_old_core_repair_run'


def edge(u, v):
    return tuple(sorted((u, v)))


def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')


def adjacency(vertices, edges):
    neighbors = {v: set() for v in vertices}
    for u, v in edges:
        assert u != v and u in neighbors and v in neighbors
        neighbors[u].add(v)
        neighbors[v].add(u)
    return neighbors


def screen(vertices, base, deleted, added):
    assert deleted <= base and not (added & base)
    assert not (deleted & added)
    edges = (base - deleted) | added
    ns = adjacency(vertices, edges)
    ports = {v: 8 - len(ns[v]) for v in vertices}
    zero = [v for v in vertices if ports[v] == 0]
    negative = [[v, ports[v]] for v in vertices if ports[v] < 0]
    forced = [
        [u, v] for u, v in combinations(vertices, 2)
        if (ports[u] == 0 or ports[v] == 0)
        and v not in ns[u] and not (ns[u] & ns[v])
    ]
    zero_capacity = [
        dict(vertex=z, old_neighbors=sorted(ns[z]),
             new_label_slot_sum=sum(ports[y] for y in ns[z]),
             required=9)
        for z in zero
    ]
    # This counts available incidences, not distinct realized labels. Passing
    # is necessary only and does not supply attachment sets.
    capacities_ok = all(x['new_label_slot_sum'] >= 9 for x in zero_capacity)
    return dict(
        deleted=sorted(deleted), added=sorted(added), old_edge_count=len(edges),
        port_sizes=ports, port_histogram=dict(sorted(Counter(ports.values()).items())),
        zero_port_vertices=zero, negative_ports=negative,
        forced_uncovered_old_pairs=forced,
        zero_port_label_capacity=zero_capacity,
        port_and_zero_old_pair_screen_pass=not negative and not forced,
        zero_port_new_label_capacity_pass=capacities_ok,
        all_recorded_necessary_conditions_pass=not negative and not forced and capacities_ok,
    ), edges


def bfs_witnesses(vertices, edges):
    """Rebuild from complete edges; independent of the local pair predicate."""
    ns = adjacency(vertices, edges)
    ports = {v: 8 - len(ns[v]) for v in vertices}
    witnesses = []
    for u in vertices:
        distances = {u: 0}
        queue = deque([u])
        while queue:
            x = queue.popleft()
            for y in ns[x]:
                if y not in distances:
                    distances[y] = distances[x] + 1
                    queue.append(y)
        for v in vertices:
            if v > u and (ports[u] == 0 or ports[v] == 0) and distances.get(v, 100) > 2:
                witnesses.append(dict(pair=[u, v], distance=distances.get(v),
                    ports=[ports[u], ports[v]], common_old_neighbors=sorted(ns[u] & ns[v]),
                    old_neighbors_u=sorted(ns[u]), old_neighbors_v=sorted(ns[v])))
    return witnesses


def main():
    started = time.process_time()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    OUT.mkdir(exist_ok=True)
    assert not (OUT / 'result.json').exists(), 'Do not repeat the completed family.'
    obstruction = json.loads((SOURCE / 'component.path2.old_core_obstruction.json').read_text())
    vertices = obstruction['old_vertices']
    old_set = set(vertices)
    lines = (SOURCE / 'component.path2.edges').read_text().splitlines()
    assert tuple(map(int, lines[0].split())) == (59, 236)
    to_original = lambda x: x + (x >= 41)
    full_edges = {edge(*(to_original(int(x)) for x in line.split())) for line in lines[1:]}
    assert len(full_edges) == 236
    old_edges = {e for e in full_edges if set(e) <= old_set}
    base = old_edges | {tuple(e) for e in obstruction['deleted_old_edges']}
    base -= {tuple(e) for e in obstruction['added_old_edges']}
    ns = adjacency(vertices, base)
    assert len(base) == 175 and all(len(ns[v]) == 7 for v in vertices)
    assert all(len(ns[u] & ns[v]) == (0 if edge(u, v) in base else 1)
               for u, v in combinations(vertices, 2))
    dump(OUT / 'base.json', dict(original_60_labels=True, vertices=vertices, edges=sorted(base)))
    original_check, _ = screen(vertices, base,
        {tuple(e) for e in obstruction['deleted_old_edges']},
        {tuple(e) for e in obstruction['added_old_edges']})
    assert original_check['forced_uncovered_old_pairs'] == obstruction['forced_uncovered_old_pairs']

    initial = []
    for q in sorted(ns[14]):
        deleted = {(50, 55), edge(14, q)}
        added = {(9, 14), (38, 55), (14, 55)}
        result, edges = screen(vertices, base, deleted, added)
        result['q'] = q
        result['bfs_failure_witnesses'] = bfs_witnesses(vertices, edges)
        assert [w['pair'] for w in result['bfs_failure_witnesses']] == result['forced_uncovered_old_pairs']
        dump(OUT / f'initial_q{q}.json', dict(original_60_labels=True,
             vertices=vertices, edges=sorted(edges), screening=result))
        initial.append(result)

    # Predeclared finite family, motivated by the common 55 failures above.
    # Undo 9-14, omit 14-55, and retain 38-55. No third deleted edge is tried.
    repaired = []
    saved_core = None
    for second in sorted(base - {(50, 55)}):
        assert time.process_time() - started < 9, 'Stop before the 10-CPU-second budget.'
        result, edges = screen(vertices, base, {(50, 55), second}, {(38, 55)})
        result['second_deleted_edge'] = second
        result['bfs_failure_witnesses'] = bfs_witnesses(vertices, edges)
        assert [w['pair'] for w in result['bfs_failure_witnesses']] == result['forced_uncovered_old_pairs']
        repaired.append(result)
        if second == (2, 14):
            assert result['all_recorded_necessary_conditions_pass']
            saved_core = dict(original_60_labels=True, vertices=vertices,
                edges=sorted(edges), screening=result,
                scope='Complete old core only; old-new attachments and H are not constructed.')
    assert len(repaired) == 174 and saved_core is not None
    dump(OUT / 'passing_core.json', saved_core)
    dump(OUT / 'enumerated_family.json', repaired)
    passed = [r for r in repaired if r['all_recorded_necessary_conditions_pass']]
    report = dict(
        source=str(SOURCE / 'component.path2.edges'),
        original_60_labels=True, restored_base_verified='50 vertices, 175 edges, 7-regular, lambda=0, mu=1',
        initial_candidates=initial,
        initial_all_fail=all(not x['all_recorded_necessary_conditions_pass'] for x in initial),
        repair_rule='Undo original addition 9-14; keep only added old edge 38-55; delete 50-55 and one other HS edge.',
        repair_family_size=len(repaired),
        negative_port_failures=sum(bool(r['negative_ports']) for r in repaired),
        zero_old_pair_failures=sum(bool(r['forced_uncovered_old_pairs']) for r in repaired),
        zero_new_capacity_failures=sum(not r['zero_port_new_label_capacity_pass'] for r in repaired),
        all_necessary_screens_pass_count=len(passed),
        passing_second_deleted_edges=[r['second_deleted_edge'] for r in passed],
        passing_zero_port_histogram=dict(Counter(len(r['zero_port_vertices']) for r in passed)),
        saved_passing_core='passing_core.json',
        solver_runs=0, attachment_search=False,
        original_source_unchanged=True, cpu_budget_seconds=10,
        threads=1, pinned_cpu=min(os.sched_getaffinity(0)), cpu_seconds=time.process_time()-started,
        scope='Necessary old-core screens only; neither a complete order-59 graph nor an exclusion of the two-deletion family.')
    dump(OUT / 'result.json', report)
    print(json.dumps({k: v for k, v in report.items() if k not in ('initial_candidates', 'passing_second_deleted_edges')}, indent=2))


if __name__ == '__main__':
    main()
