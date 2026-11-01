"""Tiny necessary-integer inventory; no hypergraph or coloring search."""
import itertools
import json
import time
from pathlib import Path

started = time.process_time()
out = {}
for r in (9, 10):
    stars = [u for u in itertools.product(range(7), repeat=4)
             if sum(u) == 6
             and u[2] + 2*u[3] - u[0] == r-7
             and 4*u[2] + 5*u[3] <= r]
    inventories = []
    for counts in itertools.product(range(r+1), repeat=len(stars)):
        if sum(counts) != r:
            continue
        incidences = [sum(c*u[j] for c, u in zip(counts, stars))
                      for j in range(4)]
        if any(v % (j+1) for j, v in enumerate(incidences)):
            continue
        nj = [v // (j+1) for j, v in enumerate(incidences)]
        n = [35-sum(nj)] + nj
        if n[0] < 0:
            continue
        assert sum(j*n[j] for j in range(5)) == 6*r
        assert sum(j*(j-1)//2*n[j] for j in range(5)) == r*(r-1)//2
        if r == 9:
            # A is the no-quad star (0,4,2,0). With any quad,
            # its unique t>=5 high point must cover all A via triples.
            a = counts[stars.index((0, 4, 2, 0))]
            closed = n[4] > 0 and a % 3 != 0
            reason = 'quad_high_requires_A_triple_partition' if closed else 'unresolved'
        else:
            # Both t=5 quad owners cover every low point via disjoint 4-traces.
            closed = r % 4 != 0
            reason = 'each_of_two_quad_highs_requires_4_divides_r'
        inventories.append({'star_counts': counts, 'n0_to_n4': n,
                            'closed_by_integer_and_Q_phase': closed, 'reason': reason})
    out[str(r)] = {'stars_a1_to_a4': stars, 'inventories': inventories,
                   'remaining_after_integer_and_Q_phase': sum(not x['closed_by_integer_and_Q_phase'] for x in inventories)}
out['final_analytic_conclusion_in_REPORT'] = {'9': 'closed_using_F3_graph_and_W25', '10': 'closed_using_quad_partition_divisibility'}
out['scope'] = 'Only necessary star/count identities under actual M17 contrapositive; no H existence claim.'
out['cpu_seconds'] = time.process_time() - started
Path(__file__).with_name('RESULT.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({r: {'inventories': len(out[r]['inventories']),
                      'remaining': out[r]['remaining_after_integer_and_Q_phase']} for r in ('9','10')}))
print('cpu_seconds', out['cpu_seconds'])
