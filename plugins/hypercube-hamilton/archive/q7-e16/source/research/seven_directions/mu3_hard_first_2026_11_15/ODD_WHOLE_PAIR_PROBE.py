"""One odd-support query with the complete gap-four whole-face pair criterion."""
from itertools import combinations, product
import json
from pathlib import Path
from time import monotonic

from ortools.sat.python import cp_model

from FINAL_JOINT_PROBE import readback_known, scalar_rows
from FREE_A6_SUPPLY import verify_supply_table
from GLOBAL_PROBE import bits, indicator_at_least
from JOINT_GAP_PROBE import old_phi
from ODD_FULL_JOINT_PROBE import build, readback_high_gap_witness, verify_candidate
from PROBE import AXES, in_side, oriented_cut
from SPLIT_SMALL_GLOBAL_PROBE import old_gate_checks

HERE = Path(__file__).resolve().parent
PARITY = 1
SECONDS = 120
WORKERS = 8


def add_whole_pair_exclusions(model, holes):
    existing = {v.name: model.get_int_var_from_proto_index(i)
                for i, v in enumerate(model.proto.variables)}
    count_cache = {}
    threshold_cache = {}

    def count(color, positions):
        pattern = tuple(sorted(set(positions)))
        if len({axis for axis, _ in pattern}) != len(pattern):
            return 0
        key = (color, pattern)
        if key not in count_cache:
            name = f"count_{key}"
            if name in existing:
                count_cache[key] = existing[name]
            else:
                total = model.new_int_var(0, 8, name)
                model.add(total == sum(flag for v, flag in holes[color].items() if bits(v, pattern)))
                count_cache[key] = total
        return count_cache[key]

    def at_least(color, minimum, *positions):
        key = (color, tuple(sorted(set(positions))), minimum)
        if key not in threshold_cache:
            previous = f"joint_threshold_{key}"
            if previous in existing:
                threshold_cache[key] = existing[previous]
            else:
                total = count(color, key[1])
                threshold_cache[key] = (
                    model.new_constant(int(total >= minimum)) if isinstance(total, int)
                    else indicator_at_least(model, total, minimum, f"whole_threshold_{key}")
                )
        return threshold_cache[key]

    def enable_choice(flag, phi, color, face, shared, side, opposite):
        # For each feasible placement, force its side-existence literal true.
        # A nonexistent side can always take false, which suffices for projection.
        for n in range(3):
            required = [phi[n]]
            if n:
                required.append(at_least(color, n, face, shared, side))
            if n < 2:
                required.append(at_least(color, 2-n, face, shared, opposite))
            model.add_bool_or([~literal for literal in required] + [flag])

    common = 0
    for j, B_side in product(AXES, (0, 1)):
        active = existing[f"joint_gap_{j}_4"]
        alpha = PARITY ^ B_side
        beta = 1-alpha
        A, B = (j, 1-B_side), (j, B_side)
        halves = [(k, side) for k, side in product(AXES, (0, 1)) if k != j]
        for (i, s), (h, t) in product(halves, repeat=2):
            S, Sc, T, Tc = (i, s), (i, 1-s), (h, t), (h, 1-t)
            donor_phi = [existing[f"joint_phi_{j}_{B_side}_{h}_{t}_{n}"] for n in range(3)]
            receiver_phi = [existing[f"joint_phi_{j}_{1-B_side}_{i}_{s}_{n}"] for n in range(3)]
            design = f"{j}_{B_side}_{i}_{s}_{h}_{t}"
            donor = model.new_bool_var(f"whole_donor_{design}")
            receiver = model.new_bool_var(f"whole_receiver_{design}")
            enable_choice(donor, donor_phi, beta, A, S, T, Tc)
            enable_choice(receiver, receiver_phi, alpha, B, T, S, Sc)
            model.add_bool_or((~active, ~donor, ~receiver))
            common += 1
    assert common == 2016
    return common


def scalar_pair(groups, S, T):
    aa, ab, ba, bb = groups
    i, s = S
    h, t = T
    a, b = (len(in_side(group, h, t)) for group in (aa, ab))
    c, d = (len(in_side(group, i, s)) for group in (ba, bb))
    X_pool = in_side(ab, i, s)
    U_pool = in_side(ba, h, t)
    X_in = len(in_side(X_pool, h, t))
    U_in = len(in_side(U_pool, i, s))
    donor = any(old_phi(len(aa), a, b-epsilon+2-a)
                and X_in >= epsilon and len(X_pool)-X_in >= 2-epsilon
                for epsilon in range(3))
    receiver = any(old_phi(len(bb), d, c-n+2-d)
                   and U_in >= n and len(U_pool)-U_in >= 2-n
                   for n in range(3))
    return donor and receiver


def direct_pair(groups, outer, S, T):
    aa, ab, ba, bb = groups
    i, s = S
    h, t = T
    a = len(in_side(aa, h, t))
    d = len(in_side(bb, i, s))
    for X in combinations(in_side(ab, i, s), 2):
        Y = {x ^ (1 << outer) for x in X}
        for U in combinations(in_side(ba, h, t), 2):
            V = {u ^ (1 << outer) for u in U}
            A_prime = (set(ab)-set(X)) | V
            B_prime = (set(ba)-set(U)) | Y
            ell_A = len(in_side(A_prime, h, t))-a
            ell_B = len(in_side(B_prime, i, s))-d
            if old_phi(len(aa), a, ell_A) and old_phi(len(bb), d, ell_B):
                return dict(X=X, U=U, Y=sorted(Y), V=sorted(V),
                            donor_cut=T, receiver_cut=S, donor_a=a, donor_ell=ell_A,
                            receiver_d=d, receiver_ell=ell_B)
    return None


