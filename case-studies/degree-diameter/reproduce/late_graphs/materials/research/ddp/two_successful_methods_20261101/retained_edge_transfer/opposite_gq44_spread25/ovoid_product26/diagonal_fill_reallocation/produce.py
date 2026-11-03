"""One fixed clone/filler reallocation; no BFS, geometry, field or Lean calls."""
import collections,json,os,resource,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
D=Path(__file__).resolve().parent;P=D.parent
def save(name,value):
    path=D/name;tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(value,indent=2)+'\n');os.replace(tmp,path)
source=P/'graph_d26_D3_n7531.edges';centerpath=P/'ORDERED_CENTERS.json'
rows=json.loads(centerpath.read_text())['centers'];assert len(rows)==289
deletions={};rawpins={};ordered_delta=[]
for r in rows:
    idx=r['index'];clone=7242+idx;center=r['old_center_label'];j=r['spread_index']
    pins=sorted(set(r['raw_neighborhood_ordered'])-{center})
    full=sorted(r['source_full_neighborhood_ordered']);rawpins[clone]=pins
    if r['is_incident_flag']:
        filler=7225+j;edge=(filler,clone);assert edge not in deletions
        assert len(pins)==24 and sorted(pins+[filler])==full
        deletions[edge]=idx;ordered_delta.append(dict(index=idx,point=r['point'],spread_index=j,spread_line=r['spread_line'],center_label=center,clone_label=clone,deleted_edge=list(edge),new_hub_edge=[filler,7531]))
    else:assert len(pins)==25 and pins==full
assert len(deletions)==17 and {e[0]for e in deletions}==set(range(7225,7242))
retained=[];found=set();input_count=0;source_count=0;previous=None
with source.open()as f:
    assert tuple(map(int,f.readline().split()))==(7531,97750)
    for line in f:
        edge=tuple(map(int,line.split()));a,b=edge
        assert 0<=a<b<7531 and(previous is None or previous<edge)
        previous=edge;input_count+=1
        if b<7242:source_count+=1
        if edge in deletions:found.add(edge)
        else:retained.append(edge)
assert input_count==97750 and source_count==90525 and found==set(deletions)
added=[(7225+j,7531)for j in range(17)]
edges=sorted(retained+added);assert len(edges)==97750
adj=[set()for _ in range(7532)]
for a,b in edges:
    assert a<b and b not in adj[a];adj[a].add(b);adj[b].add(a)
assert sum(b<7242 for a,b in edges)==source_count
assert all(sorted(adj[clone])==pins for clone,pins in rawpins.items())
assert adj[7531]==set(range(7225,7242))
hist=collections.Counter(map(len,adj));assert dict(hist)=={26:7225,25:289,24:17,17:1},hist
filler_owner={}
for f in range(7225,7242):
    for pin in adj[f]:
        if pin<7225:
            assert pin not in filler_owner;filler_owner[pin]=f
assert len(filler_owner)==425
walkrows=[]
for r in rows:
    clone=7242+r['index'];flag=next(pin for pin in sorted(adj[clone])if pin in filler_owner)
    filler=filler_owner[flag]
    assert filler in adj[7531]and flag in adj[filler]and clone in adj[flag]
    walkrows.append((r['index'],clone,filler,flag))
# One direct pair/neighborhood witness, not a source-root BFS.
u=0;v=next(v for v in range(1,7225)if v not in adj[u]and adj[u].isdisjoint(adj[v]))
assert u not in adj[v]
out=D/'graph_d26_D3_n7532.edges';tmp=out.with_suffix('.edges.partial')
with tmp.open('w')as f:
    f.write('7532 97750\n');f.writelines(f'{a} {b}\n'for a,b in edges)
os.replace(tmp,out)
save('EDGE_DELTA.json',dict(deleted=ordered_delta,inserted=[list(e)for e in added]))
with(D/'HUB_CLONE_THREE_WALKS.tsv').open('w')as f:
    f.write('clone_index\tclone_label\tfiller_label\tflag_pin\n')
    f.writelines('\t'.join(map(str,row))+'\n'for row in walkrows)
witness=dict(pair=[u,v],both_in_original_U=True,adjacent=False,common_neighbors=[],u_neighbors=sorted(adj[u]),v_neighbors=sorted(adj[v]),method='direct nonedge and neighbor-set intersection, not BFS')
save('NON_D2_OLD_U_WITNESS.json',witness)
parameters=dict(n=7532,m=97750,max_degree=26,D_target=3,degree_histogram={str(k):hist[k]for k in sorted(hist)},input_7531='../graph_d26_D3_n7531.edges',original_filled_source='../../graph_d25_D3_n7242.edges',source_H_n=7242,source_H_m=90525,source_H_old_edges_retained=True,source_U_n=7225,clone_count=289,clone_labels='7242+index0..288',center_table='../ORDERED_CENTERS.json',center_order='unchanged original ordered 17point x17spread list',clone_neighborhood='open neighborhood in original unfilled U; remove center itself from raw Cartesian row',diagonal_condition='is_incident_flag; spread_index is actual frozen owner, not ovoid index',deleted_edges=17,added_hub_label=7531,hub_neighbors=list(range(7225,7242)),inserted_edges=17,new_clone_new_clone_edges=0,format='n m header; strict lexicographic a b, a<b',predicted_newroot_histograms=dict(diagonal=dict(roots=17,histogram=[1,24,418,7089]),offdiagonal=dict(roots=272,histogram=[1,25,441,7065]),hub=dict(roots=1,histogram=[1,17,425,7089])),producer_BFS_runs=0,fresh_independent_acceptance='PENDING_SEPARATE_AGENT',Lean='NOT_AUTHORIZED_IN_THIS_BATCH',global_or_priority_certified=False)
save('PARAMETERS.json',parameters)
result=dict(status='FIXED7532_PRODUCER_PASS_PENDING_FRESH_DIAMETER_ACCEPTANCE',n=7532,m=97750,max_degree=max(hist),degree_histogram=parameters['degree_histogram'],source_input_parses=1,input_header=[7531,97750],input_strict_simple_lex=True,all90525_source_H_edges_retained=True,deleted_exact17_diagonal_filler_clone_edges=True,inserted_exact17_hub_filler_edges=True,all289_clone_open_U_neighborhoods_bound=True,diagonal_clone_degree=24,offdiagonal_clone_degree=25,hub_degree=17,hub_to_clone_three_walk_rows=len(walkrows),actual_nonD2_oldU_pair=witness['pair'],producer_BFS_runs=0,old_geometry_field_Lean_solver_runs=0,CPU_seconds=time.process_time(),CPU_budget_seconds=20,failed_attempts=0,output=str(out),new_graphs_counted_by_producer=0)
save('RESULT.json',result)
save('TERMINAL.json',dict(status='PRODUCER_TERMINAL_FIXED7532_FILE_CLOSED_FRESH_ACCEPTANCE_PENDING',running=False,active_processes=[],CPU_seconds=result['CPU_seconds'],CPU_budget_seconds=20,output=str(out),new_graphs_counted_by_producer=0))
print(json.dumps(result),flush=True)
