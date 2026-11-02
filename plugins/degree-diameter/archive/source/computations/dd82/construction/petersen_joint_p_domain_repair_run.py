"""One bounded matching repair using six complete internal Petersen choices."""
from itertools import combinations
import json
import os
import resource
import subprocess
import time

from hs_augmentation import ROOT,dump,verify
from petersen_four_fiber_reassembly import adjacency,diagnostic,matching
from petersen_fixed_route_repair_run import expand,PAIRS
from petersen_tight_row_obstruction import analyze

SOURCE=ROOT/"computations/dd82/construction/petersen_tight_row_repair_run/candidate.json"
OUT=ROOT/"computations/dd82/construction/petersen_joint_p_domain_repair_run"
LOCAL_EDGES=list(combinations(range(10),2))


def internal_edges(masks):
    result=set()
    for i,mask in enumerate(masks):
        local={e for k,e in enumerate(LOCAL_EDGES) if mask>>k&1}
        assert len(local)==15
        neighbors=[set() for _ in range(10)]
        for u,v in local:neighbors[u].add(v);neighbors[v].add(u)
        assert all(len(s)==3 for s in neighbors)
        assert all(len(neighbors[u]&neighbors[v])==(0 if v in neighbors[u] else 1)
                   for u,v in LOCAL_EDGES)
        result.update((10*i+u,10*i+v) for u,v in local)
    return result


def main():
    start,cpu_start=time.monotonic(),time.process_time()
    OUT.mkdir(exist_ok=True)
    assert not (OUT/"search.json").exists(),"One episode only"
    original={tuple(e) for e in json.loads(SOURCE.read_text())["edges"]}
    original_external={e for e in original if e[0]//10!=e[1]//10}
    command=[str(ROOT/"computations/dd82/construction/petersen_joint_p_domain_repair.bin"),
             str(SOURCE.with_suffix(".edges")),str(OUT/"search.json")]
    pin=min(os.sched_getaffinity(0))

    def limits():
        os.sched_setaffinity(0,{pin})
        resource.setrlimit(resource.RLIMIT_CPU,(15,16))
        resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))

    before=resource.getrusage(resource.RUSAGE_CHILDREN);child_start=time.monotonic()
    with (OUT/"search.log").open("w") as log:
        result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,
                              preexec_fn=limits,timeout=20)
    search_wall=time.monotonic()-child_start;after=resource.getrusage(resource.RUSAGE_CHILDREN)
    search_cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    assert result.returncode==0,result.returncode
    search=json.loads((OUT/"search.json").read_text())
    prior=original_external
    for index,state in enumerate(search["path"]):
        internal=internal_edges(state["internal_masks"])
        full=expand(state["permutations"],internal)
        constraints=analyze(full)
        forbidden={tuple(row["edge"]) for row in constraints["forbidden_internal_edges"]}
        assert constraints["external_deficit"]==0
        assert len(internal&forbidden)==state["deficit"]
        current=full-internal
        if index==0:
            assert current==original_external and state["switch"] is None
        else:
            i,j,u,v=state["switch"]
            removed,added=prior-current,current-prior
            assert len(removed)==len(added)==2
            assert {a for a,b in removed}=={10*i+u,10*i+v}
            assert {b for a,b in removed}=={b for a,b in added}
            assert all(a//10==i and b//10==j for a,b in removed|added)
        prior=current
    best_internal=internal_edges(search["best_internal_masks"])
    best=expand(search["best_permutations"],best_internal)
    assert full==best
    analysis=analyze(best)
    assert analysis["external_deficit"]==0
    assert sum(search["minimum_forbidden_edges"])==search["best_deficit"]
    assert all((size>0)==(missing==0) for size,missing in
               zip(search["best_domain_sizes"],search["minimum_forbidden_edges"]))
    dump(OUT/"candidate.json",dict(n=60,edges=sorted(best),source=str(SOURCE.relative_to(ROOT)),
        mechanism="External matching switches retain F=0 and minimize the sum of exact forbidden-edge distances of six complete Petersen copies to their tight-row allowed graphs.",
        matching_permutations=search["best_permutations"],internal_masks=search["best_internal_masks"],
        removed_edges=sorted(original-best),added_edges=sorted(best-original),
        internal_edges_by_fiber=[[list(e) for e in sorted(best_internal) if e[0]//10==i] for i in range(6)]))
    (OUT/"candidate.edges").write_text("60 240\n"+"".join(f"{u} {v}\n" for u,v in sorted(best)))
    dump(OUT/"tight_row_constraints.json",analysis)
    diag=diagnostic(best);dump(OUT/"candidate.diagnostic.json",diag)
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    checked=json.loads(verify(OUT/"candidate.json"))
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    bfs_cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
    ns0,ns1=adjacency(original),adjacency(best)
    report=dict(source=str(SOURCE.relative_to(ROOT)),initial_R=search["initial_deficit"],best_R=search["best_deficit"],
        F=0,K=analysis["cubic_neighbor_deficit"],stop=search["stop"],
        states_stored=search["states_stored"],states_expanded=search["states_expanded"],
        switch_candidates_checked=search["switch_candidates_checked"],
        path_length=len(search["path"])-1,strict_improvements=search["strict_improvements"],
        domain_sizes=search["best_domain_sizes"],minimum_forbidden_edges=search["minimum_forbidden_edges"],
        remaining_empty_fibers=[i for i,d in enumerate(search["best_domain_sizes"]) if not d],
        complete_labeled_catalog_size=search["catalog_size"],cached_allowed_graphs=search["cached_allowed_graphs"],
        popcount_checks=search["popcount_checks"],full_graph_bad_pairs=diag["bad_pair_count"],energy=diag["energy"],
        changed_external_interfaces=[[i,j] for i,j in PAIRS if matching(ns0,i,j)!=matching(ns1,i,j)],
        changed_internal_fibers=[i for i in range(6) if
            {e for e in original if e[0]//10==e[1]//10==i}!={e for e in best_internal if e[0]//10==i}],
        independent_path_replay=True,all_path_internal_graphs_directly_checked=True,
        search_cpu_seconds=search_cpu,search_wall_seconds=search_wall,
        independent_bfs_cpu_seconds=bfs_cpu,parent_cpu_seconds=time.process_time()-cpu_start,
        total_wall_seconds=time.monotonic()-start,search_cpu_budget_seconds=15,
        internal_stop_seconds=14.7,stored_state_cap=500,pinned_cpu=pin,command=command,
        scope="One nonincreasing joint complete-P domain repair from the saved 286-pair skeleton. No random restart or full external-family exhaustion.")
    dump(OUT/"resources.json",report)
    print(json.dumps({k:v for k,v in report.items() if k!="command"}))


if __name__=="__main__":main()
