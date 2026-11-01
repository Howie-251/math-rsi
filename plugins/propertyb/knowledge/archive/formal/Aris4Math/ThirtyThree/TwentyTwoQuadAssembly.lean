import Aris4Math.ThirtyThree.TwentyTwoQuad
import Aris4Math.ThirtyThree.TwentyTwoSelection

/-! Bind the selected four original vertices to their actual high-trace counts.
The finite high-count table is matched only after these input obligations. -/
namespace Aris4Math.ThirtyThree.TwentyTwoQuadAssembly

open Aris4Math.TypeCounting Aris4Math.ThirtyThree.QuadProfiles
open scoped BigOperators

variable {v : ℕ}

def fourVertices (x y z w : Fin v) (xy : x ≠ y) (xz : x ≠ z) (xw : x ≠ w)
    (yz : y ≠ z) (yw : y ≠ w) (zw : z ≠ w) : Fin 4 ↪ Fin v :=
  ⟨![x,y,z,w],by intro i j h; fin_cases i <;> fin_cases j <;> simp_all⟩

/-- High-order classes that spend one pair's codegree inventory. -/
def highPairSum (h : Fin 5 → ℕ) : Fin 6 → ℕ :=
  ![h 0+h 1+h 4,h 0+h 2+h 4,h 1+h 2+h 4,
    h 0+h 3+h 4,h 1+h 3+h 4,h 2+h 3+h 4]

theorem high_inventory (H : Simple5Hypergraph (Fin v)) (vertices : Fin 4 ↪ Fin v)
    (j : Fin 6) : highPairSum (fun i => count H vertices (highLabels i)) j ≤
      H.codegree (vertices (first j)) (vertices (second j)) := by
  have h := sum_codegree_counts H vertices (first j) (second j)
  rw [label_univ] at h
  fin_cases j <;>
    simp +decide only [labels,List.toFinset_cons,List.toFinset_nil,Finset.filter_insert,
      Finset.filter_singleton,Finset.filter_empty,Finset.sum_insert,Finset.sum_singleton,
      Finset.sum_empty,Finset.mem_insert,Finset.mem_singleton,Finset.notMem_empty,
      first,second,highPairSum,highLabels,Matrix.cons_val_zero,Matrix.cons_val_one,
      Matrix.cons_val_two,Matrix.cons_val_three,Matrix.cons_val_four,cons_val_five,
      Matrix.head_cons,Matrix.tail_cons,Matrix.cons_val_zero',Matrix.cons_val_succ',if_true,if_false] at h ⊢ <;> omega

theorem count_le_codegree (H : Simple5Hypergraph (Fin v)) (vertices : Fin 4 ↪ Fin v)
    (T : Finset (Fin 4)) (i j : Fin 4) (hi : i ∈ T) (hj : j ∈ T) :
    count H vertices T ≤ H.codegree (vertices i) (vertices j) := by
  apply Finset.card_le_card
  intro e he
  obtain ⟨he,heq⟩ := Finset.mem_filter.mp he
  exact Finset.mem_filter.mpr ⟨he,
    (mem_lockSignature vertices e i).mp (heq ▸ hi),
    (mem_lockSignature vertices e j).mp (heq ▸ hj)⟩

theorem high_le_two (H : Simple5Hypergraph (Fin v)) (vertices : Fin 4 ↪ Fin v)
    (small : ∀ j, H.codegree (vertices (first j)) (vertices (second j)) ≤ 2) :
    ∀ i : Fin 5, count H vertices (highLabels i) ≤ 2 := by
  have choose : ∀ i : Fin 5, ∃ j : Fin 6,
      first j ∈ highLabels i ∧ second j ∈ highLabels i := by decide +kernel
  intro i
  obtain ⟨j,hj1,hj2⟩ := choose i
  exact (count_le_codegree H vertices (highLabels i) (first j) (second j) hj1 hj2).trans (small j)

theorem positive_high_of_common_edge (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 4 ↪ Fin v)
    (common : ∃ e ∈ H.edges, vertices 0 ∈ e ∧ vertices 1 ∈ e ∧ vertices 2 ∈ e) :
    1 ≤ count H vertices (highLabels 0) + count H vertices (highLabels 4) := by
  obtain ⟨e,he,h0,h1,h2⟩ := common
  by_cases h3 : vertices 3 ∈ e
  · have sig : lockSignature vertices e = highLabels 4 := by
      ext i
      fin_cases i <;> simp [lockSignature,highLabels,h0,h1,h2,h3]
    have pos : 1 ≤ count H vertices (highLabels 4) := Finset.one_le_card.mpr
      ⟨e,Finset.mem_filter.mpr ⟨he,sig⟩⟩
    omega
  · have sig : lockSignature vertices e = highLabels 0 := by
      ext i
      fin_cases i <;> simp [lockSignature,highLabels,h0,h1,h2,h3]
    have pos : 1 ≤ count H vertices (highLabels 0) := Finset.one_le_card.mpr
      ⟨e,Finset.mem_filter.mpr ⟨he,sig⟩⟩
    omega

open Aris4Math.ThirtyThree.TwentyTwoQuadData (co kindOf high)

def Admissible (kind : Fin 3) (h : Fin 5 → ℕ) : Prop :=
  (∀ j, highPairSum h j ≤ co kind j) ∧ (kind = 0 → 1 ≤ h 0 + h 4)

