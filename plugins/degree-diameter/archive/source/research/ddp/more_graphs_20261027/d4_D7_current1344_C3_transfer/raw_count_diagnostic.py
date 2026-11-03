"""Count cached-source NB routes, then retain a literal minimum-slot word.

This is an endpoint-count diagnostic, not graph BFS or voltage search.
"""
from collections import Counter
import json
from pathlib import Path
import time
P=Path(__file__).resolve().parent
start=time.process_time()
source=json.loads((P/'SOURCE.json').read_text())
G=[tuple(x) for x in json.loads((P/'group_permutation_images0based.json').read_text())]
index={g:i for i,g in enumerate(G)}
W=[tuple(x-1 for x in row) for row in source['W_images_1based']]
def inverse(g):
    out=[0]*32
    for i,j in enumerate(g):out[j]=i
    return tuple(out)
V=W+[inverse(W[4]),inverse(W[5])]
ports=[[(0,0,1),(0,1,2),(1,4,5),(1,5,6)],[(1,2,3),(1,3,4),(0,6,-5),(0,7,-6)]]
adj=[];named=[]
for b in range(2):
    for g in G:
        row=[(672*c+index[tuple(V[j][g[k]] for k in range(32))],name) for c,j,name in ports[b]]
        named.append(row);adj.append([v for v,_ in row])
assert all(len(set(row))==4 and u not in row for u,row in enumerate(adj))
assert all(u in adj[v] for u,row in enumerate(adj) for v in row)
def A(v):return [sum(v[j] for j in row) for row in adj]
p0=[0]*1344;p0[0]=1;p1=A(p0)
total=[a+b for a,b in zip(p0,p1)];lengths=[1,4]
for k in range(2,9):
    av=A(p1);nxt=[x-(4 if k==2 else 3)*y for x,y in zip(av,p0)]
    total=[x+y for x,y in zip(total,nxt)];lengths.append(sum(nxt));p0,p1=p1,nxt
minimum=min(total)
first=next(i for i,n in enumerate(total) if n==minimum)
# A direct finite-word enumeration checks the diagnosed recurrence and exports
# the actual minimum-slot word; no new graph family is examined.
counter=Counter();targetwords=[];identitywords=[];stack=[(0,-1,())]
while stack:
    u,prev,word=stack.pop();counter[u]+=1
    if u==first:targetwords.append(list(word))
    if u==0:identitywords.append(list(word))
    if len(word)<8:
        for v,name in named[u]:
            if v!=prev:stack.append((v,u,word+(name,)))
assert [counter[u] for u in range(1344)]==total
assert lengths==[1,4,12,36,108,324,972,2916,8748]
result=dict(status='ARBITRARY_THREE_SHEET_SOURCE_COVER_D8_EXCLUDED',
    source_root_base=0,source_group=0,max_length=8,
    word_count_convention='All graph-NB walks of lengths0..8 including the empty word, with sheet coordinate forgotten.',
    algorithms=['Exact4regular NB recurrence on cached source','Direct graph-NB word enumeration: all1344 endpoint counts MATCH'],
    walks_by_length=lengths,raw_counts_by_base=[total[:672],total[672:]],
    minimum_raw_count=minimum,number_below3=sum(x<3 for x in total),
    all_slots_below3=[dict(base=i//672,group=i%672,count=n) for i,n in enumerate(total) if n<3],
    minimum_witness=dict(base=first//672,group=first%672,permutation_images_1based=[x+1 for x in G[first%672]],
                         complete_words=targetwords,raw_count=minimum),
    identity_raw_count=total[0],identity_complete_words=identitywords,
    arbitrary_three_sheet_cover_excluded=True,
    reason='Each base walk has a unique lift from a chosen lifted root. Backtracking in a cover cancels and preserves the endpoint. A base target with fewer than3 NB routes of length<=8 can reach fewer than3 points of its lifted fiber, regardless of the edge matchings.',
    scope='Every ordinary unbranched3-sheet graph cover of this fixed actual1344 source. No claim for arbitrary4032-vertex degree4 graphs, branched covers or source rewiring.',
    source_allroot_BFS=0,candidate_BFS_roots=0,voltage_assignments_searched=0,
    CPU_seconds=time.process_time()-start)
(P/'RAW_ROUTE_COUNTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['raw_counts_by_base']}))
