import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows5Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected5 : rows5.map Row.selected=choices (candidates 5) ∅ := by decide +kernel
theorem checked5 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 5))
  (choices (candidates 5) ∅) witnesses5 := by
  rw [← selected5]
  apply checked_rows
  simp only [rows5,List.all_append,TwentyFiveUnit9Rows5Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
