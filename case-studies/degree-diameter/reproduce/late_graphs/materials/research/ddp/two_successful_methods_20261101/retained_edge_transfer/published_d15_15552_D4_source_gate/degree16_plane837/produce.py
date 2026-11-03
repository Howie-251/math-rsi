"""Single-read exact old-neighborhood cloning, with no graph search or BFS."""
import collections,csv,json,os,resource,time
from pathlib import Path
started=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(20,20))
D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'research/ddp/more_graphs_20261027').is_dir())
def save(name,value):(D/name).write_text(json.dumps(value,indent=2)+'\n')
save('DRIVER_HANDLE.json',dict(pid=os.getpid(),running=True,CPU_budget_seconds=20))
gate=json.loads((D.parent/'CONTROL_PACKING_RESULT.json').read_text())
assert gate['status']=='FOUND31'
I=gate['selected_controller_labels'];target_sets=gate['selected_target_sets']
assert len(I)==31 and len(set(x for row in target_sets for x in row))==155
offsets=[x0+9*x2+27*x3 for x3 in range(3)for x2 in range(3)for x0 in range(3)]
centers=[81*a+x for a in I for x in offsets]
assert centers==gate['selected_original_center_labels'] and len(set(centers))==837
source=R/'research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt'
adj=[]
with source.open()as f:
    for line in f:
        fields=list(map(int,line.split()))
        assert fields[0]==len(adj)
        # The literal source already omits virtualself.  Freeze it unchanged.
        adj.append(fields[1:])
assert len(adj)==15552
new_by_old=[[]for _ in adj];roles=[]
for j,c in enumerate(centers):
    neighbors=adj[c]
    assert c not in neighbors and len(neighbors)in[14,15]
    for v in neighbors:new_by_old[v].append(15552+j)
    roles.append(dict(j=j,controller_index=j//27,controller=I[j//27],local_offset=offsets[j%27],
        source_center_label=c,new_label=15552+j,literal_source_degree=len(neighbors),
        frozen_full_source_N=' '.join(map(str,sorted(neighbors)))))
loads=[len(row)for row in new_by_old]
assert max(loads)==1
added=sum(len(adj[c])for c in centers);m=116316+added;n=16389
graph=D/'graph_d16_D4_n16389.edges'
old_count=new_count=0
with graph.open('w')as f:
    f.write(f'{n} {m}\n')
    for u in range(15552):
        for v in sorted(adj[u]):
            if u<v:f.write(f'{u} {v}\n');old_count+=1
        for v in new_by_old[u]:f.write(f'{u} {v}\n');new_count+=1
assert old_count==116316 and new_count==added
with (D/'ALL837_ROLE_BINDINGS.tsv').open('w',newline='')as f:
    writer=csv.DictWriter(f,fieldnames=list(roles[0]),delimiter='\t');writer.writeheader();writer.writerows(roles)
degree_hist=collections.Counter(len(adj[v])+loads[v]for v in range(15552))
degree_hist.update(len(adj[c])for c in centers)
assert max(degree_hist)==16 and sum(degree_hist.values())==16389
center_hist=collections.Counter(len(adj[c])for c in centers)
parameters=dict(source_literal=str(source.relative_to(R)),source_n=15552,source_m=116316,
    source_degree_histogram={'14':648,'15':14904},source_D4_inherited_public=True,
    graph=str(graph.relative_to(R)),n=n,m=m,Delta=16,D=4,
    selected_controller_labels=I,selected_completed_target_sets=target_sets,
    plane='x1=0 in actual F3^4',ordered_offsets=offsets,
    ordered_clone_recipe='j=27*controller_index+offset_index; sourcecenter=81*I[controller_index]+offset; newlabel=15552+j',
    source_center_labels=centers,new_fullN_filter='use literal old simpleN after virtualself deletion at OLDcenter global label',
    no_newclone_label_refilter=True,added_edge_formula='sum_{837 centers} actual source degree14or15',
    public_located_baseline=16384,located_margin=5,global_priority='UNKNOWN')
save('PARAMETERS.json',parameters)
result=dict(status='PRODUCER_COMPLETE_LITERAL_D16_D4_N16389_FRESH_ACCEPTANCE_PENDING',
    n=n,m=m,maxdegree=16,source_body_edges_retained=old_count,new_edges=new_count,new_new_edges=0,
    source_literal_parse_count=1,old_source_regenerated=False,fullN_role_bindings=837,
    center_degree_histogram=dict(sorted(center_hist.items())),degree_histogram=dict(sorted(degree_hist.items())),
    old_pin_load_histogram=dict(sorted(collections.Counter(loads).items())),
    all_new_fullN_copied_from_original_simple_source=True,oldcenter_virtualself_not_reintroduced=True,
    header_written=True,strictlex_by_construction=True,
    actual_graph=str(graph.relative_to(R)),role_binding='ALL837_ROLE_BINDINGS.tsv',
    source_BFS=0,candidate_BFS=0,field_rank_solver_Lean_queries_paidreview_runs=0,
    trueWalk_allpair_and_prefix_proof='PROOF.md',fresh_allroot_scope_pending=16389,
    newroot_ownoldcenter_distance_prediction=2,distinctnewpair_distance_prediction=[3,4],
    everyroot_at_least6966_old_distance4_prediction=True,
    new_graph_parameter_Lean_count_increment=0,root_files_modified=False,
    CPU_seconds=time.process_time()-started,CPU_budget_seconds=20)
save('RESULT.json',result)
save('TERMINAL.json',dict(status=result['status'],running=False,CPU_seconds=result['CPU_seconds'],CPU_budget_seconds=20,
                        graph_closed=True,new_graph_accepted=False,Lean_authorized=False))
save('DRIVER_HANDLE.json',dict(status=result['status'],running=False,CPU_seconds=result['CPU_seconds']))
print(json.dumps(result))
