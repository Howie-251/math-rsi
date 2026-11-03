#!/usr/bin/env python3
"""Exact audit of the triple-repeat elimination for the N=62 problem.

This is a small direct-enumeration checker, not a SAT/SMT/MILP call.
It verifies the only finite tables used in the human argument:

1. A symmetric 4x4 nonnegative integer matrix N with zero diagonal and
   row sum 3 has, up to simultaneous permutation, exactly three forms.
2. In the last form N=J-I, all canonical 2-lifts L of the three C4
   type-blocks and all possible simple cubic Q satisfying the forced label
   marginals, Q∩L=∅, and LQ=QL are enumerated exhaustively.
3. The forced Gram matrix G=D^T D is feasible at the entry/row-sum level
   in exactly one labeled canonical case.
4. In that case every possible row support of D is enumerated.  There are
   24 candidates, but no six of them partition the 24 V-vertices.  The
   script also checks the short GF(2) certificate used in the written proof.

The mathematical derivation of these finite objects is separate from this
checker; this file only audits the small exhaustive tables.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations, product
from typing import Iterable

Label = tuple[int, int]
Vertex = tuple[Label, int]

LABELS: list[Label] = [(p, q) for p in range(4) for q in range(4) if p != q]
VERTICES: list[Vertex] = [(label, copy) for label in LABELS for copy in range(2)]
INDEX: dict[Vertex, int] = {vertex: i for i, vertex in enumerate(VERTICES)}
NV = len(VERTICES)


def canonical_matrix(matrix: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return min(
        tuple(tuple(matrix[p[i]][p[j]] for j in range(4)) for i in range(4))
        for p in permutations(range(4))
    )


def classify_n_matrices() -> list[tuple[tuple[int, ...], ...]]:
    """Classify symmetric zero-diagonal 4x4 matrices with row sum three."""
    orbits: set[tuple[tuple[int, ...], ...]] = set()
    # Six upper-triangular entries, each between 0 and 3.
    for values in product(range(4), repeat=6):
        matrix = [[0] * 4 for _ in range(4)]
        k = 0
        for i in range(4):
            for j in range(i + 1, 4):
                matrix[i][j] = matrix[j][i] = values[k]
                k += 1
        if all(sum(row) == 3 for row in matrix):
            orbits.add(canonical_matrix(tuple(tuple(row) for row in matrix)))
    result = sorted(orbits)
    assert len(result) == 3
    return result


def make_l(bits: tuple[int, int, int]) -> list[set[int]]:
    """Canonical 2-lift of each of the three complementary C4 type-blocks.

    In each block, three perfect matchings are gauged to the identity.  The
    fourth is identity (bit 0: two C4s) or swap (bit 1: one C8).  Thus all
    isomorphism types retaining the ordered labels are represented.
    """
    adjacency = [set() for _ in range(NV)]
    complementary_pairs = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    for bit, ((p, q), (r, s)) in zip(bits, complementary_pairs):
        a, b, c, d = (p, q), (q, p), (r, s), (s, r)
        for left, right, swap in ((a, c, 0), (a, d, 0), (b, c, 0), (b, d, bit)):
            for copy in range(2):
                other_copy = copy ^ swap
                i = INDEX[(left, copy)]
                j = INDEX[(right, other_copy)]
                adjacency[i].add(j)
                adjacency[j].add(i)
    assert all(len(row) == 2 for row in adjacency)
    return adjacency


def q_row_domains(l_adjacency: list[set[int]]) -> list[list[int]]:
    """All possible Q-neighborhood masks for each vertex.

    For z=(p,q), N=J-I forces its three Q-neighbors to have distinct first
    labels [4] minus {q} and distinct second labels [4] minus {p}.  Q is simple because
    each of those marginal totals is one.  Q and L are disjoint because a
    V-vertex lies in no triangle in the derived structure.
    """
    domains: list[list[int]] = []
    for i, ((p, q), _copy) in enumerate(VERTICES):
        candidates: list[int] = []
        for j, ((r, s), _other_copy) in enumerate(VERTICES):
            if i == j or j in l_adjacency[i]:
                continue
            if r == q or s == p:
                continue
            candidates.append(j)

        options: list[int] = []
        for neighbors in combinations(candidates, 3):
            first_labels = {VERTICES[j][0][0] for j in neighbors}
            second_labels = {VERTICES[j][0][1] for j in neighbors}
            if first_labels != set(range(4)) - {q}:
                continue
            if second_labels != set(range(4)) - {p}:
                continue
            options.append(sum(1 << j for j in neighbors))
        assert len(options) == 9
        domains.append(options)
    return domains


def matrices_commute(l_adjacency: list[set[int]], q_masks: list[int]) -> bool:
    for i in range(NV):
        for j in range(NV):
            lq = sum(1 for k in l_adjacency[i] if (q_masks[k] >> j) & 1)
            ql = sum(1 for k in l_adjacency[j] if (q_masks[i] >> k) & 1)
            if lq != ql:
                return False
    return True


def enumerate_q(l_adjacency: list[set[int]]) -> list[list[int]]:
    """Exhaustively assign one local neighborhood option to every Q row.

    Propagation enforces Q_ij=Q_ji in both directions.  No branch is dropped
    for any other reason.  Completed symmetric matrices are then checked for
    LQ=QL exactly.
    """
    initial = q_row_domains(l_adjacency)
    solutions: list[list[int]] = []

    def propagate(domains: list[list[int]], queue: list[int]) -> bool:
        processed: set[int] = set()
        while queue:
            i = queue.pop()
            if len(domains[i]) != 1 or i in processed:
                continue
            processed.add(i)
            mask = domains[i][0]
            for j in range(NV):
                if i == j:
                    continue
                required = (mask >> j) & 1
                filtered = [option for option in domains[j] if ((option >> i) & 1) == required]
                if not filtered:
                    return False
                if len(filtered) != len(domains[j]):
                    domains[j] = filtered
                    if len(filtered) == 1:
                        queue.append(j)
        return True

    def recurse(domains: list[list[int]]) -> None:
        if not propagate(domains, [i for i, domain in enumerate(domains) if len(domain) == 1]):
            return
        undecided = [(len(domain), i) for i, domain in enumerate(domains) if len(domain) > 1]
        if not undecided:
            masks = [domain[0] for domain in domains]
            if matrices_commute(l_adjacency, masks):
                solutions.append(masks)
            return
        _size, vertex = min(undecided)
        for option in domains[vertex]:
            child = [domain[:] for domain in domains]
            child[vertex] = [option]
            recurse(child)

    recurse(initial)
    return solutions


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(NV)) for j in range(NV)]
        for i in range(NV)
    ]


def forced_gram(l_adjacency: list[set[int]], q_masks: list[int]) -> list[list[int]]:
    """Compute G=D^T D from the exact V,V block equation."""
    l_matrix = [[int(j in l_adjacency[i]) for j in range(NV)] for i in range(NV)]
    q_matrix = [[(q_masks[i] >> j) & 1 for j in range(NV)] for i in range(NV)]
    l_squared = matmul(l_matrix, l_matrix)
    shared_e = [
        [
            int(VERTICES[i][0][0] == VERTICES[j][0][0])
            + int(VERTICES[i][0][1] == VERTICES[j][0][1])
            for j in range(NV)
        ]
        for i in range(NV)
    ]
    return [
        [
            1
            + q_matrix[i][j]
            + (7 if i == j else 0)
            - shared_e[i][j]
            - l_squared[i][j]
            - l_matrix[i][j]
            for j in range(NV)
        ]
        for i in range(NV)
    ]


def gram_passes_elementary_tests(gram: list[list[int]]) -> bool:
    values = [value for row in gram for value in row]
    return (
        all(gram[i][i] == 4 for i in range(NV))
        and min(values) >= 0
        and max(values) <= 4
        and all(sum(row) == 16 for row in gram)
    )


def candidate_d_rows(gram: list[list[int]]) -> list[tuple[int, ...]]:
    """Enumerate every possible support of one row of D.

    C D^T=J requires one V-vertex of each first label and each second label;
    hence the type pattern is a derangement.  Any pair in one support must
    have positive Gram entry.
    """
    blocks: set[tuple[int, ...]] = set()
    for permutation in permutations(range(4)):
        if any(permutation[p] == p for p in range(4)):
            continue
        for copies in product(range(2), repeat=4):
            block = tuple(
                sorted(INDEX[((p, permutation[p]), copies[p])] for p in range(4))
            )
            if all(gram[i][j] > 0 for i, j in combinations(block, 2)):
                blocks.add(block)
    return sorted(blocks)


def count_resolutions(blocks: list[tuple[int, ...]]) -> int:
    """Count partitions of the 24 vertices into six candidate D-row supports."""
    incidence: list[list[int]] = [[] for _ in range(NV)]
    masks: list[int] = []
    for block_index, block in enumerate(blocks):
        mask = sum(1 << vertex for vertex in block)
        masks.append(mask)
        for vertex in block:
            incidence[vertex].append(block_index)

    full = (1 << NV) - 1
    count = 0

    def recurse(covered: int) -> None:
        nonlocal count
        if covered == full:
            count += 1
            return
        uncovered = [v for v in range(NV) if not ((covered >> v) & 1)]
        vertex = min(
            uncovered,
            key=lambda v: sum(1 for block_index in incidence[v] if not (masks[block_index] & covered)),
        )
        for block_index in incidence[vertex]:
            if masks[block_index] & covered:
                continue
            recurse(covered | masks[block_index])

    recurse(0)
    return count


def verify_parity_certificate(blocks: list[tuple[int, ...]]) -> None:
    """Check the concise 0=1 XOR certificate for the no-resolution claim."""
    grouped: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
    for block in blocks:
        permutation = [0] * 4
        copy_bits = [0] * 4
        for vertex in block:
            (p, q), copy = VERTICES[vertex]
            permutation[p] = q
            copy_bits[p] = copy
        grouped[tuple(permutation)].add(tuple(copy_bits))

    cycles = {
        "A": (1, 2, 3, 0),  # 01,12,23,30
        "D": (2, 3, 1, 0),  # 02,13,21,30
        "E": (3, 0, 1, 2),  # 03,10,21,32
        "F": (3, 2, 0, 1),  # 03,12,20,31
    }
    # Each local equation below must hold for every allowed copy pattern.
    local_equations = {
        "A": ((1, 3), 1),
        "D": ((2, 3), 0),
        "E": ((0, 2), 1),
        "F": ((0, 1), 1),
    }
    for name, permutation in cycles.items():
        positions, rhs = local_equations[name]
        assert grouped[permutation]
        assert all((bits[positions[0]] ^ bits[positions[1]]) == rhs for bits in grouped[permutation])

    # In a resolution, the two blocks containing any ordered type must use
    # opposite copies.  The four cover equations used are 03,12,21,30.
    cover_equations = [
        (("E", 0), ("F", 0), 1),
        (("A", 1), ("F", 1), 1),
        (("D", 2), ("E", 2), 1),
        (("A", 3), ("D", 3), 1),
    ]

    # XOR the four local equations and the four cover equations.  Every
    # variable occurs exactly twice, while the right side is odd.
    variable_counts: defaultdict[tuple[str, int], int] = defaultdict(int)
    rhs_total = 0
    for name, (positions, rhs) in local_equations.items():
        variable_counts[(name, positions[0])] ^= 1
        variable_counts[(name, positions[1])] ^= 1
        rhs_total ^= rhs
    for left, right, rhs in cover_equations:
        variable_counts[left] ^= 1
        variable_counts[right] ^= 1
        rhs_total ^= rhs
    assert all(value == 0 for value in variable_counts.values())
    assert rhs_total == 1  # 0 = 1 contradiction.


def main() -> None:
    print("Symmetric zero-diagonal row-sum-3 N matrices, up to relabeling:")
    n_orbits = classify_n_matrices()
    for index, matrix in enumerate(n_orbits, start=1):
        print(f"N{index}:")
        for row in matrix:
            print(" ", row)

    print("\nN=J-I branch: exact L,Q and Gram counts")
    all_gram_survivors: list[tuple[tuple[int, int, int], list[int], list[list[int]]]] = []
    aggregate: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
    for bits in product(range(2), repeat=3):
        l_adjacency = make_l(bits)
        q_solutions = enumerate_q(l_adjacency)
        gram_solutions: list[tuple[list[int], list[list[int]]]] = []
        for q_masks in q_solutions:
            gram = forced_gram(l_adjacency, q_masks)
            if gram_passes_elementary_tests(gram):
                gram_solutions.append((q_masks, gram))
                all_gram_survivors.append((bits, q_masks, gram))
        k = sum(bits)
        aggregate[k].append((len(q_solutions), len(gram_solutions)))
        print(
            f"  L bits={bits} (C8 blocks={k}): "
            f"commuting Q={len(q_solutions)}, elementary Gram survivors={len(gram_solutions)}"
        )

    # Relabeling the four base labels makes bit strings with equal Hamming
    # weight equivalent, and their counts agree as an audit.
    assert aggregate[0] == [(13, 0)]
    assert set(aggregate[1]) == {(5, 0)}
    assert set(aggregate[2]) == {(1, 0)}
    assert aggregate[3] == [(1, 1)]
    assert len(all_gram_survivors) == 1

    bits, _q_masks, gram = all_gram_survivors[0]
    assert bits == (1, 1, 1)
    blocks = candidate_d_rows(gram)
    incidence_counts = [sum(vertex in block for block in blocks) for vertex in range(NV)]
    resolutions = count_resolutions(blocks)
    print("\nUnique elementary Gram survivor:")
    print(f"  candidate D-row supports={len(blocks)}")
    print(f"  support incidences per V-vertex={sorted(set(incidence_counts))}")
    print(f"  six-block resolutions={resolutions}")
    assert len(blocks) == 24
    assert set(incidence_counts) == {4}
    assert resolutions == 0
    verify_parity_certificate(blocks)
    print("  GF(2) certificate verified: XOR gives 0=1")
    print("\nAll triple-edge finite checks passed.")


if __name__ == "__main__":
    main()
