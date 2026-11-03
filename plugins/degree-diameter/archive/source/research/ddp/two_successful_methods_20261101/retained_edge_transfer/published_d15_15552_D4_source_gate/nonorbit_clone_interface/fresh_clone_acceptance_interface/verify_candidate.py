#!/usr/bin/env python3
"""Prepared literal-only acceptance interface. Not executed during preparation.

Inputs: accepted headerless source rows `u neighbor...`, a new candidate with
`n m` header/strict lex body, and JSON {"centers": [old_label,...]}.
The mathematical all-pairs proof inherits the accepted source and the generic
full-neighborhood clone theorem. This tool performs zero BFS or Lean runs.
"""
import time
PROCESS_STARTED = time.process_time()
import argparse
import json
from pathlib import Path
import resource

SN = 15552
SM = 116316


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, type=Path)
    parser.add_argument('--candidate', required=True, type=Path)
    parser.add_argument('--centers', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--cpu-budget', required=True, type=float)
    args = parser.parse_args()
    start = PROCESS_STARTED
    here = Path(__file__).resolve().parent
    repo = next(p for p in here.parents if (p / 'formal/DegreeDiameter/Portfolio').is_dir())
    accepted_source = repo / 'research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt'
    accepted_final = repo / 'research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane837/formalization_full/FINAL.json'
    assert args.source.resolve() == accepted_source.resolve()
    assert not (args.out / 'TERMINAL.json').exists(), 'Do not overwrite a terminal acceptance.'
    # The root supplies the run budget only after seeing an actual new candidate.
    seconds = max(1, int(args.cpu_budget))
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds))
    args.out.mkdir(parents=True, exist_ok=True)

    def write(name, value):
        (args.out / name).write_text(json.dumps(value, indent=2) + '\n')

    phase = 'new_candidate_input_binding'
    source_parses = candidate_parses = 0
    try:
        inherited = json.loads(accepted_final.read_text())
        assert inherited['source_full_claim_complete']
        assert inherited['source_original_target'] == 'DegreeDiameter.Portfolio.F3Graph15552.d15_15552'
        data = json.loads(args.centers.read_text())
        centers = data if isinstance(data, list) else data['centers']
        assert all(type(c) is int and 0 <= c < SN for c in centers)
        assert len(centers) == len(set(centers))
        K = len(centers)
        assert K > 864, 'This new interface is not an invitation to rerun old864 acceptance.'
        N = SN + K
        write('HANDLE.json', {'status': 'RUNNING', 'phase': phase,
            'candidate': str(args.candidate), 'roles': K, 'CPU_budget_seconds': args.cpu_budget})

        # Bind the accepted source literal as input; no source D4 suite or BFS.
        S = []
        with args.source.open() as stream:
            source_parses += 1
            for row, line in enumerate(stream):
                values = list(map(int, line.split()))
                assert values and values[0] == row
                S.append(sorted(values[1:]))
        assert len(S) == SN
        source_edges = [(u, v) for u in range(SN) for v in S[u] if u < v]
        assert len(source_edges) == SM
        load = [0] * SN
        expected_added = 0
        for c in centers:
            assert S[c], 'Full-neighborhood clone needs a nonisolated center.'
            expected_added += len(S[c])
            for v in S[c]:
                load[v] += 1
        expected_degree = [len(S[v]) + load[v] for v in range(SN)] + [len(S[c]) for c in centers]
        assert max(expected_degree) <= 16
        M = SM + expected_added
        degree = [0] * N
        actual_new_N = [[] for _ in range(K)]
        phase = 'one_new_candidate_stream'
        old_index = count = added = 0
        prior = (-1, -1)
        with args.candidate.open() as stream:
            candidate_parses += 1
            assert tuple(map(int, next(stream).split())) == (N, M)
            for line in stream:
                a, b = map(int, line.split())
                assert 0 <= a < b < N and prior < (a, b)
                prior = (a, b)
                if b < SN:
                    assert old_index < SM and source_edges[old_index] == (a, b)
                    old_index += 1
                else:
                    assert a < SN, 'No clone-clone edges are permitted.'
                    actual_new_N[b - SN].append(a)
                    added += 1
                degree[a] += 1
                degree[b] += 1
                count += 1
        assert count == M and old_index == SM and added == expected_added
        for j, c in enumerate(centers):
            assert actual_new_N[j] == S[c], f'role{j} must freeze the complete original simple N'
            assert c not in actual_new_N[j]
        assert degree == expected_degree and max(degree) <= 16

        # Exact pointwise degree formula permits load2 at source-degree14 if it
        # occurs legally; do not add an unstated load<=1 restriction.
        histogram = {}
        load_histogram = {}
        for d in degree:
            histogram[str(d)] = histogram.get(str(d), 0) + 1
        for d in load:
            load_histogram[str(d)] = load_histogram.get(str(d), 0) + 1
        with (args.out / 'ALL_NEW_ROLE_BINDINGS.tsv').open('w') as stream:
            stream.write('j\told_center_label\tcontroller\tfiber_offset\tnew_label\tactual_source_N_size\tactual_new_N_size\tfull_N_equal\tactual_old_simple_neighbors\n')
            for j, c in enumerate(centers):
                stream.write(f'{j}\t{c}\t{c//81}\t{c%81}\t{SN+j}\t{len(S[c])}\t{len(actual_new_N[j])}\ttrue\t' +
                    ' '.join(map(str, actual_new_N[j])) + '\n')
        proof = (here / 'STRUCTURE_PROOF_DRAFT.md').read_text()
        proof = proof.replace('{{N}}', str(N)).replace('{{K}}', str(K)).replace('{{M}}', str(M))
        (args.out / 'STRUCTURE_PROOF.md').write_text(proof)
        write('RESULT.json', {
            'status': 'LITERAL_BINDING_PASS_ALLPAIR_D4_BY_ACCEPTED_SOURCE_AND_GENERIC_FULLN',
            'n': N, 'm': M, 'source_n': SN, 'source_m': SM, 'new_roles': K,
            'source_edges_retained_exact': old_index, 'new_old_edges': added, 'new_new_edges': 0,
            'strict_lex_simple_header_complete': True, 'all_ordered_full_N_roles_bound': K,
            'degree_histogram': histogram, 'old_load_histogram': load_histogram,
            'maximum_old_load': max(load), 'actual_maximum_degree': max(degree), 'Delta_cap': 16,
            'pointwise_degree_formula_checked': True, 'label_recipe': 'newlabel=15552+j, center=centers[j]',
            'source_literal_parses': source_parses, 'candidate_literal_parses': candidate_parses,
            'allpair_upper_D': 4, 'allpair_proof': 'STRUCTURE_PROOF.md',
            'inherited_source_FINAL': str(accepted_final.relative_to(repo)),
            'source_kernel_target': 'DegreeDiameter.Portfolio.F3Graph15552.d15_15552',
            'source_nonD3_witness_old_labels': [0, 81],
            'nonD3_transfer': 'FullNeighborhoodClones.old_walk_bound_iff/collapseHom',
            'actual_new_concrete_Lean_checked': False,
            'new_BFS_source_validity_field_Lean_solver_review_runs': 0,
            'CPU_seconds': time.process_time() - start, 'CPU_budget_seconds': args.cpu_budget,
        })
        final_status = 'PASS_PENDING_ROOT_ACCEPTANCE'
    except Exception as exc:
        write('FAILURE.json', {'status': 'FAIL_OR_UNKNOWN_INPUT_BINDING', 'phase': phase,
            'error': str(exc), 'source_literal_parses': source_parses,
            'candidate_literal_parses': candidate_parses, 'CPU_seconds': time.process_time() - start})
        final_status = 'FAIL_OR_UNKNOWN_INPUT_BINDING'
    write('TERMINAL.json', {'status': final_status, 'terminal': True, 'active_processes': 0,
        'CPU_seconds': time.process_time() - start, 'CPU_budget_seconds': args.cpu_budget,
        'ordinary_BFS_or_Lean_runs': 0})
    write('HANDLE.json', {'status': final_status, 'terminal': True, 'active_processes': 0})
    print(final_status)
    if final_status != 'PASS_PENDING_ROOT_ACCEPTANCE':
        raise SystemExit(2)


if __name__ == '__main__':
    main()
