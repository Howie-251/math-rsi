import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows39Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected39 : rows39.map Row.selected=choices (candidates 39) ∅ := by decide +kernel
theorem checked39 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 39))
  (choices (candidates 39) ∅) witnesses39 := by
  rw [← selected39]
  apply checked_rows
  simp only [rows39,List.all_append,TwentyFiveUnit9Rows39Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
