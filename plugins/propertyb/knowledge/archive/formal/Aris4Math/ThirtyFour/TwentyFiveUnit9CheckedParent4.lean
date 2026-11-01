import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows4Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows4Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows4Batch2
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected4 : rows4.map Row.selected=choices (candidates 4) ∅ := by decide +kernel
theorem checked4 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 4))
  (choices (candidates 4) ∅) witnesses4 := by
  rw [← selected4]
  apply checked_rows
  simp only [rows4,List.all_append,TwentyFiveUnit9Rows4Batch0.checked,TwentyFiveUnit9Rows4Batch1.checked,TwentyFiveUnit9Rows4Batch2.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
