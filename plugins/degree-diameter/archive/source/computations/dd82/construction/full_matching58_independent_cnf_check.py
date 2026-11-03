"""Read-only input check from edges and DIMACS; no generator imports or BFS."""
from itertools import combinations
from pathlib import Path
import json
import time


def main():
    cpu, wall = time.process_time(), time.monotonic()
    base = Path(__file__).resolve().parent
    run = base / "full_matching58_run"
    rows = [tuple(map(int, s.split())) for s in (run / "seed.edges").read_text().splitlines()]
    assert rows[0] == (58, 232)
    edges = set(rows[1:])
    assert len(edges) == len(rows) - 1 == 232
    assert all(0 <= u < v < 58 for u, v in edges)
    neighbours = [set() for _ in range(58)]
    for u, v in edges:
        neighbours[u].add(v)
        neighbours[v].add(u)
    assert {len(row) for row in neighbours} == {8}
    fibres = [list(range(10 + 6*i, 16 + 6*i)) for i in range(8)]
    scaffold = {(t, s) for t in (0, 1) for s in range(2, 10)}
    scaffold |= {(2+i, x) for i in range(8) for x in fibres[i]}
    assert scaffold <= edges
    rebuilt = set(scaffold)
    matches = []
    for i, j in combinations(range(8), 2):
        p = []
        for u in fibres[i]:
            targets = neighbours[u].intersection(fibres[j])
            assert len(targets) == 1
            v = targets.pop()
            p.append(v - fibres[j][0])
            rebuilt.add((u, v))
        assert sorted(p) == list(range(6))
        if i == 0:
            assert p == list(range(6))
        matches.append({"i": i, "j": j, "permutation": p})
    assert rebuilt == edges

    meta = json.loads((run / "variables.json").read_text())
    edge_map, values = {}, {}
    for i, a, j, b, u, v, q in meta["edge_variables"]:
        assert 0 <= i < j < 8 and 0 <= a < 6 and 0 <= b < 6
        assert (u, v) == (fibres[i][a], fibres[j][b])
        assert (i, a, j, b) not in edge_map and q not in values
        edge_map[i, a, j, b] = q
        values[q] = (u, v) in edges
    assert len(edge_map) == 1008
    assert set(values) == set(range(1, 1009))

    def var(i, a, j, b):
        return edge_map[i, a, j, b] if i < j else edge_map[j, b, i, a]

    gates = {}
    for q, p, r in meta["and_variables"]:
        assert q not in values and p in values and r in values
        assert p <= 1008 and r <= 1008
        values[q] = values[p] and values[r]
        gates[q] = (p, r)
    assert len(gates) == 36288
    assert set(values) == set(range(1, 37297))

    coverage = json.loads((run / "coverage.json").read_text())
    by_pair, by_clause = {}, {}
    used_gates = set()
    for item in coverage:
        i, a, j, b = item["coordinates"]
        assert item["pair"] == [fibres[i][a], fibres[j][b]]
        assert (i, a, j, b) not in by_pair
        assert item["clause_id"] not in by_clause
        assert item["direct"] == var(i, a, j, b)
        expected_routes = [(var(i, a, k, c), var(k, c, j, b))
                           for k in range(8) if k != i and k != j for c in range(6)]
        assert [gates[q] for q in item["paths"]] == expected_routes
        assert len(set(item["paths"])) == 36
        assert not used_gates.intersection(item["paths"])
        used_gates.update(item["paths"])
        by_pair[i, a, j, b] = item
        by_clause[item["clause_id"]] = item
    assert len(by_pair) == 1008 and used_gates == set(gates)

    expected = []
    for i, j in combinations(range(8), 2):
        lists = [[var(i, a, j, b) for b in range(6)] for a in range(6)]
        lists += [[var(i, a, j, b) for a in range(6)] for b in range(6)]
        for entries in lists:
            expected.append(tuple(entries))
            expected.extend((-p, -q) for p, q in combinations(entries, 2))
    assert len(expected) == 5376
    for j in range(1, 8):
        for a in range(6):
            for b in range(6):
                q = var(0, a, j, b)
                expected.append((q if a == b else -q,))
    assert len(expected) == 5628
    for i, j in combinations(range(8), 2):
        for a in range(6):
            for b in range(6):
                item = by_pair[i, a, j, b]
                for q in item["paths"]:
                    p, r = gates[q]
                    expected.extend([(-q, p), (-q, r), (q, -p, -r)])
                expected.append(tuple([item["direct"]] + item["paths"]))
                assert item["clause_id"] == len(expected)
    assert len(expected) == 115500

    false_ids = []
    count = 0
    with (run / "input.cnf").open() as source:
        for line in source:
            if line.startswith("c") or not line.strip():
                continue
            if line.startswith("p"):
                assert line.split() == ["p", "cnf", "37296", "115500"]
                continue
            entries = list(map(int, line.split()))
            assert entries[-1] == 0
            clause = tuple(entries[:-1])
            assert clause == expected[count]
            count += 1
            if not any(values[abs(q)] == (q > 0) for q in clause):
                false_ids.append(count)
    assert count == len(expected)
    assert all(q in by_clause for q in false_ids)
    false_pairs = sorted(by_clause[q]["pair"] for q in false_ids)
    assert len(false_ids) == 105

    saved_values = {}
    for token in (run / "seed.assignment.txt").read_text().split():
        if token == "v" or token == "0":
            continue
        q = int(token)
        assert abs(q) not in saved_values
        saved_values[abs(q)] = q > 0
    assert saved_values == values
    old = base / "false_twins58_f9_coverage_run"
    old_rows = [tuple(map(int, s.split())) for s in (old / "candidate.best.edges").read_text().splitlines()]
    assert old_rows[0] == (58, 232) and set(old_rows[1:]) == edges
    bfs = json.loads((old / "independent_bfs.json").read_text())
    assert false_pairs == sorted(item["pair"] for item in bfs["bad_pairs"])
    original = json.loads((run / "seed.cnf_check.json").read_text())
    assert false_ids == original["false_clause_ids"]
    assert false_pairs == sorted(original["false_pairs"])
    result = dict(
        parent_run_id="dd82-v3-f9-c7-20261013-0749",
        scope="Source/input/seed consistency for the full false-twin58 CNF; no SAT decision",
        imports_from_generator=False, solver_calls=0, new_bfs_runs=0,
        vertex_count=58, edge_count=232, all_degrees_eight=True,
        reconstructed_matching_blocks=matches, root_interfaces_identity=True,
        variables=37296, clauses=115500,
        actual_dimacs_equals_full_expected_clause_sequence=True,
        actual_gate_geometry_checked=True,
        independent_assignment_equals_saved_assignment=True,
        seed_edges_equal_previously_bfs_checked_graph=True,
        false_clause_count=len(false_ids), false_clause_ids=false_ids,
        false_pairs=false_pairs, all_false_clauses_are_coverage=True,
        exact_match_to_previous_independent_bfs=True,
        cpu_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall,
        review_independence="same-family", acceptance_status="provisional")
    (run / "independent_cnf_check.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items()
                     if k not in {"reconstructed_matching_blocks", "false_clause_ids", "false_pairs"}}))


if __name__ == "__main__":
    main()
