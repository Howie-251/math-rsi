"""Capped feasibility test for the joint gap-three through gap-six geometry gates."""
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path
from time import monotonic

from ortools.sat.python import cp_model

from GLOBAL_PROBE import bits, indicator_at_least, indicator_equal, make_model, verify_model_solution
from PROBE import AXES, oriented_cut

PARITY = 1
SECONDS = 30
WORKERS = 8
Q_PAIRS = tuple(product((1, 2), repeat=2))


def old_phi(r, a, ell):
    if r-a < 0 or r+4-a-ell < 0:
        return False
    return ((a in (0, 1) and ell == 4 and r-a >= 1)
            or (a in (0, 1) and ell == 5 and 1 <= r-a <= 16)
            or (a in (0, 1) and ell == 6 and r-a in (2, 3))
            or (a == 2 and ell == 3 and 0 <= r-a <= 15))


def extend_model(model, holes):
    # Reuse the counts already defined by the gap-three model.
    existing = {v.name: model.get_int_var_from_proto_index(i)
                for i, v in enumerate(model.proto.variables)}
    counts = {}
    thresholds = {}

    def count(color, *positions):
        pattern = tuple(sorted(set(positions)))
        if len({axis for axis, _ in pattern}) != len(pattern):
            return 0
        key = color, pattern
        if key not in counts:
            name = f"count_{key}"
            if name in existing:
                counts[key] = existing[name]
            else:
                entries = [flag for v, flag in holes[color].items() if bits(v, pattern)]
                total = model.new_int_var(0, min(8, len(entries)), name)
                model.add(total == sum(entries))
                counts[key] = total
        return counts[key]

    def at_least(color, threshold, *positions):
        pattern = tuple(sorted(set(positions)))
        key = color, pattern, threshold
        if key not in thresholds:
            amount = count(color, *pattern)
            thresholds[key] = (
                model.new_constant(int(amount >= threshold)) if isinstance(amount, int)
                else indicator_at_least(model, amount, threshold, f"joint_threshold_{key}")
            )
        return thresholds[key]

    lam = [count(PARITY, (j, 1)) + count(1-PARITY, (j, 0)) for j in AXES]
    for left, right in zip(lam, lam[1:]):
        model.add(left >= right)
    model.add(count(PARITY, (0, 1)) == 3)
    model.add(count(1-PARITY, (0, 0)) == 2)

    table = [(r, a, b, *(int(old_phi(r, a, b-eps+2-a)) for eps in range(5)))
             for r in range(5) for a in range(r+1) for b in range(9)]
    plans = 0
    for j in AXES:
        gap = {k: indicator_equal(model, lam[j], 8-k, f"joint_gap_{j}_{k}")
               for k in (4, 5, 6)}
        inner = [i for i in AXES if i != j]
        for B_side in (0, 1):
            alpha = PARITY ^ B_side
            beta = 1-alpha
            A, B = (j, 1-B_side), (j, B_side)
            r = count(alpha, A)
            for h, t_side in product(inner, (0, 1)):
                T, Tc = (h, t_side), (h, 1-t_side)
                a, b = count(alpha, A, T), count(beta, A, T)
                phi = [model.new_bool_var(f"joint_phi_{j}_{B_side}_{h}_{t_side}_{eps}")
                       for eps in range(5)]
                model.add_allowed_assignments([r, a, b, *phi], table).only_enforce_if(
                    ~existing[f"gap3_{j}"])
                for i in inner:
                    S, Sc = (i, 0), (i, 1)
                    g = count(alpha, B, S) - count(beta, B, S)
                    inside = count(alpha, B, S, T)
                    outside = count(alpha, B, Sc, T)
                    receiver = {}
                    for q0 in (1, 2):
                        name = f"joint_recv_{j}_{B_side}_{i}_{h}_{t_side}_{q0}"
                        receiver[q0] = [
                            indicator_at_least(model, g, q0, name+"_gap_low"),
                            ~indicator_at_least(model, g, q0+3, name+"_gap_high"),
                            indicator_at_least(model, inside-g, -q0, name+"_in"),
                            indicator_at_least(model, outside+g, 2+q0, name+"_out"),
                        ]
                    for q0, q1 in Q_PAIRS:
                        k = q0 + q1 + 2
                        common = [gap[k], *receiver[q0],
                                  at_least(beta, q0, A, S), at_least(beta, q1, A, Sc)]
                        if q0 == 2:
                            common.append(~at_least(beta, 2, B, S))
                        if q1 == 2:
                            common.append(~at_least(beta, 2, B, Sc))
                        for eps in range(q0 + q1 + 1):
                            # The six inequalities are L <= eps <= U written
                            # without auxiliary max/min terms. Source row totals
                            # are already supplied by the two terms in common.
                            capacities = (
                                (q0-eps, (A, S, Tc)), (q1-eps, (A, Sc, Tc)),
                                (q0+q1-eps, (A, Tc)),
                                (eps-q1, (A, S, T)), (eps-q0, (A, Sc, T)),
                                (eps, (A, T)),
                            )
                            source = [at_least(beta, minimum, *pattern)
                                      for minimum, pattern in capacities if minimum > 0]
                            model.add_bool_or([~flag for flag in (*common, *source, phi[eps])])
                            plans += 1
    assert plans == 16128
    return plans


