import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDualFacts
import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDualNumeric
namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDual
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyThreeLowUnitSixDualData TwentyThreeLowUnitSixDualFacts TwentyThreeLowUnitSixDualNumeric

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 23))
    (vertices : Fin 6 ↪ Fin 23) (c : Case)
    (actual : ∀ T, count H vertices T = counts c T) : PropertyB H := by
  have valid := profile_valid c
  rw [profiles_calculated,calculated_eq_profile] at valid
  have real := TwentyThreeHighSixProfiles.realizes_profile H vertices (positions c)
    (counts c) actual _ valid
  rw [← calculated_eq_profile,← profiles_calculated] at real
  apply RefinedDeletion.propertyB_of_refined_deletion H vertices (positions c) (p c) real
    (by rw [profiles_calculated,calculated_eq_profile]; rfl) (loss c)
    (avoid c) (alpha c) (quota c)
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
end Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDual
#print axioms Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDual.propertyB_of_counts
