"""Independent, search-free audit of the exact Q4 T15 classification.

Does not import or execute the producer or earlier certificate checkers.
Every negative is discharged by a forced triangle, never by failed search.
"""
from pathlib import Path
from itertools import combinations, permutations
from collections import Counter
import hashlib
import json

ROOT = Path(__file__).resolve().parent
VERTICES = frozenset(range(16))
ODD = frozenset(x for x in VERTICES if x.bit_count() % 2)
PERMS = tuple(permutations(range(4)))
REPS = ((1, 2), (2, 4), (1, 14), (2, 14))


def require(condition, label):
    if not condition:
        raise ValueError(label)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pairings(vertices):
    """Unordered edge-set universe; unrelated to producer's mate recursion."""
    vertices = tuple(sorted(vertices))
    if not vertices:
        yield frozenset()
        return
    first = vertices[0]
    for partner in vertices[1:]:
        for smaller in pairings(x for x in vertices if x not in (first, partner)):
            yield smaller | {(first, partner)}


def decode_matching(raw, holes):
    require(len(raw) == 16, 'mate length')
    require({x for x, y in enumerate(raw) if y == 255} == set(holes), 'hole support')
    for x, y in enumerate(raw):
        if x not in holes:
            require(y in VERTICES - set(holes) and x != y and raw[y] == x,
                    'mate involution')
    return frozenset((x, y) for x, y in enumerate(raw) if x < y < 16)


def check_cycle(cycle, matching, avoided):
    require(len(cycle) == 14 and set(cycle) == VERTICES - set(avoided),
            'simple 14-cycle exact support')
    edges = frozenset(tuple(sorted((cycle[i], cycle[(i + 1) % 14]))) for i in range(14))
    require(len(edges) == 14 and matching <= edges, 'all prescribed edges on cycle')
    require(all((x ^ y).bit_count() == 1 for x, y in edges - matching),
            'every new edge short')


def transform(x, perm):
    return sum(((x >> i) & 1) << perm[i] for i in range(4))


def residual_certificates():
    source = json.loads((ROOT / 'q4_six_two_avoided_results.json').read_text())
    source_rows = {tuple(row['avoided']): row for row in source['orbits']}
    require(set(source_rows) == set(REPS), 'diagnostic orbit list')
    reports = []
    for avoided in REPS:
        holes = {0, 7, 11, 13, *avoided}
        expected = set(pairings(VERTICES - holes))
        require(len(expected) == 945, 'independent matching universe count')
        name = 'q4_six_two_avoided_%d_%d.bin' % avoided
        data = (ROOT / name).read_bytes()
        require(len(data) == 945 * 30, 'residual byte length')
        negative = positive = 0
        for offset in range(0, len(data), 30):
            matching = decode_matching(data[offset:offset + 16], holes)
            require(matching in expected, 'universe membership and no duplicates')
            expected.remove(matching)
            remaining_neighbors = {1, 2, 4, 8} - set(avoided)
            obstruction = (set(avoided) <= {1, 2, 4, 8}
                           and tuple(sorted(remaining_neighbors)) in matching)
            cycle = data[offset + 16:offset + 30]
            if cycle == bytes([255]) * 14:
                require(obstruction, 'negative has forced triangle obstruction')
                p, q = sorted(remaining_neighbors)
                require(p not in holes and q not in holes and (p, q) in matching,
                        'triangle neighbors covered and prescribed edge present')
                negative += 1
            else:
                require(not obstruction, 'positive cannot contain forced triangle')
                check_cycle(cycle, matching, avoided)
                positive += 1
        require(not expected, 'complete matching coverage')
        wanted_negative = 105 if avoided in ((1, 2), (2, 4)) else 0
        require(negative == wanted_negative, 'exact negative count')
        require(source_rows[avoided]['records'] == 945
                and source_rows[avoided]['bad'] == negative, 'diagnostic count agreement')
        for first_failure in source_rows[avoided]['first_failures']:
            require(tuple(sorted({1, 2, 4, 8} - set(avoided)))
                    in {tuple(sorted(e)) for e in first_failure}, 'listed sample obstruction')
        reports.append({'file': name, 'avoided': avoided, 'records': 945,
                        'positive': positive, 'negative_with_triangle_proof': negative,
                        'sha256': digest(data)})
    return reports


