import Aris4Math.ThirtyThree.TwentyThreeLowBadHighNumeric

namespace Aris4Math.ThirtyThree.TwentyThreeLowBadHigh
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyThreeLowBadHighData TwentyThreeLowBadHighFacts TwentyThreeLowBadHighNumeric

theorem actual_profile (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 5 ↪ Fin 23) (c : Config)
    (actual : ∀ T, count H vertices T = counts c T) :
    RealizesProfile H vertices (positions c) (p c) 33 := by
  have valid := profile_valid c
  rw [profiles_calculated, calculated_eq_profile] at valid ⊢
  exact FiveProfiles.realizes_profile H vertices (positions c) (counts c) actual _ valid

/-- The only intermediate premise is the actual type multiplicity equality;
all finite dual inequalities and the final strict bound are supplied here. -/
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 5 ↪ Fin 23) (c : Config)
    (actual : ∀ T, count H vertices T = counts c T) : PropertyB H := by
  have real := actual_profile H vertices c actual
  apply RefinedDeletion.propertyB_of_refined_deletion H vertices (positions c) (p c) real
    (by rw [profiles_calculated, calculated_eq_profile]; rfl) (loss c)
    avoided (multipliers c) (quotas c)
  · intro j _
    exact (dual_exact c j).1
  · intro j _
    exact (dual_exact c j).2.1
  · intro j _
    exact (dual_exact c j).2.2.1
  · intro j _
    rw [loss_at]
    exact (dual_exact c j).2.2.2
  · exact loss_zeroOutside c
  · exact strict c

end Aris4Math.ThirtyThree.TwentyThreeLowBadHigh
#print axioms Aris4Math.ThirtyThree.TwentyThreeLowBadHigh.propertyB_of_counts
