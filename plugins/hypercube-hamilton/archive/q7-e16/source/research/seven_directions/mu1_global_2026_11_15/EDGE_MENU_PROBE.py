"""Two capped E16 edge-domain CP queries, excluding only the two given menus."""

import json
import sys
from hashlib import sha256
from itertools import product
from pathlib import Path
from time import perf_counter

import ortools
from ortools.sat.python import cp_model

from EDGE_PROBE import (
    ALPHA, BETA, DIMENSION, LIMIT_SECONDS, SEED, VERTICES, bit_is_one,
    build_hole_model, check_holes, check_matching, short_maximum_matching,
)

HERE = Path(__file__).resolve().parent
MU3 = HERE.parent / "mu3_hard_first_2026_11_15"
sys.path.insert(0, str(MU3))
from GLOBAL_PROBE import phi
from NEW_SPLIT_CHECK import check_cut
from PROBE import oriented_cut

AXES = tuple(range(DIMENSION))
COLORS = (BETA, ALPHA)
WORKERS = 8


def plan_types(r, s, a, b, c):
    """Interpret a column as a designated donor half and its return capacity."""
    k = 8 - r - s
    if k not in (3, 4, 5) or s > 3:
        return set()
    gates = set()
    for eps in (0, 1):
        if (b if eps else r + k - b) == 0:
            continue
        if k == 3 and c >= 2 and phi(r, a, b, eps):
            gates.add("same_side")
        qT = b - a - eps
        qE = k - 1 - qT
        if qT not in (1, 2) or qE not in (1, 2):
            continue
        if (qT == 2 and a > 1) or (qE == 2 and r - a > 1):
            continue
        if c >= qT and s + k - c >= qE:
            gates.add("split")
    return gates


def count_table():
    """Include either donor-half orientation in one forbidden table."""
    rows = []
    per_gate = {}
    for k, s in product((3, 4, 5), range(4)):
        r = 8 - k - s
        for a, b, c in product(range(r + 1), range(r + k + 1), range(s + k + 1)):
            gates = plan_types(r, s, a, b, c) | plan_types(r, s, r - a, r + k - b, s + k - c)
            if gates:
                rows.append((r, s, a, b, c))
            for gate in sorted(gates):
                name = f"k{k}_s{s}_{gate}"
                per_gate[name] = per_gate.get(name, 0) + 1
    assert len(rows) == len(set(rows))
    return rows, per_gate


def add_menu(model, hole):
    counts = {}

    def count(color, *positions):
        key = (color, tuple(sorted(positions)))
        if key not in counts:
            vertices = [
                v for v in COLORS[color]
                if all(bit_is_one(v, j) == side for j, side in positions)
            ]
            variable = model.new_int_var(0, 8, f"gate_count_{key}")
            model.add(variable == sum(hole[v] for v in vertices))
            counts[key] = variable
        return counts[key]

    rows, per_gate = count_table()
    tables = 0
    for j, A_side, alpha in product(AXES, (0, 1), (0, 1)):
        beta = 1 - alpha
        A = (j, A_side)
        B = (j, 1 - A_side)
        r = count(alpha, A)
        s = count(beta, B)
        for i in AXES:
            if i == j:
                continue
            T = (i, 0)
            a = count(alpha, A, T)
            b = count(beta, A, T)
            c = count(alpha, B, T)
            model.add_forbidden_assignments([r, s, a, b, c], rows)
            tables += 1
    assert tables == 168
    return dict(table_count=tables, union_rows=len(rows), rows_by_gate=per_gate)


def pointwise_gates(holes):
    """Check actual bridge choices, without the scalar menu table."""
    from itertools import combinations

    colors = tuple(tuple(v for v in side if v in holes) for side in COLORS)
    found = []
    for j, B_side in product(AXES, (0, 1)):
        aa, ab, ba, bb = oriented_cut(colors, j, B_side)
        r, s = len(aa), len(bb)
        k = len(ab) - r
        if k not in (3, 4, 5) or s > 3:
            continue
        assert len(ba) - s == k and r + s + k == 8
        mask = 1 << j
        for i in AXES:
            if i == j:
                continue
            for x in ab:
                for U in combinations(ba, k - 1):
                    V = tuple(u ^ mask for u in U)
                    assert all(v not in holes for v in V) and x ^ mask not in holes
                    new_ab = (set(ab) - {x}) | set(V)
                    t = bit_is_one(V[0], i)
                    a = sum(bit_is_one(u, i) == t for u in aa)
                    b = sum(bit_is_one(u, i) == t for u in new_ab)
                    other_a = r - a
                    other_b = len(new_ab) - b
                    q = sum(bit_is_one(v, i) == t for v in V)
                    other_q = len(V) - q
                    gate = None
                    if k == 3 and other_q == 0:
                        ell = b - a
                        if (
                            (a <= 1 and ell == 4 and other_a >= 1)
                            or (a <= 1 and ell == 5 and 1 <= other_a <= 16)
                            or (a <= 1 and ell == 6 and other_a in (2, 3))
                            or (a == 2 and ell == 3 and 0 <= other_a <= 15)
                            or (a == 1 and ell == 3)
                        ):
                            gate = "same_side"
                    if (
                        q in (1, 2) and other_q in (1, 2)
                        and (q == 1 or a <= 1) and (other_q == 1 or other_a <= 1)
                        and b - a == 2 * q and other_b - other_a == 2 * other_q
                    ):
                        gate = "split"
                    if gate:
                        found.append(dict(gate=gate, outer_axis=j, receiver_bit=B_side,
                                          inner_axis=i, donor_half_bit=int(t), r=r, s=s, k=k,
                                          x=x, U=U, y=x ^ mask, V=V,
                                          modified_donor_halves=[[a, b], [other_a, other_b]],
                                          marks=[q, other_q], modified_receiver_counts=[s + 2, s]))
                        break
    return found


