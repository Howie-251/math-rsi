from collections import Counter, deque
from itertools import combinations
import json
C=[('c',i,j) for i in range(5) for j in range(5)]
A=[('a',i) for i in range(5)]; B=[('b',i) for i in range(5)]
vertices=C+A+B
index={v:i for i,v in enumerate(vertices)}
def label(v):
    return ('d'+str(v[1])) if v[0]=='c' and v[1]==v[2] else (f'c{v[1]}{v[2]}' if v[0]=='c' else v[0]+str(v[1]))
def colors(v): return (v[1],v[2]) if v[0]=='c' else (v[1],v[1])
def diag(i,k): return ('c',i,i) if k==0 else ('a' if k==1 else 'b',i)
def edge(x,y): return tuple(sorted((index[x],index[y])))
fixed=set()
for i in range(5):
    for j in range(5):
        for dx,dy in ((1,1),(2,3)):
            fixed.add(edge(('c',i,j),('c',(i+dx)%5,(j+dy)%5)))
for i in range(5):
    fixed.remove(edge(diag(i,0),diag((i+1)%5,0)))
    for k in (1,2): fixed.add(edge(diag(i,k),diag((i+2)%5,k)))
results=[]
for rule in ('boundary_splice','uniform_layer_shift'):
    edges=set(fixed)
    for i in range(5):
        for k in range(3):
            kp=(k+1)%3 if rule=='uniform_layer_shift' or i==4 else k
            edges.add(edge(diag(i,k),diag((i+1)%5,kp)))
    ns=[set() for _ in vertices]
    for i,j in edges: ns[i].add(j); ns[j].add(i)
    seen={0}; q=deque([0])
    while q:
        i=q.popleft()
        for j in ns[i]-seen: seen.add(j); q.append(j)
    assert len(seen)==35 and len(edges)==70 and all(len(row)==4 for row in ns)
    for i,v in enumerate(vertices):
        assert {colors(vertices[w])[0] for w in ns[i]|{i}}==set(range(5))
        assert {colors(vertices[w])[1] for w in ns[i]|{i}}==set(range(5))
    matrix=[[sum(colors(v)==(i,j) for v in vertices) for j in range(5)] for i in range(5)]
    assert matrix==[[1+2*(i==j) for j in range(5)] for i in range(5)]
    triangles=[sum(v in ns[u] for u,v in combinations(ns[i],2)) for i in range(35)]
    common=[[len(ns[i]&ns[j]) for j in range(35)] for i in range(35)]
    for i,j in combinations(range(35),2):
        if any(colors(vertices[i])[k]==colors(vertices[j])[k] for k in (0,1)):
            assert j not in ns[i] and common[i][j]==0
    out=dict(rule=rule,n=35,edges=70,connected=True,degree_four=True,both_local_bijections=True,intersection_matrix=matrix,triangles=sum(triangles)//3,max_triangles_per_vertex=max(triangles))
    if rule=='uniform_layer_shift':
        assert not any(triangles)
        lower=[]
        for i in range(35):
            value=0
            for j in range(35):
                if i!=j:
                    partial=common[i][j]+int(j in ns[i])+sum(colors(vertices[i])[k]==colors(vertices[j])[k] for k in (0,1))
                    value+=max(0,partial-1)
            lower.append(value)
        i=index[('a',0)]
        witness=[]
        for w in [('b',3),('b',4),('c',2,2),('c',0,0),('b',0)]:
            j=index[w]; same=sum(colors(vertices[i])[k]==colors(w)[k] for k in (0,1))
            witness.append(dict(other=label(w),H_common=sorted(label(vertices[t]) for t in ns[i]&ns[j]),shared_UV_parents=same,defect_lower_bound=common[i][j]+int(j in ns[i])+same-1))
        assert sum(r['defect_lower_bound'] for r in witness)==6
        out.update(a0_neighbors=sorted(label(vertices[t]) for t in ns[i]),a0_defect_witness=witness,defect_row_lower_histogram=dict(Counter(lower)),a0_partial_defect_row=lower[i])
    results.append(out)
print(json.dumps(results,indent=2))
