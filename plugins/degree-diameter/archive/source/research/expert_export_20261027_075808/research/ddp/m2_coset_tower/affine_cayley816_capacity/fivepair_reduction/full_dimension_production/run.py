#!/usr/bin/env python3
"""One authorized four-worker run; disjoint saved modes, no restarts."""
from pathlib import Path
from collections import Counter
import json
import os
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
assert not (HERE / 'run.json').exists(), 'No automatic restart'


def cpu():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime + a.ru_stime + b.ru_utime + b.ru_stime


def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')


start, wall = cpu(), time.monotonic()
state = json.loads((HERE.parent / 'REMAINING_AFTER_PRODUCTION.json').read_text())
reduced_terminal = json.loads((HERE.parent / 'reduced_production/terminal.json').read_text())
assert reduced_terminal['status'] == 'COMPLETE_REDUCED_FIVEPAIR_SCOPE_NO_SOLUTION'
assert reduced_terminal['processed_inputs'] == 84607626 and reduced_terminal['patterns_completed'] == 1091
rows = json.loads((HERE.parent / 'remaining_representatives.json').read_text())
rows = [r for r in rows if r['remaining_projective_inputs'] and r['final_dimension'] == 6]
assert len(rows) == 7124 and sum(r['remaining_projective_inputs'] for r in rows) == 10747252152
assert set(r['source_cursor'] for r in rows) == set(state['remaining_source_cursors'])
for row in rows:
    assert row['basis_in_original_anchored_coordinates'] == [[int(i == j) for j in range(6)] for i in range(6)]
    assert row['status'] in ['NO_TIGHT_FIBER_UNCHANGED', 'SURVIVES_STABLE_TIGHT_LINEAR_CLOSURE']
    assert row['remaining_projective_inputs'] == 1508598
    assert not row['checked_member_cursors'] and len(row['pair_phases']) == 5
    assert row['anchor_component'] == next(i for i, j in enumerate(row['pair_phases']) if pow(3, j, 17) != 1)
rows.sort(key=lambda r: (-min(r['final_form_counts']), r['source_cursor']))
# These are actual formal production modes, moved to the first worker's prefix
# solely to combine the requested phase0/16/repeated-phase mask calibration.
special_sources = [31886, 91986]
by_source = {r['source_cursor']: r for r in rows}
selected = [by_source[s] for s in special_sources] + [r for r in rows if r['source_cursor'] not in special_sources]
assert selected[0]['pair_phases'] == [0, 5, 15, 16, 18]
assert selected[1]['pair_phases'] == [5, 15, 16, 18, 18]
assert len({r['source_cursor'] for r in selected}) == 7124
shards = [selected[i*1781:(i+1)*1781] for i in range(4)]
for worker, shard in enumerate(shards):
    directory = HERE / f'worker{worker}'
    directory.mkdir(exist_ok=True)
    with (directory / 'inputs.txt').open('w') as text, (directory / 'inputs.jsonl').open('w') as detail:
        text.write('1781\n')
        for index, row in enumerate(shard):
            assert min(row['final_form_counts']) >= 17
            text.write(' '.join(map(str, [row['source_cursor'], row['anchor_component']] + row['pair_phases'] + row['final_form_counts'])) + '\n')
            detail.write(json.dumps({'worker': worker, 'pattern_index': index, 'source_cursor': row['source_cursor'],
                                    'member_cursors': row['member_cursors'], 'pair_phases': row['pair_phases'],
                                    'anchor_component': row['anchor_component'], 'projective_scope': 1508598,
                                    'capacity_by_phase': row['final_form_counts']}) + '\n')
with (HERE / 'compile.log').open('w') as log:
    subprocess.run(['g++', '-O3', '-std=c++17', 'search.cpp', '-o', 'search'], cwd=HERE,
                   stdout=log, stderr=subprocess.STDOUT, check=True)
prep = cpu() - start
limit = min(440.0, (1800 - prep - 5) / 4)
assert limit > 0
metadata = {'group': 'F17 semidirect_3 C48', 'degree': 12, 'target_D': 3, 'n': 816,
            'pair_count': 5, 'reflection_count': 2, 'patterns': 7124, 'represented_original_modes': 13865,
            'per_pattern_scope': 1508598, 'raw_scope': 10747252152,
            'worker_count': 4, 'patterns_per_worker': 1781, 'scope_per_worker': 2686813038,
            'CPU_budget_seconds': 1800, 'preparation_compile_CPU_seconds': prep,
            'worker_CPU_limit_seconds': limit,
            'coordinate_normalization': 'nontrivial-action anchor0, six remaining coordinates first nonzero1; saved basis identity',
            'symbolic_engine': 'on-the-fly freely reduced words<=3 in seven independent component variables; compare all48 saved counts then remove anchor',
            'production_order': 'two specified calibration modes first, remaining modes minimum capacity descending then source cursor; contiguous shards',
            'formal_prefix_calibration_sources': special_sources,
            'calibration_extra_assignments': 0, 'calibration_extra_BFS': 0,
            'closed_modes_repeated': 0, 'random_seeds': 0,
            'actual_candidate_check': '12 nonidentity distinct elements; exact48 fiber coverage; full root BFS only on all-fiber pass',
            'failure_graph_policy': 'No graph generated on fiber failure',
            'capacity_minimum_histogram': dict(Counter(min(r['final_form_counts']) for r in selected))}
