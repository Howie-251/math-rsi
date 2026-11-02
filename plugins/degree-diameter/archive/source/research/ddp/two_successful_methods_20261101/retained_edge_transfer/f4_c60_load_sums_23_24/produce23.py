"""Run only after root's positive public comparison and explicit execution notice.
Fixed cap23/r21+r22 recipe; no solver, no other cap/plane/seed choices.
"""
import argparse,collections,json,resource,time
from pathlib import Path
ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--execute-cap23',action='store_true',required=True);parser.parse_args()
 if (D/'GRAPH_RESULT_d23.json').exists():raise SystemExit('This fixed recipe already has a production result; do not rerun.')
 prep=json.loads((D/'PREPARATION_RESULT.json').read_text())['CPU_seconds'];limit=max(1,int(30-prep));resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1));start=time.process_time()
 def guard():
  if time.process_time()-start+prep>29:raise RuntimeError('aggregate30CPU preparation/production reserve reached')
 recipe=json.loads((D/'RECIPE_d23.json').read_text());assert recipe['cap']==23 and recipe['predicted_n']==4336 and recipe['predicted_m']==48320
 with (ROOT/recipe['source_file']).open()as f:
  n0,m0=map(int,f.readline().split());edges=[tuple(map(int,row.split()))for row in f if row.strip()]
 assert (n0,m0)==(3840,38400) and len(edges)==m0
 oldadj=[[]for _ in range(n0)]
 for u,v in edges:oldadj[u].append(v);oldadj[v].append(u)
 adj=[row.copy()for row in oldadj];degree=list(map(len,adj));steps=[]
 for item in recipe['ordered_centers']:
  guard();j=item['clone_index'];owner=item['owner'];pins=sorted(oldadj[owner]);n=len(adj);assert n==3840+j==item['new_vertex'] and len(pins)==20
  before=[degree[v]for v in pins];assert max(before)<23
  distance=[-1]*n;queue=[]
  for v in pins:distance[v]=0;queue.append(v)
  for v in queue:
   if distance[v]==2:continue
   for w in adj[v]:
    if distance[w]<0:distance[w]=distance[v]+1;queue.append(w)
  assert len(queue)==n
  steps.append(dict(**item,pins=pins,pin_degrees_before_addition=before,current_n_before_addition=n,closed_R2_current_covered=n,uncovered_targets=0,pin_distance_histogram=dict(collections.Counter(distance))))
  adj.append(pins.copy());degree.append(20)
  for v in pins:adj[v].append(n);degree[v]+=1;edges.append((v,n))
 guard();N=len(adj);M=len(edges);assert(N,M)==(4336,48320) and max(degree)<=23
 assert all(degree[v]==20+recipe['old_fiber_loads'][v//64]for v in range(3840))
 rows=sorted((min(u,v),max(u,v))for u,v in edges);assert len(rows)==len(set(rows)) and all(u!=v for u,v in rows)
 seen={0};todo=[0]
 for v in todo:
  for w in adj[v]:
   if w not in seen:seen.add(w);todo.append(w)
 assert len(seen)==N
 with (D/'graph_d23_D3_n4336.edges').open('w')as f:
  f.write(f'{N} {M}\n')
  for u,v in rows:f.write(f'{u} {v}\n')
 recipe['status']='PRODUCER_CURRENT_COMPLETE_R2_EXTENSION_INDUCTION';recipe['graph_generated']=True;recipe['steps']=steps;(D/'RECIPE_d23.json').write_text(json.dumps(recipe,indent=2)+'\n')
 result=dict(status='PRODUCER_COMPLETE_LITERAL_GRAPH_CURRENT_R2_INDUCTION',cap=23,D=3,n=N,m=M,clone_count=496,degree_histogram=dict(sorted(collections.Counter(degree).items())),old_edges_retained=38400,simple=True,max_degree=max(degree),connected=True,connectivity_single_root_traversal=True,connectivity_vertices_seen=len(seen),current_complete_R2_pin_union_checks=496,uncovered_targets_each_step=0,source_distance_BFS_runs=0,independent_BFS_runs=0,solver_calls=0,graph_file='graph_d23_D3_n4336.edges',CPU_seconds=time.process_time()-start,aggregate_preparation_production_CPU_seconds=time.process_time()-start+prep,aggregate_CPU_limit=30,fresh_independent_acceptance='PENDING_ROOT',new_global_record_claim=False)
 (D/'GRAPH_RESULT_d23.json').write_text(json.dumps(result,indent=2)+'\n');(D/'TERMINAL_d23.json').write_text(json.dumps(dict(status='COMPLETE',running=False,**{k:result[k]for k in ['n','m','CPU_seconds','aggregate_preparation_production_CPU_seconds']}),indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
