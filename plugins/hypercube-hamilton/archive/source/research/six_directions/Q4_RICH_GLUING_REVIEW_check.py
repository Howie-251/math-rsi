"""Independent positive-certificate and symmetry audit; writes only own evidence."""
import itertools
import json
import hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PAR=[x.bit_count()%2 for x in range(16)]
EDGES=[(x,x^(1<<j)) for x in range(16) for j in range(4) if x<(x^(1<<j))]
EI={frozenset(e):i for i,e in enumerate(EDGES)}
TRANS=[]
for p in itertools.permutations(range(4)):
 TRANS.append(tuple(sum(((x>>p[j])&1)<<j for j in range(4)) for x in range(16)))

def all_matchings(vertices):
 m=[255]*16
 def rec(V):
  if not V:
   yield bytes(m);return
  x=V[0]
  for j,y in enumerate(V[1:],1):
   m[x]=y;m[y]=x
   yield from rec(V[1:j]+V[j+1:])
   m[x]=m[y]=255
 yield from rec(tuple(vertices))

def read(name,H,f):
 data=(ROOT/name).read_bytes();seen=set();position=0;count=0;cycles=0;low=[];minimum=32;hist={}
 while position<len(data):
  m=data[position:position+16];n=data[position+16];position+=17
  assert len(m)==16 and n>0 and m not in seen
  seen.add(m)
  assert {x for x in range(16) if m[x]==255}==H
  matching=set()
  for x in range(16):
   if x in H:continue
   assert m[x] in range(16) and m[x]!=x and m[m[x]]==x
   matching.add(frozenset((x,m[x])))
  spectrum=0
  for _ in range(n):
   c=data[position:position+15];position+=15
   assert len(c)==15 and len(set(c))==15 and set(c)==set(range(16))-{f}
   ce={frozenset((c[j],c[(j+1)%15])) for j in range(15)}
   assert matching<=ce
   for e in ce-matching:
    assert e in EI
    spectrum|=1<<EI[e]
   cycles+=1
  assert spectrum.bit_count()>=15
  minimum=min(minimum,spectrum.bit_count())
  if spectrum.bit_count()<18:
   low.append((f,m,spectrum));hist[spectrum.bit_count()]=hist.get(spectrum.bit_count(),0)+1
  count+=1
 assert position==len(data)
 # Independently generate all unordered complete-graph pairings and compare sets.
 expected=set(all_matchings(sorted(set(range(16))-H)))
 assert expected==seen
 return low,{'file':name,'records':count,'cycles':cycles,'below18':len(low),'low_size_histogram':hist,'minimum':minimum,'sha256':hashlib.sha256(data).hexdigest(),'complete_matching_set_equal':True}

def transform(row,tr,t):
 f,m,s=row;image=[255]*16
 for x,y in enumerate(m):
  if y!=255:image[tr[x]^t]=tr[y]^t
 result=0
 for j,(x,y) in enumerate(EDGES):
  if s&(1<<j):result|=1<<EI[frozenset((tr[x]^t,tr[y]^t))]
 return (tr[f]^t,bytes(image)),result

def join(d,key,value):d[key]=d.get(key,0)|value

def main():
 reports=[];two=[];four=[]
 for p in (3,15):
  lo,r=read(f'q4_n14_rich_{p}.bin',{0,p},0);two+=lo;reports.append(r)
 for p in (1,4,13):
  lo,r=read(f'q4_a4_rich_{p}.bin',{0,7,11,p},p);four+=lo;reports.append(r)
  print(json.dumps(r),flush=True)
 A={};B={};F={}
 for row in two:
  for tr in TRANS:
   key,s=transform(row,tr,0);join(A,key,s)
   for t in range(16):
    if PAR[t]:
     key,s=transform(row,tr,t);join(B,key,s)
 for (f,m),s in B.items():
  for x,y in EDGES:
   if m[x]==y:
    mm=bytearray(m);mm[x]=mm[y]=255
    join(F,(f,bytes(mm)),s|(1<<EI[frozenset((x,y))]))
 for row in four:
  for tr in TRANS:
   for t in range(16):
    key,s=transform(row,tr,t)
    if PAR[key[0]]:join(F,key,s)
 A={k:s for k,s in A.items() if s.bit_count()<18}
 B={k:s for k,s in B.items() if s.bit_count()<18}
 F={k:s for k,s in F.items() if s.bit_count()<18}
 # Independently classify every 1:3 hole set with its majority forbidden vertex.
 residual=set()
 for p in (1,4,13):
  for tr in TRANS:
   for t in range(16):
    residual.add((frozenset(tr[x]^t for x in (0,7,11,p)),tr[p]^t))
 total=adjacent=nonadjacent=0
 for minority_parity in (0,1):
  for a in range(16):
   if PAR[a]!=minority_parity:continue
   for majority in itertools.combinations([x for x in range(16) if PAR[x]!=minority_parity],3):
    for f in majority:
     H=frozenset((a,*majority));total+=1
     augment=[b for b in majority if b!=f and (a^b).bit_count()==1]
     if augment:
      adjacent+=1
      # Removing a and the chosen b leaves same-parity two holes, including f.
      for b in augment:
       HH=H-{a,b};assert len(HH)==2 and f in HH and len({PAR[x] for x in HH})==1
     else:
      nonadjacent+=1;assert (H,f) in residual
 assert len(residual)==nonadjacent
 # For each fixed forbidden root the other same-parity hole is at distance 2 or 4.
 two_types=set()
 for p in (3,15):
  for tr in TRANS:
   for t in range(16):two_types.add((frozenset((tr[0]^t,tr[p]^t)),t))
 expected_types={(frozenset((f,g)),f) for f in range(16) for g in range(16) if f!=g and PAR[f]==PAR[g]}
 assert two_types==expected_types
 mins=[];pairs=[]
 for name,d in (('n14_n14',B),('n14_a4',F)):
  minimum=32;n=0
  for ka,sa in A.items():
   assert ka[0]==0 and sa.bit_count()>=15
   for kb,sb in d.items():
    assert PAR[kb[0]]==1 and sb.bit_count()>=15
    overlap=(sa&sb).bit_count();assert overlap>0
    minimum=min(minimum,overlap);n+=1
  mins.append(minimum);pairs.append({'type':name,'pairs':n,'minimum_intersection':minimum,'disjoint':0})
 result={'status':'PASS','files':reports,'records':sum(r['records'] for r in reports),'cycles':sum(r['cycles'] for r in reports),'n14_low_A':len(A),'n14_low_B':len(B),'a4_low_B_candidates':len(F),'pairs':pairs,'hole_classification':{'typed_a4_instances':total,'adjacent_augmentable':adjacent,'nonadjacent':nonadjacent,'nonadjacent_orbit_image_count':len(residual),'typed_n14_instances':len(two_types)},'source_files_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ('q4_n14_richer_spectrum.cpp','q4_a4_richer_spectrum.cpp','verify_q4_rich_spectrum_gluing.py')},'full_p6_proved':False}
 (ROOT/'Q4_RICH_GLUING_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('files','source_files_sha256')}),flush=True)

if __name__=='__main__':main()
