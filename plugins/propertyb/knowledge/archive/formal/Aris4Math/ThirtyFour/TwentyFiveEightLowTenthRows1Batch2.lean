import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthRowsData
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowTenthRows1Batch2
open TwentyFiveConditionalBudgetRows TwentyFiveColoredActual TwentyFiveEightLowTenthRowsData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows1_2.all (fun r => decide (Check 8
    TwentyFiveEightLowTenthInventoryData.big (oldBig 1) r))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveEightLowTenthRows1Batch2
