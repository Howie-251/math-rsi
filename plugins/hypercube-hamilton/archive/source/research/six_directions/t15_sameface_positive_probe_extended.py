from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
R=Path('research/six_directions');V=set(range(16));D3=(7,11,13,14)
def e(a,b):return tuple(sorted((a,b)))
def tr(x,p):return sum(((x>>i)&1)<<p[i] for i in range(4))
d=(R/'q4_distance3_avoided_table.bin').read_bytes();ns=[frozenset(e(x,row[x]) for x in range(16) if x<row[x]<16) for i in range(0,len(d),30) if (row:=d[i:i+30])[16]==255]
neg={z:{frozenset(e(tr(a,p),tr(b,p)) for a,b in t) for t in ns} for z in D3 for p in [next(p for p in permutations(range(4)) if tr(7,p)==z)]}
def compress(f,z,u,v):
 es=list(f)+[(0,u),(z,v)];adj={x:[] for x in V}
 for i,(a,b) in enumerate(es):adj[a].append((b,i));adj[b].append((a,i))
 if any(len(adj[x])!=(2 if x in (0,z) else 1) for x in V):return None
 used=set();out=set()
 for x in V-{0,z}:
  if adj[x][0][1] in used:continue
  a=x;prev=-1
  while True:
   choices=[(b,k) for b,k in adj[a] if k!=prev]
   if len(choices)!=1:return None
   b,k=choices[0]
   if k in used:return None
   used.add(k);a=b;prev=k
   if a not in (0,z):break
  out.add(e(x,a))
 if len(used)!=len(es):return None
 return frozenset(out)
counts=Counter();stalled=[]
for y in combinations(range(16),2):
 z=next(z for z in D3 if z not in y);u,v=y
 if u==0:u,v=v,u
 candidates=set()
 for t in neg[z]:
  m={a:b for a,b in t}|{b:a for a,b in t}
  if v==0:
   b=m[u];f=t-{e(u,b)}|{e(z,b)}
  elif m[u]==v:f=t-{e(u,v)}|{e(0,z)}
  else:
   a,b=m[u],m[v];f=t-{e(u,a),e(v,b)}|{e(0,a),e(z,b)}
  assert sorted(x for a in f for x in a)==sorted(V-set(y))
  assert compress(f,z,u,v)==t
  candidates.add(f)
 counts['initial_candidates']+=len(candidates)
 for f in candidates:
  good=[]
  for zz in D3:
   for uu,vv in (y,y[::-1]):
    tt=compress(f,zz,uu,vv)
    if tt is not None and tt not in neg[zz]:good.append((zz,uu,vv))
  if not good:stalled.append((y,sorted(f)))
print(counts,'stalled',len(stalled));print(stalled[:5])
patterns=[tuple((z,o) for z in D3 for o in (0,1)),((7,0),(7,1),(11,0),(11,1),(13,0),(13,1),(14,0)),((7,0),(7,1),(11,0),(11,1),(13,0),(13,1),(14,1)),((7,1),(11,0),(11,1),(13,0),(13,1),(14,0))]
patterns=set(patterns)|{tuple(sorted((z,1-o) for z,o in pat)) for pat in patterns}
for pat in sorted(patterns):
 stalled=[];total=0
 for y in combinations(range(16),2):
  zz,o=next((zz,o) for zz,o in pat if zz not in y and y[o]!=0)
  u,v=y[o],y[1-o];candidates=set()
  for t in neg[zz]:
   m={a:b for a,b in t}|{b:a for a,b in t}
   if v==0:
    b=m[u];f=t-{e(u,b)}|{e(zz,b)}
   elif m[u]==v:f=t-{e(u,v)}|{e(0,zz)}
   else:
    a,b=m[u],m[v];f=t-{e(u,a),e(v,b)}|{e(0,a),e(zz,b)}
   assert compress(f,zz,u,v)==t;candidates.add(f)
  total+=len(candidates)
  for f in candidates:
   if not any((tt:=compress(f,zz,y[o],y[1-o])) is not None and tt not in neg[zz] for zz,o in pat):stalled.append((y,sorted(f)))
 print('PAT',pat,'candidates',total,'stalled',len(stalled),stalled[:1])
