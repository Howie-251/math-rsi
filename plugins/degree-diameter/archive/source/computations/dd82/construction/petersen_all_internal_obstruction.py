"""Read-only route obstruction with all six internal cubic graphs free.

No graph search, CNF generation, or solver call.  Each cross-fiber row has
five immutable slots (one matching edge and four matching compositions).
The two arbitrary internal cubic graphs can supply only six more slots.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "computations/dd82/construction/petersen_four_fiber_reassembly_run/seed.json"
OUT = ROOT / "computations/dd82/construction/petersen_all_internal_completion_run"


def dump(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def main():
    wall_start, cpu_start = time.monotonic(), time.process_time()
    OUT.mkdir(exist_ok=True)
    source = json.loads(SOURCE.read_text())
    edges = {tuple(sorted(e)) for e in source["edges"]}
    assert source["n"] == 60 and len(edges) == 240
    ns = [set() for _ in range(60)]
    for u, v in edges:
        assert 0 <= u < v < 60
        ns[u].add(v)
        ns[v].add(u)
    fibers = [set(range(10*i, 10*i+10)) for i in range(6)]
    match = {}
    for i in range(6):
        for u in sorted(fibers[i]):
            assert len(ns[u]) == 8 and len(ns[u] & fibers[i]) == 3
        for j in range(6):
            if i == j:
                continue
            match[i, j] = {}
            for u in sorted(fibers[i]):
                targets = ns[u] & fibers[j]
                assert len(targets) == 1
                match[i, j][u] = next(iter(targets))
            assert set(match[i, j].values()) == fibers[j]

    rows = []
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            for u in sorted(fibers[i]):
                routes = [[u, match[i, j][u]]]
                for k in range(6):
                    if k not in (i, j):
                        w = match[i, k][u]
                        routes.append([u, w, match[k, j][w]])
                assert len(routes) == 5
                for path in routes:
                    assert all(tuple(sorted((a, b))) in edges
                               and a//10 != b//10
                               for a, b in zip(path, path[1:]))
                counts = Counter(path[-1] for path in routes)
                surplus = 5 - len(counts)
                assert surplus == sum(max(0, n-1) for n in counts.values())
                rows.append(dict(source_fiber=i, target_fiber=j, source=u,
                                 fixed_paths=routes,
                                 counts=[counts[v] for v in sorted(fibers[j])],
                                 distinct_targets=sorted(counts),
                                 fixed_surplus=surplus,
                                 maximum_covered_with_internal_cubic=min(10, len(counts)+6),
                                 unavoidable_bad_pairs=max(0, surplus-1)))
    assert len(rows) == 300
    violations = [r for r in rows if r["unavoidable_bad_pairs"]]
    assert violations, "This input no longer has the saved direct obstruction."
    strongest = min(violations, key=lambda r: (-r["fixed_surplus"], r["source"], r["target_fiber"]))

    blocks = []
    for i, j in combinations(range(6), 2):
        sums = [sum(r["unavoidable_bad_pairs"] for r in rows
                    if r["source_fiber"] == a and r["target_fiber"] == b)
                for a, b in ((i,j), (j,i))]
        blocks.append(dict(fibers=[i,j], directed_bad_pair_lower_bounds=sums,
                           bad_pair_lower_bound=max(sums)))

    report = dict(
        status="ANALYTICALLY_OBSTRUCTED_BEFORE_CNF",
        source=str(SOURCE.relative_to(ROOT)),
        scope="All fifteen external matchings fixed to the saved 97-bad-pair seed; all six internal graphs independently arbitrary simple cubic graphs on their ten vertices. This includes all labeled Petersen choices.",
        directed_rows_checked=len(rows),
        fixed_surplus_histogram=dict(sorted(Counter(r["fixed_surplus"] for r in rows).items())),
        violating_directed_rows=len(violations),
        strongest_witness=strongest,
        block_lower_bounds=blocks,
        total_bad_pair_lower_bound=sum(b["bad_pair_lower_bound"] for b in blocks),
        all_violating_rows=violations,
        cnf_generated=False, solver_calls=0, solver_cpu_seconds=0,
        all_six_internal_graphs_free=True,
        graph_enumerations=0,
        bfs_repeated=False,
        prior_independent_bfs="computations/dd82/construction/petersen_four_fiber_reassembly_run/seed.verification.json",
        proof="Each directed cross row has five fixed slots and six internal slots. A fixed surplus greater than one leaves fewer than ten possible targets, even when all six internal graphs change."
    )
    dump(OUT / "fixed_routes.json", rows)
    dump(OUT / "obstruction.json", report)
    resources = dict(operation="Read actual matching edges and count 300 immutable directed rows",
                     cpu_seconds=time.process_time()-cpu_start,
                     wall_seconds=time.monotonic()-wall_start,
                     solver_calls=0, cnf_generated=False, bfs_calls=0,
                     graph_searches=0, completed=True)
    dump(OUT / "resources.json", resources)
    print(json.dumps({k: report[k] for k in ("status", "fixed_surplus_histogram",
                     "violating_directed_rows", "strongest_witness",
                     "total_bad_pair_lower_bound")}))
    print(json.dumps(resources))


if __name__ == "__main__":
    main()
