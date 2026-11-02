#!/usr/bin/env python3
"""Exact lightweight audit for the N59 c1 high-Q2 reduction.

This program enumerates only graphs on the root-repeat support (at most six
vertices) and parent sets on the eight root neighbours.  It never enumerates
59-vertex graphs and does not call a SAT/SMT/MILP solver.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import comb

M0_PARTS = [
    (4, 2), (4, 1, 1), (3, 3), (3, 2, 1), (3, 1, 1, 1),
    (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1),
]
M1_PARTS = [(3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]


def edge_list(n: int):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def graph_from_mask(n: int, mask: int):
    adj = [set() for _ in range(n)]
    for bit, (i, j) in enumerate(edge_list(n)):
        if (mask >> bit) & 1:
            adj[i].add(j)
            adj[j].add(i)
    return adj


def triangles_at(adj, i: int) -> int:
    return sum(1 for a, b in combinations(adj[i], 2) if b in adj[a])


def has_k4(adj) -> bool:
    return any(
        all(v in adj[u] for u, v in combinations(S, 2))
        for S in combinations(range(len(adj)), 4)
    )


def common_count(adj, i: int, j: int) -> int:
    return len(adj[i] & adj[j])


def support_pair_lower(adj, i: int, j: int, m1: bool = False) -> int:
    """Lower bound for B_ij from common vertices already in the support.

    In m=1 the root itself is an additional common neighbour of the fixed
    adjacent pair a,b (vertices 0,1).
    """
    c = common_count(adj, i, j)
    if j in adj[i]:
        return c + (1 if m1 and {i, j} == {0, 1} else 0)
    return max(0, c - 1)


def canonical_edges(adj, weights, m1: bool = False):
    n = len(adj)
    groups = []
    start = 0
    if m1:
        groups.append((0, 1))
        start = 2
    by_weight = defaultdict(list)
    for i in range(start, n):
        by_weight[weights[i]].append(i)
    groups.extend(tuple(by_weight[w]) for w in sorted(by_weight, reverse=True))
    choices = [list(permutations(g)) for g in groups]
    original = [(i, j) for i in range(n) for j in range(i + 1, n) if j in adj[i]]
    best = None
    for picked in product(*choices):
        p = list(range(n))
        for group, image in zip(groups, picked):
            for old, new in zip(group, image):
                p[old] = new
        e = tuple(sorted((min(p[i], p[j]), max(p[i], p[j])) for i, j in original))
        best = e if best is None or e < best else best
    return best


def enumerate_m0_support(part):
    weights = list(part)
    n = len(weights)
    accepted = {}
    for mask in range(1 << len(edge_list(n))):
        adj = graph_from_mask(n, mask)
        if has_k4(adj):
            continue
        if any(triangles_at(adj, i) > (6 - weights[i]) // 2 for i in range(n)):
            continue
        weighted_degree = [sum(weights[j] for j in adj[i]) for i in range(n)]
        sigma = [6 - weights[i] - weighted_degree[i] for i in range(n)]
        if min(sigma) < 0:
            continue
        lower = {
            (i, j): support_pair_lower(adj, i, j)
            for i in range(n) for j in range(i + 1, n)
        }
        if any(
            sum(lower[min(i, j), max(i, j)] for j in range(n) if j != i) > sigma[i]
            for i in range(n)
        ):
            continue
        q2 = sum(weights[i] * weights[j] for i in range(n) for j in adj[i] if i < j)
        key = canonical_edges(adj, weights)
        accepted[q2, key] = (adj, tuple(sigma))
    return accepted


def enumerate_m1_support(part):
    weights = [1, 1, *part]
    n = len(weights)
    edges = edge_list(n)
    ab_bit = edges.index((0, 1))
    accepted = {}
    for mask in range(1 << len(edges)):
        if not ((mask >> ab_bit) & 1):
            continue
        adj = graph_from_mask(n, mask)
        if has_k4(adj):
            continue
        tri = [triangles_at(adj, i) for i in range(n)]
        if 1 + tri[0] > 3 or 1 + tri[1] > 3:
            continue
        if any(tri[i + 2] > (6 - part[i]) // 2 for i in range(len(part))):
            continue
        ell = [len(adj[i + 2] & {0, 1}) for i in range(len(part))]
        fdeg = [
            sum(part[j] for j in range(len(part)) if j + 2 in adj[i + 2])
            for i in range(len(part))
        ]
        sigma = [6 - part[i] - ell[i] - fdeg[i] for i in range(len(part))]
        if min(sigma) < 0:
            continue
        lower = {
            (i, j): support_pair_lower(adj, i, j, True)
            for i in range(n) for j in range(i + 1, n)
        }
        # Every support vertex already spends b_i units on its B-edge to the root.
        if any(
            weights[i] + sum(lower[min(i, j), max(i, j)] for j in range(n) if j != i) > 6
            for i in range(n)
        ):
            continue
        # The exact X-side residual of every exceptional vertex must cover the
        # forced B-interactions with the other exceptional vertices.
        for i in range(len(part)):
            ii = i + 2
            need = sum(lower[min(ii, j + 2), max(ii, j + 2)] for j in range(len(part)) if j != i)
            if need > sigma[i]:
                break
        else:
            q2 = sum(weights[i] * weights[j] for i in range(n) for j in adj[i] if i < j)
            key = canonical_edges(adj, weights, True)
            accepted[q2, key] = (adj, tuple(sigma))
    return accepted


def bpp_matrix(parent_sets, m: int):
    out = [[0] * 8 for _ in range(8)]
    for p in range(8):
        for q in range(p + 1, 8):
            h = int(m == 1 and {p, q} == {0, 1})
            rr = sum(int(p in S and q in S) for S in parent_sets)
            out[p][q] = out[q][p] = h + rr
    return out


def parent_subset_cuts(parent_sets, m: int) -> bool:
    for mask in range(1, 256):
        U = {p for p in range(8) if (mask >> p) & 1}
        lhs = sum(comb(len(S & U), 2) for S in parent_sets)
        lhs += int(m == 1 and {0, 1} <= U)
        if lhs > 3 * len(U) - 1:
            return False
    return True


def forced_parent_triangles(parent_sets, part, fadj, m: int) -> bool:
    # Exceptional vertices.
    for i, e in enumerate(part):
        forced = int(m == 1 and {0, 1} <= parent_sets[i])
        forced += sum(len(parent_sets[i] & parent_sets[j]) for j in fadj[i])
        forced += triangles_at(fadj, i)
        if forced > (6 - e) // 2:
            return False
    # Root-neighbour vertices.
    for p in range(8):
        forced = int(m == 1 and p in {0, 1})
        if m == 1 and p in {0, 1}:
            forced += sum(int({0, 1} <= S) for S in parent_sets)
        forced += sum(
            int(p in parent_sets[i] and p in parent_sets[j])
            for i in range(len(part)) for j in fadj[i] if i < j
        )
        if forced > 3:
            return False
    return True


def exception_pair_lowers(parent_sets, fadj):
    k = len(parent_sets)
    lower = {}
    for i in range(k):
        for j in range(i + 1, k):
            common = len(parent_sets[i] & parent_sets[j]) + len(fadj[i] & fadj[j])
            lower[i, j] = common if j in fadj[i] else max(0, common - 1)
    return lower


def lower_b_parent_exception(p, i, parent_sets, fadj, m: int) -> int:
    hr = 0
    if m == 1:
        if p == 0 and 1 in parent_sets[i]:
            hr = 1
        if p == 1 and 0 in parent_sets[i]:
            hr = 1
    r = int(p in parent_sets[i])
    known_rd = sum(int(p in parent_sets[j]) for j in fadj[i])
    return max(0, hr + r + known_rd - 1)


def parent_rows_fit(parent_sets, part, fadj, m: int) -> bool:
    bpp = bpp_matrix(parent_sets, m)
    for p in range(8):
        used = int(m == 1 and p in {0, 1})
        used += sum(bpp[p][q] for q in range(8) if q != p)
        used += sum(lower_b_parent_exception(p, i, parent_sets, fadj, m) for i in range(len(part)))
        if used > 6:
            return False
    return True


def parent_assignment_exists_m0(part, adj, sigma) -> bool:
    sizes = [e + 1 for e in part]
    # S_0 may be fixed by the full S_8 symmetry of the empty root neighbourhood.
    choices = [[frozenset(range(sizes[0]))]]
    choices += [[frozenset(c) for c in combinations(range(8), s)] for s in sizes[1:]]
    for parent_sets in product(*choices):
        parent_sets = list(parent_sets)
        if not forced_parent_triangles(parent_sets, part, adj, 0):
            continue
        lower = exception_pair_lowers(parent_sets, adj)
        if any(
            sum(lower[min(i, j), max(i, j)] for j in range(len(part)) if j != i) > sigma[i]
            for i in range(len(part))
        ):
            continue
        if not parent_rows_fit(parent_sets, part, adj, 0):
            continue
        if parent_subset_cuts(parent_sets, 0):
            return True
    return False


def parent_assignment_exists_m1(part, full_adj, sigma) -> bool:
    k = len(part)
    fadj = [set(j - 2 for j in full_adj[i + 2] if j >= 2) for i in range(k)]
    choices = []
    for i, e in enumerate(part):
        special = tuple(p for p in (0, 1) if i + 2 in full_adj[p])
        choices.append([
            frozenset((*special, *iso))
            for iso in combinations(range(2, 8), e + 1 - len(special))
        ])
    for parent_sets in product(*choices):
        parent_sets = list(parent_sets)
        if not forced_parent_triangles(parent_sets, part, fadj, 1):
            continue
        lower = exception_pair_lowers(parent_sets, fadj)
        if any(
            sum(lower[min(i, j), max(i, j)] for j in range(k) if j != i) > sigma[i]
            for i in range(k)
        ):
            continue
        if not parent_rows_fit(parent_sets, part, fadj, 1):
            continue
        if parent_subset_cuts(parent_sets, 1):
            return True
    return False


def main() -> None:
    print("N59 HIGH-Q2 ROOT-SUPPORT AUDIT")
    print("standard library only; no external solver; support order <= 6")
    print()

    m0_high = []
    for part in M0_PARTS:
        accepted = enumerate_m0_support(part)
        max_q = max(q for q, _ in accepted)
        feasible_high = []
        for (q, key), (adj, sigma) in accepted.items():
            if q >= 9 and parent_assignment_exists_m0(part, adj, sigma):
                feasible_high.append((q, key))
        print(f"m=0 {part}: support_max={max_q}; parent-feasible Q2>=9={sorted(feasible_high)}")
        m0_high.extend((part, q, key) for q, key in feasible_high)

    print()
    m1_high = []
    for part in M1_PARTS:
        accepted = enumerate_m1_support(part)
        max_q = max(q for q, _ in accepted)
        feasible_high = []
        for (q, key), (adj, sigma) in accepted.items():
            if q >= 9 and parent_assignment_exists_m1(part, adj, sigma):
                feasible_high.append((q, key))
        print(f"m=1 {part}: support_max={max_q}; parent-feasible Q2>=9={sorted(feasible_high)}")
        m1_high.extend((part, q, key) for q, key in feasible_high)

    expected_m0 = {
        ((3, 3), 9, ((0, 1),)),
        ((3, 2, 1), 9, ((0, 1), (0, 2))),
        ((3, 1, 1, 1), 9, ((0, 1), (0, 2), (0, 3))),
    }
    assert set(m0_high) == expected_m0, m0_high

    # The surviving m=1 support macros before the human fibre-charge lemma.
    assert max(q for _, q, _ in m1_high) == 10
    assert sum(q == 10 for _, q, _ in m1_high) == 1
    assert all(q in {9, 10} for _, q, _ in m1_high)

    print()
    print("AUDIT PASS")
    print("m=0: Q2<=9; Q2=9 has exactly the three displayed weighted support stars/edge.")
    print("m=1: Q2<=10 before the human fibre-charge exclusions; only Q2=9/10 macros remain.")


if __name__ == "__main__":
    main()
