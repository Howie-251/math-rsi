from pathlib import Path
from itertools import permutations
import json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent;OUT=ROOT/'formal/Aris4Math/ThirtyFour'
old=json.load(open(HERE.parent/'twentyone-math/FOUR_SEVENS_RESIDUES.json'))['representatives']
five=json.load(open(HERE/'TwentyOneSevenFive77777_REPLAY.json'))
quad=json.load(open(HERE/'TwentyOneSevenQuad7777_REPLAY.json'))
joint_raw=json.load(open(HERE.parent/'twentyone-math/MANY_SEVENS_JOINT.json'))['results']
for i in [0,1,3,4,18,19,20,21,32]:quad.append(joint_raw[i])
# joint replay may wrap its original counts
for i,r in enumerate(quad):
 if isinstance(r,list):assert len(r)==1;quad[i]=r[0]
assert len(five)==10 and len(quad)==61
clean=lambda r:{int(t):v for t,v in r['counts'].items() if v}
ps=list(permutations(range(5)));projs=list(permutations(range(5),4));sigs5={};sigs4={}
for c,r in enumerate(five):
 for pi,p in enumerate(ps):
  mu=clean(r);z={sum(1<<p[i]for i in range(5)if t>>i&1):v for t,v in mu.items()}
  sigs5.setdefault(tuple(sorted(z.items())),(c,pi))
for c,r in enumerate(quad):sigs4[tuple(sorted(clean(r).items()))]=c

def allocations(es,k=0,caps=(7,2,2,2,2)):
 if k==len(es):yield [];return
 t,m=es[k];cost=[1]+[(t>>i)&1 for i in range(4)]
 for v in range(m+1):
  if all(v*a<=b for a,b in zip(cost,caps)):
   for vs in allocations(es,k+1,tuple(b-v*a for a,b in zip(cost,caps))):yield [v]+vs

def code(vs):return sum(v*3**i for i,v in enumerate(vs))
fs=lambda t,n:'{'+','.join(str(i)for i in range(n)if t>>i&1)+'}' if t else '∅'
vec=lambda xs:'!['+','.join(map(str,xs))+']'
records=[];allalloc=[];entries=[];replay=[]
for ri,r in enumerate(old):
 mu=clean(r);es=sorted((t,v)for t,v in mu.items()if t);entries.append(es);alloc=list(allocations(es));allalloc.append(alloc);lookup=[];valid=direct=0
 for vs in alloc:
  lam=[sum(v for (t,_),v in zip(es,vs)if t>>i&1)for i in range(4)];q=7-sum(vs)
  if min(lam)<1 or q>mu[0]:continue
  valid+=1;z=dict(mu)
  for (t,m),v in zip(es,vs):z[t]-=v;z[t|16]=v
  z[0]-=q;z[16]=q;z={t:v for t,v in z.items()if v};sig=tuple(sorted(z.items()))
  if sig in sigs5:
   c,pi=sigs5[sig];lookup.append((code(vs),0,c,pi));direct+=1;continue
  found=False
  for pi,p in enumerate(projs):
   w={}
   for t,v in z.items():
    u=sum(1<<j for j,i in enumerate(p)if t>>i&1);w[u]=w.get(u,0)+v
   sig=tuple(sorted(w.items()))
   if sig in sigs4:lookup.append((code(vs),1,sigs4[sig],pi));found=True;break
  assert found,(ri,vs,z)
 records.append(lookup);replay.append(dict(seed=ri,allocations=len(alloc),valid=valid,strict_five=direct,strict_four=valid-direct))
