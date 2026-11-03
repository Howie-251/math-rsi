"""Summarize the already computed pair tables; no graph traversal or search."""
import csv
import json
import statistics
from collections import Counter
from pathlib import Path

OUT = Path(__file__).resolve().parent
result = {}
for name in ('baseline650', 'expanded676', 'cyclic676'):
    with (OUT / f'{name}.pairs.tsv').open() as stream:
        rows = list(csv.DictReader(stream, delimiter='\t'))
    selected = [row for row in rows if int(row['direct_leaf_edges']) == 0]
    stats = {'all_cross_group_head_block_pairs': len(rows),
             'pairs_without_direct_leaf_edge': len(selected),
             'pairs_with_direct_leaf_edge': len(rows) - len(selected)}
    for field in ('potential_middle_blocks', 'potential_unweighted_block_two_walks',
                  'potential_incidence_pair_routes', 'actual_leaf_two_walks'):
        values = [int(row[field]) for row in selected]
        stats[field] = {'minimum': min(values), 'median': statistics.median(values),
                        'maximum': max(values), 'sum': sum(values),
                        'histogram': dict(sorted(Counter(values).items()))}
    result[name] = stats
(OUT / 'without_direct_edge_comparison.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
