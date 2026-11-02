"""Diagnose actual saved eight-regular graphs; no search or new candidates."""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent


def main():
    cpu, wall = time.process_time(), time.monotonic()
    reports = []
    for candidate in sorted((HERE / 'pilot').glob('seed*/candidate.json')):
        data = json.loads(candidate.read_text())
        verified = json.loads(candidate.with_suffix('.verification.json').read_text())
        neighbors = [set() for _ in range(data['n'])]
        for u, v in data['edges']:
            neighbors[u].add(v)
            neighbors[v].add(u)
        bad_degree = [0] * data['n']
        for item in verified['bad_pairs']:
            u, v = item['pair']
            bad_degree[u] += 1
            bad_degree[v] += 1
        local = []
        for u in range(data['n']):
            adjacent_repeat = sum(len(neighbors[u] & neighbors[v]) for v in neighbors[u])
            other_repeat = sum(max(len(neighbors[u] & neighbors[v]) - 1, 0)
                               for v in range(data['n']) if u != v and v not in neighbors[u])
            # The 1+8+8*7=65 nonbacktracking walks cover 58-bad_degree[u]
            # distinct vertices. Repeated visits split into triangles and
            # multiple common neighbors of nonadjacent endpoints.
            assert adjacent_repeat + other_repeat == 7 + bad_degree[u]
            local.append(dict(vertex=u, ambient_label=data['ambient_labels'][u],
                              bad_degree=bad_degree[u], triangle_repeat=adjacent_repeat,
                              nonneighbor_repeat=other_repeat))
        rounds = json.loads((candidate.parent / 'rounds.json').read_text())['rounds']
        report = dict(seed=data['seed'], bad_pair_count=verified['bad_pair_count'],
                      diameter=verified['diameter'], triangle_count=data['triangle_count'],
                      bad_degree_histogram=dict(sorted(Counter(bad_degree).items())),
                      common_neighbor_histogram_nonadjacent=dict(sorted(Counter(
                          len(neighbors[u] & neighbors[v]) for u, v in combinations(range(data['n']), 2)
                          if v not in neighbors[u]).items())),
                      triangle_repeat_total=sum(x['triangle_repeat'] for x in local),
                      nonneighbor_repeat_total=sum(x['nonneighbor_repeat'] for x in local),
                      retained_geometric_edges=data['retained_geometric_edges'],
                      deleted_geometric_edges=data['deleted_geometric_edges'],
                      actual_bad_pairs_by_round=[r['bad_pair_count'] for r in rounds],
                      shared_repair_overcount_by_round=[r['shared_repair_overcount'] for r in rounds],
                      local_collision_identity_checked=True, local=local)
        reports.append(report)
    assert reports
    result = dict(status='SAVED_GRAPH_DIAGNOSTICS', scope='Only the actually saved pilot seeds',
                  seeds=reports, best_seed=min(reports, key=lambda x: x['bad_pair_count'])['seed'],
                  elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)
    (HERE / 'pilot/diagnostics.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'seeds'}))
    for row in reports:
        print(json.dumps({k: v for k, v in row.items() if k != 'local'}))


if __name__ == '__main__':
    main()
