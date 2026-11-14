"""Geometry-only checks of larger k and the uncovered T15 projections."""

from collections import Counter, defaultdict
from itertools import combinations
import json
from pathlib import Path
from time import process_time

from R7_CONTROLLED_CYCLE_DONOR_PROBE import BITS, INPUT, PERMUTATIONS, canonical, digest, project


def geometry(holes, k, start):
    for j, outer in enumerate(BITS):
        for side in range(2):
            donor = [v for v in holes if bool(v & outer) == side]
            receiver = [v for v in holes if bool(v & outer) != side]
            for beta in range(2):
                source_pool = [v for v in donor if v.bit_count() % 2 == beta]
                if 2 * len(source_pool) - len(donor) != k:
                    continue
                for source in combinations(source_pool, k):
                    if process_time() - start >= 60:
                        raise TimeoutError('geometry probe exceeded 60 CPU seconds')
                    marks = [v ^ outer for v in source]
                    for i, inner in enumerate(BITS):
                        if inner == outer:
                            continue
                        axes = [bit for bit in BITS if bit not in (outer, inner)]
                        faces = []
                        for b in range(2):
                            local_marks = sorted(project(v, axes) for v in marks if bool(v & inner) == b)
                            q = len(local_marks)
                            if not q:
                                break
                            local_minor = sorted(project(v, axes) for v in receiver
                                                 if bool(v & inner) == b and v.bit_count() % 2 == beta)
                            local_included = sorted(project(v, axes) for v in receiver
                                                    if bool(v & inner) == b and v.bit_count() % 2 != beta)
                            if len(local_included) - len(local_minor) != q:
                                break
                            faces.append({'minority': local_minor, 'majority': sorted(local_included + local_marks),
                                          'marks': local_marks, 'q': q})
                        if len(faces) == 2:
                            yield {'outer': j, 'donor_side': side, 'beta': beta, 'inner': i, 'sources': source,
                                   'marks': marks, 'faces': faces}


def main():
    start = process_time()
    reps = json.loads(INPUT.read_bytes())['representatives']
    geometry_counts = {k: {} for k in (3, 4, 5, 6)}
    k7_outer = []
    larger = defaultdict(dict)
    t15_orbits = defaultdict(list)
    for row in reps:
        holes = row['L'] + [127 ^ v for v in row['V']]
        for j, bit in enumerate(BITS):
            gap = sum(1 if v.bit_count() % 2 else -1 for v in holes if v & bit)
            if abs(gap) == 7:
                k7_outer.append({'id': row['id'], 'outer': j, 'side_one_odd_minus_even': gap})
        for k in geometry_counts:
            if k == 3 and row['id'] != 1:
                continue
            witnesses = list(geometry(holes, k, start))
            if witnesses:
                geometry_counts[k][row['id']] = len(witnesses)
            if k > 3 and witnesses:
                larger[k][row['id']] = witnesses
            elif k == 3:
                for witness in witnesses:
                    for face in witness['faces']:
                        if (face['q'], len(face['minority'])) == (2, 1):
                            key = canonical(face['minority'][0], tuple(face['majority']), tuple(face['marks']))
                            t15_orbits[key].append(witness)
    result = {'scope': 'Geometry only. k=3 tests ID 1, k=4,5,6 test all fixed 35 representatives. k=7 checks outer entries.',
              'input_sha256': digest(INPUT), 'geometry_counts': geometry_counts,
              'k7_outer_entries': k7_outer,
              'larger_k_geometry_witnesses': larger, 'id_1_t15_orbits': [
                  {'minority': 0, 'majority': k[0], 'marks': k[1], 'witnesses': v}
                  for k, v in sorted(t15_orbits.items())], 'cpu_seconds': round(process_time() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(geometry_counts, k7_outer, Counter({k: len(v) for k, v in t15_orbits.items()}), result['cpu_seconds'])


if __name__ == '__main__':
    main()
