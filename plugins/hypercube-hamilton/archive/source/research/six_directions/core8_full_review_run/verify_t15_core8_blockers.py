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

reports=[];nulls={}
for z in (3,15):
 raw=(R/f'q4_balanced_two_avoided_{z}_1.bin').read_bytes();assert len(raw)==10395*30
 neg=set()
 for i in range(0,len(raw),30):
  if raw[i+16]!=255:continue
  assert raw[i+16:i+30]==bytes([255])*14
  a=raw[i:i+16];neg.add(matching((v,a[v]) for v in range(16) if v<a[v]<16))
 assert len(neg)==(3 if z==3 else 10)
 prod=json.loads((R/f'r3_boundary_blocking_{z}_1.json').read_text());assert prod['bridge']==z and prod['omitted']==1
 assert {(a['c'],a['mode']) for a in prod['reports']}=={(c,t) for c in (5,7,9,11,13) for t in ('internal','occupied') if not(c==13 and t=='internal')}
 for row in prod['reports']:
  c,mode=row['c'],row['mode'];m=(13-c)//2;expected=collections.defaultdict(set)
  for L in neg:
   if mode=='occupied':
    for sub in itertools.combinations(sorted(L),m):
     F=matching(sub);expected[F].add(L-F)
   else:
    for a,b in L:
     for k,q in ((a,b),(b,a)):
      rest=L-{norm(k,q)}
      for sub in itertools.combinations(sorted(rest),m-1):
       J=matching(sub);F=matching(J|{norm(z,k)});Q=matching(rest-J|{norm(z,q)});expected[F].add(Q)
  actual={};null=set();checked=0
  for item in row['items']:
   F=matching(item['matching']);assert len(F)==m and F not in actual
   qs={matching(q) for q in item['bad_outputs']};assert F in expected and qs==expected[F];actual[F]=qs
   ports=set(range(16))-{0,7,1}-{v for e in F for v in e};assert len(ports)==c
   boundary=ports|{z} if mode=='internal' else ports-{z}
   assert (z not in ports) if mode=='internal' else (z in ports)
   for q in qs:matching(q,boundary)
   if item['blocking_pairing'] is None:
    assert c==5 and mode=='occupied';a,b,d,e=sorted(boundary)
    assert qs=={matching(q,boundary) for q in [[(a,b),(d,e)],[(a,d),(b,e)],[(a,e),(b,d)]]};null.add(F)
   else:
    D=matching(item['blocking_pairing'],boundary);assert all(disc(D,q) for q in qs);checked+=1
  assert actual==expected and len(actual)==row['inverse_candidates'] and len(null)==row['unresolved']
  nulls[z,c,mode]=null
  reports.append(dict(bridge=z,c=c,mode=mode,inverse_families=len(actual),explicit_blockers_checked=checked,null_families=len(null)))
common=nulls[3,5,'occupied']&nulls[15,5,'occupied']
J=matching([(2,4),(5,6),(9,11),(10,13)]);assert common=={J}
prod=next(r for r in json.loads((R/'t15_r3_c5_negative_kernels.json').read_text())['reports'] if r['core']==8)
assert {matching(r['matching']) for r in prod['common_bad']}==common
out=dict(status='PASS',reports=reports,c5_common_bad=[sorted(f) for f in common],full_core8_proved=False)
(R/'t15_core8_blockers_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
