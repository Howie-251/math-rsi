"""Independent full/reduced forest and GF(2) audit for nine frozen local rows."""
import collections,json,pathlib
R=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
class DS:
 def __init__(self):self.p=list(range(32))
 def root(self,x):
  while x!=self.p[x]:self.p[x]=self.p[self.p[x]];x=self.p[x]
  return x
 def add(self,a,b):
  a=self.root(a);b=self.root(b)
  if a==b:return False
  self.p[a]=b;return True
def records(n,size,count):
 raw=(R/n).read_bytes();assert len(raw)==size*count,n
 return [raw[j:j+size] for j in range(0,len(raw),size)]
def pairs(raw,K):
 out=[tuple(sorted(raw[j:j+2])) for j in range(0,len(raw),2)]
 assert len(out)*2==len(K) and {x for e in out for x in e}==K and all(a!=b for a,b in out)
 return tuple(sorted(out))
out=[];totalbits=0
for row in read('FOURTEEN_FORCED_candidate_classes.json')['classes']:
 i=row['index'];g=row['geometry'];H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H
 cherries=[]
 for h in sorted(H-U):
  ns={h^(1<<d) for d in range(5)}-U
  if len(ns)==2 and ns<=K:cherries.append((h,*sorted(ns)))
 forced=tuple(sorted((a,b) for h,a,b in cherries));assert forced==tuple(sorted(tuple(p) for p in row['forced_pairs']))
 assert len({x for e in forced for x in e})==2*len(forced)
 Km=K-{x for e in forced for x in e};N=len(Km);rank=1<<(N//2-1)
 assert len(K)==20 and N==row['reduced_endpoints'] and rank==row['target_rank']
 prefix=f'FOURTEEN_FORCED_orbit_{i:03d}' if forced else row['source_prefix']
 cfg=list(map(int,(R/(prefix+'_config.txt')).read_text().split()));assert cfg==sorted(H)+g['omitted']
 deg={x:0 if x in U else 2 if x in H else 1 for x in range(32)};E=sum(deg.values())//2
 fs=records(prefix+'_forests.bin',E*2,rank)
 reduced=records(prefix+'_pairs.bin',N,rank);cols=records(prefix+'_columns.bin',N,rank)
 full=records(prefix+'_full_pairs.bin',20,rank) if forced else reduced
 derived=[];column=[]
 for j,raw in enumerate(fs):
  ds=DS();got=collections.Counter();edges=set()
  for at in range(0,len(raw),2):
   a,b=raw[at:at+2];assert a<32 and b<32 and (a^b).bit_count()==1 and tuple(sorted((a,b))) not in edges
   edges.add(tuple(sorted((a,b))));got[a]+=1;got[b]+=1;assert ds.add(a,b)
  assert all(got[x]==deg[x] for x in range(32))
  groups=collections.defaultdict(list)
  for x in K:groups[ds.root(x)].append(x)
  assert all(len(xs)==2 for xs in groups.values())
  actual=tuple(sorted(tuple(sorted(xs)) for xs in groups.values()));assert actual==pairs(full[j],K)
  assert set(forced)<=set(actual)
  for h,a,b in cherries:assert tuple(sorted((h,a))) in edges and tuple(sorted((h,b))) in edges
  minus=tuple(p for p in actual if p not in forced);assert minus==pairs(reduced[j],Km)
  derived.append(minus);column.append(pairs(cols[j],Km))
 mat=records(prefix+'_matrix.bin',rank//8,rank);rebuilt=[]
 for j,ps in enumerate(derived):
  bits=0
  for k,cs in enumerate(column):
   ds=DS()
   for a,b in ps+cs:ds.add(a,b)
   if len({ds.root(x) for x in Km})==1:bits|=1<<k
  assert bits==int.from_bytes(mat[j],'little'),(i,j)
  rebuilt.append(bits)
 basis={}
 for bits in rebuilt:
  while bits:
   pivot=bits.bit_length()-1
   if pivot not in basis:basis[pivot]=bits;break
   bits^=basis[pivot]
 assert len(basis)==rank
 # Check supplied pivot equations in addition to the independently computed rank.
 pp=records(prefix+'_pivots.bin',rank//8,rank);cc=records(prefix+'_combos.bin',rank//8,rank)
 for j in range(rank):
  expected=int.from_bytes(pp[j],'little');combo=int.from_bytes(cc[j],'little');actual=0
  while combo:
   b=combo&-combo;actual^=rebuilt[b.bit_length()-1];combo-=b
  assert actual==expected and expected.bit_length()==j+1
 totalbits+=rank*rank
 out.append({'index':i,'forced_cherries':[list(x) for x in cherries],'full_endpoints':20,'reduced_endpoints':N,'forests_checked':rank,'all_connectivity_bits_recomputed':rank*rank,'independent_rank_GF2':len(basis),'all_pivot_combination_equations_verified':True})
result={'status':'PASS','rows':out,'local_inputs':len(out),'forests':sum(x['forests_checked'] for x in out),'connectivity_bits':totalbits,'universal_forced_cherries_proved_by_exact_two_available_short_neighbors':True,'producer_rank_or_pivot_used_as_rank_oracle':False}
assert len(out)==9
(R/'FOURTEEN_FORCED_REVIEW_local.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
