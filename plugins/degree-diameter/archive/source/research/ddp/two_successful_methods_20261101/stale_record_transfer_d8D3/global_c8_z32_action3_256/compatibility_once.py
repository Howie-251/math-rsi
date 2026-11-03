#!/usr/bin/env python3
"""Single read of saved tuples; no new word or parameter evaluation."""
import time
START = time.process_time()
import itertools
import json
from pathlib import Path
import resource

resource.setrlimit(resource.RLIMIT_CPU, (1, 1))
HERE = Path(__file__).resolve().parent
original = json.loads((HERE / 'RESULT.json').read_text())
frequency = [0] * 256
first = {}
rows = 0
with (HERE / 'ALL_NORMALIZED_CONNECTED_PARAMETERS.tsv').open() as stream:
    header = next(stream).strip().split('\t')
    assert header[7:15] == [f'cover{p}' for p in range(8)]
    for line in stream:
        cells = list(map(int, line.split()))
        mask = sum(1 << p for p in range(8) if cells[7 + p] == 32)
        frequency[mask] += 1
        if mask not in first:
            first[mask] = {
                'parameter_id': cells[0], 'first_odd_index': cells[1],
                'normals': cells[2:6], 'actual_degree': cells[6],
                'all_phase_coverages': cells[7:15], 'full_phase_mask': mask,
                'first_failed_phase': cells[15], 'first_missing_normal': cells[16],
            }
        rows += 1
assert rows == 57344 and frequency[255] == 0
superset_count = frequency.copy()
for bit in range(8):
    for mask in range(256):
        if not mask & (1 << bit):
            superset_count[mask] += superset_count[mask | (1 << bit)]

smallest = None
all_minimum = []
for size in range(1, 9):
    for phases in itertools.combinations(range(8), size):
        mask = sum(1 << p for p in phases)
        if superset_count[mask] == 0:
            if smallest is None:
                smallest = (phases, mask)
            all_minimum.append(list(phases))
    if smallest is not None:
        break

phases, mask = smallest
proper = []
for size in range(len(phases)):
    for subset in itertools.combinations(phases, size):
        part = sum(1 << p for p in subset)
        witnesses = [row for full, row in first.items() if full & part == part]
        assert witnesses
        witness = min(witnesses, key=lambda row: row['parameter_id'])
        proper.append({'phases': list(subset), 'simultaneous_full_count': superset_count[part],
                       'actual_saved_witness': witness})

result = {
    'status': 'COMPLETE_SAVED_PARAMETER_COMPATIBILITY_POSTPROCESS',
    'prediction_test': 'locate first minimum-cardinality incompatible phase subset, with every proper-subset actual saved witness',
    'source_rows_read_once': rows, 'new_words_parameters_BFS_graphs': 0,
    'full_phase_mask_frequency': [
        {'mask': i, 'phases': [p for p in range(8) if i & (1 << p)],
         'count': c, 'first_saved_parameter': first[i]} for i, c in enumerate(frequency) if c
    ],
    'all_subset_simultaneous_full_counts': superset_count,
    'minimum_incompatible_size': len(phases), 'chosen_incompatible_phases': list(phases),
    'chosen_incompatible_mask': mask, 'all_minimum_incompatible_phase_sets': all_minimum,
    'chosen_incompatible_simultaneous_full_count': superset_count[mask],
    'every_proper_subset_witness': proper,
    'scope': 'same fixed C8-action3/Z32/phases1234 connected normalized domain; not other groups/actions/phases',
}
actual = time.process_time() - START
result.update({'actual_postprocess_CPU_seconds': actual,
    'postprocess_preparation_charge_CPU_seconds': .05,
    'prior_case_CPU_seconds': original['wholecase_CPU_seconds'],
    'wholecase_CPU_seconds': original['wholecase_CPU_seconds'] + .05 + actual,
    'postprocess_CPU_cap_seconds': 1, 'terminal': True, 'active_processes': 0})
(HERE / 'COMPATIBILITY.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ('status', 'minimum_incompatible_size',
    'chosen_incompatible_phases', 'all_minimum_incompatible_phase_sets',
    'every_proper_subset_witness', 'actual_postprocess_CPU_seconds', 'wholecase_CPU_seconds')}))
