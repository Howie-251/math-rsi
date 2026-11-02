#!/usr/bin/env python3
"""Exact local binary full-N packing gate; no BFS, solver or source regeneration."""
import time
START=time.process_time()
import csv,json,os,resource,signal,traceback
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if(p/'research-wiki').is_dir())
SOURCE=ROOT/'research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt'
BASE=HERE.parents[1]
PARAMETERS=BASE/'degree16_plane864/PARAMETERS.json'
PRIOR=2.0;PREP=.5;CAP=20.0;SOFT=15.5;N=15552

class BudgetStop(Exception):pass
def cpu_signal(signum,frame):raise BudgetStop('CPU soft signal')
signal.signal(signal.SIGXCPU,cpu_signal)
resource.setrlimit(resource.RLIMIT_CPU,(16,17))
def dump(name,obj):(HERE/name).write_text(json.dumps(obj,indent=2)+'\n')
def budget():
 if time.process_time()-START>=SOFT:raise BudgetStop('soft return deadline')
phase='INPUT';prefix={};result=None;source_parses=0
dump('HANDLE.json',dict(status='RUNNING',pid=os.getpid(),single_worker=True,source_D4_BFS=0,
 prior_read_CPU_seconds=PRIOR,new_preparation_CPU_seconds=PREP,wholecase_CPU_cap_seconds=CAP))
