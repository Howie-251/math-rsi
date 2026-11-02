#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SOURCE = ROOT / 'research/ddp/more_graphs_20261027/d3_D9_current600_source/source600.edges'
BUDGET = 20.0
PREP_CHARGE = 0.2
PRIOR_CHARGE = json.loads((HERE.parent / 'TERMINAL.json').read_text())['total_charged_CPU_seconds']
start_self = time.process_time()
start_children = resource.getrusage(resource.RUSAGE_CHILDREN)


def children_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime - start_children.ru_utime - start_children.ru_stime


def consumed():
    return PRIOR_CHARGE + PREP_CHARGE + time.process_time() + children_cpu()


def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def limit_child(seconds):
    def set_limit():
        ceiling = max(1, math.ceil(seconds))
        resource.setrlimit(resource.RLIMIT_CPU, (ceiling, ceiling + 1))
    return set_limit


save('HANDLE.json', {'pid': os.getpid(), 'phase': 'compile', 'running': True,
                     'worker_count': 1, 'total_CPU_budget_seconds': BUDGET,
                     'prior_case_charged_CPU_seconds': PRIOR_CHARGE, 'preparation_charge_seconds': PREP_CHARGE})
compile_start = children_cpu()
with (HERE / 'COMPILE.log').open('w') as log:
    compiler = subprocess.Popen(['g++', '-O2', '-std=c++17', str(HERE / 'run.cpp'), '-o', str(HERE / 'run')],
                                stdout=log, stderr=subprocess.STDOUT,
                                preexec_fn=limit_child(BUDGET - consumed() - 0.5))
    save('HANDLE.json', {'pid': os.getpid(), 'child_pid': compiler.pid, 'phase': 'compile', 'running': True,
                         'worker_count': 1, 'total_CPU_budget_seconds': BUDGET})
    code = compiler.wait()
compile_cpu = children_cpu() - compile_start
if code:
    terminal = {'status': 'COMPILE_FAILED_NO_SAMPLE_EXECUTED', 'exit_code': code, 'running': False,
                'all_processes_terminal': True, 'compile_CPU_seconds': compile_cpu,
                'total_charged_CPU_seconds': consumed(), 'CPU_budget_seconds': BUDGET,
                'no_timer_reset': True, 'no_automatic_continuation': True}
    save('RESULT.json', terminal)
    save('TERMINAL.json', terminal)
    save('HANDLE.json', terminal)
    print(json.dumps(terminal, indent=2))
    raise SystemExit(code)

remaining = BUDGET - consumed() - 0.5
assert remaining > 0.1
run_start = children_cpu()
with (HERE / 'RUN.log').open('w') as log:
    child = subprocess.Popen([str(HERE / 'run'), str(SOURCE), str(HERE), str(remaining)],
                             stdout=log, stderr=subprocess.STDOUT,
                             preexec_fn=limit_child(remaining + 0.2))
    save('HANDLE.json', {'pid': os.getpid(), 'child_pid': child.pid, 'phase': 'bounded_sample', 'running': True,
                         'worker_count': 1, 'total_CPU_budget_seconds': BUDGET,
                         'actual_compile_CPU_seconds': compile_cpu,
                         'run_CPU_limit_seconds': remaining, 'sample_cap': 10000,
                         'seed': 202611010309})
    code = child.wait()
run_cpu = children_cpu() - run_start
if code:
    result = {'status': 'RUN_INTERRUPTED_UNKNOWN', 'exit_code': code, 'candidate_pass': False}
else:
    result = json.loads((HERE / 'RAW_RESULT.json').read_text())
