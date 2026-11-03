#!/usr/bin/env python3
"""Independent best-graph BFS, edit replay, pattern count and HS difference check."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from math import comb
import json
from twin59_to_58_deflation_verify import read_edges,bfs,matchings
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin58_three_switch_two_hs_deletions_run'
def main():
    r=json.loads((OUT/'neighborhood.json').read_text())
    n,seed=read_edges(Path(r['source']));nn,graph=read_edges(OUT/'neighborhood.best.edges')
    assert n==nn==58
    removed={tuple(sorted(e)) for e in r['best_removed_order58']}
    added={tuple(sorted(e)) for e in r['best_added_order58']}
    assert len(removed)==len(added)==3 and removed<=seed and not added&seed
    endpoints={v for e in removed for v in e}
    assert len(endpoints)==6 and Counter(v for e in added for v in e)=={v:1 for v in endpoints}
    assert graph==(seed-removed)|added
    patterns=list(matchings(tuple(range(6))));original={(0,1),(2,3),(4,5)}
    kinds=Counter(len(set(p)&original) for p in patterns)
    assert len(patterns)==15 and kinds=={0:8,1:6,3:1}
    delta_adj={u:set() for u in endpoints}
    for u,v in removed|added:delta_adj[u].add(v);delta_adj[v].add(u)
    reached={next(iter(endpoints))}
    while True:
        bigger=reached|{v for u in reached for v in delta_adj[u]}
        if bigger==reached:break
        reached=bigger
    assert reached==endpoints and all(len(v)==2 for v in delta_adj.values())
    adj=[set() for _ in range(58)]
    for u,v in seed:adj[u].add(v);adj[v].add(u)
    triangles=sum(len(adj[u]&adj[v]) for u,v in seed)//3
    # Independent count of three-edge matchings via independent triples of
    # the line graph: C(M,3)-E_L(M-2)+sum C(d_L,2)-triangles(L).
    line_edges=sum(comb(len(a),2) for a in adj)
    line_wedges=sum(comb(len(adj[u])+len(adj[v])-2,2) for u,v in seed)
    line_triangles=sum(comb(len(a),3) for a in adj)+triangles
    disjoint=comb(232,3)-line_edges*230+line_wedges-line_triangles
    assert r['complete_neighborhood'] and r['edge_triples_visited']==comb(232,3)
    assert r['disjoint_edge_triples']==disjoint==1698699
    assert r['legal_three_switches']==r['rejected_for_fewer_than_two_hs_deletions']+r['eligible_moves_scored']
    assert sum(r['bad_pair_histogram'].values())==sum(r['net_hs_deletion_histogram'].values())==r['eligible_moves_scored']
    assert min(map(int,r['bad_pair_histogram']))==r['minimum_bad_pairs']
    _,hs60=read_edges(Path(r['hs_reference_source']))
    old60=set(range(40))|set(range(50,60));hs={e for e in hs60 if set(e)<=old60}
    label=lambda v:v if v<41 else v+2
    expanded={(label(u),label(v)) for u,v in graph};initial={(label(u),label(v)) for u,v in seed}
    finalold={e for e in expanded if set(e)<=old60}
    assert len(hs)==175 and len(hs-initial)==1 and len(hs-finalold)==r['best_net_hs_deletions']>=2
    assert sorted(hs-finalold)==[tuple(e) for e in r['best_deleted_hs_edges_original60']]
    assert sorted(finalold-hs)==[tuple(e) for e in r['best_added_old_edges_original60']]
    oldadj={u:set() for u in old60}
    for u,v in finalold:oldadj[u].add(v);oldadj[v].add(u)
    ports={u:8-len(oldadj[u]) for u in old60};zero=[];forced=set()
    for u in sorted(old60):
        if ports[u]:continue
        missingold=[v for v in sorted(old60) if v!=u and v not in oldadj[u] and not oldadj[u]&oldadj[v]]
        forced.update(tuple(sorted((u,v))) for v in missingold)
        capacity=sum(ports[v] for v in oldadj[u])
        zero.append({'vertex':u,'old_neighbors':sorted(oldadj[u]),'old_pairs_without_old_path':[[u,v] for v in missingold],
          'neighbor_port_sum':capacity,'required_auxiliary_vertices':8,
          'forced_old_auxiliary_bad_pair_count':max(0,8-capacity)})
    obstruction={'labels':'original order60 labels','old_vertices':sorted(old60),
      'old_induced_edge_count':len(finalold),'old_port_counts':ports,
      'zero_port_checks':zero,'unavoidable_zero_port_old_pairs':sorted(forced),
      'unavoidable_old_auxiliary_bad_pair_count':sum(x['forced_old_auxiliary_bad_pair_count'] for x in zero),
      'fixed_old_core_bad_pair_lower_bound':len(forced)+sum(x['forced_old_auxiliary_bad_pair_count'] for x in zero),
      'scope':'Only completions keeping this selected best graph old induced graph, with arbitrary attachments and auxiliary edges'}
    (OUT/'neighborhood.best.old_core_obstruction.json').write_text(json.dumps(obstruction,indent=2)+'\n')
    checked=bfs(58,graph);before=bfs(58,seed)
    assert checked['bad_pair_count']==r['minimum_bad_pairs'] and before['bad_pair_count']==21
    oldbad={(p['u'],p['v']) for p in before['bad_pairs']};newbad={(p['u'],p['v']) for p in checked['bad_pairs']}
    checked['bad_pair_changes']={'repaired':sorted(oldbad-newbad),'introduced':sorted(newbad-oldbad),'retained':sorted(oldbad&newbad)}
    (OUT/'neighborhood.best.verification.json').write_text(json.dumps(checked,indent=2)+'\n')
    (OUT/'neighborhood.best.json').write_text(json.dumps({'n':58,'edges':sorted(graph),'removed_order58':sorted(removed),'added_order58':sorted(added)},indent=2)+'\n')
    result={'best_graph_exact_edit_replayed':True,'independent_all_source_bfs_verified':True,
      'independent_15_pattern_classification':dict(kinds),'independent_disjoint_triple_count':disjoint,
      'edit_difference_is_one_alternating_six_cycle':True,
      'minimum_bad_pairs':checked['bad_pair_count'],'distance_histogram':checked['distance_histogram'],
      'net_deleted_hs_edges_original60':sorted(hs-finalold),'added_old_edges_original60':sorted(finalold-hs),
      'removed_edges_original60':sorted((label(u),label(v)) for u,v in removed),
      'added_edges_original60':sorted((label(u),label(v)) for u,v in added),
      'repaired_old_bad_pairs':len(oldbad-newbad),'introduced_bad_pairs':len(newbad-oldbad),
      'retained_bad_pairs':len(oldbad&newbad),'improved_over_seed':checked['bad_pair_count']<21,
      'unavoidable_zero_port_old_pairs_for_fixed_best_core':sorted(forced),
      'fixed_best_old_core_bad_pair_lower_bound':obstruction['fixed_old_core_bad_pair_lower_bound'],
      'valid_degree8_diameter2':checked['valid_degree8_diameter2']}
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
