"""One actual repair of tight-row internal-degree obstructions, with F=0."""
from pathlib import Path
import json
import os
import resource
import subprocess
import time

from hs_augmentation import ROOT, dump, verify
from petersen_four_fiber_reassembly import adjacency, diagnostic, matching
from petersen_fixed_route_repair_run import expand, PAIRS
from petersen_tight_row_obstruction import analyze

SOURCE = ROOT / "computations/dd82/construction/petersen_fixed_route_repair_run/candidate.json"
OUT = ROOT / "computations/dd82/construction/petersen_tight_row_repair_run"


def main():
    start,cpu_start=time.monotonic(),time.process_time()
    OUT.mkdir(exist_ok=True)
    assert not (OUT/"search.json").exists(), "Only one episode, no unchanged rerun"
    original={tuple(e) for e in json.loads(SOURCE.read_text())["edges"]}
    internal={e for e in original if e[0]//10==e[1]//10}
    command=[str(ROOT/"computations/dd82/construction/petersen_tight_row_repair.bin"),
             str(SOURCE.with_suffix(".edges")),str(OUT/"search.json")]
    pin=min(os.sched_getaffinity(0))

    def limits():
        os.sched_setaffinity(0,{pin})
        resource.setrlimit(resource.RLIMIT_CPU,(10,11))
        resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))

    before=resource.getrusage(resource.RUSAGE_CHILDREN);search_start=time.monotonic()
    with (OUT/"search.log").open("w") as log:
        result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,
                              preexec_fn=limits,timeout=14)
    search_wall=time.monotonic()-search_start
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    search_cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    assert result.returncode==0,result.returncode
    search=json.loads((OUT/"search.json").read_text())
    best=expand(search["best_permutations"],internal)
    analysis=analyze(best)
    assert analysis["external_deficit"]==0
    assert analysis["cubic_neighbor_deficit"]==search["best_deficit"]
    prior=original
    for index,state in enumerate(search["path"]):
        current=expand(state["permutations"],internal)
        actual=analyze(current)
        assert actual["external_deficit"]==0
        assert actual["cubic_neighbor_deficit"]==state["deficit"]
        if index==0:
            assert current==original and state["switch"] is None
        else:
            i,j,u,v=state["switch"]
            removed,added=prior-current,current-prior
            assert len(removed)==len(added)==2
            assert {a for a,b in removed}=={10*i+u,10*i+v}
            assert {b for a,b in removed}=={b for a,b in added}
            assert all(a//10==i and b//10==j for a,b in removed|added)
        prior=current
    assert prior==best
    dump(OUT/"candidate.json",dict(n=60,edges=sorted(best),source=str(SOURCE.relative_to(ROOT)),
         mechanism="Hold immutable route deficit F=0 while reducing the sum of degree-three deficits in the tight-row allowed internal graphs.",
         matching_permutations=search["best_permutations"],
         removed_edges=sorted(original-best),added_edges=sorted(best-original)))
    (OUT/"candidate.edges").write_text("60 240\n"+"".join(f"{u} {v}\n" for u,v in sorted(best)))
    dump(OUT/"tight_row_constraints.json",analysis)
    diag=diagnostic(best);dump(OUT/"candidate.diagnostic.json",diag)
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    if best!=original:
        checked=json.loads(verify(OUT/"candidate.json"))
    else:
        checked=json.loads(SOURCE.with_suffix(".verification.json").read_text())
        dump(OUT/"candidate.verification.json",checked)
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    bfs_cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime

    rows={tuple(r["row"]):r for r in analysis["tight_rows"]}
    old_keys=[(9,2),(9,5),(57,0)]
    present=[rows[key] for key in old_keys if key in rows]
    old_banned={b if a==9 else a for r in present for a,b in r["forbidden_internal_edges"] if 9 in (a,b)}
    old_witness=dict(previous_rows=old_keys,rows_still_tight=[r["row"] for r in present],
                     forbidden_neighbors_of_9_from_these_rows=sorted(old_banned),
                     direct_degree_contradiction_still_present=(len(old_banned)>6))
    dump(OUT/"old_witness_after_repair.json",old_witness)
    ns0,ns1=adjacency(original),adjacency(best)
    report=dict(source=str(SOURCE.relative_to(ROOT)),
        initial_cubic_neighbor_deficit=search["initial_deficit"],
        best_cubic_neighbor_deficit=search["best_deficit"],external_deficit=0,
        stop=search["stop"],states_stored=search["states_stored"],
        states_expanded=search["states_expanded"],switch_candidates_checked=search["switch_candidates_checked"],
        path_length=len(search["path"])-1,strict_improvements=search["strict_improvements"],
        old_three_row_obstruction_removed=not old_witness["direct_degree_contradiction_still_present"],
        all_tight_row_degree_obstructions_removed=(search["best_deficit"]==0),
        remaining_deficient_vertices=analysis["deficient_vertices"],
        allowed_degree_histogram=analysis["allowed_degree_histogram"],
        forbidden_internal_edges=len(analysis["forbidden_internal_edges"]),
        full_graph_bad_pairs=diag["bad_pair_count"],energy=diag["energy"],
        changed_external_interfaces=[[i,j] for i,j in PAIRS if matching(ns0,i,j)!=matching(ns1,i,j)],
        independent_path_replay=True,source_bfs_reused=(best==original),
        command=command,search_exit_code=result.returncode,search_cpu_seconds=search_cpu,
        search_wall_seconds=search_wall,independent_bfs_cpu_seconds=bfs_cpu,
        parent_cpu_seconds=time.process_time()-cpu_start,total_wall_seconds=time.monotonic()-start,
        search_cpu_budget_seconds=10,internal_stop_seconds=9.8,stored_state_cap=2000,
        pinned_cpu=pin,
        scope="One nonincreasing local episode from the actual repaired external skeleton, with F=0 as a hard invariant. No new seed or random restart. This is not an exhaustion of all F=0 skeletons.")
    dump(OUT/"resources.json",report)
    print(json.dumps({k:v for k,v in report.items() if k!="command"}))


if __name__=="__main__":
    main()
