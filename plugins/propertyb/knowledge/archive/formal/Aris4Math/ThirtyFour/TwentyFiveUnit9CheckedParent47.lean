import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows47Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected47 : rows47.map Row.selected=choices (candidates 47) ∅ := by decide +kernel
theorem checked47 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 47))
  (choices (candidates 47) ∅) witnesses47 := by
  rw [← selected47]
  apply checked_rows
  simp only [rows47,List.all_append,TwentyFiveUnit9Rows47Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
