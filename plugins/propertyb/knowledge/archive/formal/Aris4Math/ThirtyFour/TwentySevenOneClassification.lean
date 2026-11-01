import Aris4Math.ThirtyFour.TwentySevenOneQuad
import Aris4Math.ThirtyFour.QuadTransport
import Aris4Math.ThirtyFour.QuadIncidence
import Aris4Math.ThirtyFour.TwentyRemainingTriples

namespace Aris4Math.ThirtyFour.TwentySevenOneClassification
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (highPairSum high_inventory high_le_two)
open Aris4Math.ThirtyFour.TwentySevenOneQuadData (degree coData highData Case)
open Aris4Math.ThirtyFour.QuadIncidence
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
def permFn : Fin 6 → Fin 4 → Fin 4 := ![![0,1,2,3],![0,1,3,2],![0,2,1,3],![0,2,3,1],![0,3,1,2],![0,3,2,1]]
theorem permFn_bijective : ∀ p, Function.Bijective (permFn p) := by decide
noncomputable def perm (p : Fin 6) : Equiv.Perm (Fin 4) := Equiv.ofBijective (permFn p) (permFn_bijective p)
def coIndex : Fin 6 → Fin 6 → Fin 6 := ![![0,1,2,3,4,5],![0,2,1,4,3,5],![1,0,2,3,5,4],![1,2,0,5,3,4],![2,0,1,4,5,3],![2,1,0,5,4,3]]
def highIndex : Fin 6 → Fin 5 → Fin 5 := ![![0,1,2,3,4],![1,0,2,3,4],![0,2,1,3,4],![2,0,1,3,4],![1,2,0,3,4],![2,1,0,3,4]]
theorem high_image : ∀ p j, (highLabels j).image (perm p)=highLabels (highIndex p j) := by decide +kernel
theorem degree_perm : ∀ p j, degree (perm p j)=degree j := by decide +kernel

