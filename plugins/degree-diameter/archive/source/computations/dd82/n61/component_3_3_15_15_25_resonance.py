#!/usr/bin/env python3
"""New five-entry C15-versus-Cq resonance table; no graph search.

Reuses only exact polynomial arithmetic from the earlier C30 calculation.
Importing that module does not execute its previous table.
"""
from pathlib import Path
import json
import resource
import time
from component_6_25_30_resonance import (
    add, compose_minus_one_minus_x, divide, gcd, ints,
)


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (1, 1))
    cpu, wall = time.process_time(), time.perf_counter()
    lp = [[2], [0, 1]]
    for p in range(2, 26):
        lp.append(add([0]+lp[-1], [-x for x in lp[-2]]))
    chi = {p: add(lp[p], [-2]) for p in range(3, 26)}
    records = []
    for q in (5, 10, 15, 20, 25):
        shifted = compose_minus_one_minus_x(chi[q])
        g, degrees = gcd(chi[15], shifted)
        qa, ra = divide(chi[15], g)
        qb, rb = divide(shifted, g)
        assert ra == rb == [0]
        records.append({
            'p': 15, 'q': q,
            'chi_q_ascending': chi[q],
            'shifted_chi_q_ascending': shifted,
            'monic_gcd_ascending': ints(g),
            'chi_15_over_gcd_ascending': ints(qa),
            'shifted_chi_q_over_gcd_ascending': ints(qb),
            'euclidean_dividend_divisor_degrees': degrees,
        })
    result = {
        'scope': 'gcd_Q[x](chi_C15(x),chi_Cq(-1-x)), q=5,10,15,20,25',
        'complete': True,
        'arithmetic': 'integer cycle recurrence and rational Euclidean division',
        'chi_15_ascending': chi[15],
        'records': records,
        'cpu_limit_seconds': 1,
        'graph_searches': 0, 'solver_calls': 0,
        'previous_resonance_table_reruns': 0,
        'cpu_seconds': time.process_time()-cpu,
        'wall_seconds': time.perf_counter()-wall,
    }
    out = Path(__file__).with_suffix('.result.json')
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({
        'output': str(out), 'complete': True,
        'gcds': [[r['q'], r['monic_gcd_ascending']] for r in records],
        'cpu_seconds': result['cpu_seconds'],
        'wall_seconds': result['wall_seconds'],
    }, indent=2))


if __name__ == '__main__':
    main()
