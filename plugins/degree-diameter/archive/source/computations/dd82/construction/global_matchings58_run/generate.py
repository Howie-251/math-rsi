"""Construct actual 58-vertex graphs through eight disjoint perfect matchings.

No SAT, local switches, restarts, or protected old edges. NetworkX's exact
integer maximum-weight matching selects each round; root owns run limits
and the independent final graph checker.
"""
import argparse
from collections import deque
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import random
import sys
import time

import networkx as nx

HERE = Path(__file__).resolve().parent
POLARITY = HERE.parent / 'polarity73_reduction_run'
SOURCE = POLARITY / 'refined/n58/deletion_candidate.json'
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('global_matching_ambient', POLARITY / 'screen.py')
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)
N = 58
SCOPE = ('Eight disjoint perfect matchings on the saved 58 surviving labels. '
         'Every old edge is optional; polarity overlap only breaks marginal-gain ties. '
         'Initial 1-factorable seed family, not all 8-regular graphs; no local search.')


def save(path, data):
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, indent=2) + '\n')
    temporary.replace(path)


def pair(x, y):
    return (x, y) if x < y else (y, x)


def bit_adjacency(n, edges):
    adj = [0] * n
    for x, y in edges:
        assert 0 <= x < y < n and not (adj[x] >> y & 1)
        adj[x] |= 1 << y
        adj[y] |= 1 << x
    return adj


def bad_pairs(adj):
    pairs, masks = [], [0] * len(adj)
    for x, y in combinations(range(len(adj)), 2):
        if not (adj[x] >> y & 1) and not (adj[x] & adj[y]):
            pairs.append((x, y))
            masks[x] |= 1 << y
            masks[y] |= 1 << x
    return pairs, masks


def single_edge_gain(adj, bad_masks, x, y):
    assert x != y and not (adj[x] >> y & 1)
    # Only pairs incident with x or y can gain coverage. These three sets
    # are disjoint because xy is currently absent and there are no loops.
    return ((bad_masks[x] >> y & 1) +
            (bad_masks[x] & adj[y]).bit_count() +
            (bad_masks[y] & adj[x]).bit_count())


def bfs_bad_pairs(n, edges):
    """Independent adjacency-list BFS used only by the small gain sanity."""
    neighbors = [[] for _ in range(n)]
    for x, y in edges:
        neighbors[x].append(y)
        neighbors[y].append(x)
    bad = []
    for x in range(n):
        distances, queue = {x: 0}, deque([x])
        while queue:
            u = queue.popleft()
            for v in neighbors[u]:
                if v not in distances:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        bad.extend((x, y) for y in range(x+1, n)
                   if y not in distances or distances[y] > 2)
    return bad


def sanity():
    cpu, wall = time.process_time(), time.monotonic()
    cases = [('empty6', 6, set()),
             ('path6', 6, {(x, x+1) for x in range(5)}),
             ('cycle6', 6, {pair(x, (x+1) % 6) for x in range(6)}),
             ('two_triangles6', 6, {(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5)}),
             ('K33', 6, {(x, y) for x in range(3) for y in range(3, 6)})]
    records = []
    for label, n, edges in cases:
        adj = bit_adjacency(n, edges)
        bad, masks = bad_pairs(adj)
        assert bad == bfs_bad_pairs(n, edges)
        checked = 0
        for x, y in combinations(range(n), 2):
            if (x, y) in edges:
                continue
            predicted = single_edge_gain(adj, masks, x, y)
            actual = len(bad) - len(bfs_bad_pairs(n, edges | {(x, y)}))
            assert predicted == actual, (label, x, y, predicted, actual)
            checked += 1
        records.append(dict(graph=label, single_edges_checked=checked))
    old, added = {(0, 1), (2, 3)}, {(0, 2), (1, 3)}
    adj = bit_adjacency(4, old)
    bad, masks = bad_pairs(adj)
    predicted = sum(single_edge_gain(adj, masks, x, y) for x, y in added)
    actual = len(bad) - len(bfs_bad_pairs(4, old | added))
    assert predicted == 6 and actual == 4
    assert 29*999 < 30000 and 29 < 30
    return dict(status='PASSED_SMALL_GRAPH_BFS_GAIN_SANITY', records=records,
                single_edges_checked=sum(row['single_edges_checked'] for row in records),
                shared_repair_example=dict(predicted_gain=predicted, actual_gain=actual),
                matching_size_for_weight_priority=29, weight_priority_bounds_checked=True,
                full_58_seeds_generated=0, elapsed_cpu=time.process_time()-cpu,
                elapsed_wall=time.monotonic()-wall)


