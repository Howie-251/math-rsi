import Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedCore
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
open scoped BigOperators
open TwentyThreeSixLowExtra7Joint16Data
open MixedLayoutApplication MixedLayoutCounts
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem penalty_3 : penalty support μ beta (weights positions p) 3 (R 3) (delta 3)=penaltyValue 3 := by
  simp only [LocalProfiles.weights_eq]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowExtra7Joint16CachedNumeric
