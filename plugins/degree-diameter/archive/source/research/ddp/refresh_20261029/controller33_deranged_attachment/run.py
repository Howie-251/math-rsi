import collections,itertools,json,os,resource,time
from pathlib import Path
D=Path(__file__).resolve().parent;ROOT=D.parents[3]
resource.setrlimit(resource.RLIMIT_CPU,(19,20));start=time.process_time();wall=time.monotonic()
def dump(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
dump('HANDLE.json',{'status':'RUNNING','pid':os.getpid()})
old=json.load(open(D.parent/'controller33_parallel_triangle/CASES.json'))
inp=json.load(open(D.parent/'controller33_parallel_triangle/INPUT.json'))
source_edges=set(map(tuple,inp['source_edges']))
source_triangles=inp['source_triangles'];source_cycleof={v:i for i,c in enumerate(inp['source_C5s']) for v in c}
Tedges={tuple(sorted(e)) for T in source_triangles for e in itertools.combinations(T,2)}
newtri=[30,31,32];newTedges=set(itertools.combinations(newtri,2))
sigmas=[[1,2,0],[2,0,1]];cases=[];passes=[];distinct=set()
firsthist=collections.Counter();allhist=collections.Counter();cuthist=collections.Counter();cutfails=[]
def cls(u,v):
 if u==v:return 'self'
 if u<30 and v<30:return 'old-old'
 if u>=30 and v>=30:return 'new-new'
 return 'new-old'
for previous in old:
 vs=previous['old_triangle'];rs=previous['chosen_external_neighbors']
 cuts={tuple(e) for e in previous['cut_edges']}
 for si,sigma in enumerate(sigmas):
  inverse=[sigma.index(i) for i in range(3)]
  add=set(newTedges)
  add.update((v,30+i) for i,v in enumerate(vs))
  add.update((rs[sigma[i]],30+i) for i in range(3))
  edges=(source_edges-cuts)|add;signature=tuple(sorted(edges))
  assert len(edges)==66 and signature not in distinct
  distinct.add(signature)
  adj=[set() for _ in range(33)]
  for u,v in edges:
   assert u!=v;adj[u].add(v);adj[v].add(u)
  assert all(len(row)==4 for row in adj)
  ext=edges-(Tedges|newTedges);ea=[set() for _ in range(33)]
  for u,v in ext:ea[u].add(v);ea[v].add(u)
  assert len(ext)==33 and all(len(row)==2 for row in ea)
  unseen=set(range(33));cycs=[]
  while unseen:
   first=min(unseen);u=first;prev=-1;cyc=[]
   while True:
    cyc.append(u);unseen.remove(u)
    nxt=min(ea[u]-{prev}) if prev in ea[u] else min(ea[u])
    prev,u=u,nxt
    if u==first:break
   cycs.append(cyc)
  assert sorted(map(len,cycs))==[5,5,5,18]
  counts=[[0]*33 for _ in range(33)]
  for u in range(33):
   for x in adj[u]:
    for y in adj[x]:
     if y==u:continue
     for v in adj[y]:
      if v!=x:counts[u][v]+=1
   assert sum(counts[u])==36
  cutrecords=[]
  for i,(v,r) in enumerate(zip(vs,rs)):
   path=[v,30+i,30+inverse[i],r]
   good=all(path[k+1] in adj[path[k]] for k in range(3)) and path[0]!=path[2] and path[1]!=path[3]
   cuthist[counts[v][r]]+=1
   cutrec={'cutpair':[v,r],'designated_path':path,'path_is_actual_NB3':good,'actual_NB3_count':counts[v][r]}
   cutrecords.append(cutrec)
   if not good or counts[v][r]==0:cutfails.append(cutrec)
  missing=[(u,v) for u in range(33) for v in range(33) if v not in adj[u] and counts[u][v]==0]
  mc=collections.Counter(cls(u,v) for u,v in missing);allhist.update(mc)
  first=missing[0] if missing else None
  if first:firsthist[cls(*first)]+=1
  case={'candidate_index':len(cases),'parent80_index':previous['candidate_index'],'source_triangle_index':previous['source_triangle_index'],'old_triangle':vs,'new_triangle':newtri,'choice_bits':previous['choice_bits'],'chosen_external_neighbors':rs,'sigma_index':si,'sigma':sigma,'sigma_inverse':inverse,'cut_edges':sorted(cuts),'added_edges':sorted(add),'n':33,'m':66,'simple':True,'degree_histogram':{'4':33},'external_cycle_sizes':[5,5,5,18],'cut_pair_repairs':cutrecords,'missing_nonadjacent_or_equal_NB3_ordered_pairs':len(missing),'missing_class_counts':dict(mc),'first_missing':None if first is None else {'u':first[0],'v':first[1],'class':cls(*first),'NB3_count':0},'NB3_nonadjacent_or_equal_min':min(counts[u][v] for u in range(33) for v in range(33) if v not in adj[u]),'pass':not missing,'controller_edges':signature,'ordinary_global_D':None,'ordinary_bad_pairs':None}
  cases.append(case)
  if not missing:passes.append(case)
assert len(cases)==160 and len(distinct)==160 and not cutfails
dump('INPUT.json',{'source_edges':sorted(source_edges),'source_triangles':source_triangles,'source_C5s':inp['source_C5s'],'parent80_cases':'../controller33_parallel_triangle/CASES.json','sigmas':sigmas,'raw_parameter_count':160,'literal_duplicate_count':0,'other4_S3_permutations_not_executed':True})
dump('CASES.json',cases);dump('PASSERS.json',passes)
result={'status':'COMPLETE_160_RAW_GATE_NO_PASS' if not passes else 'COMPLETE_160_RAW_GATE_WITH_PASSERS','structural_predictions':'SUPPORTED','cut_pair_repair_prediction':'SUPPORTED','joint_existence_prediction':'REFUTED' if not passes else 'SUPPORTED_RAW_ONLY','controller_candidates_generated':160,'raw_NB3_candidates_checked':160,'distinct_literal_controllers':160,'pass_count':len(passes),'failed_count':160-len(passes),'untested_count':0,'cut_pair_paths_checked':480,'cut_pair_path_failures':cutfails,'cut_pair_actual_NB3_count_histogram':dict(sorted(cuthist.items())),'first_missing_class_histogram':dict(firsthist),'all_missing_class_occurrence_counts':dict(allhist),'missing_ordered_count_histogram':dict(sorted(collections.Counter(c['missing_nonadjacent_or_equal_NB3_ordered_pairs'] for c in cases).items())),'hypothetical_target_n':2112,'target_Delta':16,'target_D':3,'actual_fiber_target_graphs':0,'actual_fiber_target_n':None,'actual_fiber_target_D':None,'controller_or_source_BFS':0,'new_field_matrix_search':0,'solver_calls':0,'record_count':0,'other_S3_permutation_cases_executed':0,'cpu_seconds':time.process_time()-start,'wall_seconds':time.monotonic()-wall,'pid':os.getpid(),'budget_cpu_seconds':20}
dump('RESULT.json',result);dump('TERMINAL.json',{'status':'TERMINAL','result_status':result['status'],'pending':[],'cpu_seconds':result['cpu_seconds']});dump('HANDLE.json',{'status':'TERMINAL','pid':os.getpid()})
print(json.dumps(result),flush=True)
