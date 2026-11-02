"""Diagnose all local Petersen domains for the new and original skeletons."""
from itertools import combinations
import json
import os
import resource
import subprocess
import time

from hs_augmentation import ROOT, dump
from petersen_tight_row_obstruction import analyze

OUT=ROOT/"computations/dd82/construction/petersen_allowed_petersen_domains_run"
SOURCES=[ROOT/"computations/dd82/construction/petersen_tight_row_repair_run/candidate.json",
         ROOT/"computations/dd82/construction/petersen_all_matchings_run/candidate.best.json"]
LOCAL_EDGES=list(combinations(range(10),2))


def decode(mask,offset=0):
    return [[u+offset,v+offset] for e,(u,v) in enumerate(LOCAL_EDGES) if mask>>e&1]


def main():
    started,cpu_started=time.monotonic(),time.process_time()
    OUT.mkdir(exist_ok=True)
    assert not (OUT/"domains.json").exists(),"No unchanged domain rerun"
    inputs=[];records=[]
    for source in SOURCES:
        full={tuple(e) for e in json.loads(source.read_text())["edges"]}
        constraints=analyze(full)
        allowed={int(u):set(vs) for u,vs in constraints["allowed_neighbor_lists"].items()}
        graphs=[]
        for i in range(6):
            mask=sum(1<<e for e,(u,v) in enumerate(LOCAL_EDGES) if 10*i+v in allowed[10*i+u])
            seed_mask=sum(1<<e for e,(u,v) in enumerate(LOCAL_EDGES) if (10*i+u,10*i+v) in full)
            inputs.append((mask,seed_mask))
            graphs.append(dict(fiber=i,allowed_edges=decode(mask,10*i),
                               allowed_neighbor_lists={u:sorted(allowed[u]) for u in range(10*i,10*i+10)},
                               seed_internal_edges=decode(seed_mask,10*i)))
        records.append(dict(source=str(source.relative_to(ROOT)),
             F=constraints["external_deficit"],K=constraints["cubic_neighbor_deficit"],
             tight_rows=len(constraints["tight_rows"]),graphs=graphs,
             all_tight_rows=constraints["tight_rows"]))
    (OUT/"input.txt").write_text("12\n"+"".join(f"{mask} {seed}\n" for mask,seed in inputs))
    dump(OUT/"input_graphs.json",dict(local_edge_index=LOCAL_EDGES,sources=records))
    command=[str(ROOT/"computations/dd82/construction/petersen_allowed_petersen_domains.bin"),
             str(OUT/"input.txt"),str(OUT/"domains.json")]
    pin=min(os.sched_getaffinity(0))

    def limits():
        os.sched_setaffinity(0,{pin})
        resource.setrlimit(resource.RLIMIT_CPU,(5,6))
        resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))

    before=resource.getrusage(resource.RUSAGE_CHILDREN);child_start=time.monotonic()
    with (OUT/"enumerator.log").open("w") as log:
        result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,
                              preexec_fn=limits,timeout=8)
    wall=time.monotonic()-child_start;after=resource.getrusage(resource.RUSAGE_CHILDREN)
    assert result.returncode==0,result.returncode
    catalog=json.loads((OUT/"domains.json").read_text())
    assert catalog["complete"] and catalog["catalog_size"]==30240
    summaries=[]
    for s,source in enumerate(SOURCES):
        domains=catalog["domains"][6*s:6*s+6]
        for d in domains:
            assert d["domain_size"]==len(d["all_domain_masks"])
            assert len(set(d["all_domain_masks"]))==d["domain_size"]
            assert all(mask & ~d["allowed_mask"]==0 for mask in d["all_domain_masks"])
            d["one_closest_copy_edges"]=decode(d["one_closest_copy_mask"],10*d["fiber"])
            d["forbidden_edges_in_closest_copy"]=decode(d["one_closest_copy_mask"] & ~d["allowed_mask"],10*d["fiber"])
        summaries.append(dict(source=str(source.relative_to(ROOT)),F=records[s]["F"],K=records[s]["K"],
                         domain_sizes=[d["domain_size"] for d in domains],
                         minimum_forbidden_edges=[d["minimum_forbidden_edges"] for d in domains],
                         source_internal_membership=[d["seed_internal_in_domain"] for d in domains]))
    dump(OUT/"domains.json",catalog)
    report=dict(complete=True,sources=summaries,catalog_size=30240,domains_completed=12,
                catalog_containment_checks=12*30240,all_survivors_saved=True,
                enumeration_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                enumeration_wall_seconds=wall,parent_cpu_seconds=time.process_time()-cpu_started,
                total_wall_seconds=time.monotonic()-started,
                cpu_budget_seconds=5,pinned_cpu=pin,command=command,
                graph_repairs=0,solver_calls=0,bfs_replays=0,
                scope="All labeled Petersen subgraphs of the twelve actual tight-row allowed graphs. This is a local containment domain; surviving fibers still need joint cross-pair coverage and F=0.")
    dump(OUT/"resources.json",report)
    print(json.dumps({k:v for k,v in report.items() if k!="command"}))


if __name__=="__main__":main()
