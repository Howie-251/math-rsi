"""BareK41356: exact ordinary-clone domain and explicit integer row-cover upper bound."""
from pathlib import Path
from collections import Counter,defaultdict
from fractions import Fraction
import heapq,json,sys,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
start=time.process_time();assert (HERE/'PREDICTION.json').exists()
previous=ROOT/'research/ddp/global_coverage_20261027/h9_clone_capacity'
source=ROOT/'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout'
pads=json.loads((source/'partial_fold_source/witnesses/pf_d12_k5_n41699.json').read_text())['pad']
N=41356;adj=[[] for _ in range(N)];copy_neighbors=[[] for _ in range(280)];edges=[]
with (previous/'core.edges').open() as f:
    n,m=map(int,next(f).split());assert (n,m)==(41636,237006)
    count=0
    for line in f:
        u,v=map(int,line.split());assert 0<=u<v<n;count+=1
        if v<N:
            edges.append((u,v));adj[u].append(v);adj[v].append(u)
        elif u<N:copy_neighbors[v-N].append(u)
    assert count==m
assert len(pads)==63 and all(v<N for v in pads)
degree=[len(vs) for vs in adj];deficit=[12-d for d in degree]
assert min(degree)>0 and max(degree)<=12
signature=defaultdict(list)
for v,ns in enumerate(adj):signature[tuple(sorted(ns))].append(v)
copy_mapping=[]
for i,ns in enumerate(copy_neighbors):
    key=tuple(sorted(ns));assert key in signature
    v=min(signature[key]);assert sorted(adj[v])==list(key)
    copy_mapping.append(dict(source_extra_vertex=N+i,prototype=v,old_K_neighbors=list(key)))
known=Counter(pads)
for r in copy_mapping:known[r['prototype']]+=1
assert sum(known.values())==343
knownload=[sum(known[v] for v in ns) for ns in adj]
assert all(knownload[u]<=deficit[u] for u in range(N))
blocker=[next((u for u in ns if deficit[u]==0),-1) for ns in adj]
allowed=[v for v in range(N) if blocker[v]<0]
assert all(v in allowed for v in known)
upper={v:min(deficit[u] for u in adj[v]) for v in allowed}
rows={u:sorted(v for v in ns if blocker[v]<0) for u,ns in enumerate(adj)}
rows={u:vs for u,vs in rows.items() if vs}
assert all(deficit[u]>0 for u in rows)
uncovered=set(allowed)
heap=[(-Fraction(len(vs),deficit[u]),deficit[u],u) for u,vs in rows.items()];heapq.heapify(heap)
cover=[]
while uncovered:
    score,cost,u=heapq.heappop(heap);new=uncovered.intersection(rows[u])
    if not new:continue
    actual=-Fraction(len(new),cost)
    if actual!=score:
        heapq.heappush(heap,(actual,cost,u));continue
    cover.append(dict(vertex=u,weight=1,deficit=cost,clone_variables=rows[u],newly_covered=sorted(new)))
    uncovered.difference_update(new)
