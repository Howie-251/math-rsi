import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionCoverage0
import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionCoverage1
import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionCoverage2
import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionCoverage3
import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionCoverage4
import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionCoverage5
import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionCoverage6
import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionCoverage7
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 2000
theorem coverage (c : OldCase) (values : List ℕ) (mem : values∈catalogue c) : covered c values := by
  fin_cases c
  · exact coverage0 values mem
  · exact coverage1 values mem
  · exact coverage2 values mem
  · exact coverage3 values mem
  · exact coverage4 values mem
  · exact coverage5 values mem
  · exact coverage6 values mem
  · exact coverage7 values mem
end Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
