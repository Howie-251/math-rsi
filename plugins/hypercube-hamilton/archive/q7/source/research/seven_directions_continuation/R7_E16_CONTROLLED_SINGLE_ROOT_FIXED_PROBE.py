"""Check the proposed controlled single-root gate on two frozen hole sets."""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from time import process_time

from R7_E16_ODD_22_WHOLE_FACE_PROBE import AXES, face, whole_face_gate


HERE = Path(__file__).resolve().parent
SOURCE = 'R7_E16_MU4_TWO_OBSTRUCTIONS_REALIZATION.json'
CPU_LIMIT = 10
IMPORTS = (
    SOURCE,
    'R7_TWO_RETURN_CONTROLLED_SINGLE_ROOT.md',
    'R7_DELTA2_ODD_SAME_SIDE_RECEIVERS.md',
    'R7_DELTA2_ODD_SAME_SIDE_RECEIVERS_REVIEW.json',
    'R7_E16_ODD_22_WHOLE_FACE_PROBE.py',
)


def receiver_gate(minority, majority, marks, outer):
    for inner in AXES:
        if inner == outer:
            continue
        for z_side in (0, 1):
            roots = face(minority, inner, z_side)
            p, q = len(roots), len(minority) - len(roots)
            z_major = len(face(majority, inner, z_side))
            t_major = len(majority) - z_major
            z_marks = len(face(marks, inner, z_side))
            if z_marks == 2 and p in (1, 2) and z_major == p + 3 and t_major == q + 1:
                kind = 'same_side'
            elif z_marks == 1 and p >= 1 and q in (0, 1) and z_major == p + 1 and t_major == q + 3:
                kind = 'separated'
            else:
                continue
            for a in roots:
                w = a ^ (1 << inner)
                if w not in marks:
                    return dict(kind=kind, inner=inner, Z_side=z_side, T_side=1 - z_side,
                                p=p, q=q, a=a, w=w, mark_counts=(z_marks, 2 - z_marks),
                                hole_counts=((p, z_major), (q, t_major)))
    return None


def find_plan(colors, counts, start):
    holes = set(colors[0] + colors[1])
    for outer in AXES:
        bit = 1 << outer
        for a_side in (0, 1):
            a_colors = [face(vertices, outer, a_side) for vertices in colors]
            if abs(len(a_colors[0]) - len(a_colors[1])) != 4:
                continue
            beta = int(len(a_colors[1]) > len(a_colors[0]))
            alpha = 1 - beta
            a_min, a_maj = a_colors[alpha], a_colors[beta]
            b_min = face(colors[beta], outer, 1 - a_side)
            b_maj = face(colors[alpha], outer, 1 - a_side)
            assert len(a_maj) - len(a_min) == len(b_maj) - len(b_min) == 4
            counts['directed_cuts_visited'] += 1
            for X in combinations(a_maj, 2):
                Y = tuple(sorted(x ^ bit for x in X))
                a_kept = tuple(x for x in a_maj if x not in X)
                for U in combinations(b_maj, 2):
                    if process_time() - start >= CPU_LIMIT:
                        raise TimeoutError
                    counts['source_choices_visited'] += 1
                    V = tuple(sorted(u ^ bit for u in U))
                    assert set(Y + V).isdisjoint(holes)
                    a_majority = tuple(sorted(a_kept + V))
                    supply = whole_face_gate(a_min, a_majority, V, outer)
                    if supply is None:
                        continue
                    counts['supplier_hits'] += 1
                    b_majority = tuple(sorted(tuple(x for x in b_maj if x not in U) + Y))
                    receive = receiver_gate(b_min, b_majority, Y, outer)
                    if receive is None:
                        continue
                    assert receive['a'] in b_min and receive['w'] not in holes
                    counts['both_hits'] += 1
                    return dict(outer=outer, A_side=a_side, B_side=1 - a_side,
                                alpha_parity=alpha, beta_parity=beta,
                                original_A_by_alpha_beta=(a_min, a_maj),
                                original_B_by_alpha_beta=(b_maj, b_min),
                                X=X, U=U, Y=Y, V=V,
                                H_prime_A=sorted(a_min + a_majority),
                                H_prime_B=sorted(b_min + b_majority),
                                H_prime_A_by_alpha_beta=(a_min, a_majority),
                                H_prime_B_by_alpha_beta=(b_majority, b_min),
                                supplier=supply, receiver=receive)
    return None


def run():
    start = process_time()
    source = json.loads((HERE / SOURCE).read_bytes())
    assert source['status'] == 'complete' and len(source['rows']) == 2
    rows = []
    status = 'complete'
    for item in source['rows']:
        assert item['certificate']['kind'] == 'perfect_short_matching'
        assert item['verification']['status'] == 'PASS'
        colors = tuple(tuple(sorted(item[field])) for field in ('even_holes', 'odd_holes'))
        for parity, holes in enumerate(colors):
            assert len(set(holes)) == 8 and all(x.bit_count() % 2 == parity for x in holes)
        assert all((x ^ y).bit_count() != 1 for x in colors[0] for y in colors[1])
        counts = Counter()
        try:
            plan = find_plan(colors, counts, start)
        except TimeoutError:
            status = 'cpu_limit'
            break
        rows.append(dict(obstruction=item['input'], even_holes=colors[0], odd_holes=colors[1],
                         status='first_legal_plan' if plan else 'no_plan', counters=dict(counts), plan=plan))
    elapsed = process_time() - start
    return dict(status=status, cpu_seconds=elapsed, cpu_limit_seconds=CPU_LIMIT, fixed_inputs=2,
                interface_status='AUTHOR_SUBMISSION_PENDING_INDEPENDENT_REVIEW',
                original_matching_enumerations=0, hamilton_solver_calls=0, rows=rows,
                input_hashes={name: sha256((HERE / name).read_bytes()).hexdigest() for name in IMPORTS})


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False))
