from pathlib import Path
from itertools import permutations
ROOT=Path(__file__).resolve().parents[4]
v=lambda xs:'!['+','.join(map(str,xs))+']'
ps=list(permutations(range(4)))
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)];highs=[(0,1,2),(0,1,3),(0,2,3),(1,2,3),(0,1,2,3)]
s=(ROOT/'formal/Aris4Math/ThirtyFour/TwentySevenOneClassification.lean').read_text()
s=s.replace('TwentySevenOne','TwentyEight')
s=s.replace('def permFn : Fin 6 → Fin 4 → Fin 4 := '+s.split('def permFn : Fin 6 → Fin 4 → Fin 4 := ')[1].split('\n')[0], 'def permFn : Fin 24 → Fin 4 → Fin 4 := '+v(v(p) for p in ps))
s=s.replace('p : Fin 6','p : Fin 24')
for name,base in [('coIndex',pairs),('highIndex',highs)]:
 start=s.index(f'def {name}');end=s.index('\n',start)
 rows=[v(base.index(tuple(sorted(p[x] for x in q))) for q in base) for p in ps]
 s=s[:start]+f'def {name} : Fin 24 → Fin {len(base)} → Fin {len(base)} := '+v(rows)+s[end:]
start=s.index('def Residue');end=s.index('def TripleSuitable',start)
s=s[:start]+'''def shapes : Fin 5 → Fin 6 → ℕ :=
  ![![2,2,2,2,2,2],![1,2,2,2,2,2],![1,2,2,1,2,1],![1,1,1,2,2,2],![1,2,1,1,2,1]]
def quadOf : Fin 5 → ℕ := ![0,0,0,0,1]
def SmallResidue (co : Fin 6 → ℕ) (q : ℕ) : Prop :=
  ∃ p : Fin 24, ∃ i : Fin 5, (∀ j, co (coIndex p j)=shapes i j) ∧ q=quadOf i
instance (co : Fin 6 → ℕ) (q : ℕ) : Decidable (SmallResidue co q) := by unfold SmallResidue; infer_instance
def Residue (co : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Prop :=
  ((∃ j, co j=3) ∧ ∀ j, h j=0) ∨ SmallResidue co (h 4)
instance (co : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Decidable (Residue co h) := by unfold Residue; infer_instance

''' +s[end:]
s=s.replace('Suitable true', 'Suitable false').replace('Fin 6 → Fin 2','Fin 6 → Fin 3').replace('Fin 5 → Fin 3','Fin 5 → Fin 4')
s=s.replace('H.degree (f 0)=7','H.degree (f 0)=8').replace('true d0','false d0')
s=s.replace('≤ 2)', '≤ 3)')
s=s.replace('  have bounded := ThirtyThree.TwentyTwoQuadAssembly.high_le_two H f (fun j => (hc j).2)', '''  have bounded : ∀ i : Fin 5, count H f (highLabels i) ≤ 3 := by
    have choose : ∀ i : Fin 5, ∃ j : Fin 6, first j ∈ highLabels i ∧ second j ∈ highLabels i := by decide +kernel
    intro i
    obtain ⟨j,hj1,hj2⟩ := choose i
    exact (ThirtyThree.TwentyTwoQuadAssembly.count_le_codegree H f (highLabels i) (first j) (second j) hj1 hj2).trans (hc j).2''')
