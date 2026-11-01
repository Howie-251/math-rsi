import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows51Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected51 : rows51.map Row.selected=choices (candidates 51) ∅ := by decide +kernel
theorem checked51 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 51))
  (choices (candidates 51) ∅) witnesses51 := by
  rw [← selected51]
  apply checked_rows
  simp only [rows51,List.all_append,TwentyFiveUnit9Rows51Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
