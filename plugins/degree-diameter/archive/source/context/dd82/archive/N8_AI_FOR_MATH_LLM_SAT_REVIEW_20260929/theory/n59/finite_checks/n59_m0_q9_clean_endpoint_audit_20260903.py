#!/usr/bin/env python3
"""Finite audit of the final 4x4 clean-endpoint argument for N59.

This is the missing companion imported by
``n59_q2_le8_theorem_audit_20260903.py``.  It starts after Section 9 of
``N59_COARSE_THEORY_FORWARD_Q2_BOUND_20260903.md`` has reduced both excess
degree vectors to ``(1,1,1,0)``.  It enumerates every labelled 4x4 support
matrix K and every transportation matrix N satisfying (8.1)--(8.3), checks
the aggregate Delta feasibility conditions (8.5)--(8.6), and identifies the
applicable branch of the clean-endpoint contradiction in Section 10.

Only Python's standard library is used; no 59-vertex graph is generated.
"""

from __future__ import annotations

from itertools import combinations, permutations
from typing import Iterator, Sequence


Matrix = tuple[tuple[int, ...], ...]


def _row_sums(matrix: Sequence[Sequence[int]]) -> tuple[int, ...]:
    return tuple(sum(row) for row in matrix)


def _col_sums(matrix: Sequence[Sequence[int]]) -> tuple[int, ...]:
    return tuple(sum(matrix[i][j] for i in range(4)) for j in range(4))


def _permute_matrix(K: Matrix, rows: Sequence[int], cols: Sequence[int]) -> Matrix:
    return tuple(tuple(K[rows[i]][cols[j]] for j in range(4)) for i in range(4))


def _canonical_matrix(K: Matrix) -> Matrix:
    return min(
        _permute_matrix(K, rows, cols)
        for rows in permutations(range(4))
        for cols in permutations(range(4))
    )


def k_matrices() -> Iterator[Matrix]:
    """Yield row/column-permutation representatives after Section 9.

    The row and column degrees are both a permutation of ``(2,2,2,1)``;
    equivalently their excess vectors are permutations of ``(1,1,1,0)``.
    Independent row and column permutations preserve every condition checked
    below, so one lexicographically canonical representative per orbit is
    exhaustive.
    """

    positions = tuple((i, j) for i in range(4) for j in range(4))
    representatives: set[Matrix] = set()
    for chosen in combinations(positions, 7):
        chosen_set = set(chosen)
        matrix = tuple(
            tuple(int((i, j) in chosen_set) for j in range(4))
            for i in range(4)
        )
        if sorted(_row_sums(matrix)) != [1, 2, 2, 2]:
            continue
        if sorted(_col_sums(matrix)) != [1, 2, 2, 2]:
            continue
        representatives.add(_canonical_matrix(matrix))
    yield from sorted(representatives)


def _bounded_rows(total: int, lower: Sequence[int]) -> Iterator[tuple[int, ...]]:
    """Enumerate four nonnegative entries with fixed total and lower bounds."""

    remaining = total - sum(lower)
    if remaining < 0:
        return
    for a in range(remaining + 1):
        for b in range(remaining - a + 1):
            for c in range(remaining - a - b + 1):
                d = remaining - a - b - c
                yield (
                    lower[0] + a,
                    lower[1] + b,
                    lower[2] + c,
                    lower[3] + d,
                )


def _delta_transport_exists(K: Matrix, N: Matrix) -> bool:
    """Check (8.5)--(8.6) after alpha,beta are zero/one.

    Here Delta is a capacitated integral 4x4 transportation matrix.  A cell
    has capacity N[i][j] exactly when both corresponding excesses are one;
    otherwise its capacity is zero.
    """

    alpha = tuple(value - 1 for value in _row_sums(K))
    beta = tuple(value - 1 for value in _col_sums(K))
    row_need = tuple(4 * value for value in alpha)
    col_need = [4 * value for value in beta]

    def visit(row: int) -> bool:
        if row == 4:
            return all(value == 0 for value in col_need)
        target = row_need[row]
        capacities = tuple(
            N[row][j] if alpha[row] and beta[j] else 0 for j in range(4)
        )

        def distribute(col: int, remaining: int) -> bool:
            if col == 4:
                return remaining == 0 and visit(row + 1)
            upper = min(capacities[col], col_need[col], remaining)
            for value in range(upper + 1):
                col_need[col] -= value
                if distribute(col + 1, remaining - value):
                    col_need[col] += value
                    return True
                col_need[col] += value
            return False

        return distribute(0, target)

    return visit(0)


