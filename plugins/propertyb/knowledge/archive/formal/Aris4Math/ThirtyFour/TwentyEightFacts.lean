import Aris4Math.ThirtyFour.TwentyEightClassification

namespace Aris4Math.ThirtyFour.TwentyEightFacts
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 1000
open Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyFour.TwentyEightClassification

theorem small_bounds (co : Fin 6 → ℕ) (q : ℕ) (h : SmallResidue co q) :
    (∀ j, 1 ≤ co j ∧ co j ≤ 2) ∧ q ≤ 1 := by
  obtain ⟨p,i,hc,hq⟩ := h
  have onto : ∀ p : Fin 24, Function.Surjective (coIndex p) := by decide +kernel
  have bounded : ∀ i j, 1 ≤ shapes i j ∧ shapes i j ≤ 2 := by decide +kernel
  constructor
  · intro j
    obtain ⟨k,hk⟩ := onto p j
    rw [← hk,hc]
    exact bounded i k
  · rw [hq]
    fin_cases i <;> decide

def GraphFacts (co : Fin 6 → ℕ) (q : ℕ) : Prop :=
  (co 0=1 → co 1=1 → co 3 ≠ 1) ∧
  (co 0=1 → co 5=1 → co 1=2 → co 2=2 → co 3=2 → co 4 ≠ 2) ∧
  (co 0=1 → co 1=1 → co 2=2 → co 3=2 → co 4=2 → co 5 ≠ 2) ∧
  (co 0=1 → co 1=2 → co 2=1 → co 3=1 → co 4=2 → co 5=1 → q=1) ∧
  (co 0=1 → co 1=1 → co 2=1 → q=0) ∧
  ((∀ j, co j=2) → q=0) ∧
  ((Finset.univ.filter fun j => co j=1).card ≤ 1 → q=0) ∧
  ((Finset.univ.filter fun j : Fin 3 => co (j.castLE (by decide : 3 ≤ 6))=1).card ≤ 1 → q=0)
instance (co : Fin 6 → ℕ) (q : ℕ) : Decidable (GraphFacts co q) := by unfold GraphFacts; infer_instance

theorem finite_graph_facts : ∀ co : Fin 6 → Fin 2, ∀ q : Fin 2,
    SmallResidue (fun j => (co j).val+1) q.val → GraphFacts (fun j => (co j).val+1) q.val := by
  decide +kernel

theorem graph_facts (co : Fin 6 → ℕ) (q : ℕ) (h : SmallResidue co q) : GraphFacts co q := by
  obtain ⟨hc,hq⟩ := small_bounds co q h
  let c : Fin 6 → Fin 2 := fun j => ⟨co j-1,by have := hc j; omega⟩
  have eq (j) : (c j).val+1=co j := by dsimp [c]; have := hc j; omega
  have := finite_graph_facts c ⟨q,by omega⟩ (by simpa only [eq] using h)
  simpa only [eq] using this

theorem all_high_zero_of_three (co : Fin 6 → ℕ) (h : Fin 5 → ℕ)
    (residue : Residue co h) (three : ∃ j, co j=3) : ∀ j, h j=0 := by
  rcases residue with ⟨_,zero⟩ | small
  · exact zero
  · obtain ⟨j,hj⟩ := three
    have bounded := (small_bounds co (h 4) small).1 j
    omega

theorem small_of_bounded (co : Fin 6 → ℕ) (h : Fin 5 → ℕ)
    (residue : Residue co h) (bounded : ∀ j, co j ≤ 2) : SmallResidue co (h 4) := by
  rcases residue with ⟨⟨j,hj⟩,_⟩ | small
  · have := bounded j; omega
  · exact small
end Aris4Math.ThirtyFour.TwentyEightFacts
