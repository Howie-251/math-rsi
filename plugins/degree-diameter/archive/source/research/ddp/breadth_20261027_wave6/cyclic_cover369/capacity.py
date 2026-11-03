from pathlib import Path
import json,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(5,5));P=Path(__file__).resolve().parent;started=time.process_time()
rows=[list(map(int,line.split())) for line in (P/'base41.edges').read_text().splitlines()];n,m=rows[0];edges=[tuple(e) for e in rows[1:]];dist=json.loads((P/'base41_distances.json').read_text());adj=[[] for _ in range(n)]
for e,(u,v) in enumerate(edges):adj[u].append((v,e,1));adj[v].append((u,e,-1))
parent=list(range(n))
def find(u):
 while parent[u]!=u:parent[u]=parent[parent[u]];u=parent[u]
 return u
tree=[]
for e,(u,v) in enumerate(edges):
 a,b=find(u),find(v)
 if a!=b:parent[a]=b;tree.append(e)
free=[e for e in range(m) if e not in tree];assert len(tree)==40 and len(free)==42
(P/'tree_gauge.json').write_text(json.dumps(dict(edges=edges,tree_edge_ids=tree,free_edge_ids=free,reason='For fixed endpoints, two walk coefficient vectors differ by a circulation; a circulation supported only on a tree is zero, so dropping tree coefficients loses no distinct functions.'),indent=2)+'\n')
all_functions=[];records=[];witness=None;total_walks=0
for root in range(n):
 forms=[{} for _ in range(n)];coeff=[0]*m;walk=[root];walks=0
 def rec(u,depth):
  global walks
  walks+=1;c=tuple(coeff)
  if c not in forms[u] or len(walk)<len(forms[u][c]):forms[u][c]=walk.copy()
  if depth==5:return
  for v,e,s in adj[u]:coeff[e]+=s;walk.append(v);rec(v,depth+1);walk.pop();coeff[e]-=s
 rec(root,0);total_walks+=walks;assert walks==1365
 root_functions=[];bad=[]
 for v,ff in enumerate(forms):
  integer={tuple(c[e] for e in free) for c in ff};mod9={tuple(x%9 for x in c) for c in integer};assert len(integer)==len(ff)
  r=dict(source=root,target=v,integer_linear_forms=len(integer),mod9_linear_forms=len(mod9),required9=9);records.append(r);root_functions.append(sorted(mod9))
  if min(len(integer),len(mod9))<9:bad.append((dist[root][v],v,r))
 all_functions.append(root_functions)
 if bad:
  _,v,r=min(bad);witness=dict(**r,base_distance=dist[root][v],full_edge_integer_forms_and_representative_short_walks=[dict(coefficients=c,walk=w) for c,w in sorted(forms[v].items())],free_edge_ids=free,mod9_free_forms=root_functions[v]);break
passed=witness is None
result=dict(status='ALL_ORDERED_FORM_CAPACITIES_PASS' if passed else 'FORM_CAPACITY_OBSTRUCTION_STOP',base_vertices=41,base_edges=82,cyclic_cover_sheets=9,cover_vertices=369,maximum_degree=4,target_diameter=5,saved_threshold=364,complete_walk_length_range=[0,5],walks_per_root=1365,roots_enumerated=len(all_functions),raw_walks_enumerated=total_walks,slots_checked=len(records),tree_gauged_free_edges=42,minimum_integer_forms=min(r['integer_linear_forms'] for r in records),minimum_mod9_forms=min(r['mod9_linear_forms'] for r in records),witness=witness,records=records,voltage_search_started=False,cover_graph_generated=False,CPU_seconds=time.process_time()-started)
(P/'capacity.json').write_text(json.dumps(result,indent=2)+'\n')
if passed:(P/'functions.json').write_text(json.dumps(dict(functions=all_functions,free_edge_ids=free),separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['records','witness']},indent=2))
if witness:print(json.dumps(witness,indent=2))
