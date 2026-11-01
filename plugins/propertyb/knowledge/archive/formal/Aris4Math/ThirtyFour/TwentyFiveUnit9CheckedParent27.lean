import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows27Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected27 : rows27.map Row.selected=choices (candidates 27) ∅ := by decide +kernel
theorem checked27 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 27))
  (choices (candidates 27) ∅) witnesses27 := by
  rw [← selected27]
  apply checked_rows
  simp only [rows27,List.all_append,TwentyFiveUnit9Rows27Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
