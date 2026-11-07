import itertools

# from lib.sat import SATInstance
from lib.sat_tseitin import SATInstance

def subsets(n, k):
    return itertools.combinations(list(range(n)), k)

def _or_all(terms):
    assert len(terms) > 0
    cur = terms[0]
    for t in terms[1:]:
        cur = cur | t
    return cur

def _require_int(name, value, minimum=None):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")


def add_no_n_gon(etvp, n, m, group=None):
    """Add the legacy global no-``n``-gon target layer.

    This helper deliberately uses the same Tseitin expression construction as
    the original inline loop.  In particular, each disjunction introduces the
    same auxiliary variable and clauses, so calling it from :func:`etv`
    preserves the historical CNF byte-for-byte.
    """
    _require_int("n", n, 2)
    _require_int("m", m, 0)
    if not hasattr(etvp, "cap") or not hasattr(etvp, "cup"):
        raise TypeError("etvp must expose cap and cup path dictionaries")

    cap = etvp.cap
    cup = etvp.cup
    clause_group = group or f"no_{n}_gon"
    with etvp.clause_group(clause_group):
        for i, j in subsets(m, 2):
            for d in range(2, n + 1):
                e = n + 2 - d
                if (i, j, d) in cap and (i, j, e) in cup:
                    etvp.add(~cap[(i, j, d)] | ~cup[(i, j, e)])
    return etvp


def add_no_gon(etvp, n, m, group=None):
    """Compatibility alias with the shorter target-layer name."""
    return add_no_n_gon(etvp, n, m, group=group)


