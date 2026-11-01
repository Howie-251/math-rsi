import Aris4Math.ThirtyFour.Reduction
import Aris4Math.ThirtyFour.Twenty
import Aris4Math.ThirtyFour.TwentyOneFive
import Aris4Math.ThirtyFour.TwentyOneSix
import Aris4Math.ThirtyFour.TwentyOneEight
import Aris4Math.ThirtyFour.TwentyOneSevenOne
import Aris4Math.ThirtyFour.TwentyOneSevenMany
import Aris4Math.ThirtyFour.TwentyFourNoLow
import Aris4Math.ThirtyFour.TwentyOneSevenFour
import Aris4Math.ThirtyFour.TwentyThreeManyLowComplete

/-! Exact remaining obligations after all twenty-vertex cases and the
21-vertex minimum-five, minimum-six and minimum-eight branches, and the unique-seven, exactly-four-sevens and at-least-five-sevens branches. This file does not prove T34. -/
namespace Aris4Math.ThirtyFour.Assembly
universe u

/-- Already proved regime, retained for earlier branch audit imports. -/
def TwentyHard (H : Simple5Hypergraph (Fin 20)) : Prop :=
  (∀ x, 8 ≤ H.degree x) ∧ ∃ x, H.degree x=8

/-- The remaining 21-point inputs have minimum degree seven and exactly two or three seven-degree points. -/
def RemainingGoal : Prop :=
  (∀ H : Simple5Hypergraph (Fin 21), H.edges.card=34 → H.PairCovering →
    (∀ x, 7 ≤ H.degree x) → (2≤(TwentyOneSevenSelection.sevens H).card) →
    ((TwentyOneSevenSelection.sevens H).card≤3) → PropertyB H) ∧
  (∀ v : ℕ, 22 ≤ v → v ≤ 25 → ∀ H : Simple5Hypergraph (Fin v),
    H.edges.card=34 → H.PairCovering → (v=24 → ∃ x, H.degree x=6) → (v=23 → H.sixVertices.card≤6) → PropertyB H)

theorem target_iff_remaining_goal : Aris4Math.Target34.{u} ↔ RemainingGoal := by
  rw [Aris4Math.ThirtyFour.target_iff_remaining_goal]
  constructor
  · intro remaining
    constructor
    · intro H size cover _ _ _
      exact remaining 21 (by omega) (by omega) H size cover
    · intro v lower upper H size cover _ _
      exact remaining v (by omega) upper H size cover
  · intro remaining v lower upper H size cover
    by_cases twenty : v=20
    · subst v
      exact twenty_propertyB H cover size
    by_cases twentyone : v=21
    · subst v
      by_cases five : ∃ x, H.degree x=5
      · obtain ⟨x,dx⟩ := five
        exact TwentyOneFive.propertyB_of_degree_five H cover size x dx
      · have minimumSix (x : Fin 21) : 6≤H.degree x := by
          have bound := H.pairCovering_degree_bound cover x
          simp only [Fintype.card_fin] at bound
          have notFive : H.degree x≠5 := fun h=>five ⟨x,h⟩
          omega
        by_cases six : ∃x,H.degree x=6
        · obtain ⟨x,dx⟩:=six
          exact TwentyOneSix.propertyB_of_degree_six H cover size minimumSix x dx
        · have minimumSeven (x : Fin 21) : 7≤H.degree x := by
            have bound:=minimumSix x
            have notSix : H.degree x≠6 := fun h=>six ⟨x,h⟩
            omega
          by_cases seven : ∃x,H.degree x=7
          · have positive : 0<(TwentyOneSevenSelection.sevens H).card := by
              obtain ⟨x,dx⟩:=seven
              exact Finset.card_pos.mpr ⟨x,Finset.mem_filter.mpr ⟨Finset.mem_univ x,dx⟩⟩
            by_cases one : (TwentyOneSevenSelection.sevens H).card=1
            · exact TwentyOneSevenOne.propertyB_of_one_seven H cover size minimumSeven one
            · by_cases many : 5≤(TwentyOneSevenSelection.sevens H).card
              · exact TwentyOneSevenMany.propertyB_of_many_sevens H cover size many
              · by_cases four : (TwentyOneSevenSelection.sevens H).card=4
                · exact TwentyOneSevenFour.propertyB_of_four_sevens H cover size minimumSeven four
                · exact remaining.1 H size cover minimumSeven (by omega) (by omega)
          · apply TwentyOneEight.propertyB_of_minimum_eight H cover size
            intro x
            have bound:=minimumSeven x
            have notSeven : H.degree x≠7 := fun h=>seven ⟨x,h⟩
            omega
    · by_cases h23 : v=23
      · subst v
        by_cases many : 7≤H.sixVertices.card
        · exact TwentyThreeManyLowComplete.propertyB H cover size many
        · exact remaining.2 23 (by omega) upper H size cover (by omega)
            (fun _ => by omega)
      · by_cases hv : v=24
        · subst v
          by_cases low : ∃ x, H.degree x=6
          · exact remaining.2 24 (by omega) upper H size cover (fun _ => low) (by omega)
          · apply TwentyFourNoLow.propertyB_of_no_six H cover size
            apply Finset.card_eq_zero.mpr
            apply Finset.eq_empty_iff_forall_notMem.mpr
            intro x hx
            exact low ⟨x,(Finset.mem_filter.mp hx).2⟩
        · exact remaining.2 v (by omega) upper H size cover
            (fun h => False.elim (hv h)) (fun h => False.elim (h23 h))
end Aris4Math.ThirtyFour.Assembly
#print axioms Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal
