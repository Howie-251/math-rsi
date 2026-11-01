import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows7Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows7Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected7 : rows7.map Row.selected=choices (candidates 7) ∅ := by decide +kernel
theorem checked7 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 7))
  (choices (candidates 7) ∅) witnesses7 := by
  rw [← selected7]
  apply checked_rows
  simp only [rows7,List.all_append,TwentyFiveUnit9Rows7Batch0.checked,TwentyFiveUnit9Rows7Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
