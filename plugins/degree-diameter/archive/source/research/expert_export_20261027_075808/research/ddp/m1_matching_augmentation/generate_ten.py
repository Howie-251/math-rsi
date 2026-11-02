"""Ten predetermined deterministic six-matching augmentation policies, no random search."""
from collections import Counter
from pathlib import Path
import json
import time

OUT = Path(__file__).resolve().parent
PROJECT = OUT.parents[2]
SOURCE = PROJECT / 'research/ddp/m1_d7d5_source/baseline_normalized.edges'
N = 2810
GROUP = 1405

def edge_class(u, v):
    if v < GROUP:
        return 0
    if u >= GROUP:
        return 1
    x, i = divmod(u, 5)
    y, j = divmod(v - GROUP, 5)
    z = (y - x) * pow(86, (-i) % 5, 281) % 281
    residue = (j - i) % 5
    return 2 + [0, 412, 1338, 186, 45].index(z * 5 + residue)

def signature(matching):
    return min(tuple(sorted(matching)), tuple(sorted((b, a) for a, b in matching)))

def main():
    start = time.monotonic()
    cpu_start = time.process_time()
    lines = SOURCE.read_text().splitlines()
    assert tuple(map(int, lines[0].split())) == (2810, 9835)
    edges = [tuple(map(int, line.split())) for line in lines[1:]]
    edge_set = set(edges)
    critical_rows = [tuple(map(int, line.split())) for line in (OUT / 'baseline.edge_critical5.txt').read_text().splitlines()]
    assert [(u, v) for u, v, _ in critical_rows] == edges
    critical = [c for _, _, c in critical_rows]
    classes = [edge_class(u, v) for u, v in edges]
    assert Counter(classes) == {i: 1405 for i in range(7)}
    distance = (OUT / 'baseline.distances.u8').read_bytes()
    assert len(distance) == N * N
    balls3, balls4 = [], []
    for u in range(N):
        b3, b4 = bytearray((N + 7) // 8), bytearray((N + 7) // 8)
        for v, d in enumerate(distance[u * N:(u + 1) * N]):
            if d <= 4:
                b4[v // 8] |= 1 << (v % 8)
            if d <= 3:
                b3[v // 8] |= 1 << (v % 8)
        balls3.append(int.from_bytes(b3, 'little'))
        balls4.append(int.from_bytes(b4, 'little'))
    names = ['internal_A', 'internal_B', 'cross_e', 'cross_412', 'cross_1338', 'cross_186', 'cross_45']
    policies = [{'id': i, 'name': 'single_orbit_' + name, 'edge_class': i, 'priority': 'coverage'}
                for i, name in enumerate(names)]
    policies += [
        {'id': 7, 'name': 'mixed_balanced_coverage', 'edge_class': None, 'priority': 'coverage'},
        {'id': 8, 'name': 'mixed_low_critical5', 'edge_class': None, 'priority': 'critical5'},
        {'id': 9, 'name': 'mixed_endpoint_separation', 'edge_class': None, 'priority': 'separation'},
    ]
    description = {
        'policies': policies, 'candidate_count': 10, 'matching_size': 6, 'randomness': False,
        'coverage_rule': 'For each oriented edge (a,b), use B_G^4(a) union B_G^3(b) for u and the swapped expression for v. Rank balanced union coverage, then coverage by two different selected edges.',
        'critical5_rule': 'Number of unordered old distance-5 pairs whose every shortest path uses this edge; this is exact one-edge damage among old distance-5 pairs, not all deletion damage.',
        'separation_rule': 'Minimum and sum of original distances between the new edge endpoints and all previously selected endpoints.',
        'tie_breaks': 'Deterministic old edge index and orientation. Skip a completed matching already produced, including global u/v exchange.',
    }
    (OUT / 'policies.json').write_text(json.dumps(description, indent=2) + '\n')
    results = []
    used_signatures = set()
    for policy in policies:
        candidate_start = time.monotonic()
        allowed = [i for i in range(len(edges)) if policy['edge_class'] is None or classes[i] == policy['edge_class']]
        matching, selected_ids, endpoints, used = [], [], [], set()
        u_once = v_once = u_twice = v_twice = 0
        steps = []
        for step in range(6):
            best = None
            for eid in allowed:
                u, v = edges[eid]
                if u in used or v in used:
                    continue
                if endpoints:
                    ds = [distance[x * N + y] for x in (u, v) for y in endpoints]
                    spread = (min(ds), sum(ds))
                else:
                    spread = (0, 0)
                for orient, (a, b) in enumerate(((u, v), (v, u))):
                    if not endpoints and orient:
                        continue  # overall u/v exchange only
                    if step == 5 and signature(matching + [(a, b)]) in used_signatures:
                        continue
                    cu, cv = balls4[a] | balls3[b], balls4[b] | balls3[a]
                    nu, nv = u_once | cu, v_once | cv
                    ntu, ntv = u_twice | (u_once & cu), v_twice | (v_once & cv)
                    uc, vc, utc, vtc = nu.bit_count(), nv.bit_count(), ntu.bit_count(), ntv.bit_count()
                    coverage = (min(uc, vc), uc + vc, min(utc, vtc), utc + vtc)
                    if policy['priority'] == 'critical5':
                        rank = (-critical[eid],) + coverage + spread
                    elif policy['priority'] == 'separation':
                        rank = spread + coverage + (-critical[eid],)
                    else:
                        rank = coverage + (-critical[eid],) + spread
                    rank += (-eid, -orient)
                    if best is None or rank > best[0]:
                        best = (rank, eid, a, b, nu, nv, ntu, ntv, coverage, spread)
            assert best is not None
            _, eid, a, b, u_once, v_once, u_twice, v_twice, coverage, spread = best
            matching.append((a, b)); selected_ids.append(eid); endpoints.extend((a, b)); used.update((a, b))
            steps.append({'edge_id': eid, 'oriented_edge': [a, b], 'edge_class': classes[eid],
                          'critical5': critical[eid], 'coverage_rank': list(coverage), 'separation_rank': list(spread)})
        assert len(used) == 12
        sig = signature(matching)
        assert sig not in used_signatures
        used_signatures.add(sig)
        new_edges = edge_set.copy()
        for a, b in matching:
            new_edges.remove(tuple(sorted((a, b))))
            new_edges.add(tuple(sorted((a, N))))
            new_edges.add(tuple(sorted((b, N + 1))))
        new_edges.add((N, N + 1))
        degree = Counter(v for edge in new_edges for v in edge)
        assert len(new_edges) == 9842 and len(degree) == N + 2 and set(degree.values()) == {7}
        name = f"candidate_{policy['id']:02d}"
        (OUT / (name + '.edges')).write_text(f'{N + 2} {len(new_edges)}\n' + ''.join(f'{a} {b}\n' for a, b in sorted(new_edges)))
        record = {'candidate': policy['id'], 'policy': policy, 'matching': matching, 'steps': steps,
                  'critical5_sum': sum(critical[eid] for eid in selected_ids),
                  'predeletion_new_root_missing_upper_coverage': [N - u_once.bit_count(), N - v_once.bit_count()],
                  'predeletion_covered_by_two_edges': [u_twice.bit_count(), v_twice.bit_count()],
                  'generation_wall_seconds': time.monotonic() - candidate_start}
        (OUT / (name + '.parameters.json')).write_text(json.dumps(record, indent=2) + '\n')
        results.append(record)
        print(name, policy['name'], 'critical5', record['critical5_sum'], 'preG uncovered', record['predeletion_new_root_missing_upper_coverage'], flush=True)
    summary = {'status': 'TEN_CANDIDATES_GENERATED', 'candidates': results,
               'edge_class_critical5_histograms': {names[i]: dict(sorted(Counter(critical[j] for j, c in enumerate(classes) if c == i).items())) for i in range(7)},
               'cpu_seconds': time.process_time() - cpu_start, 'wall_seconds': time.monotonic() - start}
    (OUT / 'generation.json').write_text(json.dumps(summary, indent=2) + '\n')
    print('generation complete cpu', summary['cpu_seconds'], 'wall', summary['wall_seconds'], flush=True)

if __name__ == '__main__':
    main()
