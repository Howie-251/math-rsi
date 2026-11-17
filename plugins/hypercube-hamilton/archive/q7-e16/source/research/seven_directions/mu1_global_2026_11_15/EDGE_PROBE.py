"""Bounded E16 edge-cut hole feasibility, with an independent matching check."""

import json
import time
from pathlib import Path

import ortools
from ortools.sat.python import cp_model


DIMENSION = 7
OUTER = 6
LIMIT_SECONDS = 60
SEED = 20261115
VERTICES = tuple(range(1 << DIMENSION))
ALPHA = tuple(v for v in VERTICES if v.bit_count() % 2)
BETA = tuple(v for v in VERTICES if v.bit_count() % 2 == 0)
A_ALPHA = tuple(v for v in ALPHA if v < (1 << OUTER))
A_BETA = tuple(v for v in BETA if v < (1 << OUTER))
B_ALPHA = tuple(v for v in ALPHA if v >= (1 << OUTER))
B_BETA = tuple(v for v in BETA if v >= (1 << OUTER))
EDGES = tuple((u, u ^ (1 << j)) for u in ALPHA for j in range(DIMENSION))
FORBIDDEN_LARGE_FACE_DIFFERENCES = {-1, 0, 1, 2}


def bit_is_one(v, axis):
    return v & (1 << axis) != 0


def admissible_global_counts(alpha, beta):
    gap = abs(alpha - beta)
    smaller_minority = min(alpha, beta, 8 - alpha, 8 - beta)
    return gap >= 2 or (gap == 1 and smaller_minority <= 1)


def build_hole_model(a):
    model = cp_model.CpModel()
    hole = [model.new_bool_var(f"hole_{v}") for v in VERTICES]
    for side, count in (
        (A_ALPHA, a),
        (A_BETA, a + 1),
        (B_ALPHA, 8 - a),
        (B_BETA, 7 - a),
    ):
        model.add(sum(hole[v] for v in side) == count)
    model.add(hole[0] == 1)

    for u, v in EDGES:
        model.add(hole[u] + hole[v] <= 1)

    allowed_counts = [
        (alpha, beta)
        for alpha in range(9)
        for beta in range(9)
        if admissible_global_counts(alpha, beta)
    ]
    for j in range(DIMENSION):
        alpha = model.new_int_var(0, 8, f"global_alpha_{j}")
        beta = model.new_int_var(0, 8, f"global_beta_{j}")
        model.add(alpha == sum(hole[v] for v in ALPHA if bit_is_one(v, j)))
        model.add(beta == sum(hole[v] for v in BETA if bit_is_one(v, j)))
        model.add_allowed_assignments([alpha, beta], allowed_counts)

        if j != OUTER:
            large_alpha = sum(hole[v] for v in B_ALPHA if bit_is_one(v, j))
            large_beta = sum(hole[v] for v in B_BETA if bit_is_one(v, j))
            allowed_differences = cp_model.Domain.from_intervals([[-8, -2], [3, 8]])
            model.add_linear_expression_in_domain(
                large_alpha - large_beta, allowed_differences
            )

    return model, hole


def short_maximum_matching(holes):
    """Augment along short edges only, without another CP call."""
    odd_vertices = [u for u in ALPHA if u not in holes]
    neighbors = {
        u: [u ^ (1 << j) for j in range(DIMENSION) if (u ^ (1 << j)) not in holes]
        for u in odd_vertices
    }
    odd_mate_of_even = {}

    def augment(u, seen_even):
        for v in neighbors[u]:
            if v in seen_even:
                continue
            seen_even.add(v)
            previous = odd_mate_of_even.get(v)
            if previous is None or augment(previous, seen_even):
                odd_mate_of_even[v] = u
                return True
        return False

    for u in sorted(odd_vertices, key=lambda vertex: (len(neighbors[vertex]), vertex)):
        augment(u, set())
    return sorted((u, v) for v, u in odd_mate_of_even.items())


