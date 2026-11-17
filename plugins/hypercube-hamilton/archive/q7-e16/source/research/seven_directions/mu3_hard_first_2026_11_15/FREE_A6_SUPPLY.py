"""Thin CP-SAT model for the six-hole whole-receiver supply criterion."""
import json
from itertools import product
from pathlib import Path
from time import monotonic

from ortools.sat.python import cp_model

from GLOBAL_PROBE import indicator_equal
from PROBE import AXES, MASK, axis_info, donor_gates, in_side, load, oriented_cut, short_matching, test_central

HERE = Path(__file__).resolve().parent
SECONDS = 30
WORKERS = 8
VALID_B = {0: (2, 3, 4, 5), 1: (2, 3, 4, 5, 6), 2: (3, 4), 3: ()}
MODELED_MACROS = {"R41", "three_mono", "central_s_ge_3", "central_s_ge_2_strong"}


def make_model(parity):
    model = cp_model.CpModel()
    p = {v: model.new_bool_var(f"P{v}") for v in range(128) if v.bit_count() % 2 == parity}
    q = {MASK ^ v: model.new_bool_var(f"Q{v}") for v in p}
    by_color = {parity: p, 1-parity: q}
    for group in (p, q):
        model.add(sum(group.values()) == 8)
    for v in p:
        for j in AXES:
            model.add_bool_or((~p[v], ~q[v ^ (1 << j)]))
    if parity == 1:
        model.add(sum(flag for v, flag in p.items() if v.bit_count() == 1) <= 6)
        model.add(sum(flag for v, flag in q.items() if (MASK ^ v).bit_count() == 1) <= 6)

    counts = {}

    def count(color, *positions):
        pattern = tuple(sorted(positions))
        key = color, pattern
        if key not in counts:
            entries = [flag for v, flag in by_color[color].items()
                       if all(v >> j & 1 == bit for j, bit in pattern)]
            total = model.new_int_var(0, 8, f"count_{key}")
            model.add(total == sum(entries))
            counts[key] = total
        return counts[key]

    for j in AXES:
        pj = count(parity, (j, 1))
        qj = count(1-parity, (j, 0))
        lam = pj+qj
        model.add_linear_constraint(lam, 2, 5)
        if j:
            model.add(lam <= previous)
        else:
            model.add(pj == 3)
            model.add(qj == 2)
        previous = lam
        gap3 = indicator_equal(model, lam, 5, f"gap3_{j}")
        model.add(pj >= 2).only_enforce_if(gap3)
        model.add(qj >= 2).only_enforce_if(gap3)

        strong_columns = [(c, d, int(c-d in (1, 2)), int((c, d) in ((2, 0), (3, 2))))
                          for c, d in product(range(6), range(3))]
        suppliers = [(a, b, c) for a, values in VALID_B.items() for b in values for c in range(2, 6)]
        for B_side in (0, 1):
            alpha = parity ^ B_side
            beta = 1-alpha
            A, B = (j, 1-B_side), (j, B_side)
            r3 = indicator_equal(model, count(alpha, A), 3, f"r3_{j}_{B_side}")
            forward = (gap3, r3)
            scarce, strong = [], []
            for k in AXES:
                if k == j:
                    continue
                c, d = count(alpha, B, (k, 1)), count(beta, B, (k, 1))
                rare = model.new_bool_var(f"rare_{j}_{B_side}_{k}")
                fixed = model.new_bool_var(f"strong_{j}_{B_side}_{k}")
                model.add_allowed_assignments((c, d, rare, fixed), strong_columns).only_enforce_if(forward)
                scarce.append(rare)
                strong.append(fixed)
                for t in (0, 1):
                    a = count(alpha, A, (k, t))
                    b = count(beta, A, (k, t))
                    c = count(alpha, B, (k, t))
                    model.add_forbidden_assignments((a, b, c), suppliers).only_enforce_if(forward)
            model.add(sum(scarce) <= 2).only_enforce_if(forward)
            for fixed in strong:
                model.add(sum(scarce) <= 1).only_enforce_if((*forward, fixed))
    return model, by_color


def verify_supply_table():
    for a, b in product(range(4), range(7)):
        possible = any(any(donor_gates(3, a, b-epsilon+2-a)) for epsilon in (0, 1)
                       if (b if epsilon else 6-b) > 0)
        assert possible == (b in VALID_B[a])


