import json,itertools
from pathlib import Path
p=Path(__file__).parent
T=json.loads((p/'t15_core4_q4_twelve_table.json').read_text())
V=set(range(16))-set(T['omitted']); C=V-{0,7}
def pairs(v,short=False):
 if not v:yield ();return
 a=min(v)
 for b in sorted(v-{a}):
  if short and (a^b).bit_count()!=1:continue
  for q in pairs(v-{a,b},short):yield ((a,b),)+q
N=[]
for a,b in itertools.combinations([x for x in C if x.bit_count()==1],2):
 for d,e in itertools.combinations([x for x in C if (x^7).bit_count()==1],2):
  if len({a,b,d,e})<4:continue
  for q in pairs(C-{a,b,d,e},True):N.append(((0,a),(0,b),(7,d),(7,e))+q)
def canon(es):return frozenset(tuple(sorted(e)) for e in es)
def valid(m,n):
 if canon(m)&canon(n):return False
 adj={v:[] for v in V}
 for a,b in m+n:adj[a].append(b);adj[b].append(a)
 assert all(len(q)==2 for q in adj.values())
 seen={0}; todo=[0]
 while todo:
  for v in adj[todo.pop()]:
   if v not in seen:seen.add(v);todo.append(v)
 return seen==V
seen=set(); positive=0
for r in T['records']:
 m=tuple(tuple(e) for e in r['matching']);seen.add(canon(m))
 yes=any(valid(m,n) for n in N)
 assert yes==bool(r['cycle'])
 if yes:
  cyc=r['cycle'];assert len(cyc)==len(V) and set(cyc)==V
  E=canon(list(zip(cyc,cyc[1:]+cyc[:1])))
  assert canon(m)<=E
  assert all((a^b).bit_count()==1 for a,b in E-canon(m))
 positive+=yes
assert seen=={canon(m) for m in pairs(C)}
B=list(pairs(set(range(16))-{0,1,2,7})); good=set(canon(r['matching']) for r in T['records'] if r['cycle'])
hist={'positive':0,'negative':0,'closed_component':0}
for f in B:
 mate={a:b for e in f for a,b in (e,e[::-1])}
 if mate[3]==15:hist['closed_component']+=1;continue
 x,y=mate[3],mate[15]
 L=canon(f)-{tuple(sorted((3,x))),tuple(sorted((15,y)))}|{tuple(sorted((x,y)))}
 hist['positive' if L in good else 'negative']+=1
out={'table_records':len(T['records']),'positive':positive,'negative':len(T['records'])-positive,'short_degree_patterns':len(N),'B_full_matchings':len(B),'zero_crossing_two_bridge_histogram':hist}
(p/'t15_core4_q4_twelve_verification.json').write_text(json.dumps(out,indent=2));print(out)
