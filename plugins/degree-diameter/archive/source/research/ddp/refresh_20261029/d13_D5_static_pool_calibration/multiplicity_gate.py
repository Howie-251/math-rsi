import json
from pathlib import Path
from time import process_time

started = process_time()
here = Path(__file__).resolve().parent
saved = json.loads((here / 'RESULT.json').read_text())
assert saved['failed_sets'] == saved['incompatible_pairs'] == saved['port_overloads'] == 0
ports = {p['vertex']: p for p in saved['used_ports']}
sets = saved['sets']
rows = []
for index, item in enumerate(sets):
    members = item['neighbors']
    ub = min(ports[v]['base_spare'] for v in members)
    residual = min(ports[v]['base_spare'] - ports[v]['usage'] for v in members)
    rows.append({
        'index': index,
        'source_new_vertex': item['new_vertex'],
        'neighbors': members,
        'upper_bound': ub,
        'upper_bound_witnesses': [v for v in members if ports[v]['base_spare'] == ub],
        'minimum_incumbent_residual': residual,
        'blocked_incumbent_ports': [v for v in members if ports[v]['base_spare'] == ports[v]['usage']],
        'direct_duplicate_feasible': residual >= 1,
    })
direct = [row['index'] for row in rows if row['direct_duplicate_feasible']]
all_one_ubs = all(row['upper_bound'] == 1 for row in rows)
result = {
    'scope': 'multiplicities of the exact40 saved independently covering compatible neighborhoods',
    'incumbent': [1] * len(sets),
    'incumbent_total': len(sets),
    'rows': rows,
    'upper_bound_histogram': {str(k): sum(r['upper_bound'] == k for r in rows) for k in sorted({r['upper_bound'] for r in rows})},
    'sum_individual_upper_bounds': sum(r['upper_bound'] for r in rows),
    'direct_duplicate_indices': direct,
    'all_upper_bounds_one': all_one_ubs,
    'status': 'MAXIMUM_EXACTLY40' if all_one_ubs else ('DIRECT_CONSTRUCTION_PARAMETERS_FOUND' if direct else 'NEEDS_AUTHORIZED_SINGLE_PACKING_CALL'),
    'solver_calls': 0,
    'graph_reads': 0,
    'BFS_runs': 0,
    'new_graphs': 0,
    'cpu_seconds': process_time() - started,
}
if direct:
    result['proposed_multiplicities'] = [1 + (i == direct[0]) for i in range(len(sets))]
    result['proposed_added_vertices'] = 41
(here / 'MULTIPLICITY_RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k not in ['rows', 'incumbent']}, indent=2))
