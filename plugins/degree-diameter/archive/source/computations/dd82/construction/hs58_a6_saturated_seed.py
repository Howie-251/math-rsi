"""One direct, knowingly failed a6 seed. No search, flow, or solver."""
from pathlib import Path
from collections import Counter
import json
import os
import resource
import time
from hs_augmentation import base, dump, verify

OUT = Path(__file__).with_name("hs58_a6_saturated_seed_run")


def main():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    start_wall, start_cpu = time.monotonic(), time.process_time()
    child_before = resource.getrusage(resource.RUSAGE_CHILDREN)
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "result.json").exists(), "No unchanged rerun"
    Q, qn = base()
    D = {(0, 1), (10, 11)}
    A = {(25, 26), (35, 41), (4, 36), (45, 46), (14, 33), (32, 42)}
    Z = {v for e in A for v in e}
    P = {v for e in D for v in e}
    H = [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
         (1, 2), (1, 3), (1, 4), (1, 5), (6, 7)]
    assert D <= set(Q) and not (A & set(Q))
    assert len(Z) == 12 and not (Z & P)
    assert all(not (qn[z] & Z) for z in Z)
    B = [[] for _ in range(50)]
    B[0] = B[10] = [1, 6]
    B[1] = B[11] = [1, 7]
    forced = {30: 7, 40: 7, 39: 7, 48: 7, 2: 6, 31: 6, 12: 6, 49: 6}
    for v, label in forced.items():
        B[v] = [label]
    remaining = sorted(set(range(50)) - Z - P - set(forced))
    fill = [0] * 2 + [2] * 6 + [3] * 6 + [4] * 6 + [5] * 6
    assert len(remaining) == len(fill) == 26
    for v, label in zip(remaining, fill):
        B[v] = [label]
    M = sorted((set(Q) - D) | A)
    mn = [set() for _ in range(50)]
    for v, w in M:
        mn[v].add(w)
        mn[w].add(v)
    hd = Counter(v for e in H for v in e)
    columns = Counter(label for row in B for label in row)
    assert all(len(mn[v]) + len(B[v]) == 8 for v in range(50))
    assert all(columns[a] + hd[a] == 8 for a in range(8))
    edges = sorted(M + [(50+a, 50+b) for a, b in H]
                   + [(v, 50+a) for v in range(50) for a in B[v]])
    assert len(edges) == len(set(edges)) == 232
    dump(OUT / "seed.json", dict(n=58, edges=edges, base_edges=Q,
         deleted_edges=sorted(D), added_edges=sorted(A), auxiliary_edges=H,
         old_new_ports=B, zero_old_vertices=sorted(Z),
         scope="One explicit failed assignment, not an a6 existence candidate after the known zero-row obstruction."))
    (OUT / "seed.edges").write_text("58 232\n" + "".join(f"{v} {w}\n" for v, w in edges))
    checked = json.loads(verify(OUT / "seed.json"))
    full = json.loads((OUT / "seed.verification.json").read_text())
    assert full["degrees"] == [8] * 58
    counts = Counter("old-old" if b < 50 else "old-new" if a < 50 else "new-new"
                     for entry in full["bad_pairs"] for a, b in [entry["pair"]])
    assert counts["old-old"] == counts["new-new"] == 0
    old = 33
    slots = [(v, a) for v in sorted(mn[old]) for a in B[v]]
    reached = sorted({a for _, a in slots})
    dump(OUT / "analysis.json", dict(
         bad_pairs_by_source=dict(counts), old_pair_coverage_complete=True,
         new_pair_coverage_complete=True, column_sizes=[columns[a] for a in range(8)],
         forced_ordinary_ports=forced, deterministic_fill_old_vertices=remaining,
         deterministic_fill_labels=fill,
         known_failure=dict(old_vertex=old, ports=B[old], old_neighbors=sorted(mn[old]),
             neighbor_port_slots=slots, reached_new_labels=reached,
             missing_new_labels=sorted(set(range(8))-set(reached))),
         reason="Zero 33 sees label 7 at deletion endpoint 11 and ordinary old vertex 30; its exactly eight slots are not rainbow. B30=7 is forced by lost old pair (1,30) and saturated column 1."))
    child_after = resource.getrusage(resource.RUSAGE_CHILDREN)
    child_cpu = ((child_after.ru_utime + child_after.ru_stime)
                 - (child_before.ru_utime + child_before.ru_stime))
    report = dict(status="COMPLETE_FAILED_SEED", independent_bfs=checked,
         bad_pairs_by_source=dict(counts), constructions=1, searches=0,
         flow_calls=0, solver_calls=0, construction_cpu_seconds=time.process_time()-start_cpu,
         independent_bfs_cpu_seconds=child_cpu, wall_seconds=time.monotonic()-start_wall,
         cpu_budget_seconds=5, pinned_cpu=min(os.sched_getaffinity(0)))
    dump(OUT / "result.json", report)
    print(json.dumps(report))


if __name__ == "__main__":
    main()
