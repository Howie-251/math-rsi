"""Check only the previously identified 50-label induced core in best-energy."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"computations/dd82/construction/full_matching58_collision_anneal_run"


def main():
    cpu,wall=time.process_time(),time.monotonic()
    candidate=json.loads((OUT/"candidate.best_energy.json").read_text())
    removed={0,8,*range(46,52)}
    labels=sorted(set(range(58))-removed)
    edges=[(u,v) for u,v in candidate["edges"] if u not in removed and v not in removed]
    adj={u:set() for u in labels}
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    hist={"adjacent":Counter(),"nonadjacent":Counter()};first_violation=None
    for u,v in combinations(labels,2):
        adjacent=v in adj[u];common=sorted(adj[u]&adj[v]);expected=0 if adjacent else 1
        hist["adjacent" if adjacent else "nonadjacent"][len(common)]+=1
        if len(common)!=expected and first_violation is None:
            first_violation=dict(pair=[u,v],adjacent=adjacent,common_neighbors=common,
                                 expected_common_count=expected)
    degree_hist=Counter(map(len,adj.values()))
    is_hs=(len(edges)==175 and degree_hist=={7:50} and
           hist["adjacent"]=={0:175} and hist["nonadjacent"]=={1:1050})
    result=dict(candidate="candidate.best_energy.json",F=candidate["F"],bad_pairs=candidate["bad_pairs"],
        removed_original_labels=sorted(removed),remaining_original_labels=labels,
        vertex_count=50,edge_count=len(edges),degree_histogram=dict(degree_hist),
        common_neighbor_histograms={k:dict(sorted(v.items())) for k,v in hist.items()},
        same_previously_identified_core_still_has_parameters_50_7_0_1=is_hs,
        first_parameter_violation=first_violation,induced_vertex_sets_checked=1,
        scope="Only this fixed 50-label subset is checked; no claim about other possible HS50 induced cores",
        graph_search_runs=0,new_bfs_runs=0,cpu_seconds=time.process_time()-cpu,
        wall_seconds=time.monotonic()-wall)
    (OUT/"best_energy.prior_core_check.json").write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!="remaining_original_labels"}))


if __name__=="__main__":main()
