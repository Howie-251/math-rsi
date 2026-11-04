"""Positive spectrum certificates and simultaneous zero-crossing gluing cover.

No upper bound on an exact spectrum is used: small stored unions are simply
exceptional positive certificate rows, compared exhaustively after symmetry.
"""
import hashlib,itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
EDGES=[(x,y) for x in range(16) for y in range(x+1,16) if (x^y).bit_count()==1]
INDEX={e:i for i,e in enumerate(EDGES)}
PERMS=[[sum(((x>>j)&1)<<p[j] for j in range(4)) for x in range(16)] for p in itertools.permutations(range(4))]
def edge(a,b):return tuple(sorted((a,b)))
def double_factorial(n):
 r=1
 for i in range(1,n,2):r*=i
 return r
def read(name,holes,forbidden):
 raw=(ROOT/name).read_bytes();count=double_factorial(16-len(holes));seen=bytearray(count)
 pos=0;small=[];cycles=0;minimum=33
 while pos<len(raw):
  m=tuple(raw[pos:pos+16]);n=raw[pos+16];pos+=17;assert n>0
  assert {x for x in range(16) if m[x]==255}==set(holes)
  covered=set(range(16))-set(holes)
  for x in covered:assert m[x] in covered and m[x]!=x and m[m[x]]==x
  rest=sorted(covered);rank=0
  while rest:
   x=rest.pop(0);i=rest.index(m[x]);rank+=i*double_factorial(len(rest)-1);rest.pop(i)
  assert not seen[rank];seen[rank]=1
  required={edge(x,m[x]) for x in covered};union=set()
  for k in range(n):
   c=raw[pos:pos+15];pos+=15
   assert len(c)==len(set(c))==15 and set(c)==set(range(16))-{forbidden}
   es={edge(x,y) for x,y in zip(c,c[1:]+c[:1])};assert required<=es
   assert all(e in INDEX for e in es-required)
   union.update(es-required);cycles+=1
  assert len(union)>=15
  mask=sum(1<<INDEX[e] for e in union);minimum=min(minimum,len(union))
  if len(union)<18:small.append((forbidden,m,mask))
 assert pos==len(raw) and all(seen)
 return small,{'file':name,'records':count,'cycles':cycles,'below18':len(small),'minimum_certified_union':minimum,'sha256':hashlib.sha256(raw).hexdigest()}
def transformed(row,tr,t):
 v,m,mask=row;new=[255]*16
 for x,y in enumerate(m):
  if y!=255:new[tr[x]^t]=tr[y]^t
 mask2=sum(1<<INDEX[edge(tr[x]^t,tr[y]^t)] for i,(x,y) in enumerate(EDGES) if mask>>i&1)
 return (tr[v]^t,tuple(new)),mask2
def main():
 low=[];nonadj=[];reports=[]
 for p in (3,15):
  x,r=read(f'q4_n14_rich_{p}.bin',[0,p],0);low+=x;reports.append(r)
 for p in (1,4,13):
  x,r=read(f'q4_a4_rich_{p}.bin',[0,7,11,p],p);nonadj+=x;reports.append(r)
 A={};B={}
 for row in low:
  for tr in PERMS:
   key,mask=transformed(row,tr,0);A[key]=A.get(key,0)|mask
   for t in range(16):
    if t.bit_count()%2:
     key,mask=transformed(row,tr,t);B[key]=B.get(key,0)|mask
 B4={}
 # Any adjacent-reducible A4 instance is obtained by deleting a short
 # edge from a two-hole completion. A high completion proves >=18 at once.
 for (v,m),mask in B.items():
  for x,y in enumerate(m):
   if y!=255 and x<y and (x^y).bit_count()==1:
    f=list(m);f[x]=f[y]=255;key=(v,tuple(f));value=mask|(1<<INDEX[(x,y)])
    B4[key]=B4.get(key,0)|value
 for row in nonadj:
  for tr in PERMS:
   for t in range(16):
    key,mask=transformed(row,tr,t)
    if key[0].bit_count()%2:B4[key]=B4.get(key,0)|mask
 # These are conservative low candidate lists. Other reductions may give
 # a high certificate too; leaving such cases here cannot overclaim.
 A={k:m for k,m in A.items() if m.bit_count()<18}
 B={k:m for k,m in B.items() if m.bit_count()<18}
 B4={k:m for k,m in B4.items() if m.bit_count()<18}
 bad14=[];bad4=[];minimum14=33;minimum4=33
 for a,x in A.items():
  for b,y in B.items():
   n=(x&y).bit_count();minimum14=min(minimum14,n)
   if not n:bad14.append((a,b))
  for b,y in B4.items():
   n=(x&y).bit_count();minimum4=min(minimum4,n)
   if not n:bad4.append((a,b))
 result={'status':'PASS' if not bad14 and not bad4 else 'OPEN_PAIRS','scope':'Q4 optional-edge intersections for opposite-parity forbidden vertices; not full Q5 T15',
 'files':reports,'records':sum(x['records'] for x in reports),'cycles':sum(x['cycles'] for x in reports),
 'n14_low_A':len(A),'n14_low_B':len(B),'a4_low_B_candidates':len(B4),
 'n14_n14_bad_pairs':len(bad14),'n14_a4_bad_pairs':len(bad4),'minimum_low_intersection_n14':minimum14,'minimum_low_intersection_a4':minimum4,
 'bad_pair_examples_n14':bad14[:10],'bad_pair_examples_a4':bad4[:10],'full_p6_proved':False}
 (ROOT/'q4_rich_spectrum_gluing_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('files','bad_pair_examples_n14','bad_pair_examples_a4')}))
if __name__=='__main__':main()
