import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows29Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected29 : rows29.map Row.selected=choices (candidates 29) ∅ := by decide +kernel
theorem checked29 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 29))
  (choices (candidates 29) ∅) witnesses29 := by
  rw [← selected29]
  apply checked_rows
  simp only [rows29,List.all_append,TwentyFiveUnit9Rows29Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
