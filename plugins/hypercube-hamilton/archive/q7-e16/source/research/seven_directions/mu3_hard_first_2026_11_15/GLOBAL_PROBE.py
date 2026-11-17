"""One capped CP-SAT feasibility probe over both normalized Q7 hole parities."""
import json
from itertools import product
from pathlib import Path
from time import monotonic

from ortools.sat.python import cp_model

from PROBE import AXES, MASK, axis_info, short_matching, test_central

PER_PARITY_SECONDS = 30
WORKERS = 8


def bits(v, pattern):
    return all(((v >> axis) & 1) == side for axis, side in pattern)


def indicator_equal(model, expr, value, name):
    flag = model.new_bool_var(name)
    model.add(expr == value).only_enforce_if(flag)
    model.add(expr != value).only_enforce_if(~flag)
    return flag


def indicator_at_least(model, expr, value, name):
    flag = model.new_bool_var(name)
    model.add(expr >= value).only_enforce_if(flag)
    model.add(expr < value).only_enforce_if(~flag)
    return flag


def phi(r, a, b, epsilon):
    ell = b - epsilon + 2 - a
    complement_beta = r + 4 - a - ell
    if complement_beta < 0:
        return False
    return (
        (a in (0, 1) and ell == 4 and r - a >= 1)
        or (a in (0, 1) and ell == 5 and 1 <= r-a <= 16)
        or (a in (0, 1) and ell == 6 and r-a in (2, 3))
        or (a == 2 and ell == 3 and 0 <= r-a <= 15)
        or (a == 1 and ell == 3)
    )


def make_model(parity):
    model = cp_model.CpModel()
    support = tuple(v for v in range(128) if v.bit_count() % 2 == parity)
    groups = [{v: model.new_bool_var(f"P{v}") for v in support},
              {MASK ^ v: model.new_bool_var(f"Q{v}") for v in support}]
    by_parity = {parity: groups[0], 1-parity: groups[1]}
    for group in groups:
        model.add(sum(group.values()) == 8)
    for p in groups[0]:
        for k in AXES:
            model.add_bool_or((~groups[0][p], ~groups[1][p ^ (1 << k)]))

    counts = {}

    def count(color, *positions):
        pattern = tuple(sorted(positions))
        key = (color, pattern)
        if key not in counts:
            entries = [flag for v, flag in by_parity[color].items()
                       if bits(v, pattern)]
            total = model.new_int_var(0, min(8, len(entries)), f"count_{key}")
            model.add(total == sum(entries))
            counts[key] = total
        return counts[key]

    active = []
    for j in AXES:
        p = count(parity, (j, 1))
        q = count(1-parity, (j, 0))
        model.add(p + q >= 2)
        model.add(p + q <= 5)
        central = indicator_equal(model, p+q, 5, f"gap3_{j}")
        active.append(central)
        model.add(p >= 2).only_enforce_if(central)
        model.add(q >= 2).only_enforce_if(central)
    model.add_bool_or(active)

    macros = [(c, d, int(c-d in (1, 2)), int((c, d) in ((2, 0), (3, 2))))
              for c, d in product(range(6), range(3))]
    phi_rows = [(r, a, b, int(phi(r, a, b, 0)), int(phi(r, a, b, 1)))
                for r in (2, 3) for a in range(r+1) for b in range(r+4)]
    plan_count = 0
    for j in AXES:
        inner = [k for k in AXES if k != j]
        for B_side in (0, 1):
            # Since lambda_j <= 5, the bit-zero majority is P and the
            # bit-one majority is MASK xor Q, independently of support parity.
            alpha = parity ^ B_side
            beta = 1 - alpha
            A = (j, 1 - B_side)
            B = (j, B_side)
            r = count(alpha, A)
            minor_two = indicator_equal(model, count(beta, B), 2,
                                        f"minor_two_{j}_{B_side}")
            rare_flags = []
            strong_flags = []
            for k in inner:
                c, d = count(alpha, B, (k, 1)), count(beta, B, (k, 1))
                rare = model.new_bool_var(f"rare_{j}_{B_side}_{k}")
                strong = model.new_bool_var(f"strong_{j}_{B_side}_{k}")
                model.add_allowed_assignments([c, d, rare, strong], macros).only_enforce_if(
                    [active[j], minor_two])
                rare_flags.append(rare)
                strong_flags.append(strong)
            model.add(sum(rare_flags) <= 2).only_enforce_if([active[j], minor_two])
            for strong in strong_flags:
                model.add(sum(rare_flags) <= 1).only_enforce_if(
                    [active[j], minor_two, strong])

            gap = {}
            for i, s in product(inner, (0, 1)):
                S = (i, s)
                g = count(alpha, B, S) - count(beta, B, S)
                gap[i, s] = (
                    g,
                    indicator_at_least(model, g, 1, f"gap_lower_{j}_{B_side}_{i}_{s}"),
                    ~indicator_at_least(model, g, 4, f"gap_excl_upper_{j}_{B_side}_{i}_{s}"),
                )
            for k, t in product(inner, (0, 1)):
                T = (k, t)
                a, b = count(alpha, A, T), count(beta, A, T)
                gate = [model.new_bool_var(f"donor_{j}_{B_side}_{k}_{t}_{eps}")
                        for eps in (0, 1)]
                model.add_allowed_assignments([r, a, b, *gate], phi_rows).only_enforce_if(active[j])
                for (i, s), (g, lower_gap, valid_upper_gap) in gap.items():
                    if i == k:
                        continue
                    S = (i, s)
                    inside = count(alpha, B, T, S)
                    outside = count(alpha, B, T, (i, 1-s))
                    left_ok = indicator_at_least(model, inside-g, -1,
                                                  f"left_{j}_{B_side}_{k}_{t}_{i}_{s}")
                    right_ok = indicator_at_least(model, outside+g, 3,
                                                   f"right_{j}_{B_side}_{k}_{t}_{i}_{s}")
                    for eps in (0, 1):
                        x_on_k = t if eps else 1-t
                        source = count(beta, A, S, (k, x_on_k))
                        present = indicator_at_least(model, source, 1,
                                                     f"source_{j}_{B_side}_{k}_{t}_{i}_{s}_{eps}")
                        model.add_bool_or((~active[j], ~gate[eps], ~present,
                                           ~lower_gap, ~valid_upper_gap, ~left_ok, ~right_ok))
                        plan_count += 1
    assert plan_count == 3360
    return model, by_parity, plan_count


