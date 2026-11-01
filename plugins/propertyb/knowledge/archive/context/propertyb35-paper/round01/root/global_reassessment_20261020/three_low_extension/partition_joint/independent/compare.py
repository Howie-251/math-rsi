"""Check every independent output against both producer JSON artifacts."""
import json
from collections import Counter
from pathlib import Path

here = Path(__file__).resolve().parent
actual = json.loads((here / 'RESULT.json').read_text())
producer = json.loads((here.parent / 'RESULT.json').read_text())
representatives = json.loads((here.parent / 'REPRESENTATIVES.json').read_text())
assert actual['status'] == 'PASS' and actual['complete_domain_checked']
assert actual['terminal_matrices'] == 19834 and actual['canonical_domain'] == 264
assert actual['representatives_checked'] == 264
expected = {x['id']: x for x in representatives}
assert len(expected) == 264
for row in actual['representatives']:
    p = expected[row['id']]
    assert row['key'] == p['key'] and row['jointcount'] == p['jointcount']
assert sum(x['row_sorted_terminals_in_orbit'] for x in actual['representatives']) == 19834
assert len({x['key'] for x in actual['representatives']}) == 264
histogram = dict(sorted(Counter(str(x['jointcount']) for x in actual['representatives']).items()))
assert histogram == actual['histogram'] == producer['histogram']
assert (actual['minimum'], actual['maximum'], actual['minimizer_count']) == (400, 16980, 1)
minimizer = [x for x in actual['representatives'] if x['jointcount'] == 400]
assert len(minimizer) == 1
matrix = expected[minimizer[0]['id']]['matrix']
assert all(sorted(row) == [0, 1, 1, 1, 1] for row in matrix)
assert all(sorted(matrix[i][j] for i in range(5)) == [0, 1, 1, 1, 1] for j in range(5))
summary = {
    'status': 'PASS',
    'all_representative_keys_and_counts_match': True,
    'all_histogram_bins_match': True,
    'terminal_multiplicity_sum': 19834,
    'unique_minimizer_is_J_minus_I_up_to_row_column_permutations': True,
    'unique_minimizer_id': minimizer[0]['id'],
    'unique_minimizer_key': minimizer[0]['key'],
    'literal_representative_coloring_pairs': actual['representative_coloring_pairs'],
    'literal_control_colorings': actual['additional_control_colorings'],
}
(here / 'COMPARISON.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary))
