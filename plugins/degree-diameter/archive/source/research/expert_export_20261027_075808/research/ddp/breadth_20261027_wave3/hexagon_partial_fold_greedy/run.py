from pathlib import Path
import json,random,time,resource
from collections import Counter

resource.setrlimit(resource.RLIMIT_CPU,(30,30))
P=Path(__file__).resolve().parent
S=P.parent/'hexagon_partial_fold_scout';started=time.process_time();wall=time.monotonic()
D=json.loads((S/'Q_data.json').read_text());W=json.loads((S/'witness12_state.json').read_text())
Q=D['Q'];h_of=D['H3_neighbors'];HN=D['H3_graph'];HQ=D['H3_generic_neighbors'];absolute=D['H3_absolute'];copies=W['h3_extra_copies'];initial=W['states'];N=len(Q)
target_split=8666
def exact_loads(state):
 loads=[]
 for u in range(N):
  count=sum(state[v]!=0 if state[u]==0 else state[v]==state[u] for v in Q[u])
  loads.append(count+(copies[h_of[u]] if h_of[u]>=0 else 0))
 hd=[7-int(absolute[h])+sum(state[v]!=0 for v in HQ[h])+sum(copies[k] for k in HN[h]) for h in range(364)]
 return loads,hd
initial_loads,initial_hd=exact_loads(initial)
assert max(initial_loads)<=2 and max(initial_hd)<=12
orders=[list(range(N)),list(reversed(range(N))),list(range(N)),list(range(N))]
random.Random(2026102701).shuffle(orders[2]);random.Random(2026102702).shuffle(orders[3])
names=['natural','reverse','random_2026102701','random_2026102702']
profiles=[];best_state=initial.copy();best_loads=initial_loads.copy();best_hd=initial_hd.copy();best_split=sum(x!=0 for x in initial);best_profile=None
hit=False;limited=False;checks=0;legal_color_checks=0
for order,name in zip(orders,names):
 state=initial.copy();loads=initial_loads.copy();hd=initial_hd.copy();split=sum(x!=0 for x in state)
 moves=[];pass_added=[];passes=0;cursor=-1
 while not hit and not limited:
  added=0;passes+=1
  for cursor,u in enumerate(order):
   if cursor%1024==0 and time.process_time()-started>=27.0:limited=True;break
   if state[u]:continue
   checks+=1;h=h_of[u]
   if h>=0 and hd[h]>=12:continue
   if any(state[v]==0 and loads[v]>=2 for v in Q[u]):continue
   choice=[]
   for color in (1,2):
    legal_color_checks+=1
    same=[v for v in Q[u] if state[v]==color]
    own=len(same)+(copies[h] if h>=0 else 0)
    if own>2 or any(loads[v]>=2 for v in same):continue
    choice.append((len(same),color,own))
   if not choice:continue
   _,color,own=min(choice)
   state[u]=color;loads[u]=own
   for v in Q[u]:
    if state[v]==0 or state[v]==color:loads[v]+=1
   if h>=0:hd[h]+=1
   split+=1;added+=1;moves.append([u,color-1])
   if split>=target_split:hit=True;break
  pass_added.append(added)
  if not added:break
 if split>best_split:
  best_split=split;best_state=state;best_loads=loads;best_hd=hd;best_profile=name
 profiles.append(dict(name=name,passes=passes,added_per_pass=pass_added,added=len(moves),split_fibers=split,core_order=33397+split+sum(copies),fixed_point_completed=not hit and not limited and pass_added[-1]==0,cursor_in_priority_order=cursor,moves=moves))
 if hit or limited:break

# One exact best-state local-load recalculation checks the incremental update, without BFS.
checked_loads,checked_hd=exact_loads(best_state)
assert checked_loads==best_loads and checked_hd==best_hd
assert max(best_loads)<=2 and max(best_hd)<=12
assert all(initial[u]==0 or best_state[u]==initial[u] for u in range(N))
record=dict(states=best_state,state_meaning=['merged','split_color0','split_color1'],h3_extra_copies=copies,pad=[],split_fibers=best_split,core_order=33397+best_split+sum(copies),max_degree_bound=12,diameter_upper_bound=5,diameter_basis='author Theorem5.1+5.2 for arbitrary S and coloring',source_record='23056128',base_witness='pf_d12_k5_n41699.json',profile=best_profile)
(P/'best_state.json').write_text(json.dumps(record,separators=(',',':'))+'\n')
(P/'best_loads.json').write_text(json.dumps(dict(generic_loads=best_loads,generic_degree='10+load, one vertex if merged, two if split',H3_copy_degrees=best_hd,max_generic_load=max(best_loads),max_H3_degree=max(best_hd),recalculated_from_best_state=True),separators=(',',':'))+'\n')
counts=dict(Counter(best_state));degrees=[]
for u,st in enumerate(best_state):degrees.extend([10+best_loads[u]]*(2 if st else 1))
for h in range(364):degrees.extend([best_hd[h]]*(1+copies[h]))
result=dict(status='HIT_CORE_ABOVE_42342' if hit else 'CPU_LIMIT_INCOMPLETE_PROFILE' if limited else 'FOUR_FIXED_GREEDY_PROFILES_COMPLETE',workers=1,source_split_fibers=7959,fixed_H3_extra_copies=sum(copies),padding_twins_removed=63,forbidden_operations=['recolor_existing_split','delete_existing_split','change_H3_copy_counts','optimize_twins'],priority_profiles=names,profiles=profiles,completed_profiles=sum(p['fixed_point_completed'] for p in profiles),best_profile=best_profile,best_split_fibers=best_split,best_added_splits=best_split-7959,best_core_order=len(degrees),degree_histogram=dict(sorted(Counter(degrees).items())),free_degree_slots=sum(12-x for x in degrees),state_histogram=counts,target_core_order=42343,target_split_fibers=target_split,merged_candidate_checks=checks,color_legality_checks=legal_color_checks,CPU_hard_limit_seconds=30,CPU_internal_stop_seconds=27,CPU_seconds=time.process_time()-started,wall_seconds=time.monotonic()-wall,CPU_limit_reached=limited,explicit_large_graph_generated=False,full_BFS_performed=False)
(P/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='profiles'},indent=2))
print('profiles',[(p['name'],p['split_fibers'],p['added_per_pass']) for p in profiles])
