import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows10Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected10 : rows10.map Row.selected=choices (candidates 10) ∅ := by decide +kernel
theorem checked10 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 10))
  (choices (candidates 10) ∅) witnesses10 := by
  rw [← selected10]
  apply checked_rows
  simp only [rows10,List.all_append,TwentyFiveUnit9Rows10Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
