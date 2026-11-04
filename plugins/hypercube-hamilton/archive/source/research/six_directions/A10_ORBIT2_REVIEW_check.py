"""Independent exhaustive domain reconstruction and positive witness verifier.
Does not import, invoke, or modify any producer or prior verifier.
"""
import hashlib
import itertools as it
import json
import time
from pathlib import Path

R=Path(__file__).resolve().parent
manifest=json.loads((R/'A10_ORBIT2_MANIFEST.json').read_text())
names=[row['file'] for row in manifest['files']]+['A10_ORBIT2_MANIFEST.json',
 'A10_FIRST_ORBIT_ANALYTIC_CLOSURE.md','A10_FIRST_ORBIT_REVIEW.md',
 'Q4_GENERAL_AUGMENTATION.md','Q4_T15_CLASSIFICATION.md']
def hashes():
 return {n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in names}
before=hashes()
for row in manifest['files']:
 assert (R/row['file']).stat().st_size==row['bytes']
 assert before[row['file']]==row['sha256']
print('Frozen manifest and all declared hashes match.',flush=True)
H={0,3,5,6,8,15,23,25,26,28};Z={3,5,6,15,23};W={8,25,26,28}
V=set(range(32));C={16,17,18,20,24,27,29,30};D=V-H-C
assert len(D)==14 and len(C)==8 and C.isdisjoint(H)
assert all(x.bit_count()%2==0 for x in Z|{0})
assert all(x.bit_count()%2==1 for x in W)
bits=[1,2,4,8,16];group=[];images=set()
for order in it.permutations(bits):
 tr=bytes(sum(order[i] for i in range(5) if x&bits[i]) for x in range(32))
 geom=(tuple(sorted(tr[x] for x in Z)),tuple(sorted(tr[x] for x in W)))
 images.add(geom)
 if geom==(tuple(sorted(Z)),tuple(sorted(W))):
  assert set(tr[x] for x in C)==C and set(tr[x] for x in D)==D
  assert tr[8]==8 and tr[16]==16
  group.append(tr)
assert len(images)==20 and len(group)==6
A={x for x in V if not x&16};B=V-A;M={23^j for j in bits if j!=16}
assert (len((Z|{0})&A),W&A,(Z|{0})&B,W&B)==(5,{8},{23},{25,26,28})
assert M=={x^16 for x in Z&A}=={19,21,22,31}
assert M.isdisjoint(H) and B-M-H==C
traps=[]
for b in [1,2,4,8]:
 A={x for x in V if not x&b};B=V-A
 if b==8:
  choices=list(it.combinations(sorted(x^b for x in Z&A),3));a=15
 else:
  choices=[tuple(sorted(x^b for x in W&A))];a=next(iter(W&B))
 for choice in choices:
  assert len({a^j for j in bits if j!=b}-set(choice))==1
 traps.append(dict(bit=b,singleton=a,choices=choices))

# Construct all perfect matchings using an explicit stack of partial states.
# Endpoint bytes are canonical edge lists, with least uncovered vertex first.
def matchings(vertices):
 stack=[(tuple(sorted(vertices)),b'')]
 while stack:
  remaining,edges=stack.pop()
  if not remaining:
   yield edges
   continue
  a=remaining[0]
  for j in range(len(remaining)-1,0,-1):
   b=remaining[j]
   stack.append((remaining[1:j]+remaining[j+1:],edges+bytes((a,b))))
def transform(f,tr):
 pairs=[]
 for i in range(0,len(f),2):
  a,b=tr[f[i]],tr[f[i+1]]
  pairs.append(bytes((min(a,b),max(a,b))))
 return b''.join(sorted(pairs))
