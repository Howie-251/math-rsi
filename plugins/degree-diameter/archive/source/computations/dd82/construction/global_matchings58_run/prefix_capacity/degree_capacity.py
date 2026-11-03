"""Integer degree-capacity bounds for saved seed0/3, round6 only.

At most ten strictly improving coordinate sweeps on bound parameters.
No graph generation, matching optimizer, SAT, or floating-point solver.
"""
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('degree_capacity_gain', HERE.parent / 'generate.py')
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


def diagnose(seed):
    cpu, wall = time.process_time(), time.monotonic()
    source = HERE.parent / f'pilot/seed{seed}/rounds.json'
    data = json.loads(source.read_text())
    edges = set()
    for row in data['rounds'][:6]:
        matching = list(map(tuple, row['matching_edges']))
        assert len(matching) == 29 and not edges.intersection(matching)
        edges.update(matching)
    adj = generator.bit_adjacency(58, edges)
    assert all(row.bit_count() == 6 for row in adj)
    bad, masks = generator.bad_pairs(adj)
    assert [list(xy) for xy in bad] == data['rounds'][5]['bad_pairs']
    gains, incident = [], [[] for _ in range(58)]
    for x, y in combinations(range(58), 2):
        if (x, y) not in edges:
            gain = generator.single_edge_gain(adj, masks, x, y)
            gains.append((x, y, gain))
            incident[x].append((y, gain))
            incident[y].append((x, gain))
    d = 2
    initial_t = [sorted((gain for _, gain in row), reverse=True)[d-1] for row in incident]
    t = list(initial_t)

    def rhs():
        return d*sum(t) + sum(max(0, 2*g-t[x]-t[y]) for x, y, g in gains)

    initial_rhs = current = rhs()
    updates, sweeps = [], []
    for sweep in range(1, 11):
        changed = 0
        for x in range(58):
            changes = []
            for step in (-1, 1):
                delta = d*step + sum(max(0, 2*g-t[x]-step-t[y]) -
                                     max(0, 2*g-t[x]-t[y]) for y, g in incident[x])
                changes.append((delta, step))
            delta, step = min(changes)
            if delta < 0:
                previous = t[x]
                t[x] += step
                current += delta
                changed += 1
                updates.append(dict(sweep=sweep, vertex=x, before=previous, after=t[x],
                                    rhs_change=delta, rhs_after=current))
        assert current == rhs()
        sweeps.append(dict(sweep=sweep, accepted_updates=changed, rhs=current))
        if not changed:
            break
        assert time.process_time()-cpu < 5
    positive = [dict(edge=[x, y], gain=g, positive_residual=2*g-t[x]-t[y])
                for x, y, g in gains if 2*g-t[x]-t[y] > 0]
    residual_sum = sum(row['positive_residual'] for row in positive)
    assert current == d*sum(t) + residual_sum
    top_d_total = sum(sum(sorted((g for _, g in row), reverse=True)[:d]) for row in incident)
    two_new_bound = 58
    bound = current//2 + two_new_bound
    return dict(seed=seed, round=6, residual_degree=d, bad_pairs=len(bad),
                source=str(source), ambient_labels=data['ambient_labels'],
                initial_potentials=initial_t, initial_rhs=initial_rhs,
                final_potentials=t, degree_term=d*sum(t), positive_residual_sum=residual_sum,
                positive_residual_edges=positive, final_rhs=current,
                single_edge_gain_upper_bound=current//2,
                two_new_path_upper_bound=two_new_bound, total_repair_upper_bound=bound,
                old_top_d_upper_bound=top_d_total//2+two_new_bound,
                impossible_monotone_completion=bound < len(bad),
                residual_bad_pairs_lower_bound=max(0, len(bad)-bound),
                sweeps=sweeps, updates=updates,
                stop_reason='NO_STRICT_COORDINATE_IMPROVEMENT' if not sweeps[-1]['accepted_updates']
                            else 'TEN_SWEEP_LIMIT',
                elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)


if __name__ == '__main__':
    path = HERE / 'degree_capacity.json'
    assert not path.exists(), 'Preserve previous bound witnesses'
    records = [diagnose(seed) for seed in (0, 3)]
    result = dict(status='COMPLETE_INTEGER_DEGREE_CAPACITY_DIAGNOSTIC',
                  graph_generation_calls=0, matching_calls=0, solver_calls=0,
                  maximum_coordinate_sweeps=10, records=records)
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps([{key: row[key] for key in
                      ('seed', 'round', 'bad_pairs', 'initial_rhs', 'final_rhs',
                       'old_top_d_upper_bound', 'total_repair_upper_bound',
                       'impossible_monotone_completion', 'residual_bad_pairs_lower_bound',
                       'stop_reason', 'elapsed_cpu', 'elapsed_wall')} for row in records], indent=2))
