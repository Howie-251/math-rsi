"""Recover the fixed author core; exact ordinary-clone packing and cheap integer bounds."""
from pathlib import Path
from collections import Counter
import json,lzma,sys,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
start=time.process_time()
SOURCE=ROOT/'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout'
assert (HERE/'PREDICTION.json').exists()
W=json.loads((SOURCE/'partial_fold_source/witnesses/pf_d12_k5_n41699.json').read_text())
pads=W['pad'];assert len(pads)==63
cached=json.loads((SOURCE/'structure_check.json').read_text())
N=41636;adj=[[] for _ in range(N)];pad_adj=[set() for _ in pads];edges=set();final_degrees=[0]*41699
with lzma.open(SOURCE/'partial_fold_source/graph_d12k5_n41699.edges.xz','rt') as f:
    n,m=map(int,next(f).split());assert n==41699
    edge_count=0
    for line in f:
        u,v=map(int,line.split());assert 0<=u<v<n
        final_degrees[u]+=1;final_degrees[v]+=1;edge_count+=1
        if v<N:
            assert (u,v) not in edges
            edges.add((u,v));adj[u].append(v);adj[v].append(u)
        else:
            assert u<N
            pad_adj[v-N].add(u)
    assert edge_count==m
assert all(pad_adj[i]==set(adj[p]) for i,p in enumerate(pads))
deg=[len(a) for a in adj];deficit=[12-x for x in deg]
assert Counter(deg)==Counter({int(k):v for k,v in cached['core']['degree_histogram'].items()})
assert max(deg)==12 and min(deg)==10 and sum(deficit)==25620
known=Counter(pads);known_load=[sum(known[v] for v in row) for row in adj]
assert all(known_load[u]<=deficit[u] for u in range(N))
assert all(deg[u]+known_load[u]==final_degrees[u] for u in range(N))
blocker=[next((u for u in row if deficit[u]==0),-1) for row in adj]
allowed=[v for v in range(N) if blocker[v]<0]
upper={v:min(deficit[u] for u in adj[v]) for v in allowed}
variables=[dict(vertex=v,core_degree=deg[v],integer_lower_bound=0,integer_upper_bound=upper[v],old_neighbors=sorted(adj[v])) for v in allowed]
row_vars={u:sorted(v for v in adj[u] if blocker[v]<0) for u in range(N)}
row_vars={u:vs for u,vs in row_vars.items() if vs}
assert all(deficit[u]>0 for u in row_vars)
# Valid nonnegative integer dual: chosen budget rows cover every allowed clone variable.
uncovered=set(allowed);cover=[]
while uncovered:
    choices=[(2*len(uncovered.intersection(vs))//deficit[u],-deficit[u],-u,u,uncovered.intersection(vs)) for u,vs in row_vars.items()]
    _,_,_,u,covered=max(choices,key=lambda t:t[:3])
    assert covered
    cover.append(dict(vertex=u,weight=1,deficit=deficit[u],newly_covered_clone_vertices=sorted(covered)))
    uncovered.difference_update(covered)
cover_vertices={r['vertex'] for r in cover}
assert all(any(u in cover_vertices for u in adj[v]) for v in allowed)
cover_ub=sum(deficit[u] for u in cover_vertices)
individual_ub=sum(upper.values())
global_slot_ub=sum(deficit)//min((deg[v] for v in allowed),default=10)
UB=min(cover_ub,individual_ub,global_slot_ub)
pair_cover=[dict(budget_vertex=r['vertex'],deficit=r['deficit'],clone_vertices=row_vars[r['vertex']],
                 author_chosen_prototypes=[v for v in row_vars[r['vertex']] if known[v]]) for r in cover]
is_disjoint_pair_cover=(all(r['deficit']==1 and len(r['clone_vertices'])==2 for r in pair_cover)
    and Counter(v for r in pair_cover for v in r['clone_vertices'])==Counter({v:1 for v in allowed}))
if is_disjoint_pair_cover:
    assert all(sum(known[v] for v in r['clone_vertices'])==1 for r in pair_cover)
summary=dict(status='CHEAP_INTEGER_UPPER_BOUND_DECIDES_BELOW707' if UB<707 else 'CHEAP_BOUND_UNDECIDED_NEEDS_ONE_FURTHER_CAPACITY_STEP',
             prediction_id='H9_FIXED41636_ORDINARY_CLONE_CAPACITY',
             source_edge_file=str((SOURCE/'partial_fold_source/graph_d12k5_n41699.edges.xz').relative_to(ROOT)),
             core_vertices=N,core_edges=len(edges),core_degree_histogram=dict(sorted(Counter(deg).items())),
             core_free_degree_slots=sum(deficit),saturated_core_vertices=sum(d==12 for d in deg),
             forbidden_clone_prototypes=N-len(allowed),allowed_clone_prototypes=len(allowed),
             allowed_degree_histogram=dict(sorted(Counter(deg[v] for v in allowed).items())),
             allowed_individual_ub_histogram=dict(sorted(Counter(upper.values()).items())),
             upper_bounds=dict(sum_individual_clone_bounds=individual_ub,chosen_budget_row_cover=cover_ub,
                               total_free_slots_divided_by_min_allowed_degree=global_slot_ub),
             global_total_clones_upper_bound=UB,known_feasible_clones=sum(known.values()),
             upper_bound_attained_by_known_author_padding=UB==sum(known.values()),
             disjoint_pair_cover=is_disjoint_pair_cover,disjoint_pair_budget_rows=len(pair_cover) if is_disjoint_pair_cover else None,
             final_graph_order_upper_bound=N+UB,target_order=42343,savedL=42342,required_total_clones=707,
             target_Delta=12,target_D=5,can_reach_savedL_plus1_under_this_template=UB>=707,
             known_author_padding_verified_against_core=True,all_original63_twin_neighborhoods_match=True,
             core_degree_histogram_matches_prior_structure_check=True,
             hypothesis_result='SUPPORTED_BY_EXPLICIT_GLOBAL_INTEGER_UPPER_BOUND' if UB<707 else 'NOT_DECIDED_BY_CHEAP_BOUNDS',
             graph_BFS_count=0,author_default_verifier_run=False,LP_calls=0,MILP_calls=0,new_target_graphs_generated=0,
             new_lower_bounds=0,scope='Fixed author41636core with all edges retained and S/colors/H3copies frozen; one batch of arbitrary ordinary full-neighborhood clones of core vertices, no new-new edges.',
             CPU_seconds=time.process_time()-start)
def strings(x):
    if isinstance(x,str):return [x]
    if isinstance(x,dict):return [s for y in x.values() for s in strings(y)]
    if isinstance(x,(list,tuple)):return [s for y in x for s in strings(y)]
    return []
def save(name,x):
    assert not screen('\n'.join(strings(x)))
    (HERE/name).write_text(json.dumps(x,indent=2)+'\n')
save('clone_packing.json',dict(model='max sum_v t_v, t_v nonnegative integers; sum_{v in Ncore(u)}t_v<=12-degcore(u)',
                             variable_count=len(variables),nonempty_constraint_count=len(row_vars),variables=variables,
                             budget_rows=[dict(vertex=u,deficit=deficit[u],clone_variables=vs) for u,vs in sorted(row_vars.items())],
                             known_feasible_author_clones=[dict(vertex=v,copies=c) for v,c in sorted(known.items())]))
save('forbidden_prototypes.json',dict(rule='Any saturated old neighbor forces t_v=0',saturated_neighbor_witness_by_core_vertex=blocker))
save('integer_upper_bound.json',dict(type='nonnegative integer packing dual row cover',
                                   rows=cover,total_budget=cover_ub,
                                   all_allowed_variables_covered=True,individual_bound_sum=individual_ub,
                                   proof='Sum the selected oldvertex degree-budget inequalities. Each allowed clone variable occurs at least once, hence total clones<=sum selected deficits. Forbidden variables are zero.'))
save('pair_cover_certificate.json',dict(is_disjoint_pair_cover=is_disjoint_pair_cover,
                                      every_allowed_variable_occurs_exactly_once=is_disjoint_pair_cover,
                                      budget_rows=pair_cover,total_upper_bound=cover_ub,
                                      author_clones_attain_one_per_pair=is_disjoint_pair_cover))
save('core_degrees.json',dict(n=N,degrees=deg,deficits=deficit))
(HERE/'core.edges').write_text(f'{N} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
save('RESULT.json',summary);save('terminal.json',summary)
print(json.dumps(summary,indent=2))