assert [len(a)for a in allalloc]==[551,278,96,590,578,386,194,366,579]
head='''namespace Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogue
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyFour.LockExtension
open Aris4Math.ThirtyFour.PromotionCatalog
open Aris4Math.ThirtyFour.PromotionReconstruction
open TwentyOneSevenQuadCoverage (Residue residueμ)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 1000
'''
s='''import Aris4Math.ThirtyFour.PromotionReconstruction
import Aris4Math.ThirtyFour.LockProjection
import Aris4Math.ThirtyFour.TwentyOneSevenQuadCoverage
import Aris4Math.ThirtyFour.TwentyOneSevenFive77777
'''+head
s+='def entries : Residue → List (Finset (Fin 4)×ℕ)\n'
for i,es in enumerate(entries):s+=f'  | {i} => ['+','.join(f'({fs(t,4)},{v})'for t,v in es)+']\n'
s+='''def cap : Option (Fin 4) → ℕ | none=>7 | some _=>2
def catalogue (r : Residue) := BoundedAllocations.enumerate cost (entries r) cap
def vector (r : Residue) (values : List ℕ) := BoundedAllocations.decode (entries r) values
def μ (r : Residue) (values : List ℕ) := extend (residueμ r) (vector r values) 7
def Valid (r : Residue) (values : List ℕ) : Prop :=
  (∀ T, fillEmpty (vector r values) 7 T≤residueμ r T) ∧
  (∀ i : Fin 4,1≤∑ T : Finset (Fin 4),if i∈T then vector r values T else 0)
instance (r : Residue) (values : List ℕ) : Decidable (Valid r values) := by unfold Valid;infer_instance
abbrev Perm := Fin 120
abbrev Projection := Fin 120
'''
s+='def permFn : Perm → Fin 5 → Fin 5 := '+vec(vec(p)for p in ps)+'\n'
s+='''theorem permFn_injective : ∀p,Function.Injective (permFn p) := by decide +kernel
noncomputable def perm (p : Perm) : Equiv.Perm (Fin 5) :=
  Equiv.ofBijective (permFn p) ⟨permFn_injective p,Finite.surjective_of_injective (permFn_injective p)⟩
'''
s+='def projectFn : Projection → Fin 4 → Fin 5 := '+vec(vec(p)for p in projs)+'\n'
s+='''theorem projectFn_injective : ∀p,Function.Injective (projectFn p) := by decide +kernel
def project (p : Projection) : Fin 4 ↪ Fin 5 := ⟨projectFn p,projectFn_injective p⟩
abbrev Choice := (Fin 10 × Perm) ⊕ (Fin 61 × Projection)
def choices : Residue → List (ℕ×Choice)
'''
for r,recs in enumerate(records):s+=f'  | {r} => ['+','.join(f'({k},Sum.in{"l" if kind==0 else "r"} ({c},{p}))'for k,kind,c,p in recs)+']\n'
s+='''def code (values : List ℕ) := (values.zipIdx.map (fun p=>p.1*3^p.2)).sum
def choose (r : Residue) (values : List ℕ) : Choice := ((choices r).lookup (code values)).getD (Sum.inl (0,0))
def Matched (r : Residue) (values : List ℕ) : Prop :=
  match choose r values with
  | Sum.inl (c,p) => ∀T,μ r values (T.map (perm p).toEmbedding)=TwentyOneSevenFive77777Data.μ c T
  | Sum.inr (c,p) => ∀T,(∑U : Finset (Fin 5),if LockProjection.project (project p) U=T then μ r values U else 0)=
      TwentyOneSevenQuadCoverage.μ ⟨c.val,by omega⟩ T
noncomputable instance (r : Residue) (values : List ℕ) : Decidable (Matched r values) := by unfold Matched;split <;> infer_instance
'''
chunks=[]
for r,alloc in enumerate(allalloc):
 for i in range(0,len(alloc),70):
  name=f'chunk{r}_{i//70}';ch=alloc[i:i+70];chunks.append((r,name,ch));s+=f'def {name} : List (List ℕ) := '+repr(ch).replace(' ','')+'\n'
(OUT/'TwentyOneSevenManyCatalogueData.lean').write_text(s+'end Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogue\n')
k='import Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogueData\n'+head
for r,alloc in enumerate(allalloc):
 names=[name for rr,name,_ in chunks if rr==r]
 k+=f'theorem catalogue_eq{r} : catalogue {r}='+'++'.join(names)+' := by decide +kernel\n'
for r,name,ch in chunks:k+=f'theorem certificate_{name} : ({name}).all (fun values=>decide (Valid {r} values→Matched {r} values))=true := by decide +kernel\n'
(OUT/'TwentyOneSevenManyCatalogueCertificates.lean').write_text(k+'end Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogue\n')
z='import Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogueCertificates\n'+head
z+='''theorem coverage (r : Residue) (values : List ℕ) (member : values∈catalogue r) (valid : Valid r values) : Matched r values := by
  have all : (catalogue r).all (fun values=>decide (Valid r values→Matched r values))=true := by
    fin_cases r
'''
for r in range(9):
 names=[name for rr,name,_ in chunks if rr==r]
 z+=f'    · change (catalogue {r}).all (fun values=>decide (Valid {r} values→Matched {r} values))=true\n      rw [catalogue_eq{r}]\n      simp only [List.all_append,'+','.join('certificate_'+name for name in names)+',Bool.and_self]\n'
z+='  exact (of_decide_eq_true (List.all_eq_true.mp all values member)) valid\nend Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogue\n'
(OUT/'TwentyOneSevenManyCatalogueKernel.lean').write_text(z)
(HERE/'MANY_CATALOGUE_REPLAY.json').write_text(json.dumps(dict(allocations=sum(len(a)for a in allalloc),families=replay),indent=2)+'\n')
print(replay)
