import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows36Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected36 : rows36.map Row.selected=choices (candidates 36) ∅ := by decide +kernel
theorem checked36 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 36))
  (choices (candidates 36) ∅) witnesses36 := by
  rw [← selected36]
  apply checked_rows
  simp only [rows36,List.all_append,TwentyFiveUnit9Rows36Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
