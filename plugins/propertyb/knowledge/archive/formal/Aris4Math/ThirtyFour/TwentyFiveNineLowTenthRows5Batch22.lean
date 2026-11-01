import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRowsData
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows5Batch22
open TwentyFiveConditionalRows TwentyFiveNineLowTenthRowsData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows5_22.all (fun r => decide (QuickCheck (degrees 5) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 5) r))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows5Batch22
