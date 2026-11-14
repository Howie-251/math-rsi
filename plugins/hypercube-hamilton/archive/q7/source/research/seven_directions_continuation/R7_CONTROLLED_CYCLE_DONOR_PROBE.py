"""Replay the bounded k=3,4 geometry probe on the 35 E14 mu=3 representatives."""

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations
import json
from pathlib import Path
import re
from time import process_time


HERE = Path(__file__).resolve().parent
LOCAL = Path('E:/新问题/research/six_directions')
INPUT = HERE / 'R7_MU3_FINAL_REMAINDER.json'
RANK_PROOF = LOCAL / 'Q5_T15_RANK_BATCH_PROOF.md'
RANK_REVIEW = LOCAL / 'Q5_T15_RANK_BATCH_REVIEW.json'
CORE_REVIEW = LOCAL / 'EIGHT_HOLE_FULL_REVIEW.json'
ANALYTIC_GEOMETRY = LOCAL / 't15_analytic_geometry.json'
SPLIT_PROOF = LOCAL / 'Q4_RICH_GLUING.md'
SPLIT_REVIEW = LOCAL / 'Q4_RICH_GLUING_REVIEW.json'
BITS = tuple(1 << i for i in range(7))
PERMUTATIONS = [
    tuple(sum(((v >> i) & 1) << p[i] for i in range(5)) for v in range(32))
    for p in permutations(range(5))
]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def project(v, axes):
    return sum(bool(v & bit) << i for i, bit in enumerate(axes))


@lru_cache(maxsize=None)
def canonical(minor, major, marks):
    return min((tuple(sorted(p[v ^ minor] for v in major)),
                tuple(sorted(p[v ^ minor] for v in marks))) for p in PERMUTATIONS)


def registry():
    review = json.loads(RANK_REVIEW.read_bytes())
    assert review['verdict'] == 'PASS'
    assert digest(RANK_PROOF) == review['audited_input_hashes'][RANK_PROOF.name]
    rows = re.findall(r'^\| (\d+) \| ([\d,]+) \| ([\d,]+) \| \d+ \| 4096 \|$',
                      RANK_PROOF.read_text(encoding='utf-8'), re.MULTILINE)
    ranks = {}
    for i, majority, marks in rows:
        key = canonical(0, tuple(map(int, majority.split(','))), tuple(map(int, marks.split(','))))
        ranks[key] = int(i)
    assert len(ranks) == 15 and set(ranks.values()) == set(range(15))
    return {key: f'Q5_T15_RANK_{index:02}' for key, index in ranks.items()}


def analytic_registry():
    review = json.loads(CORE_REVIEW.read_bytes())
    assert review['verdict'] == 'PASS'
    geo = json.loads(ANALYTIC_GEOMETRY.read_bytes())['T15']['residual_orbits']
    assert digest(ANALYTIC_GEOMETRY) in CORE_REVIEW.read_text(encoding='utf-8')
    registry_rows = review['complete_marked_core_registry']
    cores = {}
    for i, row in registry_rows.items():
        majority = tuple(v for v in row['holes'] if v)
        key = canonical(0, majority, tuple(row['omitted']))
        core = geo[int(i)]
        assert key == canonical(0, tuple(sorted(core['included'] + core['avoided'])), tuple(core['avoided']))
        cores[key] = f'Q5_T15_CORE_{int(i):02}'
    assert len(cores) == 24
    split_review = json.loads(SPLIT_REVIEW.read_bytes())
    assert split_review['verdict'] == 'PASS'
    assert 'sha256:' + digest(SPLIT_PROOF) == split_review['audited_input_hashes'][SPLIT_PROOF.name]
    return cores


