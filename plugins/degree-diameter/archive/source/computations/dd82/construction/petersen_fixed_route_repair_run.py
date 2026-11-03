"""Single bounded fixed-route repair, expanded graph, independent BFS."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import os
import resource
import subprocess
import sys
import time

from hs_augmentation import ROOT, dump, verify
from petersen_four_fiber_reassembly import adjacency, diagnostic, matching

OUT = ROOT / "computations/dd82/construction/petersen_fixed_route_repair_run"
SOURCE = ROOT / "computations/dd82/construction/petersen_four_fiber_reassembly_run/seed.json"
PAIRS = list(combinations(range(6), 2))


def fixed_rows(ns):
    m = {(i,j): matching(ns,i,j) for i in range(6) for j in range(6) if i != j}
    rows = []
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            for u in range(10):
                targets = [m[i,j][u]]
                for k in range(6):
                    if k not in (i,j):
                        targets.append(m[k,j][m[i,k][u]-10*k])
                rows.append(dict(source=10*i+u, target_fiber=j,
                                 fixed_targets=targets,
                                 distinct=len(set(targets)),
                                 deficit=max(0,4-len(set(targets)))))
    return rows


def expand(permutations, internal):
    edges = set(internal)
    for (i,j), permutation in zip(PAIRS, permutations):
        assert sorted(permutation) == list(range(10))
        edges.update((10*i+u,10*j+v) for u,v in enumerate(permutation))
    assert len(edges) == 240 and all(len(s) == 8 for s in adjacency(edges))
    return edges


def main():
    start = time.monotonic()
    cpu_start = time.process_time()
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "search.json").exists(), "Do not repeat this repair episode"
    original = {tuple(e) for e in json.loads(SOURCE.read_text())["edges"]}
    internal = {e for e in original if e[0]//10 == e[1]//10}
    command = [str(ROOT / "computations/dd82/construction/petersen_fixed_route_repair.bin"),
               str(SOURCE.with_suffix(".edges")), str(OUT / "search.json")]
    pinned_cpu = min(os.sched_getaffinity(0))

    def limits():
        os.sched_setaffinity(0,{pinned_cpu})
        resource.setrlimit(resource.RLIMIT_CPU,(5,6))
        resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))

    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    search_wall = time.monotonic()
    with (OUT / "search.log").open("w") as log:
        result = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                preexec_fn=limits, timeout=8)
    search_wall = time.monotonic()-search_wall
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    search_cpu = after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    assert result.returncode == 0, result.returncode
    search = json.loads((OUT / "search.json").read_text())
    best = expand(search["best_permutations"], internal)
    rows = fixed_rows(adjacency(best))
    assert sum(r["deficit"] for r in rows) == search["best_deficit"]
    # Replay the recorded switch path independently using complete edge sets.
    prior = original
    for index, state in enumerate(search["path"]):
        current = expand(state["permutations"],internal)
        assert sum(r["deficit"] for r in fixed_rows(adjacency(current))) == state["deficit"]
        if index == 0:
            assert current == original and state["switch"] is None
        else:
            i,j,u,v = state["switch"]
            removed,added = prior-current,current-prior
            assert len(removed) == len(added) == 2
            assert {a for a,b in removed} == {10*i+u,10*i+v}
            assert {b for a,b in removed} == {b for a,b in added}
            assert all(a//10 == i and b//10 == j for a,b in removed|added)
        prior = current
    assert prior == best

    dump(OUT / "candidate.json",dict(n=60,edges=sorted(best),source=str(SOURCE.relative_to(ROOT)),
         mechanism="Deterministic nonincreasing matching switches minimize missing distinct targets among the five immutable external routes; internal Petersen edges retained only for this actual seed.",
         matching_permutations=search["best_permutations"],
         removed_edges=sorted(original-best),added_edges=sorted(best-original)))
    (OUT / "candidate.edges").write_text("60 240\n"+"".join(f"{u} {v}\n" for u,v in sorted(best)))
    dump(OUT / "fixed_routes.json",rows)
    diag = diagnostic(best)
    dump(OUT / "candidate.diagnostic.json",diag)
    bfs_before = resource.getrusage(resource.RUSAGE_CHILDREN)
    if best != original:
        checked = json.loads(verify(OUT / "candidate.json"))
    else:
        checked = json.loads(SOURCE.with_suffix(".verification.json").read_text())
        dump(OUT / "candidate.verification.json",checked)
    bfs_after = resource.getrusage(resource.RUSAGE_CHILDREN)
    bfs_cpu = bfs_after.ru_utime+bfs_after.ru_stime-bfs_before.ru_utime-bfs_before.ru_stime
    ns0,ns1 = adjacency(original),adjacency(best)

    def local_profile(ns,i,j):
        permutation=matching(ns,i,j)
        return [[int(v == permutation[u-10*i])+int(v in ns[permutation[u-10*i]])
                 +sum(v == permutation[w-10*i] for w in ns[u] if w//10 == i)
                 for v in range(10*j,10*j+10)] for u in range(10*i,10*i+10)]

    report = dict(source=str(SOURCE.relative_to(ROOT)),
        initial_deficit=search["initial_deficit"],best_deficit=search["best_deficit"],
        stop=search["stop"],states_stored=search["states_stored"],
        states_expanded=search["states_expanded"],switch_candidates_checked=search["switch_candidates_checked"],
        path_length=len(search["path"])-1,strict_improvements=search["strict_improvements"],
        full_graph_bad_pairs=diag["bad_pair_count"],energy=diag["energy"],
        changed_external_interfaces=[[i,j] for i,j in PAIRS if matching(ns0,i,j) != matching(ns1,i,j)],
        changed_local_route_profiles=[[i,j] for i,j in PAIRS if local_profile(ns0,i,j) != local_profile(ns1,i,j)],
        fixed_row_distinct_histogram=dict(sorted(Counter(r["distinct"] for r in rows).items())),
        remaining_violations=[r for r in rows if r["deficit"]],
        source_bfs_reused=(best == original),independent_path_replay=True,
        command=command,search_exit_code=result.returncode,
        search_cpu_seconds=search_cpu,search_wall_seconds=search_wall,
        independent_bfs_cpu_seconds=bfs_cpu,
        parent_cpu_seconds=time.process_time()-cpu_start,
        total_wall_seconds=time.monotonic()-start,
        search_cpu_budget_seconds=5,internal_stop_seconds=4.8,
        stored_state_cap=500,pinned_cpu=pinned_cpu,
        scope="One nonincreasing local episode on matching permutations from the actual 97-pair seed, targeting only immutable cross-route coverage. No global optimality or full-domain exclusion claim.")
    dump(OUT / "resources.json",report)
    print(json.dumps({k:v for k,v in report.items() if k not in ("remaining_violations","command")}))


if __name__ == "__main__":
    main()
