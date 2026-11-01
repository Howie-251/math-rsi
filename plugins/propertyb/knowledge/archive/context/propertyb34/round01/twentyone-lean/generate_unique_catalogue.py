from pathlib import Path
from itertools import combinations,permutations
import json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
high=[t for t in range(32) if t.bit_count()>=3];pairs=[(1<<i)|(1<<j) for i,j in combinations(range(5),2)]
def enum(k,cap):
 if k==len(high):yield [];return
 cost=[int(high[k]&p==p) for p in pairs]
 for a in range(3):
  if all(a*c<=b for c,b in zip(cost,cap)):
   for rest in enum(k+1,[b-a*c for c,b in zip(cost,cap)]):yield [a]+rest
alloc=list(enum(0,[2]*10));assert len(alloc)==925
pure=[]
for b in range(3):pure+=json.load(open(HERE/f'TwentyOneSevenSix788888Batch{b:03d}_REPLAY.json'))
joint=json.load(open(ROOT/'context/propertyb34/round01/twentyone-math/UNIQUE_SEVEN_SIX_JOINT.json'))['results'][0]
mus=[{int(t):v for t,v in row['counts'].items() if v} for row in pure+[joint]]
ps=[(5,)+p for p in permutations(range(5))]
projs=[(5,)+p for p in permutations(range(5),4)]
strict={}
for c,mu in enumerate(mus):
 for pi,p in enumerate(ps):
  out={sum(1<<p[j] for j in range(6) if t>>j&1):v for t,v in mu.items()}
  strict.setdefault(tuple(sorted(out.items())),(c,pi))
jraw=json.load(open(ROOT/'context/propertyb34/round01/twentyone-math/SEVEN_UNIT_FIVE_STRICT_JOINT.json'))['results']
jmus=[{int(t):v for t,v in jraw[k]['counts'].items() if v} for k in [0,2]]
def recover5(vs):
 mu=dict(zip(high,vs))
 for t in pairs:mu[t]=2-sum(v for u,v in mu.items() if u.bit_count()>=3 and u&t==t)
 for i in range(5):mu[1<<i]=8-sum(v for u,v in mu.items() if u.bit_count()>=2 and u>>i&1)
 mu[0]=34-sum(mu.values())
 return mu
prom={0:4,3:1,12:1,16:1};lookup={};valid=0;projected=0
for vs in alloc:
 mu=recover5(vs)
 if any(mu[t]<p for t,p in prom.items()):continue
 valid+=1
 out={}
 for t,n in mu.items():
  p=prom.get(t,0)
  if n-p:out[t]=n-p
  if p:out[t|32]=p
 key=sum(a*3**i for i,a in enumerate(vs))
 sig=tuple(sorted(out.items()))
 if sig in strict:
  c,pi=strict[sig];lookup[key]=(0,c,pi);continue
 for pi,p in enumerate(projs):
  projectedMu={}
  for t,n in out.items():
   u=sum(1<<j for j,i in enumerate(p) if t>>i&1);projectedMu[u]=projectedMu.get(u,0)+n
  for c,jmu in enumerate(jmus):
   if projectedMu==jmu:lookup[key]=(1,c,pi);break
  if key in lookup:break
 assert key in lookup,(vs,out)
 projected+=1
assert valid==316,(valid,projected)
print('925 allocations;',valid,'valid;',projected,'strict via five-point projection')
vec=lambda xs:'!['+','.join(map(str,xs))+']'
fs=lambda t,n:'{'+','.join(str(i) for i in range(n) if t>>i&1)+'}' if t else '∅'
s='''import Aris4Math.ThirtyFour.ActualAllocations
import Aris4Math.ThirtyFour.PromotionReconstruction
import Aris4Math.ThirtyFour.TwentyOneSevenSix788888Batch000
import Aris4Math.ThirtyFour.TwentyOneSevenSix788888Batch001
import Aris4Math.ThirtyFour.TwentyOneSevenSix788888Batch002
import Aris4Math.ThirtyFour.TwentyOneSevenJointUniqueSix0
import Aris4Math.ThirtyFour.TwentyOneSevenJointUnitFive0
import Aris4Math.ThirtyFour.TwentyOneSevenJointUnitFive2
namespace Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogue
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''
s+='def entries : List (Finset (Fin 5)×ℕ):=['+','.join(f'({fs(t,5)},2)' for t in high)+']\n'
s+='theorem entries_nodup : (entries.map Prod.fst).Nodup := by decide +kernel\n'
s+='def pair : Fin 10→Finset (Fin 5):='+vec(fs(t,5) for t in pairs)+'\n'
s+='''def catalogue : List (List ℕ):=BoundedAllocations.enumerate
  (fun T j=>ActualAllocations.cost (pair j) T) entries (fun _=>2)
