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
SOURCE = HERE.parent / 'Exoo_132_NXadjlist.author.txt'
BUDGET = 20.0
PREP_CHARGE = 0.2
PRIOR_CHARGE = json.loads((HERE.parent / 'RESULT.json').read_text())['total_charged_CPU_seconds']
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
                         'seed': 202611010306})
    code = child.wait()
run_cpu = children_cpu() - run_start
if code:
    result = {'status': 'RUN_INTERRUPTED_UNKNOWN', 'exit_code': code, 'candidate_pass': False}
else:
    result = json.loads((HERE / 'RAW_RESULT.json').read_text())
result.update({
    'target': {'degree': 3, 'diameter': 6, 'order': 134},
    'source': str(SOURCE.relative_to(ROOT)), 'source_order': 132, 'source_edges': 198,
    'source_degree_diameter_scope': 'Cubic literal newlybound once fromprimaryNXinput; publishedD6 inherited; no sourceD6/allroots validation. Oneoldpairdiagnostic onlyif firstoldfailure.',
    'prediction': 'At least one sampled configuration passes both helper R6 coverage; old-old preservation remains a separate exact check.',
    'prediction_both_helpers_supported': result.get('both_helpers_passed', 0) > 0,
    'exact_rule': 'Three disjoint old edge cuts; one original-nonedge repair on two cut endpoints; other four pins split2+2; helpers adjacent.',
    'complete_configuration_family_exclusion': False,
    'scope': 'One fixed-seed sample of at most10000 distinct configurations, not all three-matchings or all degree3/D6 graphs.',
    'prior_case_charged_CPU_seconds': PRIOR_CHARGE, 'preparation_charge_seconds': PREP_CHARGE,
    'actual_compile_CPU_seconds': compile_cpu, 'actual_run_child_CPU_seconds': run_cpu,
    'driver_process_CPU_seconds': time.process_time(), 'total_charged_CPU_seconds': consumed(),
    'CPU_budget_seconds': BUDGET, 'worker_count': 1,
    'source_D6_validity_or_source_allroot_BFS': 0, 'source_literal_structure_check_count': 1, 'solver_Lean_remote_install_or_hash': 0,
    'graph_parameter_Lean_increment_before_root_acceptance': [0, 0, 0],
    'next': 'STOP_REPORT_TO_ROOT_NO_OTHER_SEED_CUT_PATTERN_OR_TIMER'})
if (HERE / 'SOURCE_INPUT_BINDING.json').exists():
    result['source_input_binding'] = json.loads((HERE / 'SOURCE_INPUT_BINDING.json').read_text())
if result.get('hit'):
    save('PARAMETERS.json', {'n':134,'m':201,'degree':3,'actual_diameter':result['winning_diameter'],
                            'source':str(SOURCE.relative_to(ROOT)), 'new_labels':[132,133],
                            'configuration':result['winning_configuration'],
                            'all_final_BFS_roots':134,'actual_distance_witness':result['winning_distance_witness'],
                            'graph':'graph_d3_D6_n134.edges','root_acceptance':'PENDING','priority':'UNKNOWN'})
save('RESULT.json', result)
status = result['status']
both = result.get('both_helpers_passed', 0)
old_fail = result.get('rejected_old_old', 0)
note = f'''# Exoo132 adjacent-helper repair sample

Actual status: {status}. Tested {result.get('distinct_configurations_finished', 0)} distinct configurations to a terminal decision. Both helper roots passed radius6 in {both}; {old_fail} of those then failed an old-old pair. Stage counts and first actual counterexamples are in RESULT.json; ATTEMPTS.csv records every sampled configuration. The published sourceD6 fact is inherited; no source-wide D6 validation was run in this case.

The prediction that some candidate preserves new-old coverage was {'supported' if both else 'not supported in this sample'}. Old-old testing is only reported for candidates that passed both helper roots. A sample with no hit is UNKNOWN about the full rule. No claim of an exhaustive negative result or a new graph is made without a saved full candidate and root acceptance.

The operation keeps every source vertex cubic: six cut endpoints each lose exactly one edge and gain exactly one via repair or helper. Each helper has two old pins plus the peer edge. Repair endpoints must be anoriginalsource nonedge,so restoring a cutedge is excluded fromthisnumericdomain. The only allowed old modifications are the three cuts and single original nonedge repair. A hit has134 vertices and201 edges. This uses a different source and diameter from the old AFY70/D5 and Exoo600/D9 experiments; their negatives do not exclude this Exoo132/D6 rule.

Exact cooperative helper routes and old-old route cases are in ../PAPER_SCOPE_REVIEW.md. Ordinary BFS was performed only on modified134-vertex candidates, with both helpers first; old-labelled BFS rows are final-candidate checks. Onlyone firstfailedoldpair may have anoriginalsource shortestpathdiagnostic,recordedseparately. No source-wide original D6 BFS, symmetry search, solver, Lean, web or review was run.

Budget inherits priorcase{PRIOR_CHARGE:.9f},includes conservative newpreparation0.2CPU,actualcompiler{compile_cpu:.9f} and run child{run_cpu:.9f}, plus driver CPU. Total{consumed():.9f}/20CPU, one worker. All processes terminal; fixed seed202611010306, no automatic retry or extension. Root owns acceptance, counts and global documents.
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
