import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows25Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected25 : rows25.map Row.selected=choices (candidates 25) ∅ := by decide +kernel
theorem checked25 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 25))
  (choices (candidates 25) ∅) witnesses25 := by
  rw [← selected25]
  apply checked_rows
  simp only [rows25,List.all_append,TwentyFiveUnit9Rows25Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
