#!/usr/bin/env python3
from pathlib import Path
import csv
import json
import os
import resource
import time
from collections import Counter

HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent / 'coefficient_alias_gate'


def dump(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


prior = json.loads((PRIOR / 'TERMINAL.json').read_text())['cumulative_charged_CPU_seconds']
prep = 0.1
failed_prep = 0.1
budget = 20.0
remaining = budget - prior - prep - failed_prep
resource.setrlimit(resource.RLIMIT_CPU, (int(remaining), int(remaining) + 1))
dump('HANDLE.json', {'pid': os.getpid(), 'phase': 'critical_slot_evaluation', 'running': True,
                     'worker_count': 1, 'prior_charged_CPU_seconds': prior,
                     'preparation_charge_seconds': prep, 'failed_preparation_charge_seconds': failed_prep,
                     'branch_CPU_budget_seconds': budget, 'process_hard_CPU_limit_seconds': int(remaining) + 1})
dump('PREPARATION_RESULT.json', {'failed_preparation': 'Python source heredoc triple-quote parse failure; no experiment executed',
                                'failed_preparation_CPU_seconds': None, 'conservative_failed_preparation_charge_seconds': failed_prep,
                                'conservative_preparation_charge_seconds': prep,
                                'prior_terminal_CPU_seconds': prior, 'total_branch_CPU_budget_seconds': budget})
saved = json.loads((PRIOR / 'TIGHT_WORD_FORM_CLASSES.json').read_text())
forms = [tuple(c['coefficient_vector']) for c in saved['classes']]
assert len(forms) == len(set(forms)) == 159
assert (saved['source_state'], saved['target_state']) == (46, 52)
q = 139
phases = (3, 11, 6, 4)
gauge = tuple((pow(6, a, q) - 1) % q for a in phases)
assert gauge[2] != 0
offset = (pow(6, 6, q) - 1) % q
assert all(sum(c * g for c, g in zip(f, gauge)) % q == offset for f in forms)
representatives = [(1, a, 0, b) for a in range(q) for b in range(q)]
representatives += [(0, 1, 0, b) for b in range(q)]
representatives += [(0, 0, 0, 1), (0, 0, 0, 0)]
assert len(representatives) == len(set(representatives)) == 19462
hist = Counter()
max_count = -1
best = None
survivors = []
with (HERE / 'ALL_REPRESENTATIVE_COVERAGES.csv').open('w', newline='') as out:
    writer = csv.writer(out)
    writer.writerow(['representative_index', 'c0', 'c1', 'c2', 'c12', 'image_cardinality', 'first_missing_normal_endpoint'])
    for idx, params in enumerate(representatives):
        c0, c1, _, c12 = params
        image = {(f[0] * c0 + f[1] * c1 + f[3] * c12) % q for f in forms}
        n = len(image)
        hist[n] += 1
        missing = next((z for z in range(q) if z not in image), None)
        writer.writerow([idx, *params, n, '' if missing is None else missing])
        if n > max_count:
            max_count = n
            best = {'representative_index': idx, 'parameters': list(params), 'image_cardinality': n,
                    'image': sorted(image), 'missing_endpoints': [z for z in range(q) if z not in image]}
        if n == q:
            survivors.append({'representative_index': idx, 'parameters': list(params), 'image_cardinality': n})
assert sum(hist.values()) == 19462
status = 'CRITICAL_SLOT_SURVIVORS_FULL_D8_UNTESTED' if survivors else 'COMPLETE_NO_FIXED_FOUR_PARAMETER_D8_FAMILY'
prediction = 'REFUTED_CRITICAL_SLOT_SURVIVORS' if survivors else 'SUPPORTED_ALL19462_REPRESENTATIVES_FAIL'
dump('NORMALIZATION_BINDING.json', {
    'parameter_order': ['c0', 'c1', 'c2', 'c12'], 'positive_phases': list(phases), 'gauge_vector': list(gauge),
    'eliminated_parameter': 'c2', 'elimination_denominator': gauge[2], 'saved_tight_slot': [46, 52],
    'saved_distinct_forms': 159, 'common_gauge_increment': offset, 'all159_forms_have_same_gauge_increment': True,
    'representative_count': len(representatives), 'projective_representative_blocks': [139 * 139, 139, 1],
    'extra_pure_gauge_zero_representative': 1, 'normal_zero_root_fixed_pointwise': False,
    'fixed_slot_image_cardinality_preserved': True})
dump('BEST_CRITICAL_SLOT_COVERAGE.json', best)
dump('SURVIVORS.json', survivors)
cpu = time.process_time()
result = {
    'status': status, 'prediction': prediction, 'target_degree': 4, 'target_D': 8, 'hypothetical_order': 9591,
    'controller_states': 69, 'normal_field_size': q, 'multiplier': 6,
    'shared_parameters': ['c0', 'c1', 'c2', 'c12'], 'critical_slot': [46, 52],
    'inherited_raw_words': 160, 'inherited_distinct_forms': 159,
    'parameter_representatives_evaluated': len(representatives), 'complete_normalized_parameter_domain': True,
    'critical_slot_survivor_count': len(survivors), 'maximum_actual_image_cardinality': max_count,
    'required_image_cardinality': q, 'image_cardinality_histogram': dict(sorted(hist.items())),
    'all_representatives_have_saved_first_missing_endpoint': not survivors,
    'best_representative': best['parameters'], 'gauge_binding_all159': True,
    'exact_scope': 'Fixed69-state three-base/23-phase controller; r6 on F139; four shared translations with two identity-cross translations0; true inverse darts; diameter at most8.',
    'not_excluded': ['other controller or phase structures', 'other normal-field multipliers',
                     'independent per-phase translations', 'arbitrary permutation voltage covers', 'general degree4 diameter8 graphs'],
    'proof_reason': 'Each <=8 geodesic projects to a saved nonbacktracking controller word. Its displacement is a saved form evaluation; every representative misses some endpoint in slot46→52. Gauge and scale preserve each slot image cardinality.',
    'old_words_or_forms_recounted': 0, 'old_source_field_validation': 0,
    'new_graph_BFS_solver_Lean_web_or_external_review': 0, 'new_graph_parameter_Lean_count_increment': [0, 0, 0],
    'single_worker': True, 'prior_charged_CPU_seconds': prior, 'conservative_preparation_charge_seconds': prep,
    'conservative_failed_preparation_charge_seconds': failed_prep, 'actual_evaluation_process_CPU_seconds': cpu,
    'cumulative_charged_CPU_seconds': prior + prep + failed_prep + cpu, 'cumulative_CPU_budget_seconds': budget,
    'next': 'STOP_REPORT_TO_ROOT_NO_OTHER_SLOT_OR_PARAMETER_EXTENSION'}
if survivors:
    result['proof_reason'] = 'Critical-slot necessary pass only; no claim about other slots or graph diameter.'
dump('RESULT.json', result)
if not survivors:
    interpretation = (f'All19462 representatives fail. The best actual tight-slot image has{max_count} endpoints rather than139. '
                      'The abstract159-form capacity passed, but no compatible four-parameter evaluation covers this slot. '
                      'This completely excludes only the stated fixed family.')
else:
    interpretation = f'{len(survivors)} critical-slot survivors were saved; all other slots and graph diameter remain untested.'
(HERE / 'NOTE.md').write_text(f'''# Complete normalized parameter gate

{interpretation}

Gauge: Y=y+6^x d gives c'_j=c_j+(6^a_j−1)d. The c2 elimination denominator is{gauge[2]}≠0; its unique zero gauge followed by scaling gives P²(F139) plus the pure-gauge zero point. Each saved form has common gauge shift{offset} in slot46→52. This translation and nonzero scaling preserve image cardinality; the normal0 root need not be pointwise fixed. Independent paper review is in [parameter_gate_normalization_review.md](parameter_gate_normalization_review.md).

The19462-row CSV is the full domain, with actual image sizes and a missing endpoint for each failure. The best representative is{best['parameters']}, image size{max_count}. All words and coefficient classes were inherited without recounting. No9591-vertex graph was generated.

A geodesic projects to a nonbacktracking controller word, since adjacent inverse darts return to the same full vertex and can be removed. Thus missing an endpoint in the complete <=8 word image proves diameter greater than8 or disconnection. This uses the already-bound true inverse model, not the earlier single centered assignment.

CPU includes prior{prior:.9f}, conservative preparation{prep:.1f}, failed parse charge{failed_prep:.1f}, and this single process. Branch budget20CPU, no reset or continuation. No source/field/graph/BFS/solver/Lean/web/review computation was performed.
''')
final_cpu = time.process_time()
terminal = {'status': status, 'running': False, 'all_processes_terminal': True, 'worker_count': 1,
            'actual_evaluation_process_CPU_seconds': final_cpu, 'conservative_preparation_charge_seconds': prep,
            'conservative_failed_preparation_charge_seconds': failed_prep, 'prior_charged_CPU_seconds': prior,
            'cumulative_charged_CPU_seconds': prior + prep + failed_prep + final_cpu,
            'cumulative_CPU_budget_seconds': budget, 'no_timer_reset': True, 'no_automatic_continuation': True}
dump('TERMINAL.json', terminal)
dump('HANDLE.json', {'pid': os.getpid(), 'phase': 'terminal', 'running': False, 'worker_count': 1,
                     'status': status, 'cumulative_charged_CPU_seconds': terminal['cumulative_charged_CPU_seconds'],
                     'branch_CPU_budget_seconds': budget})
print(json.dumps({'result': result, 'terminal': terminal}, ensure_ascii=False, indent=2))