result.update({
    'target': {'degree': 3, 'diameter': 9, 'order': 602},
    'source': str(SOURCE.relative_to(ROOT)), 'source_order': 600, 'source_edges': 900,
    'source_degree_diameter_scope': 'Cubic literal and published D9 inherited; source non-bipartite; no new source validity/BFS.',
    'prediction': 'At least one sampled configuration passes both helper R9 coverage; old-old preservation remains a separate exact check.',
    'prediction_both_helpers_supported': result.get('both_helpers_passed', 0) > 0,
    'exact_rule': 'Four disjoint old edge cuts; exactly one endpoint per cut is a newpin; other four endpoints receive two original-nonedge repairs; pins split2+2; helpers adjacent.',
    'complete_configuration_family_exclusion': False,
    'scope': 'One fixed-seed sample of at most10000 distinct configurations, not all four-matchings or all degree3/D9 graphs.',
    'prior_case_charged_CPU_seconds': PRIOR_CHARGE, 'preparation_charge_seconds': PREP_CHARGE,
    'actual_compile_CPU_seconds': compile_cpu, 'actual_run_child_CPU_seconds': run_cpu,
    'driver_process_CPU_seconds': time.process_time(), 'total_charged_CPU_seconds': consumed(),
    'CPU_budget_seconds': BUDGET, 'worker_count': 1,
    'source_validity_or_source_BFS': 0, 'solver_Lean_remote_install_or_hash': 0,
    'graph_parameter_Lean_increment_before_root_acceptance': [0, 0, 0],
    'next': 'STOP_REPORT_TO_ROOT_NO_OTHER_SEED_CUT_PATTERN_OR_TIMER'})
save('RESULT.json', result)
status = result['status']
both = result.get('both_helpers_passed', 0)
old_fail = result.get('rejected_old_old', 0)
note = f'''# Exoo600 adjacent-helper repair sample

Actual status: {status}. Tested {result.get('distinct_configurations_finished', 0)} distinct configurations to a terminal decision. Both helper roots passed radius9 in {both}; {old_fail} of those then failed an old-old pair. Stage counts and first actual counterexamples are in RESULT.json; ATTEMPTS.csv records every sampled configuration. The original600 graph was never distance-validated again.

The prediction that some candidate preserves new-old coverage was {'supported' if both else 'not supported in this sample'}. Old-old testing is only reported for candidates that passed both helper roots. A sample with no hit is UNKNOWN about the full rule. No claim of an exhaustive negative result or a new graph is made without a saved full candidate and root acceptance.

The operation keeps every source vertex cubic: eight cut endpoints each lose exactly one edge and gain exactly one via two repairs or a helper. Each helper has two old pins plus the peer edge. The only allowed old modifications are the four cuts and two original nonedge repairs. A hit has602 vertices and903 edges. This differs from the old AFY70/D5 source and the Exoo600 branch that stopped solely at a false bipartite premise.

Exact cooperative helper routes and old-old route cases are in PAPER_NOTE.md. Ordinary BFS was performed only on modified602-vertex candidates, with both helpers first; old-labelled BFS rows are final-candidate checks. No source-wide original D9 BFS, symmetry search, solver, Lean, web or review was run.

Budget inherits prior case{PRIOR_CHARGE:.9f} plus conservative new preparation0.2CPU, actual compiler{compile_cpu:.9f} and run child{run_cpu:.9f}, plus driver CPU. Total{consumed():.9f}/20CPU, one worker. All processes terminal; fixed seed202611010309, no automatic retry or extension. Root owns acceptance, counts and global documents.
'''
(HERE / 'NOTE.md').write_text(note)
terminal = {'status': status, 'running': False, 'all_processes_terminal': True,
            'actual_compile_CPU_seconds': compile_cpu, 'actual_run_child_CPU_seconds': run_cpu,
            'driver_process_CPU_seconds': time.process_time(), 'prior_case_charged_CPU_seconds': PRIOR_CHARGE, 'preparation_charge_seconds': PREP_CHARGE,
            'total_charged_CPU_seconds': consumed(), 'CPU_budget_seconds': BUDGET,
            'sample_cap': 10000, 'distinct_configurations_finished': result.get('distinct_configurations_finished', 0),
            'worker_count': 1, 'no_timer_reset': True, 'no_automatic_continuation': True}
save('TERMINAL.json', terminal)
save('HANDLE.json', {'pid': os.getpid(), 'phase': 'terminal', **terminal})
print(json.dumps({'result': result, 'terminal': terminal}, ensure_ascii=False, indent=2))
