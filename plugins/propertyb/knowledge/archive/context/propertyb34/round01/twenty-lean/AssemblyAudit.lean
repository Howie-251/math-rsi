import Aris4Math.ThirtyFour.Assembly
namespace T34TwentyAssemblyAudit
universe u
theorem conditional_original
    (remaining : Aris4Math.ThirtyFour.Assembly.RemainingGoal)
    (V : Type u) [Finite V] (E : Finset (Finset V))
    (uniform : ∀ e ∈ E, e.card=5) (size : E.card ≤ 34) :
    ∃ c : V → Bool, ∀ e ∈ E,
      1 ≤ (e.filter fun x => c x=true).card ∧ (e.filter fun x => c x=true).card ≤ 4 := by
  classical
  letI : Fintype V := Fintype.ofFinite V
  exact (Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal.mpr remaining) V ⟨E,uniform⟩ size
end T34TwentyAssemblyAudit
#print Aris4Math.ThirtyFour.Assembly.RemainingGoal
#print axioms Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal
#print axioms T34TwentyAssemblyAudit.conditional_original
