import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionData
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
set_option maxHeartbeats 0
set_option maxRecDepth 100000
example : ¬ TwentyThreeLowPromotionBase.Feasible (newCounts 7 [3,3,0,0,0,0,0]) := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
