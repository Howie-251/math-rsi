"""Exact, scoped additions from N59_MANUAL12_ACTIVE r1.

No projected integer variables are independent of A/B.  This module only
compiles the supplied identities; it does not prove the source theorems.
"""
from itertools import combinations

from sat59.enc.and_gate import add_iff_and, add_simplified_clause as clause, negate
from sat59.enc.cardinality import unary_thresholds
from sat59.enc.structural_v6 import conjunction, disjunction, pair


def gated_sum(builder, selector, tokens, key):
    """Unary integer multiplication, not Boolean support multiplication."""
    return [add_iff_and(builder, selector, term, (key, j))
            for j, term in enumerate(tokens)]


def bounded_tokens(builder, terms, cap, key):
    count = unary_thresholds(builder, terms, cap + 1, key)
    clause(builder, negate(count.ge(cap + 1)))
    return [count.ge(j) for j in range(1, cap + 1)]


def equal_sums(builder, left, right, key, guard=True):
    """guard -> sum(left)=sum(right); preserve the complement and overflow.

    One side cannot exceed its number of input occurrences.  Comparing
    through min(lengths)+1 is therefore sufficient, including overflow.
    """
    left, right = list(left), list(right)
    maximum = min(len(left), len(right)) + 1
    lc = unary_thresholds(builder, left, maximum, (key, "left"))
    rc = unary_thresholds(builder, right, maximum, (key, "right"))
    for j in range(1, maximum + 1):
        clause(builder, negate(guard), negate(lc.ge(j)), rc.ge(j))
        clause(builder, negate(guard), lc.ge(j), negate(rc.ge(j)))


def triangle_guard(builder, exceptional_triangle_terms, dirty_children, t_zero, key):
    positive = disjunction(builder, exceptional_triangle_terms, (key, "a_positive"))
    ell = unary_thresholds(builder, dirty_children, 2, (key, "ell"))
    clause(builder, positive, ell.ge(2), t_zero)
    return {"a_positive": positive, "ell_ge1": ell.ge(1), "ell_ge2": ell.ge(2),
            "t_zero": t_zero}


def add_m0_triangle_guards(encoder):
    """M.1.  Existing V5 already enforces t=0 -> exact nonedge support <= K."""
    e, b = encoder, encoder.builder
    exceptions = tuple(e.parent_spec.exceptional_vertices)
    ordinary = tuple(e.parent_spec.ordinary_vertices)
    output = {}
    for p in range(1, 9):
        dirty = [conjunction(b, (e.a(p, x), negate(e.clean_terms[x])),
                             ("manual12_dirty_child", p, x)) for x in ordinary]
        exceptional_triangles = [
            conjunction(b, (e.a(p, i), e.a(p, j), e.a(i, j)),
                        ("manual12_parent_EE_triangle", p, i, j))
            for i, j in combinations(exceptions, 2)]
        exceptional_triangles += [
            conjunction(b, (e.a(p, i), e.a(p, x), e.a(i, x)),
                        ("manual12_parent_EO_triangle", p, i, x))
            for i in exceptions for x in ordinary]
        output[str(p)] = triangle_guard(b, exceptional_triangles, dirty,
                                       e.is_t[p][0], ("manual12_M1", p))
    return output


def add_m0_transport(encoder):
    """H38 A1/A2, all 8K+28 equations, exact selected A/B sums."""
    e, b = encoder, encoder.builder
    E = tuple(e.parent_spec.exceptional_vertices)
    O = tuple(e.parent_spec.ordinary_vertices)
    P = tuple(range(1, 9))
    weights = dict(zip(E, e.partition.defects))

    def b_tokens(u, v):
        return [e.b_entries[pair(u, v)].ge_b(j) for j in range(1, 5)]

    def count(terms, cap, key):
        return bounded_tokens(b, terms, cap, ("manual12_transport", key))

    def gate(s, terms, key):
        return gated_sum(b, s, terms, ("manual12_transport", key))

    f = {p: count([e.a(p, i) for i in E], len(E), ("f", p)) for p in P}
    N = {p: count([e.a(p, x) for x in O], 7, ("N", p)) for p in P}
    d = {i: [e.a(i, j) for j in E if j != i] for i in E}
    n, H, eps, z, Z = {}, {}, {}, {}, {}
    for p in P:
        for i in E:
            n[p, i] = count([add_iff_and(b, e.a(p, x), e.a(i, x),
                                        ("manual12_n", p, i, x)) for x in O],
                            7, ("n", p, i))
            eps[p, i] = count([t for x in O for t in
                               gate(e.a(p, x), b_tokens(i, x), ("eps", p, i, x))],
                              6, ("eps", p, i))
            z[p, i] = count([t for x in O for t in
                             gate(e.a(i, x), b_tokens(p, x), ("z", p, i, x))],
                            6, ("z", p, i))
        for q in P:
            if p != q:
                Z[p, q] = count([t for x in O for t in
                                 gate(e.a(q, x), b_tokens(p, x), ("Z", p, q, x))],
                                6, ("Z", p, q))
    for i, j in combinations(E, 2):
        H[i, j] = count([add_iff_and(b, e.a(i, x), e.a(j, x),
                                    ("manual12_H", i, j, x)) for x in O],
                        7, ("H", i, j))
    for p in P:
        for i in E:
            lhs = z[p, i] + [t for j in E if j != i for t in
                              gate(e.a(i, j), n[p, j], ("Fn", p, i, j))]
            rhs = eps[p, i] + [t for j in E if j != i for t in
                                gate(e.a(p, j), H[pair(i, j)], ("rhoH", p, i, j))]
            equal_sums(b, lhs, rhs, ("manual12_A1_member", p, i), e.a(p, i))
            equal_sums(b, lhs + f[p], [True] * weights[i] + d[i] + rhs,
                       ("manual12_A1_nonmember", p, i), negate(e.a(p, i)))
    for p, q in combinations(P, 2):
        lhs = N[p] + Z[q, p] + [t for i in E for t in
                                  gate(e.a(p, i), n[q, i], ("rho_n", p, q, i))]
        rhs = N[q] + Z[p, q] + [t for i in E for t in
                                  gate(e.a(q, i), n[p, i], ("rho_n", q, p, i))]
        equal_sums(b, lhs, rhs, ("manual12_A2", p, q))
    return {"A1_equations": 8 * len(E), "A2_equations": 28,
            "n": {f"{p},{i}": value for (p, i), value in n.items()},
            "H": {f"{i},{j}": value for (i, j), value in H.items()},
            "epsilon": {f"{p},{i}": value for (p, i), value in eps.items()},
            "z": {f"{p},{i}": value for (p, i), value in z.items()},
            "Z": {f"{p},{q}": value for (p, q), value in Z.items()}}
