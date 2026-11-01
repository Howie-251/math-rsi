import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows0Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows0Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows0Batch2
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows0Batch3
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows0Batch4
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows0Batch5
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected0 : rows0.map Row.selected=choices (candidates 0) ∅ := by decide +kernel
theorem checked0 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 0))
  (choices (candidates 0) ∅) witnesses0 := by
  rw [← selected0]
  apply checked_rows
  simp only [rows0,List.all_append,TwentyFiveUnit9Rows0Batch0.checked,TwentyFiveUnit9Rows0Batch1.checked,TwentyFiveUnit9Rows0Batch2.checked,TwentyFiveUnit9Rows0Batch3.checked,TwentyFiveUnit9Rows0Batch4.checked,TwentyFiveUnit9Rows0Batch5.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
