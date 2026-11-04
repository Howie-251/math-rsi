"""Independent read-only certificate audit for the new c2 same-face kernel.
Imports the audited completeness of the opposite-hole Q4 table.
No producer module or DFS is imported.
"""
from pathlib import Path
from itertools import permutations,combinations
import json,hashlib
R=Path(__file__).resolve().parent
V=set(range(16));D3=(7,11,13,14)
def edge(a,b):return tuple(sorted((a,b)))
def canon(es):return frozenset(edge(a,b) for a,b in es)
def mapping(es):return {a:b for a,b in es}|{b:a for a,b in es}
def rec(xs):
 xs=sorted(xs)
 if not xs:yield frozenset();return
 a=xs[0]
 for b in xs[1:]:
  for t in rec(set(xs)-{a,b}):yield t|{edge(a,b)}
def contraction(f,z,u,v):
 es=list(f)+[(0,u),(z,v)];adj={x:[] for x in V}
 for k,(a,b) in enumerate(es):adj[a].append((b,k));adj[b].append((a,k))
 assert all(len(adj[x])==(2 if x in {0,z} else 1) for x in V)
 used=set();out=set()
 for a in V-{0,z}:
  if adj[a][0][1] in used:continue
  x=a;last=-1
  while True:
   b,k=next((b,k) for b,k in adj[x] if k!=last)
   assert k not in used;used.add(k);x=b;last=k
   if x not in {0,z}:break
  out.add(edge(a,x))
 assert len(used)==len(es) and len(out)==7
 return frozenset(out)
def main():
 raw=(R/'t15_sameface_positive_c2_certificates.json').read_bytes();obj=json.loads(raw)
 data=(R/'q4_distance3_avoided_table.bin').read_bytes()
 assert hashlib.sha256(data).hexdigest()==obj['imports']['q4_distance3_avoided_table.bin']
 base=[]
 for i in range(0,len(data),30):
  row=data[i:i+30]
  if row[16]==255:base.append(frozenset(edge(a,row[a]) for a in V if a<row[a]<16))
 assert len(base)==53
 def trans(x,p):return sum(((x>>i)&1)<<p[i] for i in range(4))
 neg={}
 for z in D3:
  p=next(p for p in permutations(range(4)) if trans(7,p)==z)
  neg[z]={frozenset(edge(trans(a,p),trans(b,p)) for a,b in t) for t in base}
 remaining={}
 for v,w,p,q in ((1,2,4,8),(2,4,1,8)):
  remaining[(v,w)]=set(rec(V-{0,7,11,13,v,w,p,q}));assert len(remaining[(v,w)])==105
 paths=0
 for r in obj['A_certificates']:
  av=tuple(r['avoid']);p,q=r['artificial_pair'];fa=canon(r['F_A'])
  assert fa in remaining[av];remaining[av].remove(fa)
  assert {p,q}=={1,2,4,8}-set(av)
  seen=set()
  for w in r['witnesses']:
   path=w['path'];z=w['z'];first=w['root_side_port'];full=fa|{edge(p,q)}
   assert len(path)==len(set(path))==14 and set(path)==V-set(av)
   assert path[0]==0 and path[-1]==z and z in D3
   assert first in {p,q} and path.index(first)<path.index(q if first==p else p)
   es=canon(zip(path,path[1:]));assert full<=es
   assert all((a^b).bit_count()==1 for a,b in es-full)
   assert (z,first) not in seen;seen.add((z,first));paths+=1
  assert seen=={(z,t) for z in D3 for t in (p,q)}
 assert all(not x for x in remaining.values())
 expected={}
 for y in combinations(range(16),2):
  z=next(z for z in D3 if z not in y);u,v=y
  if u==0:u,v=v,u
  fs=set()
  for t in neg[z]:
   m=mapping(t)
   if v==0:
    b=m[u];f=t-{edge(u,b)}|{edge(z,b)}
   elif m[u]==v:f=t-{edge(u,v)}|{edge(0,z)}
   else:
    a,b=m[u],m[v];f=t-{edge(u,a),edge(v,b)}|{edge(0,a),edge(z,b)}
   assert contraction(f,z,u,v)==t;fs.add(f)
  assert len(fs)==53;expected[y]=fs
 checked=0
 for r in obj['B_exception_certificates']:
  y=tuple(r['ports']);f=canon(r['F_B']);assert f in expected[y];expected[y].remove(f)
  z=r['z'];u=r['root_side_B_port'];v=r['other_B_port'];assert {u,v}==set(y)
  t=contraction(f,z,u,v);c=r['compressed_cycle'];assert t not in neg[z]
  assert len(c)==len(set(c))==14 and set(c)==V-{0,z}
  es=canon((c[k],c[(k+1)%14]) for k in range(14));assert t<=es
  assert all((a^b).bit_count()==1 for a,b in es-t);checked+=1
 assert all(not x for x in expected.values()) and checked==6360 and paths==1680
 result={'status':'PASS','A_matching_inputs':210,'A_positive_paths':paths,'B_negative_inverse_candidates':checked,'independence':'No generator/checker module imported; audited Q4 table completeness remains an explicit import.','certificate_sha256':hashlib.sha256(raw).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (R/'t15_sameface_positive_c2_independent_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
