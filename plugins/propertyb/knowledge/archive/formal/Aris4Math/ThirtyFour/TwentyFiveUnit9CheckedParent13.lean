import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows13Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected13 : rows13.map Row.selected=choices (candidates 13) ∅ := by decide +kernel
theorem checked13 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 13))
  (choices (candidates 13) ∅) witnesses13 := by
  rw [← selected13]
  apply checked_rows
  simp only [rows13,List.all_append,TwentyFiveUnit9Rows13Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
