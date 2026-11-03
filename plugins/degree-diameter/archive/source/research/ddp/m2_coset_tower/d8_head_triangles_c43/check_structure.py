"""Two specified cyclic triangle-head parameter tables; no S search or graphs."""
import json
import time
from math import comb
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent


def check_case(p, degree):
    r = 3
    k_order = p-1
    h_order = degree-1
    block_index = degree-2
    a_order = 3*p
    assert h_order*block_index == k_order
    powers = [pow(r, i, p) for i in range(k_order)]
    assert len(set(powers)) == k_order and pow(r, k_order, p) == 1
    U = sorted({powers[block_index*j] for j in range(h_order)})
    assert len(U) == h_order

    def encode(x, w, i):
        return x % p + p*(w % 3) + a_order*(i % k_order)

    def decode(g):
        return (g % a_order) % p, (g % a_order) // p, g // a_order

    def multiply(g, h):
        x, w, i = decode(g)
        y, v, j = decode(h)
        return encode(x+powers[i]*y, w+v, i+j)

    def inverse(g):
        x, w, i = decode(g)
        return encode(-powers[-i % k_order]*x, -w, -i)

    group_order = a_order*k_order
    for g in range(group_order):
        assert multiply(g, inverse(g)) == multiply(inverse(g), g) == 0
        x, w, i = decode(g)
        # Conjugation by the primitive scalar generates every K scaling.
        conjugator = encode(0, 0, 1)
        conjugated = multiply(multiply(conjugator, g), inverse(conjugator))
        assert conjugated == encode(r*x, w, i)
    G0 = [encode(x,0,i) for i in range(k_order) for x in range(p)]
    invols = [g for g in G0 if g and inverse(g) == g]
    pairs = [(g,inverse(g)) for g in G0 if g < inverse(g)]
    zero_invols = [g for g in invols if decode(g)[0] == 0]
    zero_pairs = [pair for pair in pairs if decode(pair[0])[0] == 0]
    assert len(invols) == p
    assert {decode(g)[2] for g in invols} == {k_order//2}
    assert len(pairs) == (p*k_order-1-p)//2
    assert len(zero_invols) == 1 and len(zero_pairs) == (k_order-2)//2

    cross_representatives = [encode(x,1,i) for i in range(k_order) for x in range(p)]
    assert all(decode(inverse(g))[1] == 2 for g in cross_representatives)
    assert len(set(map(inverse,cross_representatives))) == len(cross_representatives)
    cross_total = len(cross_representatives)
    cross_zero = k_order
    composition_rows = []
    no_internal_excluded = []
    for t in range(1, (degree-1)//2+1):
        internal_size = degree-1-2*t
        if internal_size == 0:
            no_internal_excluded.append(t)
            continue
        rows = []
        for invol_count in range(internal_size, -1, -2):
            pair_count = (internal_size-invol_count)//2
            total = comb(len(invols),invol_count)*comb(len(pairs),pair_count)
            all_zero = comb(len(zero_invols),invol_count)*comb(len(zero_pairs),pair_count)
            rows.append({'internal_involutions':invol_count, 'internal_inverse_pairs':pair_count,
                         'legal_internal_choices':total,
                         'all_zero_field_internal_choices':all_zero,
                         'HH_compatible_internal_choices':total-all_zero})
        cross_HH = comb(cross_total,t)-comb(cross_zero,t)
        internal_HH = sum(row['HH_compatible_internal_choices'] for row in rows)
        row = {'cross_inverse_pairs_t':t, 'internal_size':internal_size,
               'internal_compositions':rows,
               'HH_compatible_unordered_cross_pair_subsets':cross_HH,
               'HH_compatible_internal_choices':internal_HH,
               'raw_HH_component_sets':cross_HH*internal_HH}
        if t == 1:
            row['unique_nonzero_w1_anchor_normalized_x1_cross_choices'] = k_order
            row['t1_exact_normalized_component_sets'] = k_order*internal_HH
        composition_rows.append(row)

    unseen = set(range(1,p))
    h_orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {representative*u % p for u in U}
        assert len(orbit) == h_order and orbit <= unseen
        h_orbits.append(sorted(orbit))
        unseen -= orbit
    assert len(h_orbits) == block_index
    compressed_orbits = []
    for w in range(3):
        for field_orbit_index, field_members in enumerate([[0]]+h_orbits):
            compressed_orbits.append({
                'bit':w*(block_index+1)+field_orbit_index, 'w':w,
                'field_orbit_index':field_orbit_index,
                'A_members':[x+p*w for x in field_members], 'weight':len(field_members),
            })
    assert sum(o['weight'] for o in compressed_orbits) == a_order
    profile_strata = []
    for row in composition_rows:
        t = row['cross_inverse_pairs_t']
        for composition in row['internal_compositions']:
            inv_count = composition['internal_involutions']
            pair_count = composition['internal_inverse_pairs']
            for zero_inv in range(min(inv_count,1)+1):
                for zero_pair in range(pair_count+1):
                    if zero_inv == inv_count and zero_pair == pair_count:
                        continue
                    internal_choices = (comb(1,zero_inv)*comb(p-1,inv_count-zero_inv)
                                        *comb(len(zero_pairs),zero_pair)
                                        *comb(len(pairs)-len(zero_pairs),pair_count-zero_pair))
                    assert internal_choices > 0
                    for additional_cross_zero in range(t):
                        profile_strata.append({
                            't':t, 'internal_inverse_pairs':pair_count, 'internal_involutions':inv_count,
                            'internal_zero_field_pairs':zero_pair, 'internal_zero_field_involutions':zero_inv,
                            'additional_cross_zero_field_pairs':additional_cross_zero,
                            'additional_cross_nonzero_field_pairs':t-1-additional_cross_zero,
                            'internal_component_choice_count':internal_choices,
                        })
    assert len(profile_strata) == (24 if degree == 8 else 14)
    # An explicit algebraic witness against uniform division by |K| for t=2.
    # This is not a graph and is not a search: one written seven-element set for d8.
    scaling_caution = None
    if degree == 8:
        witness = {encode(1,1,0), encode(-1,1,0), encode(1,2,0), encode(-1,2,0),
                   encode(0,0,k_order//2), encode(1,0,k_order//2), encode(-1,0,k_order//2)}
        assert len(witness) == 7 and {inverse(g) for g in witness} == witness
        stabilizer = [scalar for scalar in range(1,p)
                      if {encode(scalar*decode(g)[0],decode(g)[1],decode(g)[2]) for g in witness} == witness]
        assert stabilizer == [1,p-1]
        scaling_caution = {'single_written_component_set_coordinates':sorted(map(decode,witness)),
                           'scalar_stabilizer':stabilizer,
                           'purpose':'t=2 HH-compatible example shows scaling action need not be free; no graph generated.'}
    leaf_count = a_order*k_order
    block_count = a_order*block_index
    n = leaf_count+block_count+a_order
    return {
        'p':p, 'degree':degree, 'primitive_root':r, 'primitive_powers':powers,
        'A_order':a_order, 'K_order':k_order, 'H_order':h_order, 'K_over_H_index':block_index,
        'H_scalar_elements':U, 'H_contains_minus_one':p-1 in U,
        'H_nonzero_field_orbits':h_orbits,
        'BB_compressed_orbits':compressed_orbits,
        'BB_compressed_bits_per_quotient_layer':len(compressed_orbits),
        'BB_quotient_layers':block_index,
        'BB_automatically_covered_zero_bits':[w*(block_index+1) for w in range(3)],
        'BB_missing_multiple':h_order,
        'group_order':group_order, 'G0_order':p*k_order,
        'G0_nonidentity_involutions':len(invols), 'G0_nonselfinverse_pairs':len(pairs),
        'G0_zero_field_involutions':len(zero_invols), 'G0_zero_field_inverse_pairs':len(zero_pairs),
        'G0_nonzero_field_involutions':len(invols)-len(zero_invols),
        'G0_nonzero_field_inverse_pairs':len(pairs)-len(zero_pairs),
        'G0_involution_exponent':k_order//2,
        'G0_involution_exponent_mod_block_index':(k_order//2)%block_index,
        'cross_inverse_pairs':cross_total, 'cross_nonzero_field_pairs':cross_total-cross_zero,
        'cross_zero_field_pairs':cross_zero,
        'layer_sizes':[leaf_count,block_count,a_order], 'n':n, 'edges':n*degree//2,
        'head_triangle_count':p, 'head_triangle_edges':3*p,
        'HH_criterion':'At least one nonzero-field cross-w inverse pair AND at least one nonzero-field internal element.',
        'legal_internal_compositions_and_counts':composition_rows,
        'HH_excluded_t_with_no_internal_elements':no_internal_excluded,
        't0_excluded_by_HH':True,
        't_greater_1_uniform_scalar_division_claimed':False,
        't2_scaling_nonfree_witness':scaling_caution,
        'profile_strata':profile_strata,
        'profile_strata_count':len(profile_strata),
        'profile_strata_counts_by_t':{t:sum(s['t']==t for s in profile_strata)
                                     for t in sorted({s['t'] for s in profile_strata})},
        'profile_strata_are_uniform_or_exhaustive_samples':False,
        'inverse_and_primitive_scalar_conjugation_checks':group_order,
    }


cases = [check_case(43,8), check_case(31,7)]
assert cases[0]['n'] == 6321 and cases[1]['n'] == 3348
result = {
    'status':'COMPLETE_TWO_SPECIFIED_PARAMETER_TABLES_NO_GRAPH_NO_BFS_NO_S_SEARCH',
    'coordinate_rule':'g=(x,w,i), encode=x+p*w+3*p*i',
    'group_product':'(x,w,i)(y,v,j)=(x+r^i*y modp,w+v mod3,i+j mod(p-1))',
    'group_inverse':'(-r^(-i)*x modp,-w mod3,-i mod(p-1))',
    'BB_formula':'For j=0..m-1: H_orbit(W3 horizontal coordinates with i_word modm=j) union H_orbit(S_horizontal) union H_orbit((r^(j-i_s)*x_s,w_s):s in W1) union {(0,1),(0,2)}; H multiplies field by U=<r^m> and fixes w.',
    'cases':cases,
    'cpu_seconds':time.process_time()-START,
    'scope':'Only p43,d8 and p31,d7; individual group inverses, scalar-conjugation and component counting. No graph expansion/BFS or candidate enumeration.',
}
(OUT/'STRUCTURE.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'cpu_seconds':result['cpu_seconds'],
                  'cases':[{k:c[k] for k in ['p','degree','primitive_root','layer_sizes','n','edges',
                                             'G0_nonidentity_involutions','G0_nonselfinverse_pairs',
                                             'cross_inverse_pairs','H_contains_minus_one',
                                             'legal_internal_compositions_and_counts']}
                           for c in cases]},indent=2))
