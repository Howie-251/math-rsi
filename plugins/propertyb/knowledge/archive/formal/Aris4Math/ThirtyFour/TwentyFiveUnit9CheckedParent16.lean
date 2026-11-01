import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows16Batch0
import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows16Batch1
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected16 : rows16.map Row.selected=choices (candidates 16) ∅ := by decide +kernel
theorem checked16 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 16))
  (choices (candidates 16) ∅) witnesses16 := by
  rw [← selected16]
  apply checked_rows
  simp only [rows16,List.all_append,TwentyFiveUnit9Rows16Batch0.checked,TwentyFiveUnit9Rows16Batch1.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
