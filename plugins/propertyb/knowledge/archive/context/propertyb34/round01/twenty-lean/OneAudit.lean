import Aris4Math.ThirtyFour.Assembly
namespace T34OneSevenAudit
universe u
theorem original_coloring
    (E : Finset (Finset (Fin 20)))
    (uniform : ∀ e ∈ E, e.card=5)
    (cover : ∀ x y : Fin 20, x ≠ y → ∃ e ∈ E, x ∈ e ∧ y ∈ e)
    (size : E.card=34)
    (minimum : ∀ x : Fin 20, 7 ≤ (E.filter fun e => x ∈ e).card)
    (one : (Finset.univ.filter fun x : Fin 20 => (E.filter fun e => x ∈ e).card=7).card=1) :
    ∃ c : Fin 20 → Bool, ∀ e ∈ E,
      1 ≤ (e.filter fun x => c x=true).card ∧ (e.filter fun x => c x=true).card ≤ 4 := by
  exact Aris4Math.ThirtyFour.TwentySevenOne.propertyB_of_one_seven
    ⟨E,uniform⟩ cover size minimum one

theorem conditional_original
    (remaining : Aris4Math.ThirtyFour.Assembly.RemainingGoal)
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (uniform : ∀ e ∈ E, e.card=5) (size : E.card ≤ 34) :
    ∃ c : V → Bool, ∀ e ∈ E,
      1 ≤ (e.filter fun x => c x=true).card ∧ (e.filter fun x => c x=true).card ≤ 4 := by
  classical
  letI : Fintype V := Fintype.ofFinite V
  exact (Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal.mpr remaining) V ⟨E,uniform⟩ size
end T34OneSevenAudit
#check @Aris4Math.ThirtyFour.TwentySevenOne.propertyB_of_one_seven
#print Aris4Math.ThirtyFour.Assembly.TwentyHard
#print Aris4Math.ThirtyFour.Assembly.RemainingGoal
#print axioms Aris4Math.ThirtyFour.TwentySevenOne.propertyB_of_one_seven
#print axioms T34OneSevenAudit.original_coloring
#print axioms T34OneSevenAudit.conditional_original
