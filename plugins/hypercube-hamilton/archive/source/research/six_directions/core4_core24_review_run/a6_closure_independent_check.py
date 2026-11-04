"""Independent A6 geometry, cut-exception, and imported-hash checks.

Does not import the producer/census or modify proof or project status.
All assertions must remain enabled. The semantic transfer proof is audited
separately in A6_CLOSURE_REVIEW.md; this is not enumeration of K(Q5) matchings.
"""
from pathlib import Path
from itertools import combinations, permutations
from collections import Counter
import hashlib
import json

ROOT = Path(__file__).resolve().parent
V = set(range(32))
odd = {x for x in V if x.bit_count() % 2}


def permute(x, p):
    return sum(((x >> i) & 1) << p[i] for i in range(5))


def geometry():
    counts = Counter()
    normalized = Counter()
    exceptions = []
    total = 0
    for z in sorted(V - odd - {0}):
        allowed = [x for x in sorted(odd)
                   if x.bit_count() > 1 and (x ^ z).bit_count() > 1]
        # Explicitly construct a cube automorphism normalizing each minority pair.
        target = 3 if z.bit_count() == 2 else 15
        p = next(p for p in permutations(range(5)) if permute(z, p) == target)
        for triple in combinations(allowed, 3):
            for v in sorted(odd-set(triple)):
                total += 1
                H_E, H_O = {0, z}, set(triple) | {v}
                ds = []
                for j in range(5):
                    A = {x for x in V if (x ^ v) & (1 << j) == 0}
                    e, o = len(A & H_E), len(A & H_O)
                    ds.append(o-e)
                    # These forbidden cases are excluded geometrically, not by c.
                    assert (o-e, e) not in {(1, 0), (2, 2)}
                chosen = next((d for d in (2, 3, 4, 1) if d in ds), 0)
                counts[chosen] += 1
                if z in (3, 15):
                    normalized[z] += 1
                if not chosen:
                    assert ds == [0]*5
                    image = (target, tuple(sorted(permute(t, p) for t in triple)), permute(v, p))
                    assert image in {(3, (14, 22, 26), 1), (3, (13, 21, 25), 2)}
                    exceptions.append((z, triple, v))
    assert total == 8580 and normalized == {3: 728, 15: 260}
    # Each normalized cover itself has precisely the advertised two exceptions.
    canonical_exceptions = [x for x in exceptions if x[0] in (3, 15)]
    assert canonical_exceptions == [(3, (13, 21, 25), 2), (3, (14, 22, 26), 1)]
    return {'all_minority_second_vertices': 15, 'residual_rooted_geometries': total,
            'canonical_counts': dict(normalized), 'selected_delta_counts_all_z': dict(counts),
            'canonical_exceptions': canonical_exceptions,
            'noncanonical_exception_count': len(exceptions)}


def exceptional_cut_barrier():
    H = {0, 1, 3, 14, 22, 26}
    S = {x for x in V if (x >> 2).bit_count() <= 1}
    assert len(S) == 16 and H & S == {0, 1, 3} and len(S-H) == 13
    for j in (2, 3, 4):
        A = {x for x in V if not x & (1 << j)}
        assert A & H & {0, 3} == {0, 3}
        assert len(A & H & odd) == 2 and len((V-A) & H) == 2
        assert {1 << j, (1 << j)+3}.isdisjoint(H)
    # Allow every edge consistent with B-port restrictions, a relaxation of
    # all eight assignments of c_j=0 or c_j=2. If no edge leaves S even in
    # this relaxation, none can leave S under any actual bad-cut assignment.
    blocked = 0
    for x in S-H:
        for r in V-S-H:
            restrictive_coordinates = [j for j in (2, 3, 4)
                                       if (x ^ r) & (1 << j)]
            forbidden = False
            for j in restrictive_coordinates:
                b_endpoint = r if r & (1 << j) else x
                if b_endpoint not in {1 << j, (1 << j)+3}:
                    forbidden = True
            assert forbidden
            blocked += 1
    assert blocked == 169
    return {'barrier_vertices': sorted(S), 'holes_in_barrier': sorted(S & H),
            'covered_vertices_in_barrier': 13, 'forbidden_covered_boundary_pairs': blocked}


def imported_hashes():
    checked = {}
    for review in ('A6_FINITE_INPUTS_REVIEW.json', 'Q4_CORE_REVIEW.json',
                   'Q4_TWO_AVOIDED_REVIEW.json', 'CANONICAL_COMPLETION_REVIEW.json',
                   'EIGHT_HOLE_CONDITIONAL_REDUCTION_REVIEW.json'):
        obj = json.loads((ROOT/review).read_text(encoding='utf-8'))
        assert obj.get('status', obj.get('verdict')) == 'PASS'
        entries = dict(obj.get('audited_input_hashes', {}))
        if review == 'EIGHT_HOLE_CONDITIONAL_REDUCTION_REVIEW.json':
            entries.update(obj['imported_dependency_hashes'])
            entries.update(obj['checker_artifact_hashes'])
        entries.update(obj.get('source_sha256', {}))
        entries.update({x['file']: x['sha256'] for x in obj.get('files', [])})
        for name, expected in entries.items():
            got = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
            assert got == expected.removeprefix('sha256:'), (review, name)
            checked[name] = got
        checked[review] = hashlib.sha256((ROOT/review).read_bytes()).hexdigest()
    for name in ('A6_CLOSURE_DRAFT.md', 'Q4_GENERAL_AUGMENTATION.md',
                 'a6_closure_independent_check.py'):
        checked[name] = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    return checked


if __name__ == '__main__':
    report = {'status': 'PASS', 'geometry': geometry(),
              'exceptional_cut_barrier': exceptional_cut_barrier(),
              'checked_sha256': imported_hashes(),
              'scope': 'Geometry and hash integrity; semantic transfers separately audited',
              'full_p6_proved': False}
    (ROOT/'a6_closure_independent_check.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'checked_sha256'}))
