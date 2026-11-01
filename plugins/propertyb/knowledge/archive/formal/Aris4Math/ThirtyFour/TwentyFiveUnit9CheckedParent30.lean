import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows30Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected30 : rows30.map Row.selected=choices (candidates 30) ∅ := by decide +kernel
theorem checked30 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 30))
  (choices (candidates 30) ∅) witnesses30 := by
  rw [← selected30]
  apply checked_rows
  simp only [rows30,List.all_append,TwentyFiveUnit9Rows30Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
