import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows60Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows60Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected60 : rows60.map Row.selected=choices (candidates 60) ∅ := by decide +kernel
theorem checked60 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 60))
  (choices (candidates 60) ∅) witnesses60 := by
  rw [← selected60]
  apply checked_rows
  simp only [rows60,List.all_append,TwentyFiveUnit9Rows60Batch0.checked,TwentyFiveUnit9Rows60Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
