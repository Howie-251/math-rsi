import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows24Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected24 : rows24.map Row.selected=choices (candidates 24) ∅ := by decide +kernel
theorem checked24 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 24))
  (choices (candidates 24) ∅) witnesses24 := by
  rw [← selected24]
  apply checked_rows
  simp only [rows24,List.all_append,TwentyFiveUnit9Rows24Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