instance (kind : Fin 3) (h : Fin 5 → ℕ) : Decidable (Admissible kind h) := by
  unfold Admissible; infer_instance

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
/-- Covers every bounded high-trace vector satisfying the six true pair
inventories. These are local integer data, not an enumeration of hypergraphs. -/
theorem data_complete : ∀ kind : Fin 3, ∀ h : Fin 5 → Fin 3,
    Admissible kind (fun a => (h a).val) →
      ∃ i : Fin 20, kindOf i = kind ∧ ∀ a, (h a).val = high i a := by
  intro kind
  fin_cases kind <;> decide +kernel

/-- Actual four-lock high traces satisfy the complete finite data constraints. -/
theorem actual_data (H : Simple5Hypergraph (Fin v)) (vertices : Fin 4 ↪ Fin v)
    (kind : Fin 3)
    (pairCounts : ∀ j, H.codegree (vertices (first j)) (vertices (second j)) = co kind j)
    (common : kind = 0 → ∃ e ∈ H.edges, vertices 0 ∈ e ∧ vertices 1 ∈ e ∧ vertices 2 ∈ e) :
    ∃ i : Fin 20, kindOf i = kind ∧ ∀ a, count H vertices (highLabels a) = high i a := by
  have small : ∀ k : Fin 3, ∀ j : Fin 6, co k j ≤ 2 := by decide +kernel
  have bounded := high_le_two H vertices (fun j => by rw [pairCounts]; exact small kind j)
  let h : Fin 5 → Fin 3 := fun a => ⟨count H vertices (highLabels a),by have := bounded a; omega⟩
  have admissible : Admissible kind (fun a => (h a).val) := by
    constructor
    · intro j
      change highPairSum (fun a => count H vertices (highLabels a)) j ≤ co kind j
      rw [← pairCounts j]
      exact high_inventory H vertices j
    · intro hk
      exact positive_high_of_common_edge H vertices (common hk)
  exact data_complete kind h admissible

/-- The three selected four-lock patterns determine one of the twenty actual
labelled data rows. All inputs are bound to the selected original vertices. -/
theorem data_of_quadCase (H : Simple5Hypergraph (Fin v))
    (x y z w : Fin v) (xy : x ≠ y) (xz : x ≠ z) (xw : x ≠ w)
    (yz : y ≠ z) (yw : y ≠ w) (zw : z ≠ w)
    (hcase : TwentyTwoSelection.QuadCase H x y z w) :
    ∃ i : Fin 20,
      (∀ j, H.degree (fourVertices x y z w xy xz xw yz yw zw j) = 7) ∧
      (∀ a, H.codegree (fourVertices x y z w xy xz xw yz yw zw (first a))
        (fourVertices x y z w xy xz xw yz yw zw (second a)) = co (kindOf i) a) ∧
      (∀ a, count H (fourVertices x y z w xy xz xw yz yw zw) (highLabels a) = high i a) := by
  let vertices := fourVertices x y z w xy xz xw yz yw zw
  obtain ⟨dx,dy,dz,dw,relations⟩ := hcase
  have degrees : ∀ j, H.degree (vertices j) = 7 := by
    intro j
    fin_cases j
    · exact dx
    · exact dy
    · exact dz
    · exact dw
  have assemble (kind : Fin 3)
      (pairCounts : ∀ a, H.codegree (vertices (first a)) (vertices (second a)) = co kind a)
      (common : kind = 0 → ∃ e ∈ H.edges, vertices 0 ∈ e ∧ vertices 1 ∈ e ∧ vertices 2 ∈ e) :
      ∃ i : Fin 20, (∀ j, H.degree (vertices j) = 7) ∧
        (∀ a, H.codegree (vertices (first a)) (vertices (second a)) = co (kindOf i) a) ∧
        (∀ a, count H vertices (highLabels a) = high i a) := by
    obtain ⟨i,hkind,hh⟩ := actual_data H vertices kind pairCounts common
    exact ⟨i,degrees,by simpa only [hkind] using pairCounts,hh⟩
  rcases relations with ⟨cxy,cxz,cyz,cxw,cyw,czw⟩ |
    ⟨cxy,cxz,cxw,cyz,cyw,czw⟩ | ⟨cxy,cxz,cxw,cyz,cyw,czw,common⟩
  · apply assemble 2
    · intro a
      fin_cases a
      · exact cxy
      · exact cxz
      · exact cxw
      · exact cyz
      · exact cyw
      · exact czw
    · intro h
      contradiction
  · apply assemble 1
    · intro a
      fin_cases a
      · exact cxy
      · exact cxz
      · exact cxw
      · exact cyz
      · exact cyw
      · exact czw
    · intro h
      contradiction
  · apply assemble 0
    · intro a
      fin_cases a
      · exact cxy
      · exact cxz
      · exact cxw
      · exact cyz
      · exact cyw
      · exact czw
    · intro _
      exact common

/-- Every selected actual four-lock configuration gives Property B, with no
profile or high-trace certificate remaining as a premise. -/
theorem propertyB_of_quadCase (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (x y z w : Fin 22) (xy : x ≠ y) (xz : x ≠ z) (xw : x ≠ w)
    (yz : y ≠ z) (yw : y ≠ w) (zw : z ≠ w)
    (hcase : TwentyTwoSelection.QuadCase H x y z w) : PropertyB H := by
  obtain ⟨i,hd,hc,hh⟩ := data_of_quadCase H x y z w xy xz xw yz yw zw hcase
  exact TwentyTwoQuad.propertyB_of_data H cover edges33
    (fourVertices x y z w xy xz xw yz yw zw) i hd hc hh

end Aris4Math.ThirtyThree.TwentyTwoQuadAssembly

#print axioms Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.high_inventory
#print axioms Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.high_le_two
#print axioms Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.positive_high_of_common_edge

#print axioms Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.data_complete
#print axioms Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.data_of_quadCase

#print axioms Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.propertyB_of_quadCase