dump(HERE / 'metadata.json', metadata)
run = {'status': 'RUNNING', 'running': True, 'driver_pid': os.getpid(), 'worker_count': 4,
       'CPU_budget_seconds': 1800, 'preparation_compile_CPU_seconds': prep,
       'worker_CPU_limit_seconds': limit, 'raw_scope': 10747252152, 'workers': []}
dump(HERE / 'run.json', run)
processes, logs, completed = [], [], {}
for worker in range(4):
    directory = HERE / f'worker{worker}'
    log = (directory / 'production.log').open('w')
    process = subprocess.Popen([str(HERE / 'search'), str(directory), str(limit), str(HERE / 'STOP_ON_D3'), '1' if worker == 0 else '0'], stdout=log, stderr=subprocess.STDOUT)
    item = {'worker': worker, 'pid': process.pid, 'directory': str(directory), 'status': 'RUNNING', 'start_cursor': 0,
            'patterns_scope': 1781, 'raw_scope': 2686813038, 'CPU_limit_seconds': limit}
    dump(directory / 'run.json', item)
    run['workers'].append(item)
    processes.append(process)
    logs.append(log)
dump(HERE / 'run.json', run)
print(json.dumps(run), flush=True)
while len(completed) < 4:
    for worker, process in enumerate(processes):
        if worker in completed:
            continue
        code = process.poll()
        if code is None:
            continue
        logs[worker].close()
        directory = HERE / f'worker{worker}'
        item = run['workers'][worker]
        item.update(exit_code=code, running=False)
        if code != 0:
            item['status'] = 'PROCESS_ERROR'
            (HERE / 'STOP_ON_D3').write_text('Process error: preserve other cursors; no restart\n')
            completed[worker] = None
        else:
            terminal = json.loads((directory / 'terminal.json').read_text())
            completed[worker] = terminal
            item.update(status=terminal['status'], processed_inputs=terminal['processed_inputs'],
                        patterns_completed=terminal['patterns_completed'], CPU_seconds=terminal['CPU_seconds'])
        dump(directory / 'run.json', item)
        dump(HERE / 'run.json', run)
        print(json.dumps({'event': 'WORKER_FINISHED', **item}), flush=True)
    if len(completed) < 4:
        time.sleep(0.25)
terminals = [completed[i] for i in range(4) if completed[i] is not None]
found = any(t['saved_best_graph'] for t in terminals)
full = len(terminals) == 4 and all(t['status'] == 'COMPLETE_DIMENSION6_WORKER_NO_SOLUTION' for t in terminals)
counts = {k: sum(t['counts'][k] for t in terminals) for k in ['processed_marked_inputs', 'legal_marked_inputs', 'illegal_marked_inputs', 'full_root_BFS']}
for key in ['fiber_rejections_in_test_order', 'fiber_passes_in_test_order']:
    counts[key] = [sum(t['counts'][key][j] for t in terminals) for j in range(48)]
summary = {'status': 'FOUND_D3' if found else 'COMPLETE_ALL_DIMENSION6_SCOPE_NO_SOLUTION' if full else 'INCOMPLETE_SAVED_WORKER_PREFIXES',
           'running': False, 'raw_scope': 10747252152, 'patterns_scope': 7124,
           'patterns_completed': sum(t['patterns_completed'] for t in terminals),
           'processed_inputs': counts['processed_marked_inputs'], 'counts': counts,
           'workers': run['workers'], 'worker_count': 4, 'CPU_budget_seconds': 1800,
           'preparation_compile_CPU_seconds': prep, 'sum_worker_CPU_seconds': sum(t['CPU_seconds'] for t in terminals),
           'total_measured_CPU_seconds': cpu() - start, 'wall_seconds': time.monotonic() - wall,
           'actual_full_root_BFS': counts['full_root_BFS'], 'saved_best_graph': found,
           'in_prefix_mask_calibrations': sum(t['in_prefix_exact_short_word_calibrations'] for t in terminals),
           'restarts': 0, 'random_seeds': 0,
           'pending': ['Independent verification of saved D3 graph'] if found else [] if full else ['Unprocessed worker suffixes']}
dump(HERE / 'terminal.json', summary)
run.update(status=summary['status'], running=False, total_CPU_seconds=summary['total_measured_CPU_seconds'], processed_inputs=summary['processed_inputs'])
dump(HERE / 'run.json', run)
print(json.dumps(summary, indent=2), flush=True)
