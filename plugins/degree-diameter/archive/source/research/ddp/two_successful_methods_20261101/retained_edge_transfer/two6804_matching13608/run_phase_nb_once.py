"""One phase-capacity decision model; no source graph/field/diameter work."""
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent


def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def child():
    resource.setrlimit(resource.RLIMIT_CPU, (12, 12))
    started = time.process_time()
    import numpy as np
    from scipy.optimize._highspy import _core as h
    powers = json.loads((HERE / 'CONSTANT_PHASE_RESULT.json').read_text())['Q_powers_0_to3']
    starts, indices, values = [0], [], []
    for r in range(12):
        for s in range(12):
            indices.extend([r, 12+s])
            values.extend([1.0, 1.0])
            for i in range(12):
                for j in range(12):
                    v = sum(powers[a][(r-i) % 12] * powers[b][(j-s) % 12]
                            for a in range(4) for b in range(4-a))
                    v -= 26 * (r == i and s == j)
                    v -= 38 * (powers[1][(r-i) % 12] * (s == j) +
                               (r == i) * powers[1][(j-s) % 12])
                    if v:
                        indices.append(24+12*i+j)
                        values.append(float(v))
            starts.append(len(indices))
    lp = h.HighsLp()
    lp.num_col_, lp.num_row_ = 144, 168
    lp.col_cost_ = np.zeros(144)
    lower = np.zeros(144)
    lower[0] = 1
    lp.col_lower_ = lower
    lp.col_upper_ = np.ones(144)
    lp.row_lower_ = np.array([1.0]*24 + [567.0]*144)
    lp.row_upper_ = np.array([1.0]*24 + [h.kHighsInf]*144)
    lp.integrality_ = [h.HighsVarType.kInteger]*144
    lp.a_matrix_.format_ = h.MatrixFormat.kColwise
    lp.a_matrix_.num_col_, lp.a_matrix_.num_row_ = 144, 168
    lp.a_matrix_.start_ = np.array(starts, dtype=np.int32)
    lp.a_matrix_.index_ = np.array(indices, dtype=np.int32)
    lp.a_matrix_.value_ = np.array(values)
    np.savez(HERE/'NB_PHASE_CAPACITY_MODEL_INPUT.npz', starts=starts, indices=indices,
             values=values, lower=lower)
    save('NB_PHASE_CAPACITY_MODEL.json', dict(variables=144, permutation_rows=24,
         coverage_rows=144, nonzeros=len(values), target_per_phase=567,
         objective='feasibility0', pi0_equals0_capacity_gauge=True,
         time_limit_seconds=8, threads=1))
    solver = h._Highs()
    for k, v in [('threads', 1), ('time_limit', 8.0)]:
        if solver.setOptionValue(k, v) != h.HighsStatus.kOk:
            raise RuntimeError('required option failed')
    ps = solver.passModel(lp)
    save('NB_PHASE_PASS_MODEL.json', dict(status=str(ps), version=solver.version()))
    if ps != h.HighsStatus.kOk:
        raise RuntimeError('passModel failed; no retry')
    before = time.process_time()
    run = solver.run()
    solve_cpu = time.process_time() - before
    info, sol = solver.getInfo(), solver.getSolution()
    status = solver.getModelStatus()
    raw = dict(run_status=str(run), model_status=str(status),
               message=solver.modelStatusToString(status), solver_CPU=solve_cpu,
               nodes=info.mip_node_count, value_valid=bool(sol.value_valid))
    save('NB_PHASE_RAW_SOLVER.json', dict(**raw, columns=list(sol.col_value)))
    valid, pi, counts = False, None, None
    if sol.value_valid and len(sol.col_value) == 144:
        x = np.array(sol.col_value)
        z = np.rint(x).astype(int).reshape((12, 12))
        valid = bool(np.max(np.abs(x-z.reshape(144))) <= 1e-6 and
                     np.all((z == 0) | (z == 1)) and np.all(z.sum(0) == 1) and
                     np.all(z.sum(1) == 1) and z[0, 0] == 1)
        if valid:
            pi = [int(np.flatnonzero(z[r])[0]) for r in range(12)]
            # Direct integer walk sum; no lookup into the MIP coefficient matrix.
            counts = [[sum(powers[a][(r-i) % 12] * powers[b][(j-pi[r]) % 12]
                           for a in range(4) for b in range(4-a) for r in range(12))
                       for j in range(12)] for i in range(12)]
            inv = [pi.index(j) for j in range(12)]
            q = powers[1]
            counts = [[counts[i][j] - 26 * (pi[i] == j) -
                       38 * (q[(inv[j]-i) % 12] + q[(j-pi[i]) % 12])
                       for j in range(12)] for i in range(12)]
            valid = min(map(min, counts)) >= 567
    result = dict(status='FEASIBLE_NB_PHASE_PERMUTATION_CAPACITY_ONLY' if valid else
                  ('RAW_INFEASIBLE_UNCERTIFIED_NB_PHASE_PERMUTATION_MODEL' if
                   status == h.HighsModelStatus.kInfeasible else 'UNKNOWN_NB_PHASE_CAPACITY'),
                  raw=raw, handchecked=valid, permutation=pi if valid else None,
                  counts=counts if valid else None,
                  minimum_capacity=min(map(min, counts)) if valid else None,
                  row_totals=[sum(r) for r in counts] if valid else None,
                  actual_child_CPU=time.process_time()-started,
                  graph_generated=False, new_graph_parameter_Lean=[0, 0, 0],
                  source_BFS_field_Lean_ARIS=0, solver_calls=1,
                  note='NB capacity subtracts26P+38(QP+PQ);necessary walk upper bound,not point coverage.')
    save('NB_PHASE_CAPACITY_CHILD_RESULT.json', result)


