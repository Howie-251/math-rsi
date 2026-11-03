from pathlib import Path
from functools import lru_cache
from itertools import combinations_with_replacement
from collections import deque
import json,time,resource,csv
B=Path(__file__).resolve().parent;resource.setrlimit(resource.RLIMIT_CPU,(8,8));t0=time.process_time()
assert not (B/'RESULT.json').exists()
def save(n,o):(B/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
@lru_cache(None)
def size(tree):return 1+sum(size(t) for t in tree)
@lru_cache(None)
def rooted(depth,budget):
 if depth==0:return ((),)
 below=rooted(depth-1,budget-1);out=[]
 for k in range(4):
  for kids in combinations_with_replacement(below,k):
   if 1+sum(size(t) for t in kids)<=budget:out.append(kids)
 return tuple(sorted(set(out)))
def attachments(depth,budget):
 branches=rooted(depth-1,budget);out=[]
 for k in range(3):
  for kids in combinations_with_replacement(branches,k):
   if sum(size(t) for t in kids)<=budget:out.append(kids)
 return sorted(set(out))
def canonical(seq):
 rev=seq[::-1];return seq==min([seq[i:]+seq[:i] for i in range(len(seq))]+[rev[i:]+rev[:i] for i in range(len(seq))])
def graph(c,decor):
 g=[set(((i-1)%c,(i+1)%c)) for i in range(c)]
 def add(parent,tree):
  j=len(g);g.append({parent});g[parent].add(j)
  for child in tree:add(j,child)
 for i,kids in enumerate(decor):
  for child in kids:add(i,child)
 return [sorted(x) for x in g]
def test(g):
 deg=list(map(len,g));owners=[i for i,d in enumerate(deg) if d<4];ds=[]
 for r in range(14):
  d=[-1]*14;d[r]=0;q=deque([r])
  while q:
   u=q.popleft()
   for v in g[u]:
    if d[v]<0:d[v]=d[u]+1;q.append(v)
  ds.append(d)
 for u in range(14):
  for w in owners:
   if ds[u][w]>4:return 'G1',{'helper':u,'owner':w,'distance':ds[u][w]}
 for leaf,d in enumerate(deg):
  if d==1 and deg[g[leaf][0]]>=3:
   for w in owners:
    if ds[leaf][w]>=4:return 'G2',{'leaf':leaf,'parent':g[leaf][0],'parent_degree':deg[g[leaf][0]],'owner':w,'distance':ds[leaf][w]}
 return 'SURVIVOR',{}
summary={};survivors=[];records=[]
for c in range(3,8):
 depth=4-c//2;budget=14-c;ats=attachments(depth,budget);weights=[sum(size(t) for t in kids) for kids in ats];counts={'max_attachment_depth':depth,'attachment_types':len(ats),'first_min_ordered_size14_decorations':0,'canonical_topologies':0,'G1_rejected':0,'G2_rejected':0,'survivors':0}
 def rec(seq,remaining):
  if len(seq)==c:
   if remaining:return
   counts['first_min_ordered_size14_decorations']+=1
   if not canonical(tuple(seq)):return
   g=graph(c,[ats[i] for i in seq]);assert len(g)==14 and sum(map(len,g))==28 and max(map(len,g))<=4
   assert sum(4-len(x) for x in g)==28
   status,w=test(g);ordinal=len(records);counts['canonical_topologies']+=1
   if status=='SURVIVOR':counts['survivors']+=1;survivors.append({'id':ordinal,'cycle':c,'decorations':seq.copy(),'adjacency':g})
   else:counts[status+'_rejected']+=1
   records.append({'id':ordinal,'cycle':c,'decorations':seq.copy(),'status':status,'witness':w})
   return
  for i,weight in enumerate(weights):
   if weight>remaining:continue
   # The first decoration is the least in a canonical cycle.
   if seq and i<seq[0]:continue
   rec(seq+[i],remaining-weight)
 rec([],budget);summary[str(c)]=counts
save('ALL_TOPOLOGY_RECORDS.json',records);save('SURVIVOR_TOPOLOGIES.json',survivors)
newcpu=time.process_time()-t0
r={'status':'COMPLETE_NO_FIXED_NATURAL364_PRESERVED_EDGE_HELPERS14' if not survivors else 'NECESSARY_TOPOLOGY_SURVIVORS_NO_PORT_ASSIGNMENT_YET','by_cycle':summary,'canonical_topologies_checked':len(records),'G1_rejected':sum(x['G1_rejected'] for x in summary.values()),'G2_rejected':sum(x['G2_rejected'] for x in summary.values()),'surviving_topologies':len(survivors),'k14_tree':'paperclosedfromoldtriplecapacity;notenumeratedagain','new_numeric_CPU':newcpu,'prior_read_CPU':.5,'prepare_CPU':.25,'case_CPU':.75+newcpu,'case_cap':10,'source_BFS_oldball_oldmask_portassignment_graph_Lean_solver_ARIS':0,'new_accepted_graph_parameter_Lean':[0,0,0],'scope':'fixednatural364/714,max4,D5,preservealloldedges,noaddedoldold,exact14helpers;treepaperNOplusfullunicyclicnecessarygatesifnosurvivors','terminal':True,'next':'STOP_NO_AUTOMATIC_K15_OR_PORT_ASSIGNMENT_WHEN_NOSURVIVORS;general4D5notexcluded'}
assert r['case_CPU']<10
save('RESULT.json',r);save('TERMINAL.json',{'terminal':True,'result':'RESULT.json'});print(json.dumps(r,ensure_ascii=False))
