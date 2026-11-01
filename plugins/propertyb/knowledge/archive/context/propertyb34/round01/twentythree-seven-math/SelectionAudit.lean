import Aris4Math.ThirtyFour.TwentyThreeSevenSelection
import Aris4Math.ThirtyFour.WeightedSubsetExtension

open scoped BigOperators
open Aris4Math Aris4Math.ThirtyFour
open Aris4Math.ThirtyThree.TwentyThreeSelection (sevenVertices mem_sevenVertices)

/-- Independent raw-edge caller for the actual six-lock selection. This is
selection evidence, not the final 23-point coloring theorem. -/
theorem raw_six_lock_selection (E : Finset (Finset (Fin 23)))
    (five : ∀ e ∈ E, e.card=5) (size : E.card=34)
    (cover : ∀ x y : Fin 23, x ≠ y → ∃ e ∈ E, x ∈ e ∧ y ∈ e)
    (minimum : ∀ x : Fin 23, 7 ≤ (E.filter fun e => x ∈ e).card) :
    let H : Simple5Hypergraph (Fin 23) := ⟨E,five⟩
    ∃ S : Finset (Fin 23), S.card=6 ∧
      (∀ x ∈ S, (E.filter fun e => x ∈ e).card=7) ∧
      WeightedSubsetSelection.IsMinimum (TwentyThreeSevenSelection.excess H)
        (sevenVertices H) S ∧
      WeightedSubsetSelection.energy (TwentyThreeSevenSelection.excess H) S ≤ 12 ∧
      (∀ x ∈ S, WeightedSubsetSelection.degree (TwentyThreeSevenSelection.excess H) S x ≤ 3) ∧
      (∀ x ∈ S, WeightedSubsetSelection.degree (TwentyThreeSevenSelection.excess H) S x=3 →
        WeightedSubsetSelection.energy (TwentyThreeSevenSelection.excess H) S ≤ 8) := by
  dsimp only
  let H : Simple5Hypergraph (Fin 23) := ⟨E,five⟩
  obtain ⟨S,card,minimal,bound,maximum,atThree⟩ :=
    TwentyThreeSevenSelection.actual_minimum_six H cover size minimum
  refine ⟨S,card,?_,minimal,bound,maximum,atThree⟩
  intro x hx
  exact (mem_sevenVertices H x).mp (minimal.1 hx)

#check @TwentyThreeSevenSelection.actual_minimum_six
#check @TwentyThreeSevenSelection.equality_degree_eight_lock
#check @WeightedSubsetSelection.exists_seventh
#print axioms WeightedSubsetSelection.swap_inequality
#print axioms WeightedSubsetSelection.vertex_bound
#print axioms WeightedSubsetSelection.exists_six
#print axioms WeightedSubsetSelection.six_equality_saturation
#print axioms WeightedSubsetSelection.exists_seventh
#print axioms TwentyThreeSevenSelection.actual_minimum_six
#print axioms TwentyThreeSevenSelection.equality_degree_eight_lock
#print axioms raw_six_lock_selection
