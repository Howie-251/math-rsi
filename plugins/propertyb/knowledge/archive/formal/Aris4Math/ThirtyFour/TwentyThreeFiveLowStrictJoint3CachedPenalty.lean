import Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
open scoped BigOperators
open TwentyThreeFiveLowStrictJoint3Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem penalty_0 : penalty support μ beta (weights positions p) 0 (R 0) (delta 0) = 0 := by
  simp only [LocalProfiles.weights_eq]
  decide +kernel

theorem penalty_1 : penalty support μ beta (weights positions p) 1 (R 1) (delta 1) = 0 := by
  simp only [LocalProfiles.weights_eq]
  decide +kernel

theorem penalty_2 : penalty support μ beta (weights positions p) 2 (R 2) (delta 2) = 0 := by
  simp only [LocalProfiles.weights_eq]
  decide +kernel

theorem penalty_3 : penalty support μ beta (weights positions p) 3 (R 3) (delta 3) = 0 := by
  simp only [LocalProfiles.weights_eq]
  decide +kernel

theorem penalty_4 : penalty support μ beta (weights positions p) 4 (R 4) (delta 4) = 0 := by
  simp only [LocalProfiles.weights_eq]
  decide +kernel

theorem penalty_zero (j : Fin 5) : penalty support μ beta (weights positions p) j (R j) (delta j) = 0 := by
  fin_cases j
  · exact penalty_0
  · exact penalty_1
  · exact penalty_2
  · exact penalty_3
  · exact penalty_4
end Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric
#print axioms Aris4Math.ThirtyFour.TwentyThreeFiveLowStrictJoint3CachedNumeric.penalty_zero
