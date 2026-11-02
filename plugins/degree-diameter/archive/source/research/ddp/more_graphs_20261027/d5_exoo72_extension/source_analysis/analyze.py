"""Targeted local route/critical-edge analysis. No source BFS or tuple scan."""
import collections,json,pathlib,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(119,120))
P=pathlib.Path(__file__).resolve().parent;ROOT=P.parents[4];start=time.process_time()
SRC=ROOT/'research/ddp/more_graphs_20261027/d3d4_transfer/source72.implicit_adj.txt'
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
save('PREDICTION.json',{'prediction_id':'P_EXOO72_CRITICAL_EDGE_MATCHING','frozen_before_local_cycle_and_route_counts':True,
 'falsifiable_prediction':'Every source edge has a critical-pair graph with matching size at least6. If true, deleting any sourceedge cannot be repaired by one degree<=5 new vertex without adding old-old edges.',
 'rationale':'Source72 is close to its five-degree three-step route limits and likely uses many unique short routes. A degree5 newvertex can fix a lost <=3 old-old route only if at least one oldendpoint is among its5 neighbors. Six disjoint forced losses are a uniform obstruction.',
 'target':[5,3],'savedL':72,'n':{'actual':None,'hypothetical':73},'scope':'One new vertex, preserve sourceold-old edges except deletions, no old-old additions. Predictiontestedby local<=3 path supports, not graph BFS or candidate tuplegrid.',
 'no_counteragent_ORscan_overlap':True,'workers':1,'CPU_budget_seconds':120})
adj=[set(map(int,line.split()))for line in SRC.read_text().splitlines()if line.strip()];n=len(adj)
assert n==72 and all(len(v)==5 for v in adj)
edges=sorted((u,v)for u in range(n)for v in adj[u]if u<v);ix={e:i for i,e in enumerate(edges)}
assert len(edges)==180 and all(u in adj[v]for u in range(n)for v in adj[u])

def rho(u,k=1):return u//12*12+(u%12+k)%12
rho_aut=all(tuple(sorted((rho(u),rho(v))))in ix for u,v in edges)
assert rho_aut
left=set(edges);orbits=[]
while left:
 e=min(left);orbit=sorted({tuple(sorted((rho(e[0],k),rho(e[1],k))))for k in range(12)})
 orbits.append({'representative':e,'size':len(orbit),'edges':orbit});left.difference_update(orbit)
triangles=sorted((u,v,w)for u,v in edges for w in adj[u]&adj[v]if v<w)
squares=sum(len(adj[u]&adj[v])*(len(adj[u]&adj[v])-1)//2 for u in range(n)for v in range(u+1,n))//2
# Every simplepath of length<=3; for each pair preserve path supports and their intersection.
supports={};paths={};counts=collections.Counter()
for root in range(n):
 def visit(path,mask):
  u=path[-1]
  if len(path)>1 and root<u:
   key=(root,u);supports.setdefault(key,[]).append(mask);paths.setdefault(key,[]).append(path[:]);counts[len(path)-1]+=1
  if len(path)==4:return
  for v in sorted(adj[u]):
   if v in path:continue
   eid=ix[tuple(sorted((u,v)))];visit(path+[v],mask|(1<<eid))
 visit([root],0)
critical=[[]for _ in edges];pair_details={};unique3=[];length_hist=collections.Counter();multi3=collections.Counter()
for key,vals in supports.items():
 inter=vals[0]
 for mask in vals[1:]:inter&=mask
 length=min(len(p)-1 for p in paths[key]);length_hist[length]+=1
 if length==3:
  multi3[len(vals)]+=1
  if len(vals)==1:unique3.append(key)
 pair_details[key]={'count':len(vals),'minimum_length':length,'paths':paths[key]}
 while inter:
  bit=inter&-inter;eid=bit.bit_length()-1;critical[eid].append(key);inter-=bit
# Exact maximum cardinality matching on each of just16 cyclic edge-orbit representatives.
# This is a small critical-pair graph calculation, not any source diameter verification.
import networkx as nx
cert=[]
for orbit in orbits:
 e=tuple(orbit['representative']);pairs=critical[ix[e]];K=nx.Graph();K.add_edges_from(pairs)
 matching=sorted(tuple(sorted(x))for x in nx.algorithms.matching.max_weight_matching(K,maxcardinality=True))
 selected=matching[:6]
 cert.append({'edge':e,'orbit_size':orbit['size'],'critical_pairs':len(pairs),'maximum_matching_size':len(matching),'six_disjoint_certificate':selected if len(selected)==6 else None,
 'critical_pair_witnesses':[{'pair':pair,**pair_details[pair]}for pair in selected]})
all_six=all(x['maximum_matching_size']>=6 for x in cert)
save('CRITICAL_MATCHING_CERTIFICATES.json',{'all_source_edges_covered_by_cyclic_orbits':True,'cyclic_action':'rho(12*t+i)=12*t+(i+1 mod12)','edge_orbits':orbits,'certificates':cert,'every_edge_has_six_disjoint_critical_pairs':all_six})
save('CRITICAL_PAIR_GRAPHS.json',{'edges':edges,'critical_pairs_by_edge':critical,'definition':'Pair{x,y} belongs K_e iff every simple oldsource path x->y of length<=3 contains e. Simplepaths suffice for allwalks because cycle removal shortens a path.'})
res={'status':'COMPLETE_TARGETED_SOURCE_ROUTE_DIAGNOSIS','prediction_id':'P_EXOO72_CRITICAL_EDGE_MATCHING','prediction_verdict':'SUPPORTED'if all_six else'REFUTED',
 'target_Delta':5,'target_D':3,'savedL':72,'n':{'actual':None,'hypothetical':73},'actual_D':None,'ordinary_bad_unordered_pairs':None,
 'source_path':str(SRC.relative_to(ROOT)),'source_n':72,'source_m':180,'source_degree_histogram':{'5':72},'source_all_BFS_repeated':False,
 'triangles':len(triangles),'squares':squares,'C12_shift_automorphism_verified':rho_aut,'C12_vertex_orbits':6,'edge_orbit_sizes':[o['size']for o in orbits],
 'path_length_histogram_pairs':dict(length_hist),'distance3_path_multiplicity_histogram':dict(sorted(multi3.items())),'unique_distance3_pairs':len(unique3),
 'critical_matching_sizes_by_edge_orbit':[{'edge':c['edge'],'orbit_size':c['orbit_size'],'size':c['maximum_matching_size'],'critical_pairs':c['critical_pairs']}for c in cert],
 'every_edge_has_six_disjoint_critical_pairs':all_six,'candidate_graphs_generated':0,'candidate_matching_triples_scanned':0,'source_BFS':0,'CPU_seconds':time.process_time()-start,
 'scope':'Only the actual Exoo72source and one newvertex withno old-old edge additions; no general73graph impossibility. Ifpredictionfails, this matchingcertificate doesnotexclude the operation.',
 'pending':[]}
save('RESULT.json',res)
print('CYCLES',len(triangles),squares,'orbits',len(orbits));print('CRITICAL',[(a['edge'],a['maximum_matching_size'],a['critical_pairs'])for a in cert]);print('PRED',res['prediction_verdict'],'paths',dict(length_hist),'uniqueD3',len(unique3),'CPU',res['CPU_seconds'])