def Residue (co : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Prop :=
  h 4=0 ∧ co 0+co 1+co 2 ≠ 4 ∧
    (co 0=1 → co 1=1 → co 2=1 → ∀ j, h j=0)
instance (co : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Decidable (Residue co h) := by unfold Residue; infer_instance

def TripleSuitable (co : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Prop :=
  TwentyRemainingTriples.Suitable true (co 0) (co 1) (co 3) (h 0+h 4) ∨
  TwentyRemainingTriples.Suitable true (co 0) (co 2) (co 4) (h 1+h 4) ∨
  TwentyRemainingTriples.Suitable true (co 1) (co 2) (co 5) (h 2+h 4) ∨
  TwentyRemainingTriples.Suitable false (co 3) (co 4) (co 5) (h 3+h 4)
instance (co : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Decidable (TripleSuitable co h) := by unfold TripleSuitable; infer_instance

def QuadSuitable (co : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Prop :=
  ∃ p : Fin 6, ∃ i : Case, (∀ j, co (coIndex p j)=coData i j) ∧ ∀ j, h (highIndex p j)=highData i j
instance (co : Fin 6 → ℕ) (h : Fin 5 → ℕ) : Decidable (QuadSuitable co h) := by unfold QuadSuitable; infer_instance

set_option maxHeartbeats 0 in
theorem coverage : ∀ co : Fin 6 → Fin 2, ∀ h : Fin 5 → Fin 3,
    (∀ j, highPairSum (fun z => (h z).val) j ≤ (co j).val+1) →
    Residue (fun j => (co j).val+1) (fun j => (h j).val) ∨
      TripleSuitable (fun j => (co j).val+1) (fun j => (h j).val) ∨
      QuadSuitable (fun j => (co j).val+1) (fun j => (h j).val) := by decide +kernel

theorem codegree_perm {v : ℕ} (H : Simple5Hypergraph (Fin v)) (f : Fin 4 ↪ Fin v) (p : Fin 6) (j : Fin 6) :
    H.codegree (QuadTransport.vertices (perm p) f (first j)) (QuadTransport.vertices (perm p) f (second j)) =
      H.codegree (f (first (coIndex p j))) (f (second (coIndex p j))) := by
  fin_cases p <;> fin_cases j <;> first | rfl | exact H.codegree_comm _ _

theorem propertyB_of_quad_suitable (H : Simple5Hypergraph (Fin 20)) (size : H.edges.card=34)
    (f : Fin 4 ↪ Fin 20) (hd : ∀ j, H.degree (f j)=degree j)
    (suitable : QuadSuitable
      (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j))) : PropertyB H := by
  obtain ⟨p,i,hco,hh⟩ := suitable
  apply TwentySevenOneQuad.propertyB_of_data H size (QuadTransport.vertices (perm p) f) i
  · intro j
    change H.degree (f (perm p j))=degree j
    rw [hd,degree_perm]
  · intro j
    rw [codegree_perm]
    exact hco j
  · intro j
    rw [QuadTransport.count_permute,high_image]
    exact hh j

theorem propertyB_of_triple_suitable (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (size : H.edges.card=34) (f : Fin 4 ↪ Fin 20) (hd : ∀ j, H.degree (f j)=degree j)
    (suitable : TripleSuitable
      (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j))) : PropertyB H := by
  have d0 : H.degree (f 0)=7 := hd 0
  have d1 : H.degree (f 1)=8 := hd 1
  have d2 : H.degree (f 2)=8 := hd 2
  have d3 : H.degree (f 3)=8 := hd 3
  have ne (i j : Fin 4) (h : i ≠ j) : f i ≠ f j := f.injective.ne h
  rcases suitable with h | h | h | h
  · apply TwentyRemainingTriples.propertyB_of_suitable H cover size (f 0) (f 1) (f 2)
      (ne 0 1 (by decide)) (ne 0 2 (by decide)) (ne 1 2 (by decide)) true d0 d1 d2
    have ht := triple_count H f 0
    change tripleCodegree H (f 0) (f 1) (f 2) = count H f (highLabels 0) + count H f (highLabels 4) at ht
    rw [ht]
    simpa [first,second] using h
  · apply TwentyRemainingTriples.propertyB_of_suitable H cover size (f 0) (f 1) (f 3)
      (ne 0 1 (by decide)) (ne 0 3 (by decide)) (ne 1 3 (by decide)) true d0 d1 d3
    have ht := triple_count H f 1
    change tripleCodegree H (f 0) (f 1) (f 3) = count H f (highLabels 1) + count H f (highLabels 4) at ht
    rw [ht]
    simpa [first,second] using h
  · apply TwentyRemainingTriples.propertyB_of_suitable H cover size (f 0) (f 2) (f 3)
      (ne 0 2 (by decide)) (ne 0 3 (by decide)) (ne 2 3 (by decide)) true d0 d2 d3
    have ht := triple_count H f 2
    change tripleCodegree H (f 0) (f 2) (f 3) = count H f (highLabels 2) + count H f (highLabels 4) at ht
    rw [ht]
    simpa [first,second] using h
  · apply TwentyRemainingTriples.propertyB_of_suitable H cover size (f 1) (f 2) (f 3)
      (ne 1 2 (by decide)) (ne 1 3 (by decide)) (ne 2 3 (by decide)) false d1 d2 d3
    have ht := triple_count H f 3
    change tripleCodegree H (f 1) (f 2) (f 3) = count H f (highLabels 3) + count H f (highLabels 4) at ht
    rw [ht]
    simpa [first,second] using h

theorem residual_of_not_propertyB (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (size : H.edges.card=34) (noB : ¬ PropertyB H) (f : Fin 4 ↪ Fin 20)
    (hd : ∀ j, H.degree (f j)=degree j)
    (hc : ∀ j, 1 ≤ H.codegree (f (first j)) (f (second j)) ∧
      H.codegree (f (first j)) (f (second j)) ≤ 2) :
    Residue (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j)) := by
  let co : Fin 6 → Fin 2 := fun j => ⟨H.codegree (f (first j)) (f (second j))-1,by have := hc j; omega⟩
  have ce (j) : (co j).val+1=H.codegree (f (first j)) (f (second j)) := by dsimp [co]; have := hc j; omega
  have bounded := ThirtyThree.TwentyTwoQuadAssembly.high_le_two H f (fun j => (hc j).2)
  let h : Fin 5 → Fin 3 := fun j => ⟨count H f (highLabels j),by have := bounded j; omega⟩
  have inv : ∀ j, highPairSum (fun z => (h z).val) j ≤ (co j).val+1 := by
    intro j; rw [ce]; exact high_inventory H f j
  have cases := coverage co h inv
  simp only [ce] at cases
  rcases cases with residue | triple | quad
  · exact residue
  · exact False.elim (noB (propertyB_of_triple_suitable H cover size f hd triple))
  · exact False.elim (noB (propertyB_of_quad_suitable H size f hd quad))
end Aris4Math.ThirtyFour.TwentySevenOneClassification
#print axioms Aris4Math.ThirtyFour.TwentySevenOneClassification.residual_of_not_propertyB
