"""One exact closed-B1 proxy kernel on the unchanged51457 source; no MIP."""
import json,pathlib,resource,subprocess,time
from datetime import datetime,timezone
P=pathlib.Path(__file__).resolve().parent;BASE=P.parent;START=time.process_time();WALL=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN);C0=r0.ru_utime+r0.ru_stime
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
pred=json.loads((P/'PROXY_KERNEL_PRED.json').read_text());assert pred['prototype']==51445
source=BASE/'singlefault_star_probe/continuation/graphs/graph_d13_D5_n51457.edges';native=BASE/'singlefault_star_probe/cover';pins=pred['mandatory_pins'];f=pred['omitted_full_pin'];proto=pred['prototype']
with source.open() as stream:
 n,m=map(int,next(stream).split());assert(n,m)==(51457,324863)
 adj=[set() for _ in range(n)]
 for line in stream:
  if line.strip():
   a,b=map(int,line.split());adj[a].add(b);adj[b].add(a)
assert adj[proto]==set(pins)|{f} and len(adj[f])==13
assert all(len(adj[p])<13 for p in pins)
closed=lambda v:adj[v]|{v}
Nf=set(adj[f]);covered=set().union(*(closed(p) for p in pins));targets=sorted(Nf-covered)
label_kernel=set().union(*(closed(h) for h in Nf))
eligible=sorted(v for v in label_kernel if len(adj[v])<13 and v not in pins)
rows=[]
for v in eligible:
 mask=sum(1<<i for i,h in enumerate(targets) if h in closed(v))
 if mask:rows.append({'guard':v,'mask':mask,'covered_targets':[targets[i] for i in range(len(targets)) if mask>>i&1],'current_degree':len(adj[v])})
FULL=(1<<len(targets))-1;dp={0:[]};transitions=0
# Each row is considered once. The snapshot forbids guard reuse; retain minimum-cardinality representative per union.
for row in rows:
 for mask,path in list(dp.items()):
  if len(path)>=4:continue
  transitions+=1;newmask=mask|row['mask'];newpath=path+[row['guard']]
  if newmask not in dp or (len(newpath),newpath)<(len(dp[newmask]),dp[newmask]):dp[newmask]=newpath
sol=dp.get(FULL);zero_targets=[h for i,h in enumerate(targets) if not any(row['mask']>>i&1 for row in rows)]
result={'status':'EXACT_PROXY_KERNEL_COVER_FOUND' if sol is not None else 'COMPLETE_PROXY_KERNEL_NO_AT_MOST_FOUR_GUARDS','timestamp_UTC':datetime.now(timezone.utc).isoformat(),'source_n':n,'source_m':m,'prototype':proto,'omitted_full_pin':f,'full_pin_neighbors':sorted(Nf),'mandatory_pins':pins,'Nf_already_covered_by_mandatory_closed_B1':sorted(Nf&covered),'uncovered_Nf_targets':targets,'raw_closed_B1_kernel_size':len(label_kernel),'eligible_free_kernel_vertices':len(eligible),'eligible_free_nonzero_mask_rows':len(rows),'eligible_free_guards':eligible,'guard_masks':rows,'zero_cover_Nf_targets':zero_targets,'bit_count':len(targets),'DP_states':len(dp),'DP_transitions':transitions,'DP_cardinality_limit':4,'guards':sol,'minimum_guard_count_if_found':None if sol is None else len(sol),'no_MIP':True,'R4_calls_before_possible_verify':0,'BFS_before_possible_verify':0,'source_allroot_BFS':0,'candidate_graphs':0,'main_unrestricted_four_guard_scope':'UNKNOWN unless this sufficient proxy produces a verified success','prior_MIP_UNKNOWNS_unchanged':True}
(P/'PROXY_KERNEL_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','uncovered_Nf_targets','raw_closed_B1_kernel_size','eligible_free_kernel_vertices','eligible_free_nonzero_mask_rows','zero_cover_Nf_targets','DP_states','guards']}),flush=True)
if sol is not None:
 assert len(sol)>=3, 'proxy<=2 would contradict the saved exact two-guard result'
 selected=sorted(pins+sol);assert len(selected)==len(set(selected))<=13 and all(len(adj[s])<13 for s in selected)
 (P/'proxy_selected.pins.txt').write_text(' '.join(map(str,selected))+'\n')
 with (P/'proxy_verify.log').open('w') as log:
  proc=subprocess.Popen([str(native),'verify',str(source),str(P/'proxy_selected.pins.txt'),str(P/'proxy_verified'),'13'],stdout=log,stderr=log)
  (P/'PROXY_LIVE_HANDLE.json').write_text(json.dumps({'status':'RUNNING_UNIQUE_FULL_SELECTED_R4_VERIFY','pid':proc.pid},indent=2)+'\n')
  try:code=proc.wait(timeout=15)
  except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
 assert code==0
 verified=json.loads((P/'proxy_verified.json').read_text());assert verified['status']=='FULL_SELECTED_R4_CHECK_COMPLETE' and verified['missing_count']==0 and verified['covered_count']==n
 assert verified['pin_current_degrees']==[len(adj[s]) for s in selected]
 out=P/'candidate';out.mkdir(exist_ok=True);graph=out/'graph_d13_D5_n51458.edges'
 with source.open() as old,graph.open('w') as new:
  assert tuple(map(int,next(old).split()))==(n,m);new.write(f'{n+1} {m+len(selected)}\n')
  for line in old:new.write(line)
  for s in selected:new.write(f'{s} {n}\n')
 step={'status':'PRODUCTION_COMPLETE_CURRENT_R4_AND_DEGREE','prototype':proto,'omitted_saturated_pin':f,'source_n':n,'source_m':m,'source_graph':str(source),'new_vertex':n,'new_n':n+1,'new_m':m+len(selected),'mandatory_pins':pins,'anchors':sol,'full_neighbor_set':selected,'old_pin_degrees':verified['pin_current_degrees'],'new_vertex_degree':len(selected),'max_degree':13,'all_old_edges_preserved':True,'complete_current_R4_covered':n,'complete_current_R4_missing':0,'certificate':'N(f) subset closedB1(selected), followed by one actual full selectedR4 verification','graph_file':str(graph),'parent_pending':True,'source_allroot_BFS':0,'new_graph_allroot_BFS':0}
 (out/'accepted_step.json').write_text(json.dumps(step,indent=2)+'\n');result.update(status='HIT51458_PRODUCTION_VERIFIED',guards=sol,candidate_graphs=1,accepted_step='candidate/accepted_step.json',graph='candidate/graph_d13_D5_n51458.edges',new_n=n+1,new_m=m+len(selected),selected_R4_verify_calls=1)
r1=resource.getrusage(resource.RUSAGE_CHILDREN);childCPU=r1.ru_utime+r1.ru_stime-C0
result.update(driver_CPU_seconds=time.process_time()-START,child_CPU_seconds=childCPU,aggregate_CPU_seconds=childCPU+time.process_time()-START,wall_seconds=time.monotonic()-WALL)
assert result['aggregate_CPU_seconds']<5
(P/'PROXY_KERNEL_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(P/'PROXY_KERNEL_TERMINAL.json').write_text(json.dumps({k:result[k] for k in ['status','aggregate_CPU_seconds','driver_CPU_seconds','child_CPU_seconds','wall_seconds','candidate_graphs']},indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','aggregate_CPU_seconds','candidate_graphs','guards']}),flush=True)
