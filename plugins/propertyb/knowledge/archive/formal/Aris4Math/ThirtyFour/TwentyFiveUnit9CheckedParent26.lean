import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows26Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows26Batch1
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows26Batch2
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected26 : rows26.map Row.selected=choices (candidates 26) ∅ := by decide +kernel
theorem checked26 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 26))
  (choices (candidates 26) ∅) witnesses26 := by
  rw [← selected26]
  apply checked_rows
  simp only [rows26,List.all_append,TwentyFiveUnit9Rows26Batch0.checked,TwentyFiveUnit9Rows26Batch1.checked,TwentyFiveUnit9Rows26Batch2.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
