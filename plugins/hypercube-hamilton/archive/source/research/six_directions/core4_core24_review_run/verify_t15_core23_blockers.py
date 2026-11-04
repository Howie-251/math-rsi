"""Independent completeness and graph-connectivity checker for core23 inverse blockers."""
import json,itertools,collections
from pathlib import Path
R=Path(__file__).resolve().parent
norm=lambda a,b:tuple(sorted((a,b)))
def matching(edges,vertices=None):
 f=frozenset(norm(a,b) for a,b in edges);vs=[v for e in f for v in e]
 assert len(vs)==len(set(vs)) and all(a!=b for a,b in f)
 if vertices is not None:assert set(vs)==set(vertices)
 return f
def disc(D,Q):
 vs={a for e in Q for a in e};matching(D,vs);matching(Q,vs)
 adj={a:set() for a in vs}
 for a,b in D|Q:adj[a].add(b);adj[b].add(a)
 reached=set();todo=[min(vs)]
 while todo:
  a=todo.pop()
  if a in reached:continue
  reached.add(a);todo.extend(adj[a]-reached)
 return reached!=vs
raw=(R/'q4_balanced_two_avoided_3_8.bin').read_bytes();assert len(raw)==10395*30
neg=set()
for i in range(0,len(raw),30):
 if raw[i+16]!=255:continue
 assert raw[i+16:i+30]==bytes([255])*14
 m=raw[i:i+16];neg.add(matching((a,m[a]) for a in range(16) if a<m[a]<16))
assert len(neg)==10
producer=json.loads((R/'r3_boundary_blocking_3_8.json').read_text());assert producer['bridge']==3 and producer['omitted']==8
assert {(r['c'],r['mode']) for r in producer['reports']}=={(c,mode) for c in (5,7,9,11,13) for mode in ('internal','occupied') if not(c==13 and mode=='internal')}
summaries=[];nulls={};checked=0
for report in producer['reports']:
 c,mode=report['c'],report['mode'];m=(13-c)//2;expected=collections.defaultdict(set)
 for L in neg:
  if mode=='occupied':
   for subset in itertools.combinations(sorted(L),m):
    F=matching(subset);expected[F].add(L-F)
  else:
   lm={a:b for e in L for a,b in (e,e[::-1])}
   for k in sorted(lm):
    q=lm[k];rest=L-{norm(k,q)}
    for subset in itertools.combinations(sorted(rest),m-1):
     J=matching(subset);F=matching(J|{norm(3,k)});Q=matching(rest-J|{norm(3,q)})
     expected[F].add(Q)
 actual={};null=set()
 for item in report['items']:
  F=matching(item['matching']);assert F not in actual
  assert len(F)==m
  outputs={matching(q) for q in item['bad_outputs']};assert len(outputs)==len(item['bad_outputs'])
  assert F in expected and outputs==expected[F];actual[F]=outputs
  ports=set(range(16))-{0,7,8}-{v for e in F for v in e}
  assert len(ports)==c
  boundary=ports|{3} if mode=='internal' else ports-{3}
  assert (3 not in ports) if mode=='internal' else (3 in ports)
  for Q in outputs:matching(Q,boundary)
  if item['blocking_pairing'] is None:
   null.add(F)
   assert c==5 and mode=='occupied' and len(outputs)==3
   vs=sorted(boundary);a,b,d,e=vs
   allQ={matching(q,vs) for q in [[(a,b),(d,e)],[(a,d),(b,e)],[(a,e),(b,d)]]}
   assert outputs==allQ
  else:
   D=matching(item['blocking_pairing'],boundary)
   assert all(disc(D,Q) for Q in outputs)
   checked+=1
 assert actual==expected and len(actual)==report['inverse_candidates'] and len(null)==report['unresolved']
 nulls[c,mode]=null;summaries.append(dict(c=c,mode=mode,inverse_families=len(expected),blockers_checked=len(expected)-len(null),unblocked=len(null)))
assert len(nulls[5,'occupied'])==2
# Swap local coordinates 1 and 2, preserving holes 0,7,8 and omitted A hole9.
def swap(v):return (v&9)|((v&2)<<1)|((v&4)>>1)
other={matching((swap(a),swap(b)) for a,b in F) for F in nulls[5,'occupied']}
assert not (other & nulls[5,'occupied'])
prod23=next(t for t in json.loads((R/'t15_r3_c5_negative_kernels.json').read_text())['reports'] if t['core']==23)
assert prod23['common_bad']==[]
for table,z in zip(prod23['tables'],(3,5)):
 actualbad={matching(row['matching']) for row in table['at_least_two_bad_quotients']}
 assert actualbad==(nulls[5,'occupied'] if z==3 else other)
out=dict(status='PASS',scope='Every inverse family complete and every saved blocker independently checked by graph traversal; only occupied c5 has two null families per bridge with empty intersection',bridge=3,B_omitted=8,negative_inputs=10,reports=summaries,total_explicit_blockers_checked=checked,c5_bridge3_null_F=[sorted(f) for f in sorted(nulls[5,'occupied'],key=lambda f:sorted(f))],c5_bridge5_null_F=[sorted(f) for f in sorted(other,key=lambda f:sorted(f))],c5_common_null_count=0,full_T15_proved=False)
(R/'t15_core23_blockers_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
