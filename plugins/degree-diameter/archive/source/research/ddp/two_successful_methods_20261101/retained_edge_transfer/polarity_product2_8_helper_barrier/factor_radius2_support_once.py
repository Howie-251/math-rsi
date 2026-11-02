#!/usr/bin/env python3
"""One small support experiment; no old graph generation or BFS."""
from itertools import combinations
import json
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
started = time.process_time()
base = Path(__file__).resolve().parent
adj = [set() for _ in range(15)]

def edge(x, y):
    adj[x].add(y)
    adj[y].add(x)

for i in range(5):
    edge(i, i)
    edge(i, 5+i)
    edge(i, 10+i)
    edge(5+i, 5+(i+1)%5)
    edge(10+i, 10+(i+2)%5)

absolute = set(range(5))
nonabsolute = set(range(5, 15))
direct = {b: adj[b] & nonabsolute for b in absolute}
support = {
    b: (adj[b] | set().union(*(adj[w] for w in adj[b]))) & nonabsolute
    for b in absolute
}
pair_rows = []
for b, c in combinations(sorted(absolute), 2):
    pair_rows.append({
        'pins': [b,c], 'intersection': sorted(support[b] & support[c]),
        'union_size': len(support[b] | support[c]),
        'missed': sorted(nonabsolute - support[b] - support[c]),
    })

subset_rows = []
for t in range(6):
    for selected in combinations(sorted(absolute), t):
        covered = set().union(*(support[b] for b in selected))
        missed = nonabsolute-covered
        # Direct pairs partition the ten targets. Every missed target's
        # unique owning based class must be supplied by an external route.
        required = [b for b in sorted(absolute) if direct[b] & missed]
        repairs = set().union(*(direct[b] for b in required))
        subset_rows.append({
            'own_classes': list(selected), 'distinct_own_count': t,
            'old_two_step_targets': sorted(covered), 'missed_targets': sorted(missed),
            'required_external_classes': required,
            'completion_covers_all': nonabsolute <= covered | repairs,
            'each_required_class_is_necessary': all(
                bool((direct[b] & missed) - set().union(*(
                    direct[c] for c in required if c != b
                ))) for b in required
            ),
        })

expected_counts = [5,4,1,0,0,0]
checks = {
    'literal_rows_size3': all(len(row)==3 for row in adj),
    'only_five_absolute_loops': {x for x in range(15) if x in adj[x]} == absolute,
    'direct_pairs_partition_nonabsolute': set().union(*direct.values()) == nonabsolute
        and sum(map(len,direct.values())) == len(nonabsolute),
    'all_five_supports_size6': all(len(s)==6 for s in support.values()),
    'all_ten_pair_intersections_size3': all(len(r['intersection'])==3 for r in pair_rows),
    'all_ten_pair_unions_size9_one_missed': all(r['union_size']==9 and len(r['missed'])==1 for r in pair_rows),
    'all32_external_class_predictions_match': all(
        len(r['required_external_classes']) == expected_counts[r['distinct_own_count']]
        for r in subset_rows
    ),
    'all32_completions_exact_and_necessary': all(
        r['completion_covers_all'] and r['each_required_class_is_necessary']
        for r in subset_rows
    ),
}
cpu = time.process_time()-started
result = {
    'status': 'ALL_PREDECLARED_SUPPORT_AND_COMPLETION_PREDICTIONS_PASS'
        if all(checks.values()) else 'PREDICTION_REFUTED',
    'prediction': 'FACTOR_RADIUS2_OVERLAP_PREDICTION.md',
    'CPU_seconds': cpu, 'CPU_budget_seconds': 2, 'workers': 1,
    'literal_factor_vertices': 15, 'absolute_supports': {str(b):sorted(s) for b,s in support.items()},
    'pair_rows': pair_rows, 'subset_rows': subset_rows,
    'expected_required_external_classes_by_own_count': expected_counts,
    'checks': checks,
    'q8_finite_table_examined': False,
    'q8_conclusion_scope': 'Paper-only genuine GQ interface, independent attack separate.',
    'old_225_230_graphs_read_or_rerun': False,
    'source_graph_generation_BFS_field_Lean_solver_paid_review_runs': 0,
    'portfolio_parameter_Lean_increments': [0,0,0],
}
(base/'FACTOR_RADIUS2_SUPPORT_EXPERIMENT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(base/'FACTOR_RADIUS2_SUPPORT_EXPERIMENT_TERMINAL.json').write_text(json.dumps({
    'state':result['status'], 'active_processes':False,
    'CPU_seconds':cpu, 'CPU_budget_seconds':2,
    'subsets_examined':len(subset_rows), 'pairs_examined':len(pair_rows),
    'portfolio_parameter_Lean_increments':[0,0,0],
},indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':checks,'CPU_seconds':cpu,
    'pairs':len(pair_rows),'subsets':len(subset_rows)}))
