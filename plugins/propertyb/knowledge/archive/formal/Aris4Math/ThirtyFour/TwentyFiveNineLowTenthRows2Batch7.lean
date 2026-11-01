import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRowsData
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows2Batch7
open TwentyFiveConditionalRows TwentyFiveNineLowTenthRowsData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows2_7.all (fun r => decide (QuickCheck (degrees 2) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 2) r))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows2Batch7
