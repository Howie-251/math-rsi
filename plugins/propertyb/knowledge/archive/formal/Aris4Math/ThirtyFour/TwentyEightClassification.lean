import Aris4Math.ThirtyFour.TwentyEightClassData
namespace Aris4Math.ThirtyFour.TwentyEightClassification
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (highPairSum high_inventory high_le_two)
open Aris4Math.ThirtyFour.TwentyEightQuadData (degree coData highData Case)
open Aris4Math.ThirtyFour.QuadIncidence
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
theorem codegree_perm {v : ℕ} (H : Simple5Hypergraph (Fin v)) (f : Fin 4 ↪ Fin v) (p : Fin 24) (j : Fin 6) :
    H.codegree (QuadTransport.vertices (perm p) f (first j)) (QuadTransport.vertices (perm p) f (second j)) =
      H.codegree (f (first (coIndex p j))) (f (second (coIndex p j))) := by
  fin_cases p <;> fin_cases j <;> first | rfl | exact H.codegree_comm _ _

theorem propertyB_of_quad_suitable (H : Simple5Hypergraph (Fin 20)) (size : H.edges.card=34)
    (f : Fin 4 ↪ Fin 20) (hd : ∀ j, H.degree (f j)=degree j)
    (suitable : QuadSuitable
      (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j))) : PropertyB H := by
  obtain ⟨p,i,hco,hh⟩ := suitable
  apply TwentyEightQuad.propertyB_of_data H size (QuadTransport.vertices (perm p) f) i
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
  have d0 : H.degree (f 0)=8 := hd 0
  have d1 : H.degree (f 1)=8 := hd 1
  have d2 : H.degree (f 2)=8 := hd 2
  have d3 : H.degree (f 3)=8 := hd 3
  have ne (i j : Fin 4) (h : i ≠ j) : f i ≠ f j := f.injective.ne h
  rcases suitable with h | h | h | h
  · apply TwentyRemainingTriples.propertyB_of_suitable H cover size (f 0) (f 1) (f 2)
      (ne 0 1 (by decide)) (ne 0 2 (by decide)) (ne 1 2 (by decide)) false d0 d1 d2
    have ht := triple_count H f 0
    change tripleCodegree H (f 0) (f 1) (f 2) = count H f (highLabels 0) + count H f (highLabels 4) at ht
    rw [ht]
    simpa [first,second] using h
  · apply TwentyRemainingTriples.propertyB_of_suitable H cover size (f 0) (f 1) (f 3)
      (ne 0 1 (by decide)) (ne 0 3 (by decide)) (ne 1 3 (by decide)) false d0 d1 d3
    have ht := triple_count H f 1
    change tripleCodegree H (f 0) (f 1) (f 3) = count H f (highLabels 1) + count H f (highLabels 4) at ht
    rw [ht]
    simpa [first,second] using h
  · apply TwentyRemainingTriples.propertyB_of_suitable H cover size (f 0) (f 2) (f 3)
      (ne 0 2 (by decide)) (ne 0 3 (by decide)) (ne 2 3 (by decide)) false d0 d2 d3
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

theorem residual_of_canonical (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
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
    simp only [ce] at canonical
    exact canonical j
  have r := residual_of_canonical H cover size noB g gd i gc
  apply residue_unperm _ _ p
  simpa only [g,codegree_perm,QuadTransport.count_permute,high_image] using r
end Aris4Math.ThirtyFour.TwentyEightClassification
#print axioms Aris4Math.ThirtyFour.TwentyEightClassification.residual_of_not_propertyB
