import Aris4Math.ThirtyFour.TwentyFiveUnit8Data
namespace Aris4Math.ThirtyFour.TwentyFiveUnit8Rows14Batch0
open TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit8Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows14_0.all (fun r => decide (Checks catalogue (TwentyFiveUnit7Data.catalogue 14) r.selected r.witness))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveUnit8Rows14Batch0
