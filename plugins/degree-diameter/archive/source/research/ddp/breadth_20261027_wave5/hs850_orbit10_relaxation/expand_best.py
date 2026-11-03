from pathlib import Path
from collections import Counter
import json,time

P=Path(__file__).resolve().parent
t=time.process_time()
d=json.loads((P/'best_parameters.json').read_text())
p=d['parameters'];assert len(p)==26 and all(0<=x<17 for x in p)
X=[[0,1,4,10],[0,2],[0,5],[0],[0]]
gamma=[[p[10+(i-1)*4+k-1] if i and k else 0 for k in range(5)] for i in range(5)]
def vertex(layer,i,j,z):return (25*layer+5*i+j%5)*17+z%17
edges=set()
def edge(u,v):
    assert u!=v
    edges.add(tuple(sorted((u,v))))
for i in range(5):
    for j in range(5):
        for z in range(17):
            edge(vertex(0,i,j,z),vertex(0,i,j+1,z+p[i]))
            edge(vertex(1,i,j,z),vertex(1,i,j+2,z+p[5+i]))
            for k in range(5):
                for c in X[(k-i)%5]:edge(vertex(0,i,j,z),vertex(1,k,j+i*k,z+gamma[i][k]+c))
adj=[set() for _ in range(850)]
for u,v in edges:adj[u].add(v);adj[v].add(u)
assert len(edges)==5100 and all(len(row)==12 for row in adj)
with (P/'best.edges').open('w') as f:
    print(850,5100,file=f)
    for u,v in sorted(edges):print(u,v,file=f)
d.update(alpha=p[:5],beta=p[5:10],gamma=gamma,gamma_zero_row_and_column=True,X_sets=X,
         vertex_encoding='17*(25*layer+5*row+j)+z; layer 0=U,1=V; row,j mod5,z mod17',
         edge_rule='U_i,j,z--U_i,j+1,z+alpha_i; V_k,l,z--V_k,l+2,z+beta_k; U_i,j,z--V_k,j+ik,z+gamma_ik+c, c in X_(k-i)')
(P/'best_parameters.json').write_text(json.dumps(d,indent=2)+'\n')
roots=[85*i for i in range(10)];misses=[];examples=[]
for root in roots:
    seen={root}
    for _ in range(3):seen|={v for u in seen for v in adj[u]}
    bad=sorted(set(range(850))-seen);misses.append(len(bad));examples.append(dict(root=root,missing_vertices=bad))
assert misses==d['root_missing'] and sum(misses)==d['representative_missing_total']
check=dict(status='MATCH',vertices=850,edges=len(edges),simple=True,degree_histogram=dict(Counter(map(len,adj))),
           root_vertex_ids=roots,direct_depth3_root_misses=misses,representative_misses=sum(misses),
           implied_full_unordered_D3_bad_pairs=85*sum(misses)//2,
           symbolic_score_matches=True,scope='production generator and direct exact depth-three reachability on ten proved orbit roots; not root independent all-850-source final BFS',
           root_bad_vertices=examples,CPU_seconds=time.process_time()-t)
(P/'best_direct_check.json').write_text(json.dumps(check,indent=2)+'\n')
print(json.dumps({k:v for k,v in check.items() if k!='root_bad_vertices'},indent=2))
