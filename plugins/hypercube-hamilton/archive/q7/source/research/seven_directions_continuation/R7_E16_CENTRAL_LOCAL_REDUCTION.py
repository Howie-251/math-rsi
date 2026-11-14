"""Count residual local 3/5 receiving faces for the E16 central cut."""

from collections import Counter
from hashlib import sha256
from itertools import combinations, permutations
import json
from math import comb
from pathlib import Path
from time import process_time


HERE = Path(__file__).resolve().parent
CPU_LIMIT = 10
REP_LIMIT = 2000
AXES = tuple(range(6))
UNITS = tuple(1 << i for i in AXES)
CASES = (('222', (0, 3, 5)), ('224', (0, 3, 12)), ('244', (0, 3, 29)),
         ('246', (0, 3, 60)), ('444', (0, 15, 51)))
IMPORTS = ('R7_CONTROLLED_CYCLE_DONOR_TRANSFER.md', 'R7_MU3_CONTROLLED_AND_T63_REVIEW.json',
           'R7_DELTA2_SINGLE_ROOT_RECEIVER.md', 'R7_DELTA2_SINGLE_ROOT_RECEIVER_REVIEW.json')


def check_time(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError


def permutation_maps(start):
    for permutation in permutations(AXES):
        check_time(start)
        yield tuple(sum(1 << permutation[i] for i in AXES if x & UNITS[i]) for x in range(64))


def stabilizer(S, coordinate_maps, start):
    actions = []
    for coordinate_map in coordinate_maps:
        check_time(start)
        for shift in S:
            if tuple(sorted(coordinate_map[s] ^ shift for s in S)) == S:
                actions.append(tuple(x ^ shift for x in coordinate_map))
    return tuple(actions)


def run():
    start = process_time()
    rows = []
    representative_count = 0
    status = 'complete'
    try:
        maps = tuple(permutation_maps(start))
        for kind, S in CASES:
            check_time(start)
            assert all(s.bit_count() % 2 == 0 for s in S)
            assert ''.join(str(d) for d in sorted((a ^ b).bit_count() for a, b in combinations(S, 2))) == kind
            actions = stabilizer(S, maps, start)
            forbidden = {s ^ bit for s in S for bit in UNITS}
            allowed = tuple(x for x in range(64) if x.bit_count() % 2 and x not in forbidden)
            minority_load = tuple(sum(bool(s & bit) for s in S) for bit in UNITS)
            mixed_columns = [(bit, n + 1) for bit, n in zip(UNITS, minority_load) if n in (1, 2)]
            covered = set()
            reps = []
            counts = Counter()
            row = dict(distance_type=kind, S=S, minority_column_load=minority_load,
                       stabilizer_size=len(actions), admissible_T_points=allowed,
                       candidate_T_count=comb(len(allowed), 5), counts=counts, representatives=reps,
                       status='in_progress')
            rows.append(row)
            for T in combinations(allowed, 5):
                check_time(start)
                counts['candidate_T_visited'] += 1
                if any(sum(bool(t & bit) for t in T) == target for bit, target in mixed_columns):
                    counts['automatic_column'] += 1
                    continue
                counts['labeled_residual'] += 1
                if T in covered:
                    continue
                orbit = {tuple(sorted(action[t] for t in T)) for action in actions}
                assert T == min(orbit)
                covered.update(orbit)
                reps.append(dict(T=T, orbit_size=len(orbit)))
                representative_count += 1
                if representative_count == REP_LIMIT:
                    status = 'representative_limit'
                    break
            if status != 'complete':
                row['status'] = status
                break
            assert counts['candidate_T_visited'] == row['candidate_T_count']
            assert counts['labeled_residual'] == len(covered) == sum(x['orbit_size'] for x in reps)
            row['status'] = 'complete'
        check_time(start)
    except TimeoutError:
        status = 'cpu_limit'
        if rows and rows[-1]['status'] == 'in_progress':
            rows[-1]['status'] = status
    return dict(status=status, cpu_seconds=process_time() - start, cpu_limit_seconds=CPU_LIMIT,
                local_representative_limit=REP_LIMIT, residual_representatives=representative_count,
                rows=rows, original_matching_enumerations=0, outer_face_pair_enumerations=0,
                solver_calls=0, rank_runs=0,
                imported_hashes={name: sha256((HERE / name).read_bytes()).hexdigest() for name in IMPORTS})


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    summary = {key: value for key, value in result.items() if key not in ('rows', 'imported_hashes')}
    summary['rows'] = [{**{key: value for key, value in row.items() if key != 'representatives'},
                        'residual_representatives': len(row['representatives'])} for row in result['rows']]
    print(json.dumps(summary))