def load_ambient():
    source = json.loads(SOURCE.read_text())
    deleted = source['deleted']
    assert len(deleted) == len(set(deleted)) == 15
    assert all(type(x) is int and 0 <= x < 73 for x in deleted)
    labels = sorted(set(range(73)) - set(deleted))
    assert len(labels) == N
    compact = {x: i for i, x in enumerate(labels)}
    old = {pair(compact[x], compact[y]) for x, y in baseline.geometry()['edges']
           if x in compact and y in compact}
    return labels, sorted(deleted), old


def generate_seed(seed, directory, labels, deleted, old):
    directory.mkdir(exist_ok=False)
    cpu, wall = time.process_time(), time.monotonic()
    rng = random.Random(seed)
    adj, edges, rounds = [0] * N, set(), []
    before_bad, masks = bad_pairs(adj)
    progress = dict(status='IN_PROGRESS', seed=seed, n=N, ambient_labels=labels,
                    completed_rounds=0, rounds=rounds)
    save(directory / 'rounds.json', progress)
    for r in range(8):
        round_cpu, round_wall = time.process_time(), time.monotonic()
        available = nx.Graph()
        available.add_nodes_from(range(N))
        for x, y in combinations(range(N), 2):
            if adj[x] >> y & 1:
                continue
            gain = single_edge_gain(adj, masks, x, y)
            old_flag, tie = int((x, y) in old), rng.randrange(1000)
            weight = (30*gain + old_flag)*30000 + tie
            available.add_edge(x, y, weight=weight, gain=gain, old=old_flag, tie=tie)
        matching = sorted(pair(x, y) for x, y in
                          nx.max_weight_matching(available, maxcardinality=True, weight='weight'))
        assert len(matching) == 29
        assert sorted(x for xy in matching for x in xy) == list(range(N))
        assert not edges.intersection(matching)
        predicted = sum(available[x][y]['gain'] for x, y in matching)
        matched_old = sum(available[x][y]['old'] for x, y in matching)
        tie_sum = sum(available[x][y]['tie'] for x, y in matching)
        for x, y in matching:
            edges.add((x, y))
            adj[x] |= 1 << y
            adj[y] |= 1 << x
        assert all(row.bit_count() == r+1 for row in adj)
        after_bad, after_masks = bad_pairs(adj)
        actual = len(before_bad) - len(after_bad)
        # A matching adds no two adjacent new edges. Its simultaneous gain
        # is the union of the individual gains, which may overlap.
        assert 0 <= actual <= predicted
        row = dict(round=r+1, matching_edges=matching, old_edges_in_matching=matched_old,
                   tie_sum=tie_sum, matching_weight=(30*predicted+matched_old)*30000+tie_sum,
                   before_bad_pairs=len(before_bad), bad_pair_count=len(after_bad),
                   bad_pairs=after_bad, predicted_single_edge_gain_sum=predicted,
                   actual_gain=actual, shared_repair_overcount=predicted-actual,
                   elapsed_cpu=time.process_time()-round_cpu,
                   elapsed_wall=time.monotonic()-round_wall)
        rounds.append(row)
        progress.update(completed_rounds=r+1, elapsed_cpu=time.process_time()-cpu,
                        elapsed_wall=time.monotonic()-wall)
        save(directory / 'rounds.json', progress)
        print(json.dumps(dict(seed=seed, round=r+1, bad_pairs=len(after_bad),
                              predicted_gain=predicted, actual_gain=actual)), flush=True)
        before_bad, masks = after_bad, after_masks
    assert len(edges) == 232 and all(row.bit_count() == 8 for row in adj)
    triangles = []
    for x in range(N):
        neighbors = [y for y in range(N) if adj[x] >> y & 1]
        triangles.append(sum(bool(adj[y] >> z & 1) for y, z in combinations(neighbors, 2)))
    assert sum(triangles) % 3 == 0
    result = dict(status='GENERATED_COMPLETE_8_REGULAR_GRAPH', scope=SCOPE, seed=seed,
                  n=N, edges=sorted(edges), ambient_labels=labels, deleted_ambient_labels=deleted,
                  degrees=[row.bit_count() for row in adj], bad_pair_count=len(before_bad),
                  bad_pairs=before_bad, triangles_per_vertex=triangles,
                  triangle_count=sum(triangles)//3, retained_geometric_edges=len(edges & old),
                  deleted_geometric_edges=len(old - edges), geometric_edges_in_source=len(old),
                  added_nongeometric_edges=len(edges - old),
                  target_graph_by_generator=not before_bad, independent_verification_performed=False,
                  source_deletion_file=str(SOURCE), rounds_file='rounds.json',
                  networkx_version=nx.__version__, python_version=sys.version.split()[0],
                  elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)
    (directory / 'candidate.edges').write_text(f'{N} {len(edges)}\n' +
        ''.join(f'{x} {y}\n' for x, y in sorted(edges)))
    progress.update(status='COMPLETE', completed_rounds=8,
                    elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)
    save(directory / 'rounds.json', progress)
    return result


