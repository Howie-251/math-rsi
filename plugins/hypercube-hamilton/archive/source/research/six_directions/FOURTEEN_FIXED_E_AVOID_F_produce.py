"""Producer: conditional local rank certificate, not independent acceptance."""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;prefix='FOURTEEN_FIXED_E_AVOID_F'
H={0,3,5,6,9,10,12,15,17,18,20,27};U={0,5,6,9,10,12}
K=set(range(32))-H;e=(19,23);f=(8,24);V=sorted(K-set(e)-set(f))
def basis(n):
 if n==2:return [[1,0]]
 ans=[]
 for a in basis(n-2):
  b=a[:];p=a[n-3];b.extend([p,n-3]);b[p]=n-2;b[n-3]=n-1
  ans.extend([b,a+[n-1,n-2]])
 return ans
def conn(a,b):
 seen={0};v=0
 for _ in range(len(a)//2):
  v=b[a[v]]
  if v==0:return len(seen)==len(a)//2
  seen.add(v)
 return False
source=(P/'FOURTEEN_NEW_TYPES_orbit_009_forests.bin').read_bytes()
pairs=(P/'FOURTEEN_NEW_TYPES_orbit_009_pairs.bin').read_bytes()
columns=basis(16);piv={};selected=[];rows=[];reduced=[];nonzero=0
for i in range(len(source)//32):
 p={}
 for k in range(0,20,2):
  a,b=pairs[20*i+k:20*i+k+2];p[a]=b;p[b]=a
 if p[e[0]]==e[1]:continue
 nonzero+=1;a,b=map(p.__getitem__,e);p[a]=b;p[b]=a
 assert p[f[0]]==f[1]
 q=[V.index(p[v]) for v in V]
 row=sum(conn(q,c)<<j for j,c in enumerate(columns));r=row
 while r:
  h=r.bit_length()-1
  if h in piv:r^=piv[h]
  else:
   piv[h]=r;selected.append(i);rows.append(row);reduced.append(q);break
assert len(piv)==128 and nonzero==217
# Producer sanity of actual physical forests and endpoint-pair encodings.
for i in selected:
 block=source[32*i:32*i+32];adj={v:[] for v in range(32)}
 for k in range(0,32,2):
  a,b=block[k:k+2];assert (a^b).bit_count()==1
  adj[a].append(b);adj[b].append(a)
 assert all(len(adj[v])==(0 if v in U else 2 if v in H else 1) for v in range(32))
 seen=set();p={}
 for v in sorted(K):
  if v in seen:continue
  prev=-1;x=v
  while True:
   assert x not in seen;seen.add(x)
   ns=[y for y in adj[x] if y!=prev]
   if not ns:
    assert x in K and x!=v;p[v]=x;p[x]=v;break
   assert len(ns)==1;prev,x=x,ns[0]
 assert seen==set(range(32))-U
 encoded={}
 for k in range(0,20,2):
  a,b=pairs[20*i+k:20*i+k+2];encoded[a]=b;encoded[b]=a
 assert p==encoded and p[e[0]]!=e[1]
 a,b=map(p.__getitem__,e);p[a]=b;p[b]=a
 assert p[f[0]]==f[1]
(P/(prefix+'_forests.bin')).write_bytes(b''.join(source[32*i:32*i+32] for i in selected))
def pairbytes(q):return bytes(x for a,b in enumerate(q) if a<b for x in (V[a],V[b]))
(P/(prefix+'_pairs16.bin')).write_bytes(b''.join(pairbytes(q) for q in reduced))
(P/(prefix+'_columns16.bin')).write_bytes(b''.join(pairbytes(q) for q in columns))
(P/(prefix+'_matrix.bin')).write_bytes(b''.join(r.to_bytes(16,'little') for r in rows))
j=dict(status='PRODUCER_POSITIVE_CONDITIONAL_LOCAL_PENDING_FRESH_REVIEW',
 geometry=dict(minority=[],majority=sorted(H),omitted=sorted(U)),required_edge=e,forbidden_edge=f,
 theorem='For every perfect matching F on K, if e belongs to F and f does not belong to F then a cycle on Q5 minus U containing F and adding only short edges exists.',
 covered=sorted(K),twice_reduced_vertices=V,source_nonzero_rows=nonzero,
 source_rows_selected=selected,rank=128,full_fourteen_hole_proved=False,full_P6_proved=False)
(P/(prefix+'_local.json')).write_text(json.dumps(j,indent=2)+'\n')
print('Producer local certificate:128 forests; N16 rank128; pending independent review')
