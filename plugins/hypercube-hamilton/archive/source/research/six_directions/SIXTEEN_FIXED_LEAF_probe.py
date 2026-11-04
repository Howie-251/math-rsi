"""Producer restriction probe of the actual index6 forced-edge task."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
def basis(n):
 if n==2:return [[1,0]]
 out=[]
 for a in basis(n-2):
  b=a[:];p=a[n-3];b.extend([p,n-3]);b[p]=n-2;b[n-3]=n-1
  out.extend([b,a+[n-1,n-2]])
 return out
def conn(a,b):
 v=0
 for j in range(1,len(a)//2+1):
  v=b[a[v]]
  if v==0:return j==len(a)//2
 raise ValueError('bad pair')
out=[]
for task in json.loads((P/'SIXTEEN_FIXED_LEAF_tasks.json').read_text()):
 i=task['local_index'];edges=task['edges'];assert len(edges)==1;a,b=edges[0]
 raw=(P/f'SIXTEEN_NEW_TYPES_orbit_{i:03d}_pairs.bin').read_bytes()
 K=set(raw[:18]);V=sorted(K-{a,b});cols=basis(len(V));piv={};nonzero=[];selected=[];qs=[];matrix=[]
 for ri in range(len(raw)//18):
  p={}
  for k in range(0,18,2):x,y=raw[18*ri+k:18*ri+k+2];p[x]=y;p[y]=x
  if p[a]==b:continue
  x,y=p[a],p[b];p[x]=y;p[y]=x
  q=[V.index(p[v]) for v in V];nonzero.append(ri);row=sum(conn(q,c)<<k for k,c in enumerate(cols));r=row
  while r:
   h=r.bit_length()-1
   if h in piv:r^=piv[h]
   else:piv[h]=r;selected.append(ri);qs.append(q);matrix.append(row);break
 common=set((V[x],V[y]) for x,y in enumerate(qs[0]) if x<y)
 for ri in nonzero:
  p={}
  for k in range(0,18,2):x,y=raw[18*ri+k:18*ri+k+2];p[x]=y;p[y]=x
  x,y=p[a],p[b];p[x]=y;p[y]=x
  common&={tuple(sorted((x,p[x]))) for x in V}
 item=dict(local_index=i,required_edges=edges,rank=len(piv),target=len(cols),nonzero=len(nonzero),common_compressed_pairs=sorted(common),selected=selected)
 out.append(item)
(P/'SIXTEEN_FIXED_LEAF_probe.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