def parent():
    if (HERE/'NB_PHASE_CAPACITY_ATTEMPT.json').exists():
        raise RuntimeError('one-shot already attempted; no automatic restart')
    save('NB_PHASE_CAPACITY_ATTEMPT.json', dict(pid=os.getpid(), calls=1))
    started = time.process_time()
    env = dict(os.environ)
    for k in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS']:
        env[k] = '1'
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    with (HERE/'NB_PHASE_SOLVER_STDOUT.log').open('w') as out, (HERE/'NB_PHASE_SOLVER_STDERR.log').open('w') as err:
        proc = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), '--child'],
                                env=env, cwd=HERE, stdout=out, stderr=err)
        save('NB_PHASE_CAPACITY_HANDLE.json', dict(status='RUNNING', running=True,
             driver_pid=os.getpid(), child_pid=proc.pid))
        try:
            rc = proc.wait(timeout=20)
        except subprocess.TimeoutExpired:
            proc.kill()
            rc = proc.wait()
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    child_cpu = after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    result = json.loads((HERE/'NB_PHASE_CAPACITY_CHILD_RESULT.json').read_text()) if (HERE/'NB_PHASE_CAPACITY_CHILD_RESULT.json').exists() else dict(status='UNKNOWN_NATIVE_NO_RESULT')
    result.update(native_return_code=rc, native_actual_CPU=child_cpu,
                  parent_actual_CPU=time.process_time()-started,
                  prior_ordinary_and_check_CPU=1.686393331, new_preparation_CPU_charge=0.3,
                  cumulative_CPU=1.986393331+child_cpu+time.process_time()-started,
                  cumulative_CPU_cap=15, terminal=True, running=False,
                  no_automatic_secondsolver=True)
    save('NB_PHASE_CAPACITY_RESULT.json', result)
    save('NB_PHASE_CAPACITY_TERMINAL.json', dict(status=result['status'], terminal=True,
         running=False, cumulative_CPU=result['cumulative_CPU'], CPU_cap=15,
         native_return_code=rc, native_actual_CPU=child_cpu))
    save('NB_PHASE_CAPACITY_HANDLE.json', dict(status=result['status'], running=False,
         driver_pid=os.getpid(), child_pid=proc.pid, native_return_code=rc))
    print(json.dumps({k: result.get(k) for k in ['status', 'minimum_capacity', 'permutation',
          'cumulative_CPU', 'native_return_code']}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    child() if '--child' in sys.argv else parent()
