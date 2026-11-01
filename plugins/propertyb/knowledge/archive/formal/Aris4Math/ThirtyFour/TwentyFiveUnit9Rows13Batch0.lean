import Aris4Math.ThirtyFour.TwentyFiveUnit9Data
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Rows13Batch0
open TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem checked : rows13_0.all (fun r => decide (Checks catalogue (TwentyFiveUnit8Data.catalogue 13) r.selected r.witness))=true := by decide +kernel
end Aris4Math.ThirtyFour.TwentyFiveUnit9Rows13Batch0
