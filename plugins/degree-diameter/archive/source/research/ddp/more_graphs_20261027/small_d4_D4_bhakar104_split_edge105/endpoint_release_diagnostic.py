"""Source-metric diagnostic only; no candidate graph, BFS, or parameter replay."""
import json,pathlib,resource,sys,time
from collections import Counter
from datetime import datetime,timezone
START=time.process_time(); WALL=time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU,(2,2))
P=pathlib.Path(__file__).resolve().parent
ROOT=pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
sys.path.insert(0,str(ROOT/'aris_repo/tools'))
from capture_filter import screen
SRC=ROOT/'research/ddp/breadth_20261027_wave2/sources'
d=json.loads((SRC/'bhakar104_distances.json').read_text())
lines=(SRC/'bhakar104.edges').read_text().splitlines(); assert lines[0]=='104 208'
adj=[set() for _ in range(104)]
for line in lines[1:]:
 if line.strip():
  a,b=map(int,line.split());adj[a].add(b);adj[b].add(a)
r3=[sum(1<<t for t in range(104) if d[x][t]<=3) for x in range(104)]
adjm=[sum(1<<t for t in ns) for ns in adj]
def ids(mask):return [t for t in range(104) if (mask>>t)&1]
counts=Counter();hist=Counter();first={};records=[];tests=0;edgechecks=0
for v in range(104):
 ns=sorted(adj[v]);outside=[x for x in range(104) if x!=v and x not in adj[v]]
 assert len(outside)==99
 for pick in range(1,4):
  A=[ns[0],ns[pick]];B=[s for s in ns if s not in A]
  EA=sum(1<<t for t in range(104) if d[v][t]==4 and all(d[a][t]!=3 for a in A))
  EB=sum(1<<t for t in range(104) if d[v][t]==4 and all(d[b][t]!=3 for b in B))
  XA=[x for x in outside if EA & ~r3[x]==0]
  XB=[x for x in outside if EB & ~r3[x]==0]
  tests+=2*len(outside)
  maskXB=sum(1<<x for x in XB)
  cross=[]
  for x in XA:
   edgechecks+=1
   for y in ids(adjm[x]&maskXB):cross.append([x,y])
  if not XA and not XB:category='BOTH_SIDES_EMPTY'
  elif not XA:category='A_ONLY_EMPTY'
  elif not XB:category='B_ONLY_EMPTY'
  elif not cross:category='BOTH_NONEMPTY_NO_SOURCE_EDGE'
  else:category='BOTH_NONEMPTY_WITH_SOURCE_EDGE'
  record={'v':v,'A':A,'B':B,'E_A':ids(EA),'E_B':ids(EB),'X_A':XA,'X_B':XB,'source_edges_XA_to_XB':cross,'category':category}
  records.append(record);counts[category]+=1;hist[(len(XA),len(XB))]+=1
  first.setdefault(category,record)
counts={key:counts[key] for key in ['BOTH_SIDES_EMPTY','A_ONLY_EMPTY','B_ONLY_EMPTY','BOTH_NONEMPTY_NO_SOURCE_EDGE','BOTH_NONEMPTY_WITH_SOURCE_EDGE']}
result={'status':'COMPLETE_SOURCE_METRIC_ENDPOINT_RELEASE_DIAGNOSTIC','timestamp_UTC':datetime.now(timezone.utc).isoformat(),'source_n':104,'source_m':208,'source_edges':str((SRC/'bhakar104.edges').relative_to(ROOT)),'source_metric_cache':str((SRC/'bhakar104_distances.json').relative_to(ROOT)),'canonical_splits':len(records),'eligible_endpoints_per_split':99,'endpoint_compatibility_mask_tests':tests,'XA_neighbor_mask_intersections':edgechecks,'categories':counts,'at_least_one_side_empty':counts['BOTH_SIDES_EMPTY']+counts['A_ONLY_EMPTY']+counts['B_ONLY_EMPTY'],'exactly_one_side_empty':counts['A_ONLY_EMPTY']+counts['B_ONLY_EMPTY'],'both_nonempty':counts['BOTH_NONEMPTY_NO_SOURCE_EDGE']+counts['BOTH_NONEMPTY_WITH_SOURCE_EDGE'],'first_witness_by_category':first,'coverer_size_pair_histogram':[{'X_A_size':a,'X_B_size':b,'count':count} for (a,b),count in sorted(hist.items())],'records':records,'candidate_graphs':0,'BFS':0,'solver_calls':0,'original119808_case_replay':0,'main_RESULT_or_CASES_modified':False,'CPU_seconds':time.process_time()-START,'wall_seconds':time.monotonic()-WALL,'scope':'Only source-metric endpoint coverers for the original312 canonical splits. G[X_A,X_B] edges are read from the cached source; no surgery candidate is reconstructed.','capture_screen':'clean'}
s=json.dumps(result,indent=2)+'\n';assert not screen(s),screen(s)
(P/'ENDPOINT_RELEASE_DIAGNOSTIC.json').write_text(s)
print(json.dumps({k:result[k] for k in ['status','canonical_splits','categories','at_least_one_side_empty','both_nonempty','endpoint_compatibility_mask_tests','XA_neighbor_mask_intersections','CPU_seconds','wall_seconds']}))
print(json.dumps({'first_witness_by_category':first}))
