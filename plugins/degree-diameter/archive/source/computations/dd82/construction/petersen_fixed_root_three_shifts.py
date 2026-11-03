#!/usr/bin/env python3
"""Exact three-involution subfamily; no SAT and no randomized graph search."""
from itertools import combinations,product
from collections import Counter,deque
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent
A=[5,9,8,7,6,3,2,1,0,4]
P=[{(i+1)%5,(i-1)%5,i+5} for i in range(5)]+[{5+(i+2)%5,5+(i-2)%5,i} for i in range(5)]
Q=[{v for v in range(10) if A[v] in P[A[u]]} for u in range(10)]
E=list(combinations(range(5),2));shifts=[1,2,4]
def graph(cs):
 adj=[set() for _ in range(60)]
 def edge(u,v):adj[u].add(v);adj[v].add(u)
 for i in range(6):
  for u in range(10):
   for v in (P if i==5 else Q)[u]:edge(10*i+u,10*i+v)
 for i in range(5):
  for u in range(10):edge(50+u,10*i+u)
 for (i,j),c in zip(E,cs):
  t=shifts[c]
  for u in range(10):
   v=5+(u+t)%5 if u<5 else (u-t)%5
   edge(10*i+u,10*j+v)
 return adj

def missing(adj):
 masks=[sum(1<<v for v in row) for row in adj];count=0
 for u in range(60):
  cover=(1<<u)|masks[u]
  for v in adj[u]:cover|=masks[v]
  count+=60-cover.bit_count()
 return count//2

def main():
 t=time.process_time();good=0;hist=Counter();best=2000;bestcs=None
 for cs in product(range(3),repeat=10):
  if not all(len({cs[k] for k,e in enumerate(E) if i in e})==3 for i in range(5)):continue
  good+=1;adj=graph(cs);e=missing(adj);hist[e]+=1
  if e<best:best=e;bestcs=cs
 adj=graph(bestcs);edges=[(u,v) for u in range(60) for v in adj[u] if u<v]
 out=HERE/'petersen_fixed_root_three_shifts.best.edges'
 out.write_text(f'60 {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
 # Independent adjacency reconstruction and all-source BFS from the saved edge file.
 rows=[list(map(int,l.split())) for l in out.read_text().splitlines()]
 n,m=rows[0];independent=[set() for _ in range(n)]
 for u,v in rows[1:]:independent[u].add(v);independent[v].add(u)
 distances=Counter();bad=[]
 for u in range(n):
  ds=[-1]*n;ds[u]=0;queue=deque([u])
  while queue:
   v=queue.popleft()
   for w in independent[v]:
    if ds[w]<0:ds[w]=ds[v]+1;queue.append(w)
  for v in range(u+1,n):
   distances[ds[v]]+=1
   if ds[v]>2 or ds[v]<0:bad.append({'u':u,'v':v,'distance':ds[v],'common_neighbors':sorted(independent[u]&independent[v]),'neighbors_u':sorted(independent[u]),'neighbors_v':sorted(independent[v])})
 assert len(bad)==best and all(len(row)==8 for row in independent)
 result={'scope':'fixed A; root matchings normalized identity; each of ten exterior matchings one of three involutions t=1,2,4',
 'assignments_checked':3**10,'root_coverage_assignments':good,'complete_for_stated_subfamily':True,
 'uncovered_pair_histogram':dict(sorted(hist.items())),'minimum_uncovered_pairs':best,
 'best_matching_shifts':[{'fibers':list(pair),'shift':shifts[c]} for pair,c in zip(E,bestcs)],
 'cpu_seconds':time.process_time()-t}
 (HERE/'petersen_fixed_root_three_shifts.json').write_text(json.dumps(result,indent=2)+'\n')
 verification={'n':n,'m':m,'degree_histogram':dict(Counter(map(len,independent))),
 'distance_histogram':dict(sorted(distances.items())),'uncovered_pair_count':len(bad),
 'all_root_pairs_covered':all(b['u']<50 and b['v']<50 for b in bad),
 'valid_degree8_diameter2':not bad,'uncovered_pairs':bad}
 out.with_suffix('.verification.json').write_text(json.dumps(verification,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
