"""Two capped edge probes adding independently accepted low-gap exclusions."""

import json
from hashlib import sha256
from itertools import product
from pathlib import Path
from time import perf_counter

import ortools
from ortools.sat.python import cp_model

from EDGE_MENU_PROBE import (
    ALPHA, AXES, BETA, COLORS, HERE, LIMIT_SECONDS, SEED, VERTICES, WORKERS,
    add_menu, bit_is_one, build_hole_model, check_holes, check_matching,
    oriented_cut, pointwise_gates, short_maximum_matching,
)
from PROBE import controlled_count


def peeled_outer_type(alpha, beta):
    """The four fixed E16 count types with their own unconditional theorems."""
    gap = abs(alpha - beta)
    a = min(alpha, beta, 8 - alpha, 8 - beta)
    return (gap == 2 and a < 3) or (gap == 3 and a == 0)


def central_column_hit(a, b, c):
    d = b - a
    return (
        (d == 1 and a in (1, 2))
        or (d == 1 and a in (0, 3) and 0 < c < 5)
        or (d == 2 and a <= 1 and c >= 1)
        or (d in (3, 4) and a <= 1 and c >= 2)
    )


def central_column_rows():
    """Five published central delta-two column gates, closed under half swap."""
    return {
        (3, 3, a, b, c)
        for a, b, c in product(range(4), range(6), range(6))
        if central_column_hit(a, b, c) or central_column_hit(3 - a, 5 - b, 5 - c)
    }


def scalar_receiver_rows():
    """Forbidden tuples (r,s,a,b,c) for one fixed receiver half T.

    R7_CONTROLLED_CYCLE_DONOR_TRANSFER §§1–3 and
    R7_MU3_CONTROLLED_AND_T63_REVIEW §受控圈供体 apply universally.
    a,b count minority and majority holes in B∩T, and c counts the
    available A-majority sources in the mirror of B∩T.
    """
    rows_by_k = {}
    for k in (2, 3, 4):
        rows = []
        for r in range(min(5, 8 - k) + 1):
            s = 8 - k - r
            for a, b, c in product(range(s + 1), range(s + k + 1), range(r + k + 1)):
                qT = b - a
                qE = k - qT
                if qT not in (1, 2) or qE not in (1, 2):
                    continue
                if (qT == 2 and a > 1) or (qE == 2 and s - a > 1):
                    continue
                if c >= qT and r + k - c >= qE:
                    rows.append((r, s, a, b, c))
        rows_by_k[k] = rows
    rows = [row for group in rows_by_k.values() for row in group]
    assert len(rows) == len(set(rows))
    return rows, {str(k): len(group) for k, group in rows_by_k.items()}


def add_old_coverage(model, hole):
    """Use physical coordinates without any minimum-imbalance-three constraint."""
    # Refer to the actual global count variables already bound by EDGE_PROBE.
    index = {v.name: i for i, v in enumerate(model.proto.variables)}
    outer_rows = [(p, q) for p, q in product(range(9), repeat=2) if peeled_outer_type(p, q)]
    for j in AXES:
        names = (f"global_alpha_{j}", f"global_beta_{j}")
        variables = [model.get_int_var_from_proto_index(index[name]) for name in names]
        model.add_forbidden_assignments(variables, outer_rows)

    # The earlier menu already created many of these exact physical counts.
    index.update({v.name: i for i, v in enumerate(model.proto.variables)})
    counts = {}

    def count(color, *positions):
        key = (color, tuple(sorted(positions)))
        if key not in counts:
            name = f"gate_count_{key}"
            if name in index:
                variable = model.get_int_var_from_proto_index(index[name])
            else:
                variable = model.new_int_var(0, 8, name)
                vertices = [v for v in COLORS[color]
                            if all(bit_is_one(v, j) == side for j, side in positions)]
                model.add(variable == sum(hole[v] for v in vertices))
            counts[key] = variable
        return counts[key]

    rows, per_gap = scalar_receiver_rows()
    central = central_column_rows()
    union = sorted(set(rows) | central)
    tables = 0
    for j, side, alpha in product(AXES, (0, 1), (0, 1)):
        beta = 1 - alpha
        A, B = (j, side), (j, 1 - side)
        r, s = count(alpha, A), count(beta, B)
        for i in AXES:
            if i == j:
                continue
            T = (i, 0)
            a, b, c = count(beta, B, T), count(alpha, B, T), count(beta, A, T)
            model.add_forbidden_assignments([r, s, a, b, c], union)
            tables += 1
    assert tables == 168
    return dict(outer_rows=outer_rows, scalar_tables=tables, scalar_rows_by_gap=per_gap,
                central_rows=len(central), union_rows=len(union))