def etv(n, a, b, m, flip_cup=True, include_no_gon=True):
    if not isinstance(include_no_gon, bool):
        raise TypeError("include_no_gon must be a boolean")
    etv = SATInstance()
    etv.set_metadata(problem={"n": n, "a": a, "b": b, "N": m, "flip_cup": flip_cup})
    red_path_group = f"no_red_{a}_path"
    blue_path_group = f"no_blue_{b}_path"
    v = {
        (i, j, k): etv.new_var(
            f"x_{i + 1}_{j + 1}_{k + 1}",
            role="triple",
            i=i + 1,
            j=j + 1,
            k=k + 1,
        )
        for i, j, k in subsets(m, 3)
    }

    cap = {}

    for i, j in subsets(m, 2):
        for d in range(2, min(a, j - i + 1) + 1):
            cap[(i, j, d)] = etv.new_var(f"cap({i},{j},{d})")

    with etv.clause_group(red_path_group):
        for i, j in subsets(m, 2):
            # any two points form a 2-cap
            etv.add(cap[(i, j, 2)])
            # no a-cap
            if j - i + 1 >= a:
                etv.add(~cap[(i, j, a)])
            # any d-cap induces (d-1)-cap
            for d in range(3, min(a, j - i + 1) + 1):
                etv.add_implies(cap[(i, j, d)], cap[(i, j, d - 1)])

    for i, j, k in subsets(m, 3):
        # 3-cap
        cap[(i, j, k, 3)] = ~v[(i, j, k)]
        for d in range(4, min(j - i + 2, a) + 1):
            cap[(i, j, k, d)] = etv.new_var(f"cap({i},{j},{k},{d})")

    with etv.clause_group(red_path_group):
        for i, j, k in subsets(m, 3):
            for d in range(3, min(j - i + 2, a) + 1):
                etv.add_implies(cap[(i, j, k, d)], cap[(i, k, d)])
                if d < a:
                    for l in range(k + 1, m):
                        # extending a d-cap
                        etv.add_implies(cap[(i, j, k, d)] & ~v[(j, k, l)], cap[(i, k, l, d + 1)])

    # reverse predecessor constraints for cap witnesses:
    # cap[(i,j,k,d)] means:
    #   there exists a d-cap from i to k whose penultimate point is j
    with etv.clause_group(red_path_group):
        for i, j, k in subsets(m, 3):
            for d in range(4, min(j - i + 2, a) + 1):
                terms = []
                for x in range(i + 1, j):
                    if (i, x, j, d - 1) in cap:
                        terms.append(cap[(i, x, j, d - 1)] & ~v[(x, j, k)])
                if not terms:
                    etv.add(~cap[(i, j, k, d)])
                else:
                    rhs = _or_all(terms)
                    etv.add_implies(cap[(i, j, k, d)], rhs)

    cup = {}

    for i, j in subsets(m, 2):
        for d in range(2, min(b, j - i + 1) + 1):
            cup[(i, j, d)] = etv.new_var(f"cup({i},{j},{d})")

    with etv.clause_group(blue_path_group):
        for i, j in subsets(m, 2):
            # any two points form a 2-cup
            etv.add(cup[(i, j, 2)])
            # no a-cup
            if j - i + 1 >= b:
                etv.add(~cup[(i, j, b)])
            # any d-cup induces (d-1)-cup
            for d in range(3, min(b, j - i + 1) + 1):
                etv.add_implies(cup[(i, j, d)], cup[(i, j, d - 1)])

    if flip_cup:
        for i, j, k in subsets(m, 3):
            # 3-cup
            cup[(i, j, k, 3)] = v[(i, j, k)]
            for d in range(4, min(k - j + 2, b) + 1):
                cup[(i, j, k, d)] = etv.new_var(f"cup({i},{j},{k},{d})")

        with etv.clause_group(blue_path_group):
            for i, j, k in subsets(m, 3):
                for d in range(3, min(k - j + 2, b) + 1):
                    etv.add_implies(cup[(i, j, k, d)], cup[(i, k, d)])
                    if d < b:
                        for l in range(i):
                            etv.add_implies(cup[(i, j, k, d)] & v[(l, i, j)], cup[(l, i, k, d + 1)])

        # reverse predecessor constraints for cup witnesses (flip_cup=True):
        # cup[(i,j,k,d)] means:
        #   there exists a d-cup from i to k whose second point is j
        with etv.clause_group(blue_path_group):
            for i, j, k in subsets(m, 3):
                for d in range(4, min(k - j + 2, b) + 1):
                    terms = []
                    for p in range(j + 1, k):
                        if (j, p, k, d - 1) in cup:
                            terms.append(cup[(j, p, k, d - 1)] & v[(i, j, p)])
                    if not terms:
                        etv.add(~cup[(i, j, k, d)])
                    else:
                        rhs = _or_all(terms)
                        etv.add_implies(cup[(i, j, k, d)], rhs)
    else:
        for i, j, k in subsets(m, 3):
            # 3-cup
            cup[(i, j, k, 3)] = v[(i, j, k)]
            for d in range(4, min(j - i + 2, b) + 1):
                cup[(i, j, k, d)] = etv.new_var(f"cup({i},{j},{k},{d})")

        with etv.clause_group(blue_path_group):
            for i, j, k in subsets(m, 3):
                for d in range(3, min(j - i + 2, b) + 1):
                    etv.add_implies(cup[(i, j, k, d)], cup[(i, k, d)])
                    if d < b:
                        for l in range(k + 1, m):
                            etv.add_implies(cup[(i, j, k, d)] & v[(j, k, l)], cup[(i, k, l, d + 1)])

        # reverse predecessor constraints for cup witnesses (flip_cup=False):
        # cup[(i,j,k,d)] means:
        #   there exists a d-cup from i to k whose penultimate point is j
        with etv.clause_group(blue_path_group):
            for i, j, k in subsets(m, 3):
                for d in range(4, min(j - i + 2, b) + 1):
                    terms = []
                    for x in range(i + 1, j):
                        if (i, x, j, d - 1) in cup:
                            terms.append(cup[(i, x, j, d - 1)] & v[(x, j, k)])
                    if not terms:
                        etv.add(~cup[(i, j, k, d)])
                    else:
                        rhs = _or_all(terms)
                        etv.add_implies(cup[(i, j, k, d)], rhs)

    with etv.clause_group(red_path_group):
        for i, j in subsets(m, 2):
            for d in range(3, min(a, j - i + 1) + 1):
                if (i, j, d) not in cap:
                    continue
                terms = []
                for k in range(i + 1, j):
                    if (i, k, j, d) in cap:
                        terms.append(cap[(i, k, j, d)])
                if not terms:
                    etv.add(~cap[(i, j, d)])
                else:
                    rhs = _or_all(terms)
                    etv.add_implies(cap[(i, j, d)], rhs)
                    etv.add_implies(rhs, cap[(i, j, d)])

    with etv.clause_group(blue_path_group):
        for i, j in subsets(m, 2):
            for d in range(3, min(b, j - i + 1) + 1):
                if (i, j, d) not in cup:
                    continue
                terms = []
                for k in range(i + 1, j):
                    if (i, k, j, d) in cup:
                        terms.append(cup[(i, k, j, d)])
                if not terms:
                    etv.add(~cup[(i, j, d)])
                else:
                    rhs = _or_all(terms)
                    etv.add_implies(cup[(i, j, d)], rhs)
                    etv.add_implies(rhs, cup[(i, j, d)])

    etv.v = v
    etv.cap = cap
    etv.cup = cup
    etv.include_no_gon = include_no_gon
    if include_no_gon:
        add_no_n_gon(etv, n, m)
    return etv

