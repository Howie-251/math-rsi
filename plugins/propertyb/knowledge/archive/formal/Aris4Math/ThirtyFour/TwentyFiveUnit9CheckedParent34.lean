import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows34Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected34 : rows34.map Row.selected=choices (candidates 34) ∅ := by decide +kernel
theorem checked34 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 34))
  (choices (candidates 34) ∅) witnesses34 := by
  rw [← selected34]
  apply checked_rows
  simp only [rows34,List.all_append,TwentyFiveUnit9Rows34Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
