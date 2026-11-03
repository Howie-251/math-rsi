"""Only the 37 saved four-pair d11 patterns: tight-fiber quadratic forms.

No field assignments, graph construction, BFS, or five-pair pattern processing.
"""
import json
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'axis_cayley272'))
from symbolic_affine_words import affine_word_forms

P = 31

def bilinear(Q,u,v):
    return sum(u[i]*Q[i][j]*v[j] for i in range(len(u)) for j in range(len(v))) % P

def diagonalize(Q):
    """An explicit congruence basis; never evaluates candidate field vectors."""
    n = len(Q)
    remaining = [[int(i == j) for i in range(n)] for j in range(n)]
    basis,diagonal = [],[]
    while remaining:
        pivot = next((i for i,v in enumerate(remaining) if bilinear(Q,v,v)),None)
        if pivot is None:
            off = next(((i,j) for i in range(len(remaining))
                        for j in range(i+1,len(remaining))
                        if bilinear(Q,remaining[i],remaining[j])),None)
            if off is None:
                basis += remaining
                break
            i,j = off
            remaining[i] = [(a+b) % P for a,b in zip(remaining[i],remaining[j])]
            pivot = i
        v = remaining.pop(pivot)
        a = bilinear(Q,v,v)
        assert a
        for i,u in enumerate(remaining):
            factor = bilinear(Q,v,u)*pow(a,-1,P) % P
            remaining[i] = [(x-factor*y) % P for x,y in zip(u,v)]
        basis.append(v)
        diagonal.append(a)
    rank = len(diagonal)
    assert len(basis) == n
    for i,u in enumerate(basis):
        for j,v in enumerate(basis):
            assert bilinear(Q,u,v) == (diagonal[i] if i == j and i < rank else 0)
    return diagonal,basis

def main():
    start = time.process_time()
    source = json.loads((HERE/'d11_tight_linear.survivors.json').read_text())
    selected = [r for r in source if r['pair_count'] == 4]
    assert len(selected) == 37
    multiplication = [[(i+j) % 30 for j in range(30)] for i in range(30)]
    inverse = [(-i) % 30 for i in range(30)]
    scalar = [pow(3,i,P) for i in range(30)]
    rows = []
    for saved in selected:
        assert time.process_time()-start < 20
        tight = [j for j,n in enumerate(saved['restricted_form_counts']) if n == P]
        row = {'cursor':saved['cursor'],'pair_phases':saved['pair_phases'],
               'involution_count':saved['involution_count'],
               'anchor_component':saved['anchor_component'],
               'prior_linear_rank':saved['rank_mod31'],
               'prior_nullspace_basis':saved['nullspace_basis_after_anchor'],
               'prior_nullspace_dimension':saved['nullspace_dimension'],
               'tight_phases_in_saved_nullspace':tight,'quadratics':[]}
        if not tight:
            rows.append(row)
            continue
        components = [{'phase':j,'kind':'pair'} for j in saved['pair_phases']]
        components += [{'phase':15,'kind':'involution'} for _ in range(3)]
        symbolic = affine_word_forms(P,multiplication,inverse,scalar,components)
        assert symbolic['form_counts'] == saved['symbolic_capacity']
        anchor = saved['anchor_component']
        basis = saved['nullspace_basis_after_anchor']
        after_anchor = [{c[:anchor]+c[anchor+1:] for c in forms}
                        for forms in symbolic['forms']]
        restricted = [{tuple(sum(x*y for x,y in zip(c,b)) % P for b in basis)
                       for c in forms} for forms in after_anchor]
        assert list(map(len,restricted)) == saved['restricted_form_counts']
        d = len(basis)
        for phase in tight:
            forms = sorted(restricted[phase])
            assert len(forms) == P
            Q = [[sum(c[i]*c[j] for c in forms) % P for j in range(d)] for i in range(d)]
            diagonal,congruence = diagonalize(Q)
            rank = len(diagonal)
            minus_det = -diagonal[0]*diagonal[1] % P if rank == 2 else None
            character = pow(minus_det,(P-1)//2,P) if rank == 2 else None
            anisotropic = character == P-1 if rank == 2 else None
            force_kernel = rank == 1 or (rank == 2 and anisotropic)
            row['quadratics'].append({'phase':phase,'coefficient_forms':forms,'Q':Q,
                'rank':rank,'nonzero_congruence_diagonal':diagonal,
                'congruence_basis_vectors':congruence,
                'rank2_negative_determinant':minus_det,
                'rank2_negative_determinant_Legendre_mod31':character,
                'rank2_nondegenerate_part_anisotropic':anisotropic,
                'zero_forces_Q_times_z_zero':force_kernel,
                'forced_linear_rows':Q if force_kernel else []})
        rows.append(row)
    quadratics = [q for r in rows for q in r['quadratics']]
    result = {'status':'COMPLETE_FOURPAIR_TIGHT_QUADRATIC_RANK_DIAGNOSIS',
        'input_patterns':37,'patterns_with_tight31_fibers':sum(bool(r['quadratics']) for r in rows),
        'tight_fibers':len(quadratics),
        'quadratic_rank_histogram':dict(sorted(Counter(q['rank'] for q in quadratics).items())),
        'rank1_fibers':sum(q['rank'] == 1 for q in quadratics),
        'rank2_anisotropic_fibers':sum(q['rank'] == 2 and q['rank2_nondegenerate_part_anisotropic'] for q in quadratics),
        'rank2_isotropic_fibers':sum(q['rank'] == 2 and not q['rank2_nondegenerate_part_anisotropic'] for q in quadratics),
        'patterns_with_forced_linear_rows':sum(any(q['zero_forces_Q_times_z_zero'] for q in r['quadratics']) for r in rows),
        'CPU_seconds':time.process_time()-start,'CPU_budget_seconds':20,
        'field_assignments_tested':0,'graphs_generated':0,'BFS_runs':0,
        'five_pair_patterns_processed':0,'rows':rows}
    (HERE/'D11_FOURPAIR_QUADRATIC.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'rows'},indent=2))
    for row in rows:
        if row['quadratics']:
            print(json.dumps({'cursor':row['cursor'],'pair_phases':row['pair_phases'],
                'quadratics':[{k:q[k] for k in ['phase','Q','rank','nonzero_congruence_diagonal',
                    'rank2_nondegenerate_part_anisotropic','zero_forces_Q_times_z_zero']}
                    for q in row['quadratics']]}))

if __name__ == '__main__':
    main()