def check_high_gaps(colors, delta):
    checks = []
    for j, B_side in product(AXES, (0, 1)):
        k = abs(delta[j])
        if k == 3:
            continue
        aa, ab, ba, bb = tuple(map(set, oriented_cut(colors, j, B_side)))
        assert len(ab)-len(aa) == len(ba)-len(bb) == k
        inner = [i for i in AXES if i != j]
        row = dict(axis=j, receiver_bit=B_side, gap=k, counts=Counter(),
                   four_donor_gates=None)
        for xs in combinations(sorted(ab), k-2):
            X = set(xs)
            Y = {x ^ (1 << j) for x in X}
            for us in combinations(sorted(ba), 2):
                U = set(us)
                V = {u ^ (1 << j) for u in U}
                row["counts"]["source_return_pairs"] += 1
                new_ba = (ba - U) | Y
                new_ab = (ab - X) | V
                for i in inner:
                    q0 = sum(v >> i & 1 == 0 for v in Y)
                    q1 = len(Y) - q0
                    if q0 not in (1, 2) or q1 not in (1, 2):
                        continue
                    c = sum(v >> i & 1 == 0 for v in new_ba)
                    d = sum(v >> i & 1 == 0 for v in bb)
                    if c-d != 2*q0 or (q0 == 2 and d > 1) or (q1 == 2 and len(bb)-d > 1):
                        continue
                    row["counts"]["actual_receiver_xui"] += 1
                    for h, side in product(inner, (0, 1)):
                        if not bits(us[0], [(h, side)]) or not bits(us[1], [(h, side)]):
                            continue
                        row["counts"]["same_side_donor_halves"] += 1
                        a = sum(v >> h & 1 == side for v in aa)
                        ell = sum(v >> h & 1 == side for v in new_ab) - a
                        if old_phi(len(aa), a, ell):
                            row["four_donor_gates"] = dict(X=xs, U=us, i=i, h=h, Tside=side,
                                                          a=a, ell=ell)
                            break
        assert row["four_donor_gates"] is None, row
        checks.append(row)
    return checks


def main():
    started = monotonic()
    model, holes, gap3_plans = make_model(PARITY)
    higher_plans = extend_model(model, holes)
    error = model.validate()
    if error:
        raise ValueError(error)
    built = monotonic()
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = SECONDS
    solver.parameters.num_workers = WORKERS
    solver.parameters.random_seed = 20261115
    status = solver.solve(model)
    result = dict(parity=PARITY, seconds_limit=SECONDS, workers=WORKERS,
                  status=solver.status_name(status), solver_wall_seconds=solver.wall_time,
                  build_seconds=built-started, model_stats=model.model_stats(),
                  gap3_plans=gap3_plans, higher_plans=higher_plans,
                  response_stats=solver.response_stats())
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        colors = [sorted(v for v, flag in holes[c].items() if solver.value(flag))
                  for c in (0, 1)]
        candidate = verify_model_solution(colors, PARITY)
        candidate["higher_gap_checks"] = check_high_gaps(colors, candidate["delta_even_minus_odd"])
        result["candidate"] = candidate
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n",
                                                  encoding="utf-8")
    print({k: result[k] for k in ("status", "solver_wall_seconds", "gap3_plans", "higher_plans")})


if __name__ == "__main__":
    main()

