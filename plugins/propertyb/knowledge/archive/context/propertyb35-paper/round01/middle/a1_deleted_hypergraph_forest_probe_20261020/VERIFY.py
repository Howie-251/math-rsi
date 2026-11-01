"""Independent explicit Hbar and maximum-tree verification; no search or C++ import."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
a=json.loads((P/'BEST.json').read_text());edges=[frozenset(e) for e in a['edges']]
assert len(edges)==len(set(edges))==29
assert all(len(e)==5 and all(0<=v<20 for v in e) for e in edges)
d=[sum(v in e for e in edges) for v in range(20)];assert d==[6]*5+[7]*5+[8]*10==a['degrees']
weights={0:506,1:22,2:132,3:572,4:2002}
pairs=[(weights[len(edges[i]&edges[j])],i,j,len(edges[i]&edges[j])) for i,j in combinations(range(29),2)]
hist=Counter(j for w,i,k,j in pairs);assert [hist[i] for i in range(5)]==a['intersection_histogram']
assert sum(w for w,i,k,j in pairs)==a['pair_weight_sum']
# Independent Kruskal, retaining an explicit maximum tree.
parent=list(range(29));tree=[]
def find(i):
 while parent[i]!=i:i=parent[i]
 return i
for w,i,k,j in sorted(pairs,reverse=True):
 u,v=find(i),find(k)
 if u!=v:parent[u]=v;tree.append([i,k,j,w])
assert len(tree)==28;K=sum(row[3] for row in tree)
# A separate dense Prim calculation on the literal sets.
seen=set();key=[-1]*29;key[0]=0;Pr=0
for _ in range(29):
 v=max((i for i in range(29) if i not in seen),key=lambda i:key[i]);seen.add(v);Pr+=key[v]
 for u in range(29):
  if u not in seen:key[u]=max(key[u],weights[len(edges[u]&edges[v])])
# Threshold ranks characterize the maximum possible tree weight, independently of either tree.
ranks=[]
for threshold in [132,506,572,2002]:
 unseen=set(range(29));components=0
 while unseen:
  components+=1;stack=[unseen.pop()]
  while stack:
   u=stack.pop();neighbours={v for v in unseen if weights[len(edges[u]&edges[v])]>=threshold}
   unseen-=neighbours;stack.extend(neighbours)
 ranks.append(29-components)
rank_value=22*28+110*ranks[0]+374*ranks[1]+66*ranks[2]+1430*ranks[3]
assert K==Pr==rank_value==a['F']
res=dict(status='PASS',scope='One explicit degree-correct Hbar; no paircover or extension-to-A1 claim',vertices=20,edges=29,degrees=d,
 F=K,threshold=9278,hit=K<=9278,maximum_tree=tree,intersection_histogram=[hist[i] for i in range(5)],
 threshold_rank=dict(zip([132,506,572,2002],ranks)),independent_algorithms=['Kruskal','Prim','threshold-component rank identity'],cpu_seconds=time.process_time()-st)
(P/'VERIFY.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items() if k!='maximum_tree'},indent=2))
