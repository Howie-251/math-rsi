"""Exact, shared in-memory structural constraints for N59 V6."""

from itertools import combinations

from .and_gate import add_iff_and, add_simplified_clause as clause, assert_term, negate
from .cardinality import unary_thresholds, enforce_exactly, enforce_at_most
from .triangle_counts import add_iff_and3, encode_bounded_count


def pair(u, v):
    return (min(u, v), max(u, v))


def conjunction(b, terms, key):
    terms = tuple(terms)
    if any(t is False for t in terms):
        return False
    dynamic = tuple(dict.fromkeys(t for t in terms if t is not True))
    literals = set(dynamic)
    if any(-t in literals for t in dynamic):
        return False
    if not dynamic:
        return True
    if len(dynamic) == 1:
        return dynamic[0]
    out = b.var(("v6_and", key), "v6_and")
    for t in dynamic:
        clause(b, -out, t)
    clause(b, out, *(negate(t) for t in dynamic))
    return out


def disjunction(b, terms, key):
    return negate(conjunction(b, (negate(t) for t in terms), ("or", key)))


def eq_count(b, count, value, key):
    return conjunction(b, (count.ge(value), negate(count.ge(value + 1))), ("eq", key, value))


def exact_t_terms(encoder):
    return {v: [conjunction(encoder.builder, count.equals(t), ("t", v, t))
                for t in range(4)] for v, count in encoder.triangle_counts.items()}


def encode_triangles(encoder, vertices, *, lower, upper, fixed=None, second_layer=()):
    """Define triangles once, with the requested bound before construction."""
    b = encoder.builder
    incidence = {v: [] for v in vertices}
    encoder.d_triangle_terms = {}
    second_layer = set(second_layer)
    for u, v, w in combinations(vertices, 3):
        term = add_iff_and3(b, encoder.a(u, v), encoder.a(u, w), encoder.a(v, w),
                           ("v6_triangle", u, v, w), kind="graph_triangle")
        if term is False:
            continue
        for x in (u, v, w):
            incidence[x].append(term)
        if {u, v, w} <= second_layer:
            encoder.d_triangle_terms[u, v, w] = term
    encoder.triangle_terms = {v: tuple(terms) for v, terms in incidence.items()}
    encoder.triangle_counts = {
        v: encode_bounded_count(b, terms,
                lower=fixed[v] if fixed is not None else lower,
                upper=fixed[v] if fixed is not None else upper,
                key=("v6_triangle_count", v), kind="triangle_count")
        for v, terms in incidence.items()}


def pivot(out, name, term, definition, priority=0):
    if not isinstance(term, bool):
        out.append({"name": name, "literal": term, "definition": definition,
                    "priority": priority, "exact": True})


def add_m1_structure(encoder, *, K, latest=False, exact_n1=None, components=True):
    """All m1 rows, K3 matching, and K4 K2/P3/C3 with exact predicates."""
    b, vertices = encoder.builder, tuple(range(59))
    ts = encoder.is_t
    r1, r2, d2 = {}, {}, {}
    for u, v in combinations(vertices, 2):
        uv = (u, v)
        tokens = encoder.nonedge_tokens[uv]
        one, two = tokens[0], tokens[1] if len(tokens) > 1 else False
        r1[uv] = add_iff_and(b, one, negate(two), ("v6_R1", uv), kind="v6_R1")
        r2[uv] = two
        d2[uv] = add_iff_and(b, encoder.a(u, v), encoder.b_entries[uv].ge_b(2),
                            ("v6_D2", uv), kind="v6_D2")
        for x in uv:
            clause(b, negate(two), ts[x][1])
            clause(b, negate(d2[uv]), ts[x][2])
    counts2, k4 = {}, {}
    for v in vertices:
        edges = [pair(v, u) for u in vertices if u != v]
        if K == 3:
            enforce_exactly(b, [r1[e] for e in edges], 2, ("v6_R1_degree", v))
            count = unary_thresholds(b, [r2[e] for e in edges], 2, ("v6_R2_degree", v))
            assert_term(b, count.ge(2), False)
            clause(b, negate(count.ge(1)), ts[v][1])
            clause(b, count.ge(1), negate(ts[v][1]))
            enforce_at_most(b, [encoder.b_entries[e].ge_b(2) for e in edges], 1,
                            ("v6_all_B2_matching", v))
        else:
            count = unary_thresholds(b, [r2[e] for e in edges], 3, ("v6_R2_degree", v))
            count1 = unary_thresholds(b, [r1[e] for e in edges], 5, ("v6_R1_degree", v))
            rows = []
            for t, a, c in ((1, 0, 2), (1, 2, 1), (1, 4, 0), (2, 2, 0)):
                rows.append(conjunction(b, (ts[v][t], eq_count(b, count1, a, ("r1", v)),
                                            eq_count(b, count, c, ("r2", v))), ("row", v, t, a, c)))
            clause(b, *rows)
            k4[v] = rows[2]
            enforce_at_most(b, [d2[e] for e in edges], 1, ("v6_D2_matching", v))
        counts2[v] = count
    encoder.r1, encoder.r2, encoder.d2 = r1, r2, d2
    if K == 3:
        domain = [exact_n1] if exact_n1 is not None else ([16, 28] if latest else list(range(4, 59, 6)))
        count = unary_thresholds(b, [ts[v][1] for v in vertices], max(domain) + 1, "v6_n1")
        clause(b, *(eq_count(b, count, n, "n1") for n in domain))
        encoder.n1_domain = domain
    if K == 4 and components:
        add_k4_components(encoder, counts2, k4)


