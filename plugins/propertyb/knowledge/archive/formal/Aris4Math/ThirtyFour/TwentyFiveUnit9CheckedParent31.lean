import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows31Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected31 : rows31.map Row.selected=choices (candidates 31) ∅ := by decide +kernel
theorem checked31 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 31))
  (choices (candidates 31) ∅) witnesses31 := by
  rw [← selected31]
  apply checked_rows
  simp only [rows31,List.all_append,TwentyFiveUnit9Rows31Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
