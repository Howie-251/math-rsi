"""Rebuild marked theorem registries from hash-bound statements, not producer lookup code."""
import pathlib,json,hashlib,itertools,re
R=pathlib.Path(__file__).resolve().parent
def load(p):return json.loads((R/p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
def mask(a):return sum(1<<x for x in a)
def nums(s):return tuple(map(int,s.replace('$','').split(',')))
def tables(name):
 for line in (R/name).read_text().splitlines():
  if line.startswith('|'):
   t=[x.strip() for x in line.strip('|').split('|')]
   if t[0].isdigit():yield t
def swap(x,i):return x^(3<<i) if ((x>>i)^(x>>(i+1)))&1 else x
def orb(seed):
 seen={seed};todo=[seed]
 while todo:
  t=todo.pop()
  for i in range(4):
   u=tuple(tuple(sorted(swap(x,i) for x in a)) for a in t)
   if u not in seen:seen.add(u);todo.append(u)
 return seen
m=load('HIGHER_Q5_FULL_REUSE_MANIFEST.json')
assert sha('HIGHER_Q5_FULL_REUSE_MANIFEST.json')=='cce6d2f5c216f141143292838a4a1d818a3f54b068720e50d0d071588cb96d13'
for p,h in m['hashes'].items():assert sha(p)==h and (R/p).stat().st_size==m['sizes'][p],p
bindings={};reviews=['Q5_T26_RANK_BATCH_REVIEW.json','Q5_T15_RANK_BATCH_REVIEW.json','Q5_T17_RANK_BATCH_REVIEW.json','Q5_T63_RANK_REVIEW.json','Q5_T63_COMPLETE_SPLIT_REVIEW.json','TEN_HOLE_COVERED_PARTIAL_REVIEW.json','T44_Q5_CLOSURE_REVIEW.json','Q5_A10_FULL_REVIEW.json','TEN_HOLE_FULL_REVIEW.json','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json']
for p in reviews:assert load(p)['verdict']=='PASS'
proofs=['Q5_T26_RANK_BATCH_PROOF.md','Q5_T15_RANK_BATCH_PROOF.md','Q5_T17_RANK_BATCH_PROOF.md','Q5_T63_RANK_PROOF.md']
summaries=['Q5_T26_RANK_batch_summary.json','Q5_T15_RANK_batch_summary.json','Q5_T17_RANK_batch_summary.json','Q5_T63_RANK_batch_summary.json']
for rev in reviews:
 for k in ('audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes','evidence'):
  for p,h in load(rev).get(k,{}).items():
   if p in proofs+summaries+['TEN_HOLE_COVERED_PARTIAL_REVIEW_lookup.txt','TEN_HOLE_FREE_REVIEW_imports.json'] and isinstance(h,str):
    assert sha(p)==h.removeprefix('sha256:'),(rev,p);bindings[p]=sha(p)
assert all(p in bindings for p in proofs+summaries)
g26=[(nums(t[1]),nums(t[2]),nums(t[3])) for t in tables(proofs[0]) if len(t)==6]
g15=[((0,),nums(t[1]),nums(t[2])) for t in tables(proofs[1]) if len(t)==5]
g17=[((0,),nums(t[1]),nums(t[2])) for t in tables(proofs[2]) if t[3]=='none']
g63=[(nums(t[1]),nums(t[2])) for t in tables(proofs[3]) if len(t)==3]
assert list(map(len,(g26,g15,g17,g63)))==[55,15,10,7]
for gs,name,key in zip((g26,g15,g17),summaries[:3],('reports','reports','orbits')):
 actual=[]
 for row in load(name)[key]:
  assert row['full_rank'];g=row.get('geometry',row.get('marked_geometry'))
  if name==summaries[2]:assert g['forced_cherry_pair'] is None
  actual.append(tuple(tuple(g[a]) for a in ('minority','majority','omitted')))
 assert set(actual)==set(gs)
assert set(g63)=={(tuple(r['geometry']['holes']),tuple(r['geometry']['omitted'])) for r in load(summaries[3])['reports']}
fixed=load('TEN_HOLE_FREE_REVIEW_imports.json')
for p,h in fixed['hashes'].items():assert sha(p)==h.removeprefix('sha256:');bindings[p]=sha(p)
ids=(0,1,2,4,5,7,8,10,13,14,15,18,19,21,23,24,25,27,31,32,35,37,38,44)
old=set()
for i in ids:
 row=fixed['complete_core_registry'][str(i)];assert load(row['review'])['verdict']=='PASS'
 om=tuple(row['omitted']);inc=tuple(x for x in row['holes'] if x and x not in om)
 for a,b in orb((om,inc)):old.add(mask(a)|(mask(b)<<32))
corelen=len(old);odd=tuple(x for x in range(32) if x.bit_count()%2)
split=set()
for J in itertools.combinations(odd,5):
 for O in itertools.combinations(J,2):
  if any(sum(x>>d&1 for x in J)==2 and sum(x>>d&1 for x in O)==1 for d in range(5)):
   split.add(mask(O)|(mask(set(J)-set(O))<<32))
old|=split
assert old==set(map(int,(R/'TEN_HOLE_COVERED_PARTIAL_REVIEW_lookup.txt').read_text().split()))
reg26=set();reg15={(0,(k>>32)|(k&0xffffffff),k&0xffffffff) for k in old};reg17=set();reg63=set()
for M,J,O in g26:
 for shift in M:
  seed=tuple(tuple(sorted(x^shift for x in a)) for a in (M,J,O))
  for a,b,c in orb(seed):reg26.add((mask(a),mask(b),mask(c)))
for gs,reg in [(g15,reg15),(g17,reg17)]:
 for M,J,O in gs:
  assert M==(0,)
  for a,b in orb((J,O)):reg.add((0,mask(a),mask(b)))
for H,O in g63:
 for a,b in orb((H,O)):
  for shift in range(32):reg63.add((0,mask(x^shift for x in a),mask(x^shift for x in b)))
oi={x:i for i,x in enumerate(odd)}
packed26=set()
for M,J,O in reg26:
 delta=(M^1).bit_length()-1
 jm=sum(1<<oi[x] for x in odd if J>>x&1);om=sum(1<<oi[x] for x in odd if O>>x&1)
 packed26.add(delta|(jm<<5)|(om<<21))
for n,reg,packed in [('T26',reg26,packed26),('T15',reg15,{O|((J&~O)<<32) for M,J,O in reg15}),('T17',reg17,{O|((J&~O)<<32) for M,J,O in reg17}),('T63',reg63,{J|(O<<32) for M,J,O in reg63})]:
 assert packed==set(map(int,(R/f'HIGHER_Q5_FULL_{n}_lookup.txt').read_text().split())),n
 (R/f'HIGHER_Q5_FULL_REUSE_REVIEW_{n}.txt').write_text(''.join(f'{M} {J} {O}\n' for M,J,O in sorted(reg)))
out={'status':'PASS','frozen_files_checked':len(m['hashes']),'bound_imports':bindings,'statement_rows':{'T26':55,'T15':15,'T17_unforced':10,'T63':7},'old_core_images':corelen,'old_split_images':len(split),'old_union':len(old),'lookup_exact_sets':{'T26':len(reg26),'T15':len(reg15),'T17':len(reg17),'T63':len(reg63)},'forced_T17_used':False}
(R/'HIGHER_Q5_FULL_REUSE_REVIEW_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='bound_imports'},indent=2))
