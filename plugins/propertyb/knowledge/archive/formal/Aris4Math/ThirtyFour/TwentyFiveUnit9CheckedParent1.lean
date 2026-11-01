import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows1Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected1 : rows1.map Row.selected=choices (candidates 1) ∅ := by decide +kernel
theorem checked1 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 1))
  (choices (candidates 1) ∅) witnesses1 := by
  rw [← selected1]
  apply checked_rows
  simp only [rows1,List.all_append,TwentyFiveUnit9Rows1Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