def t44_dependency():
    """Recheck all positive T44 data, without invoking an earlier checker."""
    even = VERTICES - ODD
    configs = {(p, b, t) for p in (3, 15)
               for b, t in combinations(sorted(even - {0, p}), 2)}
    reports = []
    for p, b, t in sorted(configs):
        holes = {0, p, b, t}
        expected = set(pairings(VERTICES - holes))
        require(len(expected) == 10395, 'T44 universe count')
        name = f'q4_two_avoided_{p}_{b}_{t}.bin'
        data = (ROOT / name).read_bytes()
        require(len(data) == 30 * 10395, 'T44 byte length')
        for offset in range(0, len(data), 30):
            matching = decode_matching(data[offset:offset + 16], holes)
            require(matching in expected, 'T44 complete unique matching')
            expected.remove(matching)
            check_cycle(data[offset + 16:offset + 30], matching, (0, p))
        require(not expected, 'T44 no missing matching')
        reports.append({'file': name, 'records': 10395, 'sha256': digest(data)})
    # Independent exhaustive geometry cover, both parity classes.
    checked = 0
    for parity_vertices in (even, ODD):
        for holes in combinations(sorted(parity_vertices), 4):
            for x, y in combinations(holes, 2):
                others = set(holes) - {x, y}
                require(any((transform(y ^ x, perm),
                             *sorted(transform(h ^ x, perm) for h in others)) in configs
                            for perm in PERMS), 'T44 all marked holes geometry')
                checked += 1
    require(checked == 840, 'T44 geometry count')
    return {'records': 311850, 'geometries': checked, 'certificates': reports}


def geometry_and_augmentation():
    representative_images = {}
    for rep in REPS:
        images = {(frozenset(transform(h, perm) for h in (7, 11, 13)),
                   frozenset(transform(h, perm) for h in rep)) for perm in PERMS}
        representative_images[rep] = images
    require([len(representative_images[r]) for r in REPS] == [12, 12, 4, 12],
            'residual orbit sizes')
    union = set().union(*representative_images.values())
    require(len(union) == 40, 'four residual orbits disjoint')
    counts = Counter()
    for a in sorted(VERTICES - ODD):
        neighbors = {a ^ (1 << i) for i in range(4)}
        for majority in combinations(sorted(ODD), 5):
            for forbidden in combinations(majority, 2):
                available = set(majority) - set(forbidden)
                candidates = available & neighbors
                if candidates:
                    # a and chosen b are unmatched and the edge ab is short.
                    b = min(candidates)
                    require((a ^ b).bit_count() == 1, 'short augmented edge')
                    new_holes = set(majority) - {b}
                    require(len(new_holes) == 4 and set(forbidden) <= new_holes
                            and new_holes <= ODD, 'T44 augmentation hypotheses')
                    require(len(VERTICES - {a, *majority}) == 10
                            and a not in majority, 'augmented edge disjoint from original')
                    counts['augmentation'] += 1
                else:
                    normalized = (frozenset(h ^ a for h in available),
                                  frozenset(h ^ a for h in forbidden))
                    require(normalized in union, 'residual full marked geometry cover')
                    counts['residual'] += 1
                # An adjacent available hole rules out the obstruction:
                # at least one remaining allowed neighbor is a hole, so not F-covered.
                if set(forbidden) <= neighbors:
                    p_and_q = neighbors - set(forbidden)
                    if candidates:
                        require(bool(p_and_q & set(majority)),
                                'augmentation incompatible with triangle matching edge')
                counts['all'] += 1
    require(dict(counts) == {'augmentation': 4160, 'all': 4480, 'residual': 320},
            'all marked E1/O5 geometries count')
    return {'marked_E1_O5_geometries': counts['all'],
            'augmentation_geometries': counts['augmentation'],
            'residual_geometries': counts['residual'],
            'minority_zero_orbit_sizes': {str(r): len(representative_images[r]) for r in REPS},
            'normalized_minor_zero_geometries': 560,
            'normalized_minor_zero_augmentation': 520,
            'normalized_minor_zero_residual': 40}


def main():
    residual = residual_certificates()
    t44 = t44_dependency()
    geometry = geometry_and_augmentation()
    input_names = ['q4_six_hole_two_avoided.cpp', 'q4_six_two_avoided_results.json',
                   'Q4_TWO_AVOIDED_TRANSFER.md', 'Q4_TWO_AVOIDED_REVIEW.json']
    result = {'status': 'PASS', 'method': 'independent unordered edge-set universe; '
              'explicit positive cycles; analytic forced-triangle negatives; full geometry cover',
              'residual_records': 3780, 'positive_records': 3570,
              'negative_records_with_analytic_proof': 210, 'residual_files': residual,
              't44_dependency_reverified': t44, 'geometry': geometry,
              'input_sha256': {name: digest((ROOT / name).read_bytes()) for name in input_names},
              'checker_sha256': digest(Path(__file__).read_bytes()),
              'full_q5_t15_proved': False,
              'full_p6_proved': False}
    out = ROOT / 'q4_t15_classification_independent_check.json'
    out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'residual_records', 'positive_records',
          'negative_records_with_analytic_proof', 'geometry')}, indent=2))


if __name__ == '__main__':
    main()
