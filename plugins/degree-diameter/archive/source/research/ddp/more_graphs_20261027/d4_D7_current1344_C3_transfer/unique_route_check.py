"""One targeted <=4+<=4 word check of the saved unique-route witness, no BFS."""
from pathlib import Path
from collections import defaultdict
import json,time
P=Path(__file__).parent;start=time.process_time()
src=json.loads((P/'SOURCE.json').read_text());group=[tuple(x) for x in json.loads((P/'group_permutation_images0based.json').read_text())];index={g:i for i,g in enumerate(group)}
W=[tuple(x-1 for x in row) for row in src['W_images_1based']]
def inverse(g):
 r=[0]*32
 for i,j in enumerate(g):r[j]=i
 return tuple(r)
volts={i+1:g for i,g in enumerate(W)};volts[-5]=inverse(W[4]);volts[-6]=inverse(W[5])
def invert_label(x):return x if 1<=x<=4 else -x
ports={0:[(0,1),(0,2),(1,5),(1,6)],1:[(1,3),(1,4),(0,-5),(0,-6)]}
def neighbor(state,label,targetbase):
 b,g=state;h=tuple(volts[label][j] for j in group[g]) # GAP right action, (i^g)^W
 return targetbase,index[h]
def levels(startstate):
 rows=[[(startstate,())]]
 for _ in range(4):
  nxt=[]
  for state,word in rows[-1]:
   for targetbase,label in ports[state[0]]:
    if word and label==invert_label(word[-1]):continue
    nxt.append((neighbor(state,label,targetbase),word+(label,)))
  rows.append(nxt)
 return rows
root=(0,0);target=(0,200);L=levels(root);R=levels(target)
found=[]
for length in range(9):
 a=length//2;b=length-a;right=defaultdict(list)
 for state,word in R[b]:right[state].append(word)
 for state,prefix in L[a]:
  for rw in right[state]:
   suffix=tuple(invert_label(x) for x in reversed(rw))
   if prefix and suffix and suffix[0]==invert_label(prefix[-1]):continue
   found.append(prefix+suffix)
found=sorted(set(found),key=lambda w:(len(w),w))
assert found==[(6,4,-6)],found
state=root;path=[state]
for label in found[0]:
 matches=[tb for tb,l in ports[state[0]] if l==label];assert len(matches)==1
 state=neighbor(state,label,matches[0]);path.append(state)
assert state==target
raw=json.loads((P/'RAW_ROUTE_COUNTS.json').read_text());assert raw['raw_counts_by_base'][0][200]==1
result={'status':'TARGETED_UNIQUE_NB_ROUTE_CONFIRMED','source_root':list(root),'target':list(target),'max_length':8,'complete_NB_words_at_most8':[list(w) for w in found],'base_group_path':[list(s) for s in path],'target_group_permutation_images0based':list(group[200]),'method':'For each length0..8, join nonbacktracking prefix lengthfloor(L/2) with reversed target-prefix lengthceil(L/2), rejecting inverse boundary. This includes each reduced word once.','partial_words_per_side_by_length':[len(row) for row in L],'full_graph_generated':False,'BFS':0,'group_enumeration':False,'voltage_search':False,'CPU_seconds':time.process_time()-start,'scope':'One min1 witness of the correctly bound fixed source, not another candidate experiment.'}
(P/'UNIQUE_ROUTE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='target_group_permutation_images0based'}))
