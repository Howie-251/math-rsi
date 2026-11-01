import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRowsData
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows3Batch0
open TwentyFiveConditionalRows TwentyFiveNineLowTenthRowsData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows3_0.all (fun r => decide (QuickCheck (degrees 3) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 3) r))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows3Batch0
