#!/usr/bin/env python3
"""Finalize only after all four authorized worker scopes are complete."""
from pathlib import Path
import json
import time

start = time.process_time()
HERE = Path(__file__).resolve().parent
FIVE = HERE.parent
FAMILY = FIVE.parent


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


full = read(HERE / 'terminal.json')
assert full['status'] == 'COMPLETE_ALL_DIMENSION6_SCOPE_NO_SOLUTION'
assert full['patterns_completed'] == 7124 and full['processed_inputs'] == 10747252152
assert full['actual_full_root_BFS'] == 0 and not full['saved_best_graph']
workers = [read(HERE / f'worker{i}/terminal.json') for i in range(4)]
for worker in workers:
    assert worker['status'] == 'COMPLETE_DIMENSION6_WORKER_NO_SOLUTION'
    assert worker['patterns_completed'] == 1781 and worker['processed_inputs'] == 2686813038
    assert worker['next_position'] is None
    worker['pending'] = []
for i, worker in enumerate(workers):
    write(HERE / f'worker{i}/terminal.json', worker)
old = read(FAMILY / 'maximin_production/terminal.json')
assert old['status'] == 'COMPLETE_MAXIMIN_SCOPE_NO_SOLUTION' and old['patterns_completed'] == 76
old_inputs = read(FAMILY / 'maximin_production/inputs.json')
assert sum(r['pairs'] == 5 for r in old_inputs) == 28 and sum(r['pairs'] == 6 for r in old_inputs) == 48
four_linear = read(FAMILY / 'fourpair_tight/linear.terminal.json')
four = read(FAMILY / 'fourpair_tight/terminal.json')
assert four_linear['rejected_patterns'] == 2 and four_linear['surviving_patterns'] == 10
assert four['status'] == 'COMPLETE_FOURPAIR_TIGHT_SCOPE_NO_SOLUTION' and four['patterns_completed'] == 10
six = read(FAMILY / 'sixpair_remaining/terminal.json')
assert six['status'] == 'COMPLETE_REMAINING_SIXPAIR_SCOPE_NO_SOLUTION' and six['patterns_completed'] == 50680
reduced = read(FIVE / 'reduced_production/terminal.json')
assert reduced['status'] == 'COMPLETE_REDUCED_FIVEPAIR_SCOPE_NO_SOLUTION' and reduced['patterns_completed'] == 1091
linear = read(FIVE / 'terminal.json')
assert linear['status'] == 'COMPLETE_SYMBOLIC_PREPROCESSING' and linear['rejected_original_modes'] == 314
capacity = read(FAMILY / 'terminal.json')
assert capacity['status'] == 'COMPLETE_CAPACITY_ONLY' and capacity['completed_phase_patterns'] == 593775
assert [b['symbolic_pass'] for b in capacity['branches']] == [0, 0, 0, 0, 12, 16375, 50728]
assert all(b['plain_pass'] == 0 for b in capacity['branches'][:4])
assert 28 + 314 + 2168 + 13865 == 16375
assert 48 + 50680 == 50728 and 2 + 10 == 12
production_terminals = [old, four, six, reduced, full]
assert all(t['actual_full_root_BFS'] == 0 and not t['saved_best_graph'] for t in production_terminals)
closure = {
    'status': 'COMPLETE_FIXED_GROUP_DEGREE12_CAYLEY_SCOPE_NO_D3',
    'group': 'F17 semidirect_3 C48 = AGL1(17) direct_product C3',
    'order': 816, 'degree': 12, 'target_D': 3,
    'scope': 'All simple undirected Cayley graphs with exactly12 distinct nonidentity inverse-closed generators in this fixed group',
    'initial_phase_composition_patterns': 593775,
    'initial_symbolic_survivors': 67115,
    'zero_to_three_pair_patterns_capacity_excluded': 2925,
    'four_pair_symbolic_modes': 12,
    'four_pair_linear_rejected': 2,
    'four_pair_fully_enumerated_reduced_modes': 10,
    'five_pair_symbolic_modes': 16375,
    'five_pair_previously_completed': 28,
    'five_pair_linear_rejected_original_modes': 314,
    'five_pair_reduced_completed_original_modes': 2168,
    'five_pair_dimension6_completed_original_modes': 13865,
    'six_pair_symbolic_modes': 50728,
    'six_pair_previously_completed': 48,
    'six_pair_remaining_fully_completed': 50680,
    'total_actual_marked_production_inputs': sum(t['processed_inputs'] for t in production_terminals),
    'total_actual_legal_production_inputs': sum(t['counts']['legal_marked_inputs'] for t in production_terminals),
    'total_actual_illegal_production_inputs': sum(t['counts']['illegal_marked_inputs'] for t in production_terminals),
    'full_fiber_passes': 0, 'full_root_BFS': 0, 'saved_graphs': 0,
    'remaining_patterns': 0, 'remaining_field_inputs': 0,
    'evidence_level': 'Complete finite computation with explicit reductions and arithmetic calibrations; not Lean/formal certification',
    'not_claimed': ['Arbitrary816-vertex graphs excluded', 'Other groups excluded', 'A new construction or record'],
    'pending': [],
}
write(HERE / 'FAMILY_CLOSURE.json', closure)
worker_table = '\n'.join(f"| {i} | {w['processed_inputs']:,} | {w['counts']['legal_marked_inputs']:,} | {w['counts']['illegal_marked_inputs']:,} | {w['CPU_seconds']:.6f} |" for i, w in enumerate(workers))
rejections = ', '.join(f"{i+1}: {n:,}" for i, n in enumerate(full['counts']['fiber_rejections_in_test_order']) if n)
report = f'''# Remaining dimension-six production: complete

All four workers completed their disjoint scopes: **7,124 representatives and 10,747,252,152 marked projective inputs**. No legal assignment covered all 48 exact fibers, so there was no D3 candidate, full BFS, or generated graph.

| Worker | Marked inputs | Legal inputs | Illegal inputs | CPU seconds |
|---:|---:|---:|---:|---:|
{worker_table}

The aggregate counts are {full['counts']['legal_marked_inputs']:,} legal and {full['counts']['illegal_marked_inputs']:,} illegal assignments. First-failure positions in the per-mode count/phase ordering were {rejections}. These are tested-fiber positions, not common quotient phases. Each worker retained its complete per-mode counts and has a null next cursor.

The run used four workers from one driver, session 77572, with production PIDs 3197240 through 3197243. Preparation and compilation used {full['preparation_compile_CPU_seconds']:.9f} CPU seconds; workers together used {full['sum_worker_CPU_seconds']:.9f}; total measured driver-plus-child CPU was {full['total_measured_CPU_seconds']:.9f}. The authorized aggregate limit was 1,800 CPU seconds, with 440 per worker. No process was restarted and no extra profile was run. The formal first-100,000 records are actual production prefixes.

The on-the-fly coefficient generator retained all seven component variables, including the two independent reflection slots. It compared every original 48-fiber form-count vector to saved capacity, then deleted the correct nontrivial-action anchor and checked that deduplication did not change the counts. All retained bases were identity. Actual group inverse, nonidentity, and 12-element distinctness checks preceded exact fiber evaluation.

Two legal members of worker0's formal prefix supplied the required independent direct-word-mask comparison. Source 31886, phases `[0,5,15,16,18]`, restored fields `[1,0,0,0,0,0,1]`; source 91986, phases `[5,15,16,18,18]`, restored `[0,1,0,0,1,0,1]`. All 48 masks matched in each case. Together these cover phase zero, the phase-16 action kernel, and repeated phases. There was no extra field assignment or BFS outside the formal cursor.

## Scope closure

The current run closes only the remaining 7,124 representative modes by itself. Combining the explicitly checked saved terminals now closes the entire fixed-group degree-12 Cayley scope:

| Inverse pairs / reflections | Complete reduction and actual coverage |
|---|---|
| 0/12 through 3/6 | All 2,925 composition modes fail original plain capacity. |
| 4/4 | Of 12 symbolic survivors, 2 fail iterative tight capacity and all reduced assignments of 10 were completed. |
| 5/2 | 28 old modes + 314 linear-rejected modes + 2,168 modes covered by reduced production + 13,865 covered here = 16,375. |
| 6/0 | 48 old modes + 50,680 remaining completed modes = 50,728. |

The original complete composition table had 593,775 modes, 131,540 plain survivors, and 67,115 symbolic survivors. Necessary capacity failures account for modes outside the table's symbolic survivors. The phase-17 map transfers only along the explicitly saved valid automorphism orbits; fixed modes were not mechanically halved. Actual total production across the five saved batches was {closure['total_actual_marked_production_inputs']:,} marked assignments, comprising {closure['total_actual_legal_production_inputs']:,} legal and {closure['total_actual_illegal_production_inputs']:,} illegal assignments. These are marked input counts, not distinct-graph counts.

Accordingly this complete finite calculation finds no simple undirected degree-12 diameter-at-most-3 Cayley graph on `F17 semidirect_3 C48`. It does not exclude arbitrary 816-vertex graphs or other groups, and is not a formal Lean certificate. No construction or new record was obtained. No independent final graph validation is pending because every actual candidate failed exact fiber coverage. `FAMILY_CLOSURE.json` records the cross-stage accounting; `SCOPE.md` gives the precise current iterator and route criterion.
'''
(HERE / 'REPORT.md').write_text(report)
status = {'status': closure['status'], 'five_pair_modes_total': 16375,
          'closed_original_modes': 16375, 'remaining_original_modes': 0,
          'remaining_representatives': 0, 'remaining_marked_inputs': 0,
          'full_family_closure_record': 'full_dimension_production/FAMILY_CLOSURE.json',
          'pending': []}
