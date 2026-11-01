import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows46Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected46 : rows46.map Row.selected=choices (candidates 46) ∅ := by decide +kernel
theorem checked46 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 46))
  (choices (candidates 46) ∅) witnesses46 := by
  rw [← selected46]
  apply checked_rows
  simp only [rows46,List.all_append,TwentyFiveUnit9Rows46Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
