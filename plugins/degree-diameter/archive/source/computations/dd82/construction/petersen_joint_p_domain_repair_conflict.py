"""Four actual cross clauses contradict the unique compatible fiber-3 graph.

Reads the completed catalog count and saved clause map. No solver,
catalog re-enumeration, or matching repair is performed.
"""
from itertools import combinations
import json
import time

from hs_augmentation import ROOT,dump
from petersen_four_fiber_reassembly import adjacency,matching

OUT=ROOT/"computations/dd82/construction/petersen_joint_p_domain_repair_run"
SAT=ROOT/"computations/dd82/construction/petersen_joint_p_domain_repair_completion_run"


def main():
    start,cpu_start=time.monotonic(),time.process_time()
    search=json.loads((OUT/"search.json").read_text())
    assert search["best_deficit"]==0 and search["best_domain_sizes"][3]==1
    p3={tuple(edge) for k,edge in enumerate(combinations(range(30,40),2))
        if search["best_internal_masks"][3]>>k&1}
    ns=adjacency(json.loads((OUT/"candidate.json").read_text())["edges"])
    m={(i,j):matching(ns,i,j) for i in range(6) for j in range(6) if i!=j}
    coverage=json.loads((SAT/"coverage.json").read_text())
    clauses={tuple(c["pair"]):(14221+k,c) for k,c in enumerate(coverage)}
    witnesses=[]
    for pair,required in [((1,38),(0,1)),((1,30),(1,4)),
                          ((1,37),(1,5)),((9,33),(1,9))]:
        clause_id,clause=clauses[pair]
        assert tuple(clause["source_internal_edge"])==required
        absent=tuple(clause["target_internal_edge"])
        assert absent[0]//10==3 and absent not in p3
        u,v=pair
        paths=[[u,m[0,3][u]]]
        for k in (1,2,4,5):
            w=m[0,k][u];paths.append([u,w,m[k,3][w%10]])
        assert all(path[-1]!=v for path in paths)
        witnesses.append(dict(pair=pair,clause_id=clause_id,
             required_internal_edge=required,
             alternative_internal_edge_absent_from_unique_P3=absent,
             fixed_external_paths=paths,variables=clause["variables"]))
    forced={tuple(w["required_internal_edge"]) for w in witnesses}
    assert len(forced)==4 and all(1 in edge for edge in forced)
    report=dict(status="EXPLICIT_CROSS_FIBER_DEGREE_CONTRADICTION",
        premise="The complete 30240-copy scan gives exactly one Petersen graph in the actual fiber-3 allowed graph.",
        domain_sizes=search["best_domain_sizes"],unique_P3_edges=sorted(p3),
        clauses=witnesses,forced_vertex=1,forced_neighbors=[0,4,5,9],
        conclusion="Each of the four fixed-uncovered cross pairs has its fiber-3 internal alternative absent in the unique P3, forcing four distinct internal neighbors at vertex 1. This contradicts cubic degree in fiber 0.",
        scope="The saved new external matching skeleton with arbitrary compatible Petersen choices. The other four internal fibers cannot alter these five fixed external paths or the two internal alternatives.",
        cpu_seconds=time.process_time()-cpu_start,wall_seconds=time.monotonic()-start,
        solver_calls=0,matching_searches=0,additional_catalog_scans=0)
    dump(OUT/"specific_conflict.json",report)
    print(json.dumps(report))


if __name__=="__main__":main()
