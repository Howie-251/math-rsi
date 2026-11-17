"""Independent arithmetic and bounded feasibility replay for normalized even supports."""
from collections import Counter
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import time

import ortools
from ortools.sat.python import cp_model

HERE = Path(__file__).resolve().parent
DIM = 7
AXES = range(DIM)
BITS = (0, 1)
SECONDS = 112
BASE = (3, 6, 5, 2)


def donor_ok(r, minority, gap):
    other_minor = r - minority
    other_major = r + 4 - minority - gap
    if min(other_minor, other_major) < 0:
        return False
    if minority in (0, 1):
        if gap == 4:
            return other_minor == other_major >= 1
        if gap == 5:
            return 1 <= other_minor <= 16 and other_major == other_minor - 1
        if gap == 6:
            return other_minor in (2, 3) and other_major == other_minor - 2
    return (minority, gap) in {(2, 3), (1, 3)}


def gate_reasons(cells, donor_bit):
    """cells[outer bit][inner bit][physical color]."""
    A, B = cells[donor_bit], cells[1 - donor_bit]
    alpha = int(sum(cell[1] - cell[0] for cell in B) > 0)
    beta = 1 - alpha
    r = sum(cell[alpha] for cell in A)
    s = sum(cell[beta] for cell in B)
    k = sum(cell[alpha] for cell in B) - s
    reasons = set()
    if k == 3 and s in (0, 1):
        reasons.add("mono3" if s == 0 else "R41")
    if k in (3, 4) and r <= 5 and all(
        1 <= (gap := b[alpha] - b[beta]) <= 2
        and a[beta] >= gap and (gap == 1 or b[beta] <= 1)
        for a, b in zip(A, B)
    ):
        reasons.add("old_controlled_count")
    for x_bit in BITS:
        if not A[x_bit][beta]:
            continue
        if (r, k, s) == (3, 3, 2):
            for t in BITS:
                a = A[t][alpha]
                gap = A[t][beta] - int(t == x_bit) + 2 - a
                if B[t][alpha] >= 2 and donor_ok(r, a, gap):
                    reasons.add("free_A6_same_side")
        if k in (3, 4, 5) and s <= 2:
            for u0, u1 in product((1, 2), repeat=2):
                if u0 + u1 != k - 1:
                    continue
                if all(
                    B[t][alpha] >= u
                    and A[t][beta] - A[t][alpha] - int(t == x_bit) == u
                    and (u == 1 or A[t][alpha] <= 1)
                    for t, u in enumerate((u0, u1))
                ):
                    reasons.add("split_small_receiver")
    return reasons


def independent_scalar_table():
    data = json.loads((HERE / "SCALAR_NEW_GATES.json").read_text(encoding="utf-8"))
    remaining, gap_ok, removed = set(), 0, {}
    for a, b, c, d in product(*(range(count + 1) for count in BASE)):
        gap = a + c - b - d
        if not 3 <= abs(gap) <= 6:
            continue
        gap_ok += 1
        original = (((3 - a, 6 - b), (a, b)), ((5 - c, 2 - d), (c, d)))
        transpose = tuple(tuple(original[j][i] for j in BITS) for i in BITS)
        reasons = set().union(*(gate_reasons(matrix, side)
                                for matrix, side in product((original, transpose), BITS)))
        if reasons:
            removed[a, b, c, d] = sorted(reasons)
        else:
            remaining.add((a, b, c, d))
    recorded = set(map(tuple, data["residual_rows"]))
    assert recorded == remaining, (sorted(recorded - remaining), sorted(remaining - recorded))
    counts = Counter(reason for labels in removed.values() for reason in labels)
    assert counts == data["overlapping_hits"], counts
    assert gap_ok == 202 and len(removed) == 96 and len(remaining) == 106
    return remaining, removed


