import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows20Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows20Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected20 : rows20.map Row.selected=choices (candidates 20) ∅ := by decide +kernel
theorem checked20 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 20))
  (choices (candidates 20) ∅) witnesses20 := by
  rw [← selected20]
  apply checked_rows
  simp only [rows20,List.all_append,TwentyFiveUnit9Rows20Batch0.checked,TwentyFiveUnit9Rows20Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
