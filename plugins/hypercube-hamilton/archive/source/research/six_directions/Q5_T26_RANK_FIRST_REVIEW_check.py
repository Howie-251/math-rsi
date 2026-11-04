"""Fresh reviewer checker. Does not execute or import any producer code."""
from pathlib import Path
import json, hashlib, itertools, datetime, time
P=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def data(n):return (P/n).read_bytes()
manifest=json.loads(data('Q5_T26_RANK_FIRST_MANIFEST.json'))
for n,h in manifest['hashes'].items():
 assert sha(data(n))==h,('manifest hash',n)
 assert len(data(n))==manifest['sizes'][n],('manifest size',n)
H={0,1,3,4,14,22,28,31};U={1,4};K=set(range(32))-H
def records(n,width):
 b=data(n);assert len(b)%width==0
 return [b[i:i+width] for i in range(0,len(b),width)]
def matching(b):
 assert len(b)==24 and set(b)==K
 assert all(b[i]!=b[i+1] for i in range(0,24,2))
 return list(zip(b[::2],b[1::2]))
pairs=[matching(b) for b in records('Q5_T26_RANK_first_pairs.bin',24)]
cols=[matching(b) for b in records('Q5_T26_RANK_first_columns.bin',24)]
forests=records('Q5_T26_RANK_first_forests.bin',36)
assert len(pairs)==len(cols)==len(forests)==2048
def root(p,x):
 while p[x]!=x:
  p[x]=p[p[x]];x=p[x]
 return x
for b,paired in zip(forests,pairs):
 e=list(zip(b[::2],b[1::2]));assert len(set(e))==18
 par=list(range(32));deg=[0]*32
 for x,y in e:
  assert x<y<32 and (x^y).bit_count()==1 and not ({x,y}&U)
  rx,ry=root(par,x),root(par,y);assert rx!=ry
  par[rx]=ry;deg[x]+=1;deg[y]+=1
 assert all(deg[x]==(0 if x in U else 2 if x in H else 1) for x in range(32))
 components={}
 for x in K:components.setdefault(root(par,x),[]).append(x)
 assert len(components)==12 and all(len(v)==2 for v in components.values())
 assert {tuple(sorted(v)) for v in components.values()}=={tuple(sorted(e)) for e in paired}
