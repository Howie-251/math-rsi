"""Check exactly one requested induced 50-vertex core of the failed graph."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"computations/dd82/construction/full_matching58_anneal_run"


def main():
    cpu,wall=time.process_time(),time.monotonic()
    rows=[tuple(map(int,line.split())) for line in (OUT/"candidate.best.edges").read_text().splitlines()]
    assert rows[0]==(58,232)
    removed={0,8,*range(46,52)}
    labels=sorted(set(range(58))-removed)
    assert len(labels)==50
    edges=sorted((u,v) for u,v in rows[1:] if u not in removed and v not in removed)
    adj={u:set() for u in labels}
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    degrees=[len(adj[u]) for u in labels]
    hist={"adjacent":Counter(),"nonadjacent":Counter()}
    bad=[]
    for u,v in combinations(labels,2):
        common=sorted(adj[u]&adj[v]);adjacent=v in adj[u]
        hist["adjacent" if adjacent else "nonadjacent"][len(common)]+=1
        if not adjacent and not common:bad.append([u,v])
    moore=(len(edges)==175 and degrees==[7]*50 and
           hist["adjacent"]=={0:175} and hist["nonadjacent"]=={1:1050})
    assert moore
    ids={v:i for i,v in enumerate(labels)}
    graph=dict(n=50,edges=[[ids[u],ids[v]] for u,v in edges],original_vertex_labels=labels,
               removed_original_labels=sorted(removed),source="candidate.best.edges")
    (OUT/"best.induced_hs50.json").write_text(json.dumps(graph,indent=2)+'\n')
    result=dict(removed_original_labels=sorted(removed),remaining_original_labels=labels,
        n=50,edge_count=len(edges),degrees=degrees,
        common_neighbor_histograms={kind:dict(sorted(h.items())) for kind,h in hist.items()},
        pairs_checked=1225,bad_pairs=bad,diameter=2,
        is_degree7_order50_Moore_graph=moore,
        conclusion="This one induced core has parameters (50,7,0,1), hence is the Hoffman-Singleton Moore graph",
        retained_core="best.induced_hs50.json",induced_subgraphs_checked=1,
        graph_search_runs=0,full_58_bfs_reruns=0,
        cpu_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall)
    path=OUT/"best.failure_summary.json";summary=json.loads(path.read_text())
    summary["one_induced_HS50_check"]=result
    path.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ("degrees","remaining_original_labels")}))


if __name__=="__main__":main()