def every_whole_pair(colors, delta):
    rows = []
    for outer, B_side in product(AXES, (0, 1)):
        if abs(delta[outer]) != 4:
            continue
        groups = oriented_cut(colors, outer, B_side)
        halves = [(k, b) for k, b in product(AXES, (0, 1)) if k != outer]
        counts = dict(cases=0, positives=0)
        first = None
        for S, T in product(halves, repeat=2):
            direct = direct_pair(groups, outer, S, T)
            assert scalar_pair(groups, S, T) == (direct is not None), (outer, B_side, S, T)
            counts["cases"] += 1
            if direct is not None:
                counts["positives"] += 1
                if first is None:
                    first = direct
        rows.append(dict(outer=outer, receiver_bit=B_side, counts=counts, first_plan=first))
    return rows


def regression_known_whole_face():
    rows = []
    for filename in ("FINAL_JOINT_PROBE.json", "ODD_FULL_JOINT_PROBE.json"):
        data = json.loads((HERE / filename).read_text(encoding="utf-8"))
        witness = data["candidate"] if "candidate" in data else data["solves"][-1]["candidate"]
        colors = tuple(tuple(witness[key]) for key in ("even_holes", "odd_holes"))
        M = witness["matching"]
        ends = {v for edge in M for v in edge}
        assert len(M) == 56 and all((u ^ v).bit_count() == 1 for u, v in M)
        assert set(range(128))-ends == set(colors[0]) | set(colors[1]) and len(ends)==112
        assert all((u ^ v).bit_count() != 1 for u in colors[0] for v in colors[1])
        delta = witness["delta_even_minus_odd"]
        checks = every_whole_pair(colors, delta)
        old = witness["fixed_input_old_checks"]["legacy"]["plan"]
        j, B_side = old["outer"], old["B_side"]
        S = (old["receiver"]["inner"], old["receiver"]["mark_side"])
        T = (old["supplier"]["inner"], old["supplier"]["mark_side"])
        groups = oriented_cut(colors, j, B_side)
        aa, ab, ba, bb = groups
        X, U = set(old["X"]), set(old["U"])
        assert X <= set(in_side(ab, *S)) and U <= set(in_side(ba, *T))
        a, d = len(in_side(aa, *T)), len(in_side(bb, *S))
        Y, V = {x ^ (1 << j) for x in X}, {u ^ (1 << j) for u in U}
        assert sorted(Y) == old["Y"] and sorted(V) == old["V"]
        assert old_phi(len(aa), a, len(in_side((set(ab)-X) | V, *T))-a)
        assert old_phi(len(bb), d, len(in_side((set(ba)-U) | Y, *S))-d)
        assert scalar_pair(groups, S, T)
        rows.append(dict(input=filename, comparisons=checks,
                         saved_plan_checked=dict(outer=j, receiver_bit=B_side, S=S, T=T,
                                                 X=old["X"], U=old["U"])))
    return rows


def main():
    verify_supply_table()
    rows = scalar_rows()
    old_cases = readback_known() + [readback_high_gap_witness()]
    new_cases = regression_known_whole_face()
    data = dict(support_parity=PARITY, seconds_limit=SECONDS, workers=WORKERS,
                known_input_gate_checks=old_cases, new_whole_face_regression=new_cases)
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    started = monotonic()
    model, holes, plan_counts = build(rows)
    plan_counts["whole_pairs"] = add_whole_pair_exclusions(model, holes)
    error = model.validate()
    if error:
        raise ValueError(error)
    built = monotonic()
    print(f"regressions agreed; model built and validated in {built-started:.3f}s", flush=True)
    print(model.model_stats(), flush=True)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = SECONDS
    solver.parameters.num_workers = WORKERS
    solver.parameters.random_seed = 20261115
    status = solver.solve(model)
    data.update(status=solver.status_name(status), build_seconds=built-started,
                solver_wall_seconds=solver.wall_time, model_stats=model.model_stats(),
                response_stats=solver.response_stats(), plan_counts=plan_counts)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        w = verify_candidate(solver, holes, rows)
        colors = w["even_holes"], w["odd_holes"]
        w["whole_pair_direct_checks"] = every_whole_pair(colors, w["delta_even_minus_odd"])
        assert not any(row["first_plan"] for row in w["whole_pair_direct_checks"])
        data["candidate"] = w
    path.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    print(f"parity=1 {data['status']} wall={solver.wall_time:.3f}s", flush=True)
    w = data.get("candidate")
    if w is not None and w["matching"] is not None:
        print(w["even_holes"], w["odd_holes"], "matching found", flush=True)
        w["fixed_input_old_checks"] = old_gate_checks(w)
        path.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
        print("legacy", w["fixed_input_old_checks"]["legacy"]["status"], flush=True)


if __name__ == "__main__":
    main()

