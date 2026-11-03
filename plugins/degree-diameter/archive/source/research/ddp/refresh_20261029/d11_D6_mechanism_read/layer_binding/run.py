from array import array
from collections import Counter
from pathlib import Path
import json,os,resource,sys,time
D=Path(__file__).resolve().parent;ROOT=D.parents[4]
resource.setrlimit(resource.RLIMIT_CPU,(19,20))
began=time.process_time();wall=time.monotonic()
def dump(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
bounds=[0,132860,172076,179888,182618,186033]
expected_internal=[10,8,6,5]
src=ROOT/'research/ddp/more_graphs_20261027/d11_D6_current186033'
dump('HANDLE.json',{'status':'RUNNING','pid':os.getpid(),'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'budget_cpu_seconds':20})
dump('INPUT.json',{'prediction':'../LAYER_BINDING_PREDICTION.md','source_csr':str((src/'adjacency.csr.u32le.bin').relative_to(ROOT)),'current_degrees':str((src/'degrees.u8.bin').relative_to(ROOT)),'bounds':bounds,'expected_internal_degree':expected_internal,'other_partitions_attempted':0,'budget_cpu_seconds':20,'workers':1})
def finish(status,witness=None,extra=None):
 r={'status':status,'prefix_signature_prediction':'SUPPORTED' if status in ('BOTH_GATES_PASS_CANDIDATE_POOL_BOUND_ONLY','FREE_PORT_CAPACITY_GATE_FAIL') else 'REFUTED','six_half_free_port_prediction':'SUPPORTED' if status=='BOTH_GATES_PASS_CANDIDATE_POOL_BOUND_ONLY' else ('REFUTED' if status=='FREE_PORT_CAPACITY_GATE_FAIL' else 'UNTESTED_AFTER_BINDING_FAILURE'),'source_n':186033,'source_m':1010817,'source_old_n':182618,'prefix_bounds':bounds,'counterexample':witness,'layers':layers,'layer_bipartite_connected_traversals_completed':len(layer_colors),'source_D6_BFS':0,'radius_ball_queries':0,'solver_calls':0,'candidate_graphs':0,'other_prefix_or_permutation_trials':0,'geometry_isomorphism_proved':False,'internal_D6_proved_by_this_gate':False,'automatic_179888_coverage_certified_here':False,'cpu_seconds':time.process_time()-began,'wall_seconds':time.monotonic()-wall,'pid':os.getpid(),'budget_cpu_seconds':20}
 if extra:r.update(extra)
 dump('RESULT.json',r);dump('TERMINAL.json',{'status':'TERMINAL','result_status':status,'pending':[],'cpu_seconds':r['cpu_seconds']})
 dump('HANDLE.json',{'status':'TERMINAL','pid':os.getpid(),'result_status':status})
 print(json.dumps(r),flush=True);sys.exit(0)
layers=[];layer_colors=[]
with (src/'adjacency.csr.u32le.bin').open('rb') as f:
 header=array('I');header.fromfile(f,2)
 n,arcs=header;assert(n,arcs)==(186033,2021634) and sys.byteorder=='little'
 offsets=array('I');offsets.fromfile(f,n+1)
 neighbors=array('I');neighbors.fromfile(f,arcs)
 assert not f.read(1) and offsets[0]==0 and offsets[-1]==arcs
degrees=(src/'degrees.u8.bin').read_bytes();assert len(degrees)==n
assert all(offsets[u+1]-offsets[u]==degrees[u] for u in range(n))
def level(v):
 if v<132860:return 0
 if v<172076:return 1
 if v<179888:return 2
 if v<182618:return 3
 return 4
colors=bytearray([255])*182618
# Check internal degree at the unique fixed prefix before making any color claim.
for a in range(4):
 lo,hi=bounds[a:a+2];hist=Counter()
 for v in range(lo,hi):
  count=sum(lo<=neighbors[k]<hi for k in range(offsets[v],offsets[v+1]))
  hist[count]+=1
  if count!=expected_internal[a]:
   layers.append({'layer':a,'range':[lo,hi],'internal_degree_partial_histogram':dict(hist),'vertices_degree_checked':v-lo+1})
   finish('PREFIX_INTERNAL_DEGREE_GATE_FAIL',{'layer':a,'vertex':v,'expected_internal_degree':expected_internal[a],'actual_internal_degree':count,'internal_neighbors':[neighbors[k] for k in range(offsets[v],offsets[v+1]) if lo<=neighbors[k]<hi]})
 layers.append({'layer':a,'range':[lo,hi],'n':hi-lo,'expected_internal_degree':expected_internal[a],'internal_degree_histogram':dict(hist),'vertices_degree_checked':hi-lo})
# Exactly one connectivity/two-color traversal per induced level; no distances/radius.
for a in range(4):
 lo,hi=bounds[a:a+2];colors[lo]=0;queue=array('I',[lo]);head=0
 while head<len(queue):
  u=queue[head];head+=1
  for k in range(offsets[u],offsets[u+1]):
   v=neighbors[k]
   if not lo<=v<hi:continue
   if colors[v]==255:colors[v]=1-colors[u];queue.append(v)
   elif colors[v]==colors[u]:
    finish('PREFIX_BIPARTITE_GATE_FAIL',{'layer':a,'monochromatic_edge':[u,v],'color':colors[u]})
 if len(queue)!=hi-lo:
  missing=next(v for v in range(lo,hi) if colors[v]==255)
  finish('PREFIX_CONNECTED_GATE_FAIL',{'layer':a,'component_reached':len(queue),'layer_n':hi-lo,'first_unreached':missing})
 ch=Counter(colors[v] for v in range(lo,hi))
 layers[a].update(bipartite=True,connected=True,canonical_color0_root=lo,color_class_sizes=dict(ch))
 layer_colors.append(a)
# Bind every later original vertex's two anchors to each earlier level, opposite colors.
anchor_checks=0;anchor_hist={str(a):Counter() for a in range(1,4)}
for b in range(1,4):
 lo,hi=bounds[b:b+2]
 for v in range(lo,hi):
  an=[[] for _ in range(b)]
  for k in range(offsets[v],offsets[v+1]):
   u=neighbors[k];a=level(u)
   if a<b:an[a].append(u)
  for a,ns in enumerate(an):
   anchor_checks+=1;anchor_hist[str(b)][len(ns)]+=1
   if len(ns)!=2 or {colors[u] for u in ns}!={0,1}:
    finish('PREFIX_TWO_ANCHOR_GATE_FAIL',{'later_layer':b,'vertex':v,'earlier_layer':a,'actual_anchors':ns,'actual_anchor_colors':[colors[u] for u in ns],'expected':'exactly2,oneeachcolor'})
# Later-original injections in each earlier half follow the actual degree bound; record directly.
late_hist=[]
for a in range(4):
 lo,hi=bounds[a:a+2];h=Counter()
 for v in range(lo,hi):
  ct=sum(hi<=neighbors[k]<182618 for k in range(offsets[v],offsets[v+1]));h[ct]+=1
  if ct>1:finish('PREFIX_LATER_ANCHOR_INJECTION_GATE_FAIL',{'layer':a,'vertex':v,'later_original_neighbors':[neighbors[k] for k in range(offsets[v],offsets[v+1]) if hi<=neighbors[k]<182618]})
 late_hist.append(dict(h));layers[a]['later_original_neighbor_histogram']=dict(h)
freeparts=[];pool=[]
for a in range(3):
 lo,hi=bounds[a:a+2]
 for c in (0,1):
  ids=[v for v in range(lo,hi) if colors[v]==c and degrees[v]<11]
  item={'layer':a,'color':c,'class_size':layers[a]['color_class_sizes'][c],'current_free_count':len(ids),'first_free_ids':ids[:12],'all_free_ids':ids,'passes_need6':len(ids)>=6}
  pool.append(item);freeparts.append({k:v for k,v in item.items() if k!='all_free_ids'})
  if len(ids)<6:
   dump('FREE_PORT_PARTIAL_PROFILE.json',freeparts)
   finish('FREE_PORT_CAPACITY_GATE_FAIL',{'layer':a,'color':c,'current_free_count':len(ids),'required':6},extra={'free_half_profiles':freeparts,'cross_layer_anchor_checks':anchor_checks})
(D/'old_original_colors.u8.bin').write_bytes(colors)
dump('FREE_HALF_POOLS.json',{'source_n':n,'source_m':arcs//2,'bounds':bounds,'color_convention':'Each connected original level starts its smallestlabel withcolor0;colorsarebipartitionclasses,notboundgeometricpoint-versus-lineorientation.','parts':pool})
finish('BOTH_GATES_PASS_CANDIDATE_POOL_BOUND_ONLY',extra={'free_half_profiles':freeparts,'cross_layer_anchor_checks':anchor_checks,'cross_layer_anchor_count_histograms':{a:dict(h) for a,h in anchor_hist.items()},'free_upper_total':sum(p['current_free_count'] for p in freeparts),'colors_file':'old_original_colors.u8.bin','free_pools_file':'FREE_HALF_POOLS.json','candidate_pool_only':True,'K6_graph_generated':False,'cooperative_6145_targets_coverage_checked':False})
