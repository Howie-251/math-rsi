import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRowsData
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows0Batch1
open TwentyFiveConditionalRows TwentyFiveNineLowTenthRowsData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows0_1.all (fun r => decide (QuickCheck (degrees 0) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 0) r))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows0Batch1
