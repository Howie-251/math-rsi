#!/usr/bin/env python3
"""One fixed ten-point precheck. No edge file, graph, BFS, solver or Lean."""
import datetime
import itertools
import json
from pathlib import Path
import resource
import time

OUT = Path(__file__).resolve().parent
SOURCE = OUT.parent


def read(path):
    return json.loads(path.read_text())


def B(x, y):
    return (x[0] * y[2] + 3 * x[1] * y[3]
            - x[2] * y[0] - 3 * x[3] * y[1]) % 7


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    start = time.process_time()
    pred = read(OUT / "PRED.json")
    assert not (OUT / "PRECHECK_RESULT.json").exists(), "one fixed precheck only"
    data = read(SOURCE / "PARAMETERS.json")
    accepted = read(SOURCE / "RESULT.json")
    extension = read(SOURCE / "EXTENSION_STEPS.json")
    points = [tuple(x) for x in data["points"]]
    line_points = [r["points"] for r in data["lines"]]
    point_lines = data["point_incident_lines"]
    spread = data["spread_line_labels"]
    owner = data["point_spread_owner"]
    assert len(points) == len(line_points) == len(point_lines) == 400
    assert len(spread) == len(set(spread)) == 50
    assert accepted["n"] == 160050 and accepted["m"] == 5121600
    assert accepted["degree_histogram"] == {"64": 160050}
    # Bind exactly the frozen production input arrays, without reading edges.
    words = list(map(int, (SOURCE / "TABLES_INPUT.txt").read_text().split()))
    expected = ([400, 8, 50] + [p for row in line_points for p in row]
                + [l for row in point_lines for l in row] + spread + owner)
    assert words == expected
    assert all(len(row) == len(set(row)) == 8 for row in line_points)
    assert all(len(row) == len(set(row)) == 8 for row in point_lines)
    assert all(p in line_points[l] for p in range(400) for l in point_lines[p])
    assert all(l in point_lines[p] for l in range(400) for p in line_points[l])
    assert sorted(p for l in spread for p in line_points[l]) == list(range(400))
    assert all(p in line_points[spread[owner[p]]] for p in range(400))
    steps = extension["steps"]
    assert len(steps) == 50
    for j, step in enumerate(steps):
        pins = [400 * p + l for p in line_points[spread[j]] for l in point_lines[p]]
        assert step["step"] == j and step["new_vertex"] == 160000 + j
        assert step["spread_line"] == spread[j] and step["pins"] == pins
    # Only the one proposed point set is considered.
    O = [tuple(x) for x in pred["candidate_points_mod7"]]
    assert len(O) == len(set(O)) == 10
    point_id = {p: i for i, p in enumerate(points)}
    ids = [point_id[p] for p in O]
    matrix = [[B(x, y) for y in O] for x in O]
    assert all(matrix[i][j] != 0 for i in range(10) for j in range(i))
    for s, t in itertools.product(range(7), repeat=2):
        assert B(O[s], O[t]) == pow(t - s, 3, 7)
    a_poly = [(6 + 5 * t - t**3) % 7 for t in range(7)]
    b_poly = [(1 + 5 * t - t**3) % 7 for t in range(7)]
    assert a_poly == [B(O[t], O[8]) for t in range(7)] and 0 not in a_poly
    assert b_poly == [B(O[t], O[9]) for t in range(7)] and 0 not in b_poly
    counts = [sum(p in row for p in ids) for row in line_points]
    assert max(counts) == 1 and counts.count(1) == 80
    # This is exactly hO and hS in OvoidSpreadCloneCapacity, without existence.
    assert len({owner[p] for p in ids}) == 10
    center_rows = []
    neighborhoods = []
    flag_bridges = []
    load = {}
    for i, p in enumerate(ids):
        for j, l in enumerate(spread):
            center = 400 * p + l
            neighbors = {400 * q + m for q in line_points[l] for m in point_lines[p]}
            assert len(neighbors) == 64
            flag = center in neighbors
            neighbors.discard(center)
            if flag:
                assert j == owner[p]
                assert center in steps[j]["pins"]
                neighbors.add(160000 + j)
                flag_bridges.append({"point_index": i, "point_id": p,
                                     "spread_index": j, "spread_line": l,
                                     "center": center, "source_bonus": 160000 + j})
            assert len(neighbors) == 64
            for v in neighbors:
                load[v] = load.get(v, 0) + 1
            neighborhoods.append(neighbors)
            center_rows.append({"index": 50 * i + j, "point_index": i,
                                "point_id": p, "spread_index": j,
                                "spread_line": l, "center": center,
                                "source_degree": len(neighbors), "flag": flag})
    centers = {r["center"] for r in center_rows}
    assert len(centers) == len(neighborhoods) == 500
    # Direct finite check of all 124750 pairs, in addition to the load test.
    intersections = sum(bool(x & y) for x, y in itertools.combinations(neighborhoods, 2))
    assert intersections == 0 and len(load) == 32000 and max(load.values()) == 1
    assert len(flag_bridges) == 10
    assert sum(v >= 160000 for v in load) == 10
    induced_edges = sorted((r["center"], v)
                           for r, ns in zip(center_rows, neighborhoods)
                           for v in ns & centers if r["center"] < v)
    assert len(induced_edges) == 45
    result = {
        "status": "PASS_ONE_FIXED_PARTIAL_OVOID_AND_IMMUTABLE_SOURCE_PACKING",
        "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "points_mod7": O, "point_ids": ids, "point_spread_owners": [owner[p] for p in ids],
        "B_matrix": matrix, "distinct_pair_B_nonzero_checks": 45,
        "twisted_cubic_identity_checks": 49,
        "extra_a_polynomial_values": a_poly, "extra_b_polynomial_values": b_poly,
        "GQ_line_intersection_histogram": {"0": counts.count(0), "1": counts.count(1)},
        "complete_ovoid": False,
        "source_tables_equal_frozen_production_input": True,
        "actual_bonus_steps_equal_geometry_pins": 50,
        "centers": 500, "source_neighbor_sizes": {"64": 500},
        "neighborhood_pair_intersections_checked": 124750,
        "nonempty_neighborhood_intersections": intersections,
        "load_max": 1, "distinct_source_neighbors": 32000,
        "source_original_neighbors": 31990, "source_bonus_neighbors": 10,
        "flag_center_bonus_bridges": flag_bridges,
        "centers_induced_edges": len(induced_edges),
        "centers_induced_components": {"K2": 45, "isolated": 410},
        "conditional_target": pred["conditional_graph_prediction"],
        "candidate_graph_generated": False, "source_edgefile_read": False,
        "BFS_calls": 0, "Lean_compilations": 0, "solver_calls": 0,
        "workers": 1, "CPU_seconds": time.process_time() - start,
        "CPU_budget_seconds": 30,
        "public_gate": "SEPARATE_PRIMARY_REVIEW_PENDING",
        "next": "Do not generate graph; await public65 gate and root decision."
    }
    (OUT / "CENTERS.json").write_text(json.dumps(center_rows, indent=2) + "\n")
    (OUT / "PRECHECK_RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "point_ids", "centers",
          "distinct_source_neighbors", "source_bonus_neighbors", "CPU_seconds"]}))


if __name__ == "__main__":
    main()
