"""Exact Boolean aliases and scoped consequences; no free role witnesses."""
from __future__ import annotations
from itertools import combinations
from sat59.enc.and_gate import add_iff_and, add_simplified_clause, negate
from sat59.enc.cardinality import unary_thresholds

PROFILES = {"32": (1, 1, 0), "311": (1, 0, 2), "221": (0, 2, 1),
            "2111": (0, 1, 3), "11111": (0, 0, 5)}  # c3,c2,c1


def iff_all(builder, terms, key):
    result = True
    for i, term in enumerate(terms):
        result = add_iff_and(builder, result, term, (key, i))
    return result


def require(builder, premises, conclusion, enabled=True):
    add_simplified_clause(builder, negate(enabled), *(negate(t) for t in premises), conclusion)


def exact_weights(builder, ge, key):
    # Baseline B<=3 is mandatory. The fourth threshold is not weight three.
    return (add_iff_and(builder, ge[0], negate(ge[1]), (key, "eq1")),
            add_iff_and(builder, ge[1], negate(ge[2]), (key, "eq2")), ge[2])


def row_profiles(builder, weights, key):
    # All outputs are equivalences; none is a solver-chosen profile witness.
    counters = [unary_thresholds(builder, [w[k] for w in weights], maximum, (key, k))
                for k, maximum in ((2, 2), (1, 3), (0, 6))]
    return {name: iff_all(builder,
                [t for counter, number in zip(counters, counts)
                 for t in (counter.ge(number), negate(counter.ge(number + 1)))], (key, name))
            for name, counts in PROFILES.items()}


def shared_only(builder, eq3, eq2, shared_eq1, enabled=True):
    require(builder, (eq3, eq2), shared_eq1, enabled)


def independent(builder, row_u, row_v, support, enabled=True):
    require(builder, (row_u, row_v), negate(support), enabled)


def tail_type(builder, row_u, eq2, row_x, enabled=True):
    require(builder, (row_u, eq2), row_x, enabled)


def endpoint_rule(builder, row_e, incidence, parallel_endpoint, enabled=True):
    require(builder, (row_e, incidence), negate(parallel_endpoint), enabled)


def mixed_partner(builder, row32, eq3, partner311, partner_triangle, enabled=True):
    require(builder, (row32, eq3), partner311, enabled)
    require(builder, (row32, eq3), negate(partner_triangle), enabled)


def no_triangle(builder, row_type, has_triangle, enabled=True):
    require(builder, (row_type,), negate(has_triangle), enabled)


def no_positive_A_partner(builder, row_type, b_support, a_edge, enabled=True):
    require(builder, (row_type, b_support), negate(a_edge), enabled)


def ratio(builder, left, right, multiplier, key, enabled=True, left_max=None):
    # Exact implication ladder, not a real-number relaxation.
    bound = len(left) if left_max is None else left_max
    l = unary_thresholds(builder, left, bound, (key, "left"))
    r = unary_thresholds(builder, right, multiplier * bound, (key, "right"))
    for k in range(1, bound + 1):
        require(builder, (l.ge(k),), r.ge(multiplier * k), enabled)


def packing_counts(builder, rows, components, *, q038=False, enabled=True):
    left = [r["32"] for r in rows.values()]
    total = unary_thresholds(builder, left, 8, "r13f_n32")
    require(builder, (), negate(total.ge(8)), enabled)
    ratio(builder, left, [r[name] for r in rows.values() for name in ("2111", "11111")],
          4, "r13f_four_to_one", enabled, left_max=7)
    if q038:
        for block, maximum in zip(components, (3, 4)):
            count = unary_thresholds(builder, [rows[v]["32"] for v in block], maximum + 1,
                                       ("r13f_block32", tuple(block)))
            require(builder, (), negate(count.ge(maximum + 1)), enabled)


def add_feedback(encoder, enabled):
    b = encoder.builder
    eq = {}
    for vertices in encoder.components:
        for u, v in combinations(vertices, 2):
            eq[u, v] = exact_weights(b, encoder.b_thresholds(u, v), ("r13f_B", u, v))
    rows = {u: row_profiles(b, [eq[encoder.pair(u, v)] for v in vertices if u != v], ("r13f_row", u))
            for vertices in encoder.components for u in vertices}
    encoder._record_stage("r13f_exact_B_and_row_aliases", encoder._r13f_before)
    left = [r["32"] for r in rows.values()]
    for module in enabled:
        before = b.clause_count
        if module == "R13F-32-SHARED-ONLY":
            for vertices in encoder.components:
                for u in vertices:
                    for v in vertices:
                        if u == v:
                            continue
                        for x in vertices:
                            if x != u and x != v:
                                shared_only(b, eq[encoder.pair(u, v)][2], eq[encoder.pair(u, x)][1],
                                            eq[encoder.pair(v, x)][0])
        elif module == "R13F-32-TAIL2111":
            for (u, x), weights in eq.items():
                tail_type(b, rows[u]["32"], weights[1], rows[x]["2111"])
                tail_type(b, rows[x]["32"], weights[1], rows[u]["2111"])
            ratio(b, left, [r["2111"] for r in rows.values()], 3, "r13f_three_to_one")
        elif module == "R13F-32-INDEPENDENT":
            for u, v in eq:
                independent(b, rows[u]["32"], rows[v]["32"], encoder.b_thresholds(u, v)[0])
            ratio(b, left, [r["311"] for r in rows.values()], 1, "r13f_n32_le_n311")
            ratio(b, left, [t for r in rows.values() for t in (r["221"], r["221"], r["2111"])],
                  1, "r13f_double_partner_capacity")
        elif module == "R13F-32-EIGHT-PACKING":
            packing_counts(b, rows, encoder.components, q038=encoder.job["job_id"] == "Q_C02_038")
        elif module == "R13F-32-MIXED":
            for u in rows:
                no_triangle(b, rows[u]["32"], encoder.r13_triangles[u][0])
            for (u, v), weights in eq.items():
                for a, partner in ((u, v), (v, u)):
                    mixed_partner(b, rows[a]["32"], weights[2], rows[partner]["311"], encoder.r13_triangles[partner][0])
        elif module == "R13F-221-TRANSLATION":
            for u in rows:
                no_triangle(b, rows[u]["221"], encoder.r13_triangles[u][0])
            for u, v in eq:
                for a in (u, v):
                    no_positive_A_partner(b, rows[a]["221"], encoder.b_thresholds(u, v)[0], encoder.edge_lit(u, v))
        elif module == "R13F-038-32-SIMPLE-ENDS":
            ds, es = encoder.components
            lam2 = {(r["u"], r["v"]): r["ge"][1] for r in encoder.auxiliary["lambda_weights"]}
            incident = {a: unary_thresholds(b, [lam2[encoder.pair(a, c)] for c in ds if c != a],
                         1, ("r13f_parallel_endpoint", a)).ge(1) for a in ds}
            for e in es:
                for a in ds:
                    endpoint_rule(b, rows[e]["32"], encoder.edge_lit(a, e), incident[a])
        else:
            raise ValueError(f"unknown R13F module: {module}")
        encoder._record_stage(module, before)
    return {"row_profiles": {str(u): r for u, r in rows.items()},
            "B_exact_weights": [{"u": u, "v": v, "eq1_eq2_eq3": w} for (u, v), w in eq.items()],
            "alias_preconditions": "Inherited exact B, B<=3, B row sum 5; cross-component B=0",
            "profile_order": "c3,c2,c1", "enabled_modules": list(enabled)}
