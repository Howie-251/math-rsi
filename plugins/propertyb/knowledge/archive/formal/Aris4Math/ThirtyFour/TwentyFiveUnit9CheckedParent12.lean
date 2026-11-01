import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows12Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected12 : rows12.map Row.selected=choices (candidates 12) ∅ := by decide +kernel
theorem checked12 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 12))
  (choices (candidates 12) ∅) witnesses12 := by
  rw [← selected12]
  apply checked_rows
  simp only [rows12,List.all_append,TwentyFiveUnit9Rows12Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
