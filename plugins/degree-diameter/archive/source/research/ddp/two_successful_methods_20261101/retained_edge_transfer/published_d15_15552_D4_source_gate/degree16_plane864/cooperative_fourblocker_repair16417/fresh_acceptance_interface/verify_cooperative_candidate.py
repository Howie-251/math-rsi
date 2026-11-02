#!/usr/bin/env python3
"""Prepared five-helper fresh verifier. Not run during preparation.

Params JSON: new_center (original15552 label), donors (four actual current
clone labels), H_edges (unordered pairs of actual donor/newZ labels).
Only the actual current16416 and complete candidate edge files are parsed.
"""
import time
START = time.process_time()
import argparse
import csv
import json
import os
from pathlib import Path
import resource

ORIGINAL, SN, SM, NN = 15552, 16416, 129240, 16417
Z = SN


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--params', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--cpu-budget', type=float, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    repo = next(p for p in here.parents if (p / 'formal/DegreeDiameter/Portfolio').is_dir())
    accepted_dir = repo / ('research/ddp/two_successful_methods_20261101/retained_edge_transfer/'
        'published_d15_15552_D4_source_gate/degree16_plane864')
    assert args.source.resolve() == (accepted_dir / 'graph_d16_D4_n16416.edges').resolve()
    assert not (args.out / 'TERMINAL.json').exists()
    resource.setrlimit(resource.RLIMIT_CPU, (max(1, int(args.cpu_budget)),) * 2)
    args.out.mkdir(parents=True, exist_ok=True)

    def write(name, value):
        (args.out / name).write_text(json.dumps(value, indent=2) + '\n')

    def hist(values):
        result = {}
        for value in values:
            result[str(value)] = result.get(str(value), 0) + 1
        return result

    def bfs(graph, root):
        distance, parent = [-1] * NN, [-1] * NN
        distance[root] = 0
        queue = [root]
        for u in queue:
            for v in graph[u]:
                if distance[v] < 0:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
        return distance, parent

    def path_to(parent, target):
        route = []
        while target != -1:
            route.append(target)
            target = parent[target]
        return route[::-1]

    phase = 'input_binding'
    source_parses = candidate_parses = roots = 0
    try:
        params = json.loads(args.params.read_text())
        v = params['new_center']
        donors = sorted(params['donors'])
        assert type(v) is int and 0 <= v < ORIGINAL
        assert len(donors) == len(set(donors)) == 4
        assert all(type(d) is int and ORIGINAL <= d < SN for d in donors)
        D = set(donors)
        helpers = donors + [Z]
        hset = set(helpers)
        H = set()
        for pair in params['H_edges']:
            a, b = sorted(pair)
            assert a != b and a in hset and b in hset and (a, b) not in H
            H.add((a, b))
        write('HANDLE.json', {'status': 'RUNNING', 'pid': os.getpid(), 'phase': phase,
            'actual_helpers': helpers, 'new_center': v, 'CPU_budget_seconds': args.cpu_budget})

        # Accepted old role labels only; no producer neighborhoods or new masks.
        with (accepted_dir / 'independent_acceptance/ALL864_ACTUAL_ROLE_BINDINGS.tsv').open() as stream:
            old_centers = {int(row['new_label']): int(row['old_center_label'])
                           for row in csv.DictReader(stream, delimiter='\t')}
        assert D <= set(old_centers) and v not in set(old_centers.values())
        source_adj = [set() for _ in range(SN)]
        with args.source.open() as stream:
            source_parses += 1
            assert tuple(map(int, next(stream).split())) == (SN, SM)
            source_edges = set()
            for line in stream:
                a, b = map(int, line.split())
                source_edges.add((a, b))
                source_adj[a].add(b)
                source_adj[b].add(a)
        assert len(source_edges) == SM
        original_set = set(range(ORIGINAL))
        clone_set = set(range(ORIGINAL, SN))
        Nv = source_adj[v] & original_set
        assert v not in Nv
        donor_centers = {}
        for d in donors:
            c = old_centers[d]
            assert 0 <= c < ORIGINAL
            assert source_adj[d] <= original_set
            assert source_adj[d] == source_adj[c] & original_set
            donor_centers[d] = c

        blocked = sorted(w for w in Nv if len(source_adj[w]) == 16)
        owners = {}
        for w in blocked:
            actual_owners = source_adj[w] & clone_set
            assert len(actual_owners) == 1
            owner = next(iter(actual_owners))
            assert owner in D and len(source_adj[w] & original_set) == 15
            owners[w] = owner
        assert set(owners.values()) == D
        removed = {tuple(sorted((d, w))) for w, d in owners.items()}
        assert removed <= source_edges
        Z_edges = {tuple(sorted((w, Z))) for w in Nv}
        assert not H & source_edges and not H & Z_edges
        expected_edges = sorted((source_edges - removed) | Z_edges | H)
        expected_m = SM - len(removed) + len(Nv) + len(H)
        assert len(expected_edges) == expected_m
        donor_removed = {d: sorted(w for w, owner in owners.items() if owner == d) for d in donors}
        helper_H_degree = {d: sum(d in edge for edge in H) for d in helpers}
        helper_port_degree = {d: len(source_adj[d]) - len(donor_removed[d]) for d in donors}
        helper_port_degree[Z] = len(Nv)
        assert all(helper_port_degree[d] + helper_H_degree[d] <= 16 for d in helpers)

        phase = 'one_complete_new_literal_stream'
        graph = [[] for _ in range(NN)]
        count = 0
        prior = (-1, -1)
        with args.candidate.open() as stream:
            candidate_parses += 1
            assert tuple(map(int, next(stream).split())) == (NN, expected_m)
            for line in stream:
                a, b = map(int, line.split())
                assert 0 <= a < b < NN and prior < (a, b)
                prior = (a, b)
                assert count < expected_m and expected_edges[count] == (a, b)
                graph[a].append(b)
                graph[b].append(a)
                count += 1
        assert count == expected_m
        degree = [len(neighbors) for neighbors in graph]
        assert max(degree) <= 16
        base = set(range(SN)) - D
        assert len(base) == 16412
        source_base_edges = {e for e in source_edges if e[0] in base and e[1] in base}
        candidate_base_edges = {e for e in expected_edges if e[0] in base and e[1] in base}
        assert source_base_edges == candidate_base_edges
        original_edges = {e for e in source_edges if e[0] < ORIGINAL and e[1] < ORIGINAL}
        assert len(original_edges) == 116316 and original_edges <= set(expected_edges)
        write('LITERAL_DELTA_AND_RETRACTION_BINDING.json', {
            'source_n': SN, 'source_m': SM, 'n': NN, 'm': expected_m,
            'new_center': v, 'four_donors': donors,
            'donor_to_original_center': {str(d): c for d, c in donor_centers.items()},
            'donor_complete_original_N_checked_in_current_literal': True,
            'blocked_source_vertices': blocked,
            'blocked_source_to_unique_owner': {str(w): d for w, d in owners.items()},
            'removed_donor_old_edges_exact': [list(e) for e in sorted(removed)],
            'newZ_original_neighbors_exact': sorted(Nv), 'actual_H_edges': [list(e) for e in sorted(H)],
            'helper_H_degrees': helper_H_degree, 'helper_base_port_degrees': helper_port_degree,
            'donor_removed_counts': {str(d): len(donor_removed[d]) for d in donors},
            'shared_retained_source_pins_with_Z': {str(d): len((source_adj[d] - set(donor_removed[d])) & Nv) for d in donors},
            'olddegree14_overlap_allowed': True, 'degree_histogram': hist(degree),
            'stable_induced_base_n': len(base), 'stable_induced_base_edges': len(source_base_edges),
            'all116316_original_source_edges_kept': True, 'other860_clone_edges_untouched': True,
            'source_literal_parses': source_parses, 'candidate_literal_parses': candidate_parses,
            'no_producer_masks_imported': True})

        phase = 'five_actual_helper_BFS_roots'
        summaries = []
        for root in helpers:
            assert time.process_time() - START < args.cpu_budget
            distance, parent = bfs(graph, root)
            roots += 1
            bad = next((w for w in range(NN) if distance[w] < 0 or distance[w] > 4), None)
            summaries.append({'root': root, 'kind': 'newZ' if root == Z else 'modified_donor',
                'histogram': hist(distance), 'all16417_reached_within4': bad is None})
            if bad is not None:
                write('HELPER_COUNTEREXAMPLE.json', {'root': root, 'target': bad,
                    'distance': distance[bad], 'actual_shortest_path': [] if distance[bad] < 0 else path_to(parent, bad),
                    'helper_roots_completed': roots})
            assert bad is None, 'one actual helper fails the final all-vertex D4 obligation'
        write('FIVE_HELPER_BFS_SUMMARIES.json', summaries)
        phase = 'fixed_old0_finalgraph_witness'
        distance, parent = bfs(graph, 0)
        roots += 1
        assert all(0 <= d <= 4 for d in distance) and max(distance) == 4
        target = next(w for w in range(NN) if distance[w] == 4)
        write('OLD0_GENUINE_DISTANCE4_WITNESS.json', {'root': 0, 'target': target, 'distance': 4,
            'actual_shortest_path': path_to(parent, target), 'graph': 'actual_final_cooperative16417',
            'source_only_BFS': False})
        proof = (here / 'COOPERATIVE_PROOF_DRAFT.md').read_text().replace('{{M}}', str(expected_m))
        (args.out / 'STRUCTURE_PROOF.md').write_text(proof)
        write('RESULT.json', {'status': 'PASS_COOPERATIVE_LITERAL_AND_BASE_PLUS_HELPER_D4_PENDING_ROOT',
            'n': NN, 'm': expected_m, 'max_degree': max(degree), 'degree_histogram': hist(degree),
            'literal_delta_exact': True, 'forced_four_blocked_owners_exact': True,
            'base_n': 16412, 'base_D4': 'acceptedcurrent16416 retraction of removeddonors to originalcenters',
            'helper_roots_checked': helpers, 'ordinary_candidate_BFS_roots': roots,
            'allpair_D4': 'base-base inherited + each actualhelper toall finalvertices BFS',
            'exact_D4': 'actualfinal old0 shortest4walk;also Moore3857<16417 atcap16',
            'source_literal_parses': source_parses, 'candidate_literal_parses': candidate_parses,
            'source_only_or_allroot_BFS_field_Lean_reviews': 0,
            'new_concrete_Lean_checked': False, 'sequential_helper_prefix_claim': False,
            'CPU_seconds': time.process_time() - START, 'CPU_budget_seconds': args.cpu_budget})
        status = 'PASS_PENDING_ROOT_ACCEPTANCE'
    except Exception as exc:
        write('FAILURE.json', {'status': 'FAIL_OR_BUDGET_UNKNOWN', 'phase': phase, 'error': str(exc),
            'source_literal_parses': source_parses, 'candidate_literal_parses': candidate_parses,
            'ordinary_candidate_BFS_roots': roots, 'CPU_seconds': time.process_time() - START})
        status = 'FAIL_OR_BUDGET_UNKNOWN'
    write('TERMINAL.json', {'status': status, 'terminal': True, 'active_processes': 0,
        'ordinary_candidate_BFS_roots': roots, 'source_only_or_allroot_BFS': 0,
        'CPU_seconds': time.process_time() - START, 'CPU_budget_seconds': args.cpu_budget})
    write('HANDLE.json', {'status': status, 'terminal': True, 'active_processes': 0})
    print(status)
    if status != 'PASS_PENDING_ROOT_ACCEPTANCE':
        raise SystemExit(2)


if __name__ == '__main__':
    main()
