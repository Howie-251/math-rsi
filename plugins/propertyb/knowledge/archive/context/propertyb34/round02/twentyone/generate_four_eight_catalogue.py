from pathlib import Path
from itertools import permutations
import json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent;OUT=ROOT/'formal/Aris4Math/ThirtyFour'
OLD=ROOT/'context/propertyb34/round01/twentyone-lean'
clean=lambda r:{int(t):int(v) for t,v in r['counts'].items() if v}
old=json.loads((ROOT/'context/propertyb34/round01/twentyone-math/FOUR_SEVENS_RESIDUES.json').read_text())['representatives']
ps=[p+(4,) for p in permutations(range(4))]
sigs={};sizes=[]
for b in range(33):
 name=f'TwentyOneSevenFive77778Batch{b:03d}'
 rows=json.loads(((OLD if b<2 else HERE)/(name+'_REPLAY.json')).read_text());sizes.append(len(rows))
 for i,row in enumerate(rows):
  for pi,p in enumerate(ps):
   mu=clean(row);sig=tuple(sorted((sum(1<<p[j] for j in range(5) if t>>j&1),v) for t,v in mu.items()))
   sigs.setdefault(sig,(0,b,i,pi))
js=[0,1,3,4];joint=json.loads((ROOT/'context/propertyb34/round01/twentyone-math/FOUR_SEVEN_EXTEND_JOINT.json').read_text())['results']
for c,index in enumerate(js):
 for pi,p in enumerate(ps):
  mu=clean(joint[index]);sig=tuple(sorted((sum(1<<p[j] for j in range(5) if t>>j&1),v) for t,v in mu.items()))
  sigs.setdefault(sig,(1,c,0,pi))
assert sum(sizes)==522
vec=lambda xs:'!['+','.join(xs)+']'
ns='Aris4Math.ThirtyFour.TwentyOneSevenFourCertificates'
s=''.join(f'import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch{b:03d}Data\n' for b in range(33))
s+=''.join(f'import Aris4Math.ThirtyFour.TwentyOneSevenJointFourEight{i}Data\n' for i in js)
s+=f'namespace {ns}\nset_option maxRecDepth 100000\nabbrev Choice := (Fin 33 × Fin 16) ⊕ Fin 4\n'
expr=[]
for b,size in enumerate(sizes):
 idx='i' if size==16 else f'⟨i.val%{size},Nat.mod_lt _ (by decide)⟩'
 expr.append(f'fun i => TwentyOneSevenFive77778Batch{b:03d}Data.μ {idx}')
s+='def pureμ : Fin 33 → Fin 16 → Finset (Fin 5) → ℕ := '+vec(expr)+'\n'
s+='def jointμ : Fin 4 → Finset (Fin 5) → ℕ := '+vec(f'TwentyOneSevenJointFourEight{i}Data.μ' for i in js)+'\n'
s+='def counts (c : Choice) : Finset (Fin 5) → ℕ := match c with\n  | Sum.inl bi => pureμ bi.1 bi.2\n  | Sum.inr j => jointμ j\nend '+ns+'\n'
(OUT/'TwentyOneSevenFourCertificatesData.lean').write_text(s)
s=''.join(f'import Aris4Math.ThirtyFour.TwentyOneSevenFive77778Batch{b:03d}\n' for b in range(33))
s+=''.join(f'import Aris4Math.ThirtyFour.TwentyOneSevenJointFourEight{i}\n' for i in js)
s+='import Aris4Math.ThirtyFour.TwentyOneSevenFourCertificatesData\nnamespace '+ns+'\nopen Aris4Math.ThirtyThree.MultiLockRecovery\nset_option maxRecDepth 100000\n'
s+='''theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (f : Fin 5 ↪ Fin 21)
    (c : Choice) (actual : ∀ T, count H f T=counts c T) : PropertyB H := by
  rcases c with ⟨b,i⟩|j
  · fin_cases b
'''
for b,size in enumerate(sizes):
 idx='i' if size==16 else f'⟨i.val%{size},Nat.mod_lt _ (by decide)⟩'
 s+=f'    · exact TwentyOneSevenFive77778Batch{b:03d}.propertyB_of_counts H f {idx} actual\n'
s+='  · fin_cases j\n'
for i in js:s+=f'    · exact TwentyOneSevenJointFourEight{i}.propertyB_of_counts H f actual\n'
s+='end '+ns+'\n#print axioms '+ns+'.propertyB_of_counts\n'
(OUT/'TwentyOneSevenFourCertificates.lean').write_text(s)

def allocations(es,k=0,caps=(8,2,2,2,2)):
 if k==len(es):yield [];return
 t,m=es[k];cost=[1]+[(t>>i)&1 for i in range(4)]
 for v in range(m+1):
  if all(v*a<=b for a,b in zip(cost,caps)):
   for vs in allocations(es,k+1,tuple(b-v*a for a,b in zip(cost,caps))):yield [v]+vs
