#!/usr/bin/env python3
"""Prepared SingleExtension acceptance; no execution during preparation.

After ROOT supplies an actual complete candidate and budget, bind all old
edges and its one new neighborhood, then BFS only newZ and fixed old0 on
the actual final graph. No source-only or all-root BFS is performed.
"""
import time
START = time.process_time()
import argparse
import json
import os
from pathlib import Path
import resource

SN, SM, NN = 16416, 129240, 16417


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--pins', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--cpu-budget', type=float, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    repo = next(p for p in here.parents if (p / 'formal/DegreeDiameter/Portfolio').is_dir())
    accepted_source = repo / ('research/ddp/two_successful_methods_20261101/retained_edge_transfer/'
        'published_d15_15552_D4_source_gate/degree16_plane864/graph_d16_D4_n16416.edges')
    assert args.source.resolve() == accepted_source.resolve()
    assert not (args.out / 'TERMINAL.json').exists()
    hard = max(1, int(args.cpu_budget))
    resource.setrlimit(resource.RLIMIT_CPU, (hard, hard))
    args.out.mkdir(parents=True, exist_ok=True)

    def write(name, value):
        (args.out / name).write_text(json.dumps(value, indent=2) + '\n')

    def bfs(graph, root):
        distance, parent, firstpin = [-1] * NN, [-1] * NN, [-1] * NN
        distance[root] = 0
        queue = [root]
        for u in queue:
            for v in graph[u]:
                if distance[v] < 0:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    if root == SN:
                        firstpin[v] = v if u == SN else firstpin[u]
                    queue.append(v)
        return distance, parent, firstpin

    def path_to(parent, target):
        path = []
        while target != -1:
            path.append(target)
            target = parent[target]
        return path[::-1]

    def hist(values):
        result = {}
        for v in values:
            result[str(v)] = result.get(str(v), 0) + 1
        return result

    source_parses = candidate_parses = candidate_roots = 0
    phase = 'input_binding'
    try:
        data = json.loads(args.pins.read_text())
        pins = data if isinstance(data, list) else data['pins']
        assert 1 <= len(pins) <= 16 and len(set(pins)) == len(pins)
        assert all(type(v) is int and 0 <= v < SN for v in pins)
        pinset = set(pins)
        with args.source.open() as stream:
            source_parses += 1
            assert tuple(map(int, next(stream).split())) == (SN, SM)
            source_edges = [tuple(map(int, line.split())) for line in stream]
        assert len(source_edges) == SM
        source_degree = [0] * SN
        for u, v in source_edges:
            source_degree[u] += 1
            source_degree[v] += 1
        assert all(source_degree[p] < 16 for p in pins)
        expected_degree = [source_degree[v] + (v in pinset) for v in range(SN)] + [len(pins)]
        assert max(expected_degree) <= 16
        write('HANDLE.json', {'status': 'RUNNING', 'pid': os.getpid(),
            'phase': 'one_candidate_stream', 'newroot_label': SN, 'fixed_oldroot': 0})
        graph = [[] for _ in range(NN)]
        old_index = count = 0
        actual_pins = []
        prior = (-1, -1)
        with args.candidate.open() as stream:
            candidate_parses += 1
            assert tuple(map(int, next(stream).split())) == (NN, SM + len(pins))
            for line in stream:
                u, v = map(int, line.split())
                assert 0 <= u < v < NN and prior < (u, v)
                prior = (u, v)
                if v < SN:
                    assert old_index < SM and source_edges[old_index] == (u, v)
                    old_index += 1
                else:
                    assert v == SN and u < SN
                    actual_pins.append(u)
                graph[u].append(v)
                graph[v].append(u)
                count += 1
        assert old_index == SM and count == SM + len(pins)
        assert actual_pins == sorted(pins)
        degree = [len(g) for g in graph]
        assert degree == expected_degree and max(degree) <= 16

        phase = 'actual_newroot_BFS_only'
        dz, pz, fp = bfs(graph, SN)
        candidate_roots += 1
        missing = [v for v in range(SN) if dz[v] < 0 or dz[v] > 4]
        if missing:
            target = missing[0]
            write('COUNTEREXAMPLE.json', {'root': SN, 'target': target, 'distance': dz[target],
                'actual_shortest_route': [] if dz[target] < 0 else path_to(pz, target),
                'newroot_missing_old_count': len(missing)})
        assert not missing, 'newroot does not reach every old vertex within4'
        assert max(dz) == 4
        with (args.out / 'OLD_R3_PARENT_DEPTH.tsv').open('w') as stream:
            stream.write('old_vertex\tfirst_pin\told_depth\told_parent\n')
            for v in range(SN):
                depth = dz[v] - 1
                parent = v if depth == 0 else pz[v]
                assert 0 <= depth <= 3 and fp[v] in pinset
                if depth == 0:
                    assert v in pinset
                else:
                    assert parent < SN and dz[parent] + 1 == dz[v] and v in graph[parent]
                stream.write(f'{v}\t{fp[v]}\t{depth}\t{parent}\n')
        ztarget = next(v for v in range(SN) if dz[v] == 4)
        write('NEWROOT_DISTANCE4_WITNESS.json', {'root': SN, 'target': ztarget,
            'distance': 4, 'actual_shortest_walk': path_to(pz, ztarget)})

        # One preselected OLD label on the NEW graph, not a source-only suite.
        phase = 'one_fixed_oldroot_on_final_graph'
        d0, p0, _ = bfs(graph, 0)
        candidate_roots += 1
        assert all(0 <= d <= 4 for d in d0) and max(d0) == 4
        target = next(v for v in range(NN) if d0[v] == 4)
        write('OLDROOT_DISTANCE4_WITNESS.json', {'root': 0, 'target': target,
            'distance': 4, 'actual_shortest_walk': path_to(p0, target),
            'graph': 'new_final16417', 'separate_source_BFS': False})
        proof = (here / 'SINGLE_EXTENSION_PROOF_DRAFT.md').read_text().replace('{{M}}', str(count)).replace('{{K}}', str(len(pins)))
        (args.out / 'STRUCTURE_PROOF.md').write_text(proof)
        write('RESULT.json', {'status': 'PASS_LITERAL_SINGLE_EXTENSION_ALLPAIR_EXACT_D4_PENDING_ROOT',
            'n': NN, 'm': count, 'source_n': SN, 'source_m': SM,
            'old_edges_retained_exact': SM, 'new_vertex_label': SN, 'actual_pins': sorted(pins),
            'new_edges': len(pins), 'degree_histogram': hist(degree), 'max_degree': max(degree),
            'newroot_histogram': hist(dz), 'one_fixed_oldroot_histogram': hist(d0),
            'newroot_all_old_reached_within4': True, 'genuine_old_R3_parent_depth_rows': SN,
            'allpair_D4': 'acceptedsourceD4 + oldedgeembedding + SingleExtension/PinsCoverRadius3',
            'exact_D4': 'actual final old0 distance4 witness; also16417 exceeds degree16 radius3 bound3857',
            'source_kernel_target': 'DegreeDiameter.Portfolio.F3Graph15552.Clone16416.d16_16416',
            'new_specific_concrete_Lean_checked': False,
            'source_literal_parses': source_parses, 'candidate_literal_parses': candidate_parses,
            'ordinary_candidate_BFS_roots': candidate_roots, 'source_only_BFS_roots': 0,
            'allroot_BFS_field_solver_Lean_reviews': 0,
            'CPU_seconds': time.process_time() - START, 'CPU_budget_seconds': args.cpu_budget})
        status = 'PASS_PENDING_ROOT_ACCEPTANCE'
    except Exception as exc:
        write('FAILURE.json', {'status': 'FAIL_OR_BUDGET_UNKNOWN', 'phase': phase,
            'error': str(exc), 'source_literal_parses': source_parses,
            'candidate_literal_parses': candidate_parses, 'ordinary_candidate_BFS_roots': candidate_roots,
            'source_only_BFS_roots': 0, 'CPU_seconds': time.process_time() - START})
        status = 'FAIL_OR_BUDGET_UNKNOWN'
    write('TERMINAL.json', {'status': status, 'terminal': True, 'active_processes': 0,
        'ordinary_candidate_BFS_roots': candidate_roots, 'source_only_BFS_roots': 0,
        'CPU_seconds': time.process_time() - START, 'CPU_budget_seconds': args.cpu_budget})
    write('HANDLE.json', {'status': status, 'terminal': True, 'active_processes': 0})
    print(status)
    if status != 'PASS_PENDING_ROOT_ACCEPTANCE':
        raise SystemExit(2)


if __name__ == '__main__':
    main()
