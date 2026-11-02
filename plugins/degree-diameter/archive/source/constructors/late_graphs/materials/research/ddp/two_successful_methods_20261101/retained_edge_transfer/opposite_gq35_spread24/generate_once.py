from pathlib import Path
from collections import Counter,deque
import itertools,json,time,resource,os
D=Path(__file__).resolve().parent;START=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(44,45))
def save(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
def mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return z
def pt(a,b,c):return a+4*b+16*c
P=[(k%4,k//4%4,k//16) for k in range(64)]
PG=[(1,t) for t in range(4)]+[(0,1)]
vertical=[tuple(pt(a,b,c) for a in range(4)) for c in range(4) for b in range(4)]
ordinary={};raw_ordinary_count=0
for k,(a,b,c) in enumerate(P):
    for j,(d1,d2) in enumerate(PG):
        v=(mul(b,d2)^mul(c,d1),d1,d2)
        L=tuple(sorted(pt(a^mul(t,v[0]),b^mul(t,v[1]),c^mul(t,v[2])) for t in range(4)))
        raw_ordinary_count+=1;ordinary.setdefault(L,{'anchor_point':k,'projective_direction_index':j,'projective_direction':[d1,d2],'affine_direction':v})
lines=vertical+sorted(ordinary)
checks={'point_count':64,'raw_ordinary_line_occurrences':raw_ordinary_count,'distinct_ordinary_lines':len(ordinary),'vertical_lines':len(vertical),'all_lines':len(lines),'all_lines_size4':all(len(set(L))==4 for L in lines),'distinct_lines':len(set(lines))}
if len(ordinary)!=80 or len(lines)!=96 or not checks['all_lines_size4'] or len(set(lines))!=96:
    save('COUNTEREXAMPLE.json',{'status':'GQ_LINE_COUNT_FAIL','checks':checks});raise SystemExit('GQ count counterexample saved')
incident=[[] for _ in P];line_sets=[set(L) for L in lines];pair_line={};pair_bad=None
for l,L in enumerate(lines):
    for p in L:incident[p].append(l)
    for p,q in itertools.combinations(L,2):
        if (p,q) in pair_line:pair_bad={'points':[p,q],'lines':[pair_line[p,q],l]}
        pair_line[p,q]=l
checks['point_incidence_histogram']=dict(Counter(map(len,incident)));checks['distinct_points_at_most_one_line']=pair_bad is None
if pair_bad or not all(len(row)==6 for row in incident):save('COUNTEREXAMPLE.json',{'status':'GQ_INCIDENCE_FAIL','checks':checks,'counterexample':pair_bad});raise SystemExit('GQ incidence counterexample saved')
collinear=[{p} for p in range(64)]
for L in lines:
    for p in L:collinear[p].update(L)
axiom_count=0;projections=[];bad=None
for p in range(64):
    for l,L in enumerate(line_sets):
        if p in L:continue
        projected=sorted(collinear[p]&L);axiom_count+=1
        if len(projected)!=1:bad={'point':p,'line':l,'collinear_on_line':projected};break
        projections.append([p,l,projected[0]])
    if bad:break
checks.update(nonincident_point_line_axioms_checked=axiom_count,all_unique_projection_axioms=bad is None,verticals_partition_points=sorted(x for L in vertical for x in L)==list(range(64)))
if bad or not checks['verticals_partition_points']:save('COUNTEREXAMPLE.json',{'status':'GQ_AXIOM_OR_SPREAD_FAIL','checks':checks,'counterexample':bad});raise SystemExit('GQ axiom counterexample saved')
assert axiom_count==5760
save('GQ_AXIOM_CHECK.json',{'status':'PASS_LITERAL_GQ_3_5','checks':checks,'field_multiplication_table':[[mul(a,b) for b in range(4)] for a in range(4)],'CPU_seconds':time.process_time()-START})
params={'field':'GF4=F2[w]/(w^2+w+1), binary labels0,1,w,w+1','point_label':'a+4*b+16*c','points':P,'projective_directions':PG,'lines':[{'line':l,'kind':'vertical' if l<16 else 'ordinary','points':list(L),**({} if l<16 else ordinary[L])} for l,L in enumerate(lines)],'point_incident_lines':incident,'spread_line_labels':list(range(16)),'old_vertex_label':'96*point+line','old_adjacency':'(p,l)~(q,m) iff p in m and q in l; distinct vertices only','new_vertex_label':'6144+spread_line_label','new_pins':'all flags(a,b) with a on this vertical spread line and a on b','q_scope':'GF4 only; fixed vertical spread'}
save('PARAMETERS.json',params)
# Complete old graph from literal incidence; no BFS on the6144-source graph.
adj=[set() for _ in range(6144)]
for p in range(64):
    for l,L in enumerate(lines):
        u=96*p+l
        for q in L:
            for m in incident[p]:
                v=96*q+m
                if u!=v:adj[u].add(v)
assert all(u not in row and all(u in adj[v] for v in row) for u,row in enumerate(adj))
olddegrees=list(map(len,adj));oldedges=[(u,v) for u,row in enumerate(adj) for v in row if u<v]
flags={96*p+l for p in range(64) for l in incident[p]}
assert len(flags)==384 and Counter(olddegrees)=={23:384,24:5760} and len(oldedges)==73536
assert {u for u,d in enumerate(olddegrees) if d==23}==flags
save('SOURCE_CHECK.json',{'status':'PASS_LITERAL_OPPOSITE_GQ35_SOURCE','n':6144,'m':len(oldedges),'degree_histogram':dict(Counter(olddegrees)),'simple':True,'symmetry_checked':True,'degree23_flags':sorted(flags),'flag_count':384,'old_source_BFS_runs':0,'source_D3_basis':'GQ unique-projection length<=3 walk proof in PROOF.md; no source all-roots BFS','CPU_seconds':time.process_time()-START})
pins=[sorted(96*a+b for a in vertical[i] for b in incident[a]) for i in range(16)]
assert all(len(S)==24 and len(set(S))==24 for S in pins) and sorted(x for S in pins for x in S)==sorted(flags)
steps=[]
for i,S in enumerate(pins):
    current_n=len(adj);dist=[-1]*current_n;queue=deque()
    for s in S:assert len(adj[s])==23;dist[s]=0;queue.append(s)
    while queue:
        u=queue.popleft()
        if dist[u]==2:continue
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;queue.append(v)
    missing=[u for u,d in enumerate(dist) if d<0]
    if missing:
        save('COUNTEREXAMPLE.json',{'status':'CURRENT_R2_COVER_FAIL','spread_line':i,'current_n':current_n,'missing_count':len(missing),'first_missing':missing[:20],'steps_passed':steps});raise SystemExit('Current coverage counterexample saved')
    assert max(len(adj[s]) for s in S)<24
    new=current_n;adj.append(set(S))
    for s in S:adj[s].add(new)
    assert max(map(len,adj))<=24
    steps.append({'spread_line':i,'new_vertex':new,'pins':S,'pin_count':24,'pin_degree_before':23,'current_n_before':current_n,'actual_current_closed_R2_pin_union_size':len(dist),'uncovered_targets':0,'pin_distance_histogram':dict(Counter(dist)),'previous_new_vertices_covered':i,'max_degree_after':max(map(len,adj))})
assert len(adj)==6160 and all(len(row)==24 for row in adj) and all(u not in row and all(u in adj[v] for v in row) for u,row in enumerate(adj))
edges=sorted((u,v) for u,row in enumerate(adj) for v in row if u<v);assert len(edges)==73920 and len(set(edges))==73920 and all(v in adj[u] for u,v in oldedges)
# One ordinary candidate-root connectivity BFS only, not diameter acceptance.
seen={0};q=deque([0])
while q:
    u=q.popleft()
    for v in adj[u]:
        if v not in seen:seen.add(v);q.append(v)
assert len(seen)==6160
with (D/'graph_d24_D3_n6160.edges').open('w') as f:
    f.write('6160 73920\n')
    for u,v in edges:f.write(f'{u} {v}\n')
save('EXTENSION_STEPS.json',{'status':'ALL16_CURRENT_COMPLETE_R2_EXTENSIONS_PASS','steps':steps,'all384_degree23_flags_used_once':True,'old_edges_retained':73536,'added_edges':384})
result={'status':'PRODUCER_COMPLETE_6160_CANDIDATE_READY_FOR_INDEPENDENT_ALLROOTS','n':6160,'m':73920,'Delta':24,'D_predicted':3,'degree_histogram':{'24':6160},'simple':True,'connected':True,'connectivity_BFS_roots':1,'connectivity_root':0,'source_allroots_BFS_runs':0,'candidate_allroots_BFS_runs':0,'actual_current_R2_cover_checks':16,'old_edges_retained':73536,'new_vertices':16,'new_edges':384,'solver_calls':0,'worker_count':1,'CPU_seconds':time.process_time()-START,'CPU_budget_seconds':45,'independent_acceptance_pending':True,'public_novelty_pending':True,'record_claimed':False,'running':False,'pending':['root independent complete6160-root verification','separate public inheritance comparison'],'edge_file':'graph_d24_D3_n6160.edges','parameters':'PARAMETERS.json'}
for name in ['RESULT.json','TERMINAL.json']:save(name,result)
print(json.dumps(result))
