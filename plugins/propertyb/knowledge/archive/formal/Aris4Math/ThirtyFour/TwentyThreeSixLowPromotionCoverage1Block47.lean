import Aris4Math.ThirtyFour.TwentyThreeSixLowPromotionData
namespace Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def rows1_47 : List (List ℕ × Reason) := [
([2,2,0,0,0,1,0,0,0,0,0,0,0], .zeroPair 3 5),
([2,2,0,0,0,1,0,0,0,1,0,0,0], .zeroPair 3 5),
([2,2,0,0,0,1,1,0,0,0,0,0,0], .zeroPair 4 5),
([2,2,0,0,1,0,0,0,0,0,0,0,0], .zeroPair 3 5),
([2,2,0,0,1,0,0,0,0,1,0,0,0], .zeroPair 3 5),
([2,2,0,0,1,0,1,0,0,0,0,0,0], .zeroPair 4 5),
([2,2,0,1,0,0,0,0,0,0,0,0,0], .zeroPair 3 5),
([2,2,0,1,0,0,0,0,0,0,0,1,0], .zeroPair 3 5),
([2,2,0,1,0,0,0,0,0,0,1,0,0], .zeroPair 3 5),
([2,2,0,1,0,0,0,0,0,1,0,0,0], .zeroPair 3 5),
([2,2,0,1,0,0,0,0,1,0,0,0,0], .zeroPair 4 5),
([2,2,0,1,0,0,0,1,0,0,0,0,0], .zeroPair 4 5),
([2,2,0,1,0,0,1,0,0,0,0,0,0], .zeroPair 4 5),
([2,2,0,1,0,1,0,0,0,0,0,0,0], .zeroPair 3 5),
([2,2,0,1,1,0,0,0,0,0,0,0,0], .zeroPair 3 5),
([2,2,0,2,0,0,0,0,0,0,0,0,0], .zeroPair 3 5),
([2,2,1,0,0,0,0,0,0,0,0,0,0], .zeroPair 2 5),
([2,2,1,0,0,0,0,0,0,1,0,0,0], .zeroPair 2 5),
([2,2,1,0,0,0,1,0,0,0,0,0,0], .zeroPair 2 5),
([2,2,1,1,0,0,0,0,0,0,0,0,0], .zeroPair 3 5)
]
theorem rows1_47_checked : rows1_47.all (fun row => decide (rowValid 1 row.1 row.2))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyThreeSixLowPromotion
