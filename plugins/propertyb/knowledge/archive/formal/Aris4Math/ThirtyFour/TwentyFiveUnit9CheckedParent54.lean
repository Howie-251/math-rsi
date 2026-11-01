import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows54Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected54 : rows54.map Row.selected=choices (candidates 54) ∅ := by decide +kernel
theorem checked54 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 54))
  (choices (candidates 54) ∅) witnesses54 := by
  rw [← selected54]
  apply checked_rows
  simp only [rows54,List.all_append,TwentyFiveUnit9Rows54Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
