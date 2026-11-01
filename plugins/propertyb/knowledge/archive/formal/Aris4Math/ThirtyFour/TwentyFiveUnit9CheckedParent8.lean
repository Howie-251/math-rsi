import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows8Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected8 : rows8.map Row.selected=choices (candidates 8) ∅ := by decide +kernel
theorem checked8 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 8))
  (choices (candidates 8) ∅) witnesses8 := by
  rw [← selected8]
  apply checked_rows
  simp only [rows8,List.all_append,TwentyFiveUnit9Rows8Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
