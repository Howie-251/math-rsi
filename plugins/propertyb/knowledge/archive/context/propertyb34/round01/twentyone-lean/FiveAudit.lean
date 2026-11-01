import Aris4Math.ThirtyFour.Assembly
namespace T34TwentyOneFiveAudit
universe u
theorem original_branch (E : Finset (Finset (Fin 21)))
    (uniform : ∀ e ∈ E, e.card=5) (size : E.card=34)
    (cover : ∀ x y : Fin 21, x ≠ y → ∃ e ∈ E, x ∈ e ∧ y ∈ e)
    (x : Fin 21) (degree : (E.filter fun e => x ∈ e).card=5) :
    ∃ c : Fin 21 → Bool, ∀ e ∈ E,
      1 ≤ (e.filter fun x => c x=true).card ∧ (e.filter fun x => c x=true).card ≤ 4 := by
  exact Aris4Math.ThirtyFour.TwentyOneFive.propertyB_of_degree_five ⟨E,uniform⟩ cover size x degree

theorem conditional_original
    (remaining : Aris4Math.ThirtyFour.Assembly.RemainingGoal)
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (uniform : ∀ e ∈ E, e.card=5) (size : E.card ≤ 34) :
    ∃ c : V → Bool, ∀ e ∈ E,
      1 ≤ (e.filter fun x => c x=true).card ∧ (e.filter fun x => c x=true).card ≤ 4 := by
  classical
  letI : Fintype V := Fintype.ofFinite V
  exact (Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal.mpr remaining) V ⟨E,uniform⟩ size
end T34TwentyOneFiveAudit
#print Aris4Math.ThirtyFour.TwentyOneFive.propertyB_of_degree_five
#print Aris4Math.ThirtyFour.Assembly.RemainingGoal
#print axioms Aris4Math.ThirtyFour.TwentyOneFive.propertyB_of_degree_five
#print axioms Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal
#print axioms T34TwentyOneFiveAudit.original_branch
#print axioms T34TwentyOneFiveAudit.conditional_original
