import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows49Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows49Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows49Batch2
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected49 : rows49.map Row.selected=choices (candidates 49) ∅ := by decide +kernel
theorem checked49 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 49))
  (choices (candidates 49) ∅) witnesses49 := by
  rw [← selected49]
  apply checked_rows
  simp only [rows49,List.all_append,TwentyFiveUnit9Rows49Batch0.checked,TwentyFiveUnit9Rows49Batch1.checked,TwentyFiveUnit9Rows49Batch2.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
