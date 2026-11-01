"""Exact forest consequence on four unit8 points avoiding the unique codegree3 pair.
The entire codegree1 graph need not be a forest: cycles of length>=5 remain possible.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
HERE=Path(__file__).parent;rs=json.loads((HERE/'FOUR_REMAINDERS.json').read_text())['cases'];out=[]
for r in rs:
 ns={int(t):n for t,n in r['counts'].items()};edges=[];cs=[]
 for i,j in combinations(range(4),2):
  c=sum(n for t,n in ns.items() if t>>(i+1)&1 and t>>(j+1)&1);cs.append(c)
  if c==1:edges.append((i,j))
 if 3 in cs:continue
 adj=[set() for i in range(4)]
 for i,j in edges:adj[i].add(j);adj[j].add(i)
 seen=set();components=0
 for i in range(4):
  if i in seen:continue
  components+=1;stack=[i];seen.add(i)
  while stack:
   v=stack.pop()
   for j in adj[v]:
    if j not in seen:seen.add(j);stack.append(j)
 assert len(edges)==4-components
 out.append(dict(id=r['id'],codegree1_edges=edges,sorted_degrees=sorted(map(len,adj)),edge_count=len(edges)))
seq=sorted({tuple(r['sorted_degrees']) for r in out});assert seq==[(0,0,0,0),(0,0,1,1),(0,1,1,2),(1,1,1,1),(1,1,2,2),(1,1,1,3)] or set(seq)=={(0,0,0,0),(0,0,1,1),(0,1,1,2),(1,1,1,1),(1,1,2,2),(1,1,1,3)}
result=dict(status='PASS',scope=__doc__,four_views_avoiding_codegree3=len(out),degree_sequences=seq,all_forests=True,cases=out);(HERE/'FOREST_STRUCTURE.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k!='cases'})
