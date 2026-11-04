"""Producer local certificate and actual118 sufficient application. Not review."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter
import json,hashlib
P=Path(__file__).resolve().parent;prefix='SIXTEEN_SMALLCUT'
source='Q5_T37_INDEPENDENT_orbit_00'
g=json.loads((P/'Q5_T37_INDEPENDENT_summary.json').read_text())['reports'][0]['geometry']
H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H
e=(30,31);R=(13,21);V=sorted(K-set(e)-set(R))
def basis(n):
 if n==2:return [[1,0]]
 out=[]
 for a in basis(n-2):
  b=a[:];p=a[n-3];b.extend([p,n-3]);b[p]=n-2;b[n-3]=n-1
  out.extend([b,a+[n-1,n-2]])
 return out
def conn(a,b):
 x=0
 for j in range(1,len(a)//2+1):
  x=b[a[x]]
  if x==0:return j==len(a)//2
 raise ValueError('pairing')
def encode(q):return bytes(x for a,b in enumerate(q) if a<b for x in (V[a],V[b]))
lines=[list(map(int,l.split())) for l in (P/(prefix+'_avoidpair.tsv')).read_text().splitlines()]
entry=next(r for r in lines if r[:5]==[0,13,21,256,256]);selected=entry[5:];assert len(selected)==256
raw=(P/(source+'_forests.bin')).read_bytes();pairs=(P/(source+'_pairs.bin')).read_bytes()
forests=[];qs=[];matrix=[];columns=basis(18);piv={}
for i in selected:
 block=raw[38*i:38*i+38];assert len(block)==38;adj=[[] for v in range(32)]
 for k in range(0,38,2):
  a,b=block[k:k+2];assert (a^b).bit_count()==1;adj[a].append(b);adj[b].append(a)
 assert all(len(adj[v])==(0 if v in U else 2 if v in H else 1) for v in range(32))
 seen=set();p={}
 for v in sorted(K):
  if v in seen:continue
  x=v;prev=-1
  while True:
   assert x not in seen;seen.add(x);ns=[y for y in adj[x] if y!=prev]
   if not ns:assert x in K and x!=v;p[v]=x;p[x]=v;break
   assert len(ns)==1;prev,x=x,ns[0]
 assert seen==set(range(32))-U
 pp={}
 for k in range(0,22,2):a,b=pairs[22*i+k:22*i+k+2];pp[a]=b;pp[b]=a
 assert p==pp and p[e[0]]!=e[1]
 a,b=map(p.__getitem__,e);p[a]=b;p[b]=a
 assert p[R[0]]==R[1]
 q=[V.index(p[v]) for v in V];row=sum(conn(q,c)<<j for j,c in enumerate(columns));r=row
 while r:
  h=r.bit_length()-1
  if h in piv:r^=piv[h]
  else:piv[h]=r;break
 assert r
 forests.append(block);qs.append(q);matrix.append(row)
assert len(piv)==256
(P/(prefix+'_forests.bin')).write_bytes(b''.join(forests))
(P/(prefix+'_pairs18.bin')).write_bytes(b''.join(encode(q) for q in qs))
(P/(prefix+'_columns18.bin')).write_bytes(b''.join(encode(q) for q in columns))
(P/(prefix+'_matrix.bin')).write_bytes(b''.join(r.to_bytes(32,'little') for r in matrix))
local=dict(status='PRODUCER_CONDITIONAL_LOCAL_PENDING_FRESH_REVIEW',geometry=g,
 required_edge=e,forbidden_pair=R,covered=sorted(K),twice_reduced_vertices=V,
 source_prefix=source,source_rows=selected,rows=256,rank_GF2=256,
 theorem='For every arbitrary perfect matching F on K, e in F and R not in F imply a short-added cycle on Q5 minus U.')
(P/(prefix+'_local.json')).write_text(json.dumps(local,indent=2)+'\n')
maps=[tuple(sum(((v>>p[k])&1)<<k for k in range(5)) for v in range(32)) for p in permutations(range(5))]
mask=lambda s:sum(1<<v for v in s)
lookup={}
for ca in g['minority']:
 for pi,tr in enumerate(maps):
  key=tuple(mask(tr[x^ca] for x in g[z]) for z in ('minority','majority','omitted'))
  lookup.setdefault(key,[]).append((ca,pi))
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
def peel(alive):
 alive=set(alive);out=[]
 while True:
  edge=next(((x,ns[0]) for x in sorted(alive) if len(ns:=[x^(1<<d) for d in range(6) if x^(1<<d) in alive])==1),None)
  if edge is None:return out
  out.append(edge);alive-=set(edge)
witnesses=[];reports=[]
for v in (1,7,31):
 raw=(P/f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin').read_bytes();positive=[];remaining=[]
 for idx,off in enumerate(range(0,len(raw),15)):
  rec=tuple(raw[off:off+15]);Z=set(rec[:7]);W=set(rec[7:]);alive=set(range(64))-{0}-Z-W;chain=peel(alive);forced={tuple(sorted(x)) for x in chain};found=None
  for d in range(6):
   if not v>>d&1:continue
   A=lambda x:x>>d&1;za={x for x in Z if A(x)};wa={x for x in W if A(x)}
   if (len(za),len(wa))!=(4,3):continue
   minor={x for x in Z if not A(x)};major={x for x in W if not A(x)}
   for S in combinations(sorted(za),2):
    Y={x^(1<<d) for x in S};M={project(x,d) for x in minor};J={project(x,d) for x in major|Y};UU={project(x,d) for x in Y};aa=min(M)
    key=tuple(mask(x^aa for x in xs) for xs in (M,J,UU))
    for ca,pi in lookup.get(key,[]):
     tr=maps[pi]
     def glob(x):
      q=tr[x^ca]^aa
      return (q&((1<<d)-1))|((q>>d)<<(d+1))
     ee=tuple(sorted(map(glob,e)));rr=tuple(sorted(map(glob,R)))
     if ee not in forced or set(ee)&Y:continue
     assert 0 not in rr and not set(rr)&Y
     assert len({x.bit_count()%2 for x in Y|set(rr)})==1
     if found is None:found=dict(v=v,input_index=idx,record=rec,cut=d,sources=S,canonical_anchor=ca,
      permutation_index=pi,actual_anchor=aa,actual_required_edge=ee,actual_forbidden_pair=rr,leaf_chain=chain)
  if found:witnesses.append(found);positive.append(rec)
  else:remaining.append(rec)
 for label,rr in [('positive',positive),('remaining',remaining)]:
  (P/f'{prefix}_{label}_v{v}_covered.bin').write_bytes(b''.join(map(bytes,rr)))
 reports.append(dict(v=v,input=len(raw)//15,positive=len(positive),remaining=len(remaining)))
assert [r['positive'] for r in reports]==[0,18,100]
assert [r['remaining'] for r in reports]==[0,0,30]
out=dict(status='PRODUCER_LOCAL_AND_ACTUAL118_PENDING_FRESH_INDEPENDENT_REVIEW',
 reports=reports,witnesses=witnesses,new_positive=118,remaining_covered_target_geometries=30,
 remaining_free_target_geometries=0,source_conditional_on_complete_fourteen_holes=True,
 full_fourteen_hole_proved=False,full_sixteen_hole_proved=False,full_P6_proved=False)
(P/(prefix+'_application.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'},indent=2))