def validate_sat(a, holes):
    axes = check_holes(a, holes)
    assert not any(peeled_outer_type(row["alpha"], row["beta"]) for row in axes)
    assert not pointwise_gates(holes)
    colors = tuple(tuple(v for v in color if v in holes) for color in COLORS)
    for j, side in product(AXES, (0, 1)):
        aa, ab, ba, bb = oriented_cut(colors, j, side)
        k = len(ab) - len(aa)
        if k in (2, 3, 4) and len(aa) <= 5:
            assert all(not controlled_count(ab, ba, bb, i) for i in AXES if i != j)
        if (k, len(aa), len(bb)) == (2, 3, 3):
            for i, half in product(AXES, (0, 1)):
                if i != j:
                    counts = [sum(bit_is_one(v, i) == half for v in group)
                              for group in (bb, ba, ab)]
                    assert not central_column_hit(*counts)
    return axes


def probe(a):
    start = perf_counter()
    model, hole = build_hole_model(a)
    prior_menu = add_menu(model, hole)
    old_coverage = add_old_coverage(model, hole)
    error = model.validate()
    if error:
        raise ValueError(error)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = LIMIT_SECONDS
    solver.parameters.num_search_workers = WORKERS
    solver.parameters.random_seed = SEED
    print(f"a={a}: model validated after {perf_counter()-start:.3f}s", flush=True)
    status = solver.solve(model)
    result = dict(a=a, b=7-a, status=solver.status_name(status),
                  wall_seconds=solver.wall_time, conflicts=solver.num_conflicts,
                  branches=solver.num_branches, matching_calls=0,
                  prior_menu=prior_menu, added_old_coverage=old_coverage,
                  model_stats=model.model_stats(), response_stats=solver.response_stats())
    if status == cp_model.INFEASIBLE:
        path = HERE / f"EDGE_LOW_GAP_A{a}.pb"
        assert model.export_to_file(str(path))
        result.update(model_file=path.name, model_sha256=sha256(path.read_bytes()).hexdigest())
    elif status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        holes = {v for v in VERTICES if solver.value(hole[v])}
        axes = validate_sat(a, holes)
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
    output = dict(
        scope="EDGE_MENU_PROBE plus the three noncentral gap-two and monochromatic gap-three E16 types and controlled cycle counts k=2,3,4 and the five central gap-two column gates",
        conditional_assumption="Central gap-one exclusion and the previous menu for s=3 depend on the new Q6 A8 interface.",
        audits={
            "gap2_two_holes": "R7_E16_TWO_HOLE_FACE_FULL_CLOSURE_REVIEW.md",
            "gap2_four_holes": "R7_E16_INITIAL_REDUCTION_REVIEW.md",
            "gap2_six_holes": "R7_SIX_HOLE_RECEIVER_MULTI_LAYER_REVIEW.md",
            "gap3_monochromatic": "R7_E16_THREE_MONOCHROMATIC_CLOSURE_REVIEW.md",
            "controlled_cycle": "R7_MU3_CONTROLLED_AND_T63_REVIEW.md",
            "central_gap2": "R7_CENTRAL_JOINT_COLUMN_ALPHABET.md; audits F02–F03 and TWO_MAJORITY_ROOTS_AVOID_TWO",
        },
        exclusions_not_used="R41 and gap-seven/eight macros tied to minimum imbalance three",
        code_sha256={name: sha256((HERE / name).read_bytes()).hexdigest()
                     for name in ("EDGE_PROBE.py", "EDGE_MENU_PROBE.py", Path(__file__).name)},
        cp_model_calls=0, max_seconds_per_call=LIMIT_SECONDS, num_search_workers=WORKERS,
        ortools_version=ortools.__version__, seed=SEED, results=[],
    )
    output_path = Path(__file__).with_suffix(".json")
    for a in (0, 1):
        output["results"].append(probe(a))
        output["cp_model_calls"] += 1
        output_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