def add_signotope(etvp, m):
    """
    Add signotope constraints on quadruples (i,j,k,l).
    """
    v = etvp.v
    with etvp.clause_group("pseudolinear"):
        for i, j, k, l in subsets(m, 4):
            p = v[(i, j, k)]
            q = v[(i, j, l)]
            r = v[(i, k, l)]
            s = v[(j, k, l)]
            etvp.add_implies(p & s, q)
            etvp.add_implies(q & s, r)
            etvp.add_implies(p & r, q)
            etvp.add_implies(~p & ~s, ~q)
            etvp.add_implies(~q & ~s, ~r)
            etvp.add_implies(~p & ~r, ~q)
    return etvp

def etv_signotope(n, a, b, m):
    etvp = etv(n, a, b, m, flip_cup=True)
    etvp = add_signotope(etvp, m)
    return etvp


def etv_signotope_extension(n, a, b, m):
    """Build Query A: target-free path bounds plus signotope axioms.

    Prefix triples are fixed later through the normal assumption-file layer;
    this builder intentionally does not add the legacy global no-``n``-gon
    clauses or any endpoint-synchronization conjecture.
    """
    _validate_endpoint_query_parameters(n, a, b, m)
    etvp = etv(n, a, b, m, flip_cup=True, include_no_gon=False)
    etvp = add_signotope(etvp, m)
    etvp.set_metadata(
        endpoint_sync_encoding={
            "schema": "endpoint_sync_encoding_v1",
            "query": "A",
            "right_endpoint": m,
            "global_no_gon": False,
        }
    )
    return etvp


def _validate_endpoint_query_parameters(n, a, b, m):
    for name, value, minimum in (
        ("n", n, 2),
        ("a", a, 3),
        ("b", b, 3),
        ("m", m, 3),
    ):
        _require_int(name, value, minimum)
    cap_size = a - 1
    cup_size = b - 1
    if cap_size + cup_size != n + 2:
        raise ValueError(
            "endpoint synchronization requires (a - 1) + (b - 1) == n + 2"
        )
    # Orders below a path length are legitimate scaled/base cases: the
    # corresponding forbidden-path and endpoint families are simply empty.


def add_endpoint_desync(
    etvp,
    right_endpoint,
    cap_size,
    cup_size,
    group="endpoint_desync",
):
    """Forbid a cap/cup pair sharing both endpoints at one right endpoint.

    All point arguments are 0-based.  The clauses are emitted directly as
    binary CNF, so this layer adds no variables.  Missing path states are
    skipped, matching their quantified domain rather than approximating it
    with split-partition variables.
    """
    _require_int("right_endpoint", right_endpoint, 0)
    _require_int("cap_size", cap_size, 2)
    _require_int("cup_size", cup_size, 2)
    if not isinstance(group, str) or not group:
        raise ValueError("group must be a non-empty string")
    if not hasattr(etvp, "cap") or not hasattr(etvp, "cup"):
        raise TypeError("etvp must expose cap and cup path dictionaries")

    problem = getattr(etvp, "_metadata", {}).get("problem", {})
    order = problem.get("N")
    if order is not None and right_endpoint >= order:
        raise ValueError(
            f"right_endpoint {right_endpoint} is outside the 0-based order {order}"
        )
    if problem.get("a") is not None and cap_size > problem["a"]:
        raise ValueError("cap_size exceeds the encoded cap path bound")
    if problem.get("b") is not None and cup_size > problem["b"]:
        raise ValueError("cup_size exceeds the encoded cup path bound")

    before_vars = etvp._num_vars
    starts = []
    with etvp.clause_group(group):
        for start in range(right_endpoint):
            cap_key = (start, right_endpoint, cap_size)
            cup_key = (start, right_endpoint, cup_size)
            if cap_key not in etvp.cap or cup_key not in etvp.cup:
                continue
            etvp.add_clause(
                [-etvp.cap[cap_key]._lit, -etvp.cup[cup_key]._lit]
            )
            starts.append(start)

    if etvp._num_vars != before_vars:
        raise AssertionError("endpoint_desync must not introduce variables")

    metadata = {
        "schema": "endpoint_desync_v1",
        "right_endpoint": right_endpoint + 1,
        "cap_size": cap_size,
        "cup_size": cup_size,
        "start_points": [start + 1 for start in starts],
        "clause_count": len(starts),
        "clause_group": group,
    }
    etvp.endpoint_desync_starts = tuple(starts)
    etvp.endpoint_desync_metadata = metadata
    etvp.set_metadata(endpoint_desync=metadata)
    return etvp


