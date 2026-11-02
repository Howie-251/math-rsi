#!/usr/bin/env python3
"""Exhaustive small-field check of the selfadjoint nilpotent-square criterion.

This diagnoses finite-field linear algebra only: it generates no defect B or
61-vertex graphs.  The reference enumerates every symmetric matrix X over F_3;
the tested implementation computes primitive forms of C and a separate DP.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import time


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def zero(n):
    return tuple((0,) * n for _ in range(n))


def multiply(a, b, p):
    columns = tuple(zip(*b))
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) % p
                       for col in columns) for row in a)


def apply(a, v, p):
    return tuple(sum(x * y for x, y in zip(row, v)) % p for row in a)


def columns(vectors, n):
    return tuple(tuple(v[i] for v in vectors) for i in range(n))


def rref(rows, ncols, p):
    a = [list(row) for row in rows]
    pivots = []
    for col in range(ncols):
        pivot = next((i for i in range(len(pivots), len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        k = len(pivots)
        a[k], a[pivot] = a[pivot], a[k]
        inv = pow(a[k][col], -1, p)
        a[k] = [(x * inv) % p for x in a[k]]
        for i in range(len(a)):
            if i != k and a[i][col]:
                scale = a[i][col]
                a[i] = [(x - scale * y) % p for x, y in zip(a[i], a[k])]
        pivots.append(col)
    return a, pivots


def rank(rows, ncols, p):
    return len(rref(rows, ncols, p)[1])


def kernel(a, p):
    n = len(a)
    reduced, pivots = rref(a, n, p)
    basis = []
    for free in range(n):
        if free in pivots:
            continue
        v = [0] * n
        v[free] = 1
        for i, pivot in enumerate(pivots):
            v[pivot] = -reduced[i][free] % p
        basis.append(tuple(v))
    return basis


def independent_basis(vectors, n, p):
    basis = []
    for v in vectors:
        if rank(basis + [v], n, p) > len(basis):
            basis.append(v)
    return basis


def determinant(a, p):
    if not a:
        return 1
    a = [list(row) for row in a]
    d = 1
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            d = -d
        value = a[j][j]
        d = d * value % p
        inv = pow(value, -1, p)
        for i in range(j + 1, len(a)):
            scale = a[i][j] * inv % p
            a[i] = [(x - scale * y) % p for x, y in zip(a[i], a[j])]
    return d % p


def inverse(a, p):
    n = len(a)
    augmented = [list(row) + list(unit) for row, unit in zip(a, identity(n))]
    reduced, pivots = rref(augmented, n, p)
    if pivots != list(range(n)):
        raise AssertionError("Jordan chain vectors did not form a basis")
    return tuple(tuple(row[n:]) for row in reduced)


def square_class(value, p):
    if value % p == 0:
        raise AssertionError("primitive form is degenerate")
    return 1 if pow(value % p, (p - 1) // 2, p) == 1 else -1


def primitive_forms(c, p):
    """P_j=ker C^j/(ker C^(j-1)+C ker C^(j+1)), with standard inner product."""
    n = len(c)
    powers = [identity(n)]
    for _ in range(n + 1):
        powers.append(multiply(powers[-1], c, p))
    if powers[n] != zero(n):
        raise AssertionError("primitive criterion requires a nilpotent input")
    kernels = [kernel(a, p) for a in powers]
    ranks = [rank(a, n, p) for a in powers]
    forms = []
    representatives = {}
    for j in range(1, n + 1):
        denominator = independent_basis(
            kernels[j - 1] + [apply(c, v, p) for v in kernels[j + 1]], n, p)
        if any(apply(powers[j], v, p) != (0,) * n for v in denominator):
            raise AssertionError("primitive quotient denominator is outside kernel")
        combined = denominator[:]
        reps = []
        for v in kernels[j]:
            if rank(combined + [v], n, p) > len(combined):
                combined.append(v)
                reps.append(v)
        images = [apply(powers[j - 1], w, p) for w in reps]
        gram = tuple(tuple(sum(x * y for x, y in zip(v, image)) % p
                           for image in images) for v in reps)
        if gram != tuple(zip(*gram)):
            raise AssertionError("primitive form is not symmetric")
        dimension = ranks[j - 1] - 2 * ranks[j] + ranks[j + 1]
        if dimension != len(reps):
            raise AssertionError("quotient dimension and Jordan rank formula disagree")
        det = determinant(gram, p)
        forms.append({"length": j, "dimension": dimension,
                      "gram": gram, "determinant": det,
                      "square_class": square_class(det, p)})
        representatives[j] = reps
    return forms, representatives


def selfadjoint_square_dp(forms, p):
    """States are (dim Q_j, det-square-class Q_j), descending in j.

    q_j = H^a + Q_(j-1) + Q_j.  Q_0 is free at the final step;
    imposing Q_0=0 would incorrectly reject zero operators.
    """
    states = {(0, 1)}
    minus_class = square_class(p - 1, p)
    for form in reversed(forms):
        next_states = set()
        for dim_qj, disc_qj in states:
            remaining = form["dimension"] - dim_qj
            for a in range(remaining // 2 + 1):
                dim_prev = remaining - 2 * a
                disc_prev = form["square_class"] * (minus_class ** a) * disc_qj
                if dim_prev or disc_prev == 1:
                    next_states.add((dim_prev, disc_prev))
        states = next_states
    return bool(states)


def ordinary_square_plan(forms):
    """Dimension-only Jordan pairing, separately from the form-valued DP."""
    states = {0: {}}
    for form in reversed(forms):
        j = form["length"]
        next_states = {}
        for dim_qj, plan in states.items():
            remaining = form["dimension"] - dim_qj
            for a in range(remaining // 2 + 1):
                prev = remaining - 2 * a
                if prev not in next_states:
                    next_states[prev] = dict(plan, **{str(j): (a, prev)})
        states = next_states
    return next(iter(states.values())) if states else None


def ordinary_square_witness(c, reps, plan, p):
    """Interleave C-chains into a general (not necessarily symmetric) root."""
    n = len(c)
    buckets = {}
    for length, tops in reps.items():
        buckets[length] = []
        for top in tops:
            chain = [top]
            for _ in range(length - 1):
                chain.append(apply(c, chain[-1], p))
            buckets[length].append(chain)
    vectors, images = [], []

    def pair(long_chain, short_chain):
        for k, v in enumerate(long_chain):
            vectors.append(v)
            images.append(short_chain[k] if k < len(short_chain) else (0,) * n)
        for k, v in enumerate(short_chain):
            vectors.append(v)
            images.append(long_chain[k + 1] if k + 1 < len(long_chain) else (0,) * n)

    for j in range(n, 0, -1):
        equal_pairs, odd_pairs = plan[str(j)]
        for _ in range(equal_pairs):
            pair(buckets[j].pop(), buckets[j].pop())
        if j > 1:
            for _ in range(odd_pairs):
                pair(buckets[j].pop(), buckets[j - 1].pop())
        else:
            for _ in range(odd_pairs):
                pair(buckets[1].pop(), [])
    if any(buckets.values()) or len(vectors) != n:
        raise AssertionError("ordinary Jordan pairing did not consume every chain")
    x = multiply(columns(images, n), inverse(columns(vectors, n), p), p)
    if multiply(x, x, p) != c:
        raise AssertionError("constructed ordinary square root failed direct multiplication")
    return x


def symmetric_matrices(n, p):
    positions = [(i, j) for i in range(n) for j in range(i, n)]
    for entries in itertools.product(range(p), repeat=len(positions)):
        a = [[0] * n for _ in range(n)]
        for (i, j), value in zip(positions, entries):
            a[i][j] = a[j][i] = value
        yield tuple(map(tuple, a))


class BudgetExceeded(Exception):
    pass


class Budget:
    def __init__(self, seconds):
        self.started = time.monotonic()
        self.cpu_started = time.process_time()
        self.seconds = seconds

    def check(self):
        if time.monotonic() - self.started >= self.seconds:
            raise BudgetExceeded("internal wall-time budget reached")


def run_dimension(n, p, budget):
    wall_start, cpu_start = time.monotonic(), time.process_time()
    result = {"n": n, "p": p, "status": "RUNNING", "stage": "enumerate_reference",
              "symmetric_matrices_total": p ** (n * (n + 1) // 2),
              "symmetric_matrices_scanned": 0, "nilpotent_selfadjoint_count": 0,
              "distinct_selfadjoint_squares": 0, "criterion_inputs_checked": 0,
              "criterion_accept_count": 0, "ordinary_square_accept_count": 0,
              "ordinary_square_but_no_selfadjoint_count": 0,
              "mismatch_count": 0, "mismatch_examples": [], "negative_example": None}
    nilpotents = []
    actual_squares = set()
    try:
        for a in symmetric_matrices(n, p):
            result["symmetric_matrices_scanned"] += 1
            if result["symmetric_matrices_scanned"] % 256 == 0:
                budget.check()
            # Trace is a reference-side necessary filter, not the tested criterion.
            if sum(a[i][i] for i in range(n)) % p:
                continue
            power = a
            for _ in range(n - 1):
                power = multiply(power, a, p)
            if power != zero(n):
                continue
            nilpotents.append(a)
            actual_squares.add(multiply(a, a, p))
        result["nilpotent_selfadjoint_count"] = len(nilpotents)
        result["distinct_selfadjoint_squares"] = len(actual_squares)
        result["stage"] = "compare_primitive_criterion"
        for c in nilpotents:
            budget.check()
            forms, reps = primitive_forms(c, p)
            predicted = selfadjoint_square_dp(forms, p)
            actual = c in actual_squares
            plan = ordinary_square_plan(forms)
            ordinary = plan is not None
            result["criterion_inputs_checked"] += 1
            result["criterion_accept_count"] += int(predicted)
            result["ordinary_square_accept_count"] += int(ordinary)
            if predicted != actual:
                result["mismatch_count"] += 1
                if len(result["mismatch_examples"]) < 3:
                    result["mismatch_examples"].append(
                        {"C": c, "primitive_forms": forms,
                         "predicted": predicted, "direct_enumeration": actual})
            if ordinary and not actual:
                result["ordinary_square_but_no_selfadjoint_count"] += 1
                if result["negative_example"] is None:
                    x = ordinary_square_witness(c, reps, plan, p)
                    if x == tuple(zip(*x)):
                        raise AssertionError("negative example unexpectedly has a symmetric root")
                    result["negative_example"] = {
                        "C": c, "ordinary_square_root": x,
                        "square_verified_by_direct_multiplication": True,
                        "ordinary_root_is_symmetric": False,
                        "no_selfadjoint_root_by_exhaustive_reference": True,
                        "primitive_forms": [f for f in forms if f["dimension"]]}
        result["status"] = "PASS" if not result["mismatch_count"] else "MISMATCH"
        result["stage"] = "complete"
    except BudgetExceeded as exc:
        result["status"] = "LIMIT"
        result["limit_reason"] = str(exc)
        result["nilpotent_selfadjoint_count"] = len(nilpotents)
        result["distinct_selfadjoint_squares"] = len(actual_squares)
    result["wall_seconds"] = time.monotonic() - wall_start
    result["cpu_seconds"] = time.process_time() - cpu_start
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, choices=range(1, 5), default=4)
    parser.add_argument("--time-limit", type=float, default=60)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("odd_primary_square_check.result.json"))
    args = parser.parse_args()
    budget = Budget(args.time_limit)
    report = {
        "scope": "All symmetric matrices over F_3 with standard inner product, n=1..max_n; nilpotent inputs only",
        "not_a_graph_exclusion": True,
        "reference": "Enumerate every symmetric nilpotent X and collect X^2; compare every symmetric nilpotent C",
        "criterion": "Primitive quotient forms, descending dimension/discriminant DP with free Q_0",
        "max_n_requested": args.max_n,
        "wall_budget_seconds": args.time_limit,
        "dimensions": [],
        "status": "RUNNING"}

    def save():
        report["wall_seconds"] = time.monotonic() - budget.started
        report["cpu_seconds"] = time.process_time() - budget.cpu_started
        report["mismatch_count"] = sum(r["mismatch_count"] for r in report["dimensions"])
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    for n in range(1, args.max_n + 1):
        result = run_dimension(n, 3, budget)
        report["dimensions"].append(result)
        save()
        print(json.dumps({key: result[key] for key in (
            "n", "status", "symmetric_matrices_scanned", "nilpotent_selfadjoint_count",
            "criterion_inputs_checked", "criterion_accept_count", "mismatch_count",
            "ordinary_square_but_no_selfadjoint_count", "wall_seconds", "cpu_seconds")}), flush=True)
        if result["status"] != "PASS":
            report["status"] = result["status"]
            break
    else:
        report["status"] = "PASS"
    save()
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
