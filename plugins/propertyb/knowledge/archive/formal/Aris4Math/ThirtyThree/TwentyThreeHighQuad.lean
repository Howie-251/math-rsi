import Aris4Math.ThirtyThree.TwentyThreeHighQuadData
import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly
import Aris4Math.ThirtyThree.TwentyThreeHighSelection
import Aris4Math.ThirtyThree.TwentyThreeHighPair

/-! The complete actual four-lock codegree-three branch on 23 points. -/
namespace Aris4Math.ThirtyThree.TwentyThreeHighQuad

open Aris4Math.TypeCounting
open QuadProfiles TwentyThreeHighQuadData PureLink
open TwentyTwoQuadAssembly (highPairSum high_inventory count_le_codegree)

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem data_complete : ∀ h : Fin 5 → Fin 2,
    (∀ j, highPairSum (fun a => (h a).val) j ≤ co j) →
      ∃ i : Fin 7, ∀ a, (h a).val = high i a := by decide +kernel

/-- Every large trace contains a unit pair, so its actual multiplicity is at
most one. The six pair inventories then cover the seven labeled possibilities. -/
theorem actual_data (H : Simple5Hypergraph (Fin 23)) (vertices : Fin 4 ↪ Fin 23)
    (pairs : ∀ j, H.codegree (vertices (first j)) (vertices (second j)) = co j) :
    ∃ i : Fin 7, ∀ a, count H vertices (highLabels a) = high i a := by
  have choose : ∀ a : Fin 5, ∃ j : Fin 6,
      first j ∈ highLabels a ∧ second j ∈ highLabels a ∧ co j = 1 := by decide +kernel
  have small (a : Fin 5) : count H vertices (highLabels a) ≤ 1 := by
    obtain ⟨j,hj1,hj2,one⟩ := choose a
    have h := count_le_codegree H vertices (highLabels a) (first j) (second j) hj1 hj2
    simpa [pairs,one] using h
  let h : Fin 5 → Fin 2 := fun a => ⟨count H vertices (highLabels a),by have := small a; omega⟩
  have budget : ∀ j, highPairSum (fun a => (h a).val) j ≤ co j := by
    intro j
    rw [←pairs j]
    exact high_inventory H vertices j
  exact data_complete h budget

/-- Exact recovery and actual quota deductions supply a coloring of H. -/
theorem propertyB_of_four (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (vertices : Fin 4 ↪ Fin 23)
    (degrees : ∀ j, H.degree (vertices j) = 7)
    (pairs : ∀ a, H.codegree (vertices (first a)) (vertices (second a)) = co a) : PropertyB H := by
  obtain ⟨i,hh⟩ := actual_data H vertices pairs
  obtain ⟨valid,strict,bounds⟩ := certificates i
  have hm (T) : count H vertices T = counts i T := by
    rw [actual_recovered,edges33]
    simp only [degrees,pairs,hh,counts]
  have real : RealizesProfile H vertices (positions i) (p i) 33 := by
    rw [p_eq] at valid ⊢
    exact realizes_profile H vertices (positions i) (counts i) hm _ valid
  apply CustomDeletion.propertyB_of_custom_deletion H vertices (positions i) (p i) real rfl (loss i)
  · intro j _
    obtain ⟨cn,dn,finite⟩ := bounds j
    apply TwentyTwoPureDeletion.realized_dual_deduction H cover vertices (positions i) (p i)
      real j _ 2 ((4*counts i {j}+2-19)/3) (counts i {j}) (c i j) (d i j) _ rfl
    · simp [degrees]
    · exact hm {j}
    · exact le_rfl
    · exact cn
    · exact dn
    · exact finite
  · intro k hk
    have ne (j : Fin 4) : k ≠ (positions i j).val+1 := by
      intro eq
      apply hk
      rw [eq]
      change _ ∈ List.ofFn (fun j => (positions i j).val+1)
      exact List.mem_ofFn.mpr ⟨j,rfl⟩
    simp only [loss,if_neg (ne 0),if_neg (ne 1),if_neg (ne 2),if_neg (ne 3)]
  · exact strict

/-- The actual common-neighbor selection discharges all four-lock inputs. -/
theorem propertyB_of_pair_three (H : Simple5Hypergraph (Fin 23)) (cover : H.PairCovering)
    (edges33 : H.edges.card = 33) (many : 19 ≤ (TwentyThreeSelection.sevenVertices H).card)
    (x y : Fin 23) (dx : H.degree x = 7) (dy : H.degree y = 7)
    (xy : x ≠ y) (codegree : H.codegree x y = 3) : PropertyB H := by
  obtain ⟨f,inj,_,_,degrees,c01,others⟩ :=
    TwentyThreeHighSelection.exists_four_high_of_three H cover (by decide) many x y dx dy xy codegree
  let vertices : Fin 4 ↪ Fin 23 := ⟨f,inj⟩
  apply propertyB_of_four H cover edges33 vertices degrees
  intro a
  fin_cases a
  · exact c01
  · exact others 0 2 (by decide) (by decide)
  · exact others 0 3 (by decide) (by decide)
  · exact others 1 2 (by decide) (by decide)
  · exact others 1 3 (by decide) (by decide)
  · exact others 2 3 (by decide) (by decide)

theorem propertyB_of_pair_at_least_three (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33)
    (many : 19 ≤ (TwentyThreeSelection.sevenVertices H).card)
    (x y : Fin 23) (dx : H.degree x = 7) (dy : H.degree y = 7)
    (xy : x ≠ y) (large : 3 ≤ H.codegree x y) : PropertyB H := by
  by_cases four : 4 ≤ H.codegree x y
  · exact TwentyThreeHighPair.propertyB_of_high_pair H edges33 x y xy dx dy four
  · exact propertyB_of_pair_three H cover edges33 many x y dx dy xy (by omega)

end Aris4Math.ThirtyThree.TwentyThreeHighQuad
