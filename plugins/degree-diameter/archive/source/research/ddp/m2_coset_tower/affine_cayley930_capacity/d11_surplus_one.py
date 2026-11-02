"""q+1-form moment condition on the 37 OPEN four-pair degree-11 modes.

No assignments or graph searches. For exactly q+1 distinct forms covering Fq,
their values are Fq plus y. Thus sum(L^2) - sum(L)^2 = 0 for q=31.
"""
import json
import time
from collections import Counter
from pathlib import Path

from D11_FOURPAIR_QUADRATIC import diagonalize, affine_word_forms
from d11_tight_linear import kernel

HERE = Path(__file__).resolve().parent
P = 31


def main():
    start = time.process_time()
    saved = json.loads((HERE / 'd11_tight_linear.survivors.json').read_text())
    selected = [row for row in saved if row['pair_count'] == 4]
    assert len(selected) == 37
    product = [[(i+j) % 30 for j in range(30)] for i in range(30)]
    inverse = [(-i) % 30 for i in range(30)]
    scalar = [pow(3, i, P) for i in range(30)]
    rows = []
    for source in selected:
        assert time.process_time() - start < 20
        components = [{'phase': j, 'kind': 'pair'} for j in source['pair_phases']]
        components += [{'phase': 15, 'kind': 'involution'} for _ in range(3)]
        symbolic = affine_word_forms(P, product, inverse, scalar, components)
        anchor = source['anchor_component']
        old_basis = source['nullspace_basis_after_anchor']
        forms = []
        for fiber in symbolic['forms']:
            anchored = {c[:anchor]+c[anchor+1:] for c in fiber}
            forms.append({tuple(sum(x*y for x,y in zip(c,b)) % P for b in old_basis)
                          for c in anchored})
        assert list(map(len, forms)) == source['restricted_form_counts']
        dimension = len(old_basis)
        quadratics, linear_rows = [], []
        for phase, fiber in enumerate(forms):
            if len(fiber) != P+1:
                continue
            coeffs = sorted(fiber)
            sums = [sum(c[i] for c in coeffs) % P for i in range(dimension)]
            Q = [[(sum(c[i]*c[j] for c in coeffs) - sums[i]*sums[j]) % P
                  for j in range(dimension)] for i in range(dimension)]
            diagonal, congruence = diagonalize(Q)
            rank = len(diagonal)
            character = (pow(-diagonal[0]*diagonal[1] % P, (P-1)//2, P)
                         if rank == 2 else None)
            forces_kernel = rank == 1 or (rank == 2 and character == P-1)
            if forces_kernel:
                linear_rows.extend(Q)
            quadratics.append({'phase': phase, 'forms': coeffs, 'coefficient_sum': sums,
                               'Q': Q, 'rank': rank, 'diagonal': diagonal,
                               'congruence_basis': congruence,
                               'rank2_negative_determinant_character': character,
                               'zero_forces_kernel': forces_kernel})
        _, pivots, restriction = kernel(linear_rows, dimension)
        restricted_forms = [{tuple(sum(x*y for x,y in zip(c,b)) % P for b in restriction)
                             for c in fiber} for fiber in forms]
        counts = list(map(len, restricted_forms))
        deficient = [j for j,count in enumerate(counts) if count < P]
        rows.append({'cursor': source['cursor'], 'pair_phases': source['pair_phases'],
                     'quadratics': quadratics, 'new_linear_rank': len(pivots),
                     'restriction_basis_in_prior_coordinates': restriction,
                     'restricted_counts': counts, 'deficient_phases': deficient,
                     'survives': not deficient})
    quads = [q for row in rows for q in row['quadratics']]
    result = {'status': 'COMPLETE_Q_PLUS_ONE_MOMENT_CHECK', 'input_modes': len(rows),
              'modes_with_32_form_fiber': sum(bool(row['quadratics']) for row in rows),
              'fibers_with_32_forms': len(quads),
              'rank_histogram': dict(sorted(Counter(q['rank'] for q in quads).items())),
              'modes_with_new_linear_constraints': sum(bool(row['new_linear_rank']) for row in rows),
              'modes_rejected': sum(not row['survives'] for row in rows),
              'modes_remaining': sum(row['survives'] for row in rows),
              'CPU_seconds': time.process_time()-start, 'CPU_budget_seconds': 20,
              'field_assignments': 0, 'graphs': 0, 'BFS_runs': 0, 'rows': rows}
    (HERE / 'd11_surplus_one.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'rows'}, indent=2))


if __name__ == '__main__':
    main()