cover_vertices={r['vertex'] for r in cover}
assert all(any(u in cover_vertices for u in adj[v]) for v in allowed)
cover_ub=sum(deficit[u] for u in cover_vertices);individual_ub=sum(upper.values());slots_ub=sum(deficit)//min(degree[v] for v in allowed)
UB=min(cover_ub,individual_ub,slots_ub)
coverage=Counter(v for r in cover for v in r['clone_variables'])
is_partition=coverage==Counter({v:1 for v in allowed})
partition_types=Counter((len(r['clone_variables']),r['deficit']) for r in cover)
known_attains_all_rows=all(sum(known[v] for v in r['clone_variables'])==r['deficit'] for r in cover)
summary=dict(status='GLOBAL_INTEGER_UPPER_BOUND_BELOW987' if UB<987 else 'CHEAP_BOUND_UNDECIDED_ONE_LP_ALLOWED',
             prediction_id='H9_BARE41356_ORDINARY_CLONE_THRESHOLD',
             source_core_file=str((previous/'core.edges').relative_to(ROOT)),
             bare_core_vertices=N,bare_core_edges=len(edges),degree_histogram=dict(sorted(Counter(degree).items())),
             total_degree_deficit=sum(deficit),saturated_vertices=sum(d==12 for d in degree),
             forced_zero_prototypes=N-len(allowed),allowed_prototypes=len(allowed),
             allowed_degree_histogram=dict(sorted(Counter(degree[v] for v in allowed).items())),
             per_variable_integer_upper_bound_histogram=dict(sorted(Counter(upper.values()).items())),
             nonempty_packing_rows=len(rows),known_feasible_clones=343,known_old_H3copies=280,known_old_pads=63,
             all280_H3copy_K_neighborhoods_match_some_K_prototype=True,known343_all_degree_budgets_pass=True,
             upper_bounds=dict(sum_individual_bounds=individual_ub,integer_row_cover=cover_ub,
                               number_cover_rows=len(cover),total_deficit_over_min_allowed_degree=slots_ub),
             global_clones_upper_bound=UB,total_order_upper_bound=N+UB,
             upper_bound_known_attained=UB==343,exact_optimum=343 if UB==343 else None,
             certificate_rows_partition_all_allowed_variables=is_partition,
             certificate_group_types=[dict(variables_per_group=k[0],budget=k[1],group_count=v) for k,v in sorted(partition_types.items())],
             known343_attains_every_certificate_row=known_attains_all_rows,
             required_clones=987,target_order=42343,target_Delta=12,target_D=5,savedL=42342,
             can_reach_target=UB>=987,hypothesis_result='SUPPORTED_GLOBAL_CAPACITY_EXCLUSION' if UB<987 else 'UNDECIDED',
             LP_calls=0,MILP_calls=0,BFS_count=0,default_author_verifier_run=False,new_target_graphs_generated=0,new_lower_bounds=0,
             scope='Fixed barepartialfoldK41356, allS/colors/edges fixed, any nonnegative ordinaryclone counts of ANYKvertex; clone neighborhoods exactlyNK(v), no new-new edges.',
             fixed41636_63_result_used_as_upper_bound=False,CPU_seconds=time.process_time()-start)
def strings(x):
    if isinstance(x,str):return [x]
    if isinstance(x,dict):return [s for y in x.values() for s in strings(y)]
    if isinstance(x,(list,tuple)):return [s for y in x for s in strings(y)]
    return []
def save(fn,x):
    assert not screen('\n'.join(strings(x)))
    (HERE/fn).write_text(json.dumps(x,indent=2)+'\n')
save('clone_packing.json',dict(model='max sumt; t>=0integer; sum_{v in NK(u)}t_v<=12-degreeK(u)',
                             variables=[dict(vertex=v,degree=degree[v],upper_bound=upper[v],K_neighbors=sorted(adj[v])) for v in allowed],
                             budget_rows=[dict(vertex=u,deficit=deficit[u],clone_variables=vs) for u,vs in sorted(rows.items())],
                             known_feasible343=[dict(vertex=v,copies=t) for v,t in sorted(known.items())]))
save('forced_zero.json',dict(rule='saturatedKneighborforcesclonecountzero',saturated_neighbor_witness_by_vertex=blocker))
save('bare_core_degrees.json',dict(n=N,degrees=degree,deficits=deficit))
save('old343_clone_mapping.json',dict(H3copy_mapping=copy_mapping,padding_prototypes=pads,
                                     known_feasible343=[dict(vertex=v,copies=t) for v,t in sorted(known.items())],
                                     old_extra_extra_edges_not_used=True))
save('integer_upper_bound.json',dict(type='nonnegative integer dualrowcover',rows=cover,total_budget=cover_ub,
                                   every_allowed_variable_covered=True,
                                   proof='Sum chosen budget inequalities: every allowedclone variable has coefficient>=1 and every forcedzero prototype is zero, so totalclones<=sum selecteddeficits.'))
(HERE/'bare_core.edges').write_text(f'{N} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in edges))
save('RESULT.json',summary);save('terminal.json',summary)
print(json.dumps(summary,indent=2))
