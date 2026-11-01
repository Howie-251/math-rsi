import Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotionData
namespace Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
set_option maxHeartbeats 0
set_option maxRecDepth 100000
example : ∀ T, newCounts 7 [1,1,0,1,1,0,0] (T.map (newPerm 28).toEmbedding)=μ 9 T := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeFiveLowPromotion
