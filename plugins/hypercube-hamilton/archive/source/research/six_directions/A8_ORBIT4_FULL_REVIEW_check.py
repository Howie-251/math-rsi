"""Fresh semantic-template/domain/cycle check, with no producer imports."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import hashlib,json
P=Path(__file__).resolve().parent
H={0,1,2,4,15,23,27,29}; V=set(range(32))-H
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def even(x):return x.bit_count()%2==0
def encode(edges):return bytes(x for e in sorted(tuple(sorted(e)) for e in edges) for x in e)
names=['A8_ORBIT4_FULL_CLOSURE.md','A8_orbit4_joint_bad_enumerate.py',
 'A8_orbit4_joint_bad_enumeration.json','verify_A8_orbit4_joint_bad.py',
 'A8_orbit4_joint_bad_verification.json','A8_orbit4_joint_bad_inputs.bin',
 'A8_orbit4_joint_bad_certificates.bin','A8_DOUBLE_BRIDGE_SUFFICIENT.md',
 'A8_THREE_BRIDGE_SUFFICIENT.md','A8_BRIDGE_INPUTS_REVIEW.md','A8_BRIDGE_INPUTS_REVIEW.json',
 'A8_Q4_T63_CLASSIFICATION.md','Q4_T15_CLASSIFICATION.md','Q4_GENERAL_AUGMENTATION.md']
hashes={n:sha(P/n) for n in names}
templates=[]
for bit in (2,4,8,16):
 A={x for x in range(32) if not x&bit};B=set(range(32))-A
 sources={x for x in H&A if not even(x)}
 Y={x^bit for x in sources}
 assert Y <= V and Y <= B and 0 in A
 assert {x for x in H&A if even(x)}==({0,29} if bit==2 else {0,27} if bit==4 else {0,23} if bit==8 else {0,15})
 local_neighbors=lambda a:{a^(1<<i) for i in range(5) if (1<<i)!=bit}
 if len(Y)==2:
  assert len(H&A)==4 and len(H&B)==4
  singleton={x for x in H&B if not even(x)};assert len(singleton)==1
  a=next(iter(singleton));assert Y<=local_neighbors(a)
  ob=tuple(sorted(local_neighbors(a)-Y));assert len(ob)==2
  assert len((H&B)|Y)==6 and sum(even(x) for x in (H&B)|Y)==5
 else:
  assert len(Y)==3 and len(H&A)==5 and len(H&B)==3
  common={a for a in B if Y<=local_neighbors(a)};assert len(common)==1
  a=next(iter(common));rest=local_neighbors(a)-Y;assert len(rest)==1
  ob=tuple(sorted((a,next(iter(rest)))))
  assert len((H&B)|Y)==6 and all(even(x) for x in (H&B)|Y)
 assert set(ob)<=V-Y and all(x&bit for x in ob)
 templates.append((bit,Y,ob))
assert [t[2] for t in templates]==[(10,18),(12,20),(8,24),(16,24)]
raw=(P/'A8_orbit4_joint_bad_inputs.bin').read_bytes()
assert len(raw)==200475*24
records=set()
for i in range(0,len(raw),24):
 rec=raw[i:i+24];pairs=[tuple(rec[j:j+2]) for j in range(0,24,2)]
 assert set(rec)==V and len(set(rec))==24 and encode(pairs)==rec
 assert rec not in records;records.add(rec)
branches=[]
def rule(e,bit,Y,ob):
 Bends={x for x in e if x&bit};S=Y|set(ob)
 if len(Bends)==1:return Bends<=S
 if len(Bends)==2 and set(e)&Y:return set(e)<=S
 return True
for mask in range(16):
 fixed=[ob for j,(_,_,ob) in enumerate(templates) if mask&(1<<j)]
 endpoints=[x for e in fixed for x in e]
 if len(endpoints)!=len(set(endpoints)):
  branches.append({'mask':mask,'count':0,'empty_reason':'fixed edges share 24'});continue
 def allowed(e):
  return all((mask&(1<<j)) or (e!=ob and rule(e,bit,Y,ob)) for j,(bit,Y,ob) in enumerate(templates))
 assert all(allowed(e) for e in fixed)
 left=V-set(endpoints);adj={x:set() for x in left}
 for e in combinations(sorted(left),2):
  if allowed(e):
   x,y=e;adj[x].add(y);adj[y].add(x)
 unseen=set(left);components=[]
 while unseen:
  reach={min(unseen)};front=list(reach)
  while front:
   for y in adj[front.pop()]-reach:reach.add(y);front.append(y)
  assert all(adj[x]<=reach for x in reach)
  unseen-=reach;components.append(sorted(reach))
 odd=[c for c in components if len(c)%2]
 count=[0]
 def visit(rem,edges):
  if not rem:
   rec=encode(fixed+edges)
   assert rec in records,('missing or duplicated',mask,edges)
   actual=sum(1<<j for j,(_,_,ob) in enumerate(templates) if ob in fixed+edges)
   assert actual==mask
   records.remove(rec);count[0]+=1;return
  x=min(rem)
  for y in sorted(adj[x]&rem):visit(rem-{x,y},edges+[(min(x,y),max(x,y))])
 if not odd:visit(left,[])
 branches.append({'mask':mask,'count':count[0],'odd_components':odd})
assert not records
assert [b['count'] for b in branches]==[0,0,0,2025,0,0,0,99225,0,0,0,99225,0,0,0,0]
cert=(P/'A8_orbit4_joint_bad_certificates.bin').read_bytes()
assert len(cert)==200475*55
for i in range(200475):
 rec=cert[55*i:55*i+55];assert rec[:24]==raw[24*i:24*i+24]
 mate={}
 for j in range(0,24,2):a,b=rec[j:j+2];mate[a]=b;mate[b]=a
 c=rec[24:];assert len(c)==31 and set(c)==set(range(1,32))
 for j,a in enumerate(c):
  b=c[(j+1)%31]
  assert mate.get(a)==b or (a^b) in (1,2,4,8,16)
 for j,a in enumerate(c):
  if a in mate:assert mate[a] in (c[(j-1)%31],c[(j+1)%31])
orbit=set()
for perm in permutations(range(5)):
 orbit.add(tuple(sorted(sum(((x>>perm[i])&1)<<i for i in range(5)) for x in H)))
assert len(orbit)==30
assert hashes=={n:sha(P/n) for n in names},'Audited input changed'
out={'status':'PASS','matching_count':200475,'positive_31cycles':200475,'geometry_orbit_size':30,
 'templates':[{'bit':b,'mirrors':sorted(y),'actual_obstruction_edge':list(ob)} for b,y,ob in templates],
 'branches':branches,'audited_input_hashes':hashes,'checker_sha256':sha(Path(__file__)),
 'no_producer_or_existing_verifier_imported':True,'full_A8_proved':False,'full_P6_proved':False}
(P/'A8_ORBIT4_FULL_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('branches','audited_input_hashes')}))
