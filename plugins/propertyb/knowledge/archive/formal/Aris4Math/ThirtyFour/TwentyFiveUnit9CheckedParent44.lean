import Aris4Math.ThirtyFour.TwentyFiveUnit9Rows44Batch0
namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem selected44 : rows44.map Row.selected=choices (candidates 44) ∅ := by decide +kernel
theorem checked44 : List.Forall₂ (Checks catalogue (TwentyFiveUnit8Data.catalogue 44))
  (choices (candidates 44) ∅) witnesses44 := by
  rw [← selected44]
  apply checked_rows
  simp only [rows44,List.all_append,TwentyFiveUnit9Rows44Batch0.checked,Bool.true_and]
end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
