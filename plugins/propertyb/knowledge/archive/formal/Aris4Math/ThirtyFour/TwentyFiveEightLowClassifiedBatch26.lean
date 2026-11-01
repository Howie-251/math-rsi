import Aris4Math.ThirtyFour.TwentyFiveEightLowClassifiedData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowClassifiedBatch26
open TwentyFiveColoredRows TwentyFiveEightLowClassifiedData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows26.all (fun r => decide (Check 8 TwentyFiveEightLowInventoryData.big r))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowClassifiedBatch26