def etv_signotope_extension_desync(n, a, b, m):
    """Build Query B as Query A plus the new-endpoint desync clauses."""
    _validate_endpoint_query_parameters(n, a, b, m)
    etvp = etv_signotope_extension(n, a, b, m)
    etvp = add_endpoint_desync(
        etvp,
        right_endpoint=m - 1,
        cap_size=a - 1,
        cup_size=b - 1,
    )
    endpoint_metadata = dict(etvp._metadata["endpoint_sync_encoding"])
    endpoint_metadata["query"] = "B"
    endpoint_metadata["endpoint_desync_clause_count"] = len(
        etvp.endpoint_desync_starts
    )
    etvp.set_metadata(endpoint_sync_encoding=endpoint_metadata)
    return etvp

def add_ax4(etvp, m):
    v = etvp.v
    for i, j, k, l in subsets(m, 4):
        p = v[(i, j, k)]
        q = v[(i, j, l)]
        r = v[(i, k, l)]
        s = v[(j, k, l)]
        etvp.add_implies(p & ~q & r, s)
        etvp.add_implies(~p & q & ~r, ~s)
    return etvp

def etv_ax4(n, a, b, m):
    etvp = etv(n, a, b, m, flip_cup=True)
    etvp = add_ax4(etvp, m)
    return etvp

def add_ax4_interior(etvp, m):
    v = etvp.v
    for i, j, k, l in subsets(m, 4):
        p = v[(i, j, k)]
        q = v[(i, j, l)]
        r = v[(i, k, l)]
        s = v[(j, k, l)]
        etvp.add_implies(p & r, q)
        etvp.add_implies(~p & ~r, ~q)
        etvp.add_implies(q & s, r)
        etvp.add_implies(~q & ~s, ~r)
    return etvp

def etv_ax4_interior(n, a, b, m):
    etvp = etv(n, a, b, m, flip_cup=True)
    etvp = add_ax4_interior(etvp, m)
    return etvp

def add_ax5(etvp, m):
    v = etvp.v
    for a, b, c, d, e in subsets(m, 5):
        pts = (a, b, c, d, e)
        lit = {}
        # ordered triple literal table on these 5 points
        for x, y, z in itertools.permutations(pts, 3):
            arr = [x, y, z]
            key = tuple(sorted(arr))
            inv = 0
            if arr[0] > arr[1]:
                inv += 1
            if arr[0] > arr[2]:
                inv += 1
            if arr[1] > arr[2]:
                inv += 1
            base = v[key]._lit
            lit[(x, y, z)] = base if (inv % 2 == 0) else -base
        seen = set()
        for t, s, p, q, r in itertools.permutations(pts, 5):
            # -------------------------------------------------
            # Knuth Axiom 5:
            # tsp & tsq & tsr & tpq & tqr -> tpr
            # -------------------------------------------------
            clause = (
                -lit[(t, s, p)],
                -lit[(t, s, q)],
                -lit[(t, s, r)],
                -lit[(t, p, q)],
                -lit[(t, q, r)],
                 lit[(t, p, r)],
            )
            clause_set = set(clause)
            if all(-x not in clause for x in clause):
                seen.add(tuple(sorted(clause_set)))
            # -------------------------------------------------
            # Dual Axiom 5:
            # stp & stq & str & tpq & tqr -> tpr
            # -------------------------------------------------
            clause = (
                -lit[(s, t, p)],
                -lit[(s, t, q)],
                -lit[(s, t, r)],
                -lit[(t, p, q)],
                -lit[(t, q, r)],
                 lit[(t, p, r)],
            )
            clause_set = set(clause)
            if all(-x not in clause for x in clause):
                seen.add(tuple(sorted(clause_set)))
        for clause in seen:
            etvp.add_clause(list(clause))
    return etvp
    
def etv_ax5(n, a, b, m):
    etvp = etv(n, a, b, m, flip_cup=True)
    etvp = add_ax5(etvp, m)
    return etvp

def add_knuth_redundant(etvp, m):
    """
    Redundant propagation strengthening from Axioms and Hulls:
      (1) interior transitivity
      (2) quadrilateral propagation
    """
    v = etvp.v
    for a, b, c, d, e in subsets(m, 5):
        pts = (a, b, c, d, e)

        lit = {}
        for x, y, z in itertools.permutations(pts, 3):
            arr = [x, y, z]
            key = tuple(sorted(arr))
            inv = 0
            if arr[0] > arr[1]:
                inv += 1
            if arr[0] > arr[2]:
                inv += 1
            if arr[1] > arr[2]:
                inv += 1
            base = v[key]._lit
            lit[(x, y, z)] = base if (inv % 2 == 0) else -base

        seen = set()

        for p, q, r, s, t in itertools.permutations(pts, 5):
            # -------------------------------------------------
            # Interior transitivity:
            # t in Apqr and s in Apqt  ->  s in Apqr
            #
            # tqr & ptr & pqt & sqt & pst & pqs -> sqr
            # tqr & ptr & pqt & sqt & pst & pqs -> psr
            # -------------------------------------------------
            clause = (
                -lit[(t, q, r)],
                -lit[(p, t, r)],
                -lit[(p, q, t)],
                -lit[(s, q, t)],
                -lit[(p, s, t)],
                -lit[(p, q, s)],
                 lit[(s, q, r)],
            )
            clause_set = set(clause)
            if not any(-x in clause_set for x in clause_set):
                seen.add(tuple(sorted(clause_set)))

            clause = (
                -lit[(t, q, r)],
                -lit[(p, t, r)],
                -lit[(p, q, t)],
                -lit[(s, q, t)],
                -lit[(p, s, t)],
                -lit[(p, q, s)],
                 lit[(p, s, r)],
            )
            clause_set = set(clause)
            if not any(-x in clause_set for x in clause_set):
                seen.add(tuple(sorted(clause_set)))

            # -------------------------------------------------
            # Quadrilateral propagation:
            # [pqrs] and t in Apqr -> [ptrs]
            #
            # pqr & qrs & rsp & spq & tqr & ptr & pqt -> trs
            # pqr & qrs & rsp & spq & tqr & ptr & pqt -> spt
            # -------------------------------------------------
            clause = (
                -lit[(p, q, r)],
                -lit[(q, r, s)],
                -lit[(r, s, p)],
                -lit[(s, p, q)],
                -lit[(t, q, r)],
                -lit[(p, t, r)],
                -lit[(p, q, t)],
                 lit[(t, r, s)],
            )
            clause_set = set(clause)
            if not any(-x in clause_set for x in clause_set):
                seen.add(tuple(sorted(clause_set)))

            clause = (
                -lit[(p, q, r)],
                -lit[(q, r, s)],
                -lit[(r, s, p)],
                -lit[(s, p, q)],
                -lit[(t, q, r)],
                -lit[(p, t, r)],
                -lit[(p, q, t)],
                 lit[(s, p, t)],
            )
            clause_set = set(clause)
            if not any(-x in clause_set for x in clause_set):
                seen.add(tuple(sorted(clause_set)))

        for clause in seen:
            etvp.add_clause(list(clause))

    return etvp

def add_knuth_all(etvp, m):
    etvp = add_ax5(etvp, m)
    etvp = add_knuth_redundant(etvp, m)
    return etvp

def add_semisimple(etvp, m):
    v = etvp.v
    for i, j, k, l in subsets(m, 4):
        p = v[(i, j, k)]
        q = v[(i, j, l)]
        r = v[(i, k, l)]
        s = v[(j, k, l)]
        etvp.add_implies(q & s, r)
        etvp.add_implies(p & r, q)
        etvp.add_implies(~q & ~s, ~r)
        etvp.add_implies(~p & ~r, ~q)
        etvp.add_implies(p & ~q & s, ~r)
        etvp.add_implies(p & ~r & s, ~q)
        etvp.add_implies(~p & q & ~s, r)
        etvp.add_implies(~p & r & ~s, q)
    return etvp

def etv_semisimple(n, a, b, m):
    etvp = etv(n, a, b, m, flip_cup=True)
    etvp = add_semisimple(etvp, m)
    return etvp

def add_split_gon(etvp, n, a, b, m):
    """
    Add existence of a split n-gon:
      exists right endpoint r and a feasible split type (d,e)
      such that there is a d-cap ending at r and an e-cup ending at r.

    Expose auxiliary variables for assumptions and reuse:
      split_cap_exists[(r,d)]
      split_cup_exists[(r,e)]
      split_pair[(r,d,e)]
      split_end[r]

    The split_cap_exists / split_cup_exists variables are not logically
    indispensable, but they keep the encoding modular: split_pair and
    split_end can reuse them, and assumption files may also pin them.
    """

    def feasible_split_types(n, a, b):
        """
        All split-(d,e)-types relevant to (n,a,b):
        d + e = n + 2
        2 <= d <= a-1
        2 <= e <= b-1
        """
        ans = []
        for d in range(2, a):
            e = n + 2 - d
            if 2 <= e < b:
                ans.append((d, e))
        return ans

    def feasible_types_for_r(types, r):
        """
        r is 0-based here, so an interval [i, r] has length at most r+1.
        A split-(d,e) type can end at r only if r+1 >= d and r+1 >= e.
        """
        return [(d, e) for (d, e) in types if r + 1 >= max(d, e)]

    cap = etvp.cap
    cup = etvp.cup

    types = feasible_split_types(n, a, b)
    if not types:
        etvp.add_clause([])
        return etvp

    split_cap_exists = {}
    split_cup_exists = {}
    split_pair = {}
    split_end = {}

    all_split_end_terms = []

    for r in range(m):
        types_r = feasible_types_for_r(types, r)
        d_values_r = sorted(set(d for d, _ in types_r))
        e_values_r = sorted(set(e for _, e in types_r))

        # cap-side ORs
        for d in d_values_r:
            var = etvp.new_var(f"split_cap_exists({r},{d})")
            split_cap_exists[(r, d)] = var
            cap_terms = [cap[(i, r, d)] for i in range(r) if (i, r, d) in cap]
            if not cap_terms:
                etvp.add(~var, group="split_partition")
            else:
                cap_exists = _or_all(cap_terms)
                etvp.add_implies(var, cap_exists, group="split_partition")
                etvp.add_implies(cap_exists, var, group="split_partition")

        # cup-side ORs
        for e in e_values_r:
            var = etvp.new_var(f"split_cup_exists({r},{e})")
            split_cup_exists[(r, e)] = var
            cup_terms = [cup[(i, r, e)] for i in range(r) if (i, r, e) in cup]
            if not cup_terms:
                etvp.add(~var, group="split_partition")
            else:
                cup_exists = _or_all(cup_terms)
                etvp.add_implies(var, cup_exists, group="split_partition")
                etvp.add_implies(cup_exists, var, group="split_partition")

        # pair vars
        pair_terms = []
        for d, e in types_r:
            var = etvp.new_var(f"split_pair({r},{d},{e})")
            split_pair[(r, d, e)] = var

            lhs = split_cap_exists[(r, d)] & split_cup_exists[(r, e)]
            etvp.add_implies(var, lhs, group="split_partition")
            etvp.add_implies(lhs, var, group="split_partition")

            pair_terms.append(var)

        # split_end[r]
        split_end[r] = etvp.new_var(f"split_end({r})")
        if not pair_terms:
            etvp.add(~split_end[r], group="split_partition")
        else:
            rhs = _or_all(pair_terms)
            etvp.add_implies(split_end[r], rhs, group="split_partition")
            etvp.add_implies(rhs, split_end[r], group="split_partition")
            all_split_end_terms.append(split_end[r])

    if not all_split_end_terms:
        etvp.add_clause([], group="split_partition")
    else:
        etvp.add(_or_all(all_split_end_terms), group="split_partition")

    etvp.split_cap_exists = split_cap_exists
    etvp.split_cup_exists = split_cup_exists
    etvp.split_pair = split_pair
    etvp.split_end = split_end
    return etvp

def etv_signotope_split(n, a, b, m):
    """
    signotope constraints + existence of split gon
    """
    etvp = etv_signotope(n, a, b, m)
    etvp = add_split_gon(etvp, n, a, b, m)
    return etvp

def etv_signotope_knuth(n, a, b, m):
    etvp = etv(n, a, b, m, flip_cup=True)
    etvp = add_signotope(etvp, m)
    etvp = add_ax5(etvp, m)
    # etvp = add_knuth_redundant(etvp, m)
    return etvp

def etv_signotope_knuth_split(n, a, b, m):
    etvp = etv_signotope_knuth(n, a, b, m)
    etvp = add_split_gon(etvp, n, a, b, m)
    return etvp

def etv_solution(n, a, b, m):
    etvp = etv(n, a, b, m, flip_cup=True)
    if etvp.solve():
        return {key: val.solution() for key, val in etvp.v.items()}
    else:
        return None
    