write(FIVE / 'CURRENT_SCOPE_STATUS.json', status)
old_report = (FIVE / 'REPORT.md').read_text()
heading = '# Five-pair preprocessing and the authorized reduced production\n'
replacement = '''# Five-pair scope: complete

**Final update:** the subsequently authorized four-worker dimension-six production also completed all 10,747,252,152 inputs without full fiber coverage. All 16,375 five-pair symbolic modes are now closed, and combining the saved four-pair and six-pair terminals closes the fixed group's degree-12 Cayley scope. See [the complete final report](full_dimension_production/REPORT.md), [the scope accounting](full_dimension_production/FAMILY_CLOSURE.json), and `CURRENT_SCOPE_STATUS.json`. No graph or new record was obtained. The sections below retain the earlier preprocessing and reduced-production snapshots; their remaining-scope statements describe the state before the final batch.
'''
assert old_report.startswith(heading)
(FIVE / 'REPORT.md').write_text(old_report.replace(heading, replacement, 1))
full['final_report_CPU_seconds'] = time.process_time() - start
full['total_including_final_report_CPU_seconds'] = full['total_measured_CPU_seconds'] + full['final_report_CPU_seconds']
assert full['total_including_final_report_CPU_seconds'] < 1800
full['pending'] = []
write(HERE / 'terminal.json', full)
print(json.dumps({'status': full['status'], 'processed_inputs': full['processed_inputs'],
                  'legal': full['counts']['legal_marked_inputs'], 'illegal': full['counts']['illegal_marked_inputs'],
                  'total_CPU_including_report': full['total_including_final_report_CPU_seconds'],
                  'fixed_group_degree12_scope_closed': True}, indent=2))
