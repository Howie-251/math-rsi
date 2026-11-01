import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage0
import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionCoverage1
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 2000
theorem coverage (c : OldCase) (values : List ℕ) (mem : values∈catalogue c) : covered c values := by
  fin_cases c
  · exact coverage0 values mem
  · exact coverage1 values mem
end Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
