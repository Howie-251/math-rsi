from pathlib import Path
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
d=json.loads((P.parent/'block_geometry_analysis/F_COMPONENT_RESULT.json').read_text())
adj={int(k):set(v)for k,v in d['free_adjacency'].items()}
paths=[];forced=[];pairs=[];pairinfo=[];p3=[]
for ci,comp in enumerate(sorted(d['components'],key=lambda c:min(c['vertices']))):
 V=set(comp['vertices']);ends=sorted(x for x in V if len(adj[x])==1)
 assert len(ends)==2
 order=[];prev=None;cur=ends[0]
 while True:
  order.append(cur);nxt=adj[cur]-({prev}if prev is not None else set())
  if not nxt:break
  assert len(nxt)==1;prev,cur=cur,next(iter(nxt))
 assert set(order)==V and len(order)==len(V) and order[-1]==ends[1]
 n=len(order);mandatory=[];candidates=[]
 if n==2:candidates=[[0,1]]
 elif n==3:mandatory=[1];p3.append(order[1])
 elif n==4:candidates=[[0,1],[2,3]]
 elif n==6:mandatory=[1,4]
 else:raise AssertionError(n)
 fp=[order[i]for i in mandatory];forced+=fp
 ids=[]
 for positions in candidates:
  options=[order[i]for i in positions];ids.append(len(pairs));pairs.append(options)
  pairinfo.append({'pair_id':len(pairs)-1,'component_id':ci,'positions':positions,'options':options,'required_count':1})
 paths.append({'component_id':ci,'path_type':f'P{n}','path_order':order,'mandatory_positions':mandatory,
 'mandatory_pins':fp,'choice_pair_ids':ids,'minimum_domination':(n+2)//3})
assert Counter(len(p['path_order'])for p in paths)=={2:18,3:6,4:9,6:3}
assert len(forced)==len(set(forced))==12 and len(pairs)==36
opts=[x for pair in pairs for x in pair]
assert len(set(opts))==72 and not(set(opts)&set(forced))
candidate=set(forced)|set(opts)
p3.sort();assert len(p3)==6
model={'status':'READY_EXACT_ALL_MINIMUM_F_DOMINATION_MODEL','source_n':972,'source_m':6264,'free_vertices':sorted(adj),
 'F_component_types':{'P2':18,'P3':6,'P4':9,'P6':3},'F_domination_number':48,
 'forced_selected':sorted(forced),'forced_selected12':sorted(forced),
 'choice_pairs':pairs,'choice_pair_count':len(pairs),'choice_pair_info':pairinfo,
 'sorted_P3_centers':p3,'fixed_color_centers':p3,
 'fixed_color_constraints':[{'pin':pin,'color':c}for c,pin in enumerate(p3)],
 'forbidden_in_any_min_F_domset':sorted(set(adj)-candidate),
 'canonical_paths':paths,'pin_selection_constraints':'Each forcedpin selected; eachchoicepair exactlyone; otherszero. Total48.',
 'color_constraints':'Each selectedpin assignedexactlyone of6colors; eachcolor exactly8pins; sortedP3centers fixedtoseparatecolors0..5. DistinctP3colors isextraexplicitrestriction.',
 'canonical_order':'Components sortedbyminvertex; path startsatlowerlabeldegree1endpoint; traversalunique. P3colororder sortedbycenterlabels.',
 'min_dom_completeness':'P2 endpointcoverage needsone arbitrarypin;P3gamma1 onlycenter;P4 endpoints forceonefrompositions0/1 andonefrom2/3,all4work;P6gamma2 forcesdisjoint3-neighborhoods centeredpositions1/4. Componentsindependent.',
 'newrule_n':978,'newrule_maxdegree':13,'source_BFS':0,'distance_caches_or_R2_matrix':0,'solver_runs':0,'candidate_graphs':0,
 'CPU_seconds':time.process_time()-start}
(P/'min_dom_model.json').write_text(json.dumps(model,indent=2)+'\n')
(P/'RESULT.json').write_text(json.dumps({k:v for k,v in model.items()if k not in ['canonical_paths','choice_pair_info','free_vertices']},indent=2)+'\n')
(P/'terminal.json').write_text(json.dumps({'status':model['status'],'CPU_seconds':model['CPU_seconds'],'pending':[]},indent=2)+'\n')
print(json.dumps({k:model[k]for k in ['status','F_domination_number','forced_selected','choice_pair_count','fixed_color_centers','CPU_seconds']},indent=2))
