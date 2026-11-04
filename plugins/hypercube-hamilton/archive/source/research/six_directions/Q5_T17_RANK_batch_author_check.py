"""Producer direct verification of every full/reduced batch matrix and forest."""
from pathlib import Path
import json,time
R=Path(__file__).resolve().parent
def verify(prefix,reduced):
 cfg=list(map(int,(R/(prefix+'_config.txt')).read_text().split()));H=set(cfg[:8]);U=set(cfg[8:11]);K=set(range(32))-H
 forced=set(cfg[11:13]) if reduced else set();KR=sorted(K-forced);ix={x:i for i,x in enumerate(KR)}
 n=1<<(len(KR)//2-1);rb=n//8
 forests=(R/(prefix+'_forests.bin')).read_bytes();full=(R/(prefix+('_full_pairs' if reduced else '_pairs')+'.bin')).read_bytes();pairs=(R/(prefix+'_pairs.bin')).read_bytes()
 assert len(forests)==n*34 and len(full)==n*24 and len(pairs)==n*len(KR)
 for i in range(n):
  rec=forests[34*i:34*i+34];es=[tuple(rec[j:j+2]) for j in range(0,34,2)];assert es==sorted(set(es))
  adj={x:[] for x in range(32)}
  for a,b in es:assert a<b and (a^b).bit_count()==1;adj[a].append(b);adj[b].append(a)
  assert all(len(adj[x])==(0 if x in U else 1 if x in K else 2) for x in adj)
  seen=set();pp=[]
  for start in sorted(K):
   if start in seen:continue
   old=-1;x=start
   while True:
    assert x not in seen;seen.add(x);nxt=[y for y in adj[x] if y!=old]
    if not nxt:break
    assert len(nxt)==1;old,x=x,nxt[0]
   assert x in K and x!=start;pp.append(tuple(sorted((start,x))))
  assert seen==set(range(32))-U and len(pp)==12
  assert bytes(x for e in sorted(pp) for x in e)==full[24*i:24*i+24]
  if reduced:assert tuple(sorted(forced)) in pp;pp.remove(tuple(sorted(forced)))
  assert bytes(x for e in sorted(pp) for x in e)==pairs[len(KR)*i:len(KR)*(i+1)]
 def matchings(suffix):
  raw=(R/(prefix+suffix+'.bin')).read_bytes();assert len(raw)==n*len(KR);out=[]
  for i in range(n):
   rec=raw[len(KR)*i:len(KR)*(i+1)];assert len(set(rec))==len(KR) and set(rec)==set(KR)
   m=[-1]*len(KR)
   for j in range(0,len(KR),2):a,b=rec[j:j+2];assert a!=b;m[ix[a]]=ix[b];m[ix[b]]=ix[a]
   out.append(m)
  return out
 ps=matchings('_pairs');cs=matchings('_columns')
 def ints(suffix):
  raw=(R/(prefix+suffix+'.bin')).read_bytes();assert len(raw)==n*rb
  return [int.from_bytes(raw[rb*i:rb*(i+1)],'little') for i in range(n)]
 mat=ints('_matrix');pivots=ints('_pivots');combos=ints('_combos')
 half=len(KR)//2
 for i,p in enumerate(ps):
  value=0
  for j,c in enumerate(cs):
   x=0
   for k in range(1,half+1):
    x=c[p[x]]
    if x==0:
     if k==half:value|=1<<j
     break
   else:raise AssertionError('bad matching')
  assert value==mat[i]
 for i in range(n):
  assert pivots[i].bit_length()==i+1
  value=0;bits=combos[i]
  while bits:
   bit=bits&-bits;value^=mat[bit.bit_length()-1];bits^=bit
  assert value==pivots[i]
 return {'prefix':prefix,'reduced':reduced,'status':'PASS_PRODUCER','selected_forests':n,'full_endpoint_count':24,'matrix_endpoint_count':len(KR),'matrix_bits_recomputed':n*n,'rank_GF2':n}
allrows=[]
for file,reduced in [('Q5_T17_RANK_batch_summary.json',False),('Q5_T17_RANK_forced_summary.json',True)]:
 for row in json.loads((R/file).read_text())['orbits']:
  a=verify(row['prefix'],reduced);allrows.append(a);print(a['prefix'],a['rank_GF2'],'PASS',flush=True)
(R/'Q5_T17_RANK_batch_author_verified.json').write_text(json.dumps({'status':'ALL_17_BATCH_PRODUCER_CHECKS_PASS','rows':allrows,'fresh_independent_acceptance':False},indent=2)+'\n')