def n_matrices(K: Matrix) -> Iterator[Matrix]:
    """Yield every N satisfying (8.1)--(8.3) and Delta feasibility."""

    row_targets = tuple(7 - degree for degree in _row_sums(K))
    col_targets = tuple(7 - degree for degree in _col_sums(K))
    rows: list[tuple[int, ...]] = []
    remaining_cols = list(col_targets)

    def visit(i: int) -> Iterator[Matrix]:
        if i == 4:
            if any(remaining_cols):
                return
            matrix = tuple(rows)
            if _delta_transport_exists(K, matrix):
                yield matrix
            return

        lower = tuple(0 if K[i][j] else 1 for j in range(4))
        for row in _bounded_rows(row_targets[i], lower):
            if any(row[j] > remaining_cols[j] for j in range(4)):
                continue
            # Row half of (8.3).
            if sum(row[j] for j in range(4) if K[i][j]) > 3:
                continue
            rows.append(row)
            for j in range(4):
                remaining_cols[j] -= row[j]
            # Column half of (8.3), including a lower-bound feasibility test.
            if all(
                sum(rows[h][j] for h in range(i + 1) if K[h][j]) <= 3
                for j in range(4)
            ):
                yield from visit(i + 1)
            for j in range(4):
                remaining_cols[j] += row[j]
            rows.pop()

    yield from visit(0)


def rejection_reason(K: Matrix, N: Matrix) -> str:
    """Return the exact Section 10 branch that rejects ``(K,N)``.

    An empty result would signal that the proof interface has a survivor.
    """

    row_degrees = _row_sums(K)
    col_degrees = _col_sums(K)
    if sorted(row_degrees) != [1, 2, 2, 2] or sorted(col_degrees) != [1, 2, 2, 2]:
        return "outside_section9_reduction"
    if not _delta_transport_exists(K, N):
        return "delta_transport_infeasible"

    u0 = row_degrees.index(1)
    v0 = col_degrees.index(1)
    p = next(i for i in range(4) if K[i][v0])
    q = next(j for j in range(4) if K[u0][j])

    # Equations (10.1) and (10.2) are necessary clean-cover conditions.
    if N[p][v0] != 0 or N[u0][q] != 0:
        return "clean_same_colour_cell_nonempty"
    if K[u0][v0]:
        return "low_row_column_use_more_than_nine_delta0_vertices"

    n00 = N[u0][v0]
    if n00 < 3:
        return "too_many_delta0_vertices_in_low_row_column"
    if n00 > 4:
        return "low_column_nonedge_witness_capacity"
    if n00 == 3:
        return "forced_extra_high_high_delta0_vertex"

    # For n00=4, Section 10.4 fills the 2x2 endpoint block and forces at
    # least five points into (p,q).  Either status of K[p,q] contradicts a
    # previously encoded condition.
    if K[p][q]:
        return "edge_pq_has_at_least_five_triangles"
    return "nonedge_pq_has_no_witness"


def main() -> None:
    k_count = 0
    n_count = 0
    survivors = 0
    reasons: dict[str, int] = {}
    for K in k_matrices():
        k_count += 1
        for N in n_matrices(K):
            n_count += 1
            reason = rejection_reason(K, N)
            if not reason:
                survivors += 1
            else:
                reasons[reason] = reasons.get(reason, 0) + 1
    print("N59 M0 Q2=9 CLEAN-ENDPOINT AUDIT")
    print(f"K row/column-permutation orbits: {k_count}")
    print(f"transport-feasible (K,N) pairs: {n_count}")
    for reason in sorted(reasons):
        print(f"{reason}: {reasons[reason]}")
    print(f"survivors: {survivors}")
    if survivors:
        raise SystemExit(1)
    print("AUDIT PASS")


if __name__ == "__main__":
    main()