def verify_model_solution(colors, parity):
    p = colors[parity]
    q = sorted(MASK ^ v for v in colors[1-parity])
    holes = set(colors[0] + colors[1])
    assert len(holes) == 16 and all(len(c) == 8 for c in colors)
    for color, vs in enumerate(colors):
        assert all(v.bit_count() % 2 == color for v in vs)
    assert all((v ^ w) not in (1, 2, 4, 8, 16, 32, 64)
               for v in colors[0] for w in colors[1])
    lam = [sum((v >> j) & 1 for v in p+q) for j in AXES]
    assert min(lam) >= 2 and max(lam) == 5
    delta = [sum((v >> j) & 1 for v in colors[0]) -
             sum((v >> j) & 1 for v in colors[1]) for j in AXES]
    assert tuple(map(abs, delta)) == tuple(8-x for x in lam)
    modeled_macros = {"R41", "three_mono", "central_s_ge_3", "central_s_ge_2_strong"}
    metrics = []
    omitted_macro_hits = set()
    for j, b in product(AXES, (0, 1)):
        row = axis_info(colors, j, b)
        assert not modeled_macros.intersection(row["accepted_macros"])
        omitted_macro_hits.update(row["accepted_macros"])
        if abs(delta[j]) == 3:
            row["five_gates"] = test_central(colors, j, b)
            assert row["five_gates"]["joint_witness"] is None
            if row["five_gates"]["receiver_witness"] is None:
                omitted_macro_hits.add("receiver_failure")
        metrics.append(row)
    matching = short_matching(colors)
    if matching is not None:
        assert set(range(128)) - {v for edge in matching for v in edge} == holes
    return dict(support_parity=parity, P=p, Q=q, even_holes=colors[0], odd_holes=colors[1],
                lambda_by_axis=lam, delta_even_minus_odd=delta,
                axis_metrics=metrics, omitted_macro_hits=sorted(omitted_macro_hits),
                matching=matching)


def solve(parity):
    started = monotonic()
    model, by_parity, plan_count = make_model(parity)
    model_error = model.validate()
    if model_error:
        raise ValueError(model_error)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = PER_PARITY_SECONDS
    solver.parameters.num_workers = WORKERS
    solver.parameters.random_seed = 20261115
    stats = model.model_stats()
    built = monotonic()
    status = solver.solve(model)
    row = dict(parity=parity, status=solver.status_name(status), build_seconds=built-started,
               solver_wall_seconds=solver.wall_time, model_stats=stats,
               plans=plan_count, response_stats=solver.response_stats())
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        colors = [sorted(v for v, flag in by_parity[c].items() if solver.value(flag))
                  for c in (0, 1)]
        row["candidate"] = verify_model_solution(colors, parity)
    return row


def main():
    result = dict(seconds_per_parity=PER_PARITY_SECONDS, workers=WORKERS, solves=[])
    out = Path(__file__).with_suffix(".json")
    for parity in (0, 1):
        row = solve(parity)
        result["solves"].append(row)
        out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
        print(f"parity={parity} {row['status']} wall={row['solver_wall_seconds']:.3f}", flush=True)
        if "candidate" in row:
            print({k: row["candidate"][k] for k in ("even_holes", "odd_holes", "omitted_macro_hits")},
                  flush=True)
            break


if __name__ == "__main__":
    main()

