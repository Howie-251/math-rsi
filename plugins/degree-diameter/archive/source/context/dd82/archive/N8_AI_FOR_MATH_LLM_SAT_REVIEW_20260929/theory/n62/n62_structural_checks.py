#!/usr/bin/env python3
"""Exact finite checks supporting the theoretical N=62 reductions.

No SAT/SMT/MILP solver is used.  All searches are direct enumeration over
small integer matrices, followed by exact integer checks.

Checks performed:
  1. Classify all component-quotient matrices when the repeat multigraph B
     has exactly three connected components.
  2. Classify all component-quotient matrices when B has exactly five
     components and one component has order 2 (the triple-edge case).
  3. Classify the 4x4 symmetric nonnegative integer matrices N with row sum 3
     and diagonal at most 1 that occur in the forced 8-vertex block of the
     triple-edge reduction.
  4. Verify the forced five-cell quotient identity and characteristic
     polynomial.
"""

from __future__ import annotations

from itertools import permutations, product
from math import gcd
from typing import Iterable, Iterator, Sequence

try:
    import sympy as sp
except ImportError as exc:  # pragma: no cover
    raise SystemExit("This script needs sympy for the final characteristic-polynomial check.") from exc

Matrix = tuple[tuple[int, ...], ...]


def compositions(total: int, length: int) -> Iterator[tuple[int, ...]]:
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def partitions_k(total: int, length: int, minimum: int = 1) -> Iterator[tuple[int, ...]]:
    """Nondecreasing positive integer partitions of total into length parts."""
    if length == 0:
        if total == 0:
            yield ()
        return
    for first in range(minimum, total // length + 1):
        for tail in partitions_k(total - first, length - 1, first):
            yield (first,) + tail


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def quotient_identity_holds(r: Matrix, n_sizes: Sequence[int]) -> bool:
    """Check R^2 + R - 10 I = 1 n^T exactly."""
    r2 = matmul(r, r)
    c = len(r)
    for i in range(c):
        for j in range(c):
            lhs = r2[i][j] + r[i][j] - (10 if i == j else 0)
            if lhs != n_sizes[j]:
                return False
    return True


def canonical_pair(n_sizes: Sequence[int], r: Matrix) -> tuple[tuple[int, ...], Matrix]:
    """Canonicalize (component sizes, quotient) under simultaneous relabeling."""
    c = len(n_sizes)
    candidates: list[tuple[tuple[int, ...], Matrix]] = []
    for p in permutations(range(c)):
        np = tuple(n_sizes[p[i]] for i in range(c))
        rp = tuple(tuple(r[p[i]][p[j]] for j in range(c)) for i in range(c))
        candidates.append((np, rp))
    return min(candidates)


def enumerate_quotients_for_half_sizes(w: Sequence[int]) -> list[Matrix]:
    """Enumerate reversible integer quotients for n_i=2w_i.

    Balance n_i r_ij = n_j r_ji implies
      (r_ij, r_ji) = q (w_j/g, w_i/g),  g=gcd(w_i,w_j).
    The row sum is 8.  The trace is forced to 8-(c-1)/2.
    """
    c = len(w)
    pairs = [(i, j) for i in range(c) for j in range(i + 1, c)]
    pair_options: list[list[tuple[int, int]]] = []
    for i, j in pairs:
        g = gcd(w[i], w[j])
        base_ij = w[j] // g
        base_ji = w[i] // g
        q_max = min(8 // base_ij, 8 // base_ji)
        pair_options.append([(q * base_ij, q * base_ji) for q in range(q_max + 1)])

    # Smallest option sets first; this is only a speed improvement, not pruning.
    order = sorted(range(len(pairs)), key=lambda k: len(pair_options[k]))
    ordered_pairs = [pairs[k] for k in order]
    ordered_options = [pair_options[k] for k in order]

    cross_sum = [0] * c
    r_work = [[0] * c for _ in range(c)]
    solutions: list[Matrix] = []
    required_trace = 8 - (c - 1) // 2

    def recurse(position: int) -> None:
        if position == len(ordered_pairs):
            diagonal = [8 - cross_sum[i] for i in range(c)]
            if any(d < 0 or d > min(8, 2 * w[i] - 1) for i, d in enumerate(diagonal)):
                return
            if sum(diagonal) != required_trace:
                return
            for i, d in enumerate(diagonal):
                r_work[i][i] = d
            r = tuple(tuple(row) for row in r_work)
            n_sizes = tuple(2 * value for value in w)
            if quotient_identity_holds(r, n_sizes):
                solutions.append(r)
            return

        i, j = ordered_pairs[position]
        for rij, rji in ordered_options[position]:
            if cross_sum[i] + rij > 8 or cross_sum[j] + rji > 8:
                continue
            r_work[i][j] = rij
            r_work[j][i] = rji
            cross_sum[i] += rij
            cross_sum[j] += rji
            recurse(position + 1)
            cross_sum[i] -= rij
            cross_sum[j] -= rji
        r_work[i][j] = 0
        r_work[j][i] = 0

    recurse(0)
    return solutions


def classify_component_quotients() -> None:
    # Component orders are even and sum to 62, hence half-sizes sum to 31.
    for c, require_size_two in ((3, False), (5, True)):
        orbits: dict[tuple[tuple[int, ...], Matrix], None] = {}
        tested_partitions = 0
        for w in partitions_k(31, c):
            if require_size_two and w[0] != 1:
                continue
            tested_partitions += 1
            n_sizes = tuple(2 * value for value in w)
            for r in enumerate_quotients_for_half_sizes(w):
                orbits[canonical_pair(n_sizes, r)] = None

        label = f"c={c}" + (", with an order-2 component" if require_size_two else "")
        print(f"\n{label}: tested {tested_partitions} half-size partitions; {len(orbits)} orbit(s).")
        for n_sizes, r in sorted(orbits):
            print("sizes =", n_sizes)
            for row in r:
                print("  ", row)


def canonical_symmetric_n(n: Matrix) -> Matrix:
    candidates: list[Matrix] = []
    for p in permutations(range(4)):
        candidates.append(tuple(tuple(n[p[i]][p[j]] for j in range(4)) for i in range(4)))
    return min(candidates)


def classify_forced_eight_vertex_blocks() -> None:
    row_options = [row for row in compositions(3, 4)]
    orbits: dict[Matrix, None] = {}
    labeled_count = 0
    for rows in product(row_options, repeat=4):
        n = tuple(tuple(value for value in row) for row in rows)
        if any(n[i][i] > 1 for i in range(4)):
            continue
        if any(n[i][j] != n[j][i] for i in range(4) for j in range(4)):
            continue
        labeled_count += 1
        orbits[canonical_symmetric_n(n)] = None

    print(f"\nForced 4x4 N blocks: {labeled_count} labeled matrices; {len(orbits)} orbit(s).")
    for index, n in enumerate(sorted(orbits), start=1):
        print(f"N{index} =")
        for row in n:
            print("  ", row)


def verify_forced_five_cell_quotient() -> None:
    r = sp.Matrix(
        [
            [0, 4, 4, 0, 0],
            [2, 0, 0, 6, 0],
            [1, 0, 1, 0, 6],
            [0, 1, 0, 3, 4],
            [0, 0, 2, 4, 2],
        ]
    )
    n = sp.Matrix([[2, 4, 8, 24, 24]] * 5)
    identity_check = r * r + r - 10 * sp.eye(5)
    x = sp.symbols("x")
    characteristic = sp.factor(r.charpoly(x).as_expr())
    print("\nForced five-cell quotient R =")
    print(r)
    print("R^2 + R - 10 I =")
    print(identity_check)
    assert identity_check == n
    print("characteristic polynomial =", characteristic)
    assert characteristic == (x - 8) * (x**2 + x - 10) ** 2


def main() -> None:
    classify_component_quotients()
    classify_forced_eight_vertex_blocks()
    verify_forced_five_cell_quotient()
    print("\nAll exact checks passed.")


if __name__ == "__main__":
    main()
