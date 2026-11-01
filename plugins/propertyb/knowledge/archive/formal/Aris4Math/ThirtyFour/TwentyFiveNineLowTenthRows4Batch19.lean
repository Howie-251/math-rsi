import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRowsData
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows4Batch19
open TwentyFiveConditionalRows TwentyFiveNineLowTenthRowsData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows4_19.all (fun r => decide (QuickCheck (degrees 4) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 4) r))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows4Batch19
