"""Check one saved quotient against the generalized pentagon obstruction.

This reads one 12x12 matrix. It runs no graph search, lift or solver.
"""
import json
from pathlib import Path
import time


def main():
    cpu, wall = time.process_time(), time.monotonic()
    base = Path(__file__).resolve().parent
    source = base / "cyclic5_full60_quotient_escape_run/best_quotient.json"
    data = json.loads(source.read_text())
    m = data["matrix"]
    assert len(m) == 12 and all(len(row) == 12 for row in m)
    assert all(m[i][j] == m[j][i] for i in range(12) for j in range(12))
    assert all(sum(row) == 8 for row in m)
    d = [[sum(m[i][k] * m[k][j] for k in range(12)) + m[i][j]
          - 7 * (i == j) - 5 for j in range(12)] for i in range(12)]
    assert d == data["defect"]
    assert all(x >= 0 for row in d for x in row)
    assert all(sum(row) == 5 for row in d)
    parts = ([0, 4, 6, 7, 10, 11], [1, 2, 3, 5, 8, 9])
    cycles = ([0, 4, 7, 10, 6], [1, 3, 2, 8, 5])
    isolated = (11, 9)
    assert sorted(parts[0] + parts[1]) == list(range(12))
    assert all(d[a][b] == 0 for a in parts[0] for b in parts[1])
    records = []
    for part, cycle, isolate in zip(parts, cycles, isolated):
        expected = {(a, b): 0 for a in part for b in part}
        expected[isolate, isolate] = 2
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            expected[a, b] = expected[b, a] = 1
        assert all(m[a][b] == expected[a, b] for a in part for b in part)
        internal = [sum(m[a][b] for b in part) for a in part]
        assert internal == [2] * 6
        records.append(dict(labels=part, unit_cycle=cycle,
                            diagonal_two_isolate=isolate,
                            internal_matrix=[[m[a][b] for b in part] for a in part],
                            within_half_degrees=internal,
                            cross_half_degrees=[8 - x for x in internal]))
    result = dict(
        source=source.name,
        checked_matrix_count=1,
        stored_defect_matches_direct_matrix_product=True,
        quotient_row_sums=[sum(row) for row in m],
        defect_row_sums=[sum(row) for row in d],
        defect_diagonal=[d[i][i] for i in range(12)],
        cross_defect_block=[[d[a][b] for b in parts[1]] for a in parts[0]],
        halves=records,
        generalized_pentagon_obstruction_matches=True,
        former_two_k6_defect_condition_matches=False,
        conclusion="No diameter-two free-C5 lift by the generalized structural corollary",
        solver_calls=0, voltage_assignments=0, graph_distance_runs=0,
        cpu_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall)
    assert any(result["defect_diagonal"])
    out = source.with_name("best_quotient.pentagon_obstruction.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