def check_holes(a, holes):
    assert 0 in holes
    assert tuple(len(holes.intersection(side)) for side in (A_ALPHA, A_BETA, B_ALPHA, B_BETA)) == (
        a, a + 1, 8 - a, 7 - a
    )
    assert not any(u in holes and v in holes for u, v in EDGES)
    axes = []
    for j in range(DIMENSION):
        alpha = sum(v in holes and bit_is_one(v, j) for v in ALPHA)
        beta = sum(v in holes and bit_is_one(v, j) for v in BETA)
        assert admissible_global_counts(alpha, beta)
        row = {"axis": j, "alpha": alpha, "beta": beta, "delta": alpha - beta}
        if j != OUTER:
            large_alpha = sum(v in holes and bit_is_one(v, j) for v in B_ALPHA)
            large_beta = sum(v in holes and bit_is_one(v, j) for v in B_BETA)
            large_delta = large_alpha - large_beta
            assert large_delta not in FORBIDDEN_LARGE_FACE_DIFFERENCES
            row["large_face_deltas"] = [1 - large_delta, large_delta]
        axes.append(row)
    assert min(abs(row["delta"]) for row in axes) == 1
    return axes


def check_matching(holes, matching):
    endpoints = [endpoint for edge in matching for endpoint in edge]
    assert len(set(endpoints)) == len(endpoints)
    assert set(endpoints).isdisjoint(holes)
    assert all((u ^ v).bit_count() == 1 for u, v in matching)
    if len(matching) == 56:
        assert set(endpoints) == set(VERTICES) - holes
        return True
    return False


def probe(a):
    model, variables = build_hole_model(a)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = LIMIT_SECONDS
    solver.parameters.num_search_workers = 1
    solver.parameters.random_seed = SEED
    start = time.perf_counter()
    status = solver.solve(model)
    result = {
        "a": a,
        "b": 7 - a,
        "cp_status": solver.status_name(status),
        "elapsed_seconds": time.perf_counter() - start,
        "cp_wall_seconds": solver.wall_time,
        "cp_conflicts": solver.num_conflicts,
        "cp_branches": solver.num_branches,
        "matching_calls": 0,
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        holes = {v for v in VERTICES if solver.value(variables[v])}
        axes = check_holes(a, holes)
        matching = short_maximum_matching(holes)
        realized = check_matching(holes, matching)
        result.update({
            "axes": axes,
            "holes_alpha_odd": sorted(holes.intersection(ALPHA)),
            "holes_beta_even": sorted(holes.intersection(BETA)),
            "matching_calls": 1,
            "matching_size": len(matching),
            "realized_by_short_matching": realized,
            "short_matching": matching,
        })
    return result


def main():
    results = [probe(a) for a in (0, 1)]
    output = {
        "purpose": "diagnostic of the E16 edge-cut domain after conditionally excluding central gap one",
        "conditional_filter": "Excludes gap-one (a'=3) as if Q6 A8 were established. It is currently open.",
        "global_filters": "independent 8+8 holes, gap minimum one, all gap-one cuts have normalized a'<=1",
        "local_filter": "bit 6 is outer; 0 is a beta hole in its zero face; large-face imbalance is never -1,0,1,2 on a bit-one inner half",
        "status_meaning": "CP is feasibility for holes only. A witness requires a verified 56-edge short matching. CP INFEASIBLE is diagnostic without a proof certificate.",
        "cp_calls": len(results),
        "max_seconds_per_cp_call": LIMIT_SECONDS,
        "seed": SEED,
        "ortools_version": ortools.__version__,
        "results": results,
    }
    output_path = Path(__file__).with_suffix(".json")
    output_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    for result in results:
        print(f"a={result['a']} cp={result['cp_status']} seconds={result['elapsed_seconds']:.3f} matching={result.get('matching_size')}", flush=True)


if __name__ == "__main__":
    main()
