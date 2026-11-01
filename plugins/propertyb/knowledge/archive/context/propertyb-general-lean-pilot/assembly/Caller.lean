import Aris4Math.General.RS.PilotMain

namespace Aris4Math.General.RS
universe u

/-- Independent original-form pilot caller. -/
theorem bare_seventeen_caller (V : Type u) [Finite V] (E : Finset (Finset V))
    (hu : ∀ e ∈ E, e.card = 17) (hm : E.card ≤ 2 ^ 17) :
    ∃ c : V → Bool, ∀ e ∈ E,
      (∃ x ∈ e, c x = true) ∧ (∃ y ∈ e, c y = false) := by
  exact propertyB_seventeen_of_at_most_two_pow V E hu hm

end Aris4Math.General.RS

#print Aris4Math.General.RS.rsFailureProbability
#check Aris4Math.General.RS.rs_recoloring_failure_le
#check Aris4Math.General.RS.propertyB_of_rs_bound
#check Aris4Math.General.RS.propertyB_seventeen_of_at_most_two_pow
#print axioms Aris4Math.General.RS.rs_recoloring_failure_le
#print axioms Aris4Math.General.RS.propertyB_of_rs_bound
#print axioms Aris4Math.General.RS.bare_seventeen_caller
