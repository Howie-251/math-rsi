import resource
resource.setrlimit(resource.RLIMIT_CPU,(13,13))
from pathlib import Path
from collections import Counter
import json,time
out=Path(__file__).resolve().parent;start=time.process_time();source=out.parents[1]/'second_mechanism/rajiv252.edges'
# Explicit project-relative original source; do not substitute the old254 graph.
source=Path('research/ddp/second_mechanism/rajiv252.edges')
def save(n,obj):(out/n).write_text(json.dumps(obj,indent=2)+'\n')
raw=[tuple(map(int,line.split())) for line in source.read_text().splitlines() if line.strip()]
assert len(raw)==630
edges=sorted(tuple(sorted(e)) for e in raw)
assert len(set(edges))==630 and all(len(e)==2 and 0<=e[0]<e[1]<252 for e in edges)
adj=[[] for _ in range(252)]
for eid,(u,v) in enumerate(edges):adj[u].append((v,eid));adj[v].append((u,eid))
assert all(len(a)==5 for a in adj)
for a in adj:a.sort()
save('INPUT.json',{'source_path':str(source),'source_status':'existing252/630/5regular/D4 evidence inherited; no source all-root BFS','n':252,'m':630,'edges_by_id':edges,'adjacency_with_edge_ids':adj,'proposed_rule':'remove F avoiding all edges at prototype x, with at least one removed incidence at each neighbor of x; addclone y with all5 oldneighbors of x','source_D4_reverified_by_BFS':False})
edgebit=[1<<i for i in range(630)];witnesses=[None]*630;rootstats=[];prefix_total=0;intersection_pair_count=0
with (out/'NONZERO_ROUTE_INTERSECTIONS.jsonl').open('w') as log:
 for root in range(252):
  inter=[None]*252;routecounts=[0]*252;firstpath=[None]*252;depthcounts=[0]*5
  stack=[(root,-1,0,0,(root,))]
  while stack:
   u,prev,depth,mask,path=stack.pop();depthcounts[depth]+=1;routecounts[u]+=1
   if inter[u] is None:inter[u]=mask;firstpath[u]=path
   else:inter[u]&=mask
   if depth==4:continue
   for v,eid in adj[u]:
    if v!=prev:stack.append((v,u,depth+1,mask|edgebit[eid],path+(v,)))
  assert depthcounts==[1,5,20,80,320] and all(x is not None for x in inter)
  prefix_total+=sum(depthcounts);critical_for_root=0;root_edge_union=0
  for target,mask in enumerate(inter):
   if not mask:continue
   critical_for_root+=1;intersection_pair_count+=1;root_edge_union|=mask;ids=[];left=mask
   while left:
    bit=left&-left;left-=bit;eid=bit.bit_length()-1;ids.append(eid)
    if witnesses[eid] is None:
     witnesses[eid]={'edge_id':eid,'edge':edges[eid],'first_root':root,'target':target,'all_NB_le4_routes_use_edge':True,'NB_routes_to_target':routecounts[target],'one_route':firstpath[target],'common_edge_ids':None}
   for eid in ids:
    if witnesses[eid]['first_root']==root and witnesses[eid]['target']==target:witnesses[eid]['common_edge_ids']=ids
   log.write(json.dumps({'root':root,'target':target,'NB_routes':routecounts[target],'common_edge_ids':ids})+'\n')
  rootstats.append({'root':root,'depth_wordcounts':depthcounts,'total_prefixes':426,'covered_endpoint_count':sum(x>0 for x in routecounts),'endpoints_with_nonzero_route_intersection':critical_for_root,'distinct_critical_edges_for_root':root_edge_union.bit_count()})
assert prefix_total==107352
critical=[i for i,w in enumerate(witnesses) if w is not None];noncritical=[i for i,w in enumerate(witnesses) if w is None];nonset=set(noncritical)
prototypes=[]
for x in range(252):
 supports=[]
 for v,e in adj[x]:
  support=[i for w,i in adj[v] if w!=x and i in nonset]
  supports.append({'neighbor':v,'noncritical_cut_edge_ids_avoiding_x_star':support})
 if all(s['noncritical_cut_edge_ids_avoiding_x_star'] for s in supports):prototypes.append({'prototype':x,'neighbor_supports':supports})
save('CRITICAL_WITNESSES.json',{'critical_edge_count':len(critical),'noncritical_edge_count':len(noncritical),'witnesses':[w for w in witnesses if w is not None],'edge_ids_derive_from':'INPUT.json edges_by_id','proof_condition':'For each witness root/target, intersect all426 NB<=4 prefix edge sets by endpoint; listed edge belongs to target intersection.'})
save('ROOT_COUNTS.json',rootstats)
save('NEIGHBORHOOD_NONCRITICAL_GATE.json',{'noncritical_edge_ids':noncritical,'eligible_prototypes':prototypes,'eligible_prototype_count':len(prototypes),'meaning':'Necessary only if positive: each neighbor can be touched by some individually noncritical edge avoiding the prototype star. Joint deletion need not preserve D4.'})
closed=not prototypes
r={'status':'COMPLETE_FIXED_SOURCE_CLONE_CUT_EXCLUDED' if closed else 'COMPLETE_CRITICALITY_GATE_OPEN_JOINT_CUT_GAP','prediction':'REFUTED_BY_STRICT_GATE' if closed else 'UNRESOLVED_NECESSARY_GATE_PASSED','target_Delta':5,'target_D':4,'savedL':252,'source_n':252,'source_m':630,'hypothetical_n':253,'target_actual_n':None,'target_actual_D':None,'ordinary_bad_unordered_pairs':None,'roots_enumerated':252,'NB_prefixes_per_root':426,'depthcounts_per_root':[1,5,20,80,320],'NB_prefixes_total':prefix_total,'endpoint_pairs_with_nonzero_route_intersection':intersection_pair_count,'critical_edges':len(critical),'noncritical_edges':len(noncritical),'eligible_prototypes_under_noncritical_necessary_gate':len(prototypes),'all_edges_critical':len(critical)==630,'scope':'Fixed original252 source; F avoids prototype star and a single newvertex duplicates the complete unchanged neighborhood. Not arbitrary253graphs or other source surgery.','CPU_seconds':time.process_time()-start,'BFS':0,'new_graphs':0,'cut_set_searches':0,'allroot_source_distance_reaudit':0}
save('WORKER_RESULT.json',r);save('checkpoint.json',{'status':r['status'],'roots_complete':252,'critical_edges':len(critical),'NB_prefixes':prefix_total});print(json.dumps(r),flush=True)