def plans(holes, k, ranks, cores, start):
    colors = tuple(tuple(v for v in holes if v.bit_count() % 2 == p) for p in range(2))
    gaps = Counter()
    first_miss = None
    for outer_index, outer in enumerate(BITS):
        for a_side in range(2):
            counts_a = tuple(sum(bool(v & outer) == a_side for v in color) for color in colors)
            for beta in range(2):
                r = counts_a[1 - beta]
                s = 7 - counts_a[beta]
                if counts_a[beta] - r != k:
                    continue
                assert 0 <= r <= 5 and r + s + k == 7
                gaps['outer_orientations'] += 1
                donors = tuple(v for v in colors[beta] if bool(v & outer) == a_side)
                minority = tuple(v for v in colors[beta] if bool(v & outer) != a_side)
                majority = tuple(v for v in colors[1 - beta] if bool(v & outer) != a_side)
                for source in combinations(donors, k):
                    if process_time() - start >= 60:
                        raise TimeoutError('geometry probe exceeded 60 CPU seconds')
                    marks = tuple(sorted(v ^ outer for v in source))
                    assert not set(marks) & set(holes)
                    for inner_index, inner in enumerate(BITS):
                        if inner == outer:
                            continue
                        axes = tuple(bit for bit in BITS if bit not in (outer, inner))
                        faces = []
                        for side in range(2):
                            face_minor = tuple(v for v in minority if bool(v & inner) == side)
                            face_major = tuple(v for v in majority if bool(v & inner) == side)
                            face_marks = tuple(v for v in marks if bool(v & inner) == side)
                            q = len(face_marks)
                            if q == 0 or len(face_major) - len(face_minor) != q:
                                break
                            faces.append((face_minor, face_major, face_marks))
                        if len(faces) != 2:
                            continue
                        gaps['geometry_plans'] += 1
                        admitted = []
                        for face_minor, face_major, face_marks in faces:
                            local_minor = tuple(sorted(project(v, axes) for v in face_minor))
                            local_marks = tuple(sorted(project(v, axes) for v in face_marks))
                            local_major = tuple(sorted(project(v, axes) for v in face_major + face_marks))
                            q = len(local_marks)
                            m = len(local_minor)
                            if q == 1:
                                tool = 'Q5_A_ALL'
                            elif (q, m) == (2, 0):
                                tool = 'Q5_T44'
                            elif (q, m) == (2, 1):
                                key = canonical(local_minor[0], local_major, local_marks)
                                tool = ranks.get(key)
                                if tool is None and cores is not None:
                                    translated_major = tuple(v ^ local_minor[0] for v in local_major)
                                    split = [i for i in range(5) if (local_marks[0] ^ local_marks[1]) & (1 << i)
                                             and sum(bool(v & (1 << i)) for v in translated_major) == 2]
                                    tool = cores.get(key)
                                    if tool is None and split:
                                        tool = f'Q5_T15_SPLIT_AXIS_{split[0]}'
                                if tool is None and first_miss is None:
                                    first_miss = {'minority': 0, 'majority': key[0], 'marked': key[1]}
                            else:
                                tool = None
                            if tool is None:
                                gaps[f'missing_q{q}_m{m}'] += 1
                            admitted.append({'minority': local_minor, 'majority': local_major,
                                             'marked': local_marks, 'tool': tool})
                        if all(face['tool'] for face in admitted):
                            return {'k': k, 'r': r, 's': s, 'outer_axis': outer_index,
                                    'donor_outer_side': a_side, 'beta': beta, 'inner_axis': inner_index,
                                    'donor_sources': source, 'receiver_marks': marks,
                                    'faces_by_inner_side': admitted}, gaps, first_miss
    return None, gaps, first_miss


def main():
    start = process_time()
    ranks = registry()
    cores = analytic_registry()
    rows = json.loads(INPUT.read_bytes())['representatives']
    assert len(rows) == 35
    result = []
    for row in rows:
        holes = tuple(sorted(row['L'] + [127 ^ v for v in row['V']]))
        assert len(set(holes)) == 14
        assert all((u ^ v).bit_count() != 1 for u, v in combinations(holes, 2))
        entry = {key: row[key] for key in ('id', 'template', 'L', 'V')}
        for name, k, domain in (('k3_rank_only', 3, None), ('k4_rank_only', 4, None), ('k3_expanded', 3, cores)):
            witness, diagnostics, first_miss = plans(holes, k, ranks, domain, start)
            entry[name] = {'witness': witness, 'diagnostics_until_first_hit': diagnostics,
                           'first_nonadmitted_canonical_T15': first_miss}
        result.append(entry)
    summary = {name: [row['id'] for row in result if row[name]['witness']]
               for name in ('k3_rank_only', 'k4_rank_only', 'k3_expanded')}
    summary['uncovered'] = [row['id'] for row in result if not any(row[name]['witness'] for name in summary)]
    payload = {'scope': 'Geometry-only probe with q=1 difference-two and q=2 T44 and T15. The k=3 expanded pass adds the audited 24 analytic cores and geometric split domain. Pending transfer and projection audit.',
               'sha256': {path.name: digest(path) for path in (INPUT, RANK_PROOF, RANK_REVIEW, CORE_REVIEW,
                                                               ANALYTIC_GEOMETRY, SPLIT_PROOF, SPLIT_REVIEW)},
               'cpu_seconds': round(process_time() - start, 3), 'summary': summary, 'representatives': result}
    Path(__file__).with_suffix('.json').write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(summary, payload['cpu_seconds'])


if __name__ == '__main__':
    main()
