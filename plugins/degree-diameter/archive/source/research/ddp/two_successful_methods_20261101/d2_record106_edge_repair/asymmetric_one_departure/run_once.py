#!/usr/bin/env python3
import time
START = time.process_time()
import json
import math
import os
import resource
import subprocess
from pathlib import Path

D = Path(__file__).resolve().parent
C = D.parent
PRIOR = 10.711203943
BUDGET = 6.0
PREPARATION_CHARGE = 0.1  # Conservative allowance, distinct from measured process CPU.
STAGES = []


def cpu():
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return PREPARATION_CHARGE + time.process_time() - START + child.ru_utime + child.ru_stime


def dump(name, data):
    (D / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def mark(stage, **extra):
    STAGES.append(dict(stage=stage, actual_batch_CPU_seconds=cpu(), **extra))
    dump('HANDLE.json', dict(actual_driver_PID=os.getpid(), stage=stage,
        prior_case_CPU_seconds=PRIOR, batch_CPU_budget_seconds=BUDGET,
        case_CPU_budget_seconds=20, single_worker=True, **extra))
    dump('BUDGET_LEDGER.json', dict(prior_case_CPU_seconds=PRIOR,
        batch_CPU_budget_seconds=BUDGET, case_CPU_budget_seconds=20, stages=STAGES))


def prelimit(limit):
    def setlimit():
        n = max(1, math.ceil(limit))
        resource.setrlimit(resource.RLIMIT_CPU, (n, n))
    return setlimit


def finish(result, note):
    (D / 'NOTE.md').write_text(note + '\n')
    result.update(prior_case_CPU_seconds=PRIOR, batch_CPU_seconds=cpu(),
        case_CPU_seconds=PRIOR + cpu(), batch_CPU_budget_seconds=BUDGET,
        conservative_code_preparation_charge_seconds=PREPARATION_CHARGE,
        case_CPU_budget_seconds=20, single_worker=True,
        graph_parameter_or_Lean_count_increment=0,
        candidate_accepted_by_root=False, source_graph_BFS_or_full_D2_recheck=0,
        old_MILP_solver_web_Lean_field_rank_automorphism_runs=0,
        rootdocs_Wiki_oldfiles_modified=False)
    dump('RESULT.json', result)
    mark('TERMINAL', status=result['status'])
    receipt = dict(status=result['status'], all_processes_terminal=True,
        running=False, prior_case_CPU_seconds=PRIOR, batch_CPU_seconds=cpu(),
        case_CPU_seconds=PRIOR + cpu(), batch_CPU_budget_seconds=BUDGET,
        case_CPU_budget_seconds=20, no_automatic_continuation=True)
    dump('TERMINAL.json', receipt)
    print(json.dumps(dict(status=result['status'], batch_CPU_seconds=receipt['batch_CPU_seconds'],
        case_CPU_seconds=receipt['case_CPU_seconds'],
        visited_representatives=result.get('visited_representatives'),
        DFS_nodes=result.get('DFS_nodes'))), flush=True)


try:
    mark('PREPARE_EXISTING_LITERAL_SOURCE_AND_ACCEPTED_ORBITS')
    rows = []
    with (C / 'source106.author.adjlist.txt').open() as source:
        for line in source:
            v = list(map(int, line.split()))
            rows.append(' '.join(map(str, [v[0], len(v) - 1] + v[1:])))
    action = json.loads((C / 'sector_matching_extension/ORDER7_GENERATOR_AND_ORBITS.json').read_text())
    fixed = [row[0] for row in action['orbits'] if len(row) == 1]
    orbits = [sorted(row) for row in action['orbits'] if len(row) == 7]
    with (D / 'INPUT.txt').open('w') as target:
        target.write('\n'.join(rows) + '\n')
        target.write(str(len(fixed)) + ' ' + ' '.join(map(str, fixed)) + '\n')
        target.write(str(len(orbits)) + '\n')
        target.write('\n'.join(' '.join(map(str, row)) for row in orbits) + '\n')
    with (D / 'COMPILE.log').open('w') as log:
        p = subprocess.Popen(['g++', '-std=c++17', '-O2', str(D / 'search.cpp'), '-o', str(D / 'search')],
            cwd=D, stdout=log, stderr=subprocess.STDOUT,
            preexec_fn=prelimit(BUDGET - cpu()))
        mark('COMPILING_ONLY_NEW_SMALL_SEARCH', actual_child_PID=p.pid)
        rc = p.wait()
    mark('COMPILE_TERMINAL', exit_code=rc)
    if rc:
        raise RuntimeError('new C++ compile failed; no retry')
    remaining = BUDGET - cpu() - 0.25
    if remaining <= 0.05:
        raise RuntimeError('compile/preparation exhausted batch budget; no search')
    with (D / 'SEARCH.log').open('w') as log:
        p = subprocess.Popen([str(D / 'search'), str(remaining)], cwd=D,
            stdout=log, stderr=subprocess.STDOUT, preexec_fn=prelimit(remaining))
        mark('ACTUAL_BOUNDED_SEARCH_RUNNING', actual_child_PID=p.pid,
            search_CPU_limit_seconds=remaining)
        rc = p.wait()
    mark('SEARCH_PROCESS_TERMINAL', exit_code=rc)
    if rc:
        raise RuntimeError('search exited without ordinary terminal; no retry')
    r = json.loads((D / 'SEARCH_RESULT.json').read_text())
    if r['status'].startswith('SAT_'):
        note = '''# An asymmetric one-departure candidate, awaiting fresh acceptance

PRED.md fixes the two representative families and the exact55-edge internal
model. The actual first solution is returned as a full107-vertex edge file,
with original deleted/added edges and selected pins in CANDIDATE_EDGE_DELTA.json.
MIXED_AND_NEW_ROOT_ROUTES.csv gives the mixed and new-root route witnesses
from the chosen y assignment. No graph is counted or declared independently
accepted here.

All source edges outside G[S], including cross edges, are preserved. Therefore
outside/outside source routes of length at most two survive, even when their
middle is selected. Both-selected endpoints use their two edges through z.
Selected/outside endpoints use the frozen direct edge, a frozen outside common
middle, or a chosen internal edge to an original neighbor of the outside
endpoint. The positive model clauses cover exactly the last obligation. z
reaches every outside point via a selected original neighbor by closed
domination, and every selected point directly. Bounds L/U give degree10..11
for selected vertices; outside degrees remain their accepted source10/11;
z has degree11. The graph file is generated once from the selected internal
assignment, never by deleting a larger graph. Root must still perform the
fresh candidate acceptance before any graph or record increment.

No source-distance BFS/full common-neighbor validation, solver, automorphism
search, field/rank/Lean or web step was run. The two-family search stops at
the first candidate; unvisited representatives are not claimed infeasible.
'''
    elif r['status'].startswith('EXACT_NO_'):
        note = '''# Exact rejection of the two fixed one-departure pin families

The actual counts and propagation/finite-tree decomposition are saved in
RESULT.json. All10976 specified representatives were resolved by closed
domination, frozen-cross degree, empty mixed-route clauses, sound unit/degree
propagation or complete finite DFS. DFS has only55 internal edge variables;
coverage clauses are positive disjunctions, degree bounds are exact, and
both Boolean branches are visited unless rejected by propagation. This is
an exact NO only for the two PRED.md families, not for arbitrary asymmetric
pin sets or other edge modifications. No new graph was generated.

The accepted source C7 justifies removing the minimum orbit point in A and
choosing the minimum external-orbit point in B. It does not impose symmetry
on the internal y assignment. Selected/selected pairs use z; outside/outside
old routes retain their edges, including routes through a selected middle;
mixed pairs have exactly the preserved-direct/preserved-outside-middle or
chosen-internal-middle alternatives encoded by the model. z-to-outside is
exactly the closed-domination gate. Thus a solver is not needed for the
finite rejection shown here. The earlier general internal-S MILP remains
numerically UNKNOWN and is not rewritten by this restricted result.

No old-source D2/BFS, automorphism/refinement, field/rank/Lean, external
solver or web operation was rerun. The batch is terminal with no continuation.
'''
    else:
        note = '''# Bounded two-pattern search: unresolved scope retained

The node/CPU stop, visited representatives, exact gate rejections and any
unresolved current representative are recorded in RESULT.json. Unvisited or
unresolved pin sets remain UNKNOWN. There is no all-family infeasibility
claim, no new timer, and no additional pattern. PRED.md states the exact
mixed-route and degree interface; no source validation/BFS, old MILP,
automorphism/refinement, field/rank/Lean, external solver or web was rerun.
'''
    finish(r, note)
except Exception as e:
    finish(dict(status='UNKNOWN_IMPLEMENTATION_OR_BUDGET_STOP_NO_RETRY', exception=repr(e)),
        '# The single batch stopped\nActual failure and all spent compilation/preparation CPU are retained. No retry, graph count or mathematical infeasibility conclusion follows.')
