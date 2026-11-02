#!/usr/bin/env python3
"""One FP-coverage feasibility solve; at most one frozen 15-pairing prototype."""
import time
START = time.process_time()
import os
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import csv
import json
import math
from pathlib import Path
import resource
import traceback
import warnings

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
CACHE = REPO / 'research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate'
PRIOR = 1.50087698
PREP = .25
resource.setrlimit(resource.RLIMIT_CPU, (40, 40))


def write(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2) + '\n')


def elapsed():
    return time.process_time() - START


write('FP_HANDLE.json', {'status': 'PREPARING_SINGLE_MODEL', 'pid': os.getpid(),
    'single_worker': True, 'prior_case_CPU_seconds': PRIOR,
    'new_preparation_charge_CPU_seconds': PREP, 'wholecase_CPU_cap_seconds': 45,
    'process_hard_CPU_seconds': 40, 'solver_time_limit_seconds': 20})
solver_calls = 0
result = None
try:
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
    from scipy.sparse import coo_matrix, save_npz

    structure = json.loads((CACHE / 'STRUCTURE_ROOT.json').read_text())
    P, F = structure['P_vertices'], structure['F_vertices']
    pset, fset = set(P), set(F)
    source = REPO / 'research/ddp/more_graphs_20261027/d3d4_transfer/source650.implicit_adj.txt'
    adj = [set(map(int, line.split())) for line in source.read_text().splitlines() if line.strip()]
    assert len(adj) == 650
    source_edges = {(u, v) for u in range(650) for v in adj[u] if u < v}
    FP = sorted((f, p) for f in F for p in adj[f] & pset)
    assert len(FP) == 1040
    pindex, findex = {p: i for i, p in enumerate(P)}, {f: i for i, f in enumerate(F)}
    A2 = np.fromfile(CACHE / 'A2.u16le.bin', dtype='<u2').reshape(650, 650)
    R2 = A2 > 0
    np.fill_diagonal(R2, True)
    for u in range(650):
        R2[u, list(adj[u])] = True
    f_targets = np.asarray(F, dtype=np.int32)

    row_ids, col_ids, values, lower, upper, row_labels = [], [], [], [], [], []

    def newrow(label, lo=-np.inf, hi=np.inf):
        index = len(lower)
        row_labels.append(label)
        lower.append(lo)
        upper.append(hi)
        return index

    frows = {f: newrow(['distinct_cut_F', f], hi=1) for f in F}
    prows = {p: newrow(['distinct_cut_P', p], hi=1) for p in P}
    donor_rows = {p: newrow(['starP_requires_donorP', p], hi=0) for p in P}
    cuts_sum = newrow(['eight_FP_cuts'], 8, 8)
    star_sum = newrow(['two_star_P'], 2, 2)
    cover_rows = [newrow(['F_target_R2_coverage', f], lo=1) for f in F]

    def add(row, col, value=1):
        row_ids.append(row)
        col_ids.append(col)
        values.append(value)

    for e, (f, p) in enumerate(FP):
        add(frows[f], e)
        add(prows[p], e)
        add(donor_rows[p], e, -1)
        add(cuts_sum, e)
        for target in np.flatnonzero(R2[f, f_targets]):
            add(cover_rows[int(target)], e)
    for i, p in enumerate(P):
        variable = 1040 + i
        add(donor_rows[p], variable)
        add(star_sum, variable)
        for target in np.flatnonzero(R2[p, f_targets]):
            add(cover_rows[int(target)], variable)
    matrix = coo_matrix((np.asarray(values, dtype=float),
        (np.asarray(row_ids, dtype=np.int32), np.asarray(col_ids, dtype=np.int32))),
        shape=(len(lower), 1170)).tocsc()
    save_npz(HERE / 'FP_MODEL_MATRIX.npz', matrix)
    variable_labels = [['cut_FP', f, p] for f, p in FP] + [['star_P', p] for p in P]
    write('FP_MODEL.json', {'binary_variables': 1170, 'FP_variables': 1040, 'starP_variables': 130,
        'rows': len(lower), 'nonzeros': matrix.nnz, 'variable_labels': variable_labels,
        'row_labels': row_labels, 'row_lower': [None if not math.isfinite(x) else x for x in lower],
        'row_upper': [None if not math.isfinite(x) else x for x in upper],
        'bound_interpretation': 'None lower=-infinity, None upper=+infinity; variables allbinary0..1',
        'objective': 'allzero feasibility', 'solver_options': {'threads': 1, 'time_limit': 20., 'presolve': True},
        'ordinary_A2_input': str((CACHE / 'A2.u16le.bin').relative_to(REPO)),
        'new_walk_matrix_or_source_BFS_computations': 0})
    write('FP_HANDLE.json', {'status': 'SOLVING_SINGLE_F_COVER_MODEL', 'pid': os.getpid(),
        'solver': 'SciPy milp / HiGHS', 'variables': 1170, 'rows': len(lower), 'nonzeros': matrix.nnz,
        'threads': 1, 'time_limit_seconds': 20, 'CPU_before_solver': elapsed(),
        'prior_case_CPU_seconds': PRIOR, 'wholecase_CPU_cap_seconds': 45})
    solve_start = time.process_time()
    solver_calls += 1
    with warnings.catch_warnings(record=True) as caught:
        solution = milp(np.zeros(1170), integrality=np.ones(1170, dtype=np.uint8),
            bounds=Bounds(np.zeros(1170), np.ones(1170)),
            constraints=LinearConstraint(matrix, np.asarray(lower), np.asarray(upper)),
            options={'threads': 1, 'time_limit': 20., 'presolve': True})
    solver_cpu = time.process_time() - solve_start

    def numeric(value):
        if value is None:
            return None
        value = float(value)
        return value if math.isfinite(value) else None

    raw_solver = {'status': int(solution.status), 'success': bool(solution.success),
        'message': str(solution.message), 'fun': numeric(solution.fun),
        'mip_node_count': numeric(getattr(solution, 'mip_node_count', None)),
        'mip_dual_bound': numeric(getattr(solution, 'mip_dual_bound', None)),
        'mip_gap': numeric(getattr(solution, 'mip_gap', None)), 'CPU_seconds': solver_cpu,
        'warnings': [str(w.message) for w in caught],
        'incumbent': None if solution.x is None else solution.x.tolist(),
        'infeasibility_certificate_checked': False}
    write('FP_SOLVER_RETURN.json', raw_solver)
    if solution.x is None:
        result = {'status': 'NUMERICAL_MIP_INFEASIBLE_NO_CERTIFIED_FAMILY_NO' if solution.status == 2 else
            'UNKNOWN_F_COVER_MODEL_NO_INCUMBENT', 'solver_return': raw_solver,
            'candidate_pairings_checked': 0, 'newroot_BFS_count': 0, 'oldroot_BFS_count': 0,
            'scope': 'one numeric feasibility window; not a certified global FP-transfer family exclusion',
            'next': 'STOP no second solve/seed/model/prototype'}
    else:
        selected = np.rint(solution.x).astype(int)
        assert np.max(np.abs(solution.x - selected)) < 1e-5
        assert np.all((selected == 0) | (selected == 1))
        cut_ids = [i for i in range(1040) if selected[i]]
        cuts = [FP[i] for i in cut_ids]
        star_P = sorted(P[i] for i in range(130) if selected[1040 + i])
        donors_P = sorted(p for f, p in cuts)
        donors_F = sorted(f for f, p in cuts)
        assert len(cuts) == len(set(donors_F)) == len(set(donors_P)) == 8
        assert len(star_P) == 2 and set(star_P) <= set(donors_P)
        assert all(p in adj[f] for f, p in cuts)
        star_pins = sorted(donors_F + star_P)
        literal_coverage = set()
        for pin in star_pins:
            literal_coverage.add(pin)
            literal_coverage.update(adj[pin])
            for neighbor in adj[pin]:
                literal_coverage.update(adj[neighbor])
        assert fset <= literal_coverage
        leftover = sorted(set(donors_P) - set(star_P))
        assert len(leftover) == 6
        frozen = {'cut_variable_ids': cut_ids, 'eight_actual_FP_cuts': [list(e) for e in cuts],
            'eight_F_labels': donors_F, 'eight_P_donors': donors_P, 'two_starP_labels': star_P,
            'newroot_label': 650, 'ten_actual_star_pins': star_pins, 'remaining_six_P': leftover,
            'independent_selected_literal_F_R2_coverage': len(literal_coverage & fset),
            'domain_and_cover_handcheck': 'PASS', 'prototype_frozen_no_second_incumbent': True}
        write('FP_FROZEN_PROTOTYPE.json', frozen)

        def pairings(vertices):
            if not vertices:
                yield []
                return
            a = vertices[0]
            for j in range(1, len(vertices)):
                b = vertices[j]
                rest = vertices[1:j] + vertices[j + 1:]
                for tail in pairings(rest):
                    yield [(a, b)] + tail

        all_pairings = list(pairings(leftover))
        assert len(all_pairings) == 15
        write('FP_HANDLE.json', {'status': 'TESTING_FROZEN_15_PP_PAIRINGS', 'pid': os.getpid(),
            'solver_calls': 1, 'frozen_prototype': frozen, 'prior_case_CPU_seconds': PRIOR,
            'CPU_before_pairings': elapsed(), 'wholecase_CPU_cap_seconds': 45})

        def bfs(graph, root):
            distance = [-1] * 651
            parent = [-1] * 651
            queue = [root]
            distance[root] = 0
            for u in queue:
                for v in graph[u]:
                    if distance[v] < 0:
                        distance[v] = distance[u] + 1
                        parent[v] = u
                        queue.append(v)
            return distance, parent

        def route(distance, parent, target):
            if distance[target] < 0:
                return []
            result = []
            while target != -1:
                result.append(target)
                target = parent[target]
            return result[::-1]

        def histogram(distance):
            result = {}
            for d in distance:
                result[str(d)] = result.get(str(d), 0) + 1
            return result

        A3 = None

        def source_pair_diagnostic(u, v):
            nonlocal_placeholder = None
            global A3
            if v in adj[u]:
                oldpath = [u, v]
            elif A2[u, v] > 0:
                mid = min(adj[u] & adj[v])
                oldpath = [u, mid, v]
            else:
                if A3 is None:
                    A3 = np.fromfile(CACHE / 'A3.u16le.bin', dtype='<u2').reshape(650, 650)
                assert A3[u, v] > 0
                oldpath = None
                for first in sorted(adj[u]):
                    if A2[first, v] > 0:
                        last = min(adj[first] & adj[v])
                        oldpath = [u, first, last, v]
                        break
                assert oldpath is not None
            cutset = {tuple(sorted(e)) for e in cuts}
            return {'old_pair': [u, v], 'source_distance': len(oldpath) - 1,
                'one_old_source_shortest_route': oldpath,
                'cuts_on_this_route': [list(sorted((a, b))) for a, b in zip(oldpath, oldpath[1:])
                    if tuple(sorted((a, b))) in cutset],
                'source_BFS': 0, 'old_shortest_route_not_claimed_unique': True}

        pairing_records = []
        first_old_diagnostic = None
        full_hit = False
        new_BFS = old_BFS = 0
        new_pass = old_failed = 0
        time_stop = False
        root_order = donors_P + [v for v in range(650) if v not in set(donors_P)]
        for pid, repairs in enumerate(all_pairings):
            if elapsed() > 38:
                time_stop = True
                break
            graph = [neighbors.copy() for neighbors in adj] + [set()]
            for f, p in cuts:
                graph[f].remove(p)
                graph[p].remove(f)
            for pin in star_pins:
                graph[650].add(pin)
                graph[pin].add(650)
            added = []
            preserved = []
            for p, q in repairs:
                if q in adj[p]:
                    preserved.append([p, q])
                else:
                    added.append([p, q])
                    graph[p].add(q)
                    graph[q].add(p)
            degrees = [len(g) for g in graph]
            assert max(degrees) <= 10 and min(degrees) >= 9
            edges_count = sum(degrees) // 2
            assert edges_count == 3252 + len(added)
            degree_hist = {str(d): degrees.count(d) for d in sorted(set(degrees))}
            g = [sorted(neighbors) for neighbors in graph]
            distance, parent = bfs(g, 650)
            new_BFS += 1
            fmiss = [f for f in F if distance[f] < 0 or distance[f] > 3]
            pmiss = [p for p in P if distance[p] < 0 or distance[p] > 3]
            bad = next((v for v in range(651) if distance[v] < 0 or distance[v] > 3), None)
            record = {'pairing_id': pid, 'actual_repair_pairs': [list(e) for e in repairs],
                'actual_new_PP_edges': added, 'already_old_PP_edges_preserved': preserved,
                'n': 651, 'actual_m': edges_count, 'degree_histogram': degree_hist,
                'newroot_histogram': histogram(distance), 'newroot_missing_F_count': len(fmiss),
                'newroot_missing_P_count': len(pmiss), 'newroot_measured': True,
                'oldroots_measured': 0, 'full_graph_accepted': False}
            stats = [{'root': 650, 'histogram': histogram(distance)}]
            if bad is not None:
                record.update({'stage': 'NEWROOT_FAIL', 'first_failed_pair': [650, bad],
                    'actual_shortest_distance': distance[bad], 'actual_shortest_path': route(distance, parent, bad)})
            else:
                new_pass += 1
                witness_target = next(v for v in range(651) if distance[v] == 3)
                record['distance3_witness'] = route(distance, parent, witness_target)
                record['stage'] = 'FULL_HIT_PENDING_FRESH_ACCEPTANCE'
                for root in root_order:
                    if elapsed() > 38:
                        time_stop = True
                        record['stage'] = 'UNKNOWN_OLDROOT_CPU_CAP'
                        break
                    distance, parent = bfs(g, root)
                    old_BFS += 1
                    record['oldroots_measured'] += 1
                    stats.append({'root': root, 'histogram': histogram(distance)})
                    bad = next((v for v in range(651) if distance[v] < 0 or distance[v] > 3), None)
                    if bad is not None:
                        old_failed += 1
                        record.update({'stage': 'OLDROOT_FAIL', 'first_failed_pair': [root, bad],
                            'actual_shortest_distance': distance[bad], 'actual_shortest_path': route(distance, parent, bad)})
                        if first_old_diagnostic is None:
                            first_old_diagnostic = source_pair_diagnostic(root, bad)
                            write('FP_FIRST_OLDPAIR_SOURCE_ROUTE_DIAGNOSTIC.json', first_old_diagnostic)
                        break
                if record['stage'] == 'FULL_HIT_PENDING_FRESH_ACCEPTANCE':
                    assert record['oldroots_measured'] == 650
                    full_hit = True
                    with (HERE / 'graph_d10_D3_n651.edges').open('w') as stream:
                        stream.write(f'651 {edges_count}\n')
                        for u in range(651):
                            for v in g[u]:
                                if u < v:
                                    stream.write(f'{u} {v}\n')
                    write('FP_HIT_PARAMETERS.json', {'frozen': frozen, 'pairing': record})
                    write('FP_HIT_ALL651_ROOT_STATS.json', stats)
            pairing_records.append(record)
            write(f'FP_PAIRING{pid:02d}.json', record)
            if full_hit or time_stop:
                break
        write('FP_ALL_PAIRING_RESULTS.json', pairing_records)
        complete = len(pairing_records) == 15 and not full_hit and not time_stop
        result = {'status': 'FULL651_D3_HIT_PENDING_FRESH_ACCEPTANCE' if full_hit else
            'COMPLETE_NO_THIS_FROZEN_FP_PROTOTYPE_ALL15_PP_PAIRINGS_FAMILY_UNKNOWN' if complete else
            'UNKNOWN_FROZEN_FP_PROTOTYPE_CPU_CAP', 'solver_status': raw_solver['status'],
            'solver_CPU_seconds': solver_cpu, 'frozen_prototype': frozen,
            'pairing_domain_size': 15, 'candidate_pairings_checked': len(pairing_records),
            'newroot_BFS_count': new_BFS, 'oldroot_BFS_count': old_BFS,
            'newroot_pass_pairings': new_pass, 'oldroot_failed_pairings': old_failed,
            'full_hit': full_hit, 'selected_pairing_domain_complete': complete,
            'source_single_pair_diagnostic_count': int(first_old_diagnostic is not None),
            'core_coverage_prediction_for_incumbent': 'SUPPORTED_BY_LITERAL_SELECTED_ROOTS',
            'actual_candidate_newroot_F_misses': sum(r['newroot_missing_F_count'] for r in pairing_records),
            'scope': 'one frozen8FP/2Pstar prototype; at most all15 exact PP pairings, existingPP branches included; wholeFPtransfer familyUNKNOWN',
            'next': 'STOP; no second solve, prototype, seed, or repairs'}
    result.update({'solver_calls': solver_calls, 'source_literal_input_parses': 1,
        'old_A2_reused': True, 'source_D3_or_source_allroot_BFS': 0,
        'new_source_walk_matrix_or_field_Lean_or_review': 0})
