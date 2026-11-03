"""One exact necessary-quotient check for arbitrary order61 targets.

Enumerate all 3x3 nonnegative integer Q with row sums 8. This does not
assume a simple defect graph, CP02 types, or any historical SAT result.
"""
from itertools import product
from pathlib import Path
import json
import time


def main():
    cpu, wall = time.process_time(), time.monotonic()
    rows = [(a, b, 8-a-b) for a in range(9) for b in range(9-a)]
    assert len(rows) == 45
    counts = dict(all_labeled_matrices=0, trace_seven=0,
                  positive_component_identity=0, balance=0,
                  size_and_handshake=0)
    survivors = []
    for q in product(rows, repeat=3):
        counts["all_labeled_matrices"] += 1
        if sum(q[i][i] for i in range(3)) != 7:
            continue
        counts["trace_seven"] += 1
        p = [[sum(q[i][k]*q[k][j] for k in range(3)) + q[i][j]
              - 11*(i == j) for j in range(3)] for i in range(3)]
        n = p[0]
        if not (min(n) >= 2 and sum(n) == 61 and p[1] == n and p[2] == n):
            continue
        counts["positive_component_identity"] += 1
        if any(n[i]*q[i][j] != n[j]*q[j][i]
               for i in range(3) for j in range(3)):
            continue
        counts["balance"] += 1
        if any(q[i][i] >= n[i] or (n[i]*q[i][i]) % 2 for i in range(3)):
            continue
        counts["size_and_handshake"] += 1
        survivors.append(dict(component_sizes=n, quotient=q))
    assert counts["all_labeled_matrices"] == 45**3 == 91125
    result = dict(scope="Exactly three support components of the actual weighted defect B in an arbitrary order61 target",
                  rows=45, complete=True, counts=counts,
                  all_labeled_survivors=survivors,
                  solver_calls=0, graph_searches=0,
                  cpu_seconds=time.process_time()-cpu,
                  wall_seconds=time.monotonic()-wall)
    output = Path(__file__).with_name("component_quotient_three.result.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