def independently_built_model(rows):
    """Use physical parity variables and unconditional cell definitions."""
    m = cp_model.CpModel()
    V = range(1 << DIM)
    holes = [m.new_bool_var(f"h{v}") for v in V]
    coordinates = [tuple(v >> i & 1 for i in AXES) for v in V]
    colors = [[v for v in V if (v.bit_count() % 2) == c] for c in BITS]
    for color in colors:
        m.add(sum(holes[v] for v in color) == 8)
    for v in colors[0]:
        for i in AXES:
            m.add(holes[v] + holes[v ^ (1 << i)] <= 1)

    counts = {}
    def ct(c, *region):
        region = tuple(sorted(region))
        key = (c, region)
        if key not in counts:
            z = m.new_int_var(0, 8, f"cell_{c}_{region}")
            m.add(z == sum(holes[v] for v in colors[c]
                          if all(coordinates[v][i] == t for i, t in region)))
            counts[key] = z
        return counts[key]

    flags = {}
    def ge(z, threshold):
        key = (str(z), threshold)
        if key not in flags:
            f = m.new_bool_var(f"test{len(flags)}")
            m.add(z >= threshold).only_enforce_if(f)
            m.add(z < threshold).only_enforce_if(~f)
            flags[key] = f
        return flags[key]

    def eq(z, value):
        f = m.new_bool_var(f"eq{len(m.proto.variables)}")
        m.add(z == value).only_enforce_if(f)
        m.add(z != value).only_enforce_if(~f)
        return f

    # Normalize with physical even holes dominant at side zero, axis zero
    # having degrees 3 for even projected supports and 2 for odd complements.
    loads = [ct(0, (i, 1)) + ct(1, (i, 0)) for i in AXES]
    for load in loads:
        m.add(load >= 2)
        m.add(load <= 5)
    for left, right in zip(loads, loads[1:]):
        m.add(left >= right)
    m.add(ct(0, (0, 1)) == 3)
    m.add(ct(1, (0, 0)) == 2)

    def split_counts(r, s, k):
        allowed = []
        if s > 2:
            return allowed
        for a, b, c in product(range(r + 1), range(r + k + 1), range(s + k + 1)):
            for x_bit in BITS:
                u = b - a - int(x_bit == 1)
                v = k - 1 - u
                if (
                    (b if x_bit else r + k - b) > 0
                    and 1 <= u <= min(c, 2) and 1 <= v <= min(s + k - c, 2)
                    and (u == 1 or a <= 1) and (v == 1 or r - a <= 1)
                ):
                    allowed.append((a, b, c))
                    break
        return allowed

    for j in AXES:
        inners = [i for i in AXES if i != j]
        central = eq(loads[j], 5)
        m.add(ct(0, (j, 1)) >= 2).only_enforce_if(central)
        m.add(ct(1, (j, 0)) >= 2).only_enforce_if(central)
        for alpha in BITS:
            A, B = (j, 1-alpha), (j, alpha)
            beta = 1-alpha
            r_var, s_var = ct(alpha, A), ct(beta, B)
            front = eq(r_var, 3)
            rare, strong = [], []
            for i in inners:
                a, b = ct(alpha, A, (i, 1)), ct(beta, A, (i, 1))
                c, d = ct(alpha, B, (i, 1)), ct(beta, B, (i, 1))
                m.add_allowed_assignments((a, b, c, d), sorted(rows)).only_enforce_if(
                    central, front
                )
                rare_i = m.new_bool_var(f"rare_{j}_{alpha}_{i}")
                strong_i = m.new_bool_var(f"strong_{j}_{alpha}_{i}")
                col_rows = [(x, y, int(x-y in (1, 2)), int((x, y) in {(2, 0), (3, 2)}))
                            for x, y in product(range(6), range(3))]
                m.add_allowed_assignments((c, d, rare_i, strong_i), col_rows).only_enforce_if(
                    central, front
                )
                rare.append(rare_i)
                strong.append(strong_i)
                all_split = [(k, r, s, x, y, z)
                             for k, s in product((3, 4, 5), range(3))
                             for r in [8 - k - s]
                             for x, y, z in split_counts(r, s, k)]
                k_var = m.new_int_var(3, 6, f"gap_{j}_{alpha}_{i}")
                m.add(k_var + loads[j] == 8)
                m.add_forbidden_assignments((k_var, r_var, s_var, a, b, c), all_split)
            m.add(sum(rare) <= 2).only_enforce_if(central, front)
            for f in strong:
                m.add(sum(rare) <= 1).only_enforce_if(central, front, f)

            # The scalar table includes forward free-A6 on every inner axis.
            # It already excludes any joint five-gate hit in that orientation.
            # Check only the reverse orientation on the two distinct inner axes.
            for k, t in product(inners, BITS):
                T = (k, t)
                a, b = ct(alpha, A, T), ct(beta, A, T)
                for eps in BITS:
                    gate = m.new_bool_var(f"donor_{j}_{alpha}_{k}_{t}_{eps}")
                    donor_rows = [(x, y, int(donor_ok(2, x, y-eps+2-x)))
                                  for x, y in product(range(3), range(6))]
                    m.add_allowed_assignments((a, b, gate), donor_rows).only_enforce_if(
                        central, ~front
                    )
                    for i, sb in product(inners, BITS):
                        if i == k:
                            continue
                        S = (i, sb)
                        g = ct(alpha, B, S) - ct(beta, B, S)
                        left = ct(alpha, B, T, S)
                        right = ct(alpha, B, T, (i, 1-sb))
                        source = ct(beta, A, (k, t if eps else 1-t), S)
                        m.add_bool_or((
                            ~central, front, ~gate, ~ge(source, 1), ~ge(g, 1), ge(g, 4),
                            ~ge(left - g, -1), ~ge(right + g, 3)
                        ))
    return m


