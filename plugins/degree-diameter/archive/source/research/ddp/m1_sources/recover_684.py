"""Reconstruct all source edges from recovered semidirect coordinates."""
from pathlib import Path
from collections import deque,Counter
import json
P=Path(__file__).resolve().parent
m,n,r=38,9,23

def mul(g,h):
 a,b=g;c,d=h
 return ((a+pow(r,b,m)*c)%m,(b+d)%n)
def inv(g):
 a,b=g
 return ((-pow(r,(-b)%n,m)*a)%m,(-b)%n)
def encode(b,g):return b*m*n+g[0]*n+g[1]
S0=[(4,4),(8,5),(25,3),(29,6)]
S1=[(10,1),(23,6),(26,8),(29,3)]
T=[(2,2),(2,6),(24,3)]
S=[[S0,T],[[inv(t) for t in T],S1]]
assert pow(r,n,m)==1
assert all(inv(x) in S0 for x in S0) and all(inv(x) in S1 for x in S1)
edges=set()
for b in (0,1):
 for a in range(m):
  for k in range(n):
   u=encode(b,(a,k))
   for c in (0,1):
    for s in S[b][c]:
     v=encode(c,mul((a,k),s));assert u!=v
     edges.add(tuple(sorted((u,v))))
source=set()
for line in (P/'graph_7_4_n684.txt').read_text().splitlines():
 if not line.startswith('#'):source.add(tuple(map(int,line.split())))
assert edges==source
adj=[[] for _ in range(684)]
for u,v in sorted(edges):adj[u].append(v);adj[v].append(u)
assert {len(x) for x in adj}=={7}
root_distributions={}
for u in (0,342):
 dist=[-1]*684;dist[u]=0;q=deque([u])
 while q:
  v=q.popleft()
  for w in adj[v]:
   if dist[w]==-1:dist[w]=dist[v]+1;q.append(w)
 assert min(dist)==0 and max(dist)==4
 root_distributions[str(u)]=dict(sorted(Counter(dist).items()))
out={'group':'C38 semidirect C9','m':m,'n':n,'r':r,'multiplication':'(a,b)*(c,d)=((a+r^b*c) mod m,(b+d) mod n)','vertex_id':'type*m*n+a*n+b','voltage_sets':S,'order':684,'degree':7,'edge_count':len(edges),'recovered_equals_source':True,'root_distance_distributions':root_distributions,'diameter_verification':'2 orbit representatives; left multiplication acts regularly on each of the two fibers'}
(P/'684_recovered_construction.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
