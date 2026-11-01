import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows14Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected14 : rows14.map Row.selected=choices (candidates 14) ∅ := by decide +kernel
theorem checked14 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 14))
  (choices (candidates 14) ∅) witnesses14 := by
  rw [← selected14]
  apply checked_rows
  simp only [rows14,List.all_append,TwentyFiveUnit9Rows14Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