def high (values : List ℕ) (T : Finset (Fin 5)) : ℕ:=BoundedAllocations.decode entries values T
def low (T : Finset (Fin 5)) : ℕ:=if T=∅ then 34 else if T.card=1 then 8 else 2
def oldμ (values : List ℕ) : Finset (Fin 5)→ℕ:=recovered low (high values)
def promotion (T : Finset (Fin 5)) : ℕ:=if T={0,1} ∨ T={2,3} ∨ T={4} then 1 else 0
def μ (values : List ℕ) : Finset (Fin 6)→ℕ:=PromotionReconstruction.extend (oldμ values) promotion 7
def Valid (values : List ℕ) : Prop:=∀T,PromotionReconstruction.fillEmpty promotion 7 T≤oldμ values T
instance (values : List ℕ) : Decidable (Valid values):=by unfold Valid;infer_instance
abbrev Case:=Fin 40
abbrev Perm:=Fin 120
abbrev Projection:=Fin 120
'''
s+='def permFn : Perm→Fin 6→Fin 6:='+vec(vec(p) for p in ps)+'\n'
s+='''theorem permFn_injective : ∀p,Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 6):=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
'''
s+='def projectFn : Projection→Fin 5→Fin 6:='+vec(vec(p) for p in projs)+'\n'
s+='''theorem projectFn_injective : ∀p,Function.Injective (projectFn p) := by decide +kernel
def project (p : Projection) : Fin 5↪Fin 6:=⟨projectFn p,projectFn_injective p⟩
def targetμ (c : Case) (T : Finset (Fin 6)) : ℕ:=
  if h:c.val<16 then TwentyOneSevenSix788888Batch000Data.μ ⟨c.val,h⟩ T
  else if h:c.val<32 then TwentyOneSevenSix788888Batch001Data.μ ⟨c.val-16,by omega⟩ T
  else if h:c.val<39 then TwentyOneSevenSix788888Batch002Data.μ ⟨c.val-32,by omega⟩ T
  else TwentyOneSevenJointUniqueSix0Data.μ T
def targetFive (c : Fin 2) (T : Finset (Fin 5)) : ℕ:=
  if c=0 then TwentyOneSevenJointUnitFive0Data.μ T else TwentyOneSevenJointUnitFive2Data.μ T
abbrev Choice:=(Case×Perm)⊕(Fin 2×Projection)
'''
s+='def choices : List (ℕ×Choice):=['+','.join(f'({k},Sum.in{"l" if kind==0 else "r"} ({c},{pi}))' for k,(kind,c,pi) in sorted(lookup.items()))+']\n'
s+='def choose (k : ℕ) : Choice:=(choices.lookup k).getD (Sum.inl (0,0))\n'
s+='''def code (values : List ℕ) : ℕ:=(values.zipIdx.map (fun p=>p.1*3^p.2)).sum
def Matched (values : List ℕ) : Prop:=
  match choose (code values) with
  | Sum.inl (c,p) => ∀T,μ values (T.map (perm p).toEmbedding)=targetμ c T
  | Sum.inr (c,p) => ∀T,(∑U : Finset (Fin 6),
      if LockProjection.project (project p) U=T then μ values U else 0)=targetFive c T
noncomputable instance (values : List ℕ) : Decidable (Matched values):=by unfold Matched;split <;> infer_instance
'''
chunks=[alloc[k:k+100] for k in range(0,len(alloc),100)]
for i,ch in enumerate(chunks):s+=f'def chunk{i} : List (List ℕ):='+repr(ch).replace(' ','')+'\n'
s+='theorem catalogue_eq : catalogue='+'++'.join(f'chunk{i}' for i in range(len(chunks)))+' := by decide +kernel\n'
for i in range(len(chunks)):
 s+=f'theorem certificate{i} : ∀values∈chunk{i},Valid values→Matched values := by decide +kernel\n'
expr='certificate0'
for i in range(1,len(chunks)):expr=f'List.forall_mem_append.mpr ⟨{expr}, certificate{i}⟩'
s+='''theorem coverage (values : List ℕ) (mem : values∈catalogue) (valid : Valid values) : Matched values := by
  have covered : ∀xs∈catalogue,Valid xs→Matched xs := by
    rw [catalogue_eq]
    exact '''+expr+'''
  exact covered values mem valid
'''
s+='end Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogue\n'
out=ROOT/'formal/Aris4Math/ThirtyFour'
cut=s.index('theorem catalogue_eq')
(out/'TwentyOneSevenUniqueCatalogueData.lean').write_text(s[:cut]+'end Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogue\n')
header='namespace Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogue\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
cover=s.index('theorem coverage')
(out/'TwentyOneSevenUniqueCatalogueCertificates.lean').write_text('import Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogueData\n'+header+s[cut:cover]+'end Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogue\n')
(out/'TwentyOneSevenUniqueCatalogueKernel.lean').write_text('import Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogueCertificates\n'+header+s[cover:])
(out/'TwentyOneSevenUniqueCatalogue.lean').write_text('import Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogueKernel\n')
(HERE/'UNIQUE_CATALOGUE_REPLAY.json').write_text(json.dumps(dict(allocations=len(alloc),valid=valid,strict_six=valid-projected,strict_five=projected,strict_six_representatives=len(mus),chunks=list(map(len,chunks))),indent=2)+'\n')
