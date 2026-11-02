from pathlib import Path
from collections import deque
import json,random,resource,subprocess,time

B=Path(__file__).resolve().parent
start_wall=time.monotonic()
def usage():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
c0=usage()
cap=json.loads((B/'CAPACITY.json').read_text());assert cap['Q8_necessary_pass']
edges=[tuple(x) for x in cap['edges']];free=cap['free_edge_ids']
def dump(name,x):(B/name).write_text(json.dumps(x,indent=2)+'\n')
units=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1)]
index={x:i for i,x in enumerate(units)}
def times(x,y):
 a,b,c,d=x;e,f,g,h=y
 return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def mult(g,h):return index[times(units[g],units[h])]
inverse=[next(j for j in range(8) if mult(i,j)==0) for i in range(8)]
rng=random.Random(20261027142)
starts=[]
for _ in range(12):
 h=[0]*28
 for e in free:h[e]=rng.randrange(8)
 starts.append(h)
adj=[set() for _ in range(112)]
for e,(i,j) in enumerate(edges):
 for g in range(8):
  u=8*i+g;v=8*j+mult(g,starts[0][e]);adj[u].add(v);adj[v].add(u)
assert all(len(a)==4 and u not in a for u,a in enumerate(adj))
dist=[]
for i in range(14):
 d=[-1]*112;d[8*i]=0;q=deque([8*i])
 while q:
  u=q.popleft()
  for v in adj[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 dist.extend(d)
dump('first_python_check.json',dict(simple=True,vertices=112,edges=224,degree=4,quaternion_tuple_multiplication=True,complete_adjacency=[sorted(a) for a in adj],fourteen_complete_distance_arrays=dist,source='first actual random start, not an extra pilot'))
dump('group_and_graph_definition.json',dict(group='Q8',group_labels=units,identity=0,inverses=inverse,tuple_product='Hamilton quaternion multiplication',base_vertices=14,base_edges=edges,tree_edge_ids=cap['tree_edge_ids'],free_edge_ids=free,vertex_labels='8*i+g',edge_rule='for every oriented base edge i<j with voltage h_e and every g, join (i,g) to (j,g*h_e)',left_action='(i,g)->(i,a*g) gives14 proven orbits; bad unordered pairs=4*sum14 root deficits',target_degree=4,target_diameter=4,saved_baseline=104))
dump('starts.json',dict(start_seed=20261027142,kick_seed=20261027143,starts=starts,segments_per_start=3,max_strict_moves_per_segment=12,neighbors_per_scan=105))
lines=['28']+[f'{u} {v}' for u,v in edges]+[' '.join(map(str,free)),'12']+[' '.join(map(str,h)) for h in starts]+[' '.join(str(v) for a in adj for v in sorted(a)),' '.join(map(str,dist))]
(B/'input.txt').write_text('\n'.join(lines)+'\n')
subprocess.run(['g++','-std=c++17','-O3',str(B/'search.cpp'),'-o',str(B/'search')],check=True)
prep=usage()-c0;remaining=max(0,60-prep-cap['CPU_seconds']-1)
dump('run.json',dict(status='RUNNING',running=True,preparation_CPU_seconds=prep,capacity_CPU_seconds=cap['CPU_seconds'],production_budget=remaining,total_CPU_budget=60,worker_count=1,restarts=0))
with (B/'search.log').open('w') as log:r=subprocess.run([str(B/'search'),str(B),str(remaining)],stdout=log,stderr=subprocess.STDOUT)
assert r.returncode==0,(r.returncode,(B/'search.log').read_text()[-2000:])
t=json.loads((B/'terminal.json').read_text());t.update(preparation_CPU_seconds=prep,capacity_CPU_seconds=cap['CPU_seconds'],total_measured_CPU_seconds=usage()-c0+cap['CPU_seconds'],driver_wall_seconds=time.monotonic()-start_wall,total_CPU_budget=60,worker_count=1,restarts=0)
dump('terminal.json',t);dump('run.json',dict(status=t['status'],running=False,total_measured_CPU_seconds=t['total_measured_CPU_seconds'],pending=t['pending']))
print(json.dumps(t))
