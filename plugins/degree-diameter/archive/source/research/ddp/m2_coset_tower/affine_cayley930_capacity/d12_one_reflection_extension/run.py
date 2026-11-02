#!/usr/bin/env python3
"""Exactly the 30 one-reflection extensions of the saved degree-11 best."""
import json
import time
from collections import Counter, deque
from pathlib import Path


def main():
    started = time.process_time()
    wall = time.time()
    out = Path(__file__).resolve().parent
    original = json.loads((out.parent / 'd11_production.best.json').read_text())
    n, p, m = 930, 31, 30
    powers = [pow(3, j, p) for j in range(m)]
    S0 = original['S']
    assert len(S0) == len(set(S0)) == 11 and 0 not in S0
    assert [s for s in S0 if s // p == 15] == [9 + p * 15]

    def mul(g, h):
        x, j = g % p, g // p
        y, k = h % p, h // p
        return (x + powers[j] * y) % p + p * ((j + k) % m)

    def inv(g):
        x, j = g % p, g // p
        return (-powers[-j % m] * x) % p + p * (-j % m)

    assert set(map(inv, S0)) == set(S0)
    base_adjacency = [[mul(g, s) for s in S0] for g in range(n)]
    xs = [x for x in range(p) if x != 9]
    rows = []
    best = None
    status = 'COMPLETE_NO_SOLUTION'
    for x in xs:
        if time.process_time() - started >= 5:
            status = 'CPU_LIMIT'
            break
        new_reflection = x + p * 15
        S = S0 + [new_reflection]
        assert len(set(S)) == 12 and inv(new_reflection) == new_reflection
        adjacency = [base_adjacency[g] + [mul(g, new_reflection)] for g in range(n)]
        distances = [-1] * n
        distances[0] = 0
        queue = deque([0])
        while queue:
            g = queue.popleft()
            for h in adjacency[g]:
                if distances[h] < 0:
                    distances[h] = distances[g] + 1
                    queue.append(h)
        spectrum = dict(sorted(Counter(distances).items()))
        missing = sum(t < 0 or t > 3 for t in distances)
        row = {
            'index': len(rows), 'added_reflection': [x, 15],
            'added_element_code': new_reflection, 'S': S,
            'root_deficit_gt3_or_unreachable': missing,
            'bad_unordered_pairs': n * missing // 2,
            'connected': -1 not in spectrum,
            'diameter': max(distances) if -1 not in spectrum else None,
            'root_distance_histogram': spectrum,
        }
        rows.append(row)
        if best is None or missing < best['root_deficit_gt3_or_unreachable']:
            best = dict(row, n=n, m=n * 12 // 2, degree=12, r=3,
                        encoding='x+31*j',
                        selection='minimum_root_deficit_among_evaluated_one_reflection_extensions')
            edges = [(g, h) for g in range(n) for h in adjacency[g] if g < h]
            assert len(edges) == 5580
            with (out / 'best.edges').open('w') as f:
                f.write(f'{n} {len(edges)}\n')
                f.writelines(f'{g} {h}\n' for g, h in edges)
            (out / 'best.json').write_text(json.dumps(best, indent=2) + '\n')
        if missing == 0:
            status = 'FOUND_DIAMETER3'
            break

    with (out / 'results.jsonl').open('w') as f:
        for row in rows:
            f.write(json.dumps(row) + '\n')
    summary = {
        'status': status,
        'scope': 'Add each of the other 30 phase15 reflections to the fixed saved degree11 best S; no replacements or other base graphs',
        'source': '../d11_production.best.json',
        'fixed_S': S0, 'existing_reflection': [9, 15],
        'n': n, 'degree': 12, 'target_diameter': 3,
        'full_scope': 30, 'checked': len(rows),
        'complete_single_root_BFS_runs': len(rows),
        'next_added_x': xs[len(rows)] if len(rows) < len(xs) else None,
        'minimum_root_deficit': best['root_deficit_gt3_or_unreachable'],
        'best_added_reflection': best['added_reflection'],
        'best_diameter': best['diameter'],
        'best_bad_unordered_pairs': best['bad_unordered_pairs'],
        'worker_count': 1, 'restarts': 0,
        'CPU_budget_seconds': 5,
        'CPU_seconds': time.process_time() - started,
        'wall_seconds': time.time() - wall,
        'independent_final': 'parent-owned, pending only for the saved best graph',
    }
    if len(rows) == len(xs):
        best['selection'] = 'minimum_root_deficit_among_all_30_one_reflection_extensions'
        best['selection_scope_complete'] = True
        (out / 'best.json').write_text(json.dumps(best, indent=2) + '\n')
    (out / 'terminal.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