def generate(seed_start, seed_stop, out_dir):
    assert 0 <= seed_start < seed_stop <= 8
    out_dir.mkdir(parents=True, exist_ok=True)
    assert not (out_dir / 'results.json').exists(), 'Preserve the previous batch; choose a new output directory'
    labels, deleted, old = load_ambient()
    seen = []
    for path in sorted(out_dir.glob('seed*/candidate.json')):
        row = json.loads(path.read_text())
        assert row['ambient_labels'] == labels
        seen.append((row['seed'], row['edges']))
    results = dict(status='IN_PROGRESS', scope=SCOPE, seed_start=seed_start, seed_stop=seed_stop,
                   ambient_labels=labels, deleted_ambient_labels=deleted, completed_seeds=[],
                   unique_labeled_seeds=[], records=[], deduplication='direct sorted edge-table equality',
                   nonisomorphism_claim=False)
    save(out_dir / 'results.json', results)
    for seed in range(seed_start, seed_stop):
        result = generate_seed(seed, out_dir / f'seed{seed}', labels, deleted, old)
        edge_table = [list(xy) for xy in result['edges']]
        duplicate = next((previous for previous, previous_edges in seen
                          if previous_edges == edge_table), None)
        result['duplicate_of_seed'] = duplicate
        save(out_dir / f'seed{seed}/candidate.json', result)
        if duplicate is None:
            seen.append((seed, edge_table))
            results['unique_labeled_seeds'].append(seed)
        results['completed_seeds'].append(seed)
        results['records'].append({key: result[key] for key in
                                  ('seed', 'bad_pair_count', 'triangle_count', 'retained_geometric_edges',
                                   'deleted_geometric_edges', 'duplicate_of_seed', 'elapsed_cpu', 'elapsed_wall')})
        save(out_dir / 'results.json', results)
    results['status'] = 'COMPLETE_REQUESTED_SEED_RANGE'
    results['unique_labeled_count'] = len(results['unique_labeled_seeds'])
    save(out_dir / 'results.json', results)
    print(json.dumps(results), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('generate', 'sanity'))
    parser.add_argument('--seed-start', type=int, default=0)
    parser.add_argument('--seed-stop', type=int, default=8, help='exclusive, at most 8')
    parser.add_argument('--out-dir', type=Path, default=HERE)
    args = parser.parse_args()
    if args.action == 'sanity':
        args.out_dir.mkdir(parents=True, exist_ok=True)
        assert not (args.out_dir / 'sanity.json').exists(), 'Preserve existing sanity record'
        record = sanity()
        save(args.out_dir / 'sanity.json', record)
        print(json.dumps(record, indent=2))
    else:
        generate(args.seed_start, args.seed_stop, args.out_dir)
