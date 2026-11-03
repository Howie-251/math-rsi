"""Independent Python lower-bound check on saved ten candidates; no BFS or search."""
from collections import Counter
from pathlib import Path
import json
import sys
import time

HERE = Path(__file__).resolve().parent
OLD = HERE.parent / 'm1_matching_augmentation'
SOURCE = HERE.parent / 'm1_d7d5_source' / 'baseline_normalized.edges'
N = 2810
UPTO5 = '--upto5' in sys.argv

def main():
    started = time.process_time()
    source_lines = SOURCE.read_text().splitlines()
    edges = [tuple(map(int, line.split())) for line in source_lines[1:]]
    edge_id = {edge: i for i, edge in enumerate(edges)}
    parameters = [json.loads((OLD / f'candidate_{i:02d}.parameters.json').read_text()) for i in range(10)]
    truth = json.loads((OLD / 'independent_validation.json').read_text())['candidates']
    needed = {edge_id[tuple(sorted(edge))] for p in parameters for edge in p['matching']}
    pair_sets = {}
    counts = []
    pair_filename = 'critical_upto5_pairs.txt' if UPTO5 else 'critical_pairs.txt'
    with (HERE / pair_filename).open() as f:
        n, m, total = map(int, next(f).split())
        assert (n, m) == (2810, 9835)
        for index, line in enumerate(f):
            values = list(map(int, line.split()))
            eid, count = values[:2]
            assert eid == index and count == len(values) - 2
            counts.append(count)
            if eid in needed:
                pairs = values[2:]
                assert pairs == sorted(set(pairs))
                assert all(0 <= x < y < N for x, y in (divmod(code, N) for code in pairs))
                pair_sets[eid] = set(pairs)
        assert len(counts) == m and sum(counts) == total
    distance = (OLD / 'baseline.distances.u8').read_bytes()
    assert len(distance) == N * N
    results, omission_witnesses = [], {}
    for i, (p, actual) in enumerate(zip(parameters, truth)):
        assert actual['candidate_id'] == p['candidate'] == i
        oriented = [tuple(pair) for pair in p['matching']]
        ids = [edge_id[tuple(sorted(edge))] for edge in oriented]
        C = set().union(*(pair_sets[eid] for eid in ids))
        assert all((0 < distance[code] <= 5) if UPTO5 else distance[code] == 5 for code in C)
        a = [min(distance[aa * N + x] for aa, bb in oriented) for x in range(N)]
        b = [min(distance[bb * N + x] for aa, bb in oriented) for x in range(N)]
        def lengths(x, y):
            return [a[x] + a[y] + 2, b[x] + b[y] + 2,
                    a[x] + b[y] + 3, b[x] + a[y] + 3]
        forced_old = sorted(code for code in C if min(lengths(*divmod(code, N))) > 5)
        forced_u = [x for x in range(N) if a[x] > 4 and b[x] > 3]
        forced_v = [x for x in range(N) if b[x] > 4 and a[x] > 3]
        lower_old, lower_new = len(forced_old), len(forced_u) + len(forced_v)
        actual_old = actual['bad_unordered_pairs']['old_old']
        actual_new = actual['bad_unordered_pairs']['new_old']
        assert lower_old <= actual_old and lower_new <= actual_new
        assert [len(forced_u), len(forced_v)] == [r['missing_within_5'] for r in actual['new_roots']]
        categories = Counter()
        examples = []
        for x, y in actual['bad_pair_examples']['old_old']:
            code = x * N + y
            original_distance = distance[code]
            if code in C:
                category = ('optimistic_G_endpoint_route_does_not_survive_deletion'
                            if min(lengths(x, y)) <= 5 else 'counted_by_lower_bound')
            elif UPTO5:
                category = 'joint_length_at_most_5_path_cut_without_single_compulsory_edge'
            elif original_distance < 5:
                category = 'original_distance_less_than_5'
            else:
                category = 'joint_shortest_path_cut_without_single_compulsory_edge'
            categories[category] += 1
            witness = {'candidate': i, 'pair': [x, y], 'original_G_distance': original_distance,
                       'actual_F_distance': 6, 'in_C': code in C,
                       'aG_values': [a[x], a[y]], 'bG_values': [b[x], b[y]],
                       'four_optimistic_lengths': lengths(x, y), 'category': category,
                       'truth_source': 'previously saved independent full-BFS bad_pair_examples'}
            examples.append(witness)
            if category != 'counted_by_lower_bound':
                omission_witnesses.setdefault(category, witness)
        sum_key = 'critical_upto5_sum_with_multiplicity' if UPTO5 else 'critical5_sum_with_multiplicity'
        result = {'candidate': i, sum_key: sum(counts[eid] for eid in ids),
                  'C_union_size': len(C), 'lower_bound_old_old': lower_old,
                  'lower_bound_new_u': len(forced_u), 'lower_bound_new_v': len(forced_v),
                  'lower_bound_new_old': lower_new, 'lower_bound_total': lower_old + lower_new,
                  'actual_old_old': actual_old, 'actual_new_old': actual_new,
                  'actual_total': actual_old + actual_new, 'omitted_actual_old_old_count': actual_old - lower_old,
                  'saved_bad_examples_categories': dict(categories), 'saved_bad_examples': examples,
                  'forced_old_old_pairs': [list(divmod(code, N)) for code in forced_old],
                  'forced_new_u_vertices': forced_u, 'forced_new_v_vertices': forced_v}
        results.append(result)
        print('candidate', i, 'C', len(C), 'LB', lower_old, '+', lower_new, '=', lower_old + lower_new,
              'actual', actual_old + actual_new, 'omitted_old', actual_old - lower_old)
    out = {'scope': 'Exactly the saved ten six-matching candidates; no graph BFS or new candidates.',
           'pair_definition': 'all original pairs with every walk of length at most 5 using e' if UPTO5 else 'original distance5 pairs with every shortest path using e',
           'pair_file': pair_filename,
           'candidate_results': results, 'actual_omission_witnesses': omission_witnesses,
           'saved_examples_are_partial': True, 'all_lower_bounds_at_most_saved_truth': True,
           'all_new_old_lower_bounds_exact_on_these_ten': True,
           'cpu_seconds': time.process_time() - started}
    output_filename = 'lower_bound_upto5_ten_check.json' if UPTO5 else 'lower_bound_ten_check.json'
    (HERE / output_filename).write_text(json.dumps(out, indent=2) + '\n')
    print('omission categories witnessed:', list(omission_witnesses), 'cpu', out['cpu_seconds'])

if __name__ == '__main__':
    main()
