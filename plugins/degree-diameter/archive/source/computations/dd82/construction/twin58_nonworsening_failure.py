#!/usr/bin/env python3
"""Direct old-HS-core failure data for the saved final order-58 graph."""
from pathlib import Path
from collections import Counter
import json
from twin59_to_58_deflation_verify import read_edges
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin58_nonworsening_levels_run'
def main():
    n,edges58=read_edges(OUT/'final.edges');assert n==58
    original_label=lambda v:v if v<41 else v+2
    edges={tuple(sorted((original_label(u),original_label(v)))) for u,v in edges58}
    _,original=read_edges(HERE/'petersen_all_matchings_run/candidate.best.edges')
    old=set(range(40))|set(range(50,60));aux=set(range(60))-old-{41,42}
    adj={u:set() for u in old|aux}
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    hs={e for e in original if set(e)<=old};oldedges={e for e in edges if set(e)<=old}
    auxedges={e for e in edges if set(e)<=aux};ports={u:8-len(adj[u]&old) for u in old}
    bad=[];oldbad=[]
    for u in sorted(old|aux):
        for v in sorted(old|aux):
            if u>=v:continue
            if v not in adj[u] and not adj[u]&adj[v]:bad.append((u,v))
            if u in old and v in old and v not in adj[u] and not adj[u]&adj[v]&old:oldbad.append((u,v))
    forcedold=[(u,v) for u,v in oldbad if ports[u]==0 or ports[v]==0]
    capacities=[]
    for u in sorted(old):
        if ports[u]:continue
        capacity=sum(ports[w] for w in adj[u])
        capacities.append({'old_vertex':u,'old_neighbors':sorted(adj[u]),
          'total_neighbor_ports':capacity,'auxiliary_vertex_count':len(aux),
          'forced_uncovered_old_new_pairs':max(0,len(aux)-capacity),
          'actual_uncovered_auxiliary_vertices':sorted(v for v in aux if not adj[u]&adj[v])})
    deficit=sum(r['forced_uncovered_old_new_pairs'] for r in capacities)
    assert sorted(hs-oldedges)==[(50,55)]
    assert sorted(oldedges-hs)==[(3,12),(9,14),(28,29),(38,55)]
    assert forcedold==[(9,55),(14,55),(28,55)] and deficit==3
    result={'graph':str(OUT/'final.edges'),'label_convention':'original order60 labels; deleted originals41,42; order58 v>=41 maps to v+2',
      'old_vertices':sorted(old),'auxiliary_vertices':sorted(aux),'old_induced_edge_count':len(oldedges),
      'old_edges_removed_from_hs':sorted(hs-oldedges),'old_edges_added_to_hs':sorted(oldedges-hs),
      'old_port_counts':ports,'old_port_count_histogram':dict(Counter(ports.values())),
      'zero_port_old_vertices':sorted(v for v in old if ports[v]==0),
      'auxiliary_edges':sorted(auxedges),'auxiliary_internal_degrees':{v:len(adj[v]&aux) for v in sorted(aux)},
      'old_to_auxiliary_incidence_count':sum(ports.values()),'bad_pairs_original60_labels':bad,
      'bad_pair_partition_counts':dict(Counter('old-old' if u in old and v in old else 'auxiliary-auxiliary' if u in aux and v in aux else 'old-auxiliary' for u,v in bad)),
      'pairs_without_old_distance_at_most_two':oldbad,
      'unavoidable_old_old_pairs_for_fixed_old_induced_graph':forcedold,
      'saturated_vertex_neighbor_port_capacities':capacities,
      'unavoidable_old_auxiliary_pair_count_for_fixed_old_induced_graph':deficit,
      'unavoidable_total_bad_pair_lower_bound_for_fixed_old_induced_graph':len(forcedold)+deficit,
      'scope':'Any maximum-degree-eight graph retaining this old induced graph and these eight auxiliary vertices, with arbitrary attachments and auxiliary edges'}
    (OUT/'failure_structure.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('old_edges_removed_from_hs','old_edges_added_to_hs','zero_port_old_vertices','bad_pair_partition_counts','unavoidable_old_old_pairs_for_fixed_old_induced_graph','unavoidable_total_bad_pair_lower_bound_for_fixed_old_induced_graph')},indent=2))
if __name__=='__main__':main()