def forward_supply(colors, j, B_side):
    aa, ab, ba, bb = oriented_cut(colors, j, B_side)
    if tuple(map(len, (aa, ab, ba, bb))) != (3, 6, 5, 2):
        return None
    for k, side in product(AXES, (0, 1)):
        if k == j:
            continue
        a, b, c = (len(in_side(vs, k, side)) for vs in (aa, ab, ba))
        if c < 2 or b not in VALID_B[a]:
            continue
        U = in_side(ba, k, side)[:2]
        for x in ab:
            epsilon = int(x >> k & 1 == side)
            ell = b-epsilon+2-a
            gates = donor_gates(3, a, ell)
            if any(gates):
                y = x ^ (1 << j)
                V = tuple(u ^ (1 << j) for u in U)
                H_a_beta = (set(ab)-{x}) | set(V)
                H_b_alpha = (set(ba)-set(U)) | {y}
                return dict(axis=j, receiver_bit=B_side, donor_axis=k, donor_bit=side,
                            a=a, b=b, c=c, epsilon=epsilon, ell=ell, x=x, U=U, y=y, V=V,
                            after_donor=[aa, sorted(H_a_beta)],
                            after_receiver=[sorted(H_b_alpha), bb])
        raise AssertionError("supply table did not recover a forward source")
    return None


def verify_candidate(colors, parity):
    p, q = colors[parity], sorted(MASK ^ v for v in colors[1-parity])
    assert all(len(c) == 8 for c in colors)
    assert all(v.bit_count() % 2 == c for c in (0, 1) for v in colors[c])
    assert all((v ^ w).bit_count() != 1 for v in colors[0] for w in colors[1])
    lam = [load(p, k)+load(q, k) for k in AXES]
    delta = [load(colors[0], k)-load(colors[1], k) for k in AXES]
    assert lam == sorted(lam, reverse=True) and lam[0] == 5 and lam[-1] >= 2
    assert load(p, 0) == 3 and load(q, 0) == 2
    assert tuple(map(abs, delta)) == tuple(8-x for x in lam)
    rows = []
    omitted_macros = set()
    for j, side in product(AXES, (0, 1)):
        row = axis_info(colors, j, side)
        assert not (set(row["accepted_macros"]) & MODELED_MACROS)
        omitted_macros.update(row["accepted_macros"])
        if abs(delta[j]) == 3:
            assert forward_supply(colors, j, side) is None
            row["old_five_gates"] = test_central(colors, j, side)
            if row["old_five_gates"]["receiver_witness"] is None:
                omitted_macros.add("receiver_failure")
        rows.append(row)
    return dict(P=p, Q=q, even_holes=colors[0], odd_holes=colors[1],
                lambda_by_axis=lam, delta_even_minus_odd=delta, axes=rows,
                omitted_macro_hits=sorted(omitted_macros), matching=short_matching(colors))


def solve(parity):
    start = monotonic()
    model, holes = make_model(parity)
    error = model.validate()
    if error:
        raise ValueError(error)
    build_seconds = monotonic()-start
    print(f"parity={parity} model built in {build_seconds:.3f}s", flush=True)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = SECONDS
    solver.parameters.num_workers = WORKERS
    solver.parameters.random_seed = 20261115
    status = solver.solve(model)
    result = dict(parity=parity, status=solver.status_name(status),
                  solver_wall_seconds=solver.wall_time, build_seconds=build_seconds,
                  model_stats=model.model_stats(), response_stats=solver.response_stats())
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        colors = [sorted(v for v, flag in holes[c].items() if solver.value(flag)) for c in (0, 1)]
        result["candidate"] = verify_candidate(colors, parity)
    return result


def main():
    verify_supply_table()
    previous = json.loads((HERE / "GLOBAL_PROBE.json").read_text(encoding="utf-8"))
    fixed = previous["solves"][-1]["candidate"]
    colors = [fixed["even_holes"], fixed["odd_holes"]]
    recovered = forward_supply(colors, 0, 1)
    assert recovered and recovered["epsilon"] == 1
    result = dict(seconds_per_parity=SECONDS, workers=WORKERS, prior_witness=recovered, solves=[])
    path = Path(__file__).with_suffix(".json")
    for parity in (0, 1):
        row = solve(parity)
        result["solves"].append(row)
        path.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
        print(f"parity={parity} {row['status']} wall={row['solver_wall_seconds']:.3f}s", flush=True)
        if "candidate" in row:
            c = row["candidate"]
            print(c["even_holes"], c["odd_holes"], "matching found", c["matching"] is not None,
                  "omitted macros", c["omitted_macro_hits"], flush=True)
            break


if __name__ == "__main__":
    main()