def check_saved_controls():
    data = json.loads((HERE / "EDGE_PROBE.json").read_text(encoding="utf-8"))
    summary = []
    for case in data["results"]:
        colors = tuple(tuple(case[key]) for key in ("holes_beta_even", "holes_alpha_odd"))
        holes = set().union(*colors)
        check_holes(case["a"], holes)
        assert check_matching(holes, case["short_matching"])
        old_splits = [plan for j, side in product(AXES, (0, 1))
                      if (plan := check_cut(colors, j, side))]
        plans = pointwise_gates(holes)
        old_same_side = [p for p in plans if p["gate"] == "same_side" and p["s"] == 2]
        assert old_splits and old_same_side
        summary.append(dict(a=case["a"], current_accepted_split_plans=old_splits,
                            first_accepted_same_side_plan=old_same_side[0],
                            same_side_plans_s_le_2=sum(p["gate"] == "same_side" and p["s"] <= 2 for p in plans),
                            same_side_plans_s_3=sum(p["gate"] == "same_side" and p["s"] == 3 for p in plans)))
    return summary


def probe(a):
    start = perf_counter()
    model, hole = build_hole_model(a)
    table_stats = add_menu(model, hole)
    error = model.validate()
    if error:
        raise ValueError(error)
    build_seconds = perf_counter() - start
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = LIMIT_SECONDS
    solver.parameters.num_search_workers = WORKERS
    solver.parameters.random_seed = SEED
    print(f"a={a}: model validated; starting one {LIMIT_SECONDS}s query", flush=True)
    status = solver.solve(model)
    result = dict(
        a=a, b=7-a, status=solver.status_name(status), build_seconds=build_seconds,
        wall_seconds=solver.wall_time, conflicts=solver.num_conflicts, branches=solver.num_branches,
        table_stats=table_stats, matching_calls=0,
        model_stats=model.model_stats(), response_stats=solver.response_stats(),
    )
    if status == cp_model.INFEASIBLE:
        model_path = HERE / f"EDGE_MENU_A{a}.pb"
        assert model.export_to_file(str(model_path))
        result.update(model_file=model_path.name, model_sha256=sha256(model_path.read_bytes()).hexdigest())
    elif status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        holes = {v for v in VERTICES if solver.value(hole[v])}
        axes = check_holes(a, holes)
        assert not pointwise_gates(holes), "Unexpected plan on the purported residual"
        matching = short_maximum_matching(holes)
        realized = check_matching(holes, matching)
        result.update(axes=axes, holes_alpha_odd=sorted(holes.intersection(ALPHA)),
                      holes_beta_even=sorted(holes.intersection(BETA)), matching_calls=1,
                      matching_size=len(matching), realized_by_short_matching=realized,
                      short_matching=matching)
    print(f"a={a}: {result['status']} in {result['wall_seconds']:.3f}s matching={result.get('matching_size')}",
          flush=True)
    return result


def main():
    raw = (HERE / "EDGE_PROBE.json").read_bytes()
    output = dict(
        scope="EDGE_PROBE physical necessary domain with only same-side k=3 and split k=3..5 exclusions",
        conditional_assumption="Q6 A8 completes the central gap-one exclusion and enables s=3 receivers; this probe is not a proof.",
        input_sha256=sha256(raw).hexdigest(),
        code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        base_model_sha256=sha256((HERE / "EDGE_PROBE.py").read_bytes()).hexdigest(),
        phi_source_sha256=sha256((MU3 / "GLOBAL_PROBE.py").read_bytes()).hexdigest(),
        cp_model_calls=0, max_seconds_per_call=LIMIT_SECONDS, num_search_workers=WORKERS,
        ortools_version=ortools.__version__, seed=SEED, fixed_controls=check_saved_controls(), results=[],
    )
    output_path = Path(__file__).with_suffix(".json")
    for a in (0, 1):
        output["results"].append(probe(a))
        output["cp_model_calls"] += 1
        output_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
