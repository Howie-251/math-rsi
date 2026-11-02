import collections,itertools,json,os,resource,time
from pathlib import Path
D=Path(__file__).resolve().parent;ROOT=D.parents[3]
resource.setrlimit(resource.RLIMIT_CPU,(19,20));start=time.process_time();wall=time.monotonic()
def dump(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
dump('HANDLE.json',{'status':'RUNNING','pid':os.getpid()})
src=ROOT/'research/ddp/breadth_20261027_wave4/mizuno_d3_source'
source=json.load(open(src/'construction.json'));structure=json.load(open(src/'controller_structure.json'))
C=source['controller'];triangles=structure['triangles'];cycles=structure['external_2factor_cycles']
E={tuple(sorted((u,v))) for u,row in enumerate(C) for v in row}
assert len(C)==30 and len(E)==60 and all(len(row)==4 for row in C)
assert len(triangles)==10 and sorted(sum(triangles,[]))==list(range(30))
assert len(cycles)==6 and all(len(c)==5 for c in cycles)
cycle_of={v:i for i,c in enumerate(cycles) for v in c}
Tedges={tuple(sorted((a,b))) for T in triangles for a,b in itertools.combinations(T,2)}
Xedges={tuple(sorted((c[i],c[(i+1)%5]))) for c in cycles for i in range(5)}
assert len(Tedges)==30 and len(Xedges)==30 and Tedges.isdisjoint(Xedges) and E==Tedges|Xedges
newtri=[30,31,32];newTedges=set(itertools.combinations(newtri,2))
cases=[];passes=[];distinct=set();firstclass=collections.Counter();allmissclass=collections.Counter()
def cls(u,v):
 if u==v:return 'self'
 if u<30 and v<30:return 'old-old'
 if u>=30 and v>=30:return 'new-new'
 return 'new-old'
for ti,T in enumerate(triangles):
 oldT=sorted(T);choices=[sorted(set(C[v])-set(oldT)) for v in oldT]
 assert all(len(x)==2 for x in choices)
 assert len({cycle_of[v] for v in oldT})==3
 for choice in itertools.product(range(2),repeat=3):
  rs=[choices[i][choice[i]] for i in range(3)]
  cuts={tuple(sorted((v,r))) for v,r in zip(oldT,rs)}
  assert len(cuts)==3 and cuts<=Xedges
  add=set(newTedges)
  for i,(v,r) in enumerate(zip(oldT,rs)):
   add.add(tuple(sorted((v,30+i))));add.add(tuple(sorted((r,30+i))))
  edges=(E-cuts)|add
  assert len(edges)==66
  signature=tuple(sorted(edges));assert signature not in distinct;distinct.add(signature)
  adj=[set() for _ in range(33)]
  for u,v in edges:
   assert u!=v;adj[u].add(v);adj[v].add(u)
  assert all(len(a)==4 for a in adj)
  # Exact external cycles after deleting the eleven designated triangle edge sets.
  ext=edges-(Tedges|newTedges);extadj=[set() for _ in range(33)]
  for u,v in ext:extadj[u].add(v);extadj[v].add(u)
  assert len(ext)==33 and all(len(a)==2 for a in extadj)
  unseen=set(range(33));actualcycles=[]
  while unseen:
   a=min(unseen);prev=-1;u=a;cyc=[]
   while True:
    cyc.append(u);unseen.remove(u)
    nxt=min(extadj[u]-{prev}) if prev in extadj[u] else min(extadj[u])
    prev,u=u,nxt
    if u==a:break
   actualcycles.append(cyc)
  assert sorted(map(len,actualcycles))==[5,5,5,6,6,6]
  counts=[[0]*33 for _ in range(33)]
  for u in range(33):
   for a in adj[u]:
    for b in adj[a]:
     if b==u:continue
     for v in adj[b]:
      if v!=a:counts[u][v]+=1
   assert sum(counts[u])==36
  missing=[(u,v) for u in range(33) for v in range(33) if v not in adj[u] and counts[u][v]==0]
  mc=collections.Counter(cls(u,v) for u,v in missing)
  allmissclass.update(mc)
  first=missing[0] if missing else None
  if first:firstclass[cls(*first)]+=1
  cid=len(cases)
  rec={'candidate_index':cid,'source_triangle_index':ti,'old_triangle':oldT,'new_triangle':newtri,'choice_bits':choice,'chosen_external_neighbors':rs,'cut_edges':sorted(cuts),'added_edges':sorted(add),'n':33,'m':66,'simple':True,'degree_histogram':{'4':33},'external_cycle_sizes':[5,5,5,6,6,6],'extended_source_C5_indices':sorted({cycle_of[v] for v in oldT}),'missing_nonadjacent_or_equal_NB3_ordered_pairs':len(missing),'missing_class_counts':dict(mc),'first_missing':None if first is None else {'u':first[0],'v':first[1],'class':cls(*first),'NB3_count':0},'NB3_nonadjacent_or_equal_min':min(counts[u][v] for u in range(33) for v in range(33) if v not in adj[u]),'pass':not missing,'controller_edges':signature,'ordinary_global_D':None,'ordinary_bad_pairs':None}
  cases.append(rec)
  if not missing:passes.append(rec)
assert len(cases)==80 and len(distinct)==80
dump('INPUT.json',{'source_controller_n':30,'source_controller_m':60,'source_triangles':triangles,'source_C5s':cycles,'source_edges':sorted(E),'source_relation':'Actual edge-local F4 matrix source; raw gate independent of field matrices','new_labels':newtri,'candidate_count':80,'literal_duplicate_count':0})
dump('CASES.json',cases);dump('PASSERS.json',passes)
result={'status':'COMPLETE_80_RAW_GATE_NO_PASS' if not passes else 'COMPLETE_80_RAW_GATE_WITH_PASSERS','structural_prediction':'SUPPORTED','existence_prediction':'REFUTED' if not passes else 'SUPPORTED_RAW_ONLY','controller_candidates_generated':80,'raw_NB3_candidates_checked':80,'distinct_literal_controllers':80,'pass_count':len(passes),'failed_count':80-len(passes),'untested_count':0,'first_missing_class_histogram':dict(firstclass),'all_missing_class_occurrence_counts':dict(allmissclass),'missing_ordered_count_histogram':dict(sorted(collections.Counter(c['missing_nonadjacent_or_equal_NB3_ordered_pairs'] for c in cases).items())),'hypothetical_target_n':2112,'hypothetical_target_Delta':16,'hypothetical_target_D':3,'actual_fiber_target_graphs':0,'actual_fiber_target_n':None,'actual_fiber_target_D':None,'controller_or_source_BFS':0,'new_field_matrix_search':0,'solver_calls':0,'record_count':0,'cpu_seconds':time.process_time()-start,'wall_seconds':time.monotonic()-wall,'pid':os.getpid(),'budget_cpu_seconds':20}
dump('RESULT.json',result);dump('TERMINAL.json',{'status':'TERMINAL','result_status':result['status'],'pending':[],'cpu_seconds':result['cpu_seconds']})
dump('HANDLE.json',{'status':'TERMINAL','pid':os.getpid()})
print(json.dumps(result),flush=True)
