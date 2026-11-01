import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows3Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected3 : rows3.map Row.selected=choices (candidates 3) ∅ := by decide +kernel
theorem checked3 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 3))
  (choices (candidates 3) ∅) witnesses3 := by
  rw [← selected3]
  apply checked_rows
  simp only [rows3,List.all_append,TwentyFiveUnit9Rows3Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
