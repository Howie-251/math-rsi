import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCatalogData
namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitSixRecovery
open MultiLockRecovery TwentyThreeLowUnitSixCatalogData
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem recovery_formula : ∀ c : Case, ∀ T : Finset (Fin 6),
    recovered (low (extra c)) (high c) T = counts c T := by
  intro c
  fin_cases c <;> decide +kernel
end Aris4Math.ThirtyThree.TwentyThreeLowUnitSixRecovery
#print axioms Aris4Math.ThirtyThree.TwentyThreeLowUnitSixRecovery.recovery_formula
