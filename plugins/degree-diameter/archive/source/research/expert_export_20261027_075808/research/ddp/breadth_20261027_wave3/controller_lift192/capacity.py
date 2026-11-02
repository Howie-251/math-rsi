from pathlib import Path
import json,time

P=Path(__file__).resolve().parent;t=time.process_time()
edges=[(0,2),(0,3),(0,4),(0,4),(1,2),(1,3),(1,5),(1,5),(2,4),(2,5),(3,4),(3,5)]
source_gamma=[(1,0),(2,4),(2,0),(2,5),(1,2),(3,5),(1,1),(1,0),(2,2),(1,5),(1,5),(3,1)]
tree=[0,1,2,4,6];free=[i for i in range(12) if i not in tree]
assert len(free)==7
adj=[[] for _ in range(6)]
for i,(u,v) in enumerate(edges):adj[u].append((v,i,1));adj[v].append((u,i,-1))
assert all(len(row)==4 for row in adj)
walks=[[[] for _ in range(6)] for _ in range(6)]
for root in range(6):
 def rec(u,prev_edge,steps,coeff,word):
  if len(word)==5:walks[root][u].append((tuple(coeff),tuple(word)));return
  for v,e,s in adj[u]:
   if e==prev_edge:continue
   coeff[e]+=s;word.append((e,s));rec(v,e,steps+1,coeff,word);word.pop();coeff[e]-=s
 rec(root,-1,0,[0]*12,[])
assert all(sum(map(len,row))==324 for row in walks)
records=[];source_sets=[]
for u in range(6):
 for v in range(6):
  funcs={tuple(c[e]%8 for e in free) for c,_ in walks[u][v]}
  source={(sum(c[e]*source_gamma[e][0] for e in range(12))%4,sum(c[e]*source_gamma[e][1] for e in range(12))%6) for c,_ in walks[u][v]}
  assert len(source)==24
  records.append(dict(root=u,target=v,raw_walks=len(walks[u][v]),distinct_C4_C8_functions=len(funcs),required_fiber_states=32,functions=sorted(funcs)))
  source_sets.append(dict(root=u,target=v,reached=len(source)))
minimum=min(x['distinct_C4_C8_functions'] for x in records)
result=dict(status='CAPACITY_ALLOWS_FINITE_VOLTAGE_TRIAL' if minimum>=32 else 'STOPPED_UNIFORM_EXACT_NB5_CAPACITY_OBSTRUCTION',base_vertices=6,base_edges=edges,tree_edges=tree,free_edges=free,voltage_group='C4 direct_product C8',controller_vertices=192,target_controller='exact length5 nonbacktracking walk coverage',required_fiber_states=32,minimum_symbolic_capacity=minimum,records=records,source_C4_C6_table_reproduction=source_sets,source_original_gamma=source_gamma,CPU_seconds=time.process_time()-t,actual192_graphs_generated=0,full_lift_generated=False)
(P/'capacity.json').write_text(json.dumps(result,indent=2)+'\n')
inputs=dict(edges=edges,source_gamma=source_gamma,tree=tree,free=free,words=[[[dict(coeff=c,word=w) for c,w in walks[u][v]] for v in range(6)] for u in range(6)])
(P/'base_words.json').write_text(json.dumps(inputs)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['records','source_C4_C6_table_reproduction','source_original_gamma']}))
print('capacities',[[records[6*u+v]['distinct_C4_C8_functions'] for v in range(6)] for u in range(6)])
