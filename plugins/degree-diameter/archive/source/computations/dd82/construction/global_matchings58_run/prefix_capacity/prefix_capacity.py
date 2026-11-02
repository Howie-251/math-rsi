"""Read saved matching prefixes and compute a necessary completion capacity.

No construction, matching optimization, SAT, or graph search. Every stored
prefix is reconstructed from its actual matching edges and checked directly.
"""
import argparse
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('prefix_gain_definitions', HERE.parent / 'generate.py')
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


def diagnose(pilot):
    cpu, wall = time.process_time(), time.monotonic()
    records, first_failures, first_repeat_failures, labels = [], [], [], None
    for seed in range(8):
        source = pilot / f'seed{seed}/rounds.json'
        data = json.loads(source.read_text())
        assert data['status'] == 'COMPLETE' and data['completed_rounds'] == 8
        assert data['n'] == 58 and data['seed'] == seed
        if labels is None:
            labels = data['ambient_labels']
        assert data['ambient_labels'] == labels
        edges, earliest, earliest_repeat = set(), None, None
        for r, row in enumerate(data['rounds'][:7], 1):
            assert row['round'] == r
            matching = list(map(tuple, row['matching_edges']))
            assert len(matching) == 29 and not edges.intersection(matching)
            assert sorted(x for xy in matching for x in xy) == list(range(58))
            edges.update(matching)
            adj = generator.bit_adjacency(58, edges)
            assert all(neighbors.bit_count() == r for neighbors in adj)
            bad, masks = generator.bad_pairs(adj)
            assert len(bad) == row['bad_pair_count']
            assert [list(xy) for xy in bad] == row['bad_pairs']
            d = 8-r
            incident = [[] for _ in range(58)]
            for x, y in combinations(range(58), 2):
                if (x, y) in edges:
                    continue
                gain = generator.single_edge_gain(adj, masks, x, y)
                incident[x].append((gain, y))
                incident[y].append((gain, x))
            top = [sorted(values, key=lambda term: (-term[0], term[1]))[:d]
                   for values in incident]
            assert all(len(values) == d for values in top)
            top_sums = [sum(gain for gain, _ in values) for values in top]
            incident_total = sum(top_sums)
            single_edge_bound = incident_total // 2
            two_new_bound = 58*d*(d-1)//2
            upper_bound = single_edge_bound + two_new_bound
            bad_at_vertex = [mask.bit_count() for mask in masks]
            repeats = [1+r*r-(58-count) for count in bad_at_vertex]
            assert all(value >= 0 for value in repeats)
            repeat_vertices = [x for x in range(58) if repeats[x] > 7]
            record = dict(seed=seed, round=r, degree=r, residual_new_degree=d,
                          edges=len(edges), bad_pairs=len(bad),
                          vertex_top_d_gain_sums=top_sums,
                          incident_top_d_total=incident_total,
                          single_edge_gain_upper_bound=single_edge_bound,
                          two_new_path_upper_bound=two_new_bound,
                          total_repair_upper_bound=upper_bound,
                          capacity_minus_bad=upper_bound-len(bad),
                          impossible_monotone_completion=upper_bound < len(bad),
                          bad_partners_per_vertex=bad_at_vertex,
                          nonbacktracking_repeat_counts=repeats,
                          repeat_obstruction_vertices=repeat_vertices,
                          impossible_by_repeat_bound=bool(repeat_vertices))
            records.append(record)
            if record['impossible_monotone_completion'] and earliest is None:
                earliest = dict(record)
                earliest['prefix_source'] = str(source)
                earliest['top_d_incident_edges'] = [dict(vertex=x,
                    ambient_vertex=labels[x], entries=[dict(neighbor=y, ambient_neighbor=labels[y], gain=g)
                                                       for g, y in top[x]]) for x in range(58)]
            if repeat_vertices and earliest_repeat is None:
                x = max(repeat_vertices, key=lambda vertex: (repeats[vertex], -vertex))
                earliest_repeat = dict(seed=seed, round=r, vertex=x, ambient_vertex=labels[x],
                                       bad_partners=bad_at_vertex[x],
                                       prefix_walks=1+r*r, reached_vertices=58-bad_at_vertex[x],
                                       repeat_count=repeats[x], target_repeat_budget=7,
                                       prefix_source=str(source))
            assert time.process_time()-cpu < 5, 'Read-only diagnostic exceeded five CPU seconds'
        first_failures.append(dict(seed=seed, earliest_failing_round=earliest['round'] if earliest else None,
                                   witness=earliest))
        first_repeat_failures.append(dict(seed=seed,
            earliest_failing_round=earliest_repeat['round'] if earliest_repeat else None,
            witness=earliest_repeat))
    assert len(records) == 56
    return dict(status='COMPLETE_SAVED_PREFIX_CAPACITY_DIAGNOSTIC',
                scope='Only the 56 saved prefixes; failure excludes every monotone 8-regular completion '
                      'of that actual prefix, not just matching-colored extensions.',
                graph_generation_calls=0, matching_calls=0, solver_calls=0,
                ambient_labels=labels, seeds=8, prefixes=56,
                excluded_prefixes=sum(row['impossible_monotone_completion'] for row in records),
                excluded_by_repeat_bound=sum(row['impossible_by_repeat_bound'] for row in records),
                first_failures=first_failures, first_repeat_failures=first_repeat_failures, records=records,
                elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pilot', type=Path, default=HERE.parent / 'pilot')
    parser.add_argument('--output', type=Path, default=HERE / 'prefix_capacity.json')
    args = parser.parse_args()
    assert not args.output.exists(), 'Preserve existing diagnostic evidence'
    result = diagnose(args.pilot)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(status=result['status'], prefixes=result['prefixes'],
                         excluded_prefixes=result['excluded_prefixes'],
                         excluded_by_repeat_bound=result['excluded_by_repeat_bound'],
                         elapsed_cpu=result['elapsed_cpu'], elapsed_wall=result['elapsed_wall'],
                         first_failures=[dict(seed=row['seed'], round=row['earliest_failing_round'],
                                             bad_pairs=row['witness']['bad_pairs'] if row['witness'] else None,
                                             upper_bound=row['witness']['total_repair_upper_bound']
                                             if row['witness'] else None) for row in result['first_failures']]), indent=2))
