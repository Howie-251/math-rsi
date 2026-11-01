import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows6Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected6 : rows6.map Row.selected=choices (candidates 6) ∅ := by decide +kernel
theorem checked6 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 6))
  (choices (candidates 6) ∅) witnesses6 := by
  rw [← selected6]
  apply checked_rows
  simp only [rows6,List.all_append,TwentyFiveUnit9Rows6Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
