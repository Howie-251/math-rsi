import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows59Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows59Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows59Batch2
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows59Batch3
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected59 : rows59.map Row.selected=choices (candidates 59) ∅ := by decide +kernel
theorem checked59 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 59))
  (choices (candidates 59) ∅) witnesses59 := by
  rw [← selected59]
  apply checked_rows
  simp only [rows59,List.all_append,TwentyFiveUnit9Rows59Batch0.checked,TwentyFiveUnit9Rows59Batch1.checked,TwentyFiveUnit9Rows59Batch2.checked,TwentyFiveUnit9Rows59Batch3.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
