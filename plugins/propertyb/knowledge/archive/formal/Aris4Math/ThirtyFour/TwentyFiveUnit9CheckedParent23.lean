import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows23Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected23 : rows23.map Row.selected=choices (candidates 23) ∅ := by decide +kernel
theorem checked23 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 23))
  (choices (candidates 23) ∅) witnesses23 := by
  rw [← selected23]
  apply checked_rows
  simp only [rows23,List.all_append,TwentyFiveUnit9Rows23Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
