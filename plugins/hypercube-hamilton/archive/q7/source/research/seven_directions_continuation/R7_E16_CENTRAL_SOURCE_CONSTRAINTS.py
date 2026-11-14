"""Bounded source-mirror geometry count over the frozen 580 receiving faces."""

from collections import Counter
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from time import process_time

from R7_E16_CENTRAL_LOCAL_REDUCTION import AXES, UNITS, permutation_maps, stabilizer


HERE = Path(__file__).resolve().parent
SOURCE = 'R7_E16_CENTRAL_LOCAL_REDUCTION.json'
SOURCE_HASH = '24125592d30e7c450145df69209c34f52757c4eb8c8a8a5088f121ceaa8ca3cd'
CPU_LIMIT = 10
REP_LIMIT = 2000
ODD = tuple(x for x in range(64) if x.bit_count() % 2)


def check_time(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError


def load(points, bit, side):
    return sum(bool(x & bit) == side for x in points)


def constraints(S, T):
    constant, fixed, sparse = [], [], []
    for i, bit in enumerate(UNITS):
        s, t = load(S, bit, 1), load(T, bit, 1)
        if t - s == 1:
            assert s in (0, 3), 'Automatic-column cases should have been removed'
            constant.append(i)
        for side, small, large in ((1, s, t), (0, 3 - s, 5 - t)):
            if small <= 1 and large - small == 2:
                fixed.append((i, 1 - side))
            if small <= 1 and large - small == 3:
                sparse.append((i, side))
    assert len(set(constant + [i for i, _ in fixed + sparse])) == len(constant) + len(fixed) + len(sparse)
    return constant, fixed, sparse


def branch_pools(T, constant, fixed, sparse):
    if len(constant) + len(fixed) >= 3:
        return (), 'fixed_coordinate_parity', Counter()
    candidates = tuple(x for x in ODD if x not in T)
    assert len(candidates) == 27
    mask = sum(1 << i for i in constant) + sum(1 << i for i, _ in fixed)
    pattern = sum(side << i for i, side in fixed)
    pools = []
    stats = Counter()
    for choices in product((0, 1), repeat=len(constant)):
        stats['assignments'] += 1
        chosen = pattern + sum(side << i for i, side in zip(constant, choices))
        available = [(x, sum(1 << i for i, side in sparse if ((x >> i) & 1) == side))
                     for x in candidates if x & mask == chosen]
        if len(available) < 5:
            stats['too_few_points'] += 1
            continue
        if sum(used == 0 for _, used in available) + len(sparse) < 5:
            stats['projection_capacity'] += 1
            continue
        pools.append(tuple(available))
    return tuple(pools), None if pools else 'all_branch_pools_impossible', stats


def valid_fives(available, sparse_count, start):
    def select(index, occupied, chosen):
        check_time(start)
        needed = 5 - len(chosen)
        if needed == 0:
            yield chosen
            return
        compatible = [(x, mask) for x, mask in available[index:] if not occupied & mask]
        if len(compatible) < needed:
            return
        if sum(mask == 0 for _, mask in compatible) + sparse_count - occupied.bit_count() < needed:
            return
        for j in range(index, len(available) - needed + 1):
            x, mask = available[j]
            if not occupied & mask:
                yield from select(j + 1, occupied | mask, (*chosen, x))

    yield from select(0, 0, ())


def run():
    start = process_time()
    frozen = (HERE / SOURCE).read_bytes()
    assert sha256(frozen).hexdigest() == SOURCE_HASH
    source = json.loads(frozen)
    assert source['status'] == 'complete' and source['residual_representatives'] == 580
    rows, pending = [], []
    status = 'complete'
    total = 0
    first_positive = None
    active = None
    for block in source['rows']:
        S = tuple(block['S'])
        for j, rep in enumerate(block['representatives']):
            row = dict(distance_type=block['distance_type'], local_index=j, S=S, T=tuple(rep['T']),
                       status='unvisited', labeled_Y_visited=0, representatives=[])
            rows.append(row)
    assert len(rows) == 580
    try:
        for row in rows:
            check_time(start)
            constant, fixed, sparse = constraints(row['S'], row['T'])
            pools, direct_zero, stats = branch_pools(row['T'], constant, fixed, sparse)
            row.update(constant=constant, fixed=fixed, sparse=sparse, assignment_counts=stats)
            if direct_zero:
                row.update(status='completed', zero_reason=direct_zero)
            else:
                pending.append((row, pools))

        maps = tuple(permutation_maps(start))
        groups = {tuple(block['S']): stabilizer(tuple(block['S']), maps, start) for block in source['rows']}
        for row, pools in pending:
            check_time(start)
            active = row
            row['status'] = 'in_progress'
            T = row['T']
            actions = tuple(action for action in groups[row['S']] if tuple(sorted(action[x] for x in T)) == T)
            row['stabilizer_size'] = len(actions)
            covered = set()
            for pool in pools:
                for Y in valid_fives(pool, len(row['sparse']), start):
                    row['labeled_Y_visited'] += 1
                    if Y in covered:
                        continue
                    orbit = {tuple(sorted(action[x] for x in Y)) for action in actions}
                    covered.update(orbit)
                    rep = dict(Y=min(orbit), orbit_size=len(orbit))
                    row['representatives'].append(rep)
                    total += 1
                    if first_positive is None:
                        first_positive = dict(distance_type=row['distance_type'], local_index=row['local_index'],
                                              S=row['S'], T=T, **rep)
                    if total == REP_LIMIT:
                        status = 'representative_limit'
                        break
                if status != 'complete':
                    break
            if status != 'complete':
                break
            assert row['labeled_Y_visited'] == len(covered)
            row['status'] = 'completed'
            if not covered:
                row['zero_reason'] = 'exact_recursive_count'
            active = None
        check_time(start)
    except TimeoutError:
        status = 'cpu_limit'
    summary = Counter(row['status'] for row in rows)
    summary.update('zero_' + row['zero_reason'] for row in rows if 'zero_reason' in row)
    summary['completed_positive'] = sum(row['status'] == 'completed' and bool(row['representatives']) for row in rows)
    return dict(status=status, cpu_seconds=process_time() - start, cpu_limit_seconds=CPU_LIMIT,
                representative_limit=REP_LIMIT, representative_count=total, row_counts=summary,
                first_positive=first_positive,
                stop_row=None if active is None else (active['distance_type'], active['local_index']),
                frozen_input=SOURCE, frozen_sha256=SOURCE_HASH, rows=rows,
                original_matching_enumerations=0, opposite_minority_completions=0, solver_calls=0, rank_runs=0)


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in result.items() if key != 'rows'}))
