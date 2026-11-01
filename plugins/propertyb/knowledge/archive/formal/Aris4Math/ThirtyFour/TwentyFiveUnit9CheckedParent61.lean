import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows61Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected61 : rows61.map Row.selected=choices (candidates 61) ∅ := by decide +kernel
theorem checked61 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 61))
  (choices (candidates 61) ∅) witnesses61 := by
  rw [← selected61]
  apply checked_rows
  simp only [rows61,List.all_append,TwentyFiveUnit9Rows61Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
