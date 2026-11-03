"""Michel72 source endpoint eligibility: adjacency-set algebra, zero BFS/candidates."""
import collections,itertools,json,pathlib,resource,sys,time
from datetime import datetime,timezone
START=time.process_time();WALL=time.monotonic();resource.setrlimit(resource.RLIMIT_CPU,(5,5))
P=pathlib.Path(__file__).resolve().parent
ROOT=pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
source=P/'source/source72.edges';lines=source.read_text().splitlines();assert lines[0]=='72 180'
adj=[set() for _ in range(72)]
for line in lines[1:]:
 if line.strip():
  x,y=map(int,line.split());assert x!=y and y not in adj[x];adj[x].add(y);adj[y].add(x)
assert all(len(ns)==5 for ns in adj)
mask=lambda ns:sum(1<<v for v in ns)
adjm=[mask(ns) for ns in adj];ALL=(1<<72)-1
r2=[]
for v in range(72):
 ns={v}|adj[v]
 for x in adj[v]:ns|=adj[x]
 r2.append(mask(ns))
def ids(m):return [v for v in range(72) if (m>>v)&1]
counts=collections.Counter();first={};records=[];h=collections.Counter();r2hist=collections.Counter(x.bit_count() for x in r2);joint=0;mask_tests=0;neighbor_tests=0
for v in range(72):
 ns=sorted(adj[v]);outside=[x for x in range(72) if x!=v and x not in adj[v]];assert len(outside)==66
 F=ALL&~r2[v]
 for A_tuple in itertools.combinations(ns,2):
  A=list(A_tuple);B=[b for b in ns if b not in A];ua=ub=0
  for a in A:ua|=r2[a]
  for b in B:ub|=r2[b]
  EA=F&~ua;EB=F&~ub
  XA=[x for x in outside if EA&~r2[x]==0];XB=[x for x in outside if EB&~r2[x]==0]
  mask_tests+=132;XBmask=mask(XB)
  edge_pairs=[]
  for x in XA:
   neighbor_tests+=1
   for y in ids(adjm[x]&XBmask):edge_pairs.append([x,y])
  if not XA and not XB:category='BOTH_SIDES_EMPTY'
  elif not XA:category='A_ONLY_EMPTY'
  elif not XB:category='B_ONLY_EMPTY'
  elif not edge_pairs:category='BOTH_NONEMPTY_NO_SOURCE_EDGE'
  else:category='BOTH_NONEMPTY_WITH_SOURCE_EDGE'
  rec={'v':v,'A':A,'B':B,'source_targets_outside_R2_v':ids(F),'E_A':ids(EA),'E_B':ids(EB),'X_A':XA,'X_B':XB,'source_oriented_edges_XA_to_XB':edge_pairs,'joint_eligible_oriented_edges':len(edge_pairs),'category':category}
  records.append(rec);counts[category]+=1;first.setdefault(category,rec);h[(len(XA),len(XB),len(edge_pairs))]+=1;joint+=len(edge_pairs)
keys=['BOTH_SIDES_EMPTY','A_ONLY_EMPTY','B_ONLY_EMPTY','BOTH_NONEMPTY_NO_SOURCE_EDGE','BOTH_NONEMPTY_WITH_SOURCE_EDGE']
counts={key:counts[key] for key in keys}
r={'status':'COMPLETE_SOURCE_ELIGIBILITY_ONLY','timestamp_UTC':datetime.now(timezone.utc).isoformat(),'source':'source/source72.edges','source_n':72,'source_m':180,'source_simple':True,'source_regular_degree':5,'source_D3':'inherited official acceptance; not recomputed','source_closed_R2_construction':'{v} union N(v) union union_{u in N(v)} N(u)','closed_R2_ball_size_histogram':dict(sorted(r2hist.items())),'canonical_partitions':len(records),'eligible_endpoint_count_per_partition':66,'endpoint_mask_subset_tests':mask_tests,'source_neighbor_mask_intersections':neighbor_tests,'categories':counts,'at_least_one_side_empty':counts['BOTH_SIDES_EMPTY']+counts['A_ONLY_EMPTY']+counts['B_ONLY_EMPTY'],'both_nonempty':counts['BOTH_NONEMPTY_NO_SOURCE_EDGE']+counts['BOTH_NONEMPTY_WITH_SOURCE_EDGE'],'partitions_with_joint_eligible_edge':counts['BOTH_NONEMPTY_WITH_SOURCE_EDGE'],'total_joint_eligible_oriented_edge_parameters':joint,'first_witness_by_category':first,'coverer_size_and_edge_count_histogram':[{'X_A_size':a,'X_B_size':b,'oriented_edges':e,'partitions':n} for (a,b,e),n in sorted(h.items())],'prediction_disposition':'SUPPORTED_ELIGIBILITY_ONLY' if joint else 'REFUTED_FIXED_SOURCE_RULE','candidate_graphs':0,'BFS':0,'source_D3_BFS':0,'solver_calls':0,'full_73_parameter_edge_enumeration':0,'CPU_seconds':time.process_time()-START,'wall_seconds':time.monotonic()-WALL,'capture_screen':'clean','scope':'Source-metric eligibility for all720 labeled A2/B3 splits. Reading adjacency intersections gives possible absorbed edges only; no73graph or old-old coverage decision.','records':records}
b={'source':'source/source72.edges','n':72,'closed_R2':{'str_vertex_keys':False,'balls':[ids(x) for x in r2]},'method':'adjacency set unions; no BFS','ball_size_histogram':dict(sorted(r2hist.items()))}
for name,obj in [('SOURCE_ELIGIBILITY_RESULT.json',r),('SOURCE_CLOSED_R2.json',b)]:
 s=json.dumps(obj,indent=2)+'\n';assert not screen(s),screen(s);(P/name).write_text(s)
print(json.dumps({k:r[k] for k in ['status','canonical_partitions','closed_R2_ball_size_histogram','categories','partitions_with_joint_eligible_edge','total_joint_eligible_oriented_edge_parameters','prediction_disposition','CPU_seconds','wall_seconds']}))
print(json.dumps({'first_witness_by_category':first}))