print('all 2048 forests, endpoint pairs, columns valid',flush=True)
saved=data('Q5_T26_RANK_first_matrix.bin'); rebuilt=bytearray(len(saved));rows=[]
for i,edges in enumerate(pairs):
 # Contract the first matching: connectivity becomes DSU on its 12 components.
 comp={x:k for k,e in enumerate(edges) for x in e}
 for j,edges2 in enumerate(cols):
  par=list(range(12));count=12
  for x,y in edges2:
   a,b=root(par,comp[x]),root(par,comp[y])
   if a!=b:par[a]=b;count-=1
  if count==1:rebuilt[i*256+j//8]|=1<<(j%8)
 rows.append(int.from_bytes(rebuilt[i*256:(i+1)*256],'little'))
assert rebuilt==saved
print('4194304 connectivity bits identical',flush=True)
# Use lowest-set-bit pivots, unlike the supplied highest-bit triangular certificate.
basis={}
for row in rows:
 while row:
  low=row&-row;k=low.bit_length()-1
  if k not in basis:basis[k]=row;break
  row^=basis[k]
assert len(basis)==2048
# Also inspect saved highest-bit combination witnesses; not needed for independent rank.
piv=[int.from_bytes(b,'little') for b in records('Q5_T26_RANK_first_pivots.bin',256)]
comb=[int.from_bytes(b,'little') for b in records('Q5_T26_RANK_first_combos.bin',256)]
for j,(v,c) in enumerate(zip(piv,comb)):
 x=0
 while c:
  low=c&-c;x^=rows[low.bit_length()-1];c^=low
 assert x==v and v.bit_length()==j+1
print('independent GF2 rank 2048 and all saved combinations verified',flush=True)
orbit={}
for perm in itertools.permutations(range(5)):
 transform=[sum(((x>>k)&1)<<perm[k] for k in range(5)) for x in range(32)]
 for shift in range(32):
  f=[x^shift for x in transform]
  key=(tuple(sorted(f[x] for x in (0,3))),tuple(sorted(f[x] for x in (1,4,14,22,28,31))),tuple(sorted(f[x] for x in (1,4))))
  orbit[key]=(perm,shift)
def project(x,d):
 bits=[j for j in range(6) if j!=d]
 return sum(((x>>j)&1)<<i for i,j in enumerate(bits))
def witness(rec,v):
 Z=set(rec[:4]);W=set(rec[4:]);assert len(Z)==4 and len(W)==5 and v not in W
 assert all(x and x.bit_count()%2==0 for x in Z)
 assert all(x.bit_count()%2==1 for x in W)
 assert all((x^y).bit_count()!=1 for x in Z for y in W)
 found=[]
 for d in range(6):
  inside=lambda x: (x>>d&1)==(v>>d&1)
  za={x for x in Z if inside(x)};wa={x for x in W if inside(x)}
  row=(len(za),len(wa))
  if row==(2,1):sources=[tuple(sorted(za))];minor=Z-za;major=W-wa
  elif row==(0,3):sources=itertools.combinations(sorted(wa-{1<<d}),2);minor=W-wa;major=Z-za
  else:continue
  for S in sources:
   Y={x^(1<<d) for x in S}
   assert len(Y)==2 and 0 not in Y and not (Y&(Z|W))
   assert all(not inside(y) and (x^y).bit_count()==1 for x,y in zip(S,[x^(1<<d) for x in S]))
   key=(tuple(sorted(project(x,d) for x in minor)),tuple(sorted(project(x,d) for x in major|Y)),tuple(sorted(project(x,d) for x in Y)))
   if key in orbit:
    perm,shift=orbit[key]
    found.append({'cut':d,'row':row,'sources':S,'marked_geometry':key,'cube_permutation':perm,'cube_shift':shift})
 return found
review=json.loads(data('TEN_COVERED_Q5_ENDPOINT_REVIEW.json'));reports=[];witnesses=[]
oldcoverage=json.loads(data('Q5_T26_RANK_first_coverage.json'))
claimed={(w['v'],w['input_index']):w for w in oldcoverage['witnesses']}
for v in (1,7,31):
 old=records(f'ten_covered_after_full_A8_v{v}.bin',9)
 currentname=f'ten_covered_q5_and_t63_remaining_v{v}.bin';current=records(currentname,9)
 assert sha(data(currentname))==review['audited_input_hashes'][currentname]
 assert len(set(old))==len(old) and len(set(current))==len(current) and set(current)<=set(old)
 covered=set();oldhit=0
 for i,rec in enumerate(old):
  found=witness(rec,v)
  assert bool(found)==((v,i) in claimed),('old membership',v,i)
  if not found:continue
  w=claimed[v,i]
  assert any(z['cut']==w['cut'] and tuple(z['row'])==tuple(w['row']) and set(z['sources'])==set(w['bridge_sources']) and all(list(z['marked_geometry'][k])==w[n] for k,n in enumerate(('local_minority','local_majority','local_omitted'))) for z in found)
  oldhit+=1
  if rec in set(current):
   covered.add(rec);witnesses.append({'v':v,'record':list(rec),**found[0]})
 remaining=b''.join(r for r in current if r not in covered)
 n=f'Q5_T26_RANK_FIRST_REVIEW_remaining_v{v}.bin';(P/n).write_bytes(remaining)
 assert set(remaining[i:i+9] for i in range(0,len(remaining),9))==set(current)-covered
 reports.append({'v':v,'latest_input':len(current),'old_input_covered':oldhit,'net_new':len(covered),'remaining':len(remaining)//9,'remaining_file':n,'remaining_sha256':sha(remaining)})
 print(reports[-1],flush=True)
out={'all_manifest_hashes_sizes_match':True,'forests_checked':2048,'columns_checked':2048,'connectivity_bits_checked':2048**2,'rank_GF2':len(basis),'matrix_sha256':sha(rebuilt),'saved_pivots_combinations_checked':2048,'automorphism_orbit_size':len(orbit),'reports':reports,'new_total':sum(r['net_new'] for r in reports),'remaining_total':sum(r['remaining'] for r in reports),'old_coverage_total':sum(r['old_input_covered'] for r in reports)}
(P/'Q5_T26_RANK_FIRST_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
(P/'Q5_T26_RANK_FIRST_REVIEW_witnesses.json').write_text(json.dumps(witnesses,indent=2)+'\n')
print(json.dumps(out),flush=True)
