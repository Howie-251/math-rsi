"""Independent positive-cycle and complete perfect-matching rank verification."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def pairings(n):
 r=1
 for x in range(1,n,2):r*=x
 return r
def check(name,holes,forbidden,bound):
 raw=(ROOT/name).read_bytes();vertices=set(range(16))-set(holes)
 required_vertices=set(range(16))-({forbidden} if forbidden is not None else set())
 length=len(required_vertices);seen=bytearray(10395);pos=count=cycles=0;minimum=33
 while pos<len(raw):
  assert pos+17<=len(raw);m=raw[pos:pos+16];n=raw[pos+16];pos+=17;assert n>0
  assert {x for x in range(16) if m[x]==255}==set(holes)
  for x in vertices:assert m[x] in vertices and m[x]!=x and m[m[x]]==x
  rest=sorted(vertices);rank=0
  while rest:
   x=rest.pop(0);i=rest.index(m[x]);rank+=i*pairings(len(rest)-1);rest.pop(i)
  assert not seen[rank];seen[rank]=1
  f={frozenset((x,m[x])) for x in vertices};union=set()
  for _ in range(n):
   c=raw[pos:pos+length];pos+=length;assert len(c)==len(set(c))==length and set(c)==required_vertices
   e={frozenset((x,y)) for x,y in zip(c,c[1:]+c[:1])};assert len(e)==length and f<=e
   for x,y in map(tuple,e-f):assert (x^y).bit_count()==1
   union|=e-f;cycles+=1
  assert len(union)>=bound;minimum=min(minimum,len(union));count+=1
 assert pos==len(raw) and count==10395 and all(seen)
 return {'file':name,'records':count,'cycles':cycles,'lower_bound':bound,'minimum_certified_union':minimum,'sha256':hashlib.sha256(raw).hexdigest()}
def main():
 files=[check(f'q4_four_spectrum_A_{v}.bin',[0,7,11,v],v,15) for v in (1,4,13)]
 files.append(check('q4_four_spectrum_balanced.bin',[0,3,13,14],None,18))
 result={'status':'PASS','scope':'Q4 four-hole optional-edge bounds, not A6 closure','records':sum(x['records'] for x in files),'cycles':sum(x['cycles'] for x in files),'files':files,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'a6_proved':False,'full_p6_proved':False}
 (ROOT/'q4_four_hole_spectrum_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:result[k] for k in ['status','records','cycles']}))
if __name__=='__main__':main()
