"""The sole passModel/setSolution/run process; only launched after root's condition."""
import argparse
import collections
import csv
import json
import math
import os
from pathlib import Path
import resource
import time
import traceback

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'formal/lean-toolchain').is_file())
CASE = HERE.parent.parent
N = 15552


def save(name, value):
    p = HERE/name
    q = p.with_suffix(p.suffix+'.tmp')
    q.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    q.replace(p)


def clean(v):
    if isinstance(v, (bool, int, str)) or v is None:
        return v
    if isinstance(v, float):
        return v if math.isfinite(v) else str(v)
    return str(v)


def checkpoint(stage, **kw):
    data = dict(stage=stage, pid=os.getpid(), **kw)
    save('CHECKPOINT.json', data)
    print(json.dumps(data, allow_nan=False), flush=True)


def produce_candidate(adj, selected, degrees, loads):
    """Export only the one best hand-checked vector; no BFS or graph search."""
    count = len(selected)
    n = N+count
    dest = HERE/f'candidate_n{n}'
    dest.mkdir()
    new_by_old = [[] for _ in range(N)]
    added = 0
    roles = []
    for j, center in enumerate(selected):
        ns = adj[center]
        for w in ns:
            new_by_old[w].append(N+j)
        added += len(ns)
        roles.append((j, center, N+j, len(ns), ' '.join(map(str, ns))))
    m = 116316+added
    graph = dest/f'graph_d16_D4_n{n}.edges'
    old_count = new_count = 0
    with graph.open('w') as f:
        f.write(f'{n} {m}\n')
        for u in range(N):
            for v in adj[u]:
                if u < v:
                    f.write(f'{u} {v}\n')
                    old_count += 1
            for v in new_by_old[u]:
                f.write(f'{u} {v}\n')
                new_count += 1
    if old_count != 116316 or new_count != added:
        raise RuntimeError('Export edge accounting mismatch; no acceptance')
    with (dest/'ALL_ROLE_BINDINGS.tsv').open('w', newline='') as f:
        wr = csv.writer(f, delimiter='\t')
        wr.writerow(['j','source_center_label','new_label','literal_N_size','frozen_old_simple_neighbors'])
        wr.writerows(roles)
    degree_hist = collections.Counter(int(degrees[w])+int(loads[w]) for w in range(N))
    degree_hist.update(int(degrees[c]) for c in selected)
    parameters = dict(source_literal='research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt',
                      source_n=N, source_m=116316, center_labels=selected,
                      clone_count=count, n=n, m=m, maximum_degree=max(degree_hist),
                      new_new_edges=0, old_source_edges_retained=old_count,
                      added_edges=added, ordered_recipe='center=selected[j];newlabel=15552+j;N(new)=originalsimpleN(center)',
                      degree_histogram=dict(sorted(degree_hist.items())),
                      old_load_histogram=dict(sorted(collections.Counter(map(int,loads)).items())),
                      source_degree_histogram={'14':648,'15':14904},
                      graph=str(graph.relative_to(ROOT)), global_priority='UNKNOWN',
                      source_D4_and_nonD3='inheritedalreadyclosedsourceFullExact;notrecompiled',
                      candidate_fresh_acceptance='PENDING_ROOT', new_graph_parameter_Lean_count=[0,0,0])
    (dest/'PARAMETERS.json').write_text(json.dumps(parameters, indent=2)+'\n')
    (dest/'PROOF.md').write_text(
        '# Full original-neighborhood clone candidate\n\n'
        'The fixed original15552 simple source is retained. Newrolej has exactly '
        'the original simple open neighborhood of selected[j], after virtual-self '
        'was removed at the OLDcenter label; no newnew edges. The handchecked '
        'source-incidence inequalities give olddegree+load<=16; newdegree is the '
        'originaldegree14/15. All actual load/degree counts are in PARAMETERS.\n\n'
        'The alreadyclosed source has genuineWalk<=4 and noisolatedvertices. '
        'For source-center distance>=2 replace only endpoints of an oldWalk. '
        'Adjacent centers use clone_c--old_d--old_c--clone_d in3 steps. '
        'Coincident centers use a commonoldneighbor in2. All interiors are '
        'originalsource, so everyprefix works. Collapse is a graphhomomorphism '
        'fixing all oldvertices; oldold Walk bounds are exactly preserved, '
        'therefore source nonD3 persists. These are inherited generic arguments, '
        'not new kernel/BFS claims. New literal/recipe acceptance remains pending.\n')
    return parameters


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hard-cpu', type=int, required=True)
    ap.add_argument('--time-limit', type=float, required=True)
    args = ap.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (args.hard_cpu,args.hard_cpu))
    started = time.process_time()
    for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
        if os.environ.get(k) != '1':
            raise RuntimeError('Singlethread numeric environment must precede process startup')
    checkpoint('IMPORTING_SINGLE_THREAD_API', hard_CPU=args.hard_cpu)
    import numpy as np
    import scipy
    import scipy.optimize._highspy._core as h
    source = ROOT/'research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt'
    adj = []
    with source.open() as f:
        for row in f:
            parts = list(map(int,row.split()))
            if parts[0] != len(adj):
                raise RuntimeError('Source label order differs from accepted input')
            adj.append(sorted(parts[1:]))
    if len(adj) != N:
        raise RuntimeError('Source row count differs from accepted input')
    degrees = np.array([len(row) for row in adj], dtype=np.int32)
    cap = 16-degrees
    incumbent = json.loads((CASE/'degree16_plane864/PARAMETERS.json').read_text())['source_center_labels']
    if len(incumbent) != 864 or len(set(incumbent)) != 864:
        raise RuntimeError('Known incumbent does not encode864distinctcenters')
    warm = np.zeros(N, dtype=np.float64)
    warm[incumbent] = 1.0
    warmloads = np.zeros(N, dtype=np.int32)
    for c in incumbent:
        warmloads[adj[c]] += 1
    if not bool(np.all(warmloads <= cap)):
        raise RuntimeError('Known864 handcheck failed; do not callsolver')
    # A column c is exactly the frozen old simple N(c); no field or graph checks.
    indptr = np.zeros(N+1, dtype=np.int32)
    np.cumsum(degrees, out=indptr[1:])
    indices = np.array([w for row in adj for w in row], dtype=np.int32)
    values = np.ones(indices.size, dtype=np.float64)
    np.savez(HERE/'MODEL_INPUT.npz', indptr=indptr, indices=indices,
             capacity=cap, degrees=degrees, warm=warm)
    model = dict(variables=N, rows=N, incidence_nonzeros=int(indices.size),
                 matrix='CSC unitdata, columnc=originalsimpleN(c)',
                 variable_domain='binary0to1,onecloneperoldcenter',
                 objective='minimize -sum x', rhs='16-originaldegree',
                 source_literal=str(source.relative_to(ROOT)), source_literal_parses=1,
                 known_start_count=864, known_start_binary=True,
                 known_start_all_rows_handchecked=True,
                 start_load_histogram=dict(sorted(collections.Counter(map(int,warmloads)).items())),
                 scipy_version=scipy.__version__, threads=1, time_limit=args.time_limit,
                 no_W27_or_targetdisjoint_constraint=True,
                 only_one_passModel_setSolution_run=True,
                 independent_optimality_proof=False)
    save('MODEL.json', model)
    checkpoint('MODEL_READY_WARM864_HANDCHECKED', **model)
    lp = h.HighsLp()
    lp.num_col_ = N
    lp.num_row_ = N
    lp.col_cost_ = -np.ones(N,dtype=np.float64)
    lp.col_lower_ = np.zeros(N,dtype=np.float64)
    lp.col_upper_ = np.ones(N,dtype=np.float64)
    lp.row_lower_ = np.full(N,-h.kHighsInf,dtype=np.float64)
    lp.row_upper_ = cap.astype(np.float64)
    lp.integrality_ = [h.HighsVarType.kInteger]*N
    lp.a_matrix_.num_col_ = N
    lp.a_matrix_.num_row_ = N
    lp.a_matrix_.format_ = h.MatrixFormat.kColwise
    lp.a_matrix_.start_ = indptr
    lp.a_matrix_.index_ = indices
    lp.a_matrix_.value_ = values
    highs = h._Highs()
    for name, value in [('threads',1),('time_limit',args.time_limit)]:
        status = highs.setOptionValue(name,value)
        if status != h.HighsStatus.kOk:
            save('OPTION_FAILURE.json',dict(name=name,status=str(status)))
            raise RuntimeError('Required knownoption rejected; no retry')
    status = highs.passModel(lp)
    save('PASS_MODEL_RETURN.json',dict(status=str(status),HiGHS_version=highs.version()))
    if status != h.HighsStatus.kOk:
        raise RuntimeError('passModel did not returnkOk; no retry')
    solution = h.HighsSolution()
    solution.col_value = warm.tolist()
    solution.row_value = warmloads.astype(np.float64).tolist()
    solution.value_valid = True
    solution.dual_valid = False
    warmstatus = highs.setSolution(solution)
    save('WARM_START_RETURN.json',dict(status=str(warmstatus),count=864,
         complete_15552_col_vector=True,complete_15552_row_vector=True,
         all_rows_handchecked=True,objective=-864))
    if warmstatus != h.HighsStatus.kOk:
        raise RuntimeError('setSolution did not returnkOk; no restart')
    checkpoint('RUN_ACTIVE', warm_set_status=str(warmstatus), solver_runs_started=1)
    run_started = time.process_time()
    runstatus = highs.run()
    run_cpu = time.process_time()-run_started
    info = highs.getInfo()
    modelstatus = highs.getModelStatus()
    best = highs.getSolution()
    raw = dict(run_status=str(runstatus), model_status=str(modelstatus),
               model_status_message=highs.modelStatusToString(modelstatus),
               solver_run_CPU_seconds=run_cpu, HiGHS_version=highs.version(),
               value_valid=bool(best.value_valid),warm_set_status=str(warmstatus))
    for name in ['objective_function_value','mip_node_count','mip_dual_bound','mip_gap',
                 'primal_solution_status','num_primal_infeasibilities','max_primal_infeasibility']:
        raw[name] = clean(getattr(info,name,None))
    x = np.asarray(best.col_value,dtype=np.float64)
    save('RAW_SOLUTION.json',dict(**raw,col_values=[clean(float(v)) for v in x]))
    valid = bool(best.value_valid) and x.size == N
    if valid:
        rounded = np.rint(x).astype(np.int32)
        valid = bool(np.all(np.abs(x-rounded)<=1e-6) and np.all(rounded>=0) and np.all(rounded<=1))
    selected = []
    loads = np.zeros(N,dtype=np.int32)
    if valid:
        selected = np.flatnonzero(rounded).tolist()
        for c in selected:
            loads[adj[c]] += 1
        valid = bool(np.all(loads<=cap))
    best_count = len(selected) if valid else None
    save('BEST_HANDCHECK.json',dict(binary_and_all15552capacities_valid=valid,
         selected_count=best_count,selected_centers=selected if valid else None,
         actual_max_load=int(loads.max()) if valid else None,
         no_BFS_or_source_validity_check=True))
    candidate = None
    if valid and best_count > 864:
        checkpoint('IMPROVED_BINARY_VECTOR_HANDCHECKED_EXPORTING',best_count=best_count)
        candidate = produce_candidate(adj,selected,degrees,loads)
    result = dict(status='IMPROVED_LITERAL_CLONE_CANDIDATE_PENDING_FRESH' if candidate else
                  ('NO_IMPROVEMENT_RAW_OPTIMAL_UNVERIFIED_GLOBAL_BOUND' if
                   modelstatus==h.HighsModelStatus.kOptimal else 'NO_VERIFIED_IMPROVEMENT_UNKNOWN'),
                  best_count=best_count, returned_vector_handchecked=valid,
                  known864_is_old_incumbent=True,candidate_generated=candidate is not None,
                  candidate=candidate,raw_solver=raw,
                  actual_child_CPU_seconds_before_finalwrite=time.process_time()-started,
                  maximality_certified=False, global_priority='UNKNOWN',
                  passModel_calls=1,setSolution_calls=1,run_calls=1,retries=0,
                  graph_BFS_field_source_validity_Lean_ARIS_runs=0,
                  source_literal_parses=1,new_graph_parameter_Lean_count=[0,0,0])
    save('RESULT.json',result)
    checkpoint('CHILD_TERMINAL',status=result['status'],best_count=best_count)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        save('FAILURE.json',dict(status='UNKNOWN_EXECUTION_FAILURE_NO_RESTART',
             error_type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        save('RESULT.json',dict(status='UNKNOWN_EXECUTION_FAILURE_NO_RESTART',
             error_type=type(exc).__name__,message=str(exc),candidate_generated=False,
             new_graph_parameter_Lean_count=[0,0,0]))
        raise