def add_k4_components(encoder, counts2, k4):
    b, r2, ts = encoder.builder, encoder.r2, encoder.is_t
    triangles = {}
    incident = {v: [] for v in range(59)}
    by_edge = {uv: [] for uv in combinations(range(59), 2)}
    for u, v, w in combinations(range(59), 3):
        term = add_iff_and3(b, r2[u, v], r2[u, w], r2[v, w],
                           ("v6_R2_triangle", u, v, w), kind="v6_R2_triangle")
        if term is False:
            continue
        triangles[u, v, w] = term
        for x in (u, v, w):
            incident[x].append(term)
        for edge in ((u, v), (u, w), (v, w)):
            by_edge[edge].append(term)
    # With maximum R2 degree two, an edge between two degree-two vertices
    # must lie in a triangle.  Exactly K2, P3, C3 can remain.
    for (u, v), term in r2.items():
        clause(b, negate(term), negate(counts2[u].ge(2)), negate(counts2[v].ge(2)),
               *by_edge[u, v])
    centers = {}
    for v in range(59):
        on_cycle = disjunction(b, incident[v], ("R2_on_C3", v))
        centers[v] = conjunction(b, (counts2[v].ge(2), negate(on_cycle)), ("P3_center", v))
        for w in range(59):
            if v == w:
                continue
            guard = (negate(centers[v]), negate(encoder.a(v, w)),
                     negate(encoder.b_entries[pair(v, w)].ge_b(1)))
            clause(b, *guard, ts[w][1])
            clause(b, *guard, k4[w])
    # Each R2 triangle indicator is exactly one C3 component. XOR parity
    # avoids a large counter over all triples.
    parity = False
    for index, term in enumerate(triangles.values()):
        both = conjunction(b, (parity, term), ("c3_parity_both", index))
        either = disjunction(b, (parity, term), ("c3_parity_either", index))
        parity = conjunction(b, (either, negate(both)), ("c3_parity", index))
    assert_term(b, parity, False)
    pivot(encoder.pivots, "R2_P3_exists", disjunction(b, centers.values(), "P3_exists"),
          {"kind": "R2_P3_exists"})
    pivot(encoder.pivots, "R2_C3_exists", disjunction(b, triangles.values(), "C3_exists"),
          {"kind": "R2_C3_exists"})


def add_m0_structure(encoder, K):
    b, ts = encoder.builder, encoder.is_t
    patterns = [(3, 0, 1), (2, 2, 0)]
    if K >= 5:
        patterns.append((4, 1, 0))
    if K >= 6:
        patterns.append((6, 0, 0))
    types = {}
    for u, v in combinations(range(59), 2):
        entry, a = encoder.b_entries[u, v], encoder.a(u, v)
        iso = conjunction(b, (a, negate(entry.ge_b(1))), ("t3_iso_edge", u, v))
        clause(b, negate(ts[u][3]), negate(iso), ts[v][0])
        clause(b, negate(ts[v][3]), negate(iso), ts[u][0])
        types[u, v] = [conjunction(b, (a, entry.ge_b(j), negate(entry.ge_b(j + 1))),
                                   ("t3_edge_type", u, v, j)) for j in (1, 2, 3)]
    for v in range(59):
        counts = [unary_thresholds(b, [types[pair(v, u)][j] for u in range(59) if u != v],
                      max(p[j] for p in patterns) + 1, ("t3_neighborhood", v, j)) for j in range(3)]
        selectors = [conjunction(b, [eq_count(b, counts[j], p[j], ("t3", v, j)) for j in range(3)],
                                 ("t3_pattern", v, p)) for p in patterns]
        clause(b, negate(ts[v][3]), *selectors)
    pivot(encoder.pivots, "t3_exists", disjunction(b, [ts[v][3] for v in range(59)], "t3_exists"),
          {"kind": "t3_exists"}, priority=1)


def mapping(encoder, *, labeling_mode, case, q2=None):
    """Complete pair map, including constants, for independent decoding."""
    cap = max(entry.max_b for entry in encoder.b_entries.values())
    return {"schema_version": "n59-structural-v6-map-1", "order": 59, "n": 59,
            "base_max_var": encoder.builder.variable_count, "semantics": "EXACT_A_B_TRIANGLE",
            "B_domain_max": cap,
            "encoding": "sat59-structural-v6", "case": case,
            "labeling_mode": labeling_mode, "evidence_mode": case["evidence_mode"],
            "A": {f"{u},{v}": encoder.a(u, v) for u, v in combinations(range(59), 2)},
            "B_ge": {f"{u},{v}": [entry.ge_b(j) for j in range(1, cap + 1)]
                     for (u, v), entry in encoder.b_entries.items()},
            "is_t": {str(v): terms for v, terms in encoder.is_t.items()},
            "top_variable": encoder.builder.variable_count,
            "structural_pivots": encoder.pivots,
            "q2_selectors": q2 or {}, "connectivity_complete": False,
            "omissions": ["explicit B-support connectivity (a relaxation)",
                          "latest Gram and all-root minimum-Q2 constraints"]}