except Exception as exc:
    result = {'status': 'UNKNOWN_FP_PROCESS_OR_INPUT_FAILURE', 'error': str(exc),
        'traceback': traceback.format_exc(), 'solver_calls': solver_calls,
        'scope': 'no uncompleted or uncertified family exclusion', 'next': 'STOP preserve spent cost/failure'}

actual = elapsed()
total = PRIOR + PREP + actual
result.update({'prior_read_CPU_seconds': PRIOR, 'new_preparation_charge_CPU_seconds': PREP,
    'actual_parent_all_threads_CPU_seconds': actual, 'actual_children_CPU_seconds': 0,
    'wholecase_CPU_seconds': total, 'wholecase_CPU_cap_seconds': 45})
write('FP_RESULT.json', result)
write('FP_TERMINAL.json', {**result, 'terminal': True, 'active_processes': 0})
write('FP_HANDLE.json', {'status': result['status'], 'pid': os.getpid(), 'terminal': True,
    'active_processes': 0, 'wholecase_CPU_seconds': total})
print(json.dumps({k: result[k] for k in ('status', 'solver_calls', 'candidate_pairings_checked',
    'newroot_BFS_count', 'oldroot_BFS_count', 'newroot_pass_pairings', 'oldroot_failed_pairings',
    'full_hit', 'wholecase_CPU_seconds', 'error') if k in result}))
