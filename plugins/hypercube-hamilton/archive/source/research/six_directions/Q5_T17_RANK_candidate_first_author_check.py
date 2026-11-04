"""Producer verification of first full-rank T17 witness and every matrix bit."""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;pre='Q5_T17_RANK_candidate_first';N=2048
H={0,1,2,7,11,13,21,31};U={1,2,13};K=sorted(set(range(32))-H);index={x:i for i,x in enumerate(K)}
f=(P/(pre+'_forests.bin')).read_bytes();pairs=(P/(pre+'_pairs.bin')).read_bytes()
assert len(f)==N*34 and len(pairs)==N*24
for i in range(N):
 edges=[tuple(f[i*34+j:i*34+j+2]) for j in range(0,34,2)];assert len(set(edges))==17 and edges==sorted(edges)
 adj={x:[] for x in range(32)}
 for a,b in edges:assert a<b and (a^b).bit_count()==1;adj[a].append(b);adj[b].append(a)
 assert all(len(adj[x])==(0 if x in U else 1 if x in K else 2) for x in range(32))
 visited=set();ends=[]
 for a in K:
  if a in visited:continue
  visited.add(a);previous=a;x=adj[a][0]
  while x not in K:
   assert x not in visited;visited.add(x);y=next(y for y in adj[x] if y!=previous);previous,x=x,y
  assert x not in visited;visited.add(x);ends.append(tuple(sorted((a,x))))
 assert visited==set(range(32))-U
 assert bytes(x for e in sorted(ends) for x in e)==pairs[i*24:i*24+24]
def matching_records(suffix):
 raw=(P/(pre+suffix+'.bin')).read_bytes();assert len(raw)==N*24;out=[]
 for i in range(N):
  rec=raw[i*24:i*24+24];assert set(rec)==set(K) and len(set(rec))==24
  m=[255]*24
  for j in range(0,24,2):a,b=rec[j:j+2];assert a!=b;m[index[a]]=index[b];m[index[b]]=index[a]
  out.append(m)
 return out
ps=matching_records('_pairs');cs=matching_records('_columns')
def integers(suffix):
 raw=(P/(pre+suffix+'.bin')).read_bytes();assert len(raw)==N*256
 return [int.from_bytes(raw[i*256:i*256+256],'little') for i in range(N)]
matrix=integers('_matrix');pivots=integers('_pivots');combos=integers('_combos')
for i,p in enumerate(ps):
 row=0
 for j,c in enumerate(cs):
  x=0
  for k in range(1,13):
   x=c[p[x]]
   if x==0:
    if k==12:row|=1<<j
    break
  else:raise AssertionError('invalid alternating walk')
 assert row==matrix[i]
for i in range(N):
 assert pivots[i].bit_length()==i+1
 actual=0;bits=combos[i]
 while bits:
  low=bits&-bits;actual^=matrix[low.bit_length()-1];bits^=low
 assert actual==pivots[i]
out={'status':'PASS_PRODUCER_NOT_FRESH_REVIEW','selected_forests':2048,'matrix_bits_recomputed':4194304,
 'all_short_degrees_acyclic_paths_verified':True,'all_endpoint_pairs_verified':True,'rank_GF2_lower_bound':2048,
 'required_external_rank_upper_bound':2048,'full_T17_proved':False,'full_P6_proved':False}
(P/(pre+'_author_check.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
