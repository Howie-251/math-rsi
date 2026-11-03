"""One bounded full-column constraint-generation feasibility experiment."""
from pathlib import Path
import json
import os
import resource
import signal
import time
import warnings

START_CPU, START_WALL = time.process_time(), time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (59, 60))
for name in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS']:
    os.environ[name] = '1'
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix, vstack
import scipy

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
CACHE = BASE / 'allfree_cover_probe'
N, K, W = 94186, 3685, 1472
SOLVER_LIMIT = 29.0
solver_cpu = 0.0


class BudgetReached(Exception):
    pass


def cpu():
    return time.process_time() - START_CPU


def wall():
    return time.monotonic() - START_WALL


def signal_stop(*_):
    raise BudgetReached()


signal.signal(signal.SIGXCPU, signal_stop)
signal.signal(signal.SIGTERM, signal_stop)


def checkpoint():
    if cpu() > 56 or wall() > 170 or solver_cpu >= SOLVER_LIMIT:
        raise BudgetReached()


def save(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2) + '\n')


def scalar(result, key):
    x = getattr(result, key, None)
    return None if x is None or not np.isfinite(x) else float(x)


def main():
    global solver_cpu
    assert json.loads((OUT / 'PREDICTION.json').read_text())['status'] == 'FROZEN_BEFORE_GLOBAL_MIP'
    assert not (OUT / 'RESULT.json').exists(), 'This bounded experiment is already terminal.'
    meta = json.loads((CACHE / 'BALLS_META.json').read_text())
    ports = json.loads((BASE / 'free_ports.json').read_text())
    assert meta['complete'] and meta['source_n'] == N and meta['source_m'] == 657452
    assert meta['words_per_row'] == W and len(meta['free_vertices']) == K
    pins = meta['free_vertices']
    assert pins == meta['computed_vertices'] == ports['ports']
    assert ports['source_n'] == N and ports['source_m'] == 657452
    assert len(set(pins)) == K and all(d < 14 for d in ports['degrees'])
    rawpath = CACHE / 'allfree_R4.u64le.bin'
    assert rawpath.stat().st_size == K * W * 8
    balls = np.memmap(rawpath, dtype='<u8', mode='r', shape=(K, W))
    support = np.fromfile(CACHE / 'target_support.u16le.bin', dtype='<u2')
    assert len(support) == N and int(support.min()) == 455 and int(support.max()) == 824
    order = np.lexsort((np.arange(N), support))
    initial = sorted(set(map(int, order[:128])) |
                     set(map(int, np.linspace(0, N - 1, 128, dtype=int))))
    active, active_set, coverers = [], set(), {}

    def add_rows(targets):
        for v in targets:
            v = int(v)
            if v not in active_set:
                idx = np.flatnonzero((balls[:, v >> 6] >> np.uint64(v & 63)) & np.uint64(1)).astype(np.int32)
                assert len(idx) == int(support[v])
                coverers[v] = idx
                active.append(v)
                active_set.add(v)

    add_rows(initial)
    save('BINDING.json', {
        'source_n': N, 'source_m': 657452,
        'source_graph': 'source94186.edges', 'cache_directory': '../allfree_cover_probe',
        'all_columns': K, 'free_vertices_exactly_match_cached_degrees': True,
        'complete_cached_ball_rows': K, 'words_per_ball': W,
        'scipy_version': scipy.__version__, 'solver': 'scipy.optimize.milp/HiGHS',
        'threads': 1, 'initial_target_ids': initial,
        'candidate_preservation': 'Every active row is an exact originaltarget constraint; all3685columns remain.'})
    print(json.dumps({'stage': 'BOUND', 'initial_constraints': len(active),
                      'CPU_seconds': cpu(), 'solver': 'SciPy/HiGHS'}), flush=True)
    iterations, hit = [], None
    terminal = 'UNKNOWN_MODEL_CANDIDATE_LIMIT'
    try:
        for number in range(1, 9):
            checkpoint()
            lengths = [len(coverers[v]) for v in active]
            indptr = np.empty(len(active) + 1, dtype=np.int64)
            indptr[0] = 0
            np.cumsum(lengths, out=indptr[1:])
            indices = np.concatenate([coverers[v] for v in active])
            rows = csr_matrix((np.ones(len(indices), dtype=np.float64), indices, indptr),
                              shape=(len(active), K))
            cap = csr_matrix(np.ones((1, K), dtype=np.float64))
            matrix = vstack([rows, cap], format='csc')
            lower = np.r_[np.ones(len(active)), 0.0]
            upper = np.r_[np.full(len(active), np.inf), 14.0]
            remaining = SOLVER_LIMIT - solver_cpu
            allowance = min(5.0 if number == 1 else 8.0, remaining - 0.15,
                            54.0 - cpu(), 165.0 - wall())
            if allowance <= 0.2:
                terminal = 'UNKNOWN_CUMULATIVE_BUDGET'
                break
            save('run.json', {'running': True, 'pid': os.getpid(), 'stage': 'HiGHS_milp',
                              'model_number': number, 'active_targets': len(active),
                              'all_columns': K, 'solver_CPU_used': solver_cpu,
                              'this_time_limit_wall_seconds': allowance,
                              'whole_CPU_seconds': cpu(), 'whole_wall_seconds': wall()})
            began = time.process_time()
            # SciPy forwards threads to HiGHS even though it is not a documented
            # top-level scipy option. One-thread setting is explicit.
            with warnings.catch_warnings():
                warnings.filterwarnings('ignore', message='Unrecognized options detected:.*threads.*')
                answer = milp(np.zeros(K), integrality=np.ones(K), bounds=Bounds(0, 1),
                              constraints=LinearConstraint(matrix, lower, upper),
                              options={'time_limit': allowance, 'presolve': True,
                                       'mip_rel_gap': 0.0, 'threads': 1, 'disp': False})
            used = time.process_time() - began
            solver_cpu += used
            item = {'model_number': number, 'active_target_count': len(active),
                    'matrix_nonzeros': int(matrix.nnz), 'solver_raw_status': int(answer.status),
                    'solver_message': str(answer.message), 'solver_CPU_seconds': used,
                    'cumulative_solver_CPU_seconds': solver_cpu,
                    'solver_mip_node_count': scalar(answer, 'mip_node_count'),
                    'solver_objective': scalar(answer, 'fun'),
                    'solver_dual_bound_for_zero_objective': scalar(answer, 'mip_dual_bound'),
                    'model_is_full_target_system': len(active) == N,
                    'LP_minimum_cardinality_computed': False}
            if answer.x is None:
                terminal = ('UNTRUSTED_SOLVER_INFEASIBLE_SUBMODEL' if answer.status == 2
                            else 'UNKNOWN_NO_INTEGER_INCUMBENT')
                item['integer_incumbent'] = False
                iterations.append(item)
                save(f'model_{number:02d}.json', item)
                print(json.dumps({'stage': terminal, 'model': number,
                                  'solver_CPU_seconds': solver_cpu,
                                  'active_targets': len(active)}), flush=True)
                break
            x = np.asarray(answer.x)
            if np.max(np.abs(x - np.rint(x))) > 1e-6:
                terminal = 'LP_ONLY_NO_INTEGER_INCUMBENT'
                item['integer_incumbent'] = False
                iterations.append(item)
                save(f'model_{number:02d}.json', item)
                break
            selected = np.flatnonzero(x > 0.5)
            assert len(selected) <= 14
            assert all(bool(np.any(x[coverers[v]] > 0.5)) for v in active)
            union = np.bitwise_or.reduce(balls[selected], axis=0) if len(selected) else np.zeros(W, dtype='<u8')
            missing = np.flatnonzero(np.unpackbits(union.view(np.uint8), bitorder='little')[:N] == 0)
            selected_pins = [int(pins[j]) for j in selected]
            item.update(integer_incumbent=True, literal_pins=selected_pins,
                        selected_columns=list(map(int, selected)),
                        complete_cached_R4_missing_count=len(missing),
                        missing_target_sample=list(map(int, missing[:20])),
                        complete_cached_R4_verified=True)
            print(json.dumps({'stage': 'MODEL_CANDIDATE_CHECKED', 'model': number,
                              'pins': len(selected_pins), 'full_cached_missing': len(missing),
                              'solver_CPU_seconds': solver_cpu}), flush=True)
            if not len(missing):
                assert all(ports['degrees'][j] < 14 for j in selected)
                hit = {'n': N + 1, 'm': 657452 + len(selected_pins),
                       'source_n': N, 'source_m': 657452, 'literal_pins': selected_pins,
                       'old_pin_degrees': [int(ports['degrees'][j]) for j in selected],
                       'new_vertex': N, 'new_degree': len(selected_pins),
                       'actual_current_cached_R4_missing': 0,
                       'all_old_edges_retained': True, 'D5_source': 'Inheritedpublishedsource',
                       'new_graph_D5_scope': 'CompletecachedR4plusoldsourceD5 singleextension induction; rootindependentacceptance pending.',
                       'independent_check_pending': True, 'record_claimed': False}
                with (BASE / 'source94186.edges').open() as source, (OUT / 'hit94187.edges').open('w') as target:
                    target.write(f'{N+1} {hit["m"]}\n')
                    count = 0
                    for line in source:
                        if not line.strip() or line.lstrip().startswith('#'):
                            continue
                        target.write(line if line.endswith('\n') else line + '\n')
                        count += 1
                    assert count == 657452
                    for p in selected_pins:
                        target.write(f'{N} {p}\n')
                save('hit_parameters.json', hit)
                terminal = 'FULL94187_CACHED_COVER_PENDING_ROOT'
                iterations.append(item)
                save(f'model_{number:02d}.json', item)
                print(json.dumps({'stage': terminal, 'literal_pins': selected_pins}), flush=True)
                break
            low = missing[np.lexsort((missing, support[missing]))[:512]]
            spread = missing[np.linspace(0, len(missing) - 1, min(512, len(missing)), dtype=int)]
            cuts = sorted(set(map(int, low)) | set(map(int, spread)))
            cuts = [v for v in cuts if v not in active_set]
            assert cuts
            item['exact_violated_target_cuts'] = cuts
            iterations.append(item)
            save(f'model_{number:02d}.json', item)
            add_rows(cuts)
    except BudgetReached:
        terminal = 'UNKNOWN_CUMULATIVE_PROCESS_BUDGET'
    result = {
        'status': terminal, 'running': False, 'source_n': N, 'source_m': 657452,
        'target_Delta': 14, 'target_D': 5, 'public_savedL': 94186,
        'all_free_columns': K, 'all_old_targets': N,
        'models_run': len(iterations),
        'integer_model_candidates_checked': sum(r.get('integer_incumbent', False) for r in iterations),
        'maximum_model_candidates': 8, 'final_active_target_count': len(active),
        'solver_CPU_seconds': solver_cpu, 'solver_CPU_budget_seconds': 30,
        'whole_CPU_seconds': cpu(), 'whole_wall_seconds': wall(),
        'whole_CPU_limit_seconds': 60, 'whole_wall_limit_seconds': 180,
        'full_cached_cover_found': hit is not None,
        'new_graphs': int(hit is not None), 'actual_n': N + 1 if hit else None,
        'actual_D': None, 'ordinary_bad_unordered_pairs': None,
        'LP_minimum_cardinality_computed': False,
        'trusted_UNSAT_certificate': False, 'family_strictly_excluded': False,
        'prediction_exists': 'SUPPORTED' if hit else 'UNRESOLVED',
        'prediction_operational': 'SUPPORTED' if hit else 'REFUTED_WITHIN_FIXED_WINDOW',
        'all_original_candidates_preserved': True,
        'new_BFS': 0, 'old_ball_recomputation': 0, 'greedy_runs': 0,
        'pending': ['Rootindependentnewgraphcheck'] if hit else [],
        'decision': 'Stop this bounded coordinatedmodel experiment; no automatic timeextension or restart.'}
    save('iterations.json', iterations)
    save('RESULT.json', result)
    save('terminal.json', result)
    save('run.json', result)
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
