"""r2 source-supported cuts; no new mathematical assumptions or root search."""
from itertools import combinations
from sat59.enc.and_gate import add_simplified_clause as clause, negate
from sat59.enc.cardinality import unary_thresholds
from sat59.enc.structural_v6 import conjunction, pair


def forbid_n1(builder, adjacency, vertices, guard=True):
    """Weights (2,2,1,1); forbid either triangle with an isolated heavy end."""
    a, b, c, d = vertices
    for heavy, isolated in ((a, b), (b, a)):
        edges = {pair(heavy, c), pair(heavy, d), pair(c, d)}
        terms = [adjacency(u, v) if pair(u, v) in edges else negate(adjacency(u, v))
                 for u, v in combinations(vertices, 2)]
        clause(builder, negate(guard), *(negate(t) for t in terms))


def n2_overlap(builder, adjacency, vertices, ordinary, guard=True):
    """Both Q4 shapes retained; each shared ordinary vertex counts in each H."""
    a, *units = vertices
    overlaps = {}
    for j in units:
        overlaps[j] = [conjunction(builder, (adjacency(a, x), adjacency(j, x)),
                                   ('manual12r2_H', a, j, x)) for x in ordinary]
    for b in units:
        gate = conjunction(builder, (guard, adjacency(a, b)), ('manual12r2_N2_guard', a, b))
        for shared in overlaps[b]:
            clause(builder, negate(gate), negate(shared))
        other = [t for j in units if j != b for t in overlaps[j]]
        count = unary_thresholds(builder, other, 2, ('manual12r2_N2_sum', a, b))
        clause(builder, negate(gate), negate(count.ge(2)))
    return {str(j): terms for j, terms in overlaps.items()}


def exact_nonedge(builder, adjacency, entry, value, key):
    return conjunction(builder, (negate(adjacency), entry.ge_b(value),
                                 negate(entry.ge_b(value + 1))), ('manual12r2_R', key, value))


def zero_matching_row(builder, zero, others, adjacency, entries, key):
    """N15's exact R1/R2 row and support matching, conditional on t=0."""
    r = {j: {x: exact_nonedge(builder, adjacency(key, x), entries[pair(key, x)], j, (key, x))
             for x in others} for j in (1, 2)}
    for j in (1, 2):
        count = unary_thresholds(builder, r[j].values(), 3, ('manual12r2_row_count', key, j))
        clause(builder, negate(zero), count.ge(2))
        clause(builder, negate(zero), negate(count.ge(3)))
    for x in others:
        clause(builder, negate(zero), adjacency(key, x), negate(entries[pair(key, x)].ge_b(3)))
    for x, y in combinations(others, 2):
        for j in (1, 2):
            clause(builder, negate(zero), negate(r[j][x]), negate(r[j][y]), adjacency(x, y))
        clause(builder, negate(zero), negate(r[1][x]), negate(r[2][y]), negate(adjacency(x, y)))
        clause(builder, negate(zero), negate(r[2][x]), negate(r[1][y]), negate(adjacency(x, y)))
    return {f'R{j}': {str(x): t for x, t in terms.items()} for j, terms in r.items()}


def k4_nonextremal_row(builder, zero, one, ge2, ge4, key):
    count2 = unary_thresholds(builder, ge2, 2, ('manual12r2_S7_ge2', key))
    for b4 in ge4:
        clause(builder, negate(one), negate(b4))
        # With zero-row sum6 and cap4, B4 plus a second B>=2 is (4,2).
        clause(builder, negate(zero), negate(b4), negate(count2.ge(2)))


def k4_nonextremal_rows(encoder):
    e, b = encoder, encoder.builder
    for v in range(59):
        ge2 = [e.nonedge_tokens[pair(v, w)][1] for w in range(59) if w != v]
        ge4 = [e.nonedge_tokens[pair(v, w)][3] for w in range(59) if w != v]
        k4_nonextremal_row(b, e.is_t[v][0], e.is_t[v][1], ge2, ge4, v)


def add_r2(encoder):
    e, b = encoder, encoder.builder
    active = e.v6_case['constraint_sets']
    E, O = tuple(e.parent_spec.exceptional_vertices), tuple(e.parent_spec.ordinary_vertices)
    result = {}
    if 'R2-N1-SHAPE' in active:
        forbid_n1(b, e.a, E, e.moment.q2_selectors.get(5, False))
    if 'R2-N2-OVERLAP' in active:
        result['N2'] = n2_overlap(b, e.a, E, O, e.moment.q2_selectors[4])
    if 'R2-S7-K4-T1-NO-B4' in active:
        k4_nonextremal_rows(e)
    if 'R2-N15-ALL-ZERO-MATCHING' in active:
        result['zero_rows'] = {str(v): zero_matching_row(
            b, e.is_t[v][0], [w for w in range(59) if w != v], e.a, e.b_entries, v)
            for v in range(59)}
    return result