def main():
    started = time.monotonic()
    rows, removed = independent_scalar_table()
    model = independently_built_model(rows)
    error = model.validate()
    assert not error, error
    build = time.monotonic() - started
    print(f"Scalar equality: 106 permitted rows, 96 removed with witnesses; model built in {build:.3f}s", flush=True)
    solver = cp_model.CpSolver()
    solver.parameters.num_workers = 8
    solver.parameters.random_seed = 20261116
    solver.parameters.max_time_in_seconds = SECONDS
    status = solver.solve(model)
    tracked = (
        "EVEN_GLOBAL_AUDIT.py", "FINAL_JOINT_PROBE.py", "FINAL_JOINT_PROBE.json",
        "GLOBAL_PROBE.py", "FREE_A6_SUPPLY.py", "FREE_A6_JOINT_PROBE.py",
        "SPLIT_SMALL_GLOBAL_PROBE.py", "SCALAR_NEW_GATES.json", "FREE_A6_TRANSFER.md",
        "SPLIT_DONOR_SMALL_RECEIVER.md", "PROBE.py", "NEW_SPLIT_CHECK.py"
    )
    result = {
        "solver": ortools.__version__,
        "hashes": {p: sha256((HERE / p).read_bytes()).hexdigest() for p in tracked},
        "status": solver.status_name(status),
        "build_seconds": build,
        "budget_solver_seconds": SECONDS,
        "seed": solver.parameters.random_seed,
        "workers": solver.parameters.num_workers,
        "solver_wall_seconds": solver.wall_time,
        "model_stats": model.model_stats(),
        "response_stats": solver.response_stats(),
        "model_text_sha256": sha256(str(model.proto).encode("utf-8")).hexdigest(),
        "scalar_removed": {str(row): reasons for row, reasons in sorted(removed.items())}
    }
    (HERE / "EVEN_GLOBAL_AUDIT.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(result["status"], result["solver_wall_seconds"], flush=True)


if __name__ == "__main__":
    main()
