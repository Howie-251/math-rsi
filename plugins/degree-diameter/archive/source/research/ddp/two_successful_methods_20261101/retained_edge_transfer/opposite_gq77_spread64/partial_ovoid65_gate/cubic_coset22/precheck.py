#!/usr/bin/env python3
"""One fixed three-coset partial-ovoid check; no graph/edge-file/BFS."""
import datetime
import itertools
import json
from pathlib import Path
import resource
import time

OUT = Path(__file__).resolve().parent
SOURCE = OUT.parent.parent


def read(path):
    return json.loads(path.read_text())


def B(x, y):
    return (x[0]*y[2] + 3*x[1]*y[3] - x[2]*y[0] - 3*x[3]*y[1]) % 7


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
    start = time.process_time()
    pred = read(OUT / "PRED.json")
    assert not (OUT / "PRECHECK_RESULT.json").exists(), "one fixed check only"
    data = read(SOURCE / "PARAMETERS.json")
    accepted = read(SOURCE / "RESULT.json")
    steps = read(SOURCE / "EXTENSION_STEPS.json")["steps"]
    points = [tuple(p) for p in data["points"]]
    lines = [r["points"] for r in data["lines"]]
    through = data["point_incident_lines"]
    spread = data["spread_line_labels"]
    owner = data["point_spread_owner"]
    assert accepted["n"] == 160050 and accepted["m"] == 5121600
    assert accepted["degree_histogram"] == {"64": 160050}
    assert len(points) == len(lines) == len(through) == 400
    assert len(spread) == len(set(spread)) == len(steps) == 50
    words = list(map(int, (SOURCE / "TABLES_INPUT.txt").read_text().split()))
    assert words == ([400,8,50] + [p for row in lines for p in row]
                     + [l for row in through for l in row] + spread + owner)
    assert sorted(p for l in spread for p in lines[l]) == list(range(400))
    assert all(p in lines[spread[owner[p]]] for p in range(400))
    for j, step in enumerate(steps):
        pins = [400*p+l for p in lines[spread[j]] for l in through[p]]
        assert step["step"] == j and step["new_vertex"] == 160000+j
        assert step["spread_line"] == spread[j] and step["pins"] == pins
    O = [tuple(p) for p in pred["candidate_points_mod7"]]
    assert len(O) == len(set(O)) == 22
    matrix = [[B(x,y) for y in O] for x in O]
    assert all(matrix[i][j] != 0 for i in range(22) for j in range(i))
    labels = list(itertools.product([0,2,4], range(7)))
    assert {pow(t,3,7) for t in range(7)} == {0,1,6}
    assert {(l-k)%7 for k,l in itertools.permutations([0,2,4],2)} == {2,3,4,5}
    for i,(k,s) in enumerate(labels):
        for j,(l,t) in enumerate(labels):
            assert matrix[i][j] == (pow(t-s,3,7)+l-k)%7
        assert matrix[i][21] == 1
    pid = {p:i for i,p in enumerate(points)}
    ids = [pid[p] for p in O]
    counts = [sum(p in line for p in ids) for line in lines]
    assert counts.count(1) == 176 and counts.count(0) == 224
    assert len({owner[p] for p in ids}) == 22
    centers = []
    neighborhoods = []
    bridges = []
    loads = {}
    for i,p in enumerate(ids):
        for j,l in enumerate(spread):
            c = 400*p+l
            ns = {400*q+m for q in lines[l] for m in through[p]}
            assert len(ns) == 64
            flag = c in ns
            ns.discard(c)
            if flag:
                assert j == owner[p] and c in steps[j]["pins"]
                ns.add(160000+j)
                bridges.append({"point_index":i,"point_id":p,"spread_index":j,
                                "spread_line":l,"center":c,"source_bonus":160000+j})
            assert len(ns) == 64
            for v in ns:
                loads[v] = loads.get(v,0)+1
            centers.append({"index":50*i+j,"point_index":i,"point_id":p,
                            "spread_index":j,"spread_line":l,"center":c,
                            "source_degree":len(ns),"flag":flag})
            neighborhoods.append(ns)
    center_set = {r["center"] for r in centers}
    assert len(centers) == len(center_set) == len(neighborhoods) == 1100
    intersection_count = sum(bool(x&y) for x,y in itertools.combinations(neighborhoods,2))
    assert intersection_count == 0 and len(loads) == 70400 and max(loads.values()) == 1
    assert len(bridges) == sum(v >= 160000 for v in loads) == 22
    induced_directed = sum(len(ns&center_set) for ns in neighborhoods)
    assert induced_directed == 462
    assert all(len(ns&center_set) <= 1 for ns in neighborhoods)
    result = {
        "status":"PASS_FIXED_CUBIC_COSET22_IMMUTABLE_SOURCE_PACKING",
        "finished_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "points_mod7":O,"point_ids":ids,"point_spread_owners":[owner[p] for p in ids],
        "B_matrix":matrix,"distinct_pair_B_nonzero_checks":231,
        "cubic_coset_identity_checks":441,"infinity_pair_checks":21,
        "cubes_mod7":[0,1,6],"nonzero_offset_differences":[2,3,4,5],
        "GQ_line_intersection_histogram":{"0":224,"1":176},
        "source_tables_equal_frozen_production_input":True,
        "actual_bonus_steps_equal_geometry_pins":50,
        "centers":1100,"source_neighbor_sizes":{"64":1100},
        "neighborhood_pair_intersections_checked":604450,
        "nonempty_neighborhood_intersections":intersection_count,
        "load_max":1,"distinct_source_neighbors":70400,
        "source_original_neighbors":70378,"source_bonus_neighbors":22,
        "flag_center_bonus_bridges":bridges,
        "centers_induced_edges":231,
        "centers_induced_components":{"K2":231,"isolated":638},
        "conditional_target":pred["conditional_graph_prediction"],
        "candidate_graph_generated":False,"source_edgefile_read":False,
        "BFS_calls":0,"Lean_compilations":0,"solver_calls":0,
        "workers":1,"CPU_seconds":time.process_time()-start,"CPU_budget_seconds":5,
        "public_gate":"ROOT_SEPARATE_PRIMARY_REVIEW_PENDING",
        "next":"Return finite PASS; no graph production or continuation without root decision."
    }
    (OUT/"CENTERS.json").write_text(json.dumps(centers,indent=2)+"\n")
    (OUT/"PRECHECK_RESULT.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["status","point_ids","centers",
          "distinct_source_neighbors","source_bonus_neighbors","CPU_seconds"]}))


if __name__ == "__main__":
    main()
