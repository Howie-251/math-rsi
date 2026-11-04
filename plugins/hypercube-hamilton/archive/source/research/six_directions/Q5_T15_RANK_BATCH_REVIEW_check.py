"""Independent application replay; no producer functions are imported/executed."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter,defaultdict
import json,hashlib,subprocess
P=Path(__file__).resolve().parent
def raw(n):return (P/n).read_bytes()
def sha(b):return hashlib.sha256(b).hexdigest()
def load(n):return json.loads(raw(n))
manifest=load('Q5_T15_RANK_BATCH_MANIFEST.json')
for n,h in manifest['hashes'].items():
 assert sha(raw(n))==h,('hash',n)
 assert len(raw(n))==manifest['sizes'][n],('size',n)
registry=load('Q5_T15_RANK_batch_summary.json')['reports']
assert len(registry)==15
import re
tables=re.findall(r'^\| (\d+) \| ([\d,]+) \| ([\d,]+) \| (\d+) \| 4096 \|\r?$',raw('Q5_T15_RANK_BATCH_PROOF.md').decode(),re.M)
assert len(tables)==15
maps=[tuple(sum(((x>>j)&1)<<p[j] for j in range(5)) for x in range(32)) for p in permutations(range(5))]
old=load('t15_analytic_geometry.json')['T15']['residual_orbits'];alignment=load('Q5_T15_RANK_old_core_alignment.json')
old_alignment=[]
for index,maj,om,examined in tables:
 r=registry[int(index)];g=r['geometry'];major=list(map(int,maj.split(',')));omit=list(map(int,om.split(',')))
 assert major==g['majority'] and omit==g['omitted'] and int(examined)==r['forests_examined']
 included=set(major)-set(omit)
 key=min((tuple(sorted(m[x] for x in omit)),tuple(sorted(m[x] for x in included))) for m in maps)
 matched=[i for i,a in enumerate(old) if (tuple(a['avoided']),tuple(a['included']))==key]
 same=any(sum((x>>j)&1 for x in major)==4 and all((x>>j)&1 for x in omit) for j in range(5))
 a=alignment[int(index)];assert a['old_core_id']==(matched[0] if matched else None)
 assert bool(a.get('excluded_by_old_same_face_test'))==same
 old_alignment.append(dict(orbit_index=int(index),old_core_id=a['old_core_id'],old_same_face_test=same))
lookup={};logs=[]
for r in registry:
 i=r['orbit_index'];g=r['geometry'];prefix=f'Q5_T15_RANK_orbit_{i:02}'
 h=[0]+list(g['majority']);u=list(g['omitted'])
 assert list(map(int,raw(prefix+'_config.txt').split()))==h+u
 assert len(h)==len(set(h))==6 and len(u)==len(set(u))==2 and set(u)<=set(h[1:])
 assert all(x.bit_count()%2==1 for x in h[1:])
 result=subprocess.run([str(P/'Q5_T15_RANK_BATCH_REVIEW_check.exe'),str(P/prefix)],capture_output=True,check=True)
 logs.append(prefix+' '+result.stdout.decode().strip());print(logs[-1],flush=True)
 for perm in permutations(range(5)):
  image=[sum(((x>>j)&1)<<perm[j] for j in range(5)) for x in range(32)]
  for shift in range(32):
   key=(image[0]^shift,tuple(sorted(image[x]^shift for x in h[1:])),tuple(sorted(image[x]^shift for x in u)))
   assert key not in lookup or lookup[key][0]==i,('overlapping registry',i)
   lookup[key]=(i,perm,shift)
(P/'Q5_T15_RANK_BATCH_REVIEW_certificates.log').write_text('\n'.join(logs)+'\n')
proj=[[sum(((x>>j)&1)<<k for k,j in enumerate(j for j in range(6) if j!=d)) for x in range(64)] for d in range(6)]
def actual(rec,v):
 Z=set(rec[:4]);W=set(rec[4:]);assert len(Z)==4 and len(W)==5 and v not in W and 0 not in Z
 assert all(x<64 and x.bit_count()%2==0 for x in Z) and all(x<64 and x.bit_count()%2 for x in W)
 assert all((x^y).bit_count()!=1 for x in Z for y in W)
 out=[];counts=[]
 for d in range(6):
  za={x for x in Z if (x>>d&1)==(v>>d&1)};wa={x for x in W if (x>>d&1)==(v>>d&1)}
  row=(len(za),len(wa));counts.append(row)
  if row==(3,2):pool=za;minor=Z-za;base=W-wa
  elif row==(1,4):pool=wa-{1<<d};minor=W-wa;base=Z-za
  else:continue
  assert len(minor)==1
  for S in combinations(sorted(pool),2):
   Y={x^(1<<d) for x in S};assert len(Y)==2 and not(Y&({0}|Z|W))
   m=proj[d][next(iter(minor))];major=tuple(sorted(proj[d][x] for x in base|Y));u=tuple(sorted(proj[d][x] for x in Y))
   key=(m,major,u);assert key in lookup,('unlisted actual orbit',rec,v,d,S,key)
   i,perm,shift=lookup[key]
   # Four balanced holes in A, with root case delta handled by accepted transfer.
   assert (row[1] if row==(3,2) else row[0]+1)==2
   out.append(dict(cut=d,row=list(row),sources=list(S),minority=m,majority=list(major),omitted=list(u),orbit_index=i,cube_permutation=list(perm),cube_shift=shift))
 return out,not any(x in ((3,1),(0,4)) for x in counts)
domainreview=load('Q5_T26_RANK_BATCH_REVIEW.json');assert domainreview['verdict']=='PASS'
profile=load('Q5_T15_RANK_profile.json');coverage=load('Q5_T15_RANK_coverage.json')
assert len(profile['records'])==4096
producer_all=defaultdict(list)
for w in profile['witnesses']:producer_all[w['record_id']].append(w)
selected={w['record_id']:w for w in coverage['selected_witnesses']}
assert len(selected)==len(coverage['selected_witnesses'])
def matches(a,w):
 return all(a[k]==w[k] for k in ('cut','row','minority','majority','omitted')) and set(a['sources'])==set(w['sources'])
reports=[];independent=[];perorbit=Counter();hard=set();covered=set();allrec=[];rid=0
for v in (1,7,31):
 n=f'Q5_T26_RANK_BATCH_REVIEW_remaining_v{v}.bin';b=raw(n);assert sha(b)==domainreview['evidence'][n]
 assert b==raw(f'Q5_T26_RANK_batch_remaining_v{v}.bin') and len(b)%9==0
 recs=[b[k:k+9] for k in range(0,len(b),9)];assert len(set(recs))==len(recs)
 remaining=[]
 for index,rec in enumerate(recs):
  found,no17=actual(rec,v);allrec.append((v,rec))
  assert profile['records'][rid]==dict(v=v,input_index=index,record=list(rec),no_T17_cut=no17)
  if no17:hard.add(rid)
  for w in producer_all[rid]:
   assert any(matches(a,w) for a in found),('invalid profile witness',rid,w)
   i=next(a['orbit_index'] for a in found if matches(a,w));g=registry[i]['geometry']
   assert w['canonical_majority']==g['majority'] and w['canonical_omitted']==g['omitted']
  assert {a['orbit_index'] for a in found}=={next(a['orbit_index'] for a in found if matches(a,w)) for w in producer_all[rid]}
  assert bool(found)==(rid in selected)
  if found:
   assert any(matches(a,selected[rid]) for a in found),('invalid selected witness',rid)
   covered.add(rid);perorbit.update(set(a['orbit_index'] for a in found))
   independent.append(dict(record_id=rid,v=v,input_index=index,record=list(rec),**found[0]))
  else:remaining.append(rec)
  rid+=1
 out=b''.join(remaining);assert out==raw(f'Q5_T15_RANK_remaining_v{v}.bin')
 assert set(remaining)==set(recs)-{bytes(w['record']) for w in independent if w['v']==v}
 n=f'Q5_T15_RANK_BATCH_REVIEW_remaining_v{v}.bin';(P/n).write_bytes(out)
 reports.append(dict(v=v,input=len(recs),covered=len(recs)-len(remaining),remaining=len(remaining),remaining_file=n,sha256=sha(out),exact_bytes_and_sets_equal=True))
assert rid==4096 and len(covered)==2346 and len(hard)==462 and hard<=covered
assert set(producer_all)<=set(range(4096)) and set(selected)==covered
# Optional independent exact union of two accepted reviewed subsets, no T17 imported.
t63=load('Q5_T63_RANK_REVIEW.json');assert t63['verdict']=='PASS'
for n,h in t63['audited_input_hashes'].items():assert sha(raw(n))==h
for n,h in t63['evidence'].items():assert sha(raw(n))==h
union=[]
for r in reports:
 v=r['v'];a=raw(r['remaining_file']);n=f'Q5_T63_RANK_REVIEW_remaining_v{v}.bin';b=raw(n)
 aa=[a[k:k+9] for k in range(0,len(a),9)];bb={b[k:k+9] for k in range(0,len(b),9)}
 src=[rec for target,rec in allrec if target==v];assert bb<=set(src)
 c=b''.join(rec for rec in aa if rec in bb)
 n=f'Q5_T15_T63_RANK_UNION_REVIEW_remaining_v{v}.bin';(P/n).write_bytes(c)
 union.append(dict(v=v,input=len(src),T15_covered=r['covered'],T63_covered=len(src)-len(bb),union_covered=len(src)-len(c)//9,remaining=len(c)//9,remaining_file=n,sha256=sha(c)))
result=dict(all_manifest_hashes_and_sizes_match=True,certificates=15,selected_forests=61440,columns_verified=61440,connectivity_bits_verified=251658240,rank_GF2_each=4096,marked_orbit_lookup_size=len(lookup),old_core_alignment=old_alignment,reports=reports,covered=len(covered),remaining=4096-len(covered),no_T17=462,no_T17_all_covered=True,profile_witnesses_checked=sum(map(len,producer_all.values())),selected_witnesses_checked=len(selected),per_orbit_coverage=dict(perorbit),T15_T63_exact_union=union)
(P/'Q5_T15_RANK_BATCH_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'Q5_T15_RANK_BATCH_REVIEW_witnesses.json').write_text(json.dumps(independent,separators=(',',':'))+'\n')
print(json.dumps(result),flush=True)
