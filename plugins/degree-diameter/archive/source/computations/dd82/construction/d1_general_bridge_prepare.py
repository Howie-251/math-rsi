#!/usr/bin/env python3
"""Write only the ten configurations and their leave choices, not 4M bridges."""
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'd1_general_bridge_run'


def cycles(edges):
    adj = [[] for _ in range(10)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    unseen = set(range(10))
    result = []
    while unseen:
        start = min(unseen)
        previous, current = start, min(adj[start])
        cycle = [start]
        while current != start:
            cycle.append(current)
            previous, current = current, next(v for v in adj[current] if v != previous)
        unseen.difference_update(cycle)
        result.append(cycle)
    return sorted(result, key=lambda c: (len(c), c))


def mate(choice):
    ans = [-1]*10
    for u, v in choice['matching']:
        ans[u], ans[v] = v, u
    return ans


def main():
    start = time.process_time()
    OUT.mkdir(exist_ok=True)
    source = HERE/'d1_10_3_catalog/local_interfaces.json'
    catalog = json.loads(source.read_text())['configurations']
    states = []
    with (OUT/'inputs.txt').open('w') as out:
        out.write('10\n')
        for c in catalog:
            z = [sum(1 << v for v in row) for row in c['primal']['Z_row_supports']]
            pc, dc = c['primal']['choices'], c['dual']['choices']
            out.write(' '.join(map(str, [c['grunbaum_number'], len(pc), len(dc)] + z))+'\n')
            for side in (pc, dc):
                for choice in side:
                    cc = cycles(choice['factor_edges'])
                    data = mate(choice)+[len(cc)]
                    for cycle in cc:
                        data += [len(cycle)]+cycle
                    out.write(' '.join(map(str, data))+'\n')
            for p, left in enumerate(pc):
                for d, right in enumerate(dc):
                    states.append({'state_id': len(states), 'configuration': c['grunbaum_number'],
                                   'primal_choice': p, 'dual_choice': d, 'Z_rows': z,
                                   'S_L': mate(left), 'S_R': mate(right)})
    assert len(states) == 531
    (OUT/'states.json').write_text(json.dumps(states, indent=2)+'\n')
    meta = {'source': str(source), 'configuration_count': 10, 'state_count': len(states),
            'expected_state_Y_bridges': 4278652,
            'expected_by_cycle_type': {'5,5':1377800, '10':1788020, '4,6':921984,
                                       '3,7':162624, '3,3,4':28224},
            'scope': 'Compact preparation only; Y alignments generated online in C++',
            'cpu_seconds': time.process_time()-start}
    (OUT/'preparation.json').write_text(json.dumps(meta, indent=2)+'\n')
    print(json.dumps(meta, indent=2))


if __name__ == '__main__':
    main()
