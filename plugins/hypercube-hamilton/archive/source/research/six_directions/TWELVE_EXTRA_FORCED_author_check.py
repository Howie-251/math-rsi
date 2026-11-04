"""Producer recomputation of all15 new reduced rank1024 local certificates."""
from pathlib import Path
from itertools import permutations
import json
P=Path(__file__).resolve().parent;N=1024
rows=json.loads((P/'TWELVE_EXTRA_FORCED_summary.json').read_text())['reports'];assert len(rows)==15
old={5:[1,2,4,7,11,28,31],6:[1,2,4,11,13,22,31],9:[1,2,4,7,11,21,31],11:[1,2,4,11,19,25,26],12:[1,2,4,7,11,13,31],13:[1,2,4,11,13,14,31],17:[1,2,4,7,11,13,14]}
maps=[tuple(sum(((x>>q[i])&1)<<i for i in range(5)) for x in range(32)) for q in permutations(range(5))]
def canonical(J,U):return min((tuple(sorted(t[x] for x in J)),tuple(sorted(t[x] for x in U))) for t in maps)
oldkeys={canonical(J,[1,2,4]):i for i,J in old.items()};reports=[]
for row in rows:
 pre=row['prefix'];g=row['geometry'];H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H;p,q=row['forced_pair'];h=row['forced_hole'];Kprime=sorted(K-{p,q});idx={x:i for i,x in enumerate(Kprime)}
 assert len(K)==24 and len(Kprime)==22 and h==0 and set(h^(1<<d) for d in range(5))-U=={p,q}
 forced=[x for x in H-U if len(set(x^(1<<d) for d in range(5))-U)==2];assert forced==[h]
 forests=(P/(pre+'_forests.bin')).read_bytes();full=(P/(pre+'_full_pairs.bin')).read_bytes();pairs=(P/(pre+'_pairs.bin')).read_bytes();columns=(P/(pre+'_columns.bin')).read_bytes()
 assert len(forests)==N*34 and len(full)==N*24 and len(pairs)==len(columns)==N*22
 for i in range(N):
  rec=forests[i*34:i*34+34];edges=[tuple(rec[j:j+2]) for j in range(0,34,2)];assert len(set(edges))==17 and edges==sorted(edges)
  adj=[[] for _ in range(32)]
  for a,b in edges:assert a<b and (a^b).bit_count()==1;adj[a].append(b);adj[b].append(a)
  assert all(len(adj[x])==(0 if x in U else 1 if x in K else 2) for x in range(32))
  assert set(adj[h])=={p,q} and adj[p]==[h] and adj[q]==[h]
  seen=set();ep=[]
  for a in sorted(K):
   if a in seen:continue
   seen.add(a);previous=a;x=adj[a][0]
   while x not in K:
    assert x not in seen;seen.add(x);nxt=next(y for y in adj[x] if y!=previous);previous,x=x,nxt
   assert x not in seen;seen.add(x);ep.append(tuple(sorted((a,x))))
  assert seen==set(range(32))-U
  ep.sort();assert bytes(x for e in ep for x in e)==full[i*24:i*24+24]
  assert (min(p,q),max(p,q)) in ep
  assert bytes(x for e in ep if set(e)!={p,q} for x in e)==pairs[i*22:i*22+22]
 def mates(raw):
  result=[]
  for i in range(N):
   rec=raw[i*22:i*22+22];assert set(rec)==set(Kprime) and len(set(rec))==22;m=[255]*22
   for j in range(0,22,2):a,b=rec[j:j+2];m[idx[a]]=idx[b];m[idx[b]]=idx[a]
   assert all(m[m[x]]==x and m[x]!=x for x in range(22));result.append(m)
  return result
 pp=mates(pairs);cc=mates(columns)
 def ints(suffix):
  raw=(P/(pre+suffix+'.bin')).read_bytes();assert len(raw)==N*128;return [int.from_bytes(raw[i*128:i*128+128],'little') for i in range(N)]
 matrix=ints('_matrix');pivots=ints('_pivots');combos=ints('_combos')
 for i,a in enumerate(pp):
  bits=0
  for j,b in enumerate(cc):
   x=0
   for k in range(1,12):
    x=b[a[x]]
    if x==0:
     if k==11:bits|=1<<j
     break
   else:raise AssertionError('invalid alternating involutions')
  assert bits==matrix[i]
 for i in range(N):
  assert pivots[i].bit_length()==i+1;actual=0;todo=combos[i]
  while todo:
   bit=todo&-todo;actual^=matrix[bit.bit_length()-1];todo^=bit
  assert actual==pivots[i]
 oldid=oldkeys.get(canonical(g['majority'],g['omitted']));assert oldid is None
 reports.append({'index':row['index'],'rank':1024,'unique_forced_hole':h,'pair':[p,q],'old_accepted_seven_orbit_id':oldid})
 print('checked',row['index'],flush=True)
out={'status':'PASS_PRODUCER_NOT_FRESH_REVIEW','new_conditional_local_cases':15,'forests_checked':15360,'connectivity_bits_recomputed':15728640,'rank_GF2_each':1024,'covered_endpoints':24,'reduced_endpoints':22,'none_in_old_accepted_seven':True,'reports':reports,'full_T17_proved':False,'full_twelve_hole_proved':False,'full_P6_proved':False}
(P/'TWELVE_EXTRA_FORCED_author_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='reports'}))