cm=list(matchings(C));dm=list(matchings(D))
assert len(cm)==len(set(cm))==105
assert len(dm)==len(set(dm))==135135
c_reps=sorted({min(transform(f,g) for g in group) for f in cm})
assert len(c_reps)==23
canonical_cache={};fixed_cache={};block_rows=[];total=weighted=0
frozen=(R/'A10_ORBIT2_canonical_inputs.bin').read_bytes()
offset=0
for fc in c_reps:
 stabilizer=tuple(g for g in group if transform(fc,g)==fc)
 if stabilizer not in canonical_cache:
  # Canonicalize every D input and take an exact SET, rather than relying
  # on Burnside or a weighted total to establish completeness.
  expected={min(transform(fd,g) for g in stabilizer) for fd in dm}
  canonical_cache[stabilizer]=expected
 expected=canonical_cache[stabilizer]
 ordered=[fd for fd in dm if fd in expected]
 assert len(ordered)==len(expected)
 rebuilt=b''.join(fc+fd for fd in ordered)
 assert frozen[offset:offset+len(rebuilt)]==rebuilt,('domain block',fc.hex())
 offset+=len(rebuilt);total+=len(ordered)
 weight=0
 for fd in ordered:
  fixed=sum(transform(fd,g)==fd for g in stabilizer)
  assert fixed and 6%fixed==0
  weight+=6//fixed
 weighted+=weight
 block_rows.append(dict(C_matching=[list(fc[i:i+2]) for i in range(0,8,2)],
  C_stabilizer_size=len(stabilizer),canonical_R_matchings=len(ordered),weighted_full_matchings=weight))
 print('Exact canonical block',len(block_rows),'records',len(ordered),flush=True)
assert offset==len(frozen)==52064694 and total==2366577 and weighted==14189175
producer_counts=json.loads((R/'A10_ORBIT2_canonical_counts.json').read_text())
for actual,claimed in zip(block_rows,producer_counts['rows']):
 for key in actual: assert actual[key]==claimed[key]
assert len(producer_counts['rows'])==23
burn=[]
for g in group:
 fc=sum(transform(f,g)==f for f in cm)
 fd=sum(transform(f,g)==f for f in dm)
 burn.append(dict(C_fixed=fc,D_fixed=fd,full_fixed=fc*fd))
assert sorted((r['C_fixed'],r['D_fixed']) for r in burn)==[(3,27)]*2+[(9,375)]*3+[(105,135135)]
assert sum(r['full_fixed'] for r in burn)//6==total
print('Exact full canonical byte stream independently reconstructed.',flush=True)

chunk_rows=[];checked=0
short={1,2,4,8,16};support=set(range(1,32))
for start,count in [(0,800000),(800000,800000),(1600000,766577)]:
 name=f'A10_ORBIT2_chunk_{start}.bin';data=(R/name).read_bytes()
 assert len(data)==53*count and checked==start
 long_required=0
 for local in range(count):
  off=53*local;record=data[off:off+53];required=record[:22];cycle=record[22:]
  assert required==frozen[22*(start+local):22*(start+local+1)]
  assert len(cycle)==31 and set(cycle)==support
  # Build cycle neighbors, then check every required edge directly.
  adjacent=[set() for _ in range(32)]
  for j,u in enumerate(cycle):
   v=cycle[(j+1)%31];adjacent[u].add(v);adjacent[v].add(u)
  mate=[-1]*32
  for j in range(0,22,2):
   u,v=required[j],required[j+1]
   assert v in adjacent[u]
   mate[u]=v;mate[v]=u
   long_required+=int(u^v not in short)
  for j,u in enumerate(cycle):
   v=cycle[(j+1)%31]
   assert (u^v in short) or mate[u]==v
  if (local+1)%200000==0: print(name,'verified',local+1,flush=True)
 checked+=count
 chunk_rows.append(dict(file=name,start=start,count=count,positive_cycles=count,long_required_edges_verified=long_required))
 print(name,'PASS',count,flush=True)
assert checked==total
assert hashes()==before
out=dict(status='PASS',audited_input_hashes=before,manifest_matches=True,
 production_inputs_unchanged=True,marked_orbit_size=20,coordinate_stabilizer_size=6,
 C_matchings=105,D_matchings=135135,unsymmetrized_domain=14189175,
 C_representatives=23,canonical_domain_records=total,
 domain_verification='Independent exact canonical set reconstruction from all C and D matchings; full ordered byte stream equality',
 canonical_domain_bytes=offset,weighted_count=weighted,blocks=block_rows,burnside=burn,
 chunks=chunk_rows,positive_cycles_checked=checked,unknown_or_negative_records=0,
 degree_obstruction_templates=traps,Hamilton_searches=0)
(R/'A10_ORBIT2_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL PASS; input hashes unchanged.',flush=True)