try:
 pars=json.loads(PARAMETERS.read_text());incumbent=list(pars['source_center_labels'])
 assert len(incumbent)==len(set(incumbent))==864
 assert all(0<=c<N for c in incumbent)
 selected_role={c:i for i,c in enumerate(incumbent)}
 adj=[None]*N
 with SOURCE.open()as f:
  for line in f:
   row=list(map(int,line.split()))
   if not row:continue
   u=row[0];ns=tuple(row[1:])
   assert 0<=u<N and adj[u]is None
   assert len(ns)==len(set(ns)) and u not in ns and all(0<=w<N for w in ns)
   adj[u]=ns
 source_parses=1
 assert all(a is not None for a in adj)
 degree=list(map(len,adj));assert Counter(degree)=={14:648,15:14904}
 assert sum(degree)==2*116316
 neighbors=list(map(set,adj))
 load=[0]*N;owner=[-1]*N
 for role,c in enumerate(incumbent):
  for w in adj[c]:
   load[w]+=1
   assert owner[w]==-1 # inherited load<=1, needed by exact responsibility filter
   owner[w]=role
 residual=[16-degree[w]-load[w]for w in range(N)]
 assert min(residual)>=0 and max(load)==1
 assert Counter(load)=={0:2628,1:12924}
 phase='BLOCKING_PROFILES';first_append=None;feasible=[[u]for u in incumbent]
 all_hist=Counter();unselected_hist=Counter();blocked_slot_hist=Counter();single_owner_new=0
 with(HERE/'ALL15552_CENTER_BLOCKING_PROFILES.tsv').open('w',newline='')as f:
  out=csv.writer(f,delimiter='\t')
  out.writerow(['source_center','selected_role_or_minus1','source_degree','zero_residual_neighbours',
   'distinct_blocking_clone_owners','blocking_old_roles','blocking_old_centers','blocking_slot_labels',
   'sole_removal_role_or_minus1'])
  for v in range(N):
   prefix={'center':v}
   if v%128==0:budget()
   blocked=sorted(w for w in adj[v]if residual[w]==0)
   roles=sorted({owner[w]for w in blocked});assert all(r>=0 for r in roles)
   count=len(roles);all_hist[count]+=1;blocked_slot_hist[len(blocked)]+=1
   sole=roles[0]if count==1 else -1
   out.writerow([v,selected_role.get(v,-1),degree[v],len(blocked),count,
    ','.join(map(str,roles)),','.join(str(incumbent[r])for r in roles),','.join(map(str,blocked)),sole])
   if v not in selected_role:
    unselected_hist[count]+=1
    if count==0 and first_append is None:first_append=v
    elif count==1:feasible[sole].append(v);single_owner_new+=1
 blocking=dict(all_center_blocking_owner_histogram=dict(sorted(all_hist.items())),
  unselected_center_blocking_owner_histogram=dict(sorted(unselected_hist.items())),
  all_center_zero_residual_slot_histogram=dict(sorted(blocked_slot_hist.items())),
  unselected_centers=N-864,unselected_zero_owner_centers=unselected_hist[0],
  unselected_single_owner_centers=single_owner_new,
  prediction_all_unselected_at_least_two_owners_supported=(unselected_hist[0]+unselected_hist[1]==0),
  incumbent_load_histogram=dict(sorted(Counter(load).items())),
  incumbent_residual_histogram=dict(sorted(Counter(residual).items())))
 dump('BLOCKING_SUMMARY.json',blocking)
 dump('ALL864_REMOVAL_FEASIBLE_CENTER_LISTS.json',{
  'append_phase_first_unselected_feasible_center':first_append,
  'stage':'READY_AFTER_NO_APPEND'if first_append is None else'NOT_ENTERED_APPEND_HIT',
  'removals':[dict(removed_old_role=i,removed_center=incumbent[i],
   individually_feasible_centers=sorted(vs))for i,vs in enumerate(feasible)]if first_append is None else[]})
 winner=None;pair_count=0;removals_completed=0;pair_failed=0;pair_overlap_allowed=0
 if first_append is not None:
  winner=dict(kind='APPEND',removed_role=None,removed_center=None,new_centers=[first_append],
   ordered_centers=incumbent+[first_append])
 else:
  phase='ONE_OUT_TWO_IN'
  with(HERE/'ALL_PAIR_STAGES.tsv').open('w',newline='')as pf,(HERE/'ALL864_REMOVAL_STAGES.tsv').open('w',newline='')as rf:
   pout=csv.writer(pf,delimiter='\t');rout=csv.writer(rf,delimiter='\t')
   pout.writerow(['remove_role','remove_center','center_v','center_t','shared_neighbours',
    'first_overcapacity_slot_or_minus1','restored_capacity_at_failure_or_minus1','stage'])
   rout.writerow(['remove_role','remove_center','feasible_center_count','pairs_checked','stage'])
   for role,u in enumerate(incumbent):
    candidates=sorted(feasible[role]);nu=neighbors[u];before_pairs=pair_count
    prefix={'remove_role':role,'remove_center':u,'next_pair_index':0};budget()
    for a,v in enumerate(candidates):
     for t in candidates[a+1:]:
      prefix={'remove_role':role,'remove_center':u,'center_v':v,'center_t':t,'pairs_completed':pair_count}
      if pair_count%128==0:budget()
      common=sorted(neighbors[v]&neighbors[t]);bad=-1;sbad=-1
      for w in common:
       capacity=residual[w]+int(w in nu)
       if capacity<2:bad=w;sbad=capacity;break
      pair_count+=1
      if bad>=0:
       pair_failed+=1;pout.writerow([role,u,v,t,len(common),bad,sbad,'OVER_CAPACITY']);continue
      if common:pair_overlap_allowed+=1
      pout.writerow([role,u,v,t,len(common),-1,-1,'DEGREE_FEASIBLE_FIRST_HIT'])
      centers=incumbent[:role]+incumbent[role+1:]+[v,t]
      assert len(centers)==len(set(centers))==865
      winner=dict(kind='ONE_OUT_TWO_IN',removed_role=role,removed_center=u,new_centers=[v,t],
       overlap_new_neighbours=common,ordered_centers=centers)
      break
     if winner:break
    rout.writerow([role,u,len(candidates),pair_count-before_pairs,'FIRST_HIT'if winner else'COMPLETE_NO_PAIR'])
    if winner:break
    removals_completed+=1
 stats=dict(append_candidates_checked=N-864,append_hit=(first_append is not None),
  removal_domains_total=864,removal_domains_completed=removals_completed,pairs_checked=pair_count,
  pairs_failed_capacity=pair_failed,feasible_pairs_with_allowed_overlap=pair_overlap_allowed,
  possible_individually_feasible_pair_domain=sum(len(vs)*(len(vs)-1)//2 for vs in feasible),
  actual_binary_scope='append or remove1/add2 about accepted864; one clone per oldcenter',
  degree14_overlap_not_pruned=True,source_literal_parses=source_parses,
  source_D4_or_old16416_BFS_field_Lean_solver_reviews=0,candidate_graphs_generated=0,
  new_graph_parameter_Lean_counts=[0,0,0],blocking=blocking)
 if winner is None:
  assert first_append is None and removals_completed==864
  result=dict(status='COMPLETE_NO_APPEND_OR_ONE_OUT_TWO_IN_FIXED864_BINARY_CLONE_SCOPE',
   terminal_scope='Onlyallappendandall1out2infromthisincumbent;notmaximum864orallnonorbitpackingNO',
   full_domain_complete=True,**stats)
 else:
  phase='CANDIDATE_ARTIFACTS';prefix={'winner':{k:v for k,v in winner.items()if k!='ordered_centers'}};budget()
  centers=winner['ordered_centers'];new_load=[0]*N
  for c in centers:
   for w in adj[c]:new_load[w]+=1
  old_degrees=[degree[w]+new_load[w]for w in range(N)]
  all_degrees=old_degrees+[degree[c]for c in centers]
  assert max(all_degrees)<=16
  m=116316+sum(degree[c]for c in centers)
  graph=HERE/'graph_d16_D4_n16417.edges';body_count=0;added=0
  with graph.open('w')as gf,(HERE/'ALL865_ROLE_BINDINGS.tsv').open('w',newline='')as bf:
   gf.write(f'16417 {m}\n');bout=csv.writer(bf,delimiter='\t')
   bout.writerow(['new_role','new_vertex_label','old_source_center','frozen_source_degree','frozen_full_source_N'])
   for u,ns in enumerate(adj):
    for w in ns:
     if u<w:gf.write(f'{u} {w}\n');body_count+=1
   for j,c in enumerate(centers):
    new=N+j;ns=sorted(adj[c]);bout.writerow([j,new,c,len(ns),','.join(map(str,ns))])
    for w in ns:gf.write(f'{w} {new}\n');added+=1
  assert body_count==116316 and body_count+added==m
  dump('ALL_OLD_VERTEX_LOADS_AND_DEGREES.json',dict(source_degree=degree,
   incumbent_load=load,incumbent_residual=residual,candidate_load=new_load,candidate_degree=old_degrees))
  params=dict(source_literal=str(SOURCE.relative_to(ROOT)),source_n=N,source_m=116316,
   source_center_labels=centers,previous_incumbent_parameters=str(PARAMETERS.relative_to(ROOT)),
   operation={k:v for k,v in winner.items()if k!='ordered_centers'},n=16417,m=m,Delta_max=16,
   intended_D=4,source_D4_and_generic_fullN_distance_interface='INHERITED_NOT_REVALIDATED',
   all_original15552_source_edges_preserved=True,previous16416_all_edges_preserved=(winner['kind']=='APPEND'),
   every_new_neighbourhood='original frozen simple open N_source(center)',new_new_edges=0,
   old_load_histogram=dict(sorted(Counter(new_load).items())),degree_histogram=dict(sorted(Counter(all_degrees).items())),
   source_degree_histogram=dict(sorted(Counter(degree).items())),
   clone_degree_histogram=dict(sorted(Counter(degree[c]for c in centers).items())),
   graph=str(graph.relative_to(ROOT)),fresh_diameter_acceptance='PENDING_ROOT',
   new_graph_parameter_Lean_counts=[0,0,0])
  dump('PARAMETERS.json',params)
  result=dict(status='FOUND_865_CENTER_DEGREE_FEASIBLE_CANDIDATE_PENDING_ROOT_ACCEPTANCE',
   full_domain_complete=False,first_hit_operation=params['operation'],candidate_n=16417,candidate_m=m,
   candidate_degree_histogram=params['degree_histogram'],old_load_histogram=params['old_load_histogram'],
   fresh_diameter_acceptance='PENDING_ROOT_NO_BFS_OR_LEAN',**stats)
  result['candidate_graphs_generated']=1
except BudgetStop as e:
 result=dict(status='UNKNOWN_CPU_CAP_IN_APPEND_ONE_OUT_TWO_IN_CASE',phase=phase,
  first_unfinished_prefix=prefix,error=str(e),full_domain_complete=False,source_literal_parses=source_parses,
  source_D4_old16416_BFS_field_Lean_solver_reviews=0,new_graph_parameter_Lean_counts=[0,0,0])
except Exception as e:
 result=dict(status='UNKNOWN_INPUT_OR_PROCESS_FAILURE',phase=phase,first_unfinished_prefix=prefix,
  error=str(e),traceback=traceback.format_exc(),full_domain_complete=False,
  source_literal_parses=source_parses,source_D4_old16416_BFS_field_Lean_solver_reviews=0,
  new_graph_parameter_Lean_counts=[0,0,0])
actual=time.process_time()-START
result.update(prior_read_CPU_seconds=PRIOR,new_preparation_CPU_seconds=PREP,
 actual_process_CPU_seconds=actual,wholecase_CPU_seconds=PRIOR+PREP+actual,
 wholecase_CPU_cap_seconds=CAP,single_worker=True,next='STOP; root dispositions hit/scopedNO/UNKNOWN; no2out3in/seed')
dump('RESULT.json',result)
dump('TERMINAL.json',{**result,'terminal':True,'active_processes':0})
dump('HANDLE.json',dict(status=result['status'],pid=os.getpid(),terminal=True,active_processes=0,
 wholecase_CPU_seconds=result['wholecase_CPU_seconds']))
print(json.dumps(result))