# Actual Fin-valued codegree variables must agree with the enlarged domain.
s=s.replace('let co : Fin 6 → Fin 3', 'let co : Fin 6 → Fin 3')
(ROOT/'formal/Aris4Math/ThirtyFour/TwentyEightClassification.lean').write_text(s)
# Canonicalize the six pair counts before the high-trace classification.
from itertools import product
ci=[[pairs.index(tuple(sorted(p[x] for x in q))) for q in pairs] for p in ps]
canonical=sorted(set(min(tuple(co[j] for j in perm) for perm in ci) for co in product(range(1,4),repeat=6)))
assert len(canonical)==66
start=s.index('set_option maxHeartbeats 0 in\ntheorem coverage')
end=s.index('theorem codegree_perm',start)
choices=[]
for code in range(729):
 co=tuple(1+code//3**j%3 for j in range(6))
 candidates=[tuple(co[j] for j in perm) for perm in ci]
 row=min(candidates)
 choices.append((candidates.index(row),canonical.index(row)))
coverage='''def canonicalCo : Fin 66 → Fin 6 → ℕ := '''+v(v(c) for c in canonical)+'''
def coNumber (co : Fin 6 → Fin 3) : Fin 729 :=
  ⟨(co 0).val+3*(co 1).val+9*(co 2).val+27*(co 3).val+81*(co 4).val+243*(co 5).val,by omega⟩
def canonicalPerm : Fin 729 → Fin 24 := '''+v(p for p,i in choices)+'''
def canonicalCase : Fin 729 → Fin 66 := '''+v(i for p,i in choices)+'''
set_option maxHeartbeats 0 in
theorem canonical_choice : ∀ co : Fin 6 → Fin 3, ∀ j,
    (co (coIndex (canonicalPerm (coNumber co)) j)).val+1=canonicalCo (canonicalCase (coNumber co)) j := by decide +kernel

theorem canonical_complete (co : Fin 6 → Fin 3) : ∃ p : Fin 24, ∃ i : Fin 66,
    ∀ j, (co (coIndex p j)).val+1=canonicalCo i j :=
  ⟨canonicalPerm (coNumber co),canonicalCase (coNumber co),canonical_choice co⟩

theorem canonical_bounds : ∀ i j, 1 ≤ canonicalCo i j ∧ canonicalCo i j ≤ 3 := by decide +kernel

set_option maxHeartbeats 0 in
theorem coverage : ∀ i : Fin 66, ∀ h : Fin 5 → Fin 4,
    (∀ j, highPairSum (fun z => (h z).val) j ≤ canonicalCo i j) →
    Residue (canonicalCo i) (fun j => (h j).val) ∨
      TripleSuitable (canonicalCo i) (fun j => (h j).val) ∨
      QuadSuitable (canonicalCo i) (fun j => (h j).val) := by
  intro i
  fin_cases i <;> decide +kernel

theorem co_composition : ∀ p r : Fin 24, ∃ s : Fin 24,
    ∀ j, coIndex p (coIndex r j)=coIndex s j := by decide +kernel
theorem high_onto : ∀ p : Fin 24, Function.Surjective (highIndex p) := by decide +kernel
theorem high_four : ∀ p, highIndex p 4=4 := by decide +kernel

theorem residue_unperm (co : Fin 6 → ℕ) (h : Fin 5 → ℕ) (p : Fin 24)
    (r : Residue (fun j => co (coIndex p j)) (fun j => h (highIndex p j))) : Residue co h := by
  rcases r with ⟨⟨j,hj⟩,zero⟩ | ⟨r,i,hc,hq⟩
  · left
    refine ⟨⟨coIndex p j,hj⟩,?_⟩
    intro j
    obtain ⟨k,hk⟩ := high_onto p j
    rw [← hk]
    exact zero k
  · right
    obtain ⟨s,hs⟩ := co_composition p r
    refine ⟨s,i,?_,?_⟩
    · intro j
      rw [← hs]
      exact hc j
    · change h (highIndex p 4)=quadOf i at hq
      simpa only [high_four] using hq

'''
s=s[:start]+coverage+s[end:]
# Keep the kernel classification in an independent compilation unit.
cut=s.index('theorem codegree_perm')
(ROOT/'formal/Aris4Math/ThirtyFour/TwentyEightClassData.lean').write_text(s[:cut]+'end Aris4Math.ThirtyFour.TwentyEightClassification\n')
head='''import Aris4Math.ThirtyFour.TwentyEightClassData
namespace Aris4Math.ThirtyFour.TwentyEightClassification
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (highPairSum high_inventory high_le_two)
open Aris4Math.ThirtyFour.TwentyEightQuadData (degree coData highData Case)
open Aris4Math.ThirtyFour.QuadIncidence
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
'''
s=head+s[cut:]
a=s.index('theorem residual_of_not_propertyB')
s=s[:a]+'''theorem residual_of_canonical (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬ PropertyB H) (f : Fin 4 ↪ Fin 20)
    (hd : ∀ j, H.degree (f j)=degree j) (i : Fin 66)
    (hc : ∀ j, H.codegree (f (first j)) (f (second j))=canonicalCo i j) :
    Residue (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j)) := by
  have bounded : ∀ a : Fin 5, count H f (highLabels a) ≤ 3 := by
    have choose : ∀ a : Fin 5, ∃ j : Fin 6, first j ∈ highLabels a ∧ second j ∈ highLabels a := by decide +kernel
    intro a
    obtain ⟨j,hj1,hj2⟩ := choose a
    have cap := ThirtyThree.TwentyTwoQuadAssembly.count_le_codegree H f (highLabels a) (first j) (second j) hj1 hj2
    rw [hc] at cap
    exact cap.trans (canonical_bounds i j).2
  let h : Fin 5 → Fin 4 := fun j => ⟨count H f (highLabels j),by have := bounded j; omega⟩
  have inv : ∀ j, highPairSum (fun z => (h z).val) j ≤ canonicalCo i j := by
    intro j; rw [← hc]; exact high_inventory H f j
  have cases := coverage i h inv
  have eq : canonicalCo i = fun j => H.codegree (f (first j)) (f (second j)) := (funext hc).symm
  rw [eq] at cases
  rcases cases with residue | triple | quad
  · exact residue
  · exact False.elim (noB (propertyB_of_triple_suitable H cover size f hd triple))
  · exact False.elim (noB (propertyB_of_quad_suitable H size f hd quad))

theorem residual_of_not_propertyB (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬ PropertyB H) (f : Fin 4 ↪ Fin 20)
    (hd : ∀ j, H.degree (f j)=degree j)
    (hc : ∀ j, 1 ≤ H.codegree (f (first j)) (f (second j)) ∧
      H.codegree (f (first j)) (f (second j)) ≤ 3) :
    Residue (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j)) := by
  let co : Fin 6 → Fin 3 := fun j => ⟨H.codegree (f (first j)) (f (second j))-1,by have := hc j; omega⟩
  have ce (j) : (co j).val+1=H.codegree (f (first j)) (f (second j)) := by dsimp [co]; have := hc j; omega
  obtain ⟨p,i,canonical⟩ := canonical_complete co
  let g := QuadTransport.vertices (perm p) f
  have gd (j) : H.degree (g j)=degree j := by
    change H.degree (f (perm p j))=degree j
    rw [hd,degree_perm]
  have gc (j) : H.codegree (g (first j)) (g (second j))=canonicalCo i j := by
    rw [codegree_perm]
    rw [ce] at canonical
    exact canonical j
  have r := residual_of_canonical H cover size noB g gd i gc
  apply residue_unperm _ _ p
  simpa only [g,codegree_perm,QuadTransport.count_permute,high_image] using r
end Aris4Math.ThirtyFour.TwentyEightClassification
#print axioms Aris4Math.ThirtyFour.TwentyEightClassification.residual_of_not_propertyB
'''
s=s.replace('    rw [ce] at canonical','    simp only [ce] at canonical')
(ROOT/'formal/Aris4Math/ThirtyFour/TwentyEightClassification.lean').write_text(s)
print('Canonical pair patterns:',len(canonical))