rows=[];stats=[]
for r,row in enumerate(old):
 mu=clean(row);es=sorted((t,v) for t,v in mu.items() if t);rr=[];valid=0
 for values in allocations(es):
  lam=[sum(v for (t,_),v in zip(es,values) if t>>i&1) for i in range(4)];q=8-sum(values)
  choice=(0,0,0,0)
  if min(lam)>=1 and q<=mu[0]:
   valid+=1;z=dict(mu)
   for (t,m),v in zip(es,values):z[t]-=v;z[t|16]=v
   z[0]-=q;z[16]=q;sig=tuple(sorted((t,v) for t,v in z.items() if v))
   assert sig in sigs,(r,values,z)
   choice=sigs[sig]
  rr.append((values,choice))
 rows.append(rr);stats.append(dict(residue=r,total=len(rr),valid=valid))
assert [s['valid'] for s in stats]==[315,134,32,339,332,206,89,209,344]
head='''namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open scoped BigOperators
open TwentyOneSevenQuadCoverage (Residue)
open TwentyOneSevenFourActualCore (catalogue μ Valid)
open TwentyOneSevenFourCertificates (Choice counts)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
abbrev Perm := TwentyOneSevenQuadCoverage.Perm
noncomputable def perm (p : Perm) := LockLiftRelabel.lift (TwentyOneSevenQuadCoverage.perm p)
abbrev Row := List ℕ × Choice × Perm
def Matched (r : Residue) (values : List ℕ) (c : Choice) (p : Perm) : Prop :=
  ∀ T, μ r values (T.map (perm p).toEmbedding)=counts c T
noncomputable instance (r : Residue) (values : List ℕ) (c : Choice) (p : Perm) :
    Decidable (Matched r values c p) := by unfold Matched;infer_instance
'''
s='import Aris4Math.ThirtyFour.TwentyOneSevenFourActualCore\nimport Aris4Math.ThirtyFour.TwentyOneSevenFourCertificatesData\n'+head
for r,rr in enumerate(rows):
 terms=[]
 for vals,(kind,b,i,p) in rr:
  c=f'Sum.inl ({b},{i})' if kind==0 else f'Sum.inr {b}'
  terms.append('('+repr(vals).replace(' ','')+f',{c},{p})')
 s+=f'def rows{r} : List Row := ['+','.join(terms)+']\n'
s+='end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue\n'
(OUT/'TwentyOneSevenFourCatalogueData.lean').write_text(s)
# Each residue's finite certificate caches independently.
for r,rr in enumerate(rows):
 s='import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData\nnamespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue\nopen TwentyOneSevenFourActualCore (catalogue Valid)\nset_option maxHeartbeats 0\nset_option maxRecDepth 100000\n'
 s+=f'theorem rows_eq{r} : rows{r}.map Prod.fst = catalogue {r} := by decide +kernel\n'
 s+=f'theorem rows_checked{r} : rows{r}.all (fun row => decide (Valid {r} row.1 → Matched {r} row.1 row.2.1 row.2.2))=true := by decide +kernel\n'
 s+='end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue\n'
 (OUT/f'TwentyOneSevenFourCatalogueChecked{r}.lean').write_text(s)
s=''.join(f'import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueChecked{r}\n' for r in range(9))
s+='''namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenQuadCoverage (Residue)
open TwentyOneSevenFourActualCore (catalogue Valid)
open TwentyOneSevenFourCertificates (Choice)
theorem coverage (r : Residue) (values : List ℕ) (member : values∈catalogue r)
    (valid : Valid r values) : ∃ c : Choice, ∃ p : Perm, Matched r values c p := by
  fin_cases r
'''
for r in range(9):
 s+=f'''  · rw [← rows_eq{r}] at member
    obtain ⟨row,mem,eq⟩ := List.mem_map.mp member
    refine ⟨row.2.1,row.2.2,?_⟩
    have h := of_decide_eq_true (List.all_eq_true.mp rows_checked{r} row mem)
    simpa only [eq] using h (by simpa only [eq] using valid)
'''
s+='end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue\n'
(OUT/'TwentyOneSevenFourCatalogueKernel.lean').write_text(s)
s='''import Aris4Math.ThirtyFour.TwentyOneSevenFourCertificates
import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueKernel
namespace Aris4Math.ThirtyFour.TwentyOneSevenFour
open Aris4Math.ThirtyThree.MultiLockRecovery

theorem propertyB_of_four_sevens (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34)
    (minimum : ∀ x, 7≤H.degree x)
    (four : (TwentyOneSevenSelection.sevens H).card=4) : PropertyB H := by
  apply TwentyOneSevenFourActualCore.propertyB_of_four_sevens H cover size minimum four
  intro r values member valid g actual
  obtain ⟨c,p,matched⟩ := TwentyOneSevenFourCatalogue.coverage r values member valid
  apply TwentyOneSevenFourCertificates.propertyB_of_counts H
    ((TwentyOneSevenFourCatalogue.perm p).toEmbedding.trans g) c
  intro T
  rw [LockRelabel.count_comp_perm,actual]
  exact matched T
end Aris4Math.ThirtyFour.TwentyOneSevenFour
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenFour.propertyB_of_four_sevens
'''
(OUT/'TwentyOneSevenFour.lean').write_text(s)
(HERE/'FOUR_EIGHT_CATALOGUE_REPLAY.json').write_text(json.dumps(dict(pure_representatives=sum(sizes),joint_representatives=4,rows=stats),indent=2)+'\n')
print(stats)
