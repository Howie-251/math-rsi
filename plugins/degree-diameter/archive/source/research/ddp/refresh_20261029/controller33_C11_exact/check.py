from pathlib import Path
from itertools import product, combinations
from collections import Counter
import json
import time

HERE = Path(__file__).resolve().parent
start = time.process_time()


def graph(kind, args):
    adj = [set() for _ in range(33)]

    def add(a, l, b, m):
        u, v = 3 * (a % 11) + l, 3 * (b % 11) + m
        assert u != v and v not in adj[u]
        adj[u].add(v)
        adj[v].add(u)

    for a in range(11):
        for l, m in combinations(range(3), 2):
            add(a, l, a, m)
    if kind == 'three_loops':
        for l, s in enumerate(args):
            for a in range(11):
                add(a, l, a + s, l)
    elif kind == 'loop_and_double':
        loop, s, d, e = args
        l, m = [i for i in range(3) if i != loop]
        for a in range(11):
            add(a, loop, a + s, loop)
            add(a, l, a + d, m)
            add(a, l, a + e, m)
    else:
        assert kind == 'triangle'
        for l, s in enumerate(args):
            for a in range(11):
                add(a, l, a + s, (l + 1) % 3)
    assert all(len(row) == 4 for row in adj)
    assert sum(map(len, adj)) == 132
    return [sorted(row) for row in adj]


def missing(adj, u):
    reach = set()
    for a in adj[u]:
        for b in adj[a]:
            if b != u:
                for c in adj[b]:
                    if c != a:
                        reach.add(c)
    return sorted(set(range(33)) - {u} - set(adj[u]) - reach), reach


def settings():
    for steps in product(range(1, 6), repeat=3):
        yield 'three_loops', steps
    for loop, s in product(range(3), range(1, 6)):
        for d, e in combinations(range(1, 11), 2):
            yield 'loop_and_double', (loop, s, d, e)
    for shifts in product(range(1, 11), repeat=3):
        yield 'triangle', shifts


control = graph('triangle', (1, 3, 5))
probe = []
for l in range(3):
    gaps, reach = missing(control, l)
    next_label = (l + 1) % 3
    same = [a for a in range(11) if 3 * a + l not in reach]
    cross = [a for a in range(11) if 3 * a + next_label in gaps]
    probe.append({'root_label': l, 'same_label_missing_NB3_phases': same,
                  'next_label_missing_nonadjacent_phases': cross})
assert all(not row['same_label_missing_NB3_phases'] for row in probe)
assert [row['next_label_missing_nonadjacent_phases'] for row in probe] == [[], [7], [7, 9]]
(HERE / 'PREDICTION_CHECK.json').write_text(json.dumps(probe, indent=2) + '\n')
counts, root_tests = Counter(), 0
hit = None
with (HERE / 'CASES.jsonl').open('w') as log:
    for kind, args in settings():
        adj = graph(kind, args)
        gaps = [missing(adj, l)[0] for l in range(3)]
        root_tests += 3
        counts[kind] += 1
        row = {'kind': kind, 'parameters': args, 'root_missing_targets': gaps}
        log.write(json.dumps(row, separators=(',', ':')) + '\n')
        if not any(gaps):
            hit = row
            assert all(not missing(adj, u)[0] for u in range(33))
            (HERE / 'CONTROLLER.json').write_text(json.dumps({'adjacency': adj, **row}, indent=2) + '\n')
            with (HERE / 'CONTROLLER.edges').open('w') as out:
                out.write('33 66\n')
                for u in range(33):
                    for v in adj[u]:
                        if u < v:
                            out.write(f'{u} {v}\n')
            break
elapsed = time.process_time() - start
assert elapsed < 2
result = {'status': 'COMPLETE_CONTROLLER_FOUND' if hit else 'ALL_1800_C11_SETTINGS_REJECTED',
          'counts_by_type': dict(counts), 'settings_tested': sum(counts.values()),
          'representative_NB3_root_tests': root_tests, 'prediction_supported': True,
          'valid_controller_count': int(hit is not None), 'complete4125_graphs': 0,
          'CPU_seconds': elapsed, 'solver_calls': 0, 'large_graph_BFS': 0,
          'scope': 'C11 simultaneous triangle-block translation; fixed triangles; disjoint simple external2factor',
          'hit': hit}
if not hit:
    assert dict(counts) == {'three_loops': 125, 'loop_and_double': 675, 'triangle': 1000}
(HERE / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
(HERE / 'TERMINAL.json').write_text(json.dumps({'running': False, 'pending': [], 'status': result['status']}, indent=2) + '\n')
print(json.dumps(result))
